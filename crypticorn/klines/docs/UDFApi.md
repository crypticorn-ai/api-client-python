# client.UDFApi

All URIs are relative to *https://api.crypticorn.dev/v1/klines*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config_udf_config_get**](UDFApi.md#get_config_udf_config_get) | **GET** /udf/config | Get Config
[**get_history_udf_history_get**](UDFApi.md#get_history_udf_history_get) | **GET** /udf/history | Get History
[**get_server_time_udf_time_get**](UDFApi.md#get_server_time_udf_time_get) | **GET** /udf/time | Get Server Time
[**get_symbol_info_udf_symbol_info_get**](UDFApi.md#get_symbol_info_udf_symbol_info_get) | **GET** /udf/symbol_info | Get Symbol Info
[**get_symbol_udf_symbols_get**](UDFApi.md#get_symbol_udf_symbols_get) | **GET** /udf/symbols | Get Symbol
[**options_handler_udf_path_options**](UDFApi.md#options_handler_udf_path_options) | **OPTIONS** /udf/{path} | Options Handler
[**search_symbols_udf_search_get**](UDFApi.md#search_symbols_udf_search_get) | **GET** /udf/search | Search Symbols


# **get_config_udf_config_get**
> UDFConfigResponse get_config_udf_config_get()

Get Config

### Example


```python
import client
from client.models.udf_config_response import UDFConfigResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/klines
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/klines"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.UDFApi(api_client)

    try:
        # Get Config
        api_response = api_instance.get_config_udf_config_get()
        print("The response of UDFApi->get_config_udf_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UDFApi->get_config_udf_config_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UDFConfigResponse**](UDFConfigResponse.md)

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

# **get_history_udf_history_get**
> ResponseGetHistoryUdfHistoryGet get_history_udf_history_get(symbol, resolution, var_from, to, countback=countback)

Get History

### Example


```python
import client
from client.models.resolution import Resolution
from client.models.response_get_history_udf_history_get import ResponseGetHistoryUdfHistoryGet
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/klines
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/klines"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.UDFApi(api_client)
    symbol = 'symbol_example' # str | 
    resolution = client.Resolution() # Resolution | 
    var_from = 56 # int | 
    to = 56 # int | 
    countback = 56 # int |  (optional)

    try:
        # Get History
        api_response = api_instance.get_history_udf_history_get(symbol, resolution, var_from, to, countback=countback)
        print("The response of UDFApi->get_history_udf_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UDFApi->get_history_udf_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 
 **resolution** | [**Resolution**](.md)|  | 
 **var_from** | **int**|  | 
 **to** | **int**|  | 
 **countback** | **int**|  | [optional] 

### Return type

[**ResponseGetHistoryUdfHistoryGet**](ResponseGetHistoryUdfHistoryGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_time_udf_time_get**
> object get_server_time_udf_time_get()

Get Server Time

### Example


```python
import client
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/klines
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/klines"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.UDFApi(api_client)

    try:
        # Get Server Time
        api_response = api_instance.get_server_time_udf_time_get()
        print("The response of UDFApi->get_server_time_udf_time_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UDFApi->get_server_time_udf_time_get: %s\n" % e)
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

# **get_symbol_info_udf_symbol_info_get**
> SymbolGroupResponse get_symbol_info_udf_symbol_info_get(group)

Get Symbol Info

Handle symbol info requests for different groups

### Example


```python
import client
from client.models.symbol_group_response import SymbolGroupResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/klines
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/klines"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.UDFApi(api_client)
    group = 'group_example' # str | 

    try:
        # Get Symbol Info
        api_response = api_instance.get_symbol_info_udf_symbol_info_get(group)
        print("The response of UDFApi->get_symbol_info_udf_symbol_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UDFApi->get_symbol_info_udf_symbol_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**|  | 

### Return type

[**SymbolGroupResponse**](SymbolGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_symbol_udf_symbols_get**
> SymbolInfoResponse get_symbol_udf_symbols_get(symbol)

Get Symbol

### Example


```python
import client
from client.models.symbol_info_response import SymbolInfoResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/klines
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/klines"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.UDFApi(api_client)
    symbol = 'symbol_example' # str | 

    try:
        # Get Symbol
        api_response = api_instance.get_symbol_udf_symbols_get(symbol)
        print("The response of UDFApi->get_symbol_udf_symbols_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UDFApi->get_symbol_udf_symbols_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 

### Return type

[**SymbolInfoResponse**](SymbolInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_handler_udf_path_options**
> object options_handler_udf_path_options(path)

Options Handler

Handle OPTIONS requests for all UDF endpoints

### Example


```python
import client
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/klines
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/klines"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.UDFApi(api_client)
    path = 'path_example' # str | 

    try:
        # Options Handler
        api_response = api_instance.options_handler_udf_path_options(path)
        print("The response of UDFApi->options_handler_udf_path_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UDFApi->options_handler_udf_path_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_symbols_udf_search_get**
> List[SearchSymbolResponse] search_symbols_udf_search_get(query, limit=limit)

Search Symbols

Called when a user searches for symbols in TradingView

### Example


```python
import client
from client.models.search_symbol_response import SearchSymbolResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/klines
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/klines"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.UDFApi(api_client)
    query = 'query_example' # str | 
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Search Symbols
        api_response = api_instance.search_symbols_udf_search_get(query, limit=limit)
        print("The response of UDFApi->search_symbols_udf_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UDFApi->search_symbols_udf_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**List[SearchSymbolResponse]**](SearchSymbolResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

