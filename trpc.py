import httpx
from pydantic import BaseModel
from typing import Optional, Union, List
from urllib.parse import urljoin

class TrpcClient:
    def __init__(
        self, base_url: str = "https://api.crypticorn.com/trpc", api_key: str = None
    ):
        self.base_url = base_url
        self.api_key = api_key
        self.client = httpx.Client()

    def verify(self, token: str) -> bool:
        response = self.client.get(
            self.base_url + "/verify",
            headers={"Authorization": f"Bearer {token}"},
        )
        response.raise_for_status()
        try:
            res = response.json()
            return res['result']['data']['json']
        except:
            return None
