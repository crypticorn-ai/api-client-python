# UserSetPasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**new_password** | **str** |  | 

## Example

```python
from client.models.user_set_password_request import UserSetPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserSetPasswordRequest from a JSON string
user_set_password_request_instance = UserSetPasswordRequest.from_json(json)
# print the JSON string representation of the object
print(UserSetPasswordRequest.to_json())

# convert the object into a dict
user_set_password_request_dict = user_set_password_request_instance.to_dict()
# create an instance of UserSetPasswordRequest from a dict
user_set_password_request_from_dict = UserSetPasswordRequest.from_dict(user_set_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


