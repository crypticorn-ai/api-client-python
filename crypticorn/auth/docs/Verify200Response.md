# Verify200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iss** | **str** | Issuer | [optional] 
**sub** | **str** | Subject | [optional] 
**aud** | **str** | Audience | [optional] 
**exp** | **float** | Expiration time | [optional] 
**nbf** | **float** | Not valid before time | [optional] 
**iat** | **float** | Issued at time | [optional] 
**jti** | **str** | JWT ID | [optional] 
**scopes** | **List[str]** | Scopes | [optional] 

## Example

```python
from client.models.verify200_response import Verify200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Verify200Response from a JSON string
verify200_response_instance = Verify200Response.from_json(json)
# print the JSON string representation of the object
print(Verify200Response.to_json())

# convert the object into a dict
verify200_response_dict = verify200_response_instance.to_dict()
# create an instance of Verify200Response from a dict
verify200_response_from_dict = Verify200Response.from_dict(verify200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


