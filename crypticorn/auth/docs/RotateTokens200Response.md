# RotateTokens200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**auth** | [**VerifyEmail200ResponseAuthAuth**](VerifyEmail200ResponseAuthAuth.md) |  | [optional] 
**token_expires_at** | **float** |  | [optional] 

## Example

```python
from client.models.rotate_tokens200_response import RotateTokens200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RotateTokens200Response from a JSON string
rotate_tokens200_response_instance = RotateTokens200Response.from_json(json)
# print the JSON string representation of the object
print(RotateTokens200Response.to_json())

# convert the object into a dict
rotate_tokens200_response_dict = rotate_tokens200_response_instance.to_dict()
# create an instance of RotateTokens200Response from a dict
rotate_tokens200_response_from_dict = RotateTokens200Response.from_dict(rotate_tokens200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


