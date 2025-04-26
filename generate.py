import os
import sys
import requests
import subprocess

# List of possible module names
MODULES = ["trade", "klines", "hive", "pay", "auth", "metrics"]
ENVIRONMENTS = ["local", "dev", "prod"]
ENV_MAP = {
    "local": "http://localhost/v1",
    "dev": "https://api.crypticorn.dev/v1",
    "prod": "https://api.crypticorn.com/v1",
}


def main():
    print(sys.argv)
    # Check if script is run from the root directory
    if not os.path.exists("python/crypticorn"):
        print("Please run the script from the root directory")
        sys.exit(1)

    if "-m" in sys.argv:
        sys.argv.remove("-m")

    # Initialize variables
    module_name = None
    environment = None

    # Parse command-line arguments
    for arg in sys.argv[1:]:
        if arg.startswith("--service="):
            module_name = arg.split("=")[1]
        elif arg.startswith("--env="):
            environment = arg.split("=")[1]

    # Check if service is provided
    if not module_name:
        print("Please provide the service name as an arg")
        print(f"Valid services: {', '.join(MODULES)}")
        print(f"Example: python python/generate.py --service=trade")
        sys.exit(1)

    # Validate service name
    if module_name not in MODULES:
        print(f"Invalid service: {module_name}")
        print(f"Valid services: {', '.join(MODULES)}")
        sys.exit(1)

    if environment is None:
        environment = "local"
    # Validate environment
    if environment not in ENVIRONMENTS:
        print(f"Invalid environment: {environment}")
        print(f"Valid environments: {', '.join(ENVIRONMENTS)}")
        sys.exit(1)

    ROOT_URL = ENV_MAP[environment]
    upper_module_name = module_name[0].upper() + module_name[1:]

    # ping the api to check if it's running
    try:
        response = requests.get("http://127.0.0.1:3000/v1/trade/openapi.json")#requests.get(f"{ROOT_URL}/{module_name}/openapi.json")
        if response.status_code != 200:
            print(
                f"No openapi.json file found for {module_name} module at path {ROOT_URL}/{module_name}/openapi.json"
            )
            sys.exit(1)
    except requests.RequestException:
        print(f"Failed to connect to API for {module_name} module")
        sys.exit(1)

    print(f"Generating {module_name} client using{ROOT_URL}/{module_name}/openapi.json")

    # Run the OpenAPI generator
    generator_cmd = [
        "openapi-generator-cli",
        "generate",
        "-i",
        f"{ROOT_URL}/{module_name}/openapi.json",
        "-g",
        "python",
        "--package-name",
        "client",
        "--global-property",
        "supportingFiles,models,apis",
        "--additional-properties",
        "pipPackageName=crypticorn,mainClientName=CrypticornClient",
        "-o",
        f"python/crypticorn/{module_name}",
        "--openapi-generator-ignore-list",
        "setup.py,setup.cfg,pyproject.toml,tox.ini,py.typed,.gitignore,.gitlab-ci.yml,.github/,git_push.sh,test/,.travis.yml,test-requirements.txt",
        "--minimal-update",
        "--library",
        "asyncio",
    ]
    subprocess.run(generator_cmd, check=True)

    # Create __init__.py file if it doesn't exist
    init_path = f"python/crypticorn/{module_name}/__init__.py"
    if not os.path.exists(init_path):
        print(f"Creating {init_path} file")
        init_content = f"""from crypticorn.{module_name}.client import *
from crypticorn.{module_name}.main import {upper_module_name}Client

__all__ = ["{upper_module_name}Client", ]
"""
        with open(init_path, "w") as f:
            f.write(init_content)

    # Create main.py file if it doesn't exist
    main_path = f"python/crypticorn/{module_name}/main.py"
    if not os.path.exists(main_path):
        with open(main_path, "w") as f:
            f.write("# Edit this file. You can look in the other modules for examples.")

    # Update imports to use fully qualified package name
    print("Updating imports to use fully qualified package name")
    for root, _, files in os.walk(f"python/crypticorn/{module_name}"):
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
    print(
        f"- Add the dependencies in crypticorn/{module_name}/requirements.txt to the requirements/main.txt file."
    )
    print(f"- Edit the generated crypticorn/{module_name}/main.py file.")
    print(f"- Edit the crypticorn/common/urls.py file to add the new module.")
    print("=========================================================")


if __name__ == "__main__":
    main()
    subprocess.run(["black", ".", "-q"])
