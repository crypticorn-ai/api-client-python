from crypticorn.pay import (
    ApiClient,
    Configuration,
    NOWPaymentsApi,
    StatusApi,
    PaymentsApi,
    ProductsApi,
)
from crypticorn.common import APIKeyScheme, BaseURL, APIVersion, Service


class PayClient:
    """
    A client for interacting with the Crypticorn Pay API.
    """

    def __init__(
        self,
        base_url: BaseURL | str,
        api_version: APIVersion,
        api_key: str = None,
        jwt: str = None,
    ):
        self.host = f"{base_url}/{api_version.value}/{Service.PAY.value}"
        self.config = Configuration(
            host=self.host,
            access_token=jwt,
            api_key={APIKeyScheme.name: api_key} if api_key else None,
            api_key_prefix=(
                {APIKeyScheme.name: APIKeyScheme.prefix} if api_key else None
            ),
        )
        self.base_client = ApiClient(configuration=self.config)
        self.now = NOWPaymentsApi(self.base_client)
        self.status = StatusApi(self.base_client)
        self.payments = PaymentsApi(self.base_client)
        self.products = ProductsApi(self.base_client)
