# ProductRead

Model for reading a product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Product name | 
**price** | **float** | Product price | 
**scopes** | [**List[Scope]**](Scope.md) |  | [optional] 
**duration** | **int** | Product duration in days. 0 means unlimited. | 
**description** | **str** | Product description | 
**is_active** | **bool** | Product is active | 
**id** | **str** | UID of the product | 

## Example

```python
from client.models.product_read import ProductRead

# TODO update the JSON string below
json = "{}"
# create an instance of ProductRead from a JSON string
product_read_instance = ProductRead.from_json(json)
# print the JSON string representation of the object
print(ProductRead.to_json())

# convert the object into a dict
product_read_dict = product_read_instance.to_dict()
# create an instance of ProductRead from a dict
product_read_from_dict = ProductRead.from_dict(product_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


