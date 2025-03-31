# RevokeUserTokensRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 

## Example

```python
from client.models.revoke_user_tokens_request import RevokeUserTokensRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeUserTokensRequest from a JSON string
revoke_user_tokens_request_instance = RevokeUserTokensRequest.from_json(json)
# print the JSON string representation of the object
print(RevokeUserTokensRequest.to_json())

# convert the object into a dict
revoke_user_tokens_request_dict = revoke_user_tokens_request_instance.to_dict()
# create an instance of RevokeUserTokensRequest from a dict
revoke_user_tokens_request_from_dict = RevokeUserTokensRequest.from_dict(revoke_user_tokens_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


