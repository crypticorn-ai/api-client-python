# DataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, Dict[str, Dict[str, List[DataValueValueValueInner]]]]** |  | 
**coins** | [**List[Coins]**](Coins.md) |  | 
**feature_sizes** | [**List[FeatureSize]**](FeatureSize.md) |  | 
**targets** | [**Dict[str, TargetType]**](TargetType.md) |  | 
**versions** | **Dict[str, float]** |  | 
**latest_version** | [**DataVersion**](DataVersion.md) |  | 

## Example

```python
from client.models.data_info import DataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataInfo from a JSON string
data_info_instance = DataInfo.from_json(json)
# print the JSON string representation of the object
print(DataInfo.to_json())

# convert the object into a dict
data_info_dict = data_info_instance.to_dict()
# create an instance of DataInfo from a dict
data_info_from_dict = DataInfo.from_dict(data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


