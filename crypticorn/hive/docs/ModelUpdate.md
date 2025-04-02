# ModelUpdate

Pydantic model for model update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Model name | 

## Example

```python
from client.models.model_update import ModelUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelUpdate from a JSON string
model_update_instance = ModelUpdate.from_json(json)
# print the JSON string representation of the object
print(ModelUpdate.to_json())

# convert the object into a dict
model_update_dict = model_update_instance.to_dict()
# create an instance of ModelUpdate from a dict
model_update_from_dict = ModelUpdate.from_dict(model_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


