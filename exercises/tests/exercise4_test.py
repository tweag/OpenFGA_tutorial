#!/usr/bin/env python3
"""
Example script demonstrating how to use the document_service module
to retrieve and search for documents.
"""

from fga_example.document_service import (
    DocumentService,
    AuthorizedDocumentService,
    AuthorizationError,
)
import asyncio


async def document_service_test():
    app = DocumentService()
    # Example 1: Get a document by its ID
    doc_id = 2
    document = await app.get_document_by_id(doc_id)
    if document:
        print(f"\nDocument with ID {doc_id}:")
        print(f"Title: {document.title}")
        print(f"Data: {document.data}")
        print(f"Created at: {document.created_at}")
        print(f"Published: {document.is_published}")
    else:
        print(f"No document found with ID {doc_id}")

    # Example 2: Search for documents containing a term
    search_term = "Behavioral"
    results = await app.search_documents(search_term)

    print(f"\nSearch results for '{search_term}':")
    if results:
        for doc in results:
            print(f"- {doc.id}: {doc.title}")
    else:
        print("No matching documents found")
    await app.close()


async def authorized_document_service_test():
    """Run the demonstration of the authorized document service."""
    # List of users to test
    users = ["anne_smith", "bob_jones", "david_rodriguez", "emily_patel"]

    print("=== Authorized Document Access Demo ===")

    # Test getting document by ID for different users
    print("\n1. Testing document retrieval for multiple users:")
    for user in users:
        app = await AuthorizedDocumentService.create(user_id=user)
        print(f"\nUser: {user}")
        for doc_id in range(1, 5):
            try:
                document = await app.get_document_by_id(doc_id)
                print(f"  - Document {doc_id}: ✅ Access granted - '{document.title}'")
            except AuthorizationError as e:
                print(f"  - Document {doc_id}: ❌ Access denied - {str(e)}")
            except ValueError as e:
                print(f"  - Document {doc_id}: ⚠️ Error - {str(e)}")
        await app.close()

    # Test searching documents for different users
    print("\n2. Testing document search for multiple users:")
    search_term = "Behavioral"
    for user in users:
        app = await AuthorizedDocumentService.create(user_id=user)
        print(f"\nUser: {user}, searching for '{search_term}':")
        try:
            results = await app.search_documents(search_term)
            print(f"\nUser '{user}' searching for '{search_term}':")
            if results:
                for doc in results:
                    print(f"  - Found document {doc.id}: '{doc.title}'")
            else:
                print(f"  - No accessible documents found containing '{search_term}'")
        except Exception as e:
            print(f"  - Error during search: {str(e)}")
        finally:
            await app.close()

    print("\nDemo completed! Note how the results differ based on user permissions.")


if __name__ == "__main__":
    asyncio.run(document_service_test())

    asyncio.run(authorized_document_service_test())
