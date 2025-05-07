# DataInfo

The complete data information for all versions, coins, feature sizes and targets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, Dict[str, DataOptions]]** | The complete data information for all versions, coins, feature sizes and targets. | 
**coins** | [**List[Coins]**](Coins.md) | The coins available on the latest data version. | 
**feature_sizes** | [**List[FeatureSize]**](FeatureSize.md) | The feature sizes available on the latest data version. | 
**targets** | [**List[TargetInfo]**](TargetInfo.md) | The targets available on the latest data version. | 
**all_versions** | [**List[DataVersionInfo]**](DataVersionInfo.md) | All ever existing data versions. Some may not be publicly available yet. | 
**available_versions** | [**List[DataVersionInfo]**](DataVersionInfo.md) | All publicly available data versions. | 

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


