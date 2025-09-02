"""
Solution for Exercise 3: Who Can Access a Document
"""
from typing import List, Dict
from openfga_sdk import OpenFgaClient
from openfga_sdk.client.models import ClientListUsersRequest
from openfga_sdk.models.fga_object import FgaObject
from openfga_sdk.client.models.list_users_request import ClientListUsersRequest
from openfga_sdk.models.user_type_filter import UserTypeFilter

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
    document_object = FgaObject(type="document", id=document_id)
    
    # Use list_users to get all users who have the specified relation to the document
    response = await client.list_users(
        ClientListUsersRequest(
            object=document_object,
            relation=relation,
            user_filters=[UserTypeFilter(type="user")]
        )
    )
    # Extract just the user IDs from the user objects (remove the "user:" prefix)
    user_ids = [user.object.id for user in response.users]
    
    return user_ids