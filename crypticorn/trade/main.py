from crypticorn.trade import (
    ApiClient,
    APIKeysApi,
    BotsApi,
    Configuration,
    ExchangesApi,
    FuturesTradingPanelApi,
    NotificationsApi,
    OrdersApi,
    StatusApi,
    StrategiesApi,
    TradingActionsApi,
)


class TradeClient:
    """
    A client for interacting with the Crypticorn Trade API.
    """

    def __init__(self, base_url: str = None, api_key: str = None, jwt: str = None):
        # Configure Trade client
        self.host = f"{base_url}/v1/trade"
        self.config = Configuration(
            host=self.host,
            access_token=jwt,
            # authorization=api_key, # TODO: add api key verification
        )
        self.base_client = ApiClient(configuration=self.config)
        # Instantiate all the endpoint clients
        self.bots = BotsApi(self.base_client)
        self.exchanges = ExchangesApi(self.base_client)
        self.notifications = NotificationsApi(self.base_client)
        self.orders = OrdersApi(self.base_client)
        self.status = StatusApi(self.base_client)
        self.strategies = StrategiesApi(self.base_client)
        self.actions = TradingActionsApi(self.base_client)
        self.futures = FuturesTradingPanelApi(self.base_client)
        self.api_keys = APIKeysApi(self.base_client)
