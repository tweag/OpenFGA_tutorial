# Exercise 2: Adding Relationships

## Problem Statement

In this exercise, you'll learn how to add new relationship tuples to the OpenFGA authorization model. You'll extend the existing document management system by adding new users, teams, and relationships.

Your tasks:
1. Create a Python script that writes new relationship tuples to the OpenFGA store
2. Add new users, teams, and folders
3. Establish permissions between these entities
4. Verify the relationships work as expected

## Scenario

You need to add the following entities and relationships:
- New user: `frank_miller`
- New editor team: `team3`
- New folder: `folder3`
- New document: `doc3_1`

Create these relationships:
1. Make `frank_miller` a member of `team3`
2. Make `team3` an editor of `folder3`
3. Make `folder3` the parent of `doc3_1`
4. Make `frank_miller` the owner of `doc3_1`

## Instructions

1. Create a new file `add_relationships.py` in the fga_example folder
2. Implement a function that uses the OpenFGA SDK to write relationship tuples
3. Add all the relationships specified in the scenario
4. Create a function to check if `frank_miller` can read and write to `doc3_1`

## Hints

- Reuse code from the first exercise for checking access
- Use the `write_tuples` function from the example code as a reference
- The write function in the SDK takes an array of tuples:
  ```python
  tuples = [
      ClientTuple(user="user:frank_miller", relation="member", object="editors:team3"),
      # Add other tuples here
  ]
  
  write_response = await client.write(ClientWriteRequest(writes=tuples))
  ```

## Solution

Check the `solutions/exercise2_solution.py` file after you've completed your implementation.

Good luck!