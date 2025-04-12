# client.HealthCheckApi

All URIs are relative to *http://localhost/v1/metrics*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check**](HealthCheckApi.md#health_check) | **GET** / | Read Root


# **health_check**
> BaseResponseHealthCheckResponse health_check()

Read Root

Health check endpoint to verify if the API is running.

### Example


```python
import client
from client.models.base_response_health_check_response import BaseResponseHealthCheckResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/metrics
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/metrics"
)


# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.HealthCheckApi(api_client)

    try:
        # Read Root
        api_response = await api_instance.health_check()
        print("The response of HealthCheckApi->health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthCheckApi->health_check: %s\n" % e)
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

