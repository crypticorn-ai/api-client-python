# client.TradingActionsApi

All URIs are relative to *http://localhost/v1/trade*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_actions**](TradingActionsApi.md#get_actions) | **GET** /actions | Get Actions
[**post_futures_action**](TradingActionsApi.md#post_futures_action) | **POST** /actions/futures | Post Futures Action
[**post_spot_action**](TradingActionsApi.md#post_spot_action) | **POST** /actions/spot | Post Spot Action


# **get_actions**
> List[ActionModel] get_actions(limit=limit, offset=offset, access_token=access_token)

Get Actions

### Example

* OAuth Authentication (OAuth2PasswordBearer):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.TradingActionsApi(api_client)
    limit = 0 # int |  (optional) (default to 0)
    offset = 0 # int |  (optional) (default to 0)
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Get Actions
        api_response = api_instance.get_actions(limit=limit, offset=offset, access_token=access_token)
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
 **access_token** | **str**|  | [optional] 

### Return type

[**List[ActionModel]**](ActionModel.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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
> PostFuturesAction post_futures_action(futures_trading_action, authorization=authorization)

Post Futures Action

Endpoint to receive futures trading actions from the trading strategy

### Example


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


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.TradingActionsApi(api_client)
    futures_trading_action = client.FuturesTradingAction() # FuturesTradingAction | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Post Futures Action
        api_response = api_instance.post_futures_action(futures_trading_action, authorization=authorization)
        print("The response of TradingActionsApi->post_futures_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingActionsApi->post_futures_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **futures_trading_action** | [**FuturesTradingAction**](FuturesTradingAction.md)|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**PostFuturesAction**](PostFuturesAction.md)

### Authorization

No authorization required

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

* OAuth Authentication (OAuth2PasswordBearer):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.TradingActionsApi(api_client)
    futures_trading_action = client.FuturesTradingAction() # FuturesTradingAction | 

    try:
        # Post Spot Action
        api_response = api_instance.post_spot_action(futures_trading_action)
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

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

