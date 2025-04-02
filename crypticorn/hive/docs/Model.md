# Model

Pydantic model for model response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **int** | Unique model identifier | 
**name** | **str** | Model name | 
**coin_id** | [**Coins**](Coins.md) | Coin ID | 
**target** | [**Target**](Target.md) | Target variable | 
**status** | [**ModelStatus**](ModelStatus.md) | Model status | 
**target_type** | [**TargetType**](TargetType.md) | Target type | 
**evaluations** | [**List[Evaluation]**](Evaluation.md) | Model evaluations | 
**user_id** | **str** | Developer user ID | 
**created_at** | **datetime** | Model creation timestamp | 
**updated_at** | **datetime** | Model update timestamp | 

## Example

```python
from client.models.model import Model

# TODO update the JSON string below
json = "{}"
# create an instance of Model from a JSON string
model_instance = Model.from_json(json)
# print the JSON string representation of the object
print(Model.to_json())

# convert the object into a dict
model_dict = model_instance.to_dict()
# create an instance of Model from a dict
model_from_dict = Model.from_dict(model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


