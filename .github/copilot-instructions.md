# OpenFGA Tutorial Project

This is an educational repository for learning OpenFGA (Fine Grained Authorization), a high-performance authorization system for implementing fine-grained access control.

## Project Purpose

This tutorial teaches OpenFGA concepts through a document management system example with users, editor teams, folders, and documents with hierarchical permissions.

## Project Structure

- `fga_example/`: Core Python library implementing OpenFGA client and document service

  - `fga_example/model.fga`: Authorization model defining user, editors, folder, and document types with relationships
  - `fga_example/fga_client.py`: Async client library for OpenFGA operations (check, batch_check, list_objects, list_users, write tuples)
  - `fga_example/document_service.py`: SQLite-backed document service
  - `fga_example/fga_init.py`: Initialization logic for OpenFGA store and model
  - `fga_example/cli.py`: CLI commands (`fga-setup`, `fga-example`)
  - `data/`: CSV files with sample users, folders, documents

- `exercises/`: 5 progressive exercises with problem statements, hints, tests, and reference solutions
  - Exercise 1: Basic check access
  - Exercise 2: List accessible documents
  - Exercise 3: Who can access a document
  - Exercise 4: Authorization for document service
  - Exercise 5: Conditional access based on publication status

## Technology Stack

- **Language**: Python 3.12+
- **Package Manager**: uv
- **OpenFGA SDK**: openfga-sdk >= 0.9.5
- **Infrastructure**: Docker Compose for OpenFGA server
- **Testing**: pytest
- **Optional**: Nix flakes with direnv for environment setup

## Authorization Model

The model uses OpenFGA schema 1.1 with:

- **user**: Individual users (anne_smith, bob_jones, clara_zhang, david_rodriguez, emily_patel)
- **editors**: Teams with member relation
- **folder**: Has editor and reader relations (reader is union of explicit readers and editors)
- **document**: Has parent folder, inherited reader/writer permissions, and conditional owner (user AND editor from parent)

## Key Patterns

1. **Relationship-based access**: Users have access through explicit assignments or team memberships
2. **Permission inheritance**: Documents inherit reader/writer from parent folders
3. **Conditional ownership**: Ownership requires both explicit assignment AND editor permission from parent
4. **Async operations**: All OpenFGA client operations use async/await

## Development Workflow

1. Start OpenFGA server: `docker-compose up -d`
2. Initialize store and model: `fga-setup` (stores IDs in .env)
3. Run tests: `pytest exercises/tests/`
4. Access OpenFGA playground: http://localhost:3000/playground

## Code Conventions

- Use async/await for all OpenFGA client operations
- User references formatted as `user:{user_id}`
- Object references formatted as `{type}:{id}` (e.g., `document:1`, `folder:2`)
- Team member references use `editors#{team_id}#member` format
- Environment variables: FGA_STORE_ID, FGA_MODEL_ID, FGA_API_URL

## When Helping with Exercises

- Encourage users to attempt exercises before reviewing solutions
- Point to SDK documentation and hints in exercise files
- Reference `exercises/solutions/` for correct implementations
- Verify solutions match test expectations in `exercises/tests/`
