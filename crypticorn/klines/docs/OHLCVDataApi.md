# client.OHLCVDataApi

All URIs are relative to *http://localhost/v1/klines*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ohlcv**](OHLCVDataApi.md#get_ohlcv) | **GET** /{market}/{timeframe}/{symbol} | Get Ohlcv


# **get_ohlcv**
> OHLCVHistory get_ohlcv(market, timeframe, symbol, start=start, end=end, limit=limit, sort_direction=sort_direction)

Get Ohlcv

Retrieve OHLCV (Open, High, Low, Close, Volume) data for a specific market, timeframe, and symbol.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.ohlcv_history import OHLCVHistory
from client.models.sort_direction import SortDirection
from client.models.timeframe import Timeframe
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/klines
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/klines"
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
    api_instance = client.OHLCVDataApi(api_client)
    market = 'market_example' # str | Market type
    timeframe = client.Timeframe() # Timeframe | Timeframe for the candles
    symbol = 'symbol_example' # str | Trading pair symbol (e.g., BTCUSDT)
    start = 56 # int | Start timestamp in milliseconds (optional)
    end = 56 # int | End timestamp in milliseconds (optional)
    limit = 56 # int | Number of candles to return (optional)
    sort_direction = client.SortDirection() # SortDirection | Klines sort direction (asc or desc) (optional)

    try:
        # Get Ohlcv
        api_response = await api_instance.get_ohlcv(market, timeframe, symbol, start=start, end=end, limit=limit, sort_direction=sort_direction)
        print("The response of OHLCVDataApi->get_ohlcv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OHLCVDataApi->get_ohlcv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**| Market type | 
 **timeframe** | [**Timeframe**](.md)| Timeframe for the candles | 
 **symbol** | **str**| Trading pair symbol (e.g., BTCUSDT) | 
 **start** | **int**| Start timestamp in milliseconds | [optional] 
 **end** | **int**| End timestamp in milliseconds | [optional] 
 **limit** | **int**| Number of candles to return | [optional] 
 **sort_direction** | [**SortDirection**](.md)| Klines sort direction (asc or desc) | [optional] 

### Return type

[**OHLCVHistory**](OHLCVHistory.md)

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

