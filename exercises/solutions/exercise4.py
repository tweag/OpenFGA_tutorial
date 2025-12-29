import os
from typing import List, Optional

from openfga_sdk import ClientConfiguration, OpenFgaClient
from fga_example.fga_example.document_service import (
    Document,
    DocumentService,
    require_authorization,
)
from fga_example.fga_example.fga_client_backup import batch_check_access


class AuthorizedDocumentService(DocumentService):
    """Document service with OpenFGA authorization checks."""

    def __init__(self, user_id: str, db_path: str = ":memory:"):
        """
        Initialize the document service with a SQLite database.

        Args:
            db_path: Path to SQLite database file. Defaults to in-memory database.
            user_id: The ID of the user making requests
        """
        super().__init__(db_path)
        self.fga_client = None
        self.user_id = user_id

    async def initialize_fga_client(self) -> None:
        """Initialize the OpenFGA client from environment variables."""
        api_url = os.environ.get("OPENFGA_API_URL", "http://localhost:8080")
        store_id = os.environ.get("FGA_STORE_ID")
        auth_model_id = os.environ.get("FGA_MODEL_ID")

        if not store_id:
            raise ValueError("FGA_STORE_ID environment variable not set")

        # Initialize OpenFGA client
        self.fga_client = OpenFgaClient(
            ClientConfiguration(
                api_url=api_url, store_id=store_id, authorization_model_id=auth_model_id
            )
        )

    @require_authorization(relation="read", object_type="document")
    async def get_document_by_id(self, document_id: int) -> Optional[Document]:
        """
        Get a document by its ID.

        Args:
            document_id: The ID of the document to retrieve

        Returns:
            The document as a Document model, or None if not found
        """
        return super().get_document_by_id(document_id)

    async def search_documents(self, search_term: str) -> List[Document]:
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
            (search_pattern, search_pattern),
        )

        results = cursor.fetchall()

        checks = [
            {
                "user": f"user:{self.user_id}",
                "relation": "read",
                "object": f"document:{row['id']}",
            }
            for row in results
        ]

        batch_results = await batch_check_access(self.fga_client, checks)
        allowed_document_ids = {
            int(result.request.object.split(":")[1])
            for result in batch_results
            if result.allowed
        }

        return [
            Document(**dict(row))
            for row in results
            if row["id"] in allowed_document_ids
        ]

    def close(self) -> None:
        """Close the database connection."""
        if self.conn:
            self.conn.close()
