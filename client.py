import httpx
import pandas as pd
from pandas import DataFrame
from pydantic import BaseModel
from typing import Optional, Union, List
from urllib.parse import urljoin
import os

class PredictionData(BaseModel):
    id: Optional[int] = None
    action: Optional[str] = None
    course_change: Optional[float]
    symbol: str
    timestamp: int
    version: str
    base_price: Optional[float]
    p10: list[float]
    p30: list[float]
    p50: list[float]
    p70: list[float]
    p90: list[float]


class TrendData(BaseModel):
    timestamps: Optional[list[int]]
    positive_prob: list[float]
    symbol: str
    version: Optional[str]


class TrendQuery(BaseModel):
    symbol: str
    limit: int
    offset: int
    sort: str
    dir: str
    from_ts: int
    to_ts: int
    version: str = "1"


class ApiClient:
    def __init__(
        self, base_url: str = "https://api.crypticorn.com", api_key: str = None, token: str = None
    ):
        self.base_url = base_url
        self.api_key = api_key
        self.token = token
        self.client = httpx.Client()

    def get_response(
        self, endpoint: str, params: dict = None, dict_key: str = None
    ) -> Union[DataFrame, dict]:
        full_url = urljoin(self.base_url, "/v1/miners" + endpoint)
        print(full_url)
        print(params)
        try:
            response = self.client.get(full_url, params=params, timeout=None)
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

    def get_bc_historical(
        self, ticker: str, interval: str, entries: int, reverse: bool = False
    ) -> DataFrame:
        """

        get: ticker + open_unix + OHLC + Volume data , as pandas dataframe

        --- structure reference: ---

        (column name: data type)

        timestamp: int,
        ticker: str
        open_interval: float,
        high_interval: float,
        low_interval: float,
        close_interval: float,
        volume_interval: float,
        """
        df = self.get_response(
            "/historical",
            {"ticker": ticker + "@" + interval, "entries": entries, "reverse": reverse},
        )
        desired_order = [
            "timestamp",
            "ticker",
            "open",
            "high",
            "low",
            "close",
            "volume",
        ]
        df = df[desired_order]
        df.rename(
            columns={
                "ticker": "coin",
                "open": f"open_{interval}",
                "high": f"high_{interval}",
                "low": f"low_{interval}",
                "close": f"close_{interval}",
                "volume": f"volume_{interval}",
            },
            inplace=True,
        )
        df[["coin", "interval"]] = df["coin"].str.split("@", expand=True)
        df.pop("interval")
        df.sort_values(by="timestamp", ascending=False, inplace=True)
        df["timestamp"] = df["timestamp"] // 1000
        return df

    def get_fgi_historical(self, days: int) -> DataFrame:
        """

        get: unix_time + value , as pandas dataframe

        --- structure reference: ---

        (column name: data type)

        unix_time: int,
        value: int,

        """
        df = self.get_response(endpoint="/historical/fgi", params={"days": days})
        return df

    def post_prediction(self, data: PredictionData) -> dict:
        response = self.client.post(
            urljoin(self.base_url, "/v1/predictions"),
            json=data.dict(),
            headers={"Authorization": f"Bearer {self.api_key}"},
        )
        return response.json()

    def get_latest_predictions(self) -> DataFrame:
        response = self.client.get(
            urljoin(self.base_url, "/v1/predictions/latest?version=2"),
            headers={"Authorization": f"Bearer {self.api_key}"},
        )
        arr = response.json()
        flatarr = []
        for i in arr:
            for index, _ in enumerate(i["p50"]):
                interval = 900
                ts = i["timestamp"]
                ts = ts - (ts % interval)
                ts = ts + (index * interval)
                pred_dict = {
                    "id": i["id"],
                    "action": i["action"],
                    "course_change": i["course_change"],
                    "symbol": i["symbol"],
                    "timestamp": ts,
                    "version": i["version"],
                    # "base_price": i["base_price"],
                    "p10": i["p10"][index],
                    "p30": i["p30"][index],
                    "p50": i["p50"][index],
                    "p70": i["p70"][index],
                    "p90": i["p90"][index],
                }
                flatarr.append(pred_dict)
        df = DataFrame(flatarr)
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
        return df

    def get_prediction(self, id: int) -> PredictionData:
        response = self.client.get(
            urljoin(self.base_url, f"/v1/predictions/id/{id}"),
            headers={"Authorization": f"Bearer {self.api_key}"},
        )
        return response.json()

    def get_prediction_time(self, id) -> DataFrame:
        response = self.client.get(
            urljoin(self.base_url, f"/v1/predictions/time/{id}"),
            headers={"Authorization": f"Bearer {self.api_key}"},
        )
        arr = response.json()
        return DataFrame(arr)

    def get_udf_history(self, symbol: str, entries: int) -> DataFrame:
        now = int(pd.Timestamp.now().timestamp())
        response = self.client.get(
            urljoin(self.base_url, "/v1/udf/history"),
            headers={"Authorization": f"Bearer {self.api_key}"},
            params={
                "from": now - (entries * 900),
                "to": now,
                "symbol": symbol,
                "resolution": "15",
                "countback": entries,
            },
        )
        # # {'s': 'ok', 't': [1710982800.0, 1710983700.0], 'c': [67860.61, 67930.01], 'o': [67656.01, 67860.6], 'h': [67944.69, 67951.15], 'l': [67656.0, 67792.06], 'v': [448.61539, 336.9907]}
        result = response.json()
        # construct dataframe for t, c, o, h, l, v arrays
        df = DataFrame(result)
        df["t"] = pd.to_datetime(df["t"], unit="s")
        df.pop("s")
        return df

    def post_trend(self, data: TrendData) -> dict:
        response = self.client.post(
            urljoin(self.base_url, "/v1/trends"),
            json=data.dict(),
            headers={"Authorization": f"Bearer {self.api_key}"},
        )
        return response.json()

    def get_trends(self, query: TrendQuery):
        response = self.client.get(
            urljoin(self.base_url, "/v1/trends"),
            headers={"Authorization": f"Bearer {self.api_key}"},
            params=query.dict(),
        )
        df = DataFrame(response.json())
        return df

    # New Kline Service
    def get_symbols(self, market: str) -> DataFrame:
        """
        get: symbol for futures or spot, as pandas dataframe
        market: futures or spot
        """
        response = self.client.get(
            urljoin(self.base_url, f"/v1/klines/symbols/{market}"), timeout=None
        )
        df = DataFrame(response.json()['symbols'])
        return df

    def get_klines(self, market: str, symbol: str,  interval: str, limit: int, start_timestamp: int = None, end_timestamp: int = None) -> DataFrame:
        """
        get: unix_time + OHLCV data , as pandas dataframe
        symbol have to be in capital case e.g. (BTCUSDT)
        market: futures or spot
        interval: 1m, 3m, 5m, 15m, 30m, 1h, 4h, 1d
        """
        params = {"limit": limit}
        if start_timestamp is not None:
            params["start"] = start_timestamp
        if end_timestamp is not None:
            params["end"] = end_timestamp
            
        response = self.client.get(
            urljoin(self.base_url, f"/v1/klines/{market}/{interval}/{symbol}"),
            params=params, timeout=None
        )
        df = DataFrame(response.json()['data'])
        df['timestamp'] = df['timestamp'] // 1000
        df['open_datetime'] = pd.to_datetime(df['timestamp'], unit='s')
        return df

    def get_funding_rate(self, symbol: str, start_timestamp: int = None, end_timestamp: int = None, limit: int = 10) -> DataFrame:
        """
        get: unix_time + funding rate data , as pandas dataframe
        symbol have to be in capital case e.g. (BTCUSDT)
        start_timestamp and end_timestamp are optional
        """
        params = {"limit": limit}
        if start_timestamp is not None:
            params["start"] = start_timestamp
        if end_timestamp is not None:
            params["end"] = end_timestamp

        response = self.client.get(
            urljoin(self.base_url, f"/v1/klines/funding_rates/{symbol}"),
            params=params, timeout=None
        )
        df = DataFrame(response.json()['data'])
        return df
    
    def list_orders(self) -> DataFrame:
        response = self.client.get(
            urljoin(self.base_url, "/v1/trade/orders"),
            headers={"Authorization": f"Bearer {self.api_key}"},
        )
        return DataFrame(response.json())
    
    def get_enabled_bots(self) -> DataFrame:
        response = self.client.get(
            urljoin(self.base_url, "/v1/trade/bots/enabled"),
            headers={"Authorization": f"Bearer {self.api_key}"},
        )
        data = response.json()
        return {
            "bots": DataFrame(data["bots"]),
            "api_keys": DataFrame(data["api_keys"])
        }
    
    # Get all keywords available for Google Trends
    def get_google_trend_keywords_available(self) -> DataFrame:
        response = self.client.get(
            urljoin(self.base_url, "/v1/google/keywords"),
        )
        df = pd.DataFrame(response.json())
        return df

    # Get Google Trends data for a specific keyword
    def get_google_trend_keyword(self, keyword: str, timeframe: str = '8m', limit: int = 100) -> DataFrame:
        """
        Retrieves Google Trends data for a specific keyword.

        Args:
            keyword (str): The keyword to retrieve Google Trends data for.
            timeframe (str, optional): The timeframe for the data. Defaults to '8m'.
            limit (int, optional): The maximum number of data points to retrieve. Defaults to 100.

        Returns:
            DataFrame: A pandas DataFrame containing the Google Trends data.

        """
        response = self.client.get(
            urljoin(self.base_url, f"/v1/google/trends/{keyword}"),
            params={"timeframe": timeframe, "limit": limit},
        )
        df = pd.DataFrame(response.json()['data'])
        df.rename(columns={"values": "trend_val", "timestamps": "timestamp"}, inplace=True)
        return df

    def get_historical_marketcap(self, symbol: str, start_date: str = None, end_date: str = None, limit: int = None) -> DataFrame:
        """
        Retrieves historical market cap data for a specific symbol.

        Args:
            symbol (str): The symbol to retrieve historical market cap data for.
            start_date (str, optional): The start date for the data. Defaults to None.
            end_date (str, optional): The end date for the data. Defaults to None.
            limit (int, optional): The maximum number of data points to retrieve. Defaults to None.

        Returns:
            DataFrame: A pandas DataFrame containing the historical market cap data.

        """
        response = self.client.get(
            urljoin(self.base_url, f"/v1/market/market-cap/{symbol}"),
            params={"start_date": start_date, "end_date": end_date, "limit": limit},
        )
        df = pd.DataFrame(response.json())
        return df
    
    def get_hist_marketcap_coins(self, limit=100, offset=0):
        """
        Retrieves coin data.

        Args:
            limit (int, optional): The maximum number of coins to retrieve. Defaults to 100.
            offset (int, optional): The offset for the data. Defaults to 0. Should be used for pagination.

        Returns:
            DataFrame: A pandas DataFrame containing the coin data.

        """
        response = self.client.get(
            urljoin(self.base_url, f"/v1/market/coins?limit={limit}&offset={offset}"),
        )
        next_offset = response.json()['offset']
        df = pd.DataFrame(response.json()['coins'])
        return next_offset, df

    def get_exchange_all_symbols(self, exchange_name: str) -> DataFrame:
        """Exchange names to be added as follows: 
        Binance, KuCoin, Gate.io, Bybit, Bingx, Bitget
        """
        response = self.client.get(
            urljoin(self.base_url, f"/v1/market/exchange-data/{exchange_name}"),
        )
        df = pd.DataFrame(response.json())
        return df

    def get_symbol_info_exchange(self, exchange_name: str, symbol: str, market: str = 'spot') -> DataFrame:
        """
        Exchange names to be added as follows: 
        Binance, KuCoin, Gate.io, Bybit, Bingx, Bitget

        Exchange symbols to be added as follows:
        Spot -> BTC-USDT, ETH-USDT, LTC-USDT
        Futures -> BTC-USDT-USDT, ETH-USDT-USDT, LTC-USDT-USDT
        """
        if market == 'futures':
            symbol = symbol + '-USDT'
        response = self.client.get(
            urljoin(self.base_url, f"/v1/market/exchange-data/{exchange_name}/{symbol}"),
        )
        df = pd.DataFrame(response.json())
        return df
    
    def get_cnn_sentiment(self, indicator_name: str, start_date: str = None, end_date: str = None, limit: int = None) -> DataFrame:
        """
        Retrieves Fear and Greed Index data for a specific indicator name.

        Args:
            indicator_name (str): The indicator name / keyword to retrieve Fear and Greed Index data for.
            start_date (str, optional): The start date for the data. Defaults to None.
            end_date (str, optional): The end date for the data. Defaults to None.
            limit (int, optional): The maximum number of data points to retrieve. Defaults to None.

        Returns:
            DataFrame: A pandas DataFrame containing the Fear and Greed Index data.

        """
        response = self.client.get(
            urljoin(self.base_url, f"/v1/market/fng-index/{indicator_name}"),
            params={"start_date": start_date, "end_date": end_date, "limit": limit},
        )
        df = pd.DataFrame(response.json())
        return df

    def get_cnn_keywords(self) -> DataFrame:
        response = self.client.get(
            urljoin(self.base_url, "/v1/market/fng-index/list-indicators"),
        )
        df = pd.DataFrame(response.json())
        df.columns = ['indicator_name']
        return df

    def verify(self, token: Union[str, None] = None) -> bool:
        if token is None:
            token = self.token
        response = self.client.get(
            self.base_url + "/v1/auth/verify",
            headers={"Authorization": f"Bearer {token}"},
        )
        response.raise_for_status()
        try:
            res = response.json()
            return res['result']['data']['json']
        except:
            return None

