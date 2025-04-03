import os
import sys
import requests
import subprocess

# List of possible module names
MODULES = ["trade", "klines", "hive", "pay", "auth"]
ROOT_URL = "http://localhost/v1"


def main():
    # Check if script is run from the root directory
    if not os.path.exists("python/crypticorn"):
        print("Please run the script from the root directory")
        sys.exit(1)

    # Check if valid module name is provided
    if len(sys.argv) != 2 or sys.argv[1] not in MODULES:
        print(f"Please provide one of as an arg: {', '.join(MODULES)}")
        sys.exit(1)

    module_name = sys.argv[1]
    upper_module_name = module_name[0].upper() + module_name[1:]

    # ping the api to check if it's running
    try:
        response = requests.get(f"{ROOT_URL}/{module_name}/openapi.json")
        if response.status_code != 200:
            print(f"No openapi.json file found for {module_name} module")
            sys.exit(1)
    except requests.RequestException:
        print(f"Failed to connect to API for {module_name} module")
        sys.exit(1)

    print(f"Generating {module_name} client")

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
"""
        with open(init_path, "w") as f:
            f.write(init_content)

    # Create main.py file if it doesn't exist
    main_path = f"python/crypticorn/{module_name}/main.py"
    if not os.path.exists(main_path):
        print(f"Creating {main_path} file")
        main_content = f'''from crypticorn.{module_name} import (
    ApiClient,
    Configuration,
    # BotsApi,
    # ExchangesApi,
    # NotificationsApi,
)
from crypticorn.common import APIKeyHeader, BaseURL, APIVersion, ServiceSuffix


class {upper_module_name}Client:
    """
    A client for interacting with the Crypticorn {upper_module_name} API.
    """

    def __init__(
        self,
        base_url: BaseURL | str,
        api_version: APIVersion,
        api_key: str = None,
        jwt: str = None,
    ):
        self.host = f"{{base_url}}/{{api_version.value}}/{{Service.{{upper_module_name}}.value}}"
        self.config = Configuration(
            host=self.host,
            access_token=jwt,
            api_key={{APIKeyHeader.name: api_key}} if api_key else None,
            api_key_prefix=(
                {{APIKeyHeader.name: APIKeyHeader.prefix}} 
                if api_key 
                else None,
            ),
        )
        self.base_client = ApiClient(configuration=self.config)
        # Instantiate all the endpoint clients
        # self.bots = BotsApi(self.base_client)
        # self.exchanges = ExchangesApi(self.base_client)
        # self.notifications = NotificationsApi(self.base_client)
'''
        with open(main_path, "w") as f:
            f.write(main_content)

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
