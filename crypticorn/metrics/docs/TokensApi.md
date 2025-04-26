# client.TokensApi

All URIs are relative to *https://api.crypticorn.dev/v1/metrics*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stable_and_wrapped_tokens**](TokensApi.md#get_stable_and_wrapped_tokens) | **GET** /tokens/{token_type} | Get Stable Wrapped Tokens


# **get_stable_and_wrapped_tokens**
> List[Dict[str, object]] get_stable_and_wrapped_tokens(token_type)

Get Stable Wrapped Tokens

Get list of stable or wrapped tokens.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
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
    api_instance = client.TokensApi(api_client)
    token_type = 'token_type_example' # str | Token type (stable or wrapped)

    try:
        # Get Stable Wrapped Tokens
        api_response = await api_instance.get_stable_and_wrapped_tokens(token_type)
        print("The response of TokensApi->get_stable_and_wrapped_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->get_stable_and_wrapped_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_type** | **str**| Token type (stable or wrapped) | 

### Return type

**List[Dict[str, object]]**

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

