from enum import Enum

class Domain(Enum):
    PROD = "crypticorn.com"
    DEV = "crypticorn.dev"

class BaseURL(Enum):
    PROD = f"https://{Domain.PROD.value}"
    DEV = "https://api.crypticorn.dev"
    LOCALHOST = "http://localhost"
    DOCKER = "http://host.docker.internal"

class APIVersion(Enum):
    V1 = "v1"

class Service(Enum):
    HIVE = "hive"
    KLINES = "klines"
    PAY = "pay"
    TRADE = "trade"
    AUTH = "auth"