from crypticorn.hive import HiveClient
from crypticorn.klines import KlinesClient
from crypticorn.pay import PayClient
from crypticorn.trade import TradeClient
from crypticorn.auth import AuthClient
import asyncio
from crypticorn.common import BaseURL, APIVersion

class ApiClient:
    def __init__(
        self,
        base_url: BaseURL | str = BaseURL.PROD,
        api_key: str = None,
        jwt: str = None,
        hive_version: APIVersion = APIVersion.V1,
        klines_version: APIVersion = APIVersion.V1,
        pay_version: APIVersion = APIVersion.V1,
        trade_version: APIVersion = APIVersion.V1,
        auth_version: APIVersion = APIVersion.V1,
    ):
        self.base_url = base_url
        self.api_key = api_key
        self.jwt = jwt
        self.hive = HiveClient(base_url, hive_version, api_key, jwt)
        self.trade = TradeClient(base_url, trade_version, api_key, jwt)
        self.klines = KlinesClient(base_url, klines_version, api_key, jwt)
        self.pay = PayClient(base_url, pay_version, api_key, jwt)
        self.auth = AuthClient(base_url, auth_version, api_key, jwt)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
    
     
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
