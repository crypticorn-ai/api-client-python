# client.FundingRatesApi

All URIs are relative to *http://localhost/v1/klines*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_funding_rates**](FundingRatesApi.md#get_funding_rates) | **GET** /funding_rates/{symbol} | Funding Rate


# **get_funding_rates**
> List[FundingRate] get_funding_rates(symbol, start=start, end=end, limit=limit)

Funding Rate

Retrieve funding rate data for a specific symbol in the futures market.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.funding_rate import FundingRate
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
    api_instance = client.FundingRatesApi(api_client)
    symbol = 'symbol_example' # str | Trading pair symbol (e.g., BTCUSDT)
    start = 56 # int | Start timestamp in milliseconds (optional)
    end = 56 # int | End timestamp in milliseconds (optional)
    limit = 56 # int | Number of funding rates to return (optional)

    try:
        # Funding Rate
        api_response = await api_instance.get_funding_rates(symbol, start=start, end=end, limit=limit)
        print("The response of FundingRatesApi->get_funding_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundingRatesApi->get_funding_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading pair symbol (e.g., BTCUSDT) | 
 **start** | **int**| Start timestamp in milliseconds | [optional] 
 **end** | **int**| End timestamp in milliseconds | [optional] 
 **limit** | **int**| Number of funding rates to return | [optional] 

### Return type

[**List[FundingRate]**](FundingRate.md)

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

