# Exercise 4: Custom Authorization Logic

## Problem Statement

In this exercise, you'll implement custom authorization logic that goes beyond the basic OpenFGA model capabilities. You'll create a Python function that combines OpenFGA checks with custom business logic.

Your tasks:
1. Create a Python module that implements custom authorization checks
2. Combine OpenFGA authorization with time-based restrictions
3. Implement role-based access controls with custom validation
4. Test your implementation with various scenarios

## Scenario

You need to implement the following authorization requirements:
- Documents can have an "embargo date" after which they become accessible
- Some documents require approval before being accessible to certain user roles
- Access to sensitive documents should be logged for audit purposes
- Rate limiting for document access (max 100 documents per user per day)

## Instructions

1. Create a new file `custom_auth.py` in the fga_example folder
2. Implement functions for each of the custom authorization requirements
3. Create a main function that demonstrates all the features
4. Test with different user roles and document types

## Hints

- Start with the basic OpenFGA check, then add your custom logic on top
- Use Python's datetime module for time-based restrictions
- Consider creating a simple in-memory cache for rate limiting
- For audit logging, you can use Python's built-in logging module
- Example structure:
  ```python
  async def check_document_access(client, user_id, document_id, context=None):
      # First check FGA permissions
      has_fga_permission = await check_fga_permission(client, user_id, "reader", document_id)
      
      if not has_fga_permission:
          return False
          
      # Check embargo date
      if not await check_embargo_date(document_id, context.get('current_time')):
          return False
          
      # Log the access
      log_document_access(user_id, document_id)
      
      # Check rate limits
      if not check_rate_limit(user_id):
          return False
          
      return True
  ```

## Solution

Check the `solutions/exercise4_solution.py` file after you've completed your implementation.

Good luck!