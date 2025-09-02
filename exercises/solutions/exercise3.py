"""
Solution for Exercise 3: Who Can Access a Document
"""
from typing import List, Dict
from openfga_sdk import OpenFgaClient
from openfga_sdk.client.models import ClientListUsersRequest

async def list_users_for_document(client: OpenFgaClient, document_id: str, relation: str = "reader") -> List[str]:
    """
    List all users who have a specific relation to a document asynchronously.
    
    Args:
        client: OpenFgaClient instance
        document_id: The document ID to check
        relation: The relation to check (default is "reader")
        
    Returns:
        List of user IDs who have the specified relation to the document
    """
    document_object = f"document:{document_id}"
    
    # Use list_users to get all users who have the specified relation to the document
    response = await client.list_users(
        ClientListUsersRequest(
            object=document_object,
            relation=relation,
            user_type="user"
        )
    )
    
    # Extract just the user IDs from the user objects (remove the "user:" prefix)
    user_ids = []
    
    for user in response.users:
        # The user strings will be in format "user:username"
        if user.startswith("user:"):
            user_ids.append(user[5:])
    
    return user_ids

async def get_document_access_report(client: OpenFgaClient, document_id: str) -> Dict[str, List[str]]:
    """
    Generate a comprehensive access report for a document.
    
    Args:
        client: OpenFgaClient instance
        document_id: The document ID to check
        
    Returns:
        Dictionary with keys for different access types and values as lists of users
    """
    # Get readers, writers, and owners
    readers = await list_users_for_document(client, document_id, "reader")
    writers = await list_users_for_document(client, document_id, "writer")
    owners = await list_users_for_document(client, document_id, "owner")
    
    # Create a comprehensive report
    return {
        "readers": readers,
        "writers": writers,
        "owners": owners
    }