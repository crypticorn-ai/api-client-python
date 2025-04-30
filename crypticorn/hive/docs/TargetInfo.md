# TargetInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**Target**](Target.md) | Target name | 
**type** | [**TargetType**](TargetType.md) | Target type | 
**version** | [**DataVersion**](DataVersion.md) | Data version | 

## Example

```python
from client.models.target_info import TargetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TargetInfo from a JSON string
target_info_instance = TargetInfo.from_json(json)
# print the JSON string representation of the object
print(TargetInfo.to_json())

# convert the object into a dict
target_info_dict = target_info_instance.to_dict()
# create an instance of TargetInfo from a dict
target_info_from_dict = TargetInfo.from_dict(target_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


