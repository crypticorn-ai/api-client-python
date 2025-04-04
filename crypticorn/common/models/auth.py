from enum import Enum

from fastapi.security import APIKeyHeader, HTTPBearer
from pydantic import BaseModel


class TokenType(str, Enum):
    BEARER = "bearer"
    API_KEY = "api_key"


class _AuthScheme(BaseModel):
    name: str
    type: str
    scheme: str | None = None
    bearerFormat: str | None = None
    in_: str | None = None
    prefix: str | None = None

    @property
    def to_dep(self) -> HTTPBearer | APIKeyHeader:
        if self.type == "http":
            return HTTPBearer(
                scheme_name=self.name, bearerFormat=self.bearerFormat, auto_error=False
            )
        elif self.type == "apiKey":
            return APIKeyHeader(
                scheme_name=self.name, name=self.prefix, auto_error=False
            )


BearerScheme = _AuthScheme(
    name="HTTPBearer", type="http", scheme="bearer", bearerFormat="JWT"
)
APIKeyScheme = _AuthScheme(
    name="APIKeyHeader", type="apiKey", in_="header", prefix="X-API-Key"
)
