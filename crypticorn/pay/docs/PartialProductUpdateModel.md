# PartialProductUpdateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**scopes** | [**List[Scope]**](Scope.md) |  | [optional] 
**duration** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from client.models.partial_product_update_model import PartialProductUpdateModel

# TODO update the JSON string below
json = "{}"
# create an instance of PartialProductUpdateModel from a JSON string
partial_product_update_model_instance = PartialProductUpdateModel.from_json(json)
# print the JSON string representation of the object
print(PartialProductUpdateModel.to_json())

# convert the object into a dict
partial_product_update_model_dict = partial_product_update_model_instance.to_dict()
# create an instance of PartialProductUpdateModel from a dict
partial_product_update_model_from_dict = PartialProductUpdateModel.from_dict(partial_product_update_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


