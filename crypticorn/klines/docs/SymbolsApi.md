# client.SymbolsApi

All URIs are relative to *http://localhost/v1/klines*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_klines_symbols**](SymbolsApi.md#get_klines_symbols) | **GET** /symbols/{market} | Symbols


# **get_klines_symbols**
> BaseResponseListStr get_klines_symbols(market)

Symbols

Retrieve a list of whitelisted symbols for a specific market.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.base_response_list_str import BaseResponseListStr
from client.models.market_type import MarketType
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
    api_instance = client.SymbolsApi(api_client)
    market = client.MarketType() # MarketType | Market type (spot or futures)

    try:
        # Symbols
        api_response = await api_instance.get_klines_symbols(market)
        print("The response of SymbolsApi->get_klines_symbols:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SymbolsApi->get_klines_symbols: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | [**MarketType**](.md)| Market type (spot or futures) | 

### Return type

[**BaseResponseListStr**](BaseResponseListStr.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with symbol list |  -  |
**404** | No symbols found |  -  |
**500** | Internal server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

