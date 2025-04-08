# BodyCreateProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**ProductModel**](ProductModel.md) |  | 
**scopes** | [**List[Scope]**](Scope.md) |  | [optional] [default to []]

## Example

```python
from client.models.body_create_product import BodyCreateProduct

# TODO update the JSON string below
json = "{}"
# create an instance of BodyCreateProduct from a JSON string
body_create_product_instance = BodyCreateProduct.from_json(json)
# print the JSON string representation of the object
print(BodyCreateProduct.to_json())

# convert the object into a dict
body_create_product_dict = body_create_product_instance.to_dict()
# create an instance of BodyCreateProduct from a dict
body_create_product_from_dict = BodyCreateProduct.from_dict(body_create_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


