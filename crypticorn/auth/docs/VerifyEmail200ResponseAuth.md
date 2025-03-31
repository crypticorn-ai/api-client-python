# VerifyEmail200ResponseAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**refresh_token** | **str** |  | 
**auth** | [**VerifyEmail200ResponseAuthAuth**](VerifyEmail200ResponseAuthAuth.md) |  | [optional] 

## Example

```python
from client.models.verify_email200_response_auth import VerifyEmail200ResponseAuth

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyEmail200ResponseAuth from a JSON string
verify_email200_response_auth_instance = VerifyEmail200ResponseAuth.from_json(json)
# print the JSON string representation of the object
print(VerifyEmail200ResponseAuth.to_json())

# convert the object into a dict
verify_email200_response_auth_dict = verify_email200_response_auth_instance.to_dict()
# create an instance of VerifyEmail200ResponseAuth from a dict
verify_email200_response_auth_from_dict = VerifyEmail200ResponseAuth.from_dict(verify_email200_response_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


