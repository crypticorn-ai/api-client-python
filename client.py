import httpx
import pandas as pd
from pandas import DataFrame
from pydantic import BaseModel
from typing import Optional, Union, List
from urllib.parse import urljoin
from datetime import datetime
import requests

from python.models import FuturesTradingAction
from .public.crypticorn import Crypticorn
from .public.crypticorn.utils import SingleModel, AccountInfo, ApiKeyGeneration, AllModels
from datetime import timedelta

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

default_version = "1.5"

class ApiClient:
    def __init__(
        self, base_url: str = "https://api.crypticorn.com", api_key: str = None, token: str = None
    ):
        self.base_url = base_url
        self.api_key = api_key
        self.token = token
        self.client = httpx.Client()
        self.hive = HiveClient(api_key)

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
    
    async def post_futures_action(self, signal: FuturesTradingAction):
        url = f"{self.base_url}/v1/trade/actions/futures"
        token = self.api_key
        headers = {"Authorization": f"Bearer {token}"}
        print(f"Posting futures action to {url} with signal: {signal}")
        try:
            async with httpx.AsyncClient(timeout=30) as http_client:
                response = await http_client.post(
                    url, headers=headers, json=signal.model_dump()
                )
            print(f"Response: {response}")
            response.raise_for_status()
            data = response.json()
            print(f"Saved futures action: {data}")
            return data
        except httpx.HTTPStatusError as e:
            error_detail = ""
            try:
                error_detail = e.response.json()
            except Exception:
                error_detail = e.response.text
            print(f"HTTP error occurred: {e.response.text}. Details: {error_detail}")
        except httpx.RequestError as e:
            print(f"Request failed: {e.request.method} {e.request.url} - {e}")
        return []

    # -------------------- START OF DATA PLATFORM SERVICE ------------------------ #
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

    def get_latest_predictions(self, version: str = default_version) -> DataFrame:
        response = self.client.get(
            urljoin(self.base_url, f"/v1/predictions/latest?version={version}"),
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

    def get_prediction(self, pair: str, version: str = default_version, limit: int = 1) -> PredictionData:
        response = self.client.get(
            urljoin(self.base_url, f"/v1/predictions/symbol/{pair}?version={version}&limit={limit}"),
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

    # -------------------- END OF DATA PLATFORM SERVICE ------------------------ #

    # -------------------- START OF KLINE SERVICE ------------------------ #
    def get_symbols(self, market: str) -> DataFrame:
        """
        get: symbol for futures or spot, as pandas dataframe
        market: futures or spot

        Returns:
            DataFrame: A pandas DataFrame containing the symbols with columns:
                - symbol: str (the trading pair symbol)
        """
        response = self.client.get(
            urljoin(self.base_url, f"/v1/klines/symbols/{market}"), timeout=None
        )
        if response.status_code == 200:
            json_response = response.json()
            if json_response.get("success"):
                # Convert the array of symbols to a DataFrame with a 'symbol' column
                df = DataFrame(json_response["data"], columns=["symbol"])
                return df
            else:
                raise Exception(f"API returned error: {json_response.get('message')}")
        else:
            raise Exception(f"Failed to get symbols: {response.json()}")

    def get_klines(self, market: str, symbol: str, interval: str, limit: int, start_timestamp: int = None, end_timestamp: int = None, sort: str = "desc") -> DataFrame:
        """
        get: unix_time + OHLCV data , as pandas dataframe
        symbol have to be in capital case e.g. (BTCUSDT)
        market: futures or spot
        interval: 1m, 3m, 5m, 15m, 30m, 1h, 4h, 1d

        Returns:
            DataFrame: A pandas DataFrame containing OHLCV data with columns:
                - timestamp: datetime
                - open: float
                - high: float
                - low: float
                - close: float
                - volume: float
        """
        params = {"limit": limit}
        if start_timestamp is not None:
            params["start"] = start_timestamp
        if end_timestamp is not None:
            params["end"] = end_timestamp
        if sort is not None:
            params["sort_direction"] = sort

        response = self.client.get(
            urljoin(self.base_url, f"/v1/klines/{market}/{interval}/{symbol}"),
            params=params, timeout=None
        )
        if response.status_code == 200:
            json_response = response.json()
            if json_response.get("success"):
                # Extract the nested data structure
                data = json_response["data"]
                # Create DataFrame from the arrays
                df = DataFrame({
                    "timestamp": data["timestamp"],
                    "open": data["open"],
                    "high": data["high"],
                    "low": data["low"],
                    "close": data["close"],
                    "volume": data["volume"]
                })
                # Convert timestamp strings to datetime then to unix timestamp
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                df['timestamp'] = df['timestamp'].astype("int64") // 10 ** 9  # use int64 instead of int for windows
                return df
            else:
                raise Exception(f"API returned error: {json_response.get('message')}")
        else:
            raise Exception(f"Failed to get klines: {response.json()}")
    
    def get_funding_rate(self, symbol: str, start_timestamp: int = None, end_timestamp: int = None, limit: int = 2000) -> DataFrame:
        """
        Get funding rate data for a specific symbol.

        Args:
            symbol (str): Trading pair symbol in capital case (e.g., 'BTCUSDT')
            start_timestamp (int, optional): Start time in unix timestamp
            end_timestamp (int, optional): End time in unix timestamp
            limit (int, optional): Number of records to return. Defaults to 2000.

        Returns:
            DataFrame: A pandas DataFrame containing funding rate data with columns:
                - symbol: str
                - timestamp: datetime
                - funding_rate: float
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
        if response.status_code == 200:
            json_response = response.json()
            if json_response.get("success"):
                # Create DataFrame from the data array
                df = DataFrame(json_response["data"])
                # Convert timestamp strings to datetime then to unix timestamp
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                df['timestamp'] = df['timestamp'].astype("int64") // 10 ** 9  # use int64 instead of int for windows
                return df
            else:
                raise Exception(f"API returned error: {json_response.get('message')}")
        else:
            raise Exception(f"Failed to get funding rates: {response.json()}")
    
    # -------------------- END OF KLINE SERVICE ------------------------ #
    
    # -------------------- START OF TRADE SERVICE ------------------------ #
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
    
    # -------------------- END OF TRADE SERVICE ------------------------ #
    
    # -------------------- START OF GOOGLE TRENDS ------------------------ #
    # Get all keywords available for Google Trends
    def get_google_trend_keywords_available(self) -> DataFrame:
        response = self.client.get(
            urljoin(self.base_url, "/v1/google/keywords"),
        )
        if response.status_code == 200:
            df = pd.DataFrame(response.json())
            return df
        else:
            raise Exception(f"Failed to get google trends keywords available: {response.json()}")

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
            params={"timeframe": timeframe, "limit": limit}, timeout=None
        )
        if response.status_code == 200:
            df = pd.DataFrame(response.json()['data'])
            df.rename(columns={"values": "trend_val", "timestamps": "timestamp"}, inplace=True)
            return df
        else:
            raise Exception(f"Failed to get google trends: {response.json()}")

    # -------------------- END OF GOOGLE TRENDS ------------------------ #
    
    # -------------------- START OF MARKET SERVICE ------------------------ #
    def get_exchange_all_symbols(self, exchange_name: str) -> DataFrame:
        """Exchange names to be added as follows: 
        Binance, KuCoin, Gate.io, Bybit, Bingx, Bitget
        """
        if exchange_name not in ['Binance', 'KuCoin', 'Gate.io', 'Bybit', 'Bingx', 'Bitget']:
            raise ValueError("Invalid exchange name it needs to be one of the following: Binance, KuCoin, Gate.io, Bybit, Bingx, Bitget")
        response = self.client.get(
            urljoin(self.base_url, f"/v1/market/exchange-data/{exchange_name}"), timeout=None
        )
        if response.status_code == 200:
            df = pd.DataFrame(response.json())
            return df
        else:
            raise Exception(f"Failed to get exchange all symbols: {response.json()}")

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
            urljoin(self.base_url, f"/v1/market/exchange-data/{exchange_name}/{symbol}"), timeout=None
        )
        if response.status_code == 200:
            df = pd.DataFrame(response.json())
            return df
        else:
            raise Exception(f"Failed to get symbol info: {response.json()}")
    
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
            params={"start_date": start_date, "end_date": end_date, "limit": limit}, timeout=None
        )
        if response.status_code == 200:
            df = pd.DataFrame(response.json())
            return df
        else:
            raise Exception(f"Failed to get cnn sentiment: {response.json()}")

    def get_cnn_keywords(self) -> DataFrame:
        response = self.client.get(
            urljoin(self.base_url, "/v1/market/fng-index/list-indicators"), timeout=None
        )
        if response.status_code == 200:
            df = pd.DataFrame(response.json())
            df.columns = ['indicator_name']
            return df
        else:
            raise Exception(f"Failed to get cnn keywords: {response.json()}")
    
    def get_economic_calendar_events(self, start_timestamp: int = None, end_timestamp: int = None, currency: str = 'EUR', country_code: str = 'DE') -> DataFrame:
        """
        Function returns a pandas dataframe with the economic calendar events for the specified currency and country code during given time period.
        currency: EUR, CNY, NZD, AUD, USD, JPY, UAH, GBP, CHF, CAD
        country_code: CA, UA, ES, US, FR, JP, IT, NZ, AU, CN, UK, CH, EMU, DE
        """
        start_date = None
        end_date = None
        if isinstance(start_timestamp, int):
            start_date = pd.to_datetime(start_timestamp, unit='s').strftime('%Y-%m-%d')
        if isinstance(end_timestamp, int):
            end_date = pd.to_datetime(end_timestamp, unit='s').strftime('%Y-%m-%d')
            
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "currency": currency,
            "country_code": country_code
        }
        response = self.client.get(
            urljoin(self.base_url, f"/v1/market/ecocal"), timeout=None, params=params
        )
        if response.status_code == 200:
            df = pd.DataFrame(response.json())
            return df
        else:
            raise Exception(f"Failed to get economic calendar events: {response.json()}")
    
    def get_bitstamp_symbols(self) -> List[str]:
        response = self.client.get(
            urljoin(self.base_url, f"/v1/market/bitstamp/symbols"), timeout=None
        )
        if response.status_code == 200:
            symbols = response.json()
            # convert all symbols to uppercase
            symbols = [symbol.upper() for symbol in symbols]
            return symbols
        else:
            raise Exception(f"Failed to get bitstamp symbols: {response.json()}")
    
    def get_bitstamp_ohlcv_spot(self, symbol: str,  interval: str, limit: int, start_timestamp: int = None, end_timestamp: int = None) -> DataFrame:
        """
        get: unix_time + OHLCV data , as pandas dataframe
        symbol have to be in capital case e.g. (BTCUSDT)
        interval: 15m, 30m, 1h, 4h, 1d
        """
        params = {"limit": limit}
        if start_timestamp is not None:
            params["start"] = start_timestamp
        if end_timestamp is not None:
            params["end"] = end_timestamp
            
        response = self.client.get(
            urljoin(self.base_url, f"/v1/market/bitstamp/{symbol}/{interval}"),
            params=params, timeout=None
        )
        if response.status_code == 200: 
            df = DataFrame(response.json())
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['timestamp'] = df['timestamp'].astype("int64") // 10 ** 9 # use int64 instead of int for windows
            return df
        else:
            raise Exception(f"Failed to get bitstamp ohlcv spot: {response.json()}")
        
    # -------------------- END OF MARKET SERVICE ------------------------ #
    
    # -------------------- START OF MARKETCAP METRICS SERVICE ------------------------ #
    # Get historical marketcap rankings for coins
    def get_historical_marketcap_rankings(self, start_timestamp: int = None, end_timestamp: int = None, interval: str = "1d", market: str = None, exchange_name: str = None) -> DataFrame:
        """
        Get historical marketcap rankings and exchange availability for cryptocurrencies.
        
        Args:
            start_timestamp (int, optional): Start timestamp for the data range
            end_timestamp (int, optional): End timestamp for the data range
            interval (str, optional): Time interval between data points (e.g. "1d")
            market (str, optional): Market type (e.g. "futures")
            exchange_name (str, optional): Exchange name (e.g. "binance", "kucoin", "gate.io", "bybit", "bingx", "bitget")
            
        Returns:
            DataFrame: A pandas DataFrame containing the historical marketcap rankings where:
                - First column is timestamp
                - Subsequent columns represent symbol rankings (e.g., BTCUSDT, ETHUSDT, etc.)
                - null values indicate the symbol was not ranked at that timestamp
        """
        response = self.client.get(
            urljoin(self.base_url, f"/v1/metrics/marketcap/symbols"), 
            timeout=None,
            params={
                "start_timestamp": start_timestamp, 
                "end_timestamp": end_timestamp, 
                "interval": interval,
                "market": market,
                "exchange": exchange_name
            }
        )
        
        if response.status_code == 200:
            json_response = response.json()
            if json_response.get("success"):
                # Create DataFrame from the data array
                df = pd.DataFrame(json_response["data"])
                # Rename first column to timestamp
                df.rename(columns={df.columns[0]: 'timestamp'}, inplace=True)
                # Convert timestamp strings to unix timestamp
                df['timestamp'] = pd.to_datetime(df['timestamp']).astype("int64") // 10 ** 9
                return df
            else:
                raise Exception(f"API returned error: {json_response.get('message')}")
        else:
            raise Exception(f"Failed to get historical marketcap rankings: {response.json()}")
    
    def get_historical_marketcap_values_for_rankings(self, start_timestamp: int = None, end_timestamp: int = None) -> DataFrame:
        """
        Get historical marketcap values for rankings.

        Args:
            start_timestamp (int, optional): Start timestamp for the data range
            end_timestamp (int, optional): End timestamp for the data range

        Returns:
            DataFrame: A pandas DataFrame containing marketcap values where:
                - First column is timestamp
                - Subsequent columns represent marketcap values for each ranking position (1-150)
                - Values are in USD
        """
        response = self.client.get(
            urljoin(self.base_url, f"/v1/metrics/marketcap"), 
            timeout=None, 
            params={"start_timestamp": start_timestamp, "end_timestamp": end_timestamp}
        )
        if response.status_code == 200:
            json_response = response.json()
            if json_response.get("success"):
                # Create DataFrame from the data array
                df = pd.DataFrame(json_response["data"])
                # Rename first column to timestamp
                df.rename(columns={df.columns[0]: 'timestamp'}, inplace=True)
                # Convert timestamp strings to unix timestamp
                df['timestamp'] = pd.to_datetime(df['timestamp']).astype("int64") // 10 ** 9
                return df
            else:
                raise Exception(f"API returned error: {json_response.get('message')}")
        else:
            raise Exception(f"Failed to get historical marketcap values for rankings: {response.json()}")
    
    def get_marketcap_indicator_values(self, symbol: str, market: str, period: int, indicator_name: str, timestamp: int = None) -> float:
        """
        Get marketcap indicator values for a specific indicator name and timestamp.

        Args:
            symbol (str): Trading pair symbol (e.g., 'BTCUSDT')
            market (str): Market type (e.g., 'spot', 'futures')
            period (int): Period for the indicator calculation
            indicator_name (str): Name of the indicator ('ker' or 'sma')
            timestamp (int, optional): Timestamp for the data point. Defaults to None.

        Returns:
            float: The indicator value for the specified parameters

        Raises:
            Exception: If the API request fails or returns an error
        """
        response = self.client.get(
            urljoin(self.base_url, f"/v1/metrics/{indicator_name}/{symbol}"), 
            timeout=None, 
            params={
                "market": market, 
                "period": period, 
                "timestamp": timestamp
            }
        )
        if response.status_code == 200:
            json_response = response.json()
            if json_response.get("success"):
                # Extract the indicator value from the data object
                return json_response["data"][indicator_name]
            else:
                raise Exception(f"API returned error: {json_response.get('message')}")
        else:
            raise Exception(f"Failed to get marketcap indicator values: {response.json()}")
    
    def get_exchanges_for_mc_symbol(self, symbol: str, market: str, interval: str = '1d', start_timestamp: int = None, end_timestamp: int = None, status: str = 'ACTIVE', quote_currency: str = 'USDT') -> DataFrame:
        """
        Get exchange availability for a specific symbol over time.

        Args:
            symbol (str): Trading pair symbol (e.g., 'BTC')
            market (str): Market type (e.g., 'spot', 'futures')
            interval (str, optional): Time interval between data points. Defaults to '1d'.
            start_timestamp (int, optional): Start timestamp for the data range
            end_timestamp (int, optional): End timestamp for the data range
            status (str, optional): Status of the exchanges ('ACTIVE' or 'RETIRED'). Defaults to 'ACTIVE'.
            quote_currency (str, optional): Quote currency for the pair. Defaults to 'USDT'.

        Returns:
            DataFrame: A pandas DataFrame containing exchange availability with columns:
                - timestamp: datetime
                - binance: bool
                - bitget: bool
                - bybit: bool
                - kucoin: bool
                (columns are sorted alphabetically)
        """
        if start_timestamp is None:
            start_timestamp = int((datetime.now() - timedelta(days=7, hours=0, minutes=0, seconds=0)).timestamp())
        if end_timestamp is None:
            end_timestamp = int((datetime.now() - timedelta(days=0, hours=0, minutes=0, seconds=0)).timestamp())
            
        params = {
            "interval": interval,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "status": status,
            "quote_currency": quote_currency
        }

        response = self.client.get(
            urljoin(self.base_url, f"/v1/metrics/available_exchanges/{market}/{symbol}"), 
            timeout=None, 
            params=params
        )
        if response.status_code == 200:
            json_response = response.json()
            if json_response.get("success"):
                # Process the data array into a DataFrame
                processed_results = []
                for row in json_response["data"]:
                    data = {'timestamp': row['timestamp']}
                    data.update(row['exchanges'])
                    processed_results.append(data)
                
                # Create DataFrame and sort columns
                df = pd.DataFrame(processed_results)
                cols = ['timestamp'] + sorted([col for col in df.columns if col != 'timestamp'])
                df = df[cols]
                
                # Convert timestamp to unix timestamp
                df['timestamp'] = pd.to_datetime(df['timestamp']).astype("int64") // 10 ** 9
                
                # Convert exchange availability to boolean integers (0/1)
                df = df.astype({'timestamp': 'int64', **{col: 'int8' for col in df.columns if col != 'timestamp'}})
                return df
            else:
                raise Exception(f"API returned error: {json_response.get('message')}")
        else:
            raise Exception(f"Failed to get exchanges for mc symbol: {response.json()}")
    
    def get_marketcap_ranking_with_ohlcv(self, market: str, timeframe: str, top_n: int, ohlcv_limit: int, 
                                        timestamp: int = int((datetime.now() - timedelta(days=1, hours=0, minutes=0, seconds=0)).timestamp())) -> dict:
        """
        Get marketcap rankings with OHLCV data for top symbols.

        Args:
            market (str): Market type (e.g., 'spot', 'futures')
            timeframe (str): Time interval for OHLCV data (e.g., '1h', '4h', '1d')
            top_n (int): Number of top symbols to retrieve
            ohlcv_limit (int): Number of OHLCV data points to retrieve
            timestamp (int, optional): Timestamp for the ranking snapshot. 
                                    Defaults to 24 hours ago.

        Returns:
            dict: A dictionary containing:
                - info (str): Request parameters information
                - symbols (List[str]): List of top symbols by marketcap
                - ohlcv (dict): Dictionary of OHLCV data for each symbol with fields:
                    - timestamp: List[str] (ISO format timestamps)
                    - open: List[float]
                    - high: List[float]
                    - low: List[float]
                    - close: List[float]
                    - volume: List[float]

        Raises:
            Exception: If the API request fails or returns an error
        """
        params = {
            "market": market, 
            "timeframe": timeframe, 
            "top_n": top_n, 
            "ohlcv_limit": ohlcv_limit, 
            "timestamp": timestamp
        }
        
        response = self.client.get(
            urljoin(self.base_url, f"/v1/metrics/marketcap/symbols/ohlcv"), 
            timeout=None, 
            params=params
        )
        
        if response.status_code == 200:
            json_response = response.json()
            if json_response.get("success"):
                # Return the first (and only) item from the data array
                return json_response["data"][0]
            else:
                raise Exception(f"API returned error: {json_response.get('message')}")
        else:
            raise Exception(f"Failed to get marketcap ranking with ohlcv: {response.json()}")
    
    def get_stable_or_wrapped_tokens(self, token_type: str = 'stable') -> DataFrame:
        """
        Get list of stable or wrapped tokens.

        Args:
            token_type (str, optional): Type of tokens to retrieve ('stable' or 'wrapped'). 
                                      Defaults to 'stable'.

        Returns:
            DataFrame: A pandas DataFrame containing token information with columns:
                - symbol: str (token symbol e.g., 'USDT', 'USDC')
                - slug: str (token identifier e.g., 'tether', 'usd-coin')

        Raises:
            ValueError: If token_type is not 'stable' or 'wrapped'
            Exception: If the API request fails or returns an error
        """
        if token_type not in ['stable', 'wrapped']:
            raise ValueError("token_type must be either stable or wrapped")
            
        response = self.client.get(
            urljoin(self.base_url, f"/v1/metrics/tokens/{token_type}"), 
            timeout=None
        )
        
        if response.status_code == 200:
            json_response = response.json()
            if json_response.get("success"):
                # Create DataFrame from the data array
                df = pd.DataFrame(json_response["data"])
                return df
            else:
                raise Exception(f"API returned error: {json_response.get('message')}")
        else:
            raise Exception(f"Failed to get stable or wrapped tokens: {response.json()}")
    
    def get_exchanges_mapping_for_specific_symbol(self, market: str, symbol: str, quote_currency: str = 'USDT', status: str = 'ACTIVE') -> DataFrame:
        """
        Get the exchanges and trading pairs information for a specific symbol and market.

        Args:
            market (str): Market type (e.g., 'spot', 'futures')
            symbol (str): Base currency symbol (e.g., 'BTC')
            quote_currency (str, optional): Quote currency for the pair. Defaults to 'USDT'.
            status (str, optional): Status of the trading pairs ('ACTIVE' or 'RETIRED'). Defaults to 'ACTIVE'.

        Returns:
            DataFrame: A pandas DataFrame containing exchange information with columns:
                - exchange_name: str (e.g., 'binance', 'kucoin')
                - symbol: str (base currency symbol)
                - pair: str (actual trading pair on the exchange)
                - quote_currency: str (quote currency used)
                - status: str (trading pair status)
                - first_trade_timestamp: str (ISO format timestamp of first trade)
                - last_trade_timestamp: str (ISO format timestamp of last trade)

        Raises:
            Exception: If the API request fails or returns an error
        """
        params = {
            "quote_currency": quote_currency,
            "status": status
        }
        
        response = self.client.get(
            urljoin(self.base_url, f"/v1/metrics/markets/{market}/{symbol}"), 
            timeout=None,
            params=params
        )
        
        if response.status_code == 200:
            json_response = response.json()
            if json_response.get("success"):
                # Create DataFrame from the data array
                df = pd.DataFrame(json_response["data"])
                return df
            else:
                raise Exception(f"API returned error: {json_response.get('message')}")
        else:
            raise Exception(f"Failed to get exchange mappings: {response.json()}")
    
    def get_exchange_mappings_for_specific_exchange(self, market: str, exchange_name: str) -> DataFrame:
        """
        Get all trading pairs and their information for a specific exchange and market.

        Args:
            market (str): Market type (e.g., 'spot', 'futures')
            exchange_name (str): Name of the exchange (e.g., 'binance', 'kucoin', 'bybit')
                               Should be in lowercase

        Returns:
            DataFrame: A pandas DataFrame containing trading pair information with columns:
                - exchange_name: str (name of the exchange)
                - symbol: str (base currency symbol)
                - quote_currency: str (quote currency used)
                - pair: str (actual trading pair on the exchange)
                - first_trade_timestamp: str (ISO format timestamp of first trade)
                - last_trade_timestamp: str (ISO format timestamp of last trade)
                - status: str ('ACTIVE' or 'RETIRED')
                - market_type: str (type of market e.g., 'spot')

        Raises:
            Exception: If the API request fails or returns an error
        """
        params = {
            "exchange_name": exchange_name.lower()
        }
        
        response = self.client.get(
            urljoin(self.base_url, f"/v1/metrics/exchange_mappings/{market}"), 
            timeout=None, 
            params=params
        )
        
        if response.status_code == 200:
            json_response = response.json()
            if json_response.get("success"):
                # Create DataFrame from the data array
                df = pd.DataFrame(json_response["data"])
                return df
            else:
                raise Exception(f"API returned error: {json_response.get('message')}")
        else:
            raise Exception(f"Failed to get exchange mappings: {response.json()}")
    
    def get_unique_quote_currencies(self, market: str) -> List[str]:
        """
        Get list of unique quote currencies available for a specific market.

        Args:
            market (str): Market type (e.g., 'spot', 'futures')

        Returns:
            List[str]: A list of quote currencies (e.g., ['USDT', 'BTC', 'ETH', ...])

        Raises:
            Exception: If the API request fails or returns an error
        """
        response = self.client.get(
            urljoin(self.base_url, f"/v1/metrics/quote_currencies/{market}"), 
            timeout=None
        )
        
        if response.status_code == 200:
            json_response = response.json()
            if json_response.get("success"):
                return json_response["data"]
            else:
                raise Exception(f"API returned error: {json_response.get('message')}")
        else:
            raise Exception(f"Failed to get unique quote currencies: {response.json()}")
    
    def get_exchanges_list_for_specific_market(self, market: str) -> List[str]:
        """
        Get the list of exchanges available for a specific market.

        Args:
            market (str): Market type (e.g., 'spot', 'futures')

        Returns:
            List[str]: A list of exchange names (e.g., ['binance', 'kucoin', 'bybit', ...])

        Raises:
            Exception: If the API request fails or returns an error
        """
        response = self.client.get(
            urljoin(self.base_url, f"/v1/metrics/exchange_list/{market}"), 
            timeout=None
        )
        
        if response.status_code == 200:
            json_response = response.json()
            if json_response.get("success"):
                return json_response["data"]
            else:
                raise Exception(f"API returned error: {json_response.get('message')}")
        else:
            raise Exception(f"Failed to get exchanges list: {response.json()}")
    
    # -------------------- END OF MARKETCAP METRICS SERVICE ------------------------ #
    
    # -------------------- START OF BINGX KLINES SERVICE ------------------------ #
    
    def get_bingx_symbols(self) -> List[str]:
        response = self.client.get(
            urljoin(self.base_url, f"/v1/bingx/symbols"), timeout=None
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get bingx symbols: {response.json()}")
    
    def get_bingx_klines(self, symbol: str,  interval: str, limit: int, start_timestamp: int = None, end_timestamp: int = None, sort: str = "desc") -> DataFrame:
        """
        get: unix_time + OHLCV data , as pandas dataframe
        symbol have to be in capital case e.g. (BTCUSDT)
        interval: 5m, 15m, 30m, 1h, 4h, 1d
        """
        params = {"limit": limit}
        if start_timestamp is not None:
            params["start"] = start_timestamp
        if end_timestamp is not None:
            params["end"] = end_timestamp
        if sort is not None:
            params["sort"] = sort

        response = self.client.get(
            urljoin(self.base_url, f"/v1/bingx/klines/{symbol}/{interval}"),
            params=params, timeout=None
        )
        if response.status_code == 200:
            df = DataFrame(response.json())
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['timestamp'] = df['timestamp'].astype("int64") // 10 ** 9 # use int64 instead of int for windows
            return df
        else:
            raise Exception(f"Failed to get bingx klines: {response.json()}")
    
    # -------------------- END OF BINGX KLINES SERVICE ------------------------ #
        
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


class HiveClient(Crypticorn):
    """
    An extension of the Crypticorn pip package to interact with the Crypticorn API via the Dashboard.

    Inherits from Crypticorn and provides methods to create accounts, retrieve account
    information, interact with models, regenerate API keys.

    """

    def __init__(self, token: str):
        """
        Initializes the API client with a bearer token.
        :param token: The bearer token to be included in the headers.
        """
        self._headers = {"Authorization": f"Bearer {token}"}
        super().__init__(api_key="", headers=self._headers)

    def create_account(self, username: str = None) -> int:
        """
        Creates a new account with the specified username. Defaults to user id in jwt.
        :param username: The username for the new account.
        :return: The JSON response from the API.
        """
        endpoint = "/account"
        response = requests.post(
            url=self._base_url + endpoint,
            params={"username": username},
            headers=self._headers
        )
        return response.json()

    def update_username(self, username: str) -> int:
        """
        Updates the username of the current account.
        :param username: The new username.
        :return: The JSON response from the API.
        """
        endpoint = "/account"
        response = requests.patch(
            url=self._base_url + endpoint,
            params={"username": username},
            headers=self._headers
        )
        return response.json()

    def get_account_info(self, username: str = None, user_id: str = None) -> AccountInfo:
        """
        Retrieves information about a user (defaults to current user if no params defined).
        :param username: The username of the account.
        :param user_id: The id of the account.
        :return: The JSON response from the API.
        """
        endpoint = "/account"
        response = requests.get(
            url=self._base_url + endpoint,
            params={"username": username, "user_id": user_id},
            headers=self._headers
        )
        return response.json()

    def get_model(self, model_id: int = None) -> Union[SingleModel, AllModels]:
        """
        Retrieves all models or a specific model by id.
        :param model_id: The id of the model to retrieve.
        :return: The JSON response from the API.
        """
        endpoint = "/model"
        response = requests.get(
            url=self._base_url + endpoint,
            params={"model_id": model_id},
            headers=self._headers
        )
        return response.json()
    
    def delete_model(self, model_id: int) -> int:
        """
        Deletes a specific model by id.
        :param model_id: The id of the model to delete.
        :return: The JSON response from the API.
        """
        endpoint = "/model"
        response = requests.delete(
            url=self._base_url + endpoint,
            params={"model_id": model_id},
            headers=self._headers
        )
        return response.json()

    def generate_api_key(self) -> ApiKeyGeneration:
        """
        Generates the API key for the current account.
        :return: The JSON response from the API.
        """
        endpoint = "/apikey"
        response = requests.post(
            url=self._base_url + endpoint,
            headers=self._headers
        )
        return response.json()

    def delete_api_key(self) -> int:
        """
        Deletes the API key for the current account.
        :return: The JSON response from the API.
        """
        endpoint = "/apikey"
        response = requests.delete(
            url=self._base_url + endpoint,
            headers=self._headers
        )
        return response.json()