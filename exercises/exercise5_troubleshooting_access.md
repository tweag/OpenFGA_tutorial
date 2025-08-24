# Exercise 5: Troubleshooting Access

## Problem Statement

In this exercise, you'll learn how to debug and troubleshoot authorization issues using OpenFGA's check explanation API. This feature helps you understand why a particular access check passed or failed.

Your tasks:
1. Create a Python script that uses the OpenFGA check explanation API
2. Analyze the authorization path for various access scenarios
3. Identify and fix authorization issues
4. Create a visualization of the authorization path

## Scenario

You have several users reporting access issues with documents in your system:
- User `clara_zhang` can't access `doc1_3` but believes she should have access
- User `david_rodriguez` unexpectedly has access to `doc2_2`
- User `emily_patel` can read but not write to `doc2_3` and doesn't understand why

## Instructions

1. Create a new file `troubleshoot_access.py` in the fga_example folder
2. Implement a function that uses the OpenFGA SDK to check explanations
3. Analyze each of the reported issues
4. Create a simple text-based visualization of the authorization path

## Hints

- Use the check_explanation endpoint in the OpenFGA SDK:
  ```python
  explanation_response = await client.check_explanation({
      "user": f"user:{user}",
      "relation": "reader",
      "object": f"document:{document}"
  })
  ```

- The response contains a tree of authorization checks that explains why access was granted or denied

- Create a simple function to format and display the explanation tree:
  ```python
  def print_explanation_tree(explanation, indent=0):
      print(" " * indent + explanation["why"])
      for child in explanation.get("children", []):
          print_explanation_tree(child, indent + 2)
  ```

## Solution

Check the `solutions/exercise5_solution.py` file after you've completed your implementation.

Good luck!