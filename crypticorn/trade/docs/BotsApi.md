# client.BotsApi

All URIs are relative to *http://localhost/v1/trade*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bot**](BotsApi.md#create_bot) | **POST** /bots | Create Bot
[**delete_bot**](BotsApi.md#delete_bot) | **DELETE** /bots/{id} | Delete Bot
[**get_bots**](BotsApi.md#get_bots) | **GET** /bots | Get Bots
[**update_bot**](BotsApi.md#update_bot) | **PUT** /bots/{id} | Update Bot


# **create_bot**
> object create_bot(bot_model, access_token=access_token)

Create Bot

### Example

* Bearer Authentication (HTTPBearer):

```python
import client
from client.models.bot_model import BotModel
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

# Configure Bearer authorization: HTTPBearer
configuration = client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.BotsApi(api_client)
    bot_model = client.BotModel() # BotModel | 
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Create Bot
        api_response = await api_instance.create_bot(bot_model, access_token=access_token)
        print("The response of BotsApi->create_bot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotsApi->create_bot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_model** | [**BotModel**](BotModel.md)|  | 
 **access_token** | **str**|  | [optional] 

### Return type

**object**

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

# **delete_bot**
> object delete_bot(id, access_token=access_token)

Delete Bot

### Example

* Bearer Authentication (HTTPBearer):

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

# Configure Bearer authorization: HTTPBearer
configuration = client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.BotsApi(api_client)
    id = 'id_example' # str | 
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Delete Bot
        api_response = await api_instance.delete_bot(id, access_token=access_token)
        print("The response of BotsApi->delete_bot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotsApi->delete_bot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **access_token** | **str**|  | [optional] 

### Return type

**object**

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

# **get_bots**
> List[BotModel] get_bots(include_deleted=include_deleted, limit=limit, offset=offset, access_token=access_token)

Get Bots

### Example

* Bearer Authentication (HTTPBearer):

```python
import client
from client.models.bot_model import BotModel
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

# Configure Bearer authorization: HTTPBearer
configuration = client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.BotsApi(api_client)
    include_deleted = False # bool |  (optional) (default to False)
    limit = 0 # int |  (optional) (default to 0)
    offset = 0 # int |  (optional) (default to 0)
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Get Bots
        api_response = await api_instance.get_bots(include_deleted=include_deleted, limit=limit, offset=offset, access_token=access_token)
        print("The response of BotsApi->get_bots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotsApi->get_bots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_deleted** | **bool**|  | [optional] [default to False]
 **limit** | **int**|  | [optional] [default to 0]
 **offset** | **int**|  | [optional] [default to 0]
 **access_token** | **str**|  | [optional] 

### Return type

[**List[BotModel]**](BotModel.md)

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

# **update_bot**
> object update_bot(id, bot_model, access_token=access_token)

Update Bot

### Example

* Bearer Authentication (HTTPBearer):

```python
import client
from client.models.bot_model import BotModel
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

# Configure Bearer authorization: HTTPBearer
configuration = client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.BotsApi(api_client)
    id = 'id_example' # str | 
    bot_model = client.BotModel() # BotModel | 
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Update Bot
        api_response = await api_instance.update_bot(id, bot_model, access_token=access_token)
        print("The response of BotsApi->update_bot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotsApi->update_bot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **bot_model** | [**BotModel**](BotModel.md)|  | 
 **access_token** | **str**|  | [optional] 

### Return type

**object**

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

