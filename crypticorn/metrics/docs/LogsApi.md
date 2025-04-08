# client.LogsApi

All URIs are relative to *https://api.crypticorn.dev/v1/metrics*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metrics_error_logs**](LogsApi.md#get_metrics_error_logs) | **GET** /error_logs | Get Error Logs


# **get_metrics_error_logs**
> BaseResponseListDict get_metrics_error_logs(severity=severity, start_timestamp=start_timestamp, end_timestamp=end_timestamp)

Get Error Logs

Get error logs with filtering options.

### Example


```python
import client
from client.models.base_response_list_dict import BaseResponseListDict
from client.models.severity import Severity
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.crypticorn.dev/v1/metrics
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://api.crypticorn.dev/v1/metrics"
)


# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.LogsApi(api_client)
    severity = client.Severity() # Severity | Severity level of errors to fetch (optional)
    start_timestamp = 1743855414 # int | Start timestamp for which to fetch error logs (optional) (default to 1743855414)
    end_timestamp = 1743941814 # int | End timestamp for which to fetch error logs (optional) (default to 1743941814)

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
 **start_timestamp** | **int**| Start timestamp for which to fetch error logs | [optional] [default to 1743855414]
 **end_timestamp** | **int**| End timestamp for which to fetch error logs | [optional] [default to 1743941814]

### Return type

[**BaseResponseListDict**](BaseResponseListDict.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with error logs |  -  |
**400** | Invalid request parameters |  -  |
**404** | No data found |  -  |
**500** | Internal server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

