# AuthorizeUser200ResponseAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**refresh_token** | **str** |  | 
**auth** | [**VerifyEmail200ResponseAuthAuth**](VerifyEmail200ResponseAuthAuth.md) |  | 

## Example

```python
from client.models.authorize_user200_response_auth import AuthorizeUser200ResponseAuth

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizeUser200ResponseAuth from a JSON string
authorize_user200_response_auth_instance = AuthorizeUser200ResponseAuth.from_json(json)
# print the JSON string representation of the object
print(AuthorizeUser200ResponseAuth.to_json())

# convert the object into a dict
authorize_user200_response_auth_dict = authorize_user200_response_auth_instance.to_dict()
# create an instance of AuthorizeUser200ResponseAuth from a dict
authorize_user200_response_auth_from_dict = AuthorizeUser200ResponseAuth.from_dict(authorize_user200_response_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


