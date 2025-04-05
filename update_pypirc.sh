#!/bin/bash

# Get the CodeArtifact token
TOKEN=$(aws codeartifact get-authorization-token \
    --domain crypticorn \
    --domain-owner 643578112146 \
    --query authorizationToken \
    --output text \
    --profile codeartifact)

# Create/update .pypirc with the actual token
cat > ~/.pypirc << EOF
[distutils]
index-servers =
    crypticorn

[crypticorn]
repository = https://crypticorn-643578112146.d.codeartifact.eu-west-1.amazonaws.com/pypi/crypticorn/
username = aws
password = $TOKEN
EOF

echo "Updated .pypirc with fresh token"