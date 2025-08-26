# OpenFGA Tutorial

This repository contains a tutorial for learning OpenFGA (Fine Grained Authorization), a high-performance authorization system that helps you implement fine-grained access control in your applications.

## Repository Structure

This repository is organized into two main directories:

- **`fga_example/`**: Contains the example Python project with OpenFGA implementation
  - Core library code for working with OpenFGA
  - Docker setup for running OpenFGA locally
  - Sample authorization model and relationship tuples

- **`exercises/`**: Contains a series of exercises to learn OpenFGA
  - Five progressive exercises covering different aspects of OpenFGA
  - Each exercise includes a problem statement, scenario, and hints
  - Reference solutions are provided for self-checking

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd OpenFGA_tutorial
   ```

2. **Set up the environment**:
   Assuming, you use [uv](https://docs.astral.sh/uv/getting-started/installation/) as your package manager:
   ```bash
   cd fga_example
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e .
   ```

3. **Start the OpenFGA server**:
   ```bash
   docker-compose up -d
   ```
   For this you make sure that Docker is installed and running on your machine. You may also need to `docker login`.

4. **Install FGA client**:
   Detailed instructions can be found [fga CLI documentation](https://github.com/openfga/cli).
   - For MacOS users:
       ```bash
       brew install openfga/tap/fga
       ```
   - For Linux users:
   Download the .deb, .rpm or .apk packages from the releases page and install them:
      ```bash
       sudo apt install ./fga_<version>_linux_<arch>.deb
       ```

5. **Initialize the OpenFGA store and model**:
   ```bash
   fga-setup
   ```
   
6. Add the update environment variables to your `.env` file:
   ```
   FGA_STORE_ID=XXXXX
   FGA_MODEL_ID=YYYYY
   ```

## Understanding the Model

The tutorial uses a document management system model with:

- **Users**: Individual users in the system (anne_smith, bob_jones, etc.)
- **Editors**: Teams that can have user members
- **Folders**: Containers for documents with editor and reader relations
- **Documents**: Files with permissions inherited from their parent folders

### Authorization Model Structure

The model (defined in `fga_example/fga_example/model.fga`) uses the following relationships:

```
model
  schema 1.1

type user

type editors
  relations
    define member: [user]

type folder
  relations
    define editor: [editors#member]
    define reader: [user] or editor

type document
  relations
    define parent: [folder]
    define reader: reader from parent
    define writer: editor from parent
    define owner: [user] and editor from parent
```

This structure demonstrates key OpenFGA concepts:
- Direct assignments (users as members of teams)
- Type inheritance (document permissions from folders)
- Computed relationships (document owners must also be editors)

## Using the OpenFGA Playground

The OpenFGA Playground is a web interface that helps you visualize and test your authorization models. The tutorial setup includes this playground, accessible at http://localhost:3000/playground after starting the Docker services.

### Exploring the Model in the Playground

1. **Access the playground**: Open http://localhost:3000/playground in your browser
2. **View the authorization model**:
   - Click on "Authorization Models" in the sidebar
   - Select the latest model
   - Explore the visual representation of types and relations

3. **Visualize relationship tuples**:
   - Click on "Tuples" in the sidebar
   - View the existing relationships between entities
   - You can add and remove tuples in this view 

4. **Test authorization queries**:
   - Click on "Assertions" in the sidebar
   - Create a test query like:
     - User: `user:anne_smith`
     - Relation: `reader`
     - Object: `document:doc1_1`
   - Click play button to see if access is granted
   - Use right panel to visualize the authorization path

5. **Experiment with the model**:
   - Try different authorization checks with various users and documents
   - Follow the authorization paths to understand how access is determined
   - This will help you understand the relationship-based model before implementing it in code

## Additional Resources

- [OpenFGA Documentation](https://openfga.dev/docs)
- [OpenFGA GitHub Repository](https://github.com/openfga/openfga)
- [Zanzibar Paper](https://research.google/pubs/pub48190/) - The Google paper that inspired OpenFGA

## License

MIT