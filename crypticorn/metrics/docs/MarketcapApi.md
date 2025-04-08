# client.MarketcapApi

All URIs are relative to *https://api.crypticorn.dev/v1/metrics*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_marketcap**](MarketcapApi.md#get_current_marketcap) | **GET** /get_current_marketcap | Get Current Marketcap
[**get_marketcap_between_timestamps**](MarketcapApi.md#get_marketcap_between_timestamps) | **GET** /marketcap | Get Marketcap Between Timestamps
[**get_marketcap_symbols**](MarketcapApi.md#get_marketcap_symbols) | **GET** /marketcap/symbols | Get Symbols Marketcap Between Timestamps
[**get_marketcap_symbols_with_ohlcv**](MarketcapApi.md#get_marketcap_symbols_with_ohlcv) | **GET** /marketcap/symbols/ohlcv | Get Symbols Marketcap With Ohlcv


# **get_current_marketcap**
> BaseResponseListDict get_current_marketcap(limit=limit)

Get Current Marketcap

Retrieve current marketcap data for all symbols.

### Example


```python
import client
from client.models.base_response_list_dict import BaseResponseListDict
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/metrics
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/metrics"
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

[**BaseResponseListDict**](BaseResponseListDict.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with current marketcap data |  -  |
**400** | Invalid request parameters |  -  |
**404** | No data found |  -  |
**500** | Internal server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketcap_between_timestamps**
> BaseResponseListDict get_marketcap_between_timestamps(start_timestamp=start_timestamp, end_timestamp=end_timestamp)

Get Marketcap Between Timestamps

Retrieve marketcap data between timestamps.

### Example


```python
import client
from client.models.base_response_list_dict import BaseResponseListDict
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/metrics
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/metrics"
)


# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.MarketcapApi(api_client)
    start_timestamp = 1743769014 # int | Start timestamp (optional) (default to 1743769014)
    end_timestamp = 1743941814 # int | End timestamp (optional) (default to 1743941814)

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
 **start_timestamp** | **int**| Start timestamp | [optional] [default to 1743769014]
 **end_timestamp** | **int**| End timestamp | [optional] [default to 1743941814]

### Return type

[**BaseResponseListDict**](BaseResponseListDict.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with marketcap data |  -  |
**400** | Invalid request parameters |  -  |
**404** | No data found |  -  |
**500** | Internal server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketcap_symbols**
> BaseResponseListDict get_marketcap_symbols(start_timestamp=start_timestamp, end_timestamp=end_timestamp, interval=interval, market=market, exchange=exchange)

Get Symbols Marketcap Between Timestamps

Retrieve marketcap data for symbols between timestamps with optional filtering.

### Example


```python
import client
from client.models.base_response_list_dict import BaseResponseListDict
from client.models.market import Market
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/metrics
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/metrics"
)


# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.MarketcapApi(api_client)
    start_timestamp = 1743769014 # int | Start timestamp (optional) (default to 1743769014)
    end_timestamp = 1743941814 # int | End timestamp (optional) (default to 1743941814)
    interval = 1d # str | Interval for which to fetch symbols and marketcap data (optional) (default to 1d)
    market = client.Market() # Market | Market for which to fetch symbols and marketcap data (optional)
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
 **start_timestamp** | **int**| Start timestamp | [optional] [default to 1743769014]
 **end_timestamp** | **int**| End timestamp | [optional] [default to 1743941814]
 **interval** | **str**| Interval for which to fetch symbols and marketcap data | [optional] [default to 1d]
 **market** | [**Market**](.md)| Market for which to fetch symbols and marketcap data | [optional] 
 **exchange** | **str**| Exchange for which to fetch symbols and marketcap data | [optional] 

### Return type

[**BaseResponseListDict**](BaseResponseListDict.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with marketcap data |  -  |
**400** | Invalid request parameters |  -  |
**404** | No data found |  -  |
**500** | Internal server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketcap_symbols_with_ohlcv**
> BaseResponseListDict get_marketcap_symbols_with_ohlcv(timestamp=timestamp, timeframe=timeframe, market=market, top_n=top_n, ohlcv_limit=ohlcv_limit)

Get Symbols Marketcap With Ohlcv

Retrieve OHLCV data with marketcap for symbols at a specific timestamp.

### Example


```python
import client
from client.models.base_response_list_dict import BaseResponseListDict
from client.models.market import Market
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/metrics
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/metrics"
)


# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.MarketcapApi(api_client)
    timestamp = 1743941814 # int | Timestamp for which to fetch symbols and OHLCV data (optional) (default to 1743941814)
    timeframe = '1h' # str | Timeframe for OHLCV data (optional) (default to '1h')
    market = client.Market() # Market | Market for OHLCV data (optional)
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
 **timestamp** | **int**| Timestamp for which to fetch symbols and OHLCV data | [optional] [default to 1743941814]
 **timeframe** | **str**| Timeframe for OHLCV data | [optional] [default to &#39;1h&#39;]
 **market** | [**Market**](.md)| Market for OHLCV data | [optional] 
 **top_n** | **int**| Number of symbols to fetch | [optional] [default to 10]
 **ohlcv_limit** | **int**| Number of OHLCV data points to fetch | [optional] [default to 100]

### Return type

[**BaseResponseListDict**](BaseResponseListDict.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with OHLCV and marketcap data |  -  |
**400** | Invalid request parameters |  -  |
**404** | No data found |  -  |
**500** | Internal server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

