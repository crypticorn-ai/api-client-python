# client.StatusApi

All URIs are relative to *http://localhost/v1/pay*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config**](StatusApi.md#get_config) | **GET** /config | Config
[**get_time**](StatusApi.md#get_time) | **GET** /time | Time
[**ping**](StatusApi.md#ping) | **GET** / | Ping


# **get_config**
> Dict[str, object] get_config()

Config

Returns the version of the crypticorn library and the environment.

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
    api_instance = client.StatusApi(api_client)

    try:
        # Config
        api_response = await api_instance.get_config()
        print("The response of StatusApi->get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusApi->get_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time**
> str get_time(type=type)

Time

Returns the current time in the specified format.

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
    api_instance = client.StatusApi(api_client)
    type = iso # str |  (optional) (default to iso)

    try:
        # Time
        api_response = await api_instance.get_time(type=type)
        print("The response of StatusApi->get_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusApi->get_time: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] [default to iso]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping**
> str ping()

Ping

Returns 'OK' if the API is running.

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
    api_instance = client.StatusApi(api_client)

    try:
        # Ping
        api_response = await api_instance.ping()
        print("The response of StatusApi->ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusApi->ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

