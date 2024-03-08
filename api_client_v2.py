from urllib.parse import urljoin
import pandas as pd
from pandas import DataFrame
import requests
import json
import time
from pydantic import BaseModel
from typing import Union


class ApiClientV2:
    def __init__(self, base_url: str = "https://api.crypticorn.dev/v1/miners/"):
        self.base_url = base_url

    def get_response(self, endpoint: str, params: dict = None, dict_key: str = None) -> pd.DataFrame or dict:
        endpoint = urljoin(self.base_url, endpoint)

        try:
            raw_response = requests.get(endpoint, params=params)
            if raw_response.status_code != 200:
                print(f"""
                Error Encountered! Status Code: {raw_response.status_code}
                Content: {raw_response.text}
                """)
                return

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

    def get_economics_news(self, entries: int, reverse: bool = False) -> pd.DataFrame:
        res = self.get_response(endpoint="ec", dict_key="data", params={
            "entries": entries,
            "reverse": reverse
        })

        class NewsData(BaseModel):
            timestamp: int
            country: Union[str, None]
            event: Union[str, None]
            currency: Union[str, None]
            previous: Union[float, None]
            estimate: Union[float, None]
            actual: Union[float, None]
            change: Union[float, None]
            impact: Union[str, None]
            changePercentage: Union[float, None]

        df = pd.DataFrame(res)
        df.columns = NewsData.__annotations__
        df.sort_values(by="timestamp", ascending=False, inplace=True)
        return df


if __name__ == "__main__":
    client = ApiClientV2()
    resp = client.get_economics_news(entries=5, reverse=True)
    print(resp)
