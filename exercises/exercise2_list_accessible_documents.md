# Exercise 2: List Accessible Documents

## Problem Statement

In this exercise, you'll learn how to determine all documents that a specific user has access to. This builds on the basic access check by performing multiple checks to compile a complete list of accessible resources.

Your tasks:
1. Create a Python script that lists all documents a user can read or write
2. Implement separate functions for checking read and write access
3. Generate a user-friendly report of accessible documents

## Scenario

Using the existing authorization model with users and documents from the system:
- Find all documents that `anne_smith` can read
- Find all documents that `bob_jones` can write
- Compare access levels (read vs. write) for `clara_zhang`

## Instructions

1. Create a new file `list_accessible_documents.py` in the fga_example folder
2. Implement a function that uses the OpenFGA SDK to list all documents a user can access
3. Create separate functions for read and write access checks
4. Format the results to show the difference between read-only and write access

## Hints

- You'll need to iterate through all document IDs and check access for each:
  ```python
  async def list_documents_with_access(client, user, relation):
      accessible_docs = []
      # Assuming document IDs 1-6 for simplicity
      for doc_id in range(1, 7):
          check_response = await client.check({
              "user": f"user:{user}",
              "relation": relation,
              "object": f"document:{doc_id}"
          })
          if check_response.allowed:
              accessible_docs.append(doc_id)
      return accessible_docs
  ```

- Consider creating a combined function that checks both read and write access:
  ```python
  async def get_user_document_access(client, user):
      readable = await list_documents_with_access(client, user, "reader")
      writable = await list_documents_with_access(client, user, "writer")
      return {
          "can_read": readable,
          "can_write": writable
      }
  ```

## Solution

Check the `solutions/exercise2_solution.py` file after you've completed your implementation.

Good luck!