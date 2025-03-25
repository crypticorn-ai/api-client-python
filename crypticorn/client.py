from crypticorn.hive import HiveClient
from crypticorn.klines import KlinesClient
from crypticorn.pay import PayClient
from crypticorn.trade import TradeClient


class Crypticorn:
    def __init__(
        self,
        base_url: str = "https://api.crypticorn.com",
        api_key: str = None,
        jwt: str = None,
    ):

        self.hive = HiveClient(base_url, api_key, jwt)
        self.trade = TradeClient(base_url, api_key, jwt)
        self.klines = KlinesClient(base_url, api_key, jwt)
        self.pay = PayClient(base_url, api_key, jwt)
