# client.ExchangesApi

All URIs are relative to *http://localhost/v1/metrics*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_exchanges**](ExchangesApi.md#get_available_exchanges) | **GET** /available_exchanges/{market}/{symbol} | Get Available Exchanges
[**get_available_exchanges_for_market**](ExchangesApi.md#get_available_exchanges_for_market) | **GET** /exchange_list/{market} | Get Exchange List
[**get_exchange_mappings**](ExchangesApi.md#get_exchange_mappings) | **GET** /exchange_mappings/{market} | Get Exchange Mappings


# **get_available_exchanges**
> List[Dict[str, object]] get_available_exchanges(market, symbol, interval=interval, start_timestamp=start_timestamp, end_timestamp=end_timestamp, quote_currency=quote_currency, status=status)

Get Available Exchanges

Get available exchanges for a symbol with various filtering options.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.time_interval import TimeInterval
from client.models.trading_status import TradingStatus
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/metrics
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/metrics"
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
    api_instance = client.ExchangesApi(api_client)
    market = 'market_example' # str | Market type (spot or futures)
    symbol = 'symbol_example' # str | Symbol to fetch available exchanges for
    interval = client.TimeInterval() # TimeInterval | Interval for which to fetch available exchanges (optional)
    start_timestamp = 1745280000 # int | Start timestamp for which to fetch available exchanges (defaults to previous 7 day's closing) (optional) (default to 1745280000)
    end_timestamp = 1745930223 # int | End timestamp for which to fetch available exchanges (optional) (default to 1745930223)
    quote_currency = 'USDT' # str | Quote currency for which to fetch available exchanges (Use quote currencies endpoint to get available quote currencies) (optional) (default to 'USDT')
    status = client.TradingStatus() # TradingStatus | Trading pair status for which to fetch available exchanges (optional)

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
 **market** | **str**| Market type (spot or futures) | 
 **symbol** | **str**| Symbol to fetch available exchanges for | 
 **interval** | [**TimeInterval**](.md)| Interval for which to fetch available exchanges | [optional] 
 **start_timestamp** | **int**| Start timestamp for which to fetch available exchanges (defaults to previous 7 day&#39;s closing) | [optional] [default to 1745280000]
 **end_timestamp** | **int**| End timestamp for which to fetch available exchanges | [optional] [default to 1745930223]
 **quote_currency** | **str**| Quote currency for which to fetch available exchanges (Use quote currencies endpoint to get available quote currencies) | [optional] [default to &#39;USDT&#39;]
 **status** | [**TradingStatus**](.md)| Trading pair status for which to fetch available exchanges | [optional] 

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

# **get_available_exchanges_for_market**
> List[str] get_available_exchanges_for_market(market)

Get Exchange List

Get list of exchanges for a market.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/metrics
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/metrics"
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
    api_instance = client.ExchangesApi(api_client)
    market = 'market_example' # str | Market type (spot or futures)

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
 **market** | **str**| Market type (spot or futures) | 

### Return type

**List[str]**

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

# **get_exchange_mappings**
> List[str] get_exchange_mappings(market, exchange=exchange)

Get Exchange Mappings

Get exchange mappings for a market with optional exchange name filter.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/metrics
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/metrics"
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
    api_instance = client.ExchangesApi(api_client)
    market = 'market_example' # str | Market type (spot or futures)
    exchange = 'exchange_example' # str | Exchange name for which to fetch exchange mappings (optional)

    try:
        # Get Exchange Mappings
        api_response = await api_instance.get_exchange_mappings(market, exchange=exchange)
        print("The response of ExchangesApi->get_exchange_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangesApi->get_exchange_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**| Market type (spot or futures) | 
 **exchange** | **str**| Exchange name for which to fetch exchange mappings | [optional] 

### Return type

**List[str]**

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

