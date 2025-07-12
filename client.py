import httpx
import pandas as pd
from pandas import DataFrame
from pydantic import BaseModel
from typing import Optional, Union, List
from urllib.parse import urljoin
from datetime import datetime, timedelta
import os
import psycopg2  # PostgreSQL driver
import io  # For efficient COPY

_DB_PARAMS: dict[str, str | None] = {
    "dbname": os.getenv("KLINES_DB_NAME", "postgres"),
    "user": os.getenv("KLINES_DB_USER", "postgres"),
    "password": os.getenv("KLINES_DB_PASSWORD", "F4l77p9bVA7kaalF"),
    "host": os.getenv("KLINES_DB_HOST", "hz.crypticorn.dev"),
    "port": os.getenv("KLINES_DB_PORT", "5480"),
}


def fetch_data_from_postgres(query: str) -> DataFrame:  # type: ignore[name-defined]
    """Run *query* and return a DataFrame with the results."""

    conn = None
    try:
        conn = psycopg2.connect(**_DB_PARAMS)  # type: ignore[arg-type]
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
        return pd.DataFrame(rows, columns=columns)
    finally:
        if conn is not None:
            conn.close()


def _fetch_data_with_copy(query: str) -> DataFrame:  # type: ignore[name-defined]
    """Use PostgreSQL COPY to efficiently stream large query results."""

    output = io.StringIO()
    conn = None
    try:
        conn = psycopg2.connect(**_DB_PARAMS)  # type: ignore[arg-type]
        with conn.cursor() as cur:
            cur.copy_expert(f"COPY ({query}) TO STDOUT WITH CSV HEADER", output)
        output.seek(0)
        return pd.read_csv(output)
    finally:
        if conn is not None:
            conn.close()


def fetch_ohlcv_data(pair: str, timeframe: str, market_type: str, *, limit: int) -> DataFrame:  # type: ignore[name-defined]
    """Return OHLCV rows for *pair* from the time-series tables."""

    table = f"ohlcv_{market_type}_{timeframe}"
    query = (
        f"SELECT timestamp, pair, open, high, low, close, volume "
        f"FROM {table} "
        f"WHERE pair = '{pair}' "
        f"ORDER BY timestamp DESC "
        f"LIMIT {limit}"
    )
    df = _fetch_data_with_copy(query)
    df["timestamp"] = pd.to_datetime(df["timestamp"]).astype("int64") // 10 ** 9
    return df


def fetch_funding_rate_data(pair: str, *, limit: int) -> DataFrame:  # type: ignore[name-defined]
    """Return funding-rate rows for *pair* from the database."""

    query = (
        "SELECT EXTRACT(EPOCH FROM funding_time)::BIGINT AS timestamp, "
        "       symbol AS pair, funding_rate "
        "FROM funding_rate "
        f"WHERE symbol = '{pair}' "
        "ORDER BY funding_time DESC "
        f"LIMIT {limit}"
    )
    return _fetch_data_with_copy(query)


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
        self,
        *,
        base_url: str = os.getenv("CRYPTICORN_API_URL", "https://api.crypticorn.dev"),
        metrics_api_key: str | None = None,
        miners_api_key: str | None = None,
        bearer_token: str | None = None,
    ):
        """Create API client with separate keys for different services.

        Parameters
        ----------
        base_url : str
            Base endpoint (defaults to env *CRYPTICORN_API_URL* or official prod).
        metrics_api_key : str | None
            Key for metrics & klines services (sent via ``x-api-key``).
        miners_api_key : str | None
            Key for miners (FGI) endpoints.
        token : str | None
            Bearer token for private Data-Platform / Trade endpoints.
        """

        self.base_url = base_url.rstrip("/")
        self.metrics_api_key = metrics_api_key or os.getenv("CRYPTICORN_API_KEY")
        self.miners_api_key = miners_api_key or os.getenv("MINERS_API_KEY") or os.getenv("CRYPTICORN_MINERS_API_KEY")
        self.bearer_token = bearer_token

        # Pre-built header dicts for speed
        self._hdr_metrics = {"x-api-key": self.metrics_api_key} if self.metrics_api_key else {}
        self._hdr_miners = {"x-api-key": self.miners_api_key} if self.miners_api_key else {}

        self.client = httpx.Client()

    def get_response(
        self, endpoint: str, params: dict = None, dict_key: str = None
    ) -> Union[DataFrame, dict]:
        full_url = urljoin(self.base_url, "/v1/miners" + endpoint)
        print(full_url)
        print(params)
        try:
            response = self.client.get(full_url, params=params, headers=self._hdr_miners, timeout=None)
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
            headers={"Authorization": f"Bearer {self.miners_api_key}"},
        )
        return response.json()

    def get_latest_predictions(self, version: str = default_version) -> DataFrame:
        response = self.client.get(
            urljoin(self.base_url, f"/v1/predictions/latest?version={version}"),
            headers={"Authorization": f"Bearer {self.miners_api_key}"},
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
            headers={"Authorization": f"Bearer {self.miners_api_key}"},
        )
        return response.json()

    def get_prediction_time(self, id) -> DataFrame:
        response = self.client.get(
            urljoin(self.base_url, f"/v1/predictions/time/{id}"),
            headers={"Authorization": f"Bearer {self.miners_api_key}"},
        )
        arr = response.json()
        return DataFrame(arr)

    def get_udf_history(self, symbol: str, entries: int) -> DataFrame:
        now = int(pd.Timestamp.now().timestamp())
        response = self.client.get(
            urljoin(self.base_url, "/v1/udf/history"),
            headers={"Authorization": f"Bearer {self.miners_api_key}"},
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
            headers={"Authorization": f"Bearer {self.miners_api_key}"},
        )
        return response.json()

    def get_trends(self, query: TrendQuery):
        response = self.client.get(
            urljoin(self.base_url, "/v1/trends"),
            headers={"Authorization": f"Bearer {self.miners_api_key}"},
            params=query.dict(),
        )
        df = DataFrame(response.json())
        return df

    # -------------------- END OF DATA PLATFORM SERVICE ------------------------ #

    # -------------------- START OF KLINE SERVICE ------------------------ #
    def get_symbols(self, market: str) -> DataFrame:
        """Return the list of distinct symbols available for *market* using Postgres.

        The function queries the ohlcv table for the given *market* (``spot`` or
        ``futures``) and the default 15-minute timeframe. It returns a single-
        column DataFrame named ``symbol`` sorted alphabetically.
        """

        if market not in {"spot", "futures"}:
            raise ValueError("market must be either 'spot' or 'futures'")

        query = (
            f"SELECT DISTINCT pair AS symbol "
            f"FROM ohlcv_{market}_15m "
            f"ORDER BY symbol"
        )
        df = fetch_data_from_postgres(query)
        if df is None:
            raise Exception("Failed to fetch symbols from database")
        return df

    def get_klines(
        self,
        market: str,
        symbol: str,
        interval: str,
        limit: int,
        start_timestamp: int | None = None,
        end_timestamp: int | None = None,
        sort: str = "desc",
    ) -> DataFrame:
        """Fetch OHLCV rows for *symbol* directly from Postgres.

        Args:
            market: ``spot`` or ``futures``.
            symbol: Trading pair (e.g. ``BTCUSDT``).
            interval: Timeframe such as ``15m``, ``1h``.
            limit: Maximum number of rows to return.
            start_timestamp: Optional UNIX-seconds lower bound (inclusive).
            end_timestamp: Optional UNIX-seconds upper bound (inclusive).
            sort: ``asc`` or ``desc`` by timestamp. Default **desc**.
        """

        if market not in {"spot", "futures"}:
            raise ValueError("market must be either 'spot' or 'futures'")
        if sort not in {"asc", "desc"}:
            raise ValueError("sort must be 'asc' or 'desc'")

        df = fetch_ohlcv_data(symbol, interval, market, limit=limit)
        if df is None:
            raise Exception("Failed to fetch OHLCV data from database")

        if start_timestamp is not None:
            df = df[df["timestamp"] >= start_timestamp]
        if end_timestamp is not None:
            df = df[df["timestamp"] <= end_timestamp]

        df.sort_values("timestamp", ascending=(sort == "asc"), inplace=True)
        df.reset_index(drop=True, inplace=True)
        return df
    
    def get_funding_rate(
        self,
        symbol: str,
        start_timestamp: int | None = None,
        end_timestamp: int | None = None,
        limit: int = 2000,
    ) -> DataFrame:
        """Retrieve funding-rate rows for *symbol* directly from Postgres."""

        df = fetch_funding_rate_data(symbol, limit=limit)
        if df is None:
            raise Exception("Failed to fetch funding rate data from database")

        if start_timestamp is not None:
            df = df[df["timestamp"] >= start_timestamp]
        if end_timestamp is not None:
            df = df[df["timestamp"] <= end_timestamp]

        df.sort_values("timestamp", ascending=False, inplace=True)
        df.reset_index(drop=True, inplace=True)
        return df
    
    # -------------------- END OF KLINE SERVICE ------------------------ #
    
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
    
    def get_cnn_sentiment(
        self,
        indicator_name: str,
        start_date: str | None = None,
        end_date: str | None = None,
        limit: int | None = None,
    ) -> DataFrame:
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
    
    def get_economic_calendar_events(
        self,
        start_timestamp: int | None = None,
        end_timestamp: int | None = None,
        currency: str = 'USD',
        country_code: str = 'US',
    ) -> DataFrame:
        """
        Fetch economic-calendar events and return as pandas DataFrame.

        Parameters
        ----------
        start_timestamp, end_timestamp : int | None
            Epoch-seconds time window (UTC). If omitted, latest events are returned.
        currency : str
            Currency code filter (e.g. 'USD').
        country_code : str
            ISO country code filter (e.g. 'US').
        """
        # Convert epoch seconds → ISO date (YYYY-MM-DD) expected by public endpoint
        start_date = pd.to_datetime(start_timestamp, unit='s').strftime('%Y-%m-%d') if isinstance(start_timestamp, int) else None
        end_date = pd.to_datetime(end_timestamp, unit='s').strftime('%Y-%m-%d') if isinstance(end_timestamp, int) else None

        params: dict = {
            "start_date": start_date,
            "end_date": end_date,
            "currency": currency,
            "country_code": country_code,
        }

        # Call the public market endpoint (no auth required, but metrics key also works)
        response = self.client.get(
            urljoin(self.base_url, "/v1/market/ecocal"),
            params=params,
            headers=self._hdr_metrics,
            timeout=None,
        )
        if response.status_code != 200:
            raise Exception(f"Failed to get economic calendar events: {response.text}")

        obj = response.json()

        # Harmonise to a flat list of event dicts
        if isinstance(obj, list):
            events = obj
        elif isinstance(obj, dict):
            events = obj.get("data") or obj.get("events") or [obj]
            if not isinstance(events, list):
                events = [events]
        else:
            events = []

        # Convert to DataFrame (empty DataFrame if no events)
        df = pd.DataFrame(events)
        if df.empty:
            return df

        # Normalise column names to lowercase for convenience
        df.rename(columns=lambda c: c.lower(), inplace=True)

        # Convert ISO start time → epoch seconds timestamp column
        if "start" in df.columns:
            df["timestamp"] = pd.to_datetime(df["start"], utc=True).astype("int64") // 10 ** 9

        # Sort by start time descending (most recent first)
        if "timestamp" in df.columns:
            df.sort_values("timestamp", ascending=False, inplace=True)

        return df
    
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
    def get_historical_marketcap_rankings(
        self,
        start_timestamp: int | None = None,
        end_timestamp: int | None = None,
        interval: str = "1d",
        market: str | None = None,
        exchange_name: str | None = None,
    ) -> DataFrame:
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
            urljoin(self.base_url, "/v1/metrics/marketcap/symbols"),
            timeout=None,
            params={
                "start_timestamp": start_timestamp,
                "end_timestamp": end_timestamp,
                "interval": interval,
                "market": market,
                "exchange": exchange_name,
            },
            headers=self._hdr_metrics,
        )

        if response.status_code != 200:
            raise Exception(f"Failed to get historical marketcap rankings: {response.json()}")

        obj = response.json()

        # New public API returns plain list
        if isinstance(obj, list):
            rows = []
            for item in obj:
                row = {"timestamp": item["timestamp"]}
                row.update({i + 1: sym for i, sym in enumerate(item.get("symbols", []))})
                rows.append(row)
            df = pd.DataFrame(rows)
            return df

        # Legacy wrapper {success:bool,data:[...]} fallback
        if isinstance(obj, dict) and obj.get("success"):
            df = pd.DataFrame(obj["data"])
            df.rename(columns={df.columns[0]: "timestamp"}, inplace=True)
            df["timestamp"] = pd.to_datetime(df["timestamp"]).astype("int64") // 10**9
            return df

        raise Exception("Unexpected response format for marketcap rankings")
    
    def get_historical_marketcap_values_for_rankings(
        self,
        start_timestamp: int | None = None,
        end_timestamp: int | None = None,
    ) -> DataFrame:
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
            urljoin(self.base_url, "/v1/metrics/marketcap"),
            timeout=None,
            params={"start_timestamp": start_timestamp, "end_timestamp": end_timestamp},
            headers=self._hdr_metrics,
        )

        if response.status_code != 200:
            raise Exception(f"Failed to get historical marketcap values for rankings: {response.json()}")

        obj = response.json()

        if isinstance(obj, list):
            rows = []
            for row in obj:
                rows.append({"timestamp": row["timestamp"], **{i+1: v for i, v in enumerate(row.get("values", []))}})
            return pd.DataFrame(rows)

        if isinstance(obj, dict) and obj.get("success"):
            df = pd.DataFrame(obj["data"])
            df.rename(columns={df.columns[0]: "timestamp"}, inplace=True)
            df["timestamp"] = pd.to_datetime(df["timestamp"]).astype("int64") // 10**9
            return df

        raise Exception("Unexpected response format for marketcap values")
    
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
            params={"market": market, "period": period, "timestamp": timestamp},
            headers=self._hdr_metrics,
        )

        if response.status_code != 200:
            raise Exception(f"Failed to get marketcap indicator values: {response.json()}")

        obj = response.json()

        if isinstance(obj, dict) and indicator_name in obj:
            return obj[indicator_name]
        if isinstance(obj, dict) and obj.get("success"):
            return obj["data"].get(indicator_name)
        raise Exception("Unexpected response format for indicator values")
    
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
            urljoin(self.base_url, "/v1/metrics/exchanges/available"),
            timeout=None,
            params={
                **params,
                "market": market,
                "symbol": symbol,
            },
            headers=self._hdr_metrics,
        )

        if response.status_code != 200:
            raise Exception(f"Failed to get exchanges for mc symbol: {response.json()}")

        obj = response.json()

        if isinstance(obj, list):
            processed = []
            for row in obj:
                r = {"timestamp": row["timestamp"]}
                r.update(row.get("exchanges", {}))
                processed.append(r)
            df = pd.DataFrame(processed)
        elif isinstance(obj, dict) and obj.get("success"):
            processed = []
            for row in obj["data"]:
                r = {"timestamp": row["timestamp"]}
                r.update(row["exchanges"])
                processed.append(r)
            df = pd.DataFrame(processed)
        else:
            raise Exception("Unexpected response format for exchange availability")

        cols = ["timestamp"] + sorted([c for c in df.columns if c != "timestamp"])
        df = df[cols]
        df["timestamp"] = pd.to_datetime(df["timestamp"]).astype("int64") // 10**9
        return df
    
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
            urljoin(self.base_url, "/v1/metrics/marketcap/symbols/ohlcv"), 
            timeout=None, 
            params=params,
            headers=self._hdr_metrics,
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
        if token_type not in ["stable", "wrapped", "stables"]:
            raise ValueError("token_type must be either stable or wrapped")
            
        endpoint = "stables" if token_type.startswith("stable") else "wrapped"
            
        response = self.client.get(
            urljoin(self.base_url, f"/v1/metrics/tokens/{endpoint}"),
            headers=self._hdr_metrics,
            timeout=None,
        )

        if response.status_code != 200:
            raise Exception(f"Failed to get stable or wrapped tokens: {response.json()}")

        obj = response.json()

        if isinstance(obj, list):
            return pd.DataFrame(obj)
        if isinstance(obj, dict) and obj.get("success"):
            return pd.DataFrame(obj["data"])
        raise Exception("Unexpected response format for tokens list")
    
    def get_exchange_mappings_for_specific_symbol(self, market: str, symbol: str, quote_currency: str = 'USDT', status: str = 'ACTIVE') -> DataFrame:
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
            urljoin(self.base_url, "/v1/metrics/exchanges/mappings"),
            timeout=None,
            params={"market": market, **params},
            headers=self._hdr_metrics,
        )
        
        if response.status_code != 200:
            raise Exception(f"Failed to get exchange mappings: {response.json()}")

        obj = response.json()
        if isinstance(obj, list):
            return pd.DataFrame(obj)
        if isinstance(obj, dict) and obj.get("success"):
            return pd.DataFrame(obj["data"])
        raise Exception("Unexpected response format for exchange mappings")
    
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
            urljoin(self.base_url, "/v1/metrics/quote-currencies"),
            params={"market": market},
            headers=self._hdr_metrics,
            timeout=None,
        )

        if response.status_code != 200:
            raise Exception(f"Failed to get unique quote currencies: {response.json()}")

        obj = response.json()
        if isinstance(obj, list):
            return obj
        if isinstance(obj, dict) and obj.get("success"):
            return obj["data"]
        raise Exception("Unexpected response format for quote currencies")
    
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
            urljoin(self.base_url, "/v1/metrics/exchanges/list"),
            params={"market": market},
            headers=self._hdr_metrics,
            timeout=None,
        )

        if response.status_code != 200:
            raise Exception(f"Failed to get exchanges list: {response.json()}")

        obj = response.json()
        if isinstance(obj, list):
            return obj
        if isinstance(obj, dict) and obj.get("success"):
            return obj["data"]
        raise Exception("Unexpected response format for exchanges list")
    
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
        
if __name__ == "__main__":
    client = ApiClient(
        base_url="https://api.crypticorn.dev", 
        metrics_api_key="REDACTED",
        miners_api_key="REDACTED",
    )
    # print("Latest Predictions")
    # print("->")
    # print(client.get_prediction("BTCUSDT", 1, 1))
    # print("")
    print("Economics News")
    print("->")
    print(client.get_economics_news(5, reverse=False))
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
    # print("Get UDF History")
    # print("->")
    # print(client.get_udf_history("BTCUSDT", 25))
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
    # print("Kline Service")
    # print("->")
    print("Kline Symbols for Futures")
    print("->")
    print(client.get_symbols("futures"))
    print("Kline Symbols for Spot")
    print("->")
    print(client.get_symbols("spot"))
    print("Futures Klines")
    print("->")
    print(client.get_klines("futures", "BTCUSDT", "15m", 100, sort="desc"))
    print("Spot Klines")
    print("->")
    print(client.get_klines("spot", "BTCUSDT", "15m", 100, sort="desc"))
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
    # print("Get Keywords for Google Trends")
    # print("->")
    # print(client.get_google_trend_keywords_available())
    # print("Google Trend Keyword")
    # print("->")
    # print(client.get_google_trend_keyword("Bitcoin", limit=1000))
    print("Get Historical Marketcap Rankings")
    print("->")
    rankings = client.get_historical_marketcap_rankings(1741219200, 1741519658, interval='1d', market="futures", exchange_name="binance")
    print(rankings)
    print("Get Historical Marketcap Values")
    print("->")
    print(client.get_historical_marketcap_values_for_rankings(1729422686, 1729595486))
    # print("Get Marketcap Indicator Values")
    # print("KER->")
    # print(client.get_marketcap_indicator_values("BTC", "futures", 15, "ker", 1729422686))
    # print("SMA->")
    # print(client.get_marketcap_indicator_values("BTC", "futures", 15, "sma", 1729422686))
    print("Exchanges for BTC")
    print("->")
    print(client.get_exchanges_for_mc_symbol("BTC", "futures", '1d', 1729382400, 1730047556, 'ACTIVE', 'USDT'))
    # print("Marketcap Ranking with OHLCV")
    # print("->")
    # print(client.get_marketcap_ranking_with_ohlcv("futures", "1h", 20, 20, 1729454444))
    print("Stable or Wrapped Tokens")
    print("->")
    print(client.get_stable_or_wrapped_tokens('stable'))
    print(client.get_stable_or_wrapped_tokens('wrapped'))
    print("Unique Quote Currencies")
    print("->")
    print(client.get_unique_quote_currencies("futures"))
    print("Exchange Mappings")
    print("->")
    print(client.get_exchange_mappings_for_specific_exchange("spot", "Binance"))
    print("Exchange List")
    print("->")
    print(client.get_exchanges_list_for_specific_market("spot"))
    print("Exchange Data")
    print("->")
    print(client.get_exchange_all_symbols("Binance"))
    print("Exchange Spot Symbol")
    print("->")
    print(client.get_symbol_info_exchange("Binance", "BTC-USDT", "spot"))
    print("Exchange Futures Symbol")
    print("->")
    print(client.get_symbol_info_exchange("Binance", "BTC-USDT", "futures"))
    print("Economic Calendar Events")
    print("->")
    print(client.get_economic_calendar_events(1748795773, 1750091773))
    print("CNN Fear and Greed Indicators")
    print("->")
    print(client.get_cnn_keywords())
    print("Fear and Greed Index for all Indicators")
    print("->")
    for index, row in client.get_cnn_keywords().iterrows():
        print(client.get_cnn_sentiment(row['indicator_name'], limit=10))
    # print("Bitstamp Symbols")
    # print("->")
    # print(client.get_bitstamp_symbols())
    # print("Bitstamp OHLCV")
    # print("->")
    # print(client.get_bitstamp_ohlcv_spot("BTCUSDT", "15m", 100))
    # print("Bingx Symbols")
    # print("->")
    # print(client.get_bingx_symbols())
    # print("Bingx Klines")
    # print("->")
    # print(client.get_bingx_klines("BTC-USDT", "5m", 100, sort="desc"))