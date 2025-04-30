# VerifyEmail200ResponseAuthAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iss** | **str** | Issuer | [optional] 
**sub** | **str** | Subject | [optional] 
**aud** | **str** | Audience | [optional] 
**exp** | **float** | Expiration time | [optional] 
**nbf** | **float** | Not valid before time | [optional] 
**iat** | **float** | Issued at time | [optional] 
**jti** | **str** | JWT ID | [optional] 
**admin** | **bool** | Whether the user is an admin | [optional] 
**scopes** | **List[str]** | Scopes | [optional] 

## Example

```python
from client.models.verify_email200_response_auth_auth import VerifyEmail200ResponseAuthAuth

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyEmail200ResponseAuthAuth from a JSON string
verify_email200_response_auth_auth_instance = VerifyEmail200ResponseAuthAuth.from_json(json)
# print the JSON string representation of the object
print(VerifyEmail200ResponseAuthAuth.to_json())

# convert the object into a dict
verify_email200_response_auth_auth_dict = verify_email200_response_auth_auth_instance.to_dict()
# create an instance of VerifyEmail200ResponseAuthAuth from a dict
verify_email200_response_auth_auth_from_dict = VerifyEmail200ResponseAuthAuth.from_dict(verify_email200_response_auth_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


