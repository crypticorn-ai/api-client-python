from crypticorn.auth import (
    ApiClient,
    Configuration,
    AdminApi,
    ServiceApi,
    UserApi,
    WalletApi,
)
from crypticorn.common import APIKeyHeader, BaseURL, APIVersion, Service


class AuthClient:
    """
    A client for interacting with the Crypticorn Auth API.
    """

    def __init__(
        self,
        base_url: BaseURL | str,
        api_version: APIVersion,
        api_key: str = None,
        jwt: str = None,
    ):
        self.host = f"{base_url}/{api_version.value}/{Service.AUTH.value}"
        self.config = Configuration(
            host=self.host,
            access_token=jwt,
            api_key={APIKeyHeader.name: api_key} if api_key else None,
            api_key_prefix=(
                {APIKeyHeader.name: APIKeyHeader.prefix} if api_key else None
            ),
        )
        self.base_client = ApiClient(configuration=self.config)
        # Instantiate all the endpoint clients
        self.admin = AdminApi(self.base_client)
        self.service = ServiceApi(self.base_client)
        self.user = UserApi(self.base_client)
        self.wallet = WalletApi(self.base_client)

    def close(self):
        self.base_client.__aexit__()
