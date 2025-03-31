# AuthorizeUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 
**admin** | **bool** |  | [optional] 
**captcha_token** | **str** |  | 

## Example

```python
from client.models.authorize_user_request import AuthorizeUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizeUserRequest from a JSON string
authorize_user_request_instance = AuthorizeUserRequest.from_json(json)
# print the JSON string representation of the object
print(AuthorizeUserRequest.to_json())

# convert the object into a dict
authorize_user_request_dict = authorize_user_request_instance.to_dict()
# create an instance of AuthorizeUserRequest from a dict
authorize_user_request_from_dict = AuthorizeUserRequest.from_dict(authorize_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


