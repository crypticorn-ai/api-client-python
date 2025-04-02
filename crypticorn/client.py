from crypticorn.hive import HiveClient
from crypticorn.klines import KlinesClient
from crypticorn.pay import PayClient
from crypticorn.trade import TradeClient
from crypticorn.auth import AuthClient
import asyncio


class ApiClient:
    def __init__(
        self,
        base_url: str = "https://api.crypticorn.com",
        api_key: str = None,
        jwt: str = None,
    ):
        self.base_url = base_url
        self.api_key = api_key
        self.jwt = jwt
        self.hive = HiveClient(base_url, api_key, jwt)
        self.trade = TradeClient(base_url, api_key, jwt)
        self.klines = KlinesClient(base_url, api_key, jwt)
        self.pay = PayClient(base_url, api_key, jwt)
        self.auth = AuthClient(base_url, api_key, jwt)

    # Async context manager protocol
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
    
    # Sync context manager protocol
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Create a new event loop for closing if needed
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # Create a new loop if the current one is already running
                new_loop = asyncio.new_event_loop()
                new_loop.run_until_complete(self.close())
                new_loop.close()
            else:
                loop.run_until_complete(self.close())
        except RuntimeError:
            # If no event loop exists in this thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.close())
            loop.close()
        
    async def close(self):
        """Close all client sessions."""
        clients = [
            self.hive.base_client,
            self.trade.base_client,
            self.klines.base_client,
            self.pay.base_client,
            self.auth.base_client
        ]
        
        for client in clients:
            if hasattr(client, 'close'):
                await client.close()
