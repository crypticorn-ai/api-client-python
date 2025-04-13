# client.PaymentsApi

All URIs are relative to *http://localhost/v1/pay*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_latest_payment_from_invoice**](PaymentsApi.md#get_latest_payment_from_invoice) | **GET** /payments | Get Latest Payment From Invoice
[**get_payment_history**](PaymentsApi.md#get_payment_history) | **GET** /payments/history | Get Payments
[**get_subscriptions**](PaymentsApi.md#get_subscriptions) | **GET** /payments/subscriptions | Get Subscriptions


# **get_latest_payment_from_invoice**
> Payment get_latest_payment_from_invoice(invoice_id)

Get Latest Payment From Invoice

Get the latest payment by a user from an invoice

### Example

* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.payment import Payment
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

# Configure Bearer authorization (JWT): HTTPBearer
configuration = client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.PaymentsApi(api_client)
    invoice_id = 'invoice_id_example' # str | The invoice ID to get the latest payment from

    try:
        # Get Latest Payment From Invoice
        api_response = await api_instance.get_latest_payment_from_invoice(invoice_id)
        print("The response of PaymentsApi->get_latest_payment_from_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_latest_payment_from_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The invoice ID to get the latest payment from | 

### Return type

[**Payment**](Payment.md)

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
> List[Payment] get_payment_history(limit=limit, offset=offset)

Get Payments

Get the combined payment history for a user across all payment services.

### Example

* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.payment import Payment
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

# Configure Bearer authorization (JWT): HTTPBearer
configuration = client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.PaymentsApi(api_client)
    limit = 0 # int | Limit the number of payments returned. 0 means no limit. (optional) (default to 0)
    offset = 0 # int | Offset the number of payments returned. 0 means no offset. (optional) (default to 0)

    try:
        # Get Payments
        api_response = await api_instance.get_payment_history(limit=limit, offset=offset)
        print("The response of PaymentsApi->get_payment_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_payment_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of payments returned. 0 means no limit. | [optional] [default to 0]
 **offset** | **int**| Offset the number of payments returned. 0 means no offset. | [optional] [default to 0]

### Return type

[**List[Payment]**](Payment.md)

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
> List[ProductSubRead] get_subscriptions(user_id=user_id)

Get Subscriptions

Get all subscriptions for a user. Subscriptions are the products a user has subscribed to. Returns both active and inactive subscriptions.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.product_sub_read import ProductSubRead
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

# Configure Bearer authorization (JWT): HTTPBearer
configuration = client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.PaymentsApi(api_client)
    user_id = 'user_id_example' # str | The user ID to get subscriptions for. Defaults to the authenticated user. (optional)

    try:
        # Get Subscriptions
        api_response = await api_instance.get_subscriptions(user_id=user_id)
        print("The response of PaymentsApi->get_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID to get subscriptions for. Defaults to the authenticated user. | [optional] 

### Return type

[**List[ProductSubRead]**](ProductSubRead.md)

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

