# client.FuturesTradingPanelApi

All URIs are relative to *http://localhost/v1/trade*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_futures_order**](FuturesTradingPanelApi.md#cancel_futures_order) | **DELETE** /futures/orders | Cancel Order
[**get_futures_balance**](FuturesTradingPanelApi.md#get_futures_balance) | **GET** /futures/balance | Get Futures Balance
[**get_futures_ledger**](FuturesTradingPanelApi.md#get_futures_ledger) | **GET** /futures/ledger | Get Futures Ledger
[**get_historical_futures_orders**](FuturesTradingPanelApi.md#get_historical_futures_orders) | **GET** /futures/orders | Get Historical Futures Orders
[**place_futures_order**](FuturesTradingPanelApi.md#place_futures_order) | **POST** /futures/orders | Place Order


# **cancel_futures_order**
> object cancel_futures_order(order_id, symbol, key, access_token=access_token)

Cancel Order

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
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
    api_instance = client.FuturesTradingPanelApi(api_client)
    order_id = 'order_id_example' # str | 
    symbol = 'symbol_example' # str | 
    key = 'key_example' # str | 
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Cancel Order
        api_response = api_instance.cancel_futures_order(order_id, symbol, key, access_token=access_token)
        print("The response of FuturesTradingPanelApi->cancel_futures_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesTradingPanelApi->cancel_futures_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 
 **symbol** | **str**|  | 
 **key** | **str**|  | 
 **access_token** | **str**|  | [optional] 

### Return type

**object**

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

# **get_futures_balance**
> List[FuturesBalance] get_futures_balance(access_token=access_token)

Get Futures Balance

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
from client.models.futures_balance import FuturesBalance
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
    api_instance = client.FuturesTradingPanelApi(api_client)
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Get Futures Balance
        api_response = api_instance.get_futures_balance(access_token=access_token)
        print("The response of FuturesTradingPanelApi->get_futures_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesTradingPanelApi->get_futures_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | [optional] 

### Return type

[**List[FuturesBalance]**](FuturesBalance.md)

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

# **get_futures_ledger**
> object get_futures_ledger(key, access_token=access_token)

Get Futures Ledger

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
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
    api_instance = client.FuturesTradingPanelApi(api_client)
    key = 'key_example' # str | 
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Get Futures Ledger
        api_response = api_instance.get_futures_ledger(key, access_token=access_token)
        print("The response of FuturesTradingPanelApi->get_futures_ledger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesTradingPanelApi->get_futures_ledger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **access_token** | **str**|  | [optional] 

### Return type

**object**

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

# **get_historical_futures_orders**
> object get_historical_futures_orders(key, access_token=access_token)

Get Historical Futures Orders

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
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
    api_instance = client.FuturesTradingPanelApi(api_client)
    key = 'key_example' # str | 
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Get Historical Futures Orders
        api_response = api_instance.get_historical_futures_orders(key, access_token=access_token)
        print("The response of FuturesTradingPanelApi->get_historical_futures_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesTradingPanelApi->get_historical_futures_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **access_token** | **str**|  | [optional] 

### Return type

**object**

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

# **place_futures_order**
> object place_futures_order(key, body, access_token=access_token)

Place Order

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
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
    api_instance = client.FuturesTradingPanelApi(api_client)
    key = 'key_example' # str | 
    body = None # object | 
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Place Order
        api_response = api_instance.place_futures_order(key, body, access_token=access_token)
        print("The response of FuturesTradingPanelApi->place_futures_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FuturesTradingPanelApi->place_futures_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **body** | **object**|  | 
 **access_token** | **str**|  | [optional] 

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

