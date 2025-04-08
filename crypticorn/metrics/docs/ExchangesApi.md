# client.ExchangesApi

All URIs are relative to *https://api.crypticorn.dev/v1/metrics*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_exchanges**](ExchangesApi.md#get_available_exchanges) | **GET** /available_exchanges/{market}/{symbol} | Get Available Exchanges
[**get_available_exchanges_for_market**](ExchangesApi.md#get_available_exchanges_for_market) | **GET** /exchange_list/{market} | Get Exchange List
[**get_exchange_mappings**](ExchangesApi.md#get_exchange_mappings) | **GET** /exchange_mappings/{market} | Get Exchange Mappings


# **get_available_exchanges**
> BaseResponseListDict get_available_exchanges(market, symbol, interval=interval, start_timestamp=start_timestamp, end_timestamp=end_timestamp, quote_currency=quote_currency, status=status)

Get Available Exchanges

Get available exchanges for a symbol with various filtering options.

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
    api_instance = client.ExchangesApi(api_client)
    market = client.Market() # Market | Market type (spot or futures)
    symbol = 'symbol_example' # str | Symbol to fetch available exchanges for
    interval = 1d # str | Interval for which to fetch available exchanges (optional) (default to 1d)
    start_timestamp = 1743292800 # int | Start timestamp for which to fetch available exchanges (defaults to previous 7 day's closing) (optional) (default to 1743292800)
    end_timestamp = 1743941814 # int | End timestamp for which to fetch available exchanges (optional) (default to 1743941814)
    quote_currency = 'USDT' # str | Quote currency for which to fetch available exchanges (Use quote currencies endpoint to get available quote currencies) (optional) (default to 'USDT')
    status = ACTIVE # str | Trading pair status for which to fetch available exchanges (optional) (default to ACTIVE)

    try:
        # Get Available Exchanges
        api_response = await api_instance.get_available_exchanges(market, symbol, interval=interval, start_timestamp=start_timestamp, end_timestamp=end_timestamp, quote_currency=quote_currency, status=status)
        print("The response of ExchangesApi->get_available_exchanges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangesApi->get_available_exchanges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | [**Market**](.md)| Market type (spot or futures) | 
 **symbol** | **str**| Symbol to fetch available exchanges for | 
 **interval** | **str**| Interval for which to fetch available exchanges | [optional] [default to 1d]
 **start_timestamp** | **int**| Start timestamp for which to fetch available exchanges (defaults to previous 7 day&#39;s closing) | [optional] [default to 1743292800]
 **end_timestamp** | **int**| End timestamp for which to fetch available exchanges | [optional] [default to 1743941814]
 **quote_currency** | **str**| Quote currency for which to fetch available exchanges (Use quote currencies endpoint to get available quote currencies) | [optional] [default to &#39;USDT&#39;]
 **status** | **str**| Trading pair status for which to fetch available exchanges | [optional] [default to ACTIVE]

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
**200** | Successful response with available exchanges |  -  |
**400** | Invalid request parameters |  -  |
**404** | No data found |  -  |
**500** | Internal server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_exchanges_for_market**
> BaseResponseListStr get_available_exchanges_for_market(market)

Get Exchange List

Get list of exchanges for a market.

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
    api_instance = client.ExchangesApi(api_client)
    market = client.Market() # Market | Market type (spot or futures)

    try:
        # Get Exchange List
        api_response = await api_instance.get_available_exchanges_for_market(market)
        print("The response of ExchangesApi->get_available_exchanges_for_market:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangesApi->get_available_exchanges_for_market: %s\n" % e)
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
**200** | Successful response with exchange list |  -  |
**400** | Invalid request parameters |  -  |
**404** | No data found |  -  |
**500** | Internal server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchange_mappings**
> BaseResponseListExchangeMapping get_exchange_mappings(market, exchange_name=exchange_name)

Get Exchange Mappings

Get exchange mappings for a market with optional exchange name filter.

### Example


```python
import client
from client.models.base_response_list_exchange_mapping import BaseResponseListExchangeMapping
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
    api_instance = client.ExchangesApi(api_client)
    market = client.Market() # Market | Market type (spot or futures)
    exchange_name = 'exchange_name_example' # str | Exchange name for which to fetch exchange mappings (optional)

    try:
        # Get Exchange Mappings
        api_response = await api_instance.get_exchange_mappings(market, exchange_name=exchange_name)
        print("The response of ExchangesApi->get_exchange_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangesApi->get_exchange_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | [**Market**](.md)| Market type (spot or futures) | 
 **exchange_name** | **str**| Exchange name for which to fetch exchange mappings | [optional] 

### Return type

[**BaseResponseListExchangeMapping**](BaseResponseListExchangeMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with exchange mappings |  -  |
**400** | Invalid request parameters |  -  |
**404** | No data found |  -  |
**500** | Internal server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

