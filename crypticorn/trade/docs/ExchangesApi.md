# client.ExchangesApi

All URIs are relative to *http://localhost/v1/trade*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_exchanges**](ExchangesApi.md#get_exchanges) | **GET** /exchanges | Get Exchanges


# **get_exchanges**
> List[Exchange] get_exchanges(access_token=access_token)

Get Exchanges

### Example

* Bearer Authentication (HTTPBearer):

```python
import client
from client.models.exchange import Exchange
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/trade
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/trade"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ExchangesApi(api_client)
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Get Exchanges
        api_response = await api_instance.get_exchanges(access_token=access_token)
        print("The response of ExchangesApi->get_exchanges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangesApi->get_exchanges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | [optional] 

### Return type

[**List[Exchange]**](Exchange.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

