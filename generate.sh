#!/bin/bash

# List of possible module names
MODULES=("trade" "klines" "hive" "pay")

# Check if script is run from the root directory
if [ ! -d "python/crypticorn" ]; then
  echo "Please run the script from the root directory"
  exit 1
fi

# Check if valid module name is provided
[[ $# -eq 1 && " ${MODULES[@]} " =~ " $1 " ]] || { echo "Please provide one of as an arg: ${MODULES[*]}"; exit 1; }
MODULE_NAME=$1
UPPER_MODULE_NAME=$(tr '[:lower:]' '[:upper:]' <<< ${MODULE_NAME:0:1})${MODULE_NAME:1}

# ping the api to check if it's running
if ! curl -s -o /dev/null -w "%{http_code}" http://localhost/v1/${MODULE_NAME}/openapi.json | grep -q "200"; then
  echo "No openapi.json file found for ${MODULE_NAME} module"
  exit 1
fi

echo "Generating ${MODULE_NAME} client"

# Run the OpenAPI generator
openapi-generator-cli generate \
  -i http://localhost/v1/${MODULE_NAME}/openapi.json \
  -g python \
  --package-name client \
  --global-property supportingFiles,models,apis \
  --additional-properties pipPackageName=crypticorn,mainClientName=CrypticornClient \
  --skip-validate-spec \
  -o python/crypticorn/${MODULE_NAME} \
  --openapi-generator-ignore-list "setup.py,setup.cfg,pyproject.toml,tox.ini,py.typed,.gitignore,.gitlab-ci.yml,.github/,git_push.sh,test/,.travis.yml,test-requirements.txt" \
  --minimal-update

# Create __init__.py file if it doesn't exist
if [ ! -f "python/crypticorn/${MODULE_NAME}/__init__.py" ]; then
  echo "Creating python/crypticorn/${MODULE_NAME}/__init__.py file"
    touch python/crypticorn/${MODULE_NAME}/__init__.py
    printf "from crypticorn.%s.client import *\nfrom crypticorn.%s.main import %sClient\n" "${MODULE_NAME}" "${MODULE_NAME}" "${UPPER_MODULE_NAME}"  > "python/crypticorn/${MODULE_NAME}/__init__.py"
fi

# Create main.py file if it doesn't exist
if [ ! -f "python/crypticorn/${MODULE_NAME}/main.py" ]; then
  echo "Creating python/crypticorn/${MODULE_NAME}/main.py file"
    touch python/crypticorn/${MODULE_NAME}/main.py
    cat > python/crypticorn/${MODULE_NAME}/main.py << EOL
from crypticorn.${MODULE_NAME} import (
    ApiClient,
    Configuration,
    # BotsApi,
    # ExchangesApi,
    # NotificationsApi,
)


class ${UPPER_MODULE_NAME}Client:
    """
    A client for interacting with the Crypticorn ${UPPER_MODULE_NAME} API.
    """

    def __init__(self, base_url: str = None, api_key: str = None, jwt: str = None):
        # Configure ${UPPER_MODULE_NAME} client
        self.host = f"{base_url}/v1/${MODULE_NAME}"
        config = Configuration(
            host=self.host,
            #access_token=jwt, # change to the correct auth method  
            #authorization=api_key, # change to the correct auth method
        )
        base_client = ApiClient(configuration=config)
        # Instantiate all the endpoint clients
        # Example:
        # self.bots = BotsApi(base_client)
        # self.exchanges = ExchangesApi(base_client)
        # self.notifications = NotificationsApi(base_client)
EOL
fi

# Update imports to use fully qualified package name, e.g. from client.* import smth -> from crypticorn.klines.client.* import smth
echo "Updating imports to use fully qualified package name"
find python/crypticorn/${MODULE_NAME} -type f -name "*.py" -exec sed -i '' \
  -e 's/from client\./from crypticorn.'${MODULE_NAME}'.client./g' \
  -e 's/from client /from crypticorn.'${MODULE_NAME}'.client /g' \
  -e 's/import client\./import crypticorn.'${MODULE_NAME}'.client./g' \
  -e 's/import client$/import crypticorn.'${MODULE_NAME}'.client/g' \
  -e 's/klass = getattr(client/klass = getattr(crypticorn.'${MODULE_NAME}'.client/g' \
  {} +

echo "========================IMPORTANT========================"
echo "Add the dependencies in crypticorn/${MODULE_NAME}/requirements.txt to the requirements/main.txt file."
echo "Edit the generated crypticorn/${MODULE_NAME}/main.py file."
echo "========================================================="
