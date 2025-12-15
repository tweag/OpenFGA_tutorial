"""
Solution for Exercise 2: List Accessible Documents
"""
from typing import List
from openfga_sdk import OpenFgaClient
from openfga_sdk.client.models import ClientListObjectsRequest


async def list_documents_for_user(client: OpenFgaClient, user: str, relation: str = "reader") -> List[str]:
    """
    List all documents a user has a specific relation to asynchronously.
    
    Args:
        client: OpenFgaClient instance
        user: The user to check
        relation: The relation to check (default is "reader")
        
    Returns:
        List of document IDs the user has the specified relation to
    """
    body = ClientListObjectsRequest(
        user=f"user:{user}",
        relation=relation,
        type="document",
    )
    
    response = await client.list_objects(body)
    
    # Extract document IDs from the response
    # The response contains objects in the format "document:1", "document:2", etc.
    # We need to extract just the ID part
    document_ids = [obj.split(":", 1)[1] for obj in response.objects]
    
    return document_ids
