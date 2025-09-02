"""
Test script for Exercise 1: Basic Check Access

This script tests the check_access and batch_check_access functions
from the Exercise 1 solution.
"""
import os
import asyncio
from openfga_sdk import OpenFgaClient, ClientConfiguration

# Import the check_access functions from the fga_example package
from fga_example.fga_client import check_access, batch_check_access

async def test_check_access():
    """Test individual and batch access checks for specific user and document combinations."""
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
    asyncio.run(test_check_access())