from pydantic import BaseModel
from enum import Enum

class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    OPTIONS = "OPTIONS"

class APIScope(BaseModel):
    name: str
    description: str
    methods: list[HTTPMethod]
    path: str
    path_regex: str

class ProductScope(APIScope):
    pass