# BodyUpdateProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**ProductModel**](ProductModel.md) |  | 
**scopes** | [**List[Scope]**](Scope.md) |  | [optional] [default to []]

## Example

```python
from client.models.body_update_product import BodyUpdateProduct

# TODO update the JSON string below
json = "{}"
# create an instance of BodyUpdateProduct from a JSON string
body_update_product_instance = BodyUpdateProduct.from_json(json)
# print the JSON string representation of the object
print(BodyUpdateProduct.to_json())

# convert the object into a dict
body_update_product_dict = body_update_product_instance.to_dict()
# create an instance of BodyUpdateProduct from a dict
body_update_product_from_dict = BodyUpdateProduct.from_dict(body_update_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


