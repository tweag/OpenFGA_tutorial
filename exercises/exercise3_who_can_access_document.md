# Exercise 3: Who Can Access a Document

## Problem Statement

In this exercise, you'll learn how to determine all users who have access to a specific document. 
This is essentially the reverse of the previous exercise and is useful for auditing and managing document permissions.

This builds on [list-users](https://openfga.dev/docs/getting-started/perform-list-users) API.

>  The List Users call allows you to retrieve a list of users that have a specific relationship with a given object. This can be used in scenarios such as retrieving users who have access to a resource or managing members in a group.

## Scenario

You need to audit access to several important documents in your system:
- Determine all users who can read `document:2`
- Find all users who can write to `document:6` 
- Create a full access report showing both readers and writers for `document:1`

## Instructions

1. Implement a function that uses the OpenFGA SDK to list all users that are in a given relationship to a document. Use:  `list_users_for_document` in fga_client.py.

## Hints

- [List Users documentation](https://openfga.dev/docs/getting-started/perform-list-users)
- [List Users Python SDK](https://github.com/openfga/python-sdk?tab=readme-ov-file#list-users)

## Solution

You can find the complete solution code in: `/exercises/solutions/exercise3.py`

Good luck!