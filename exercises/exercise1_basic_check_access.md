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

1. Implement a function that uses the OpenFGA SDK to check if a user has read access to a document `check_access` in fga_client.py.
2. Implement `batch_check_access` function.
3. Run tests and verify the results

## Hints

- (Check SDK documentation)[https://github.com/openfga/python-sdk/tree/main?tab=readme-ov-file#check]
- (Batch check SDK documentation)[https://github.com/openfga/python-sdk/tree/main?tab=readme-ov-file#batch-check]

## Solution

The solution for this exercise demonstrates how to check if a user has access to a specific document using OpenFGA's Python SDK.

You can find the complete solution code in: `/exercises/solutions/exercise1.py`

This solution implements:
- A `check_access` function to verify if a user has a specific relation to an object
- A `batch_check_access` function for efficient batch processing
