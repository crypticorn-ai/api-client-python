# TokenInfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | [**VerifyEmail200ResponseAuthAuth**](VerifyEmail200ResponseAuthAuth.md) |  | [optional] 

## Example

```python
from client.models.token_info200_response import TokenInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInfo200Response from a JSON string
token_info200_response_instance = TokenInfo200Response.from_json(json)
# print the JSON string representation of the object
print(TokenInfo200Response.to_json())

# convert the object into a dict
token_info200_response_dict = token_info200_response_instance.to_dict()
# create an instance of TokenInfo200Response from a dict
token_info200_response_from_dict = TokenInfo200Response.from_dict(token_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


