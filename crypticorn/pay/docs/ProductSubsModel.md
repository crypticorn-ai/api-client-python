# ProductSubsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**user_id** | **str** | User ID | 
**product_id** | **str** | Product ID | 
**access_from** | **int** | Access from timestamp in milliseconds | 
**access_until** | **int** | Access until timestamp in milliseconds. 0 means unlimited. | 

## Example

```python
from client.models.product_subs_model import ProductSubsModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSubsModel from a JSON string
product_subs_model_instance = ProductSubsModel.from_json(json)
# print the JSON string representation of the object
print(ProductSubsModel.to_json())

# convert the object into a dict
product_subs_model_dict = product_subs_model_instance.to_dict()
# create an instance of ProductSubsModel from a dict
product_subs_model_from_dict = ProductSubsModel.from_dict(product_subs_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


