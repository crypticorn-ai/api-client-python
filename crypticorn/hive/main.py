from crypticorn.hive import (
    ApiClient,
    Configuration,
    ModelsApi,
    DataApi,
    StatusApi,
)


class HiveClient:
    """
    A client for interacting with the Crypticorn Hive API.
    """

    def __init__(self, base_url: str = None, api_key: str = None, jwt: str = None):
        # Configure Hive client
        self.host = f"{base_url}/v1/hive"
        self.config = Configuration(
            host=self.host,
            access_token=jwt,
            # authorization=api_key, # change to the correct auth method
        )
        self.base_client = ApiClient(configuration=self.config)
        # Instantiate all the endpoint clients
        self.models = ModelsApi(self.base_client)
        self.data = DataApi(self.base_client)
        self.status = StatusApi(self.base_client)
