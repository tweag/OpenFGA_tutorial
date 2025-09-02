import sqlite3
import os
import csv
from typing import List, Optional
import pathlib
from datetime import datetime
from pydantic import BaseModel, Field

class Document(BaseModel):
    """Pydantic model for a document."""
    id: int
    title: str
    data: str
    created_at: str
    is_published: bool

class Folder(BaseModel):
    """Pydantic model for a folder."""
    id: int
    title: str
    description: str
    created_at: str

class User(BaseModel):
    """Pydantic model for a user."""
    id: str
    name: str
    surname: str
    email: str

# Create a SQLite database for documents, folders and users
def create_tables(conn: sqlite3.Connection):
    cursor = conn.cursor()
    
    # Create documents table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        data TEXT NOT NULL,
        created_at TEXT NOT NULL,
        is_published BOOLEAN NOT NULL
    )
    ''')
    
    # Create folders table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS folders (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    ''')
    
    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')
    
    conn.commit()

def populate_tables(conn: sqlite3.Connection):
    cursor = conn.cursor()
    
    # Populate documents table from CSV
    csv_path = pathlib.Path(__file__).parent.parent / 'data' / 'documents.csv'
    document_records_insert = "INSERT INTO documents (id, title, data, created_at, is_published) VALUES (?, ?, ?, ?, ?)" 
    
    if os.path.exists(csv_path):
        with open(csv_path, 'r') as f:
            documents_reader = csv.DictReader(f)
            cursor.executemany(document_records_insert, documents_reader)

    conn.commit() 

class DocumentService:
    """Service for accessing document data using SQLite."""
    
    def __init__(self, db_path: str = ':memory:'):
        """
        Initialize the document service with a SQLite database.
        
        Args:
            db_path: Path to SQLite database file. Defaults to in-memory database.
        """
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self._initialize_db()
    
    def _initialize_db(self) -> None:
        """Initialize the database with documents table and load data from CSV."""
        create_tables(self.conn)
        # Populate tables if empty  
        populate_tables(self.conn)
        
    
    def get_document_by_id(self, document_id: int) -> Optional[Document]:
        """
        Get a document by its ID.
        
        Args:
            document_id: The ID of the document to retrieve
            
        Returns:
            The document as a Document model, or None if not found
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM documents WHERE id = ?", (document_id,))
        result = cursor.fetchone()
        
        if result:
            return Document(**dict(result))
        return None
    
    def search_documents(self, search_term: str) -> List[Document]:
        """
        Search for documents containing the given term in title or data.
        
        Args:
            search_term: The term to search for
            
        Returns:
            A list of matching documents as Document models
        """
        cursor = self.conn.cursor()
        search_pattern = f"%{search_term}%"
        
        cursor.execute(
            "SELECT * FROM documents WHERE title LIKE ? OR data LIKE ?",
            (search_pattern, search_pattern)
        )
        
        results = cursor.fetchall()
        return [Document(**dict(row)) for row in results]
    
    def close(self) -> None:
        """Close the database connection."""
        if self.conn:
            self.conn.close()

