#!/usr/bin/env python3
"""
Example script demonstrating how to use the authorized_document_service module
to retrieve and search for documents with OpenFGA authorization.
"""

import asyncio
import sys

from fga_example.authorized_document_service import (
    get_document_by_id, 
    search_documents,
    AuthorizationError
)


async def main():
    """Run the demonstration of the authorized document service."""
    # List of users to test
    users = ["anne_smith", "bob_jones", "david_rodriguez", "emily_patel"]
    
    print("=== Authorized Document Access Demo ===")
    
    # Test getting document by ID for different users
    print("\n1. Testing document retrieval for multiple users:")
    for user in users:
        print(f"\nUser: {user}")
        for doc_id in range(1, 5):
            try:
                document = await get_document_by_id(user, doc_id)
                print(f"  - Document {doc_id}: ✅ Access granted - '{document['title']}'")
            except AuthorizationError as e:
                print(f"  - Document {doc_id}: ❌ Access denied - {str(e)}")
            except ValueError as e:
                print(f"  - Document {doc_id}: ⚠️ Error - {str(e)}")
    
    # Test searching documents for different users
    print("\n2. Testing document search for multiple users:")
    search_term = "Behavioral"
    for user in users:
        try:
            results = await search_documents(user, search_term)
            print(f"\nUser '{user}' searching for '{search_term}':")
            if results:
                for doc in results:
                    print(f"  - Found document {doc['id']}: '{doc['title']}'")
            else:
                print(f"  - No accessible documents found containing '{search_term}'")
        except Exception as e:
            print(f"  - Error during search: {str(e)}")

    print("\nDemo completed! Note how the results differ based on user permissions.")


if __name__ == "__main__":
    # Check that environment variables are set
    import os
    if not os.environ.get("FGA_STORE_ID") or not os.environ.get("FGA_MODEL_ID"):
        print("Error: FGA_STORE_ID and FGA_MODEL_ID environment variables must be set.")
        print("Make sure to run fga-setup first and add the store ID to your .env file.")
        sys.exit(1)
        
    asyncio.run(main())