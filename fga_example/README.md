# FGA Example

A Python project for OpenFGA (Fine Grained Authorization) tutorial.

## Description

This project demonstrates the implementation and usage of OpenFGA, a high-performance and flexible authorization system. It includes a sample authorization model for a document management system with users, teams, folders, and documents.

## Installation

```bash
# Clone the repository
git clone <your-repository-url>
cd fga_example

# Set up the environment with uv
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -e .
```

## Running with Docker

This project includes Docker configuration for easy setup and deployment. The Docker setup includes:

1. **OpenFGA server** - configured with a SQLite datastore

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) 
- [Docker Compose](https://docs.docker.com/compose/install/)

### Starting the Services

To start all services:

```bash
docker-compose up
```

Or to run them in the background:

```bash
docker-compose up -d
```

### Accessing the Services

- **OpenFGA API**: http://localhost:8080
- **OpenFGA Playground**: http://localhost:3000/playground

### Stopping the Services

To stop the services:

```bash
docker-compose down
```

To stop the services and remove all data volumes:

```bash
docker-compose down -v
```

## Project Structure

- `fga_example/model.fga` - OpenFGA authorization model definition
- `fga_example/sample_tuples.json` - Sample relationship tuples for the model
- `fga_example/fga_client.py` - Client library for interacting with OpenFGA
- `fga_example/cli.py` - Command-line interface for the project
- `fga_example/main.py` - Core functionality

## CLI Usage

The project provides several command-line tools:

```bash
# Show version information
fga-example --version

# Set up OpenFGA store, model, and sample data
fga-setup
```

## Authorization Model

The project includes a sample authorization model (`model.fga`) that implements a document management system with:

- **Users** - Individual users in the system
- **Editors** - Teams that can have members who can edit documents
- **Folders** - Containers for documents with editor and reader relationships
- **Documents** - Files with inherited permissions from their parent folders

The model demonstrates relationship-based authorization, including:
- Direct assignments (users as members of teams)
- Inherited permissions (document permissions from folders)
- Conditional relationships (document owners must also be editors)

## Development

Install development dependencies:

```bash
uv pip install -e ".[dev]"
```

## Development Tools

### Install FGA Client (Command-Line Interface)

To interact with OpenFGA from the command line, you can install the FGA client:

For macOS users:
```bash
brew install openfga/tap/fga
```

After installation, you can use the `fga` command to interact with your OpenFGA server.

### VSCode OpenFGA Extension

This project includes a `model.fga` file that defines your authorization model. To get syntax highlighting, validation, and other features for this file, install the OpenFGA VSCode extension:

1. Open VSCode
2. Go to the Extensions view (Ctrl+Shift+X or Cmd+Shift+X)
3. Search for "OpenFGA"
4. Install the "OpenFGA" extension by OpenFGA
5. Alternatively, install directly from the [VSCode Marketplace](https://marketplace.visualstudio.com/items?itemName=openfga.openfga-vscode)

The extension provides:
- Syntax highlighting for `.fga` files
- Validation of OpenFGA models
- Code completion and snippets
- Hover documentation
- Go to definition for types and relations

## License

MIT