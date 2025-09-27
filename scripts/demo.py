"""
Crypticorn API Client Demo - Quick Data Access Examples

This script demonstrates:
- Async and sync client usage
- Quick data retrieval examples
- Custom session management
- Error handling
"""

import aiohttp
from aiohttp import ClientSession

from crypticorn import AsyncClient, SyncClient

# Add your credentials here
API_KEY = ""
JWT_TOKEN = ""


def main():

    api = SyncClient(base_url="https://api.crypticorn.dev", api_key=API_KEY)

    res = api.auth.login.verify()
    print(res)


def main_sync():

    with SyncClient(base_url="https://api.crypticorn.dev", api_key=API_KEY) as client:
        res = client.trade.status.ping()
        print(res)

        # Get exchange mappings
        res = client.notification.notifications.get_notifications(market="futures")
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
    main()
    # main_sync()
    # asyncio.run(custom_session_example())

    # Uncomment to run legacy examples
    # asyncio.run(legacy_examples())
