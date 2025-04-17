# client.NOWPaymentsApi

All URIs are relative to *http://localhost/v1/pay*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_now_invoice**](NOWPaymentsApi.md#create_now_invoice) | **POST** /now/invoice | Create Invoice
[**get_now_api_status**](NOWPaymentsApi.md#get_now_api_status) | **GET** /now/status | Get Status
[**handle_now_webhook**](NOWPaymentsApi.md#handle_now_webhook) | **POST** /now/webhook | Handle Webhook


# **create_now_invoice**
> NowCreateInvoiceRes create_now_invoice(now_create_invoice_req)

Create Invoice

Create a payment invoice with a payment link for customer completion

### Example

* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.now_create_invoice_req import NowCreateInvoiceReq
from client.models.now_create_invoice_res import NowCreateInvoiceRes
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
    api_instance = client.NOWPaymentsApi(api_client)
    now_create_invoice_req = client.NowCreateInvoiceReq() # NowCreateInvoiceReq | 

    try:
        # Create Invoice
        api_response = await api_instance.create_now_invoice(now_create_invoice_req)
        print("The response of NOWPaymentsApi->create_now_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NOWPaymentsApi->create_now_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **now_create_invoice_req** | [**NowCreateInvoiceReq**](NowCreateInvoiceReq.md)|  | 

### Return type

[**NowCreateInvoiceRes**](NowCreateInvoiceRes.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_now_api_status**
> NowAPIStatusRes get_now_api_status()

Get Status

Get the status of the NOWPayments API

### Example

* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.now_api_status_res import NowAPIStatusRes
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
    api_instance = client.NOWPaymentsApi(api_client)

    try:
        # Get Status
        api_response = await api_instance.get_now_api_status()
        print("The response of NOWPaymentsApi->get_now_api_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NOWPaymentsApi->get_now_api_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NowAPIStatusRes**](NowAPIStatusRes.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_now_webhook**
> object handle_now_webhook()

Handle Webhook

Handle NOWPayments webhook notifications (IPN).
Validates the signature, updates the payment status and creates a product subscription if the payment is successful.

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
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.NOWPaymentsApi(api_client)

    try:
        # Handle Webhook
        api_response = await api_instance.handle_now_webhook()
        print("The response of NOWPaymentsApi->handle_now_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NOWPaymentsApi->handle_now_webhook: %s\n" % e)
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

