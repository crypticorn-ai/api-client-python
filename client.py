from altair import Optional
import httpx
from pandas import DataFrame
from pydantic import BaseModel
from typing import Union, List
from urllib.parse import urljoin

class PredictionData(BaseModel):
    id: Optional[int] = None
    action: Optional[str] = None
    course_change: Optional[float]
    symbol: str
    timestamp: int
    version: str
    p10: list[float]
    p30: list[float]
    p50: list[float]
    p70: list[float]
    p90: list[float]

class ApiClient:
    def __init__(self, base_url: str = "https://api.crypticorn.com"):
        self.base_url = base_url
        self.client = httpx.Client()

    def get_response(self, endpoint: str, params: dict = None, dict_key: str = None) -> Union[DataFrame, dict]:
        full_url = urljoin(self.base_url, "/v1/miners" + endpoint)
        try:
            response = self.client.get(full_url, params=params)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e}")
            return {}
        except httpx.RequestError as e:
            print(f"Request error occurred: {e}")
            return {}

        formatted_response = response.json()

        if dict_key:
            return formatted_response.get(dict_key, {})

        return DataFrame(formatted_response)

    def get_economics_news(self, entries: int, reverse: bool = False) -> DataFrame:
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

        res = self.get_response("/ec", {"entries": entries, "reverse": reverse}, "data")
        df = DataFrame(res)
        df.columns = NewsData.__annotations__
        df.sort_values(by="timestamp", ascending=False, inplace=True)
        return df

    def get_bc_historical(self, ticker: str, entries: int, reverse: bool = False) -> DataFrame:
        """

        get: ticker + open_unix + OHLC + Volume data , as pandas dataframe

        --- structure reference: ---

        (column name: data type)

        timestamp: int,
        ticker: str
        open: float,
        high: float,
        low: float,
        close: float,
        volume: float,
        """
        df = self.get_response("/historical", {"ticker": ticker, "entries": entries, "reverse": reverse})
        df.pop("id")
        desired_order = ["timestamp", "ticker", "open", "high", "low", "close", "volume"]
        df = df[desired_order]
        df.rename(columns={"ticker": "coin"}, inplace=True)
        df[["coin", "interval"]] = df["coin"].str.split("@", expand=True)
        df.sort_values(by="timestamp", ascending=False, inplace=True)
        return df
    
    def get_fgi_historical(self, days: int) -> DataFrame:
        """

        get: unix_time + value , as pandas dataframe

        --- structure reference: ---

        (column name: data type)

        unix_time: int,
        value: int,

        """
        df = self.get_response(
            endpoint="/historical/fgi",
            params={"days": days}
        )
        return df
    
    def post_prediction(self, data: PredictionData) -> dict:
        response = self.client.post(
            urljoin(self.base_url, "/v1/predictions"),
            json=data
        )
        return response.json()

# testing
if __name__ == "__main__":
    client = ApiClient("https://api.crypticorn.dev")
    print("")
    print("Economics News")
    print("->")
    print(client.get_economics_news(5))
    print("")
    print("Bitcoin Historical Data")
    print("->")
    print(client.get_bc_historical("BTCUSDT@15m", 5))
    print("")
    print("Fear and Greed Index Historical Data")
    print("->")
    print(client.get_fgi_historical(5))