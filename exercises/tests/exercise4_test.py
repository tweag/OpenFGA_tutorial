#!/usr/bin/env python3
"""
Example script demonstrating how to use the document_service module
to retrieve and search for documents.
"""

from fga_example.document_service import DocumentService

def document_service_test():
    app = DocumentService()
    # Example 1: Get a document by its ID
    doc_id = 2
    document = app.get_document_by_id(doc_id)
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
    results = app.search_documents(search_term)
    
    print(f"\nSearch results for '{search_term}':")
    if results:
        for doc in results:
            print(f"- {doc.id}: {doc.title}")
    else:
        print("No matching documents found")
    app.close()

if __name__ == "__main__":
    document_service_test()