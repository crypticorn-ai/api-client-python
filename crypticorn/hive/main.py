from crypticorn.hive import (
    ApiClient,
    Configuration,
    ModelsApi,
    DataApi,
    StatusApi,
)
from crypticorn.common import APIKeyHeader, BaseURL, APIVersion, Service


class HiveClient:
    """
    A client for interacting with the Crypticorn Hive API.
    """

    def __init__(
        self,
        base_url: BaseURL | str,
        api_version: APIVersion,
        api_key: str = None,
        jwt: str = None,
    ):
        self.host = f"{base_url}/{api_version.value}/{Service.HIVE.value}"
        self.config = Configuration(
            host=self.host,
            access_token=jwt,
            api_key={APIKeyHeader.name: api_key} if api_key else None,
            api_key_prefix=(
                {APIKeyHeader.name: APIKeyHeader.prefix}
                if api_key
                else None
            ),
        )
        self.base_client = ApiClient(configuration=self.config)
        # Instantiate all the endpoint clients
        self.models = ModelsApi(self.base_client)
        self.data = DataApi(self.base_client)
        self.status = StatusApi(self.base_client)
