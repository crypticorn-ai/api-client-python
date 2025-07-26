"""
Crypticorn API Client Demo - Quick Data Access Examples

This script demonstrates:
- Async and sync client usage
- Quick data retrieval examples
- Custom session management
- Error handling
"""

import asyncio
import aiohttp
from aiohttp import ClientSession

from crypticorn import AsyncClient, SyncClient, ApiClient
from crypticorn.klines import Timeframe
from crypticorn.trade import BotCreate
from crypticorn.auth import CreateApiKeyRequest

# Add your credentials here
API_KEY = "2SaU1KRUecTAHQBTDFxPo2MJ5pA9Sm"
JWT_TOKEN = ""


async def main():

    async with AsyncClient(
        base_url="https://api.crypticorn.dev", api_key=API_KEY
    ) as client:
        res = await client.trade.status.ping()
        print(res)

        # Get OHLCV data
        res = await client.trade.strategies.kill_strategy(
            symbol="BTCUSDT",
            timeframe=Timeframe.ENUM_1H,
            market="futures",
            limit=10,
        )
        print(res)

        # Get exchange mappings
        res = await client.metrics.exchanges.get_exchange_mappings(market="futures")
        print(res)


def main_sync():

    with SyncClient(base_url="https://api.crypticorn.dev", api_key=API_KEY) as client:
        res = client.trade.status.ping()
        print(res)
        res = client.klines.ohlcv.get_ohlcv_data_fmt(
            symbol="BTCUSDT",
            timeframe=Timeframe.ENUM_1H,
            market="futures",
            limit=10,
        )
        print(res)

        # Get exchange mappings
        res = client.metrics.exchanges.get_exchange_mappings(market="futures")
        print(res)


async def custom_session_example():

    custom_session = ClientSession(
        timeout=aiohttp.ClientTimeout(total=30.0),
    )

    async with AsyncClient(
        base_url="https://api.crypticorn.dev",
        api_key=API_KEY,
        http_client=custom_session,
    ) as client:
        res = await client.trade.status.ping()
        print(res)

    await custom_session.close()


if __name__ == "__main__":
    asyncio.run(main())
    # main_sync()
    # asyncio.run(custom_session_example())

    # Uncomment to run legacy examples
    # asyncio.run(legacy_examples())
