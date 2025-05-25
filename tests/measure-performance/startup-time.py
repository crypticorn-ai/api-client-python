import time
import asyncio
from crypticorn import ApiClient

async def test():
    start = time.time()
    client = ApiClient(api_key="dummy")
    elapsed = time.time() - start
    print(f"Startup time: {elapsed:.4f} seconds")
    
    print(f"Main HTTP client: {type(client._http_client).__name__}")
    print(f"Auth client uses same: {client.auth.base_client.rest_client.pool_manager is client._http_client}")
    print(f"Trade client uses same: {client.trade.base_client.rest_client.pool_manager is client._http_client}")
    
    await client.close()

asyncio.run(test())