# Exercise 3: Who Can Access a Document

## Problem Statement

In this exercise, you'll learn how to determine all users who have access to a specific document. This is essentially the reverse of the previous exercise and is useful for auditing and managing document permissions.

Your tasks:
1. Create a Python script that lists all users who can access a specific document
2. Implement functions to check both read and write access
3. Generate a comprehensive access report for a document

## Scenario

You need to audit access to several important documents in your system:
- Determine all users who can read `document:2`
- Find all users who can write to `document:6` 
- Create a full access report showing both readers and writers for `document:1`

## Instructions

1. Create a new file `document_access_audit.py` in the fga_example folder
2. Implement a function that lists all users who can read a specific document
3. Implement a function that lists all users who can write to a specific document
4. Create a combined function that generates a complete access report

## Hints

- You'll need to check each user's access to the document:
  ```python
  async def list_users_with_access(client, document_id, relation):
      users_with_access = []
      # Get users from users.csv or hardcode the list
      user_list = ["anne_smith", "bob_jones", "clara_zhang", "david_rodriguez", "emily_patel"]
      
      for user in user_list:
          check_response = await client.check({
              "user": f"user:{user}",
              "relation": relation,
              "object": f"document:{document_id}"
          })
          if check_response.allowed:
              users_with_access.append(user)
              
      return users_with_access
  ```

- Consider creating a combined report function:
  ```python
  async def generate_document_access_report(client, document_id):
      readers = await list_users_with_access(client, document_id, "reader")
      writers = await list_users_with_access(client, document_id, "writer")
      owners = await list_users_with_access(client, document_id, "owner")
      
      return {
          "document_id": document_id,
          "readers": readers,
          "writers": writers,
          "owners": owners
      }
  ```

## Solution

Check the `solutions/exercise3_solution.py` file after you've completed your implementation.

Good luck!