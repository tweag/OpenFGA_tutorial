import sqlite3
import os
import csv
from typing import List, Dict, Any, Optional
import pathlib

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
        self.conn.row_factory = sqlite3.Row
        self._initialize_db()
    
    def _initialize_db(self) -> None:
        """Initialize the database with documents table and load data from CSV."""
        cursor = self.conn.cursor()
        
        # Create documents table if it doesn't exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            data TEXT NOT NULL,
            created_at TEXT NOT NULL,
            is_published BOOLEAN NOT NULL
        )
        ''')
        
        # Check if we need to load data
        cursor.execute("SELECT COUNT(*) FROM documents")
        count = cursor.fetchone()[0]
        
        if count == 0:
            # Load data from CSV
            csv_path = pathlib.Path(__file__).parent.parent / 'data' / 'documents.csv'
            
            if os.path.exists(csv_path):
                with open(csv_path, 'r') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        cursor.execute(
                            "INSERT INTO documents (id, title, data, created_at, is_published) VALUES (?, ?, ?, ?, ?)",
                            (
                                row['id'], 
                                row['title'], 
                                row['data'], 
                                row['created_at'],
                                row['is_published'].lower() == 'true'
                            )
                        )
        
        self.conn.commit()
    
    def get_document_by_id(self, document_id: int) -> Optional[Dict[str, Any]]:
        """
        Get a document by its ID.
        
        Args:
            document_id: The ID of the document to retrieve
            
        Returns:
            The document as a dictionary, or None if not found
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM documents WHERE id = ?", (document_id,))
        result = cursor.fetchone()
        
        if result:
            return dict(result)
        return None
    
    def search_documents(self, search_term: str) -> List[Dict[str, Any]]:
        """
        Search for documents containing the given term in title or data.
        
        Args:
            search_term: The term to search for
            
        Returns:
            A list of matching documents as dictionaries
        """
        cursor = self.conn.cursor()
        search_pattern = f"%{search_term}%"
        
        cursor.execute(
            "SELECT * FROM documents WHERE title LIKE ? OR data LIKE ?",
            (search_pattern, search_pattern)
        )
        
        results = cursor.fetchall()
        return [dict(row) for row in results]
    
    def close(self) -> None:
        """Close the database connection."""
        if self.conn:
            self.conn.close()

# Convenience functions that use the DocumentService class

def get_document_by_id(document_id: int) -> Optional[Dict[str, Any]]:
    """
    Get a document by its ID.
    
    Args:
        document_id: The ID of the document to retrieve
        
    Returns:
        The document as a dictionary, or None if not found
    """
    service = DocumentService()
    try:
        return service.get_document_by_id(document_id)
    finally:
        service.close()

def search_documents(search_term: str) -> List[Dict[str, Any]]:
    """
    Search for documents containing the given term in title or data.
    
    Args:
        search_term: The term to search for
        
    Returns:
        A list of matching documents as dictionaries
    """
    service = DocumentService()
    try:
        return service.search_documents(search_term)
    finally:
        service.close()