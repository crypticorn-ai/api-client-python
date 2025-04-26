# client.LogsApi

All URIs are relative to *https://api.crypticorn.dev/v1/metrics*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metrics_error_logs**](LogsApi.md#get_metrics_error_logs) | **GET** /error_logs | Get Error Logs


# **get_metrics_error_logs**
> List[str] get_metrics_error_logs(severity=severity, start_timestamp=start_timestamp, end_timestamp=end_timestamp)

Get Error Logs

Get error logs with filtering options.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.severity import Severity
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/metrics
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/metrics"
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
    api_instance = client.LogsApi(api_client)
    severity = client.Severity() # Severity | Severity level of errors to fetch (optional)
    start_timestamp = 1745616674 # int | Start timestamp for which to fetch error logs (optional) (default to 1745616674)
    end_timestamp = 1745703074 # int | End timestamp for which to fetch error logs (optional) (default to 1745703074)

    try:
        # Get Error Logs
        api_response = await api_instance.get_metrics_error_logs(severity=severity, start_timestamp=start_timestamp, end_timestamp=end_timestamp)
        print("The response of LogsApi->get_metrics_error_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogsApi->get_metrics_error_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **severity** | [**Severity**](.md)| Severity level of errors to fetch | [optional] 
 **start_timestamp** | **int**| Start timestamp for which to fetch error logs | [optional] [default to 1745616674]
 **end_timestamp** | **int**| End timestamp for which to fetch error logs | [optional] [default to 1745703074]

### Return type

**List[str]**

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

