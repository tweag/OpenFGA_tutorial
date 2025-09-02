# Exercise 2: List Accessible Documents

## Problem Statement

In this exercise, you'll learn how to determine all documents that a specific user has access to. 
This builds on [list-objects](https://openfga.dev/api/service#/Relationship%20Queries/ListObjects) API.

> The List Objects API allows you to retrieve all objects of a specified type that a user has a given relationship with. This can be used in scenarios like displaying all documents a user can read or listing resources a user can manage.

## Scenario

Using the existing authorization model with users and documents from the system:
- Find all documents that `anne_smith` can read
- Find all documents that `bob_jones` can edit
- Compare access levels (read vs. write) for `clara_zhang`

## Instructions

1. Implement a function that uses the OpenFGA SDK to list all documetns that a user has access to `list_documents_for_user` in fga_client.py.
2. [bonus]Compare the time of list-objects and check endpoints.

## Hints

- [List Objects documentation](https://openfga.dev/docs/getting-started/perform-list-objects)
- [List Objects Python SDK](https://github.com/openfga/python-sdk?tab=readme-ov-file#list-objects)

## Solution

You can find the complete solution code in: `/exercises/solutions/exercise2.py`

Good luck!