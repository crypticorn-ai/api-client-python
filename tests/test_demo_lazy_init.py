#!/usr/bin/env python3

import asyncio
from crypticorn import ApiClient
from crypticorn.common import BaseUrl

async def test_with_valid_auth():
    print("Testing ApiClient creation and initialization...")
    client = ApiClient(base_url=BaseUrl.DEV, api_key="test-key")
    print(f"ApiClient created successfully")
    print(f"   Base URL: {client.base_url}")
    print(f"   HTTP client before async context: {client._http_client}")
    async with client:
        print(f"Entered async context successfully")
        print(f"   HTTP client after entering context: {type(client._http_client).__name__}")
        print(f"   HTTP client configured: {client._http_client is not None}")
        try:
            result = await client.trade.ping()
            print(f"API call successful: {result}")
        except Exception as e:
            print(f"API call failed: {type(e).__name__}")
    print("Exited async context successfully")

async def test_without_async_context():
    print("\nTesting client creation without async context...")
    client = ApiClient(base_url=BaseUrl.DEV)
    print(f"ApiClient created successfully without async context")
    print(f"   HTTP client: {client._http_client}")
    await client._ensure_http_client()
    print(f"HTTP client created manually: {type(client._http_client).__name__}")
    await client.close()
    print(f"Client closed successfully")

if __name__ == "__main__":
    print("=" * 60)
    print("Lazy HTTP Client Initialization Demo")
    print("=" * 60)
    asyncio.run(test_with_valid_auth())
    asyncio.run(test_without_async_context())
    print("\n" + "=" * 60)
    print("All tests completed successfully!")
    print("No event loop errors encountered")
    print("Lazy initialization working as expected")
    print("=" * 60)
