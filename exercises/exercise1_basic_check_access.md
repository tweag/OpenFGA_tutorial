# Exercise 1: Basic Check Access

## Problem Statement

In this exercise, you'll learn how to check if a user has access to a resource using the OpenFGA API. You'll be working with the existing document management system model.

Your tasks:
1. Create a Python script that checks if a user has read access to a specific document
2. Check access for multiple user/document combinations
3. Print the results in a user-friendly format

## Scenario

Using the existing authorization model with:
- Users: anne_smith, bob_jones, clara_zhang, david_rodriguez, emily_patel
- Documents: document:1, document:2, document:3, document:4, document:5, document:6

Check the following access scenarios:
- Can anne_smith read document:1?
- Can bob_jones read document:2?
- Can david_rodriguez read document:3?
- Can emily_patel read document:4?

## Instructions

1. Create a new file `check_access.py` in the fga_example folder
2. Implement a function that uses the OpenFGA SDK to check if a user has read access to a document
3. Test with the users and documents listed in the scenario
4. Run your script and verify the results

## Hints

- Use the `openfga_sdk` library to create a client:
  ```python
  from openfga_sdk import OpenFgaClient, ClientConfiguration
  ```

- The check function in the SDK looks like:
  ```python
  check_response = await client.check({
      "user": f"user:{user}",
      "relation": "reader",
      "object": f"document:{document}"
  })
  ```

- Don't forget to handle the async nature of the SDK

## Solution

The solution for this exercise is currently TBA (To Be Announced).

Good luck!