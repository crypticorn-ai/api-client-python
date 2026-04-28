"""Tests for the Intel service clients (news, sentiment, social, defi, derivatives)."""

import pytest
import pytest_asyncio

from crypticorn import AsyncClient, SyncClient
from crypticorn._internal.intel_client import IntelConfiguration
from crypticorn.news import NewsClient
from crypticorn.sentiment import SentimentClient
from crypticorn.social import SocialClient
from crypticorn.defi import DefiClient
from crypticorn.derivatives import DerivativesClient


@pytest_asyncio.fixture
async def client():
    async with AsyncClient(api_key="test") as c:
        yield c


@pytest.mark.asyncio
async def test_intel_services_registered(client: AsyncClient):
    """All five intel services are accessible on the client."""
    assert isinstance(client.news, NewsClient)
    assert isinstance(client.sentiment, SentimentClient)
    assert isinstance(client.social, SocialClient)
    assert isinstance(client.defi, DefiClient)
    assert isinstance(client.derivatives, DerivativesClient)


@pytest.mark.asyncio
async def test_intel_config_host(client: AsyncClient):
    """Intel services receive correctly constructed host URLs."""
    assert client.news.config.host == "https://api.crypticorn.com/v1/news"
    assert client.sentiment.config.host == "https://api.crypticorn.com/v1/sentiment"
    assert client.social.config.host == "https://api.crypticorn.com/v1/social"
    assert client.defi.config.host == "https://api.crypticorn.com/v1/defi"
    assert client.derivatives.config.host == "https://api.crypticorn.com/v1/derivatives"


@pytest.mark.asyncio
async def test_intel_config_api_key(client: AsyncClient):
    """Intel services receive the API key from the parent client."""
    for name in ("news", "sentiment", "social", "defi", "derivatives"):
        svc = getattr(client, name)
        assert svc.config.api_key == {"APIKeyHeader": "test"}


@pytest.mark.asyncio
async def test_intel_config_jwt():
    """Intel services receive the JWT when provided."""
    async with AsyncClient(jwt="my-jwt") as c:
        assert c.news.config.access_token == "my-jwt"
        assert c.derivatives.config.access_token == "my-jwt"


@pytest.mark.asyncio
async def test_intel_configure_override(client: AsyncClient):
    """configure() correctly overrides host for intel services."""
    client.configure(
        config=IntelConfiguration(host="http://localhost:9999"),
        service="news",
    )
    assert client.news.config.host == "http://localhost:9999"
    assert client.news.config.api_key == {"APIKeyHeader": "test"}


@pytest.mark.asyncio
async def test_intel_custom_base_url():
    """Custom base_url propagates to intel services."""
    async with AsyncClient(api_key="k", base_url="https://api.crypticorn.dev") as c:
        assert c.news.config.host == "https://api.crypticorn.dev/v1/news"
        assert c.derivatives.config.host == "https://api.crypticorn.dev/v1/derivatives"


def test_sync_client_intel_services():
    """SyncClient also exposes intel services."""
    with SyncClient(api_key="test") as c:
        assert isinstance(c.news, NewsClient)
        assert isinstance(c.derivatives, DerivativesClient)
        assert c.news.config.host == "https://api.crypticorn.com/v1/news"
