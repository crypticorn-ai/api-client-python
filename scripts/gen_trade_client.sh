#!/bin/bash

openapi-generator-cli generate \
  -i http://localhost/v1/trade/openapi.json \
  -g python \
  --global-property models \
  -c python/scripts/config/trade_client.json \
  --skip-validate-spec \
  -o python/public/

rm -rf python/public/docs
rm -rf python/public/test

echo "from . import *" > python/public/crypticorn/models/__init__.py
for file in python/public/crypticorn/models/*.py; do
  module=$(basename "$file" .py)
  echo "from .${module} import *" >> python/public/crypticorn/models/__init__.py
done