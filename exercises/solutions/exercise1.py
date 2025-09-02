"""
Solution for Exercise 1: Basic Check Access
"""
from typing import List
from openfga_sdk import (
    OpenFgaClient,
)
from openfga_sdk.client import ClientCheckRequest

from openfga_sdk.client.models import (
  ClientBatchCheckItem,
  ClientBatchCheckRequest,
)

async def check_access(client: OpenFgaClient, user: str, relation: str, object: str) -> bool:
    """
    Check if a user has a specific relation to an object.
    
    Args:
        client: OpenFgaClient instance
        user: The user to check
        relation: The relation to check (e.g., "viewer", "editor")
        object: The object to check against (e.g., "document:1")
    """
    body = ClientCheckRequest(
        user=f"user:{user}",
        relation=relation,
        object=object,
    )

    response = await client.check(body)
    return response.allowed

async def batch_check_access(client: OpenFgaClient, checks: List[dict]) -> List[dict]:
    """
    Perform batch access checks asynchronously.
    
    Args:
        client: OpenFgaClient instance
        checks: List of dicts with user, relation, object keys
        
    Returns:
        List of booleans indicating access results
    """
    formatted_checks = [ClientBatchCheckItem(
        user=f"user:{check['user']}",
        relation=check['relation'],
        object=check['object']) for check in checks]
    response = await client.batch_check(ClientBatchCheckRequest(checks=formatted_checks))
    return response.result