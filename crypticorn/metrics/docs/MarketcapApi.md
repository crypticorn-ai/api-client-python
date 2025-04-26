# client.MarketcapApi

All URIs are relative to *https://api.crypticorn.dev/v1/metrics*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_marketcap**](MarketcapApi.md#get_current_marketcap) | **GET** /get_current_marketcap | Get Current Marketcap
[**get_marketcap_between_timestamps**](MarketcapApi.md#get_marketcap_between_timestamps) | **GET** /marketcap | Get Marketcap Between Timestamps
[**get_marketcap_symbols**](MarketcapApi.md#get_marketcap_symbols) | **GET** /marketcap/symbols | Get Symbols Marketcap Between Timestamps
[**get_marketcap_symbols_with_ohlcv**](MarketcapApi.md#get_marketcap_symbols_with_ohlcv) | **GET** /marketcap/symbols/ohlcv | Get Symbols Marketcap With Ohlcv


# **get_current_marketcap**
> List[Dict[str, object]] get_current_marketcap(limit=limit)

Get Current Marketcap

Retrieve current marketcap data for all symbols.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/metrics
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/metrics"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): HTTPBearer
configuration = client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.MarketcapApi(api_client)
    limit = 50 # int | Number of top symbols to fetch (1-100) (optional) (default to 50)

    try:
        # Get Current Marketcap
        api_response = await api_instance.get_current_marketcap(limit=limit)
        print("The response of MarketcapApi->get_current_marketcap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketcapApi->get_current_marketcap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of top symbols to fetch (1-100) | [optional] [default to 50]

### Return type

**List[Dict[str, object]]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketcap_between_timestamps**
> List[Dict[str, object]] get_marketcap_between_timestamps(start_timestamp=start_timestamp, end_timestamp=end_timestamp)

Get Marketcap Between Timestamps

Retrieve marketcap data between timestamps.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/metrics
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/metrics"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): HTTPBearer
configuration = client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.MarketcapApi(api_client)
    start_timestamp = 1745530274 # int | Start timestamp (optional) (default to 1745530274)
    end_timestamp = 1745703074 # int | End timestamp (optional) (default to 1745703074)

    try:
        # Get Marketcap Between Timestamps
        api_response = await api_instance.get_marketcap_between_timestamps(start_timestamp=start_timestamp, end_timestamp=end_timestamp)
        print("The response of MarketcapApi->get_marketcap_between_timestamps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketcapApi->get_marketcap_between_timestamps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_timestamp** | **int**| Start timestamp | [optional] [default to 1745530274]
 **end_timestamp** | **int**| End timestamp | [optional] [default to 1745703074]

### Return type

**List[Dict[str, object]]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketcap_symbols**
> List[Dict[str, object]] get_marketcap_symbols(start_timestamp=start_timestamp, end_timestamp=end_timestamp, interval=interval, market=market, exchange=exchange)

Get Symbols Marketcap Between Timestamps

Retrieve marketcap data for symbols between timestamps with optional filtering.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.market_type import MarketType
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/metrics
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/metrics"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): HTTPBearer
configuration = client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.MarketcapApi(api_client)
    start_timestamp = 1745530274 # int | Start timestamp (optional) (default to 1745530274)
    end_timestamp = 1745703074 # int | End timestamp (optional) (default to 1745703074)
    interval = 1d # str | Interval for which to fetch symbols and marketcap data (optional) (default to 1d)
    market = client.MarketType() # MarketType | Market for which to fetch symbols and marketcap data (optional)
    exchange = 'exchange_example' # str | Exchange for which to fetch symbols and marketcap data (optional)

    try:
        # Get Symbols Marketcap Between Timestamps
        api_response = await api_instance.get_marketcap_symbols(start_timestamp=start_timestamp, end_timestamp=end_timestamp, interval=interval, market=market, exchange=exchange)
        print("The response of MarketcapApi->get_marketcap_symbols:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketcapApi->get_marketcap_symbols: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_timestamp** | **int**| Start timestamp | [optional] [default to 1745530274]
 **end_timestamp** | **int**| End timestamp | [optional] [default to 1745703074]
 **interval** | **str**| Interval for which to fetch symbols and marketcap data | [optional] [default to 1d]
 **market** | [**MarketType**](.md)| Market for which to fetch symbols and marketcap data | [optional] 
 **exchange** | **str**| Exchange for which to fetch symbols and marketcap data | [optional] 

### Return type

**List[Dict[str, object]]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketcap_symbols_with_ohlcv**
> List[Dict[str, object]] get_marketcap_symbols_with_ohlcv(timestamp=timestamp, timeframe=timeframe, market=market, top_n=top_n, ohlcv_limit=ohlcv_limit)

Get Symbols Marketcap With Ohlcv

Retrieve OHLCV data with marketcap for symbols at a specific timestamp.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.market_type import MarketType
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/metrics
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/metrics"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): HTTPBearer
configuration = client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.MarketcapApi(api_client)
    timestamp = 1745703074 # int | Timestamp for which to fetch symbols and OHLCV data (optional) (default to 1745703074)
    timeframe = '1h' # str | Timeframe for OHLCV data (optional) (default to '1h')
    market = client.MarketType() # MarketType | Market for OHLCV data (optional)
    top_n = 10 # int | Number of symbols to fetch (optional) (default to 10)
    ohlcv_limit = 100 # int | Number of OHLCV data points to fetch (optional) (default to 100)

    try:
        # Get Symbols Marketcap With Ohlcv
        api_response = await api_instance.get_marketcap_symbols_with_ohlcv(timestamp=timestamp, timeframe=timeframe, market=market, top_n=top_n, ohlcv_limit=ohlcv_limit)
        print("The response of MarketcapApi->get_marketcap_symbols_with_ohlcv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketcapApi->get_marketcap_symbols_with_ohlcv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| Timestamp for which to fetch symbols and OHLCV data | [optional] [default to 1745703074]
 **timeframe** | **str**| Timeframe for OHLCV data | [optional] [default to &#39;1h&#39;]
 **market** | [**MarketType**](.md)| Market for OHLCV data | [optional] 
 **top_n** | **int**| Number of symbols to fetch | [optional] [default to 10]
 **ohlcv_limit** | **int**| Number of OHLCV data points to fetch | [optional] [default to 100]

### Return type

**List[Dict[str, object]]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

