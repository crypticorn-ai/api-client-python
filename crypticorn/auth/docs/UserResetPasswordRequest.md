# UserResetPasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oob_code** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from client.models.user_reset_password_request import UserResetPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserResetPasswordRequest from a JSON string
user_reset_password_request_instance = UserResetPasswordRequest.from_json(json)
# print the JSON string representation of the object
print(UserResetPasswordRequest.to_json())

# convert the object into a dict
user_reset_password_request_dict = user_reset_password_request_instance.to_dict()
# create an instance of UserResetPasswordRequest from a dict
user_reset_password_request_from_dict = UserResetPasswordRequest.from_dict(user_reset_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


