# RefreshTokenInfo200ResponseUserSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**token** | **str** |  | 
**expires_at** | **datetime** |  | 
**client_ip** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 

## Example

```python
from client.models.refresh_token_info200_response_user_session import RefreshTokenInfo200ResponseUserSession

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshTokenInfo200ResponseUserSession from a JSON string
refresh_token_info200_response_user_session_instance = RefreshTokenInfo200ResponseUserSession.from_json(json)
# print the JSON string representation of the object
print(RefreshTokenInfo200ResponseUserSession.to_json())

# convert the object into a dict
refresh_token_info200_response_user_session_dict = refresh_token_info200_response_user_session_instance.to_dict()
# create an instance of RefreshTokenInfo200ResponseUserSession from a dict
refresh_token_info200_response_user_session_from_dict = RefreshTokenInfo200ResponseUserSession.from_dict(refresh_token_info200_response_user_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


