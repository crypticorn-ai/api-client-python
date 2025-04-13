# ProductCreate

Model for creating a product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Product name | 
**price** | **float** | Product price | 
**scopes** | [**List[Scope]**](Scope.md) |  | [optional] 
**duration** | **int** | Product duration in days. 0 means unlimited. | 
**description** | **str** | Product description | 
**is_active** | **bool** | Product is active | 

## Example

```python
from client.models.product_create import ProductCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCreate from a JSON string
product_create_instance = ProductCreate.from_json(json)
# print the JSON string representation of the object
print(ProductCreate.to_json())

# convert the object into a dict
product_create_dict = product_create_instance.to_dict()
# create an instance of ProductCreate from a dict
product_create_from_dict = ProductCreate.from_dict(product_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


