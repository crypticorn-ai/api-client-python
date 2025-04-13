import os
from dotenv import load_dotenv

load_dotenv()

# JWT
EXPIRED_JWT = os.getenv("EXPIRED_JWT")
VALID_JWT = os.getenv("VALID_JWT")
# API KEY
FULL_SCOPE_API_KEY = os.getenv("FULL_SCOPE_API_KEY")
ONE_SCOPE_API_KEY = os.getenv("ONE_SCOPE_API_KEY")
EXPIRED_API_KEY = os.getenv("EXPIRED_API_KEY")

if not FULL_SCOPE_API_KEY:
    raise ValueError("FULL_SCOPE_API_KEY is not set")
if not VALID_JWT:
    raise ValueError("VALID_JWT is not set")
if not EXPIRED_JWT:
    raise ValueError("EXPIRED_JWT is not set")
if not ONE_SCOPE_API_KEY:
    raise ValueError("ONE_SCOPE_API_KEY is not set")
if not EXPIRED_API_KEY:
    raise ValueError("EXPIRED_API_KEY is not set")
