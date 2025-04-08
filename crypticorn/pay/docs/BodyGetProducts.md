# BodyGetProducts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **Dict[str, object]** |  | [optional] 
**scopes** | [**List[Scope]**](Scope.md) |  | [optional] [default to []]

## Example

```python
from client.models.body_get_products import BodyGetProducts

# TODO update the JSON string below
json = "{}"
# create an instance of BodyGetProducts from a JSON string
body_get_products_instance = BodyGetProducts.from_json(json)
# print the JSON string representation of the object
print(BodyGetProducts.to_json())

# convert the object into a dict
body_get_products_dict = body_get_products_instance.to_dict()
# create an instance of BodyGetProducts from a dict
body_get_products_from_dict = BodyGetProducts.from_dict(body_get_products_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


