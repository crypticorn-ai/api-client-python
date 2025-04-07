# OauthCallback200ResponseUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**picture** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from client.models.oauth_callback200_response_user import OauthCallback200ResponseUser

# TODO update the JSON string below
json = "{}"
# create an instance of OauthCallback200ResponseUser from a JSON string
oauth_callback200_response_user_instance = OauthCallback200ResponseUser.from_json(json)
# print the JSON string representation of the object
print(OauthCallback200ResponseUser.to_json())

# convert the object into a dict
oauth_callback200_response_user_dict = oauth_callback200_response_user_instance.to_dict()
# create an instance of OauthCallback200ResponseUser from a dict
oauth_callback200_response_user_from_dict = OauthCallback200ResponseUser.from_dict(oauth_callback200_response_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


