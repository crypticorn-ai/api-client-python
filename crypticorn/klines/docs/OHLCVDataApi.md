# client.OHLCVDataApi

All URIs are relative to *http://localhost/v1/klines*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ohlcv_market_timeframe_symbol_get**](OHLCVDataApi.md#get_ohlcv_market_timeframe_symbol_get) | **GET** /{market}/{timeframe}/{symbol} | Get Ohlcv


# **get_ohlcv_market_timeframe_symbol_get**
> BaseResponseOHLCVResponse get_ohlcv_market_timeframe_symbol_get(market, timeframe, symbol, start=start, end=end, limit=limit, sort_direction=sort_direction)

Get Ohlcv

Retrieve OHLCV (Open, High, Low, Close, Volume) data for a specific market, timeframe, and symbol.

### Example


```python
import client
from client.models.base_response_ohlcv_response import BaseResponseOHLCVResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/klines
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/klines"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.OHLCVDataApi(api_client)
    market = client.Market() # Market | Market type (spot or futures)
    timeframe = client.Timeframe() # Timeframe | Timeframe for the candles
    symbol = 'symbol_example' # str | Trading pair symbol (e.g., BTCUSDT)
    start = 56 # int | Start timestamp in milliseconds (optional)
    end = 56 # int | End timestamp in milliseconds (optional)
    limit = 56 # int | Number of candles to return (optional)
    sort_direction = client.SortDirection() # SortDirection | Klines sort direction (asc or desc) (optional)

    try:
        # Get Ohlcv
        api_response = api_instance.get_ohlcv_market_timeframe_symbol_get(market, timeframe, symbol, start=start, end=end, limit=limit, sort_direction=sort_direction)
        print("The response of OHLCVDataApi->get_ohlcv_market_timeframe_symbol_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OHLCVDataApi->get_ohlcv_market_timeframe_symbol_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | [**Market**](.md)| Market type (spot or futures) | 
 **timeframe** | [**Timeframe**](.md)| Timeframe for the candles | 
 **symbol** | **str**| Trading pair symbol (e.g., BTCUSDT) | 
 **start** | **int**| Start timestamp in milliseconds | [optional] 
 **end** | **int**| End timestamp in milliseconds | [optional] 
 **limit** | **int**| Number of candles to return | [optional] 
 **sort_direction** | [**SortDirection**](.md)| Klines sort direction (asc or desc) | [optional] 

### Return type

[**BaseResponseOHLCVResponse**](BaseResponseOHLCVResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with OHLCV data |  -  |
**400** | Invalid request parameters |  -  |
**404** | No data found |  -  |
**500** | Internal server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

