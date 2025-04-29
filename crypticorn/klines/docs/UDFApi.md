# client.UDFApi

All URIs are relative to *http://localhost/v1/klines*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_symbol**](UDFApi.md#get_symbol) | **GET** /udf/symbols | Get Symbol
[**get_symbol_info**](UDFApi.md#get_symbol_info) | **GET** /udf/symbol_info | Get Symbol Info
[**get_udf_config**](UDFApi.md#get_udf_config) | **GET** /udf/config | Get Config
[**get_udf_history**](UDFApi.md#get_udf_history) | **GET** /udf/history | Get History
[**options_handler**](UDFApi.md#options_handler) | **OPTIONS** /udf/{path} | Options Handler
[**search_symbols**](UDFApi.md#search_symbols) | **GET** /udf/search | Search Symbols


# **get_symbol**
> SymbolInfo get_symbol(symbol)

Get Symbol

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.symbol_info import SymbolInfo
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/klines
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/klines"
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
    api_instance = client.UDFApi(api_client)
    symbol = 'symbol_example' # str | 

    try:
        # Get Symbol
        api_response = await api_instance.get_symbol(symbol)
        print("The response of UDFApi->get_symbol:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UDFApi->get_symbol: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 

### Return type

[**SymbolInfo**](SymbolInfo.md)

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

# **get_symbol_info**
> SymbolGroup get_symbol_info(group)

Get Symbol Info

Handle symbol info requests for different groups

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.symbol_group import SymbolGroup
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/klines
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/klines"
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
    api_instance = client.UDFApi(api_client)
    group = 'group_example' # str | 

    try:
        # Get Symbol Info
        api_response = await api_instance.get_symbol_info(group)
        print("The response of UDFApi->get_symbol_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UDFApi->get_symbol_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**|  | 

### Return type

[**SymbolGroup**](SymbolGroup.md)

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

# **get_udf_config**
> UDFConfig get_udf_config()

Get Config

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.udf_config import UDFConfig
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/klines
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/klines"
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
    api_instance = client.UDFApi(api_client)

    try:
        # Get Config
        api_response = await api_instance.get_udf_config()
        print("The response of UDFApi->get_udf_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UDFApi->get_udf_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UDFConfig**](UDFConfig.md)

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

# **get_udf_history**
> OHLCVHistory get_udf_history(symbol, resolution, var_from, to, countback=countback)

Get History

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.ohlcv_history import OHLCVHistory
from client.models.resolution import Resolution
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/klines
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/klines"
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
    api_instance = client.UDFApi(api_client)
    symbol = 'symbol_example' # str | 
    resolution = client.Resolution() # Resolution | 
    var_from = 56 # int | 
    to = 56 # int | 
    countback = 56 # int |  (optional)

    try:
        # Get History
        api_response = await api_instance.get_udf_history(symbol, resolution, var_from, to, countback=countback)
        print("The response of UDFApi->get_udf_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UDFApi->get_udf_history: %s\n" % e)
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

[**OHLCVHistory**](OHLCVHistory.md)

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

# **options_handler**
> object options_handler(path)

Options Handler

Handle OPTIONS requests for all UDF endpoints

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/klines
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/klines"
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
    api_instance = client.UDFApi(api_client)
    path = 'path_example' # str | 

    try:
        # Options Handler
        api_response = await api_instance.options_handler(path)
        print("The response of UDFApi->options_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UDFApi->options_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

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
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_symbols**
> List[SearchSymbol] search_symbols(query, limit=limit)

Search Symbols

Called when a user searches for symbols in TradingView

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.search_symbol import SearchSymbol
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/klines
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/klines"
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
    api_instance = client.UDFApi(api_client)
    query = 'query_example' # str | 
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Search Symbols
        api_response = await api_instance.search_symbols(query, limit=limit)
        print("The response of UDFApi->search_symbols:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UDFApi->search_symbols: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**List[SearchSymbol]**](SearchSymbol.md)

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

