# VerifyWalletRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oob_code** | **str** |  | 
**signature** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from client.models.verify_wallet_request import VerifyWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyWalletRequest from a JSON string
verify_wallet_request_instance = VerifyWalletRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyWalletRequest.to_json())

# convert the object into a dict
verify_wallet_request_dict = verify_wallet_request_instance.to_dict()
# create an instance of VerifyWalletRequest from a dict
verify_wallet_request_from_dict = VerifyWalletRequest.from_dict(verify_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


