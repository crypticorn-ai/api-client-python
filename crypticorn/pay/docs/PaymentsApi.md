# client.PaymentsApi

All URIs are relative to *http://localhost/v1/pay*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_latest_payment_from_invoice**](PaymentsApi.md#get_latest_payment_from_invoice) | **GET** /payments | Get Latest Payment From Invoice
[**get_payment_history**](PaymentsApi.md#get_payment_history) | **GET** /payments/history | Get Payments
[**get_subscriptions**](PaymentsApi.md#get_subscriptions) | **GET** /payments/subscriptions | Get Subscriptions


# **get_latest_payment_from_invoice**
> UnifiedPaymentModel get_latest_payment_from_invoice(invoice_id, access_token=access_token)

Get Latest Payment From Invoice

Get the latest payment from an invoice

### Example

* Bearer Authentication (HTTPBearer):

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

# Configure Bearer authorization: HTTPBearer
configuration = client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.PaymentsApi(api_client)
    invoice_id = 'invoice_id_example' # str | 
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Get Latest Payment From Invoice
        api_response = await api_instance.get_latest_payment_from_invoice(invoice_id, access_token=access_token)
        print("The response of PaymentsApi->get_latest_payment_from_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_latest_payment_from_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **access_token** | **str**|  | [optional] 

### Return type

[**UnifiedPaymentModel**](UnifiedPaymentModel.md)

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

# **get_payment_history**
> List[UnifiedPaymentModel] get_payment_history(access_token=access_token)

Get Payments

Get combined payment history for a user across all payment services.

### Example

* Bearer Authentication (HTTPBearer):

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

# Configure Bearer authorization: HTTPBearer
configuration = client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.PaymentsApi(api_client)
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Get Payments
        api_response = await api_instance.get_payment_history(access_token=access_token)
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

# **get_subscriptions**
> List[ProductSubsModel] get_subscriptions(user_id=user_id, access_token=access_token)

Get Subscriptions

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer Authentication (HTTPBearer):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization: HTTPBearer
configuration = client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.PaymentsApi(api_client)
    user_id = 'user_id_example' # str |  (optional)
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Get Subscriptions
        api_response = await api_instance.get_subscriptions(user_id=user_id, access_token=access_token)
        print("The response of PaymentsApi->get_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | [optional] 
 **access_token** | **str**|  | [optional] 

### Return type

[**List[ProductSubsModel]**](ProductSubsModel.md)

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

