# ModelCreate

Base Pydantic model for model data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coin_id** | [**Coins**](Coins.md) | Coin ID for the model | 
**target** | [**Target**](Target.md) | Target variable for the model | 
**name** | **str** | Model name | 

## Example

```python
from client.models.model_create import ModelCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreate from a JSON string
model_create_instance = ModelCreate.from_json(json)
# print the JSON string representation of the object
print(ModelCreate.to_json())

# convert the object into a dict
model_create_dict = model_create_instance.to_dict()
# create an instance of ModelCreate from a dict
model_create_from_dict = ModelCreate.from_dict(model_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


