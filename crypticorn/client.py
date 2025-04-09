from crypticorn.hive import HiveClient
from crypticorn.klines import KlinesClient
from crypticorn.pay import PayClient
from crypticorn.trade import TradeClient
from crypticorn.metrics import MetricsClient
from crypticorn.common import BaseURL, ApiVersion


class ApiClient:
    """
    The official client for interacting with the Crypticorn API.

    It is consisting of multiple microservices covering the whole stack of the Crypticorn project.
    """

    def __init__(
        self,
        base_url: BaseURL = BaseURL.PROD,
        api_key: str = None,
        jwt: str = None,
        hive_version: ApiVersion = ApiVersion.V1,
        klines_version: ApiVersion = ApiVersion.V1,
        pay_version: ApiVersion = ApiVersion.V1,
        trade_version: ApiVersion = ApiVersion.V1,
        auth_version: ApiVersion = ApiVersion.V1,
        metrics_version: ApiVersion = ApiVersion.V1,
    ):
        self.base_url = base_url
        self.api_key = api_key
        self.jwt = jwt
        self.hive = HiveClient(base_url, hive_version, api_key, jwt)
        self.trade = TradeClient(base_url, trade_version, api_key, jwt)
        self.klines = KlinesClient(base_url, klines_version, api_key, jwt)
        self.pay = PayClient(base_url, pay_version, api_key, jwt)
        self.metrics = MetricsClient(base_url, metrics_version, api_key, jwt)
        # currently not working due to circular import since the AUTH_Handler
        # is also using the ApiClient
        # self.auth = AuthClient(base_url, auth_version, api_key, jwt)

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
            self.metrics.base_client,
        ]

        for client in clients:
            if hasattr(client, "close"):
                await client.close()

    
    def configure(self, config: Configuration, sub_client: any):
        """
        Update a sub-client's configuration by overriding with the values set in the new config.
        Useful for testing a specific service against a local server instead of the default proxy.

        :param config: The new configuration to use for the sub-client.
        :param sub_client: The sub-client to configure.

        Example:
        This will override the host for the Hive client to connect to http://localhost:8000 instead of the default proxy:
        >>> async with ApiClient(base_url=BaseUrl.DEV, jwt=jwt) as client:
        >>>     client.configure(config=HiveConfig(host="http://localhost:8000"), sub_client=client.hive)
        """
        new_config = sub_client.config
        for attr in vars(config):
            new_value = getattr(config, attr)
            if new_value is not None:
                setattr(new_config, attr, new_value)

        if sub_client == self.hive:
            self.hive = HiveClient(new_config)
        elif sub_client == self.trade:
            self.trade = TradeClient(new_config)
        elif sub_client == self.klines:
            self.klines = KlinesClient(new_config)
        elif sub_client == self.pay:
            self.pay = PayClient(new_config)
        elif sub_client == self.metrics:
            self.metrics = MetricsClient(new_config)
        elif sub_client == self.auth:
            self.auth = AuthClient(new_config)
        else:
            raise ValueError(f"Unknown sub-client: {sub_client}")

