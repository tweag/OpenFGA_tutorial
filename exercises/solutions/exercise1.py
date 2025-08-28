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
# Client function for checking access


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

# Check_access.py content
# Check the following access scenarios:
# - Can anne_smith read document:1?
# - Can bob_jones read document:2?
# - Can david_rodriguez read document:3?
# - Can emily_patel read document:4?
async def main():
    """Check access for specific user and document combinations."""
    import os
    from openfga_sdk import ClientConfiguration
    
    # Get API URL and store ID from environment variables
    api_url = os.environ.get("OPENFGA_API_URL", "http://localhost:8080")
    store_id = os.environ.get("FGA_STORE_ID")
    auth_model_id = os.environ.get("FGA_MODEL_ID")
    
    if not store_id:
        print("Error: FGA_STORE_ID environment variable not set.")
        print("Make sure to run fga-setup first and add the store ID to your .env file.")
        return
    
    # Initialize OpenFGA client
    client = OpenFgaClient(ClientConfiguration(
        api_url=api_url,
        store_id=store_id,
        authorization_model_id=auth_model_id
    ))
    
    try:
        # Define the access checks to perform
        checks = [
            {"user": "anne_smith", "relation": "reader", "object": "document:1"},
            {"user": "bob_jones", "relation": "reader", "object": "document:2"},
            {"user": "david_rodriguez", "relation": "reader", "object": "document:3"},
            {"user": "emily_patel", "relation": "reader", "object": "document:4"}
        ]
        
        print("=== Individual Access Checks ===")
        for check in checks:
            result = await check_access(client, check["user"], check["relation"], check["object"])
            print(f"Can {check['user']} {check['relation']} {check['object']}? {'Yes' if result else 'No'}")
            
        print("\n=== Batch Access Check ===")
        batch_results = await batch_check_access(client, checks)
        
        for check in batch_results:
            print(f"Can {check.request.user} {check.request.relation} {check.request.object}? {'Yes' if check.allowed else 'No'}")
    
    finally:
        # Close the client session
        await client.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())