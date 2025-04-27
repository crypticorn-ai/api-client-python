import pytest_asyncio
from crypticorn.common import AuthHandler, BaseUrl
from typing import AsyncGenerator

@pytest_asyncio.fixture()
async def auth_handler() -> AsyncGenerator[AuthHandler, None]:
    handler = AuthHandler(BaseUrl.LOCAL)
    yield handler
    await handler.client.base_client.close()
