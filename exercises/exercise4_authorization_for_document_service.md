# Exercise 4: Authorization for Document Service

## Problem Statement

In this exercise, you'll learn how to integrate OpenFGA authorization with the existing document service. You'll modify the document service to only return documents that a user has permission to access.

Your tasks:
1. Create an authorized version of the document service
2. Integrate OpenFGA checks with database queries
3. Filter search results based on user permissions
4. Implement proper error handling for unauthorized access

## Scenario

The document service currently returns all documents without any authorization checks. You need to:
- Modify `get_document_by_id()` to only return documents the user can read
- Update `search_documents()` to filter results based on user permissions
- Return appropriate error messages for unauthorized access attempts

## Instructions

1. Create a new file `authorized_document_service.py` in the fga_example folder
2. Implement authorized versions of the document service functions
3. Add proper error handling for unauthorized access
4. Create a test script to demonstrate the service with different users

## Hints

- Create an authorized version of the document retrieval function:
  ```python
  async def get_document_by_id_authorized(client, user, document_id):
      # First check if the user has permission
      check_response = await client.check({
          "user": f"user:{user}",
          "relation": "reader",
          "object": f"document:{document_id}"
      })
      
      if not check_response.allowed:
          return None  # Or raise a custom unauthorized exception
      
      # If authorized, get the document
      return get_document_by_id(document_id)
  ```

- For search results, filter after retrieving from the database:
  ```python
  async def search_documents_authorized(client, user, search_term):
      # First get all matching documents
      all_results = search_documents(search_term)
      
      # Then filter based on permissions
      authorized_results = []
      for doc in all_results:
          check_response = await client.check({
              "user": f"user:{user}",
              "relation": "reader",
              "object": f"document:{doc['id']}"
          })
          
          if check_response.allowed:
              authorized_results.append(doc)
              
      return authorized_results
  ```

- Remember to handle the async nature of the OpenFGA SDK when integrating with the synchronous document service functions

## Solution

Check the `solutions/exercise4_solution.py` file after you've completed your implementation.

Good luck!