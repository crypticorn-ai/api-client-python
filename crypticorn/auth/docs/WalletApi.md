# client.WalletApi

All URIs are relative to *http://localhost/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_wallet**](WalletApi.md#add_wallet) | **POST** /wallet/add | Add a wallet to the user
[**get_balances**](WalletApi.md#get_balances) | **GET** /wallet/balances | Get the balances of the user
[**list_wallets**](WalletApi.md#list_wallets) | **GET** /wallet/list | List wallets
[**unlink_wallet**](WalletApi.md#unlink_wallet) | **POST** /wallet/unlink | Unlink a wallet
[**verify_wallet**](WalletApi.md#verify_wallet) | **POST** /wallet/verify | Verify a wallet
[**wallet_verified**](WalletApi.md#wallet_verified) | **GET** /wallet/verified | Check if a wallet is verified


# **add_wallet**
> AddWallet200Response add_wallet(add_wallet_request, x_refresh_token=x_refresh_token)

Add a wallet to the user

Add a wallet to the user

### Example

* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.add_wallet200_response import AddWallet200Response
from client.models.add_wallet_request import AddWalletRequest
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
    api_instance = client.WalletApi(api_client)
    add_wallet_request = client.AddWalletRequest() # AddWalletRequest | 
    x_refresh_token = 'x_refresh_token_example' # str | The refresh token for rotating the access token. (optional)

    try:
        # Add a wallet to the user
        api_response = await api_instance.add_wallet(add_wallet_request, x_refresh_token=x_refresh_token)
        print("The response of WalletApi->add_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->add_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_wallet_request** | [**AddWalletRequest**](AddWalletRequest.md)|  | 
 **x_refresh_token** | **str**| The refresh token for rotating the access token. | [optional] 

### Return type

[**AddWallet200Response**](AddWallet200Response.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balances**
> ListWallets200ResponseUserValue get_balances(x_refresh_token=x_refresh_token)

Get the balances of the user

Get the balances of the user

### Example

* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.list_wallets200_response_user_value import ListWallets200ResponseUserValue
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
    api_instance = client.WalletApi(api_client)
    x_refresh_token = 'x_refresh_token_example' # str | The refresh token for rotating the access token. (optional)

    try:
        # Get the balances of the user
        api_response = await api_instance.get_balances(x_refresh_token=x_refresh_token)
        print("The response of WalletApi->get_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_balances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_refresh_token** | **str**| The refresh token for rotating the access token. | [optional] 

### Return type

[**ListWallets200ResponseUserValue**](ListWallets200ResponseUserValue.md)

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

# **list_wallets**
> ListWallets200Response list_wallets(x_refresh_token=x_refresh_token, limit=limit, offset=offset)

List wallets

List the wallets of the user

### Example

* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.list_wallets200_response import ListWallets200Response
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
    api_instance = client.WalletApi(api_client)
    x_refresh_token = 'x_refresh_token_example' # str | The refresh token for rotating the access token. (optional)
    limit = 10 # float |  (optional) (default to 10)
    offset = 0 # float |  (optional) (default to 0)

    try:
        # List wallets
        api_response = await api_instance.list_wallets(x_refresh_token=x_refresh_token, limit=limit, offset=offset)
        print("The response of WalletApi->list_wallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->list_wallets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_refresh_token** | **str**| The refresh token for rotating the access token. | [optional] 
 **limit** | **float**|  | [optional] [default to 10]
 **offset** | **float**|  | [optional] [default to 0]

### Return type

[**ListWallets200Response**](ListWallets200Response.md)

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

# **unlink_wallet**
> object unlink_wallet(unlink_wallet_request, x_refresh_token=x_refresh_token)

Unlink a wallet

Unlink a wallet from the user

### Example

* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.unlink_wallet_request import UnlinkWalletRequest
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
    api_instance = client.WalletApi(api_client)
    unlink_wallet_request = client.UnlinkWalletRequest() # UnlinkWalletRequest | 
    x_refresh_token = 'x_refresh_token_example' # str | The refresh token for rotating the access token. (optional)

    try:
        # Unlink a wallet
        api_response = await api_instance.unlink_wallet(unlink_wallet_request, x_refresh_token=x_refresh_token)
        print("The response of WalletApi->unlink_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->unlink_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unlink_wallet_request** | [**UnlinkWalletRequest**](UnlinkWalletRequest.md)|  | 
 **x_refresh_token** | **str**| The refresh token for rotating the access token. | [optional] 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_wallet**
> object verify_wallet(verify_wallet_request, x_refresh_token=x_refresh_token)

Verify a wallet

Verify a wallet by signing a message

### Example

* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.verify_wallet_request import VerifyWalletRequest
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
    api_instance = client.WalletApi(api_client)
    verify_wallet_request = client.VerifyWalletRequest() # VerifyWalletRequest | 
    x_refresh_token = 'x_refresh_token_example' # str | The refresh token for rotating the access token. (optional)

    try:
        # Verify a wallet
        api_response = await api_instance.verify_wallet(verify_wallet_request, x_refresh_token=x_refresh_token)
        print("The response of WalletApi->verify_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->verify_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_wallet_request** | [**VerifyWalletRequest**](VerifyWalletRequest.md)|  | 
 **x_refresh_token** | **str**| The refresh token for rotating the access token. | [optional] 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_verified**
> WalletVerified200Response wallet_verified(address, x_refresh_token=x_refresh_token)

Check if a wallet is verified

Check if a wallet is verified

### Example

* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.wallet_verified200_response import WalletVerified200Response
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
    api_instance = client.WalletApi(api_client)
    address = 'address_example' # str | 
    x_refresh_token = 'x_refresh_token_example' # str | The refresh token for rotating the access token. (optional)

    try:
        # Check if a wallet is verified
        api_response = await api_instance.wallet_verified(address, x_refresh_token=x_refresh_token)
        print("The response of WalletApi->wallet_verified:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->wallet_verified: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **x_refresh_token** | **str**| The refresh token for rotating the access token. | [optional] 

### Return type

[**WalletVerified200Response**](WalletVerified200Response.md)

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

