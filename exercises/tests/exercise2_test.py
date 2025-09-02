"""
Test script for Exercise 2: List Accessible Documents

This script tests the list_documents_for_user and compare_access_speed functions
from the Exercise 2 solution.
"""
import os
import asyncio
from openfga_sdk import OpenFgaClient, ClientConfiguration

# Import the list_documents_for_user function from the solution file
from fga_example.fga_client import list_documents_for_user

async def compare_access_speed(client: OpenFgaClient, user: str):
    """
    Compare the speed of list-objects and multiple check operations.
    
    Args:
        client: OpenFgaClient instance
        user: The user to check
        
    Returns:
        Dictionary with timing results and found documents
    """
    import time
    import asyncio
    from openfga_sdk.client import ClientCheckRequest
    
    # Method 1: Use list-objects
    start_time = time.time()
    documents_list_objects = await list_documents_for_user(client, user, "reader")
    list_objects_time = time.time() - start_time
    
    # Method 2: Use multiple check operations
    # First, we need to get all document IDs (in a real application, you might get these from a database)
    all_document_ids = ["1", "2", "3", "4", "5", "6"]  # For this example, we know we have 6 documents
    
    start_time = time.time()
    check_results = []
    for doc_id in all_document_ids:
        body = ClientCheckRequest(
            user=f"user:{user}",
            relation="reader",
            object=f"document:{doc_id}",
        )
        response = await client.check(body)
        if response.allowed:
            check_results.append(doc_id)
    check_time = time.time() - start_time
    
    return {
        "list_objects_time": list_objects_time,
        "check_time": check_time,
        "list_objects_documents": documents_list_objects,
        "check_documents": check_results,
        "documents_match": set(documents_list_objects) == set(check_results)
    }

async def test_list_documents():
    """Test listing documents accessible to different users and comparing access methods."""
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
        # Define users to test
        users = ["anne_smith", "bob_jones", "clara_zhang", "david_rodriguez", "emily_patel"]
        
        print("=== Documents Users Can Read ===")
        for user in users:
            readable_docs = await list_documents_for_user(client, user, "reader")
            print(f"{user} can read documents: {', '.join(readable_docs) if readable_docs else 'None'}")
        
        print("\n=== Documents Users Can Write ===")
        for user in users:
            writable_docs = await list_documents_for_user(client, user, "writer")
            print(f"{user} can write to documents: {', '.join(writable_docs) if writable_docs else 'None'}")
            
        # Compare access methods for one user
        print("\n=== Performance Comparison ===")
        user_to_compare = "anne_smith"
        comparison = await compare_access_speed(client, user_to_compare)
        
        print(f"User: {user_to_compare}")
        print(f"List Objects method took: {comparison['list_objects_time']:.6f} seconds")
        print(f"Check method took: {comparison['check_time']:.6f} seconds")
        print(f"Speed difference: {comparison['check_time'] / comparison['list_objects_time']:.2f}x slower")
        print(f"Documents found by List Objects: {comparison['list_objects_documents']}")
        print(f"Documents found by Check: {comparison['check_documents']}")
        print(f"Results match: {'Yes' if comparison['documents_match'] else 'No'}")
    
    finally:
        # Close the client session
        await client.close()

if __name__ == "__main__":
    asyncio.run(test_list_documents())