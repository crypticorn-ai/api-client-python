# client.ServiceApi

All URIs are relative to *http://localhost/v1/auth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_balances_by_email**](ServiceApi.md#get_balances_by_email) | **GET** /wallet/balances/email | Get the balances of a user by email


# **get_balances_by_email**
> ListWallets200ResponseUserValue get_balances_by_email(email, x_refresh_token=x_refresh_token)

Get the balances of a user by email

Get the balances of a user by email, meant to be used between services by the Discord bot to add token holders access to the channel.

### Example


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


# Enter a context with an instance of the API client
async with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ServiceApi(api_client)
    email = 'email_example' # str | 
    x_refresh_token = 'x_refresh_token_example' # str | The refresh token for rotating the access token. (optional)

    try:
        # Get the balances of a user by email
        api_response = await api_instance.get_balances_by_email(email, x_refresh_token=x_refresh_token)
        print("The response of ServiceApi->get_balances_by_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->get_balances_by_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **x_refresh_token** | **str**| The refresh token for rotating the access token. | [optional] 

### Return type

[**ListWallets200ResponseUserValue**](ListWallets200ResponseUserValue.md)

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

