# client.ChangeInTimeframeApi

All URIs are relative to *http://localhost/v1/klines*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_change_in_timeframe**](ChangeInTimeframeApi.md#get_change_in_timeframe) | **GET** /change | Get Change In Timeframe


# **get_change_in_timeframe**
> List[ChangeInTimeframe] get_change_in_timeframe(market=market, timeframe=timeframe)

Get Change In Timeframe

Retrieve price change percentage between last two completed timestamps for all pairs.

Valid markets: spot, futures
Valid timeframes: 15m, 30m, 1h, 4h, 1d

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.change_in_timeframe import ChangeInTimeframe
from client.models.market_type import MarketType
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
    api_instance = client.ChangeInTimeframeApi(api_client)
    market = client.MarketType() # MarketType | Market type: 'spot' or 'futures' (optional)
    timeframe = client.Timeframe() # Timeframe | Timeframe: '15m', '30m', '1h', '4h', '1d' (optional)

    try:
        # Get Change In Timeframe
        api_response = await api_instance.get_change_in_timeframe(market=market, timeframe=timeframe)
        print("The response of ChangeInTimeframeApi->get_change_in_timeframe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChangeInTimeframeApi->get_change_in_timeframe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | [**MarketType**](.md)| Market type: &#39;spot&#39; or &#39;futures&#39; | [optional] 
 **timeframe** | [**Timeframe**](.md)| Timeframe: &#39;15m&#39;, &#39;30m&#39;, &#39;1h&#39;, &#39;4h&#39;, &#39;1d&#39; | [optional] 

### Return type

[**List[ChangeInTimeframe]**](ChangeInTimeframe.md)

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

