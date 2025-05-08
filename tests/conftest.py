import pytest_asyncio
from crypticorn.common import AuthHandler, BaseUrl
from typing import AsyncGenerator
from tests.envs import API_ENV


@pytest_asyncio.fixture()
async def auth_handler() -> AsyncGenerator[AuthHandler, None]:
    handler = AuthHandler(BaseUrl.from_env(API_ENV))
    assert BaseUrl.from_env(API_ENV) in handler.url
    yield handler
    await handler.client.base_client.close()
