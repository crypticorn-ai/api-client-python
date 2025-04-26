# client.APIKeysApi

All URIs are relative to *http://127.0.0.1:3000/v1/trade*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_exchange_key**](APIKeysApi.md#create_exchange_key) | **POST** /api-keys | Post Exchange Key
[**delete_exchange_key**](APIKeysApi.md#delete_exchange_key) | **DELETE** /api-keys/{id} | Delete Exchange Key
[**get_exchange_key_by_id**](APIKeysApi.md#get_exchange_key_by_id) | **GET** /api-keys/{id} | Get Exchange Key By Id
[**get_exchange_keys**](APIKeysApi.md#get_exchange_keys) | **GET** /api-keys | Get Exchange Keys
[**update_exchange_key**](APIKeysApi.md#update_exchange_key) | **PUT** /api-keys/{id} | Put Exchange Key


# **create_exchange_key**
> object create_exchange_key(exchange_key_model)

Post Exchange Key

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.exchange_key_model import ExchangeKeyModel
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:3000/v1/trade
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://127.0.0.1:3000/v1/trade"
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
    api_instance = client.APIKeysApi(api_client)
    exchange_key_model = client.ExchangeKeyModel() # ExchangeKeyModel | 

    try:
        # Post Exchange Key
        api_response = await api_instance.create_exchange_key(exchange_key_model)
        print("The response of APIKeysApi->create_exchange_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->create_exchange_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_key_model** | [**ExchangeKeyModel**](ExchangeKeyModel.md)|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_exchange_key**
> object delete_exchange_key(id)

Delete Exchange Key

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:3000/v1/trade
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://127.0.0.1:3000/v1/trade"
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
    api_instance = client.APIKeysApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Exchange Key
        api_response = await api_instance.delete_exchange_key(id)
        print("The response of APIKeysApi->delete_exchange_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->delete_exchange_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

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

# **get_exchange_key_by_id**
> ExchangeKeyModel get_exchange_key_by_id(id)

Get Exchange Key By Id

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.exchange_key_model import ExchangeKeyModel
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:3000/v1/trade
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://127.0.0.1:3000/v1/trade"
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
    api_instance = client.APIKeysApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Exchange Key By Id
        api_response = await api_instance.get_exchange_key_by_id(id)
        print("The response of APIKeysApi->get_exchange_key_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->get_exchange_key_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ExchangeKeyModel**](ExchangeKeyModel.md)

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

# **get_exchange_keys**
> List[ExchangeKeyModel] get_exchange_keys(limit=limit, offset=offset)

Get Exchange Keys

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.exchange_key_model import ExchangeKeyModel
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:3000/v1/trade
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://127.0.0.1:3000/v1/trade"
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
    api_instance = client.APIKeysApi(api_client)
    limit = 0 # int |  (optional) (default to 0)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Get Exchange Keys
        api_response = await api_instance.get_exchange_keys(limit=limit, offset=offset)
        print("The response of APIKeysApi->get_exchange_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->get_exchange_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 0]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[ExchangeKeyModel]**](ExchangeKeyModel.md)

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

# **update_exchange_key**
> object update_exchange_key(id, exchange_key_model)

Put Exchange Key

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.exchange_key_model import ExchangeKeyModel
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:3000/v1/trade
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://127.0.0.1:3000/v1/trade"
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
    api_instance = client.APIKeysApi(api_client)
    id = 'id_example' # str | 
    exchange_key_model = client.ExchangeKeyModel() # ExchangeKeyModel | 

    try:
        # Put Exchange Key
        api_response = await api_instance.update_exchange_key(id, exchange_key_model)
        print("The response of APIKeysApi->update_exchange_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->update_exchange_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **exchange_key_model** | [**ExchangeKeyModel**](ExchangeKeyModel.md)|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

