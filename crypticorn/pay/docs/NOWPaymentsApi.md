# client.NOWPaymentsApi

All URIs are relative to *http://localhost/v1/pay*

Method | HTTP request | Description
------------- | ------------- | -------------
[**now_create_invoice**](NOWPaymentsApi.md#now_create_invoice) | **POST** /now/invoice | Create Invoice
[**now_get_api_status**](NOWPaymentsApi.md#now_get_api_status) | **GET** /now/status | Get Api Status
[**now_get_currencies**](NOWPaymentsApi.md#now_get_currencies) | **GET** /now/currencies | Get Currencies
[**now_get_estimate_price**](NOWPaymentsApi.md#now_get_estimate_price) | **POST** /now/estimate | Get Estimate Price
[**now_get_minimum_payment_amount**](NOWPaymentsApi.md#now_get_minimum_payment_amount) | **POST** /now/min-amount | Get Minimum Payment Amount
[**now_get_payment_status**](NOWPaymentsApi.md#now_get_payment_status) | **GET** /now/payment/{payment_id} | Get Payment Status
[**now_get_payments_list**](NOWPaymentsApi.md#now_get_payments_list) | **GET** /now/payment | Get Payments List
[**now_handle_webhook**](NOWPaymentsApi.md#now_handle_webhook) | **POST** /now/webhook | Handle Nowpayments Webhook


# **now_create_invoice**
> CreateInvoiceRes now_create_invoice(create_invoice_req, access_token=access_token)

Create Invoice

Create a payment invoice with a payment link for customer completion

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
from client.models.create_invoice_req import CreateInvoiceReq
from client.models.create_invoice_res import CreateInvoiceRes
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
    create_invoice_req = client.CreateInvoiceReq() # CreateInvoiceReq | 
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Create Invoice
        api_response = api_instance.now_create_invoice(create_invoice_req, access_token=access_token)
        print("The response of NOWPaymentsApi->now_create_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NOWPaymentsApi->now_create_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_invoice_req** | [**CreateInvoiceReq**](CreateInvoiceReq.md)|  | 
 **access_token** | **str**|  | [optional] 

### Return type

[**CreateInvoiceRes**](CreateInvoiceRes.md)

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

# **now_get_api_status**
> APIStatusRes now_get_api_status()

Get Api Status

Get NOWPayments API status

### Example


```python
import client
from client.models.api_status_res import APIStatusRes
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
        # Get Api Status
        api_response = api_instance.now_get_api_status()
        print("The response of NOWPaymentsApi->now_get_api_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NOWPaymentsApi->now_get_api_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**APIStatusRes**](APIStatusRes.md)

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

# **now_get_currencies**
> GetCurrenciesRes now_get_currencies(access_token=access_token)

Get Currencies

Get all available cryptocurrencies

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
from client.models.get_currencies_res import GetCurrenciesRes
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
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Get Currencies
        api_response = api_instance.now_get_currencies(access_token=access_token)
        print("The response of NOWPaymentsApi->now_get_currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NOWPaymentsApi->now_get_currencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | [optional] 

### Return type

[**GetCurrenciesRes**](GetCurrenciesRes.md)

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

# **now_get_estimate_price**
> EstimatePriceRes now_get_estimate_price(estimate_price_req, access_token=access_token)

Get Estimate Price

Get price estimate for currency conversion

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
from client.models.estimate_price_req import EstimatePriceReq
from client.models.estimate_price_res import EstimatePriceRes
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
    estimate_price_req = client.EstimatePriceReq() # EstimatePriceReq | 
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Get Estimate Price
        api_response = api_instance.now_get_estimate_price(estimate_price_req, access_token=access_token)
        print("The response of NOWPaymentsApi->now_get_estimate_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NOWPaymentsApi->now_get_estimate_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **estimate_price_req** | [**EstimatePriceReq**](EstimatePriceReq.md)|  | 
 **access_token** | **str**|  | [optional] 

### Return type

[**EstimatePriceRes**](EstimatePriceRes.md)

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

# **now_get_minimum_payment_amount**
> MinAmountRes now_get_minimum_payment_amount(min_amount_req, access_token=access_token)

Get Minimum Payment Amount

Get minimum payment amount for a currency pair

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
from client.models.min_amount_req import MinAmountReq
from client.models.min_amount_res import MinAmountRes
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
    min_amount_req = client.MinAmountReq() # MinAmountReq | 
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Get Minimum Payment Amount
        api_response = api_instance.now_get_minimum_payment_amount(min_amount_req, access_token=access_token)
        print("The response of NOWPaymentsApi->now_get_minimum_payment_amount:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NOWPaymentsApi->now_get_minimum_payment_amount: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_amount_req** | [**MinAmountReq**](MinAmountReq.md)|  | 
 **access_token** | **str**|  | [optional] 

### Return type

[**MinAmountRes**](MinAmountRes.md)

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

# **now_get_payment_status**
> GetPaymentStatusRes now_get_payment_status(payment_id, access_token=access_token)

Get Payment Status

Get status of a specific payment

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
from client.models.get_payment_status_res import GetPaymentStatusRes
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
    payment_id = 56 # int | 
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Get Payment Status
        api_response = api_instance.now_get_payment_status(payment_id, access_token=access_token)
        print("The response of NOWPaymentsApi->now_get_payment_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NOWPaymentsApi->now_get_payment_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **int**|  | 
 **access_token** | **str**|  | [optional] 

### Return type

[**GetPaymentStatusRes**](GetPaymentStatusRes.md)

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

# **now_get_payments_list**
> GetPaymentsListRes now_get_payments_list(limit=limit, page=page, invoice_id=invoice_id, sort_by=sort_by, order_by=order_by, date_from=date_from, date_to=date_to, access_token=access_token)

Get Payments List

Get list of all payments with optional filtering and pagination

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
from client.models.get_payments_list_res import GetPaymentsListRes
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
    limit = 56 # int |  (optional)
    page = 56 # int |  (optional)
    invoice_id = 'invoice_id_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    date_from = 'date_from_example' # str |  (optional)
    date_to = 'date_to_example' # str |  (optional)
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Get Payments List
        api_response = api_instance.now_get_payments_list(limit=limit, page=page, invoice_id=invoice_id, sort_by=sort_by, order_by=order_by, date_from=date_from, date_to=date_to, access_token=access_token)
        print("The response of NOWPaymentsApi->now_get_payments_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NOWPaymentsApi->now_get_payments_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 
 **invoice_id** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **date_from** | **str**|  | [optional] 
 **date_to** | **str**|  | [optional] 
 **access_token** | **str**|  | [optional] 

### Return type

[**GetPaymentsListRes**](GetPaymentsListRes.md)

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

# **now_handle_webhook**
> object now_handle_webhook()

Handle Nowpayments Webhook

Handle NOWPayments webhook notifications (IPN). Validates the signature and forwards the payment status update to the auth service.

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
    api_instance = client.NOWPaymentsApi(api_client)

    try:
        # Handle Nowpayments Webhook
        api_response = api_instance.now_handle_webhook()
        print("The response of NOWPaymentsApi->now_handle_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NOWPaymentsApi->now_handle_webhook: %s\n" % e)
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

