from crypticorn.pay import ApiClient, Configuration, NOWPaymentsApi, StatusApi, PaymentsApi, ProductsApi


class PayClient:
    """
    A client for interacting with the Crypticorn Pay API.
    """

    def __init__(self, base_url: str = None, api_key: str = None, jwt: str = None):
        # Configure Pay client
        self.host = f"{base_url}/v1/pay"
        config = Configuration(
            host=self.host,
            access_token=jwt,  # change to the correct auth method
            # authorization=api_key, # change to the correct auth method
        )
        base_client = ApiClient(configuration=config)
        self.now = NOWPaymentsApi(base_client)
        self.status = StatusApi(base_client)
        self.payments = PaymentsApi(base_client)
        self.products = ProductsApi(base_client)
