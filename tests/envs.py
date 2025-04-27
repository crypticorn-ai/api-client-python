import os
from dotenv import load_dotenv
from crypticorn.common import gen_random_id
import jwt
import time

load_dotenv(dotenv_path=".env.test")


def generate_valid_jwt():
    now = int(time.time())
    payload = {
        "sub": USER_ID,
        "aud": JWT_AUDIENCE,
        "iss": JWT_ISSUER,
        "jti": gen_random_id(),
        "iat": now,
        "exp": now + JWT_EXPIRES_IN,
        "scopes": [],
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token


# JWT
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ISSUER = os.getenv("JWT_ISSUER")
JWT_AUDIENCE = os.getenv("JWT_AUDIENCE")
JWT_EXPIRES_IN = 60 * 60  # 1 hour
USER_ID = os.getenv("USER_ID")
EXPIRED_JWT = os.getenv("EXPIRED_JWT")
VALID_JWT = generate_valid_jwt()
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
