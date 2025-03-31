# RefreshTokenInfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_session** | [**RefreshTokenInfo200ResponseUserSession**](RefreshTokenInfo200ResponseUserSession.md) |  | 

## Example

```python
from client.models.refresh_token_info200_response import RefreshTokenInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshTokenInfo200Response from a JSON string
refresh_token_info200_response_instance = RefreshTokenInfo200Response.from_json(json)
# print the JSON string representation of the object
print(RefreshTokenInfo200Response.to_json())

# convert the object into a dict
refresh_token_info200_response_dict = refresh_token_info200_response_instance.to_dict()
# create an instance of RefreshTokenInfo200Response from a dict
refresh_token_info200_response_from_dict = RefreshTokenInfo200Response.from_dict(refresh_token_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


