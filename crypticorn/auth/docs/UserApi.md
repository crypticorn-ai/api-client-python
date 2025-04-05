# client.UserApi

All URIs are relative to *http://localhost/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UserApi.md#create_user) | **POST** /create-user | Create User
[**logout**](UserApi.md#logout) | **POST** /logout | Logout
[**resend_verification_email**](UserApi.md#resend_verification_email) | **POST** /resend-verification-email | Resend Verification Email
[**send_password_reset_email**](UserApi.md#send_password_reset_email) | **POST** /send-password-reset-email | Send Password Reset Email
[**update_user**](UserApi.md#update_user) | **POST** /update-user | Update User
[**user_by_id**](UserApi.md#user_by_id) | **GET** /user-by-id | User By Id
[**user_reset_password**](UserApi.md#user_reset_password) | **POST** /user-reset-password | User Reset Password
[**user_set_password**](UserApi.md#user_set_password) | **POST** /user-set-password | User Set Password
[**verify_email**](UserApi.md#verify_email) | **POST** /verify-email | Verify Email
[**whoami**](UserApi.md#whoami) | **GET** /whoami | Whoami


# **create_user**
> object create_user(create_user_request)

Create User

Creates a new user.

### Example


```python
import client
from client.models.create_user_request import CreateUserRequest
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
    api_instance = client.UserApi(api_client)
    create_user_request = client.CreateUserRequest() # CreateUserRequest | 

    try:
        # Create User
        api_response = await api_instance.create_user(create_user_request)
        print("The response of UserApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_request** | [**CreateUserRequest**](CreateUserRequest.md)|  | 

### Return type

**object**

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

# **logout**
> object logout()

Logout

Logs out the current user.

### Example

* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
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
    api_instance = client.UserApi(api_client)

    try:
        # Logout
        api_response = await api_instance.logout()
        print("The response of UserApi->logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->logout: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **resend_verification_email**
> object resend_verification_email(resend_verification_email_request)

Resend Verification Email

Resends the verification email to the user.

### Example


```python
import client
from client.models.resend_verification_email_request import ResendVerificationEmailRequest
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
    api_instance = client.UserApi(api_client)
    resend_verification_email_request = client.ResendVerificationEmailRequest() # ResendVerificationEmailRequest | 

    try:
        # Resend Verification Email
        api_response = await api_instance.resend_verification_email(resend_verification_email_request)
        print("The response of UserApi->resend_verification_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->resend_verification_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resend_verification_email_request** | [**ResendVerificationEmailRequest**](ResendVerificationEmailRequest.md)|  | 

### Return type

**object**

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

# **send_password_reset_email**
> object send_password_reset_email(resend_verification_email_request)

Send Password Reset Email

Sends a password reset email to the user.

### Example


```python
import client
from client.models.resend_verification_email_request import ResendVerificationEmailRequest
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
    api_instance = client.UserApi(api_client)
    resend_verification_email_request = client.ResendVerificationEmailRequest() # ResendVerificationEmailRequest | 

    try:
        # Send Password Reset Email
        api_response = await api_instance.send_password_reset_email(resend_verification_email_request)
        print("The response of UserApi->send_password_reset_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->send_password_reset_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resend_verification_email_request** | [**ResendVerificationEmailRequest**](ResendVerificationEmailRequest.md)|  | 

### Return type

**object**

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

# **update_user**
> object update_user(update_user_request)

Update User

Updates the user.

### Example


```python
import client
from client.models.update_user_request import UpdateUserRequest
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
    api_instance = client.UserApi(api_client)
    update_user_request = client.UpdateUserRequest() # UpdateUserRequest | 

    try:
        # Update User
        api_response = await api_instance.update_user(update_user_request)
        print("The response of UserApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | 

### Return type

**object**

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

# **user_by_id**
> Whoami200Response user_by_id(id)

User By Id

Returns the user by id.

### Example


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


# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.UserApi(api_client)
    id = 'id_example' # str | 

    try:
        # User By Id
        api_response = await api_instance.user_by_id(id)
        print("The response of UserApi->user_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Whoami200Response**](Whoami200Response.md)

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

# **user_reset_password**
> VerifyEmail200Response user_reset_password(user_reset_password_request)

User Reset Password

Resets the password for the user.

### Example


```python
import client
from client.models.user_reset_password_request import UserResetPasswordRequest
from client.models.verify_email200_response import VerifyEmail200Response
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
    api_instance = client.UserApi(api_client)
    user_reset_password_request = client.UserResetPasswordRequest() # UserResetPasswordRequest | 

    try:
        # User Reset Password
        api_response = await api_instance.user_reset_password(user_reset_password_request)
        print("The response of UserApi->user_reset_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_reset_password_request** | [**UserResetPasswordRequest**](UserResetPasswordRequest.md)|  | 

### Return type

[**VerifyEmail200Response**](VerifyEmail200Response.md)

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

# **user_set_password**
> object user_set_password(user_set_password_request)

User Set Password

Sets the password for the user.

### Example


```python
import client
from client.models.user_set_password_request import UserSetPasswordRequest
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
    api_instance = client.UserApi(api_client)
    user_set_password_request = client.UserSetPasswordRequest() # UserSetPasswordRequest | 

    try:
        # User Set Password
        api_response = await api_instance.user_set_password(user_set_password_request)
        print("The response of UserApi->user_set_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_set_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_set_password_request** | [**UserSetPasswordRequest**](UserSetPasswordRequest.md)|  | 

### Return type

**object**

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

# **verify_email**
> VerifyEmail200Response verify_email(verify_email_request)

Verify Email

Verifies the email of the user.

### Example


```python
import client
from client.models.verify_email200_response import VerifyEmail200Response
from client.models.verify_email_request import VerifyEmailRequest
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
    api_instance = client.UserApi(api_client)
    verify_email_request = client.VerifyEmailRequest() # VerifyEmailRequest | 

    try:
        # Verify Email
        api_response = await api_instance.verify_email(verify_email_request)
        print("The response of UserApi->verify_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->verify_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_email_request** | [**VerifyEmailRequest**](VerifyEmailRequest.md)|  | 

### Return type

[**VerifyEmail200Response**](VerifyEmail200Response.md)

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

# **whoami**
> Whoami200Response whoami(x_refresh_token=x_refresh_token)

Whoami

Returns the current user.

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
    api_instance = client.UserApi(api_client)
    x_refresh_token = 'x_refresh_token_example' # str | The refresh token for rotating the access token. (optional)

    try:
        # Whoami
        api_response = await api_instance.whoami(x_refresh_token=x_refresh_token)
        print("The response of UserApi->whoami:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->whoami: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_refresh_token** | **str**| The refresh token for rotating the access token. | [optional] 

### Return type

[**Whoami200Response**](Whoami200Response.md)

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

