# DataDownloadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coin** | [**Coins**](Coins.md) |  | 
**feature_size** | [**FeatureSize**](FeatureSize.md) |  | 
**version** | [**DataVersion**](DataVersion.md) |  | 
**target** | [**Target**](Target.md) |  | 
**links** | [**DownloadLinks**](DownloadLinks.md) |  | 

## Example

```python
from client.models.data_download_response import DataDownloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataDownloadResponse from a JSON string
data_download_response_instance = DataDownloadResponse.from_json(json)
# print the JSON string representation of the object
print(DataDownloadResponse.to_json())

# convert the object into a dict
data_download_response_dict = data_download_response_instance.to_dict()
# create an instance of DataDownloadResponse from a dict
data_download_response_from_dict = DataDownloadResponse.from_dict(data_download_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


