# ProductUpdateModel


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
from client.models.product_update_model import ProductUpdateModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProductUpdateModel from a JSON string
product_update_model_instance = ProductUpdateModel.from_json(json)
# print the JSON string representation of the object
print(ProductUpdateModel.to_json())

# convert the object into a dict
product_update_model_dict = product_update_model_instance.to_dict()
# create an instance of ProductUpdateModel from a dict
product_update_model_from_dict = ProductUpdateModel.from_dict(product_update_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


