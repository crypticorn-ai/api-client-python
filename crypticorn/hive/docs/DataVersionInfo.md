# DataVersionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**DataVersion**](DataVersion.md) | Data version | 
**release_date** | **int** | Release date of the data version in unix timestamp | 

## Example

```python
from client.models.data_version_info import DataVersionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataVersionInfo from a JSON string
data_version_info_instance = DataVersionInfo.from_json(json)
# print the JSON string representation of the object
print(DataVersionInfo.to_json())

# convert the object into a dict
data_version_info_dict = data_version_info_instance.to_dict()
# create an instance of DataVersionInfo from a dict
data_version_info_from_dict = DataVersionInfo.from_dict(data_version_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


