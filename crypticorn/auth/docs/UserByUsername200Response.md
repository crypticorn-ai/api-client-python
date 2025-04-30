# UserByUsername200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**username** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from client.models.user_by_username200_response import UserByUsername200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserByUsername200Response from a JSON string
user_by_username200_response_instance = UserByUsername200Response.from_json(json)
# print the JSON string representation of the object
print(UserByUsername200Response.to_json())

# convert the object into a dict
user_by_username200_response_dict = user_by_username200_response_instance.to_dict()
# create an instance of UserByUsername200Response from a dict
user_by_username200_response_from_dict = UserByUsername200Response.from_dict(user_by_username200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


