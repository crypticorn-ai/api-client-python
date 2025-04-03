from pydantic import BaseModel

class AuthScheme(BaseModel):
    name: str
    type: str
    scheme: str | None = None
    bearerFormat: str | None = None
    in_: str | None = None
    prefix: str | None = None

HTTPBearer = AuthScheme(name="HTTPBearer", type="http", scheme="bearer", bearerFormat="JWT")
APIKeyHeader = AuthScheme(name="APIKeyHeader", type="apiKey", in_="header", prefix="X-API-Key")
