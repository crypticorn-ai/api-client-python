# AddWalletRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | 
**origin** | **str** |  | 
**address** | **str** |  | 
**chain_id** | **float** |  | [optional] [default to 1]
**statement** | **str** |  | [optional] [default to 'Sign in with Ethereum wallet']

## Example

```python
from client.models.add_wallet_request import AddWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddWalletRequest from a JSON string
add_wallet_request_instance = AddWalletRequest.from_json(json)
# print the JSON string representation of the object
print(AddWalletRequest.to_json())

# convert the object into a dict
add_wallet_request_dict = add_wallet_request_instance.to_dict()
# create an instance of AddWalletRequest from a dict
add_wallet_request_from_dict = AddWalletRequest.from_dict(add_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


