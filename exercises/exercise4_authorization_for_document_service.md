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

- Remember to handle the async nature of the OpenFGA SDK when integrating with the synchronous document service functions

## Solution

The solution for this exercise is currently TBA (To Be Announced).

Good luck!