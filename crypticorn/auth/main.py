from crypticorn.auth import (
    ApiClient,
    Configuration,
    AdminApi,
    ServiceApi,
    UserApi,
    WalletApi,
)


class AuthClient:
    """
    A client for interacting with the Crypticorn Auth API.
    """

    def __init__(self, base_url: str = None, api_key: str = None, jwt: str = None):
        # Configure Auth client
        self.host = f"{base_url}/v1/auth"
        self.config = Configuration(
            host=self.host,
            access_token=jwt,  # change to the correct auth method
            # authorization=api_key, # change to the correct auth method
        )
        self.base_client = ApiClient(configuration=self.config)
        # Sub APIs
        self.admin = AdminApi(self.base_client)
        self.service = ServiceApi(self.base_client)
        self.user = UserApi(self.base_client)
        self.wallet = WalletApi(self.base_client)

    def close(self):
        self.base_client.__aexit__()

