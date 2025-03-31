from crypticorn.auth import (
    ApiClient,
    Configuration,
    AdminApi,
)


class AuthClient:
    """
    A client for interacting with the Crypticorn Auth API.
    """

    def __init__(self, base_url: str = None, api_key: str = None, jwt: str = None):
        # Configure Auth client
        self.host = f"{base_url}/v1/auth"
        config = Configuration(
            host=self.host,
            #access_token=jwt, # change to the correct auth method  
            #authorization=api_key, # change to the correct auth method
        )
        base_client = ApiClient(configuration=config)
        self.admin = AdminApi(base_client)
