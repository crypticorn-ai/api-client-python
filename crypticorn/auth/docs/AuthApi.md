# client.AuthApi

All URIs are relative to *http://localhost/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_user**](AuthApi.md#authorize_user) | **POST** /authorize | Authorize a user
[**get_google_auth_url**](AuthApi.md#get_google_auth_url) | **GET** /get-google-auth-url | Get Google Auth URL
[**oauth_callback**](AuthApi.md#oauth_callback) | **GET** /oauth-callback | OAuth Callback
[**refresh_token_info**](AuthApi.md#refresh_token_info) | **GET** /refresh-token-info | Refresh token info
[**refresh_token_scopes**](AuthApi.md#refresh_token_scopes) | **POST** /refresh-token-scopes | Refresh token scopes
[**rotate_tokens**](AuthApi.md#rotate_tokens) | **POST** /rotate-tokens | Rotate tokens
[**token_info**](AuthApi.md#token_info) | **GET** /token-info | Token info
[**verify**](AuthApi.md#verify) | **GET** /verify | Verify


# **authorize_user**
> AuthorizeUser200Response authorize_user(authorize_user_request)

Authorize a user

Authorize a user with email and password from the login page, uses a captcha to prevent bots.

### Example


```python
import client
from client.models.authorize_user200_response import AuthorizeUser200Response
from client.models.authorize_user_request import AuthorizeUserRequest
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
    api_instance = client.AuthApi(api_client)
    authorize_user_request = client.AuthorizeUserRequest() # AuthorizeUserRequest | 

    try:
        # Authorize a user
        api_response = await api_instance.authorize_user(authorize_user_request)
        print("The response of AuthApi->authorize_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->authorize_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorize_user_request** | [**AuthorizeUserRequest**](AuthorizeUserRequest.md)|  | 

### Return type

[**AuthorizeUser200Response**](AuthorizeUser200Response.md)

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

# **get_google_auth_url**
> str get_google_auth_url(origin)

Get Google Auth URL

Returns the Google Auth URL for the user to login with Google.

### Example


```python
import client
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
    api_instance = client.AuthApi(api_client)
    origin = 'origin_example' # str | 

    try:
        # Get Google Auth URL
        api_response = await api_instance.get_google_auth_url(origin)
        print("The response of AuthApi->get_google_auth_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_google_auth_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | 

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
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_callback**
> AuthorizeUser200Response oauth_callback(code, scope, authuser, prompt, origin)

OAuth Callback

Handles the OAuth callback from Google.

### Example


```python
import client
from client.models.authorize_user200_response import AuthorizeUser200Response
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
    api_instance = client.AuthApi(api_client)
    code = 'code_example' # str | 
    scope = 'scope_example' # str | 
    authuser = 'authuser_example' # str | 
    prompt = 'prompt_example' # str | 
    origin = 'origin_example' # str | 

    try:
        # OAuth Callback
        api_response = await api_instance.oauth_callback(code, scope, authuser, prompt, origin)
        print("The response of AuthApi->oauth_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->oauth_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **scope** | **str**|  | 
 **authuser** | **str**|  | 
 **prompt** | **str**|  | 
 **origin** | **str**|  | 

### Return type

[**AuthorizeUser200Response**](AuthorizeUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token_info**
> RefreshTokenInfo200Response refresh_token_info(x_refresh_token=x_refresh_token)

Refresh token info

Returns the user session record of the refresh token.

### Example


```python
import client
from client.models.refresh_token_info200_response import RefreshTokenInfo200Response
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
    api_instance = client.AuthApi(api_client)
    x_refresh_token = 'x_refresh_token_example' # str | The refresh token for rotating the access token. (optional)

    try:
        # Refresh token info
        api_response = await api_instance.refresh_token_info(x_refresh_token=x_refresh_token)
        print("The response of AuthApi->refresh_token_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->refresh_token_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_refresh_token** | **str**| The refresh token for rotating the access token. | [optional] 

### Return type

[**RefreshTokenInfo200Response**](RefreshTokenInfo200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token_scopes**
> RotateTokens200Response refresh_token_scopes(x_refresh_token=x_refresh_token)

Refresh token scopes

Refresh token scopes for a given user and a valid access token and a valid refresh token. This manually re-creates the access token with the latest scopes, in case the user changed their subscription status, access to certain features.

### Example


```python
import client
from client.models.rotate_tokens200_response import RotateTokens200Response
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
    api_instance = client.AuthApi(api_client)
    x_refresh_token = 'x_refresh_token_example' # str | The refresh token for rotating the access token. (optional)

    try:
        # Refresh token scopes
        api_response = await api_instance.refresh_token_scopes(x_refresh_token=x_refresh_token)
        print("The response of AuthApi->refresh_token_scopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->refresh_token_scopes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_refresh_token** | **str**| The refresh token for rotating the access token. | [optional] 

### Return type

[**RotateTokens200Response**](RotateTokens200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_tokens**
> RotateTokens200Response rotate_tokens(x_refresh_token=x_refresh_token)

Rotate tokens

Handles token rotation for user authentication. If access token is expired: Uses refresh token to generate a new access token. If access token is still valid: Extends (slides) the current token's expiration date. Returns both updated access and refresh tokens.

### Example


```python
import client
from client.models.rotate_tokens200_response import RotateTokens200Response
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
    api_instance = client.AuthApi(api_client)
    x_refresh_token = 'x_refresh_token_example' # str | The refresh token for rotating the access token. (optional)

    try:
        # Rotate tokens
        api_response = await api_instance.rotate_tokens(x_refresh_token=x_refresh_token)
        print("The response of AuthApi->rotate_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->rotate_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_refresh_token** | **str**| The refresh token for rotating the access token. | [optional] 

### Return type

[**RotateTokens200Response**](RotateTokens200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_info**
> TokenInfo200Response token_info(x_refresh_token=x_refresh_token)

Token info

Returns the payload of the access token.

### Example


```python
import client
from client.models.token_info200_response import TokenInfo200Response
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
    api_instance = client.AuthApi(api_client)
    x_refresh_token = 'x_refresh_token_example' # str | The refresh token for rotating the access token. (optional)

    try:
        # Token info
        api_response = await api_instance.token_info(x_refresh_token=x_refresh_token)
        print("The response of AuthApi->token_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->token_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_refresh_token** | **str**| The refresh token for rotating the access token. | [optional] 

### Return type

[**TokenInfo200Response**](TokenInfo200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify**
> Verify200Response verify()

Verify

Verifies the user is authenticated.

### Example


```python
import client
from client.models.verify200_response import Verify200Response
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
    api_instance = client.AuthApi(api_client)

    try:
        # Verify
        api_response = await api_instance.verify()
        print("The response of AuthApi->verify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->verify: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Verify200Response**](Verify200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

