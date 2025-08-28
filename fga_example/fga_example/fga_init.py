"""
OpenFGA initialization script for project setup.

This script contains functions for initializing an OpenFGA project:
1. Project initialization with store creation, model setup, and sample data

All operations are performed asynchronously.
"""

import os
import asyncio
import json
from openfga_sdk import OpenFgaClient, ClientConfiguration

from .fga_client import (
    get_project_root, 
    initialize_store, 
    initialize_authorization_model, 
    write_tuples
)


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