# Exercise 3: Extended Authorization Model

## Problem Statement

In this exercise, you'll learn how to extend the OpenFGA authorization model by adding new types and relations. You'll modify the existing model to include project types and different access levels.

Your tasks:
1. Create a modified version of the authorization model
2. Add new types and relations to support projects and sharing
3. Update the model in the OpenFGA server
4. Test the new model with sample relationship tuples

## Scenario

You need to extend the document management system to include projects with the following requirements:
- A new `project` type that can contain multiple folders
- A new `collaborator` relation for projects with different access levels:
  - `viewer` - Can only view content
  - `contributor` - Can view and edit content
  - `admin` - Can manage the project and its members
- Projects can be shared with individual users or teams

## Instructions

1. Create a new file `extended_model.fga` with your extended model
2. Implement the new types and relations based on the requirements
3. Write a Python script to update the model in the OpenFGA server
4. Create sample relationship tuples to test your model

## Hints

- Start by copying the existing model and extending it
- The model syntax for a new type might look like:
  ```
  type project
    relations
      define folder: [folder]
      define viewer: [user]
      define contributor: [user] and viewer
      define admin: [user] and contributor
  ```
- Remember that relations can reference other relations
- Use the OpenFGA Playground to validate your model

## Solution

Check the `solutions/exercise3_solution.fga` and `solutions/exercise3_solution.py` files after you've completed your implementation.

Good luck!