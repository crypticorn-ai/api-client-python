# client.StrategiesApi

All URIs are relative to *http://localhost/v1/trade*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_strategies**](StrategiesApi.md#get_strategies) | **GET** /strategies | Get Strategies


# **get_strategies**
> List[StrategyModel] get_strategies(limit=limit, offset=offset, access_token=access_token)

Get Strategies

### Example

* Bearer Authentication (HTTPBearer):

```python
import client
from client.models.strategy_model import StrategyModel
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
    api_instance = client.StrategiesApi(api_client)
    limit = 0 # int |  (optional) (default to 0)
    offset = 0 # int |  (optional) (default to 0)
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Get Strategies
        api_response = await api_instance.get_strategies(limit=limit, offset=offset, access_token=access_token)
        print("The response of StrategiesApi->get_strategies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StrategiesApi->get_strategies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 0]
 **offset** | **int**|  | [optional] [default to 0]
 **access_token** | **str**|  | [optional] 

### Return type

[**List[StrategyModel]**](StrategyModel.md)

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

