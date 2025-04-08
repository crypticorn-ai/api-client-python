# client.TradingActionsApi

All URIs are relative to *http://localhost/v1/trade*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_actions**](TradingActionsApi.md#get_actions) | **GET** /actions | Get Actions
[**post_futures_action**](TradingActionsApi.md#post_futures_action) | **POST** /actions/futures | Post Futures Action
[**post_spot_action**](TradingActionsApi.md#post_spot_action) | **POST** /actions/spot | Post Spot Action


# **get_actions**
> List[ActionModel] get_actions(limit=limit, offset=offset)

Get Actions

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.action_model import ActionModel
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
    api_instance = client.TradingActionsApi(api_client)
    limit = 0 # int |  (optional) (default to 0)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Get Actions
        api_response = await api_instance.get_actions(limit=limit, offset=offset)
        print("The response of TradingActionsApi->get_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingActionsApi->get_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 0]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[ActionModel]**](ActionModel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_futures_action**
> PostFuturesAction post_futures_action(futures_trading_action)

Post Futures Action

Endpoint to receive futures trading actions from the trading strategy

### Example

* Api Key Authentication (APIKeyHeader):

```python
import client
from client.models.futures_trading_action import FuturesTradingAction
from client.models.post_futures_action import PostFuturesAction
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.TradingActionsApi(api_client)
    futures_trading_action = client.FuturesTradingAction() # FuturesTradingAction | 

    try:
        # Post Futures Action
        api_response = await api_instance.post_futures_action(futures_trading_action)
        print("The response of TradingActionsApi->post_futures_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingActionsApi->post_futures_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **futures_trading_action** | [**FuturesTradingAction**](FuturesTradingAction.md)|  | 

### Return type

[**PostFuturesAction**](PostFuturesAction.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_spot_action**
> object post_spot_action(futures_trading_action)

Post Spot Action

### Example

* Api Key Authentication (APIKeyHeader):

```python
import client
from client.models.futures_trading_action import FuturesTradingAction
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.TradingActionsApi(api_client)
    futures_trading_action = client.FuturesTradingAction() # FuturesTradingAction | 

    try:
        # Post Spot Action
        api_response = await api_instance.post_spot_action(futures_trading_action)
        print("The response of TradingActionsApi->post_spot_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingActionsApi->post_spot_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **futures_trading_action** | [**FuturesTradingAction**](FuturesTradingAction.md)|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

