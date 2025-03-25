# client.HealthCheckApi

All URIs are relative to *https://api.crypticorn.dev/v1/klines*

Method | HTTP request | Description
------------- | ------------- | -------------
[**index_get**](HealthCheckApi.md#index_get) | **GET** / | Index


# **index_get**
> BaseResponseHealthCheckResponse index_get()

Index

Health check endpoint to verify if the API is running.

### Example


```python
import client
from client.models.base_response_health_check_response import BaseResponseHealthCheckResponse
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
    api_instance = client.HealthCheckApi(api_client)

    try:
        # Index
        api_response = api_instance.index_get()
        print("The response of HealthCheckApi->index_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthCheckApi->index_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BaseResponseHealthCheckResponse**](BaseResponseHealthCheckResponse.md)

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

