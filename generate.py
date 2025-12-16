# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "openapi-generator-cli[jdk4py]==7.14.0",
#   "requests",
# ]
# ///

import argparse
import os
import subprocess
import sys
from typing import Final, Literal

import requests

# List of possible module names
MODULE_TYPE = Literal[
    "trade",
    "hive",
    "pay",
    "auth",
    "metrics",
    "dex",
    "notification",
    "indicator",
    "klines",
]
MODULES: Final[tuple[MODULE_TYPE, ...]] = (
    "trade",
    "hive",
    "pay",
    "auth",
    "metrics",
    "dex",
    "notification",
    "indicator",
    "klines",
)
VERSION_TYPE = Literal["v1", "v2"]
VERSIONS: Final[tuple[VERSION_TYPE, ...]] = ("v1", "v2")
ENVIRONMENT_TYPE = Literal["local", "dev", "prod"]
ENVIRONMENTS: Final[tuple[ENVIRONMENT_TYPE, ...]] = ("local", "dev", "prod")
ENV_MAP = {
    "local": "http://localhost",
    "dev": "https://api.crypticorn.dev",
    "prod": "https://api.crypticorn.com",
}


def main(module_name: str, environment: str, version: str):
    ROOT_URL = ENV_MAP[environment]
    upper_module_name = module_name[0].upper() + module_name[1:]

    # ping the api to check if it's running
    try:
        response = requests.get(f"{ROOT_URL}/{version}/{module_name}/openapi.json")
        if response.status_code != 200:
            print(
                f"No openapi.json file found for {module_name} module at path {ROOT_URL}/{version}/{module_name}/openapi.json"
            )
            sys.exit(1)
    except requests.RequestException:
        print(f"Failed to connect to API for {module_name} module")
        sys.exit(1)

    print("Deleting existing packages's client folder")
    subprocess.run(["rm", "-rf", f"crypticorn/{module_name}/client"], check=True)

    print(
        f"Generating {module_name} client using {ROOT_URL}/{version}/{module_name}/openapi.json"
    )

    # Run the OpenAPI generator
    generator_cmd = [
        "openapi-generator-cli",
        "generate",
        "-i",
        f"{ROOT_URL}/{version}/{module_name}/openapi.json",
        "-g",
        "python",
        "--package-name",
        "client",
        "--global-property",
        "supportingFiles,models,apis",
        "--additional-properties",
        "pipPackageName=crypticorn",
        "-o",
        f"crypticorn/{module_name}",
        "--openapi-generator-ignore-list",
        "setup.py,setup.cfg,pyproject.toml,tox.ini,py.typed,.gitignore,.gitlab-ci.yml,.github/,git_push.sh,test/,docs/,.travis.yml,test-requirements.txt,requirements.txt,README.md,.openapi-generator-ignore",
        "--minimal-update",
        "--library",
        "asyncio",
        "-t",
        "templates",
        "--skip-validate-spec",  # used because the payment module has duplicate operation ids for one endpoint
    ]
    subprocess.run(generator_cmd, check=True)

    # Create __init__.py file if it doesn't exist
    init_path = f"crypticorn/{module_name}/__init__.py"
    if not os.path.exists(init_path):
        print(f"Creating {init_path} file")
        init_content = f"""from crypticorn.{module_name}.client import *
from crypticorn.{module_name}.main import {upper_module_name}Client

__all__ = ["{upper_module_name}Client"]
"""
        with open(init_path, "w") as f:
            f.write(init_content)

    # Create main.py file if it doesn't exist
    main_path = f"crypticorn/{module_name}/main.py"
    if not os.path.exists(main_path):
        with open(main_path, "w") as f:
            f.write("# Edit this file. You can look in the other modules for examples.")

    # Update imports to use fully qualified package name
    print("Updating imports to use fully qualified package name")
    for root, _, files in os.walk(f"crypticorn/{module_name}"):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    content = f.read()

                content = content.replace(
                    "from client.", f"from crypticorn.{module_name}.client."
                )
                content = content.replace(
                    "from client ", f"from crypticorn.{module_name}.client "
                )
                content = content.replace(
                    "import client.", f"import crypticorn.{module_name}.client."
                )
                content = content.replace(
                    "import client", f"import crypticorn.{module_name}.client"
                )
                content = content.replace(
                    "klass = getattr(client",
                    f"klass = getattr(crypticorn.{module_name}.client",
                )

                with open(file_path, "w") as f:
                    f.write(content)

    print("========================IMPORTANT========================")
    print("If you are adding a new module, you need to do the following:")
    print("- Edit the generated crypticorn/client.py file.")
    print(f"- Edit the generated crypticorn/{module_name}/main.py file.")
    print("=========================================================")


if __name__ == "__main__":
    # Check if script is run from the root directory
    if not os.path.exists("crypticorn"):
        print("Please run the script from the root directory")
        sys.exit(1)

    # Create argument parser
    parser = argparse.ArgumentParser(
        description="Generate API clients from OpenAPI specifications"
    )

    parser.add_argument("service", choices=MODULES, help="Service to generate")

    parser.add_argument(
        "--env",
        choices=ENVIRONMENTS,
        default="local",
        help="Environment to use (default: local)",
    )

    parser.add_argument(
        "--version",
        choices=VERSIONS,
        default="v1",
        help="API version to use (default: v1)",
    )

    # Parse arguments
    args = parser.parse_args()

    # Get parsed values
    module_name = args.service
    environment = args.env
    version = args.version

    # Print configuration
    print(f"Generating {module_name} client for the given environment and version")

    print(f"Environment: {environment.upper()}")
    print(f"Version: {version.upper()}")

    main(module_name, environment, version)
