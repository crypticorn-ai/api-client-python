# client.AdminApi

All URIs are relative to *http://localhost/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**revoke_user_tokens**](AdminApi.md#revoke_user_tokens) | **POST** /revoke-user-tokens | Revoke user tokens
[**user_list**](AdminApi.md#user_list) | **GET** /user-list | User List


# **revoke_user_tokens**
> LogoutDefaultResponseIssuesInner revoke_user_tokens(revoke_user_tokens_request)

Revoke user tokens

Revoke all tokens for a given user, this resets the authentication state and requires them to login again.

### Example


```python
import client
from client.models.logout_default_response_issues_inner import LogoutDefaultResponseIssuesInner
from client.models.revoke_user_tokens_request import RevokeUserTokensRequest
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/auth"
)


# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.AdminApi(api_client)
    revoke_user_tokens_request = client.RevokeUserTokensRequest() # RevokeUserTokensRequest | 

    try:
        # Revoke user tokens
        api_response = await api_instance.revoke_user_tokens(revoke_user_tokens_request)
        print("The response of AdminApi->revoke_user_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->revoke_user_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revoke_user_tokens_request** | [**RevokeUserTokensRequest**](RevokeUserTokensRequest.md)|  | 

### Return type

[**LogoutDefaultResponseIssuesInner**](LogoutDefaultResponseIssuesInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_list**
> List[Whoami200Response] user_list()

User List

Returns the list of users.

### Example

* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.whoami200_response import Whoami200Response
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/auth
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/auth"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): HTTPBearer
configuration = client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.AdminApi(api_client)

    try:
        # User List
        api_response = await api_instance.user_list()
        print("The response of AdminApi->user_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->user_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Whoami200Response]**](Whoami200Response.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

