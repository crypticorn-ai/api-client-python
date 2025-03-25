# client.NotificationsApi

All URIs are relative to *http://localhost/v1/trade*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification**](NotificationsApi.md#create_notification) | **POST** /notifications | Create Notification
[**delete_notification**](NotificationsApi.md#delete_notification) | **DELETE** /notifications/{id} | Delete Notification
[**delete_notifications**](NotificationsApi.md#delete_notifications) | **DELETE** /notifications | Delete Notifications
[**get_notifications**](NotificationsApi.md#get_notifications) | **GET** /notifications | Get Notifications
[**update_notification**](NotificationsApi.md#update_notification) | **PUT** /notifications/{id} | Update Notification
[**update_notifications**](NotificationsApi.md#update_notifications) | **PUT** /notifications | Update Notifications


# **create_notification**
> object create_notification(notification_model, access_token=access_token)

Create Notification

Create a new notification

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
from client.models.notification_model import NotificationModel
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/trade
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/trade"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.NotificationsApi(api_client)
    notification_model = client.NotificationModel() # NotificationModel | 
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Create Notification
        api_response = api_instance.create_notification(notification_model, access_token=access_token)
        print("The response of NotificationsApi->create_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->create_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_model** | [**NotificationModel**](NotificationModel.md)|  | 
 **access_token** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification**
> object delete_notification(id, access_token=access_token)

Delete Notification

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/trade
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/trade"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.NotificationsApi(api_client)
    id = 'id_example' # str | 
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Delete Notification
        api_response = api_instance.delete_notification(id, access_token=access_token)
        print("The response of NotificationsApi->delete_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->delete_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **access_token** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notifications**
> object delete_notifications(access_token=access_token)

Delete Notifications

Delete all notifications for the authenticated user

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/trade
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/trade"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.NotificationsApi(api_client)
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Delete Notifications
        api_response = api_instance.delete_notifications(access_token=access_token)
        print("The response of NotificationsApi->delete_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->delete_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications**
> List[NotificationModel] get_notifications(limit=limit, offset=offset, access_token=access_token)

Get Notifications

Get all notifications for the authenticated user

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
from client.models.notification_model import NotificationModel
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/trade
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/trade"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.NotificationsApi(api_client)
    limit = 0 # int |  (optional) (default to 0)
    offset = 0 # int |  (optional) (default to 0)
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Get Notifications
        api_response = api_instance.get_notifications(limit=limit, offset=offset, access_token=access_token)
        print("The response of NotificationsApi->get_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 0]
 **offset** | **int**|  | [optional] [default to 0]
 **access_token** | **str**|  | [optional] 

### Return type

[**List[NotificationModel]**](NotificationModel.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification**
> object update_notification(id, viewed, sent, access_token=access_token)

Update Notification

Update a notification's viewed status

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/trade
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/trade"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.NotificationsApi(api_client)
    id = 'id_example' # str | 
    viewed = True # bool | 
    sent = True # bool | 
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Update Notification
        api_response = api_instance.update_notification(id, viewed, sent, access_token=access_token)
        print("The response of NotificationsApi->update_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->update_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **viewed** | **bool**|  | 
 **sent** | **bool**|  | 
 **access_token** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notifications**
> object update_notifications(viewed, sent, access_token=access_token)

Update Notifications

Bulk update notifications

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import client
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/trade
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/trade"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.NotificationsApi(api_client)
    viewed = True # bool | 
    sent = True # bool | 
    access_token = 'access_token_example' # str |  (optional)

    try:
        # Update Notifications
        api_response = api_instance.update_notifications(viewed, sent, access_token=access_token)
        print("The response of NotificationsApi->update_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->update_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewed** | **bool**|  | 
 **sent** | **bool**|  | 
 **access_token** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

