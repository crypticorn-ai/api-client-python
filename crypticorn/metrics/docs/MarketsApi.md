# client.MarketsApi

All URIs are relative to *https://api.crypticorn.dev/v1/metrics*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_markets_for_symbol**](MarketsApi.md#get_available_markets_for_symbol) | **GET** /markets/{market}/{symbol} | Get Markets For Symbol
[**get_quote_currencies**](MarketsApi.md#get_quote_currencies) | **GET** /quote_currencies/{market} | Get Quote Currencies


# **get_available_markets_for_symbol**
> List[str] get_available_markets_for_symbol(market, symbol, quote_currency=quote_currency, status=status)

Get Markets For Symbol

Get markets for a symbol with filtering options.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.market_type import MarketType
from client.models.trading_status import TradingStatus
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/metrics
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/metrics"
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
    api_instance = client.MarketsApi(api_client)
    market = client.MarketType() # MarketType | Market type (spot or futures)
    symbol = 'symbol_example' # str | Symbol to fetch markets for
    quote_currency = 'USDT' # str | Quote currency for which to fetch markets (optional) (default to 'USDT')
    status = client.TradingStatus() # TradingStatus | Trading pair status for which to fetch markets (optional)

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
 **market** | [**MarketType**](.md)| Market type (spot or futures) | 
 **symbol** | **str**| Symbol to fetch markets for | 
 **quote_currency** | **str**| Quote currency for which to fetch markets | [optional] [default to &#39;USDT&#39;]
 **status** | [**TradingStatus**](.md)| Trading pair status for which to fetch markets | [optional] 

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

# **get_quote_currencies**
> List[str] get_quote_currencies(market)

Get Quote Currencies

Get available quote currencies for a market.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.market_type import MarketType
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/metrics
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/metrics"
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
    api_instance = client.MarketsApi(api_client)
    market = client.MarketType() # MarketType | Market type (spot or futures)

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
 **market** | [**MarketType**](.md)| Market type (spot or futures) | 

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

