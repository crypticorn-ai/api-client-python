from urllib.parse import urljoin

import pandas as pd
from pandas import DataFrame
import requests
import json
import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.4f} seconds to execute.")
        return result

    return wrapper


class ApiClient:
    def __init__(self, base_url: str = None):
        if base_url is None:
            base_url = "http://api.crypticorn.com/v1/"
        self.base_url = base_url

    def get_response(self, endpoint: str, params: dict = None, dict_key: str = None) -> pd.DataFrame or dict:
        endpoint = urljoin(self.base_url, endpoint)

        try:
            raw_response = requests.get(endpoint, params=params)
        except Exception as e:
            print(f"""
            --- Possible Error Cause---
            incorrect url , network issue or ApiClient not configured
            
            ---- Error Details: ----
            {e}
            """
                  )
            return

        formatted_response: list[dict] or dict = json.loads(raw_response.text)

        if dict_key is not None:
            return formatted_response[dict_key]

        return DataFrame(formatted_response)

    def get_fgi_historical(self, days: int) -> DataFrame:
        """

        get: unix_time + value , as pandas dataframe

        --- structure reference: ---

        (column name: data type)

        unix_time: int,
        value: int,

        """
        return self.get_response(
            endpoint="historical/fgi",
            params={"days": days}
        )

    def get_bc_historical(self, ticker: str, entries: int, reverse: bool = False) -> DataFrame:
        """

        get: ticker + open_unix + OHLC + Volume data , as pandas dataframe

        --- structure reference: ---

        (column name: data type)

        timestamp: int,
        ticker: str
        open_15m: float,
        high_15m: float,
        low_15m: float,
        close_15m: float,
        volume_15m: float,

        """
        df: DataFrame = self.get_response(
            endpoint="historical/sbc",
            params={"ticker": ticker, "entries": entries, "reverse": reverse}
        )
        df.pop("id")
        desired_order = ["timestamp", "ticker", "open_15m", "high_15m", "low_15m", "close_15m", "volume_15m"]
        df = df[desired_order]
        df.rename(columns={"ticker": "coin"}, inplace=True)
        df.sort_values(by="timestamp", ascending=False, inplace=True)
        return df

    def get_futures_bc_historical(self, ticker: str, entries: int, reverse: bool = False) -> DataFrame:
        """

        get: ticker + open_unix + OHLC + Volume data , as pandas dataframe

        --- structure reference: ---

        (column name: data type)

        timestamp: int,
        ticker: str
        open_15m: float,
        high_15m: float,
        low_15m: float,
        close_15m: float,
        volume_15m: float,

        """
        df: DataFrame = self.get_response(
            endpoint="historical/fbc",
            params={"ticker": ticker, "entries": entries, "reverse": reverse}
        )
        df.pop("id")
        desired_order = ["timestamp", "ticker", "open_15m", "high_15m", "low_15m", "close_15m", "volume_15m"]
        df = df[desired_order]
        df.rename(columns={"ticker": "coin"}, inplace=True)
        df.sort_values(by="timestamp", ascending=False, inplace=True)
        return df

    def get_all_tickers(self, filter_from: list = None) -> dict:
        """ Should be used upon program initialization and not more than once """
        response: dict = self.get_response(
            endpoint="sbc/startup-settings",
            dict_key="tickers"
        )
        if filter_from:
            for ticker in filter_from:
                if ticker in response:
                    response.pop(ticker)
        return response


if __name__ == "__main__":
    api = ApiClient()
    api_v1 = ApiClient()
    # get_bc_historical
    print(api.get_bc_historical(ticker="BTCUSDT", entries=200, reverse=False))
    print(api.get_futures_bc_historical(ticker="BTCUSDT", entries=200, reverse=False))
    print(api.get_all_tickers(filter_from=["USDTTRY", "BNBETH", "PAXGUSDT"]))
    import os

    # Get the current working directory
    current_directory = os.getcwd()
    all_files = os.listdir(current_directory)
    file_name = "requirements.txt"
    if file_name in all_files:
        os.rename(os.path.join(current_directory, file_name), "hello.txt")
        print("renaming")

    print(all_files)
    print(current_directory)