# testing
if __name__ == "__main__":
    client = ApiClient(
        base_url=os.getenv("CRYPTICORN_API_URL", "https://api.crypticorn.dev"),
        api_key="REDACTED",
    )
    print("")
    print("Economics News")
    print("->")
    print(client.get_economics_news(5))
    print("")
    print("Bitcoin Historical Data")
    print("->")
    # try 250000 there is no timeout
    print(client.get_bc_historical("BTCUSDT", "15m", 25))
    print("")
    print("Fear and Greed Index Historical Data")
    print("->")
    print(client.get_fgi_historical(5))
    print("")
    print("Get UDF History")
    print("->")
    print(client.get_udf_history("BTCUSDT", 25))
    # print("")
    # print("Post Trend Data")
    # print("->")
    # print(
    #     client.post_trend(
    #         TrendData(
    #             timestamps=[4, 8, 12, 16, 24, 32, 48, 64],
    #             positive_prob=[0.1, 0.9, 0.2, 0.8, 0.3, 0.7, 0.4, 0.6],
    #             symbol="BTCUSDT",
    #             version="1",
    #         )
    #     )
    # )
    # # query trend data
    # print("Get Trend Data")
    # print("->")
    # print(
    #     client.get_trends(
    #         TrendQuery(
    #             symbol="BTCUSDT",
    #             limit=10,
    #             offset=0,
    #             sort="timestamp",
    #             dir="desc",
    #             from_ts=1613225600,
    #             to_ts=1812793600,
    #         )
    #     )
    # )
    print("Kline Service")
    print("->")
    print("Kline Symbols for Futures")
    print("->")
    print(client.get_symbols("futures"))
    print("Kline Symbols for Spot")
    print("->")
    print(client.get_symbols("spot"))
    print("Futures Klines")
    print("->")
    print(client.get_klines("futures", "BTCUSDT", "1m", 100))
    print("Spot Klines")
    print("->")
    print(client.get_klines("spot", "BTCUSDT", "1m", 100))
    print("")
    print("Funding Rate")
    print("->")
    print(client.get_funding_rate(symbol="BTCUSDT"))
    # print("Enabled Bots")
    # print("->")
    # bots_result = client.get_enabled_bots()
    # print(bots_result["bots"])
    # print("")
    # print("API Keys")
    # print(bots_result["api_keys"])
    print("Get Keywords for Google Trends")
    print("->")
    print(client.get_google_trend_keywords_available())
    print("Google Trend Keyword")
    print("->")
    print(client.get_google_trend_keyword("Bitcoin", limit=10000))
    print("Coins")
    print("->")
    next_offset, coins = client.get_hist_marketcap_coins(limit=100)
    print(f"Next Offset for Pagination: {next_offset}")
    print(coins)
    print("Historical Market Cap")
    print("->")
    print(client.get_historical_marketcap("BTC", limit=10))
    print("Exchange Data")
    print("->")
    print(client.get_exchange_all_symbols("Binance"))
    print("Exchange Spot Symbol")
    print("->")
    print(client.get_symbol_info_exchange("Binance", "BTC-USDT", "spot"))
    print("Exchange Futures Symbol")
    print("->")
    print(client.get_symbol_info_exchange("Binance", "BTC-USDT", "futures"))
    print("CNN Fear and Greed Indicators")
    print("->")
    print(client.get_cnn_keywords())
    print("Fear and Greed Index for all Indicators")
    print("->")
    for index, row in client.get_cnn_keywords().iterrows():
        print(client.get_cnn_sentiment(row['indicator_name'], limit=10))