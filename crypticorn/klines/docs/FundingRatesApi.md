# client.FundingRatesApi

All URIs are relative to *https://api.crypticorn.dev/v1/klines*

Method | HTTP request | Description
------------- | ------------- | -------------
[**funding_rate_funding_rates_symbol_get**](FundingRatesApi.md#funding_rate_funding_rates_symbol_get) | **GET** /funding_rates/{symbol} | Funding Rate


# **funding_rate_funding_rates_symbol_get**
> BaseResponseListFundingRateResponse funding_rate_funding_rates_symbol_get(symbol, start=start, end=end, limit=limit)

Funding Rate

Retrieve funding rate data for a specific symbol in the futures market.

### Example


```python
import client
from client.models.base_response_list_funding_rate_response import BaseResponseListFundingRateResponse
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
    api_instance = client.FundingRatesApi(api_client)
    symbol = 'symbol_example' # str | Trading pair symbol (e.g., BTCUSDT)
    start = 56 # int | Start timestamp in milliseconds (optional)
    end = 56 # int | End timestamp in milliseconds (optional)
    limit = 56 # int | Number of funding rates to return (optional)

    try:
        # Funding Rate
        api_response = api_instance.funding_rate_funding_rates_symbol_get(symbol, start=start, end=end, limit=limit)
        print("The response of FundingRatesApi->funding_rate_funding_rates_symbol_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundingRatesApi->funding_rate_funding_rates_symbol_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading pair symbol (e.g., BTCUSDT) | 
 **start** | **int**| Start timestamp in milliseconds | [optional] 
 **end** | **int**| End timestamp in milliseconds | [optional] 
 **limit** | **int**| Number of funding rates to return | [optional] 

### Return type

[**BaseResponseListFundingRateResponse**](BaseResponseListFundingRateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with funding rate data |  -  |
**400** | Invalid request parameters |  -  |
**404** | No data found |  -  |
**500** | Internal server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

