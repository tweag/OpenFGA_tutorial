"""Command-line interface for fga_example."""

import argparse
import importlib.metadata
import asyncio

from fga_example.fga_init import project_init


def fga_setup():
    """Run the FGA setup process."""
    asyncio.run(project_init())
    return 0


def cli():
    """Run the CLI application."""
    parser = argparse.ArgumentParser(description="FGA Example CLI")
    parser.add_argument(
        "--version", action="store_true", help="Show version information"
    )
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Add fga_setup command
    setup_parser = subparsers.add_parser(
        "setup", help="Setup FGA store, model and sample data"
    )

    args = parser.parse_args()

    if args.version:
        __version__ = importlib.metadata.version("fga-example")
        print(f"fga_example version {__version__}")
        return 0
    if args.command == "setup":
        return fga_setup()
