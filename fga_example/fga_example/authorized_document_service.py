"""
Authorized Document Service integrating OpenFGA authorization.

This module extends the document service with OpenFGA authorization checks.
It ensures that users can only access documents they have permission to read.
"""

import os
import asyncio
from typing import List, Dict, Any, Optional

from openfga_sdk import OpenFgaClient, ClientConfiguration
from openfga_sdk.client import ClientCheckRequest
from openfga_sdk.client.models import ClientBatchCheckItem, ClientBatchCheckRequest

from fga_example.document_service import DocumentService


class AuthorizationError(Exception):
    """Exception raised when a user does not have permission to access a resource."""
    pass


class AuthorizedDocumentService:
    """Document service with OpenFGA authorization checks."""
    
    def __init__(self, user_id: str, db_path: str = ':memory:'):
        """
        Initialize the authorized document service.
        
        Args:
            user_id: The ID of the user making the request (without the 'user:' prefix)
            db_path: Path to SQLite database file. Defaults to in-memory database.
        """
        self.user_id = user_id
        self.document_service = DocumentService(db_path)
        self.fga_client = None
    
    async def initialize_fga_client(self) -> None:
        """Initialize the OpenFGA client from environment variables."""
        api_url = os.environ.get("OPENFGA_API_URL", "http://localhost:8080")
        store_id = os.environ.get("FGA_STORE_ID")
        auth_model_id = os.environ.get("FGA_MODEL_ID")
        
        if not store_id:
            raise ValueError("FGA_STORE_ID environment variable not set")
        
        # Initialize OpenFGA client
        self.fga_client = OpenFgaClient(ClientConfiguration(
            api_url=api_url,
            store_id=store_id,
            authorization_model_id=auth_model_id
        ))
    
    async def check_access(self, relation: str, object_id: str) -> bool:
        """
        Check if the user has a specific relation to an object.
        
        Args:
            relation: The relation to check (e.g., "reader")
            object_id: The object to check against (e.g., "document:1")
            
        Returns:
            True if access is allowed, False otherwise
        """
        if not self.fga_client:
            await self.initialize_fga_client()
            
        body = ClientCheckRequest(
            user=f"user:{self.user_id}",
            relation=relation,
            object=object_id,
        )

        response = await self.fga_client.check(body)
        return response.allowed
    
    async def batch_check_access(self, relation: str, object_ids: List[str]) -> Dict[str, bool]:
        """
        Perform batch access checks.
        
        Args:
            relation: The relation to check
            object_ids: List of object IDs to check access for
            
        Returns:
            Dictionary mapping object IDs to access results (True/False)
        """
        if not self.fga_client:
            await self.initialize_fga_client()
            
        formatted_checks = [
            ClientBatchCheckItem(
                user=f"user:{self.user_id}",
                relation=relation,
                object=obj_id
            ) for obj_id in object_ids
        ]
        
        response = await self.fga_client.batch_check(ClientBatchCheckRequest(checks=formatted_checks))
        
        # Create a dictionary mapping object IDs to access results
        results = {}
        for i, check_result in enumerate(response.results):
            object_id = object_ids[i]
            results[object_id] = check_result.allowed
            
        return results
    
    async def get_document_by_id(self, document_id: int) -> Dict[str, Any]:
        """
        Get a document by its ID with authorization check.
        
        Args:
            document_id: The ID of the document to retrieve
            
        Returns:
            The document as a dictionary
            
        Raises:
            AuthorizationError: If the user does not have permission to read the document
            ValueError: If the document does not exist
        """
        # First check if the document exists
        document = self.document_service.get_document_by_id(document_id)
        if not document:
            raise ValueError(f"Document with ID {document_id} not found")
        
        # Check if the user has permission to read this document
        has_access = await self.check_access("reader", f"document:{document_id}")
        
        if not has_access:
            raise AuthorizationError(
                f"User {self.user_id} does not have permission to read document:{document_id}"
            )
        
        return document
    
    async def search_documents(self, search_term: str) -> List[Dict[str, Any]]:
        """
        Search for documents with authorization filtering.
        
        Args:
            search_term: The term to search for
            
        Returns:
            A list of documents the user has permission to read
        """
        # First get all matching documents without filtering
        all_results = self.document_service.search_documents(search_term)
        
        if not all_results:
            return []
        
        # Create a list of document IDs to check
        document_ids = [f"document:{doc['id']}" for doc in all_results]
        
        # Batch check access for all documents
        access_results = await self.batch_check_access("reader", document_ids)
        
        # Filter results to only include documents the user can read
        authorized_results = []
        for doc in all_results:
            doc_id = f"document:{doc['id']}"
            if access_results.get(doc_id, False):
                authorized_results.append(doc)
        
        return authorized_results
    
    def close(self) -> None:
        """Close connections."""
        self.document_service.close()
        if self.fga_client:
            asyncio.create_task(self.fga_client.close())

