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
- Documents: doc1_1, doc1_2, doc1_3, doc2_1, doc2_2, doc2_3

Check the following access scenarios:
- Can anne_smith read doc1_1?
- Can bob_jones read doc1_2?
- Can david_rodriguez read doc2_1?
- Can emily_patel read doc1_3?

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

Check the `solutions/exercise1_solution.py` file after you've completed your implementation.

Good luck!