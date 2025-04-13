# ProductSubRead

Model for reading a product subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User ID | 
**product_id** | **str** | Product ID | 
**access_from** | **int** | Access from timestamp in milliseconds | 
**access_until** | **int** | Access until timestamp in milliseconds. 0 means unlimited. | 
**id** | **str** | UID of the product subscription | 

## Example

```python
from client.models.product_sub_read import ProductSubRead

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSubRead from a JSON string
product_sub_read_instance = ProductSubRead.from_json(json)
# print the JSON string representation of the object
print(ProductSubRead.to_json())

# convert the object into a dict
product_sub_read_dict = product_sub_read_instance.to_dict()
# create an instance of ProductSubRead from a dict
product_sub_read_from_dict = ProductSubRead.from_dict(product_sub_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


