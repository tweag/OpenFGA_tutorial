"""
Test script for Exercise 3: Who Can Access a Document

This script tests the list_users_for_document and get_document_access_report functions
from the Exercise 3 solution.
"""
import os
import asyncio
from openfga_sdk import OpenFgaClient, ClientConfiguration

# Import the user listing functions from the Exercise 3 solution
from fga_example.fga_client import list_users_for_document

async def test_list_users_for_document():
    """Test listing users who can access specific documents."""
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
        # Define the documents to test
        documents = ["1", "2", "6"]
        relations = ["reader", "writer", "owner"]
        
        # Test each document and relation combination
        for document_id in documents:
            print(f"\n=== Access report for document:{document_id} ===")
            
            for relation in relations:
                users = await list_users_for_document(client, document_id, relation)
                if users:
                    print(f"Users who can {relation} document:{document_id}: {', '.join(users)}")
                else:
                    print(f"No users can {relation} document:{document_id}")
        
        # Generate a comprehensive report for document:1
        print("\n=== Comprehensive access report for document:1 ===")
        doc_id = "1"
        
        # Import the report function from the Exercise 3 solution
        from exercises.solutions.exercise3 import get_document_access_report
        
        access_report = await get_document_access_report(client, doc_id)
        
        print(f"Readers: {', '.join(access_report['readers']) if access_report['readers'] else 'None'}")
        print(f"Writers: {', '.join(access_report['writers']) if access_report['writers'] else 'None'}")
        print(f"Owners: {', '.join(access_report['owners']) if access_report['owners'] else 'None'}")
        
        # Bonus: Find users who have multiple access types
        readers_set = set(access_report['readers'])
        writers_set = set(access_report['writers'])
        owners_set = set(access_report['owners'])
        
        read_write = readers_set.intersection(writers_set)
        if read_write:
            print(f"\nUsers with both read and write access: {', '.join(read_write)}")
        
        all_access = readers_set.intersection(writers_set).intersection(owners_set)
        if all_access:
            print(f"Users with full access (read, write, owner): {', '.join(all_access)}")
    
    finally:
        # Close the client session
        await client.close()

if __name__ == "__main__":
    asyncio.run(test_list_users_for_document())