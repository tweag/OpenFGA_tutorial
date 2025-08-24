# OpenFGA Exercises

This folder contains exercises to help you learn and practice using OpenFGA for fine-grained authorization. Each exercise focuses on different aspects of authorization modeling and implementation.

## Getting Started

Before attempting these exercises, make sure you:

1. Have set up the main project following the instructions in the root README
2. Have Docker running with the OpenFGA server (`docker-compose up -d`)
3. Have installed the required dependencies (`uv pip install -e .`)

## Exercise Structure

Each exercise includes:

- **Problem Statement**: Describes the scenario and tasks
- **Hints**: Tips to help you complete the exercise
- **Solution**: A reference solution (check only after attempting the exercise)

## Exercises Overview

1. **Basic Check Access** - Learn to check if a user has access to a resource
2. **Adding Relationships** - Add new relationship tuples to the authorization model
3. **Extended Authorization Model** - Modify the model.fga file to add new types and relations
4. **Custom Authorization Logic** - Implement conditional authorization checks
5. **Troubleshooting Access** - Debug authorization issues using the FGA check explanation API

## How to Use These Exercises

1. Start with exercise 1 and progress in order
2. Read the problem statement and try to implement the solution
3. Use the hints if you get stuck
4. Compare your solution with the reference solution after completing the exercise
5. Apply what you've learned to your own projects

## Useful Resources

- **OpenFGA Documentation**: [https://openfga.dev/docs](https://openfga.dev/docs) - Official documentation with concepts, guides, and API references
- **Python SDK**: [https://github.com/openfga/python-sdk](https://github.com/openfga/python-sdk) - Official Python SDK for interacting with OpenFGA
- **GirHub discussions**: [https://github.com/orgs/openfga/discussions](https://github.com/orgs/openfga/discussions) - Get help from the OpenFGA community

Happy learning!