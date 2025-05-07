# DataOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targets** | [**List[Target]**](Target.md) | The targets available on the latest data version. | 
**feature_sizes** | [**List[FeatureSize]**](FeatureSize.md) | The feature sizes available on the latest data version. | 

## Example

```python
from client.models.data_options import DataOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DataOptions from a JSON string
data_options_instance = DataOptions.from_json(json)
# print the JSON string representation of the object
print(DataOptions.to_json())

# convert the object into a dict
data_options_dict = data_options_instance.to_dict()
# create an instance of DataOptions from a dict
data_options_from_dict = DataOptions.from_dict(data_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


