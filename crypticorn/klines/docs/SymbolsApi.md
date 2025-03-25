# client.SymbolsApi

All URIs are relative to *https://api.crypticorn.dev/v1/klines*

Method | HTTP request | Description
------------- | ------------- | -------------
[**symbols_symbols_market_get**](SymbolsApi.md#symbols_symbols_market_get) | **GET** /symbols/{market} | Symbols


# **symbols_symbols_market_get**
> BaseResponseListStr symbols_symbols_market_get(market)

Symbols

Retrieve a list of whitelisted symbols for a specific market.

### Example


```python
import client
from client.models.base_response_list_str import BaseResponseListStr
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/klines
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/klines"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.SymbolsApi(api_client)
    market = client.Market() # Market | Market type (spot or futures)

    try:
        # Symbols
        api_response = api_instance.symbols_symbols_market_get(market)
        print("The response of SymbolsApi->symbols_symbols_market_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SymbolsApi->symbols_symbols_market_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | [**Market**](.md)| Market type (spot or futures) | 

### Return type

[**BaseResponseListStr**](BaseResponseListStr.md)

### Authorization

No authorization required

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

