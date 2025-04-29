# client.StrategiesApi

All URIs are relative to *http://localhost/v1/trade*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_strategy**](StrategiesApi.md#create_strategy) | **POST** /strategies | Create Strategy
[**get_strategies**](StrategiesApi.md#get_strategies) | **GET** /strategies | Get Strategies
[**kill_strategy**](StrategiesApi.md#kill_strategy) | **DELETE** /strategies/{id} | Kill Strategy
[**update_strategy**](StrategiesApi.md#update_strategy) | **PUT** /strategies/{id} | Update Strategy


# **create_strategy**
> object create_strategy(strategy_model_input)

Create Strategy

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.strategy_model_input import StrategyModelInput
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
    api_instance = client.StrategiesApi(api_client)
    strategy_model_input = client.StrategyModelInput() # StrategyModelInput | 

    try:
        # Create Strategy
        api_response = await api_instance.create_strategy(strategy_model_input)
        print("The response of StrategiesApi->create_strategy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StrategiesApi->create_strategy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strategy_model_input** | [**StrategyModelInput**](StrategyModelInput.md)|  | 

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
**201** | Successful Response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_strategies**
> List[StrategyModelOutput] get_strategies(limit=limit, offset=offset)

Get Strategies

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.strategy_model_output import StrategyModelOutput
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
    api_instance = client.StrategiesApi(api_client)
    limit = 0 # int |  (optional) (default to 0)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Get Strategies
        api_response = await api_instance.get_strategies(limit=limit, offset=offset)
        print("The response of StrategiesApi->get_strategies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StrategiesApi->get_strategies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 0]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[StrategyModelOutput]**](StrategyModelOutput.md)

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

# **kill_strategy**
> object kill_strategy(id)

Kill Strategy

Kills a strategy by disabling it and deleting all bots associated with it.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

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
    api_instance = client.StrategiesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Kill Strategy
        api_response = await api_instance.kill_strategy(id)
        print("The response of StrategiesApi->kill_strategy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StrategiesApi->kill_strategy: %s\n" % e)
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
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_strategy**
> object update_strategy(id, strategy_model_input)

Update Strategy

Updates a strategy. If the strategy is being disabled, all bots associated with it will be set to stopping.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.strategy_model_input import StrategyModelInput
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
    api_instance = client.StrategiesApi(api_client)
    id = 'id_example' # str | 
    strategy_model_input = client.StrategyModelInput() # StrategyModelInput | 

    try:
        # Update Strategy
        api_response = await api_instance.update_strategy(id, strategy_model_input)
        print("The response of StrategiesApi->update_strategy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StrategiesApi->update_strategy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **strategy_model_input** | [**StrategyModelInput**](StrategyModelInput.md)|  | 

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

