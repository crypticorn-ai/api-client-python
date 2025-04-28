# client.IndicatorsApi

All URIs are relative to *http://localhost/v1/metrics*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ker_indicator**](IndicatorsApi.md#get_ker_indicator) | **GET** /ker/{symbol} | Get Ker Indicator
[**get_sma_indicator**](IndicatorsApi.md#get_sma_indicator) | **GET** /sma/{symbol} | Get Sma Indicator


# **get_ker_indicator**
> Dict[str, object] get_ker_indicator(symbol, market=market, period=period, timestamp=timestamp)

Get Ker Indicator

Calculate and retrieve the KER indicator for a symbol.

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
    api_instance = client.IndicatorsApi(api_client)
    symbol = 'symbol_example' # str | 
    market = 'market_example' # str | Market (optional)
    period = 15 # int | KER indicator period (optional) (default to 15)
    timestamp = 1745832834 # int | Timestamp for which to fetch KER indicator (optional) (default to 1745832834)

    try:
        # Get Ker Indicator
        api_response = await api_instance.get_ker_indicator(symbol, market=market, period=period, timestamp=timestamp)
        print("The response of IndicatorsApi->get_ker_indicator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndicatorsApi->get_ker_indicator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 
 **market** | **str**| Market | [optional] 
 **period** | **int**| KER indicator period | [optional] [default to 15]
 **timestamp** | **int**| Timestamp for which to fetch KER indicator | [optional] [default to 1745832834]

### Return type

**Dict[str, object]**

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

# **get_sma_indicator**
> Dict[str, object] get_sma_indicator(symbol, market=market, period=period, timestamp=timestamp)

Get Sma Indicator

Calculate and retrieve the Simple Moving Average (SMA) indicator for a symbol.

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
    api_instance = client.IndicatorsApi(api_client)
    symbol = 'symbol_example' # str | 
    market = 'market_example' # str | The market type to use for the SMA indicator (optional)
    period = 15 # int | The period to use for the SMA indicator (optional) (default to 15)
    timestamp = 1745832834 # int | The timestamp for which to fetch the SMA indicator (optional) (default to 1745832834)

    try:
        # Get Sma Indicator
        api_response = await api_instance.get_sma_indicator(symbol, market=market, period=period, timestamp=timestamp)
        print("The response of IndicatorsApi->get_sma_indicator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndicatorsApi->get_sma_indicator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 
 **market** | **str**| The market type to use for the SMA indicator | [optional] 
 **period** | **int**| The period to use for the SMA indicator | [optional] [default to 15]
 **timestamp** | **int**| The timestamp for which to fetch the SMA indicator | [optional] [default to 1745832834]

### Return type

**Dict[str, object]**

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

