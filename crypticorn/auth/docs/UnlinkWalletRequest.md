# UnlinkWalletRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 

## Example

```python
from client.models.unlink_wallet_request import UnlinkWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnlinkWalletRequest from a JSON string
unlink_wallet_request_instance = UnlinkWalletRequest.from_json(json)
# print the JSON string representation of the object
print(UnlinkWalletRequest.to_json())

# convert the object into a dict
unlink_wallet_request_dict = unlink_wallet_request_instance.to_dict()
# create an instance of UnlinkWalletRequest from a dict
unlink_wallet_request_from_dict = UnlinkWalletRequest.from_dict(unlink_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


