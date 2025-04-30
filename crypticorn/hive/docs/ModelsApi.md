# client.ModelsApi

All URIs are relative to *http://localhost/v1/hive*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_model**](ModelsApi.md#create_model) | **POST** /model/creation | Create Model
[**delete_model**](ModelsApi.md#delete_model) | **DELETE** /model/{id} | Delete Model
[**evaluate_model**](ModelsApi.md#evaluate_model) | **POST** /model/evaluation/{id} | Evaluate Model
[**get_model**](ModelsApi.md#get_model) | **GET** /model/{id} | Get Model
[**get_model_by_name**](ModelsApi.md#get_model_by_name) | **GET** /model/by-name/{name} | Get Model By Name
[**get_models**](ModelsApi.md#get_models) | **GET** /model | Get All Models
[**update_model**](ModelsApi.md#update_model) | **PUT** /model/{id} | Update Model


# **create_model**
> Model create_model(model_create)

Create Model

Create a new model

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.model import Model
from client.models.model_create import ModelCreate
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/hive
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/hive"
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
    api_instance = client.ModelsApi(api_client)
    model_create = client.ModelCreate() # ModelCreate | 

    try:
        # Create Model
        api_response = await api_instance.create_model(model_create)
        print("The response of ModelsApi->create_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->create_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_create** | [**ModelCreate**](ModelCreate.md)|  | 

### Return type

[**Model**](Model.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model**
> delete_model(id)

Delete Model

Delete a model

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/hive
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/hive"
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
    api_instance = client.ModelsApi(api_client)
    id = 56 # int | Model ID to delete

    try:
        # Delete Model
        await api_instance.delete_model(id)
    except Exception as e:
        print("Exception when calling ModelsApi->delete_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Model ID to delete | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluate_model**
> EvaluationResponse evaluate_model(id, request_body, version=version)

Evaluate Model

Evaluate a model's predictions

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.data_version import DataVersion
from client.models.evaluation_response import EvaluationResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/hive
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/hive"
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
    api_instance = client.ModelsApi(api_client)
    id = 56 # int | Model ID to evaluate
    request_body = None # List[object] | 
    version = client.DataVersion() # DataVersion | Data version to evaluate against (optional)

    try:
        # Evaluate Model
        api_response = await api_instance.evaluate_model(id, request_body, version=version)
        print("The response of ModelsApi->evaluate_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->evaluate_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Model ID to evaluate | 
 **request_body** | [**List[object]**](object.md)|  | 
 **version** | [**DataVersion**](.md)| Data version to evaluate against | [optional] 

### Return type

[**EvaluationResponse**](EvaluationResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> Model get_model(id)

Get Model

Get a model by ID

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.model import Model
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/hive
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/hive"
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
    api_instance = client.ModelsApi(api_client)
    id = 56 # int | Model ID to get

    try:
        # Get Model
        api_response = await api_instance.get_model(id)
        print("The response of ModelsApi->get_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Model ID to get | 

### Return type

[**Model**](Model.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_by_name**
> Model get_model_by_name(name)

Get Model By Name

Get a model by name

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.model import Model
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/hive
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/hive"
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
    api_instance = client.ModelsApi(api_client)
    name = 'name_example' # str | Model name to get

    try:
        # Get Model By Name
        api_response = await api_instance.get_model_by_name(name)
        print("The response of ModelsApi->get_model_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_model_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Model name to get | 

### Return type

[**Model**](Model.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_models**
> List[Model] get_models(by_user=by_user, user_id=user_id)

Get All Models

List all models

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.model import Model
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/hive
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/hive"
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
    api_instance = client.ModelsApi(api_client)
    by_user = False # bool | Whether to get models by user. Else all models are returned. (optional) (default to False)
    user_id = 'user_id_example' # str | User ID to get models for. Only used if by_user is true. Default is current user. (optional)

    try:
        # Get All Models
        api_response = await api_instance.get_models(by_user=by_user, user_id=user_id)
        print("The response of ModelsApi->get_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **by_user** | **bool**| Whether to get models by user. Else all models are returned. | [optional] [default to False]
 **user_id** | **str**| User ID to get models for. Only used if by_user is true. Default is current user. | [optional] 

### Return type

[**List[Model]**](Model.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model**
> object update_model(id, model_update)

Update Model

Update a model's information

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.model_update import ModelUpdate
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/hive
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/hive"
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
    api_instance = client.ModelsApi(api_client)
    id = 56 # int | Model ID to update
    model_update = client.ModelUpdate() # ModelUpdate | 

    try:
        # Update Model
        api_response = await api_instance.update_model(id, model_update)
        print("The response of ModelsApi->update_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->update_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Model ID to update | 
 **model_update** | [**ModelUpdate**](ModelUpdate.md)|  | 

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
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

