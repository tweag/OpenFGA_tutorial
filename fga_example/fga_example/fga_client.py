"""
OpenFGA client script to demonstrate basic operations with OpenFGA.

This script contains separate functions for:
1. Initializing a store
2. Initializing the authorization model from model.fga file using the OpenFGA CLI
3. Writing tuples to the authorization model

All operations are performed asynchronously.
"""

import os
import asyncio
import json
import subprocess
from pathlib import Path
from typing import List, Tuple
from openfga_sdk import (
    OpenFgaClient,
    ClientConfiguration,
    CreateStoreRequest,
    WriteAuthorizationModelRequest)
from openfga_sdk.client.models import ClientTuple, ClientWriteRequest


# configuration = ClientConfiguration(
#     api_url=FGA_API_URL,  # required
#     store_id=FGA_STORE_ID,  # optional, not needed when calling `CreateStore` or `ListStores`
#     authorization_model_id=FGA_MODEL_ID,  # Optional, can be overridden per request
# )
    


def read_model_file(file_path):
    """Read the model.fga file and return its contents."""
    with open(file_path, 'r') as file:
        return file.read()


def get_project_root():
    """Get the project root path."""
    # Assuming the structure is /project_root/fga_example/fga_example/...
    return Path(__file__).parent.parent


async def initialize_store(api_url=None, store_name="fga_store") -> str:
    """
    Initialize an OpenFGA store asynchronously.
    
    Args:
        api_url: URL of the OpenFGA API
        store_name: Name for the new store
        
    Returns:
        store_id
    """
    api_url = api_url or os.environ.get("OPENFGA_API_URL", "http://localhost:8080")
    configuration = ClientConfiguration(
        api_url=api_url,  # required
    )
    
    body = CreateStoreRequest(
        name = store_name,
    )
    # Create a store
    async with OpenFgaClient(configuration) as fga_client:
        api_response = await fga_client.create_store(body)

    store_id = api_response.id
    
    return store_id


async def initialize_authorization_model(model_path=None, store_id=None, api_url=None):
    """
    Initialize the authorization model from a model.fga file asynchronously.
    Uses the OpenFGA CLI 'fga model write' command to write the model directly.
    
    Args:
        model_path: Path to the model.fga file, defaults to the model.fga in the project
        store_id: Store ID
        api_url: API URL
        
    Returns:
        str: Authorization model ID
    """
    # If model_path is not provided, use the default path relative to project root
    if model_path is None:
        model_path = get_project_root() / "fga_example" / "model.fga"
    
    model_path = str(model_path)
    print(f"Using model file from: {model_path}")
    
    # Validate required parameters
    if store_id is None:
        raise ValueError("store_id must be provided when calling initialize_authorization_model")
    
    if api_url is None:
        api_url = os.environ.get("OPENFGA_API_URL", "http://localhost:8080")
    
    # Use the OpenFGA CLI to write the model directly
    # Run 'fga model write' command to write the model directly
    cmd = [
        "fga", "model", "write",
        "--store-id", store_id,
        "--api-url", api_url,
        "--file", model_path
    ]
    
    print(f"Running command: {' '.join(cmd)}")
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=True
    )
    
    # Extract the authorization model ID from the output
    output = result.stdout
    
    # Try to parse the authorization model ID from the output
    import re
    match = re.search(r'([0-9A-Z]{26})', output)
    if match:
        auth_model_id = match.group(1)
    else:
        auth_model_id = None 
    
    print(f"Successfully wrote authorization model with ID: {auth_model_id}")
    
    print(f"Add the following to your .env file:")
    print(f"FGA_STORE_ID={store_id}")
    print(f"FGA_MODEL_ID={auth_model_id}")
    return auth_model_id
        


async def write_tuples(client: OpenFgaClient, to_write: List[dict]):
    """
    Write a tuple to the authorization model asynchronously.
    
    Args:
        client: OpenFgaClient instance
        user: User identifier
        relation: Relation identifier
        object_: Object identifier
        
    Returns:
        The write response
    """
    # Create the tuple key
    _tuples = [ClientTuple(user=t["user"],
                           relation=t["relation"],
                           object=t["object"])
                for t in to_write]
 

    options = { "authorization_model_id": client.get_authorization_model_id()}
    
    # Use the client directly - the SDK handles session management internally
    write_response = await client.write(
        ClientWriteRequest(writes=_tuples), options
    )

    return write_response




async def project_init():
    """Set up the project with a new store, authorization model and example tuples."""
    api_url = os.environ.get("OPENFGA_API_URL", "http://localhost:8080")
    
    # Step 1: Initialize store
    store_id = await initialize_store(api_url=api_url, store_name="Nice model store 123")
    print(f"Store initialized with ID: {store_id}")
    
    # Step 2: Initialize authorization model
    auth_model_id = await initialize_authorization_model(store_id=store_id, api_url=api_url)
    print(f"Authorization model initialized with ID: {auth_model_id}")
    
    client = OpenFgaClient(ClientConfiguration(api_url=api_url, store_id=store_id, authorization_model_id=auth_model_id))
    # Step 3: Add tuples
    # Read tuples from the sample_tuples.json file
    sample_tuples_path = get_project_root() / "fga_example" / "sample_tuples.json"
    with open(sample_tuples_path, 'r') as file:
        sample_tuples = json.load(file) 

    write_response = await write_tuples(
        client=client,
        to_write=sample_tuples
    )
    
    print("All operations completed successfully!")

    await client.close()  # Close the client session when done


def main():
    """Entry point for the script that runs the async initialize project function."""
    asyncio.run(project_init())


if __name__ == "__main__":
    main()