"""FGA Example package."""

__version__ = "0.1.0"

# Make client and init functions available at the package level
from fga_example.client import (
    initialize_store,
    initialize_authorization_model,
    write_tuples,
)
from fga_example.init import project_init
