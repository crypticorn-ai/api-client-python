# client.PaymentsApi

All URIs are relative to *http://localhost/v1/pay*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_history**](PaymentsApi.md#get_payment_history) | **GET** /payments/history | Get Payments
[**get_payments_html_get**](PaymentsApi.md#get_payments_html_get) | **GET** /payments/html | Get
[**get_subscriptions**](PaymentsApi.md#get_subscriptions) | **GET** /payments/subscriptions | Get Subscriptions


# **get_payment_history**
> List[UnifiedPaymentModel] get_payment_history(access_token=access_token)

Get Payments

Get combined payment history for a user across all payment services.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
from client.models.unified_payment_model import UnifiedPaymentModel
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/pay
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/pay"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.PaymentsApi(api_client)
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Get Payments
        api_response = api_instance.get_payment_history(access_token=access_token)
        print("The response of PaymentsApi->get_payment_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_payment_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | [optional] 

### Return type

[**List[UnifiedPaymentModel]**](UnifiedPaymentModel.md)

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

# **get_payments_html_get**
> object get_payments_html_get()

Get

### Example


```python
import client
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/pay
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/pay"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.PaymentsApi(api_client)

    try:
        # Get
        api_response = api_instance.get_payments_html_get()
        print("The response of PaymentsApi->get_payments_html_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_payments_html_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions**
> List[ProductSubsModel] get_subscriptions(access_token=access_token)

Get Subscriptions

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
from client.models.product_subs_model import ProductSubsModel
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/pay
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/pay"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.PaymentsApi(api_client)
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Get Subscriptions
        api_response = api_instance.get_subscriptions(access_token=access_token)
        print("The response of PaymentsApi->get_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | [optional] 

### Return type

[**List[ProductSubsModel]**](ProductSubsModel.md)

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

