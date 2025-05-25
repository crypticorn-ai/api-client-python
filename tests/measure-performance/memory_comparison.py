import psutil
import asyncio
from crypticorn import ApiClient

async def memory_test():
    process = psutil.Process()
    before = process.memory_info().rss / 1024 / 1024  # MB
    
    client = ApiClient(api_key="dummy")
    
    after = process.memory_info().rss / 1024 / 1024  # MB
    print(f"Memory usage: {after - before:.2f} MB")
    
    await client.close()

asyncio.run(memory_test())