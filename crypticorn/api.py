from typing import Any, Union, Dict
import pandas as pd
import requests
import os
from crypticorn.functions import download_file, logger

__version__ = "1.0.0"

class Crypticorn:
    """
    A client for interacting with the crypticorn API, offering functionality to create and evaluate models,
    download data, and retrieve information about available coins, targets, and features.
    """

    def __init__(self, api_key: str, headers: dict = None):
        """@private
        Initializes the crypticorn API client with an API key.

        :param api_key: The API key required for authenticating requests.
        """
        self._base_url = "http://localhost:3456"
        self._headers = headers if headers else {"Authorization": f"ApiKey {api_key}"}

        self.coins = [int(i) for i in list(list(self.data_info().items())[-1][1].keys())] if self.data_info() != {} else "No data available yet."
        """A list of all available coins that are available for model creation."""

        self.targets = ['Tatooine']
        """A list of all available targets that are available for model creation."""

    def create_model(self, coin_id: int, target: str) -> Dict:
        """
        Creates a new model based on the specified coin_id and target.

        :param coin_id: The ID of the coin to be used for the model. Must be one of the available `coins`.
        :param target: The target variable for the model. Must be one of the available `targets`.
        """
        if coin_id not in self.coins:
            raise ValueError(f"Invalid coin_id. Must be one of: {self.coins}")
        if target not in self.targets:
            raise ValueError(f"Invalid target. Must be one of: {self.targets}")

        endpoint = "/model/creation"
        response = requests.post(
            url=self._base_url + endpoint,
            params={"coin_id": coin_id, "target": target},
            headers=self._headers
        )
        return response.json()

    def evaluate_model(self, id: int, data: Any) -> Dict:
        """
        Evaluates an existing model using the provided data.

        :param id: The ID of the model to evaluate. Must be one of the available `coins`.
        :param data: The data to use for evaluation, provided in one of the following formats: pandas DataFrame,
                     or file paths with extensions `.feather`, `.parquet`, or `.json`.
        """
        if isinstance(data, pd.DataFrame):
            json_data = data.to_json(orient='records')
        elif isinstance(data, str):
            if data.endswith('.feather'):
                json_data = pd.read_feather(data).to_json(orient="records")
            elif data.endswith('.parquet'):
                json_data = pd.read_parquet(data).to_json(orient="records")
            else:
                raise ValueError("Unsupported file format. Use .feather, .parquet, or .json.")
        else:
            raise ValueError("Unsupported data format. Pass a pd.DataFrame or a valid file path.")

        endpoint = "/model/evaluation"
        response = requests.post(
            url=self._base_url + endpoint,
            params={"id": id},
            json=json_data,
            headers=self._headers
        )
        return response.json()

    def download_data(self, model_id: Union[int, str] = None, version: Union[float, str] = None,
                      coin_id: Union[int, str] = None, feature_size: str = None) -> None:
        """
        Downloads training data for models.
        Either pass a model_id or coin_id. For more details about available data, use `data_info()`.

        :param model_id: ID of the model to download data for.
        :param coin_id: ID of the coin for which to download data.
        :param version: (optional) Data version to download. Defaults to the latest version if not specified.
        :param feature_size: (optional) Size of the feature set to download. Default is "all".
        """
        if (not model_id and not coin_id) or (model_id and coin_id):
            raise ValueError("Either model_id or coin_id must be provided.")

        endpoint = "/data"
        response = requests.get(
            url=self._base_url + endpoint,
            params={"coin_id": coin_id, "feature_size": feature_size, "version": version, "model_id": model_id},
            headers=self._headers
        )
        if response.status_code != 200:
            logger.error(response.json()['error'])
            exit()
        data = response.json()
        base_path = f"v{data['version']}/coin_{data['coin']}/"
        os.makedirs(base_path, exist_ok=True)
        download_file(url=data["y_train"], dest_path=f"{base_path}y_train.feather")
        download_file(url=data["X_test"], dest_path=f"{base_path}X_test_{data['feature_size']}.feather")
        download_file(url=data["X_train"], dest_path=f"{base_path}X_train_{data['feature_size']}.feather")

    def help(self) -> Dict:
        """
        Retrieves useful resources from the API.
        """
        endpoint = "/help"
        response = requests.get(
            url=self._base_url + endpoint,
            headers=self._headers)
        return response.json()

    def data_info(self) -> Dict:
        """
        Returns information about the training data (versions, coins, features).
        Useful in combination with `download_data()`
        """
        endpoint = "/data-version"
        response = requests.get(
            url=self._base_url + endpoint,
            headers=self._headers)
        return response.json()


if __name__ == "__main__":
    client = Crypticorn(api_key="REDACTED")
    #print(client.coins)
    # # Testing the methods with example prints
    #print("Testing create_model:")
    #print(client.create_model(4, "Tatooine"))
    #
    #print("\nTesting evaluate_model:")
    #data = pd.DataFrame([{"feature1": 10, "feature2": 20}])
    #print(client.evaluate_model(1, data))

    print("\nTesting download_data with coin_id:")
    client.download_data(coin_id=2, feature_size="all", version=1.2)
    #print("\nTesting download_data with model_id:")
    #client.download_data(model_id=17, version=1.2)


    #print("\nTesting help:")
    #print(client.help())

    # print("\nTesting data info")
    # data = client.data_info()
    # print(type(list(data.keys())[-1]))

    # print("\nCoins:")
    # print(client.coins)
    # print("\nTargets:")
    # print(client.targets)
    # print(client.create_model(2, "Tatooine"))


