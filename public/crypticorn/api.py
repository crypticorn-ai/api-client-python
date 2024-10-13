from pydantic import BaseModel
from typing import Any, Union, Dict
import pandas as pd
import requests
import os
from .utils import download_file, ModelInfoResponse, EvaluateModelResponse, ErrorResponse, DataInfoResponse


class Crypticorn:
    """
    A client for interacting with the crypticorn API, offering functionality to create and evaluate models,
    download data, and retrieve information about available coins, targets, and features.
    """

    def __init__(self, api_key: str, headers: dict = None, base_url="https://api.crypticorn.dev"):
        """@private
        Initializes the crypticorn API client with an API key.

        :param api_key: The API key required for authenticating requests.
        """
        self._base_url = os.getenv("HIVE_BASE_URL", base_url) + "/v1/hive"
        self._headers = headers if headers else {"Authorization": f"ApiKey {api_key}"}

    def create_model(self, coin_id: int, target: str) -> Union[ModelInfoResponse, ErrorResponse]:
        """
        Creates a new model based on the specified coin_id and target.

        :param coin_id: The ID of the coin to be used for the model.
        :param target: The target variable for the model.
        """
        endpoint = "/model/creation"
        response = requests.post(
            url=self._base_url + endpoint,
            params={"coin_id": coin_id, "target": target},
            headers=self._headers
        )
        return response.json()

    def evaluate_model(self, id: int, data: Any) -> Union[EvaluateModelResponse, ErrorResponse]:
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

    def download_data(self, model_id: int, version: float = None,
                      feature_size: str = None) -> Union[int, ErrorResponse]:
        """
        Downloads training data for models.
        Either pass a model_id or coin_id. For more details about available data, use `data_info()`.

        :param model_id: ID of the model to download data for.
        :param version: (optional) Data version to download. Defaults to the latest version if not specified.
        :param feature_size: (optional) Size of the feature set to download. Default is "all".
        """
        endpoint = "/data"
        response = requests.get(
            url=self._base_url + endpoint,
            params={"feature_size": feature_size, "version": float(version), "model_id": model_id},
            headers=self._headers
        )
        if response.status_code != 200:
            return response.json()
        data = response.json()
        base_path = f"v{data['version']}/coin_{data['coin']}/"
        os.makedirs(base_path, exist_ok=True)
        download_file(url=data["y_train"], dest_path=f"{base_path}y_train.feather")
        download_file(url=data["X_test"], dest_path=f"{base_path}X_test_{data['feature_size']}.feather")
        download_file(url=data["X_train"], dest_path=f"{base_path}X_train_{data['feature_size']}.feather")
        return 200

    def data_info(self) -> Union[DataInfoResponse, ErrorResponse]:
        """
        Returns information about the training data (versions, coins, features).
        Useful in combination with `download_data()` and `create_model()`.
        """
        endpoint = "/data-version"
        response = requests.get(
            url=self._base_url + endpoint,
            headers=self._headers)
        return response.json()
