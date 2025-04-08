# client.IndicatorsApi

All URIs are relative to *https://api.crypticorn.dev/v1/metrics*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ker_indicator**](IndicatorsApi.md#get_ker_indicator) | **GET** /ker/{symbol} | Get Ker Indicator
[**get_sma_indicator**](IndicatorsApi.md#get_sma_indicator) | **GET** /sma/{symbol} | Get Sma Indicator


# **get_ker_indicator**
> BaseResponseDict get_ker_indicator(symbol, market=market, period=period, timestamp=timestamp)

Get Ker Indicator

Calculate and retrieve the KER indicator for a symbol.

### Example


```python
import client
from client.models.base_response_dict import BaseResponseDict
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
    api_instance = client.IndicatorsApi(api_client)
    symbol = 'symbol_example' # str | 
    market = client.Market() # Market | Market (optional)
    period = 15 # int | KER indicator period (optional) (default to 15)
    timestamp = 1743941814 # int | Timestamp for which to fetch KER indicator (optional) (default to 1743941814)

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
 **market** | [**Market**](.md)| Market | [optional] 
 **period** | **int**| KER indicator period | [optional] [default to 15]
 **timestamp** | **int**| Timestamp for which to fetch KER indicator | [optional] [default to 1743941814]

### Return type

[**BaseResponseDict**](BaseResponseDict.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with KER indicator data |  -  |
**400** | Invalid request parameters |  -  |
**404** | No data found |  -  |
**500** | Internal server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sma_indicator**
> BaseResponseDict get_sma_indicator(symbol, market=market, period=period, timestamp=timestamp)

Get Sma Indicator

Calculate and retrieve the Simple Moving Average (SMA) indicator for a symbol.

### Example


```python
import client
from client.models.base_response_dict import BaseResponseDict
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
    api_instance = client.IndicatorsApi(api_client)
    symbol = 'symbol_example' # str | 
    market = client.Market() # Market | Market (optional)
    period = 15 # int | SMA indicator period (optional) (default to 15)
    timestamp = 1743941814 # int | Timestamp for which to fetch SMA indicator (optional) (default to 1743941814)

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
 **market** | [**Market**](.md)| Market | [optional] 
 **period** | **int**| SMA indicator period | [optional] [default to 15]
 **timestamp** | **int**| Timestamp for which to fetch SMA indicator | [optional] [default to 1743941814]

### Return type

[**BaseResponseDict**](BaseResponseDict.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with SMA indicator data |  -  |
**400** | Invalid request parameters |  -  |
**404** | No data found |  -  |
**500** | Internal server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

