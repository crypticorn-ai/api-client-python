# client.DataApi

All URIs are relative to *http://localhost/v1/hive*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_data**](DataApi.md#download_data) | **GET** /data | Download Data
[**get_data_info**](DataApi.md#get_data_info) | **GET** /data/info | Get Data Info


# **download_data**
> DataDownloadResponse download_data(model_id, version, feature_size=feature_size)

Download Data

Get download links for model training data

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.data_download_response import DataDownloadResponse
from client.models.data_version import DataVersion
from client.models.feature_size import FeatureSize
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/hive
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/hive"
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
    api_instance = client.DataApi(api_client)
    model_id = 56 # int | Model ID
    version = client.DataVersion() # DataVersion | Data version. Default is the latest public version.
    feature_size = client.FeatureSize() # FeatureSize | Feature size (optional)

    try:
        # Download Data
        api_response = await api_instance.download_data(model_id, version, feature_size=feature_size)
        print("The response of DataApi->download_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->download_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **int**| Model ID | 
 **version** | [**DataVersion**](.md)| Data version. Default is the latest public version. | 
 **feature_size** | [**FeatureSize**](.md)| Feature size | [optional] 

### Return type

[**DataDownloadResponse**](DataDownloadResponse.md)

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

# **get_data_info**
> DataInfo get_data_info()

Get Data Info

Get information about available data and options for the latest data version

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (JWT) Authentication (HTTPBearer):

```python
import client
from client.models.data_info import DataInfo
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/v1/hive
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "http://localhost/v1/hive"
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
    api_instance = client.DataApi(api_client)

    try:
        # Get Data Info
        api_response = await api_instance.get_data_info()
        print("The response of DataApi->get_data_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->get_data_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DataInfo**](DataInfo.md)

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

