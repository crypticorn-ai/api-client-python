# client.NOWPaymentsApi

All URIs are relative to *http://localhost/v1/pay*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_now_invoice**](NOWPaymentsApi.md#create_now_invoice) | **POST** /now/invoice | Create Invoice
[**get_now_api_status**](NOWPaymentsApi.md#get_now_api_status) | **GET** /now/status | Get Status
[**send_now_webhook**](NOWPaymentsApi.md#send_now_webhook) | **POST** /now/webhook | Handle Webhook


# **create_now_invoice**
> NowCreateInvoiceRes create_now_invoice(now_create_invoice_req, access_token=access_token)

Create Invoice

Create a payment invoice with a payment link for customer completion

### Example

* OAuth Authentication (OAuth2PasswordBearer):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.NOWPaymentsApi(api_client)
    now_create_invoice_req = client.NowCreateInvoiceReq() # NowCreateInvoiceReq | 
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Create Invoice
        api_response = api_instance.create_now_invoice(now_create_invoice_req, access_token=access_token)
        print("The response of NOWPaymentsApi->create_now_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NOWPaymentsApi->create_now_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **now_create_invoice_req** | [**NowCreateInvoiceReq**](NowCreateInvoiceReq.md)|  | 
 **access_token** | **str**|  | [optional] 

### Return type

[**NowCreateInvoiceRes**](NowCreateInvoiceRes.md)

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

# **get_now_api_status**
> NowAPIStatusRes get_now_api_status()

Get Status

Get NOWPayments API status

### Example


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


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.NOWPaymentsApi(api_client)

    try:
        # Get Status
        api_response = api_instance.get_now_api_status()
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_now_webhook**
> object send_now_webhook(x_nowpayments_sig, now_webhook_payload)

Handle Webhook

Handle NOWPayments webhook notifications (IPN). Validates the signature, updates the payment status and creates a product subscription if the payment is successful.

### Example


```python
import client
from client.models.now_webhook_payload import NowWebhookPayload
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
    api_instance = client.NOWPaymentsApi(api_client)
    x_nowpayments_sig = 'x_nowpayments_sig_example' # str | Signature for the webhook
    now_webhook_payload = client.NowWebhookPayload() # NowWebhookPayload | 

    try:
        # Handle Webhook
        api_response = api_instance.send_now_webhook(x_nowpayments_sig, now_webhook_payload)
        print("The response of NOWPaymentsApi->send_now_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NOWPaymentsApi->send_now_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nowpayments_sig** | **str**| Signature for the webhook | 
 **now_webhook_payload** | [**NowWebhookPayload**](NowWebhookPayload.md)|  | 

### Return type

**object**

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

