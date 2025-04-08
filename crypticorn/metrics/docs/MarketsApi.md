# client.MarketsApi

All URIs are relative to *https://api.crypticorn.dev/v1/metrics*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_markets_for_symbol**](MarketsApi.md#get_available_markets_for_symbol) | **GET** /markets/{market}/{symbol} | Get Markets For Symbol
[**get_quote_currencies**](MarketsApi.md#get_quote_currencies) | **GET** /quote_currencies/{market} | Get Quote Currencies


# **get_available_markets_for_symbol**
> BaseResponseListDict get_available_markets_for_symbol(market, symbol, quote_currency=quote_currency, status=status)

Get Markets For Symbol

Get markets for a symbol with filtering options.

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
    api_instance = client.MarketsApi(api_client)
    market = client.Market() # Market | Market type (spot or futures)
    symbol = 'symbol_example' # str | Symbol to fetch markets for
    quote_currency = 'USDT' # str | Quote currency for which to fetch markets (optional) (default to 'USDT')
    status = ACTIVE # str | Trading pair status for which to fetch markets (optional) (default to ACTIVE)

    try:
        # Get Markets For Symbol
        api_response = await api_instance.get_available_markets_for_symbol(market, symbol, quote_currency=quote_currency, status=status)
        print("The response of MarketsApi->get_available_markets_for_symbol:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketsApi->get_available_markets_for_symbol: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | [**Market**](.md)| Market type (spot or futures) | 
 **symbol** | **str**| Symbol to fetch markets for | 
 **quote_currency** | **str**| Quote currency for which to fetch markets | [optional] [default to &#39;USDT&#39;]
 **status** | **str**| Trading pair status for which to fetch markets | [optional] [default to ACTIVE]

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
**200** | Successful response with market data |  -  |
**400** | Invalid request parameters |  -  |
**404** | No data found |  -  |
**500** | Internal server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quote_currencies**
> BaseResponseListStr get_quote_currencies(market)

Get Quote Currencies

Get available quote currencies for a market.

### Example


```python
import client
from client.models.base_response_list_str import BaseResponseListStr
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
    api_instance = client.MarketsApi(api_client)
    market = client.Market() # Market | Market type (spot or futures)

    try:
        # Get Quote Currencies
        api_response = await api_instance.get_quote_currencies(market)
        print("The response of MarketsApi->get_quote_currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketsApi->get_quote_currencies: %s\n" % e)
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
**200** | Successful response with quote currencies |  -  |
**400** | Invalid request parameters |  -  |
**404** | No data found |  -  |
**500** | Internal server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

