# AddWallet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oob_code** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from client.models.add_wallet200_response import AddWallet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddWallet200Response from a JSON string
add_wallet200_response_instance = AddWallet200Response.from_json(json)
# print the JSON string representation of the object
print(AddWallet200Response.to_json())

# convert the object into a dict
add_wallet200_response_dict = add_wallet200_response_instance.to_dict()
# create an instance of AddWallet200Response from a dict
add_wallet200_response_from_dict = AddWallet200Response.from_dict(add_wallet200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


