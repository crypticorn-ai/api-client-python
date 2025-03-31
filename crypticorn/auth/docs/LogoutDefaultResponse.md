# LogoutDefaultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**code** | **str** |  | 
**issues** | [**List[LogoutDefaultResponseIssuesInner]**](LogoutDefaultResponseIssuesInner.md) |  | [optional] 

## Example

```python
from client.models.logout_default_response import LogoutDefaultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LogoutDefaultResponse from a JSON string
logout_default_response_instance = LogoutDefaultResponse.from_json(json)
# print the JSON string representation of the object
print(LogoutDefaultResponse.to_json())

# convert the object into a dict
logout_default_response_dict = logout_default_response_instance.to_dict()
# create an instance of LogoutDefaultResponse from a dict
logout_default_response_from_dict = LogoutDefaultResponse.from_dict(logout_default_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


