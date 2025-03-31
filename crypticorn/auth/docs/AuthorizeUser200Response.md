# AuthorizeUser200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**Whoami200Response**](Whoami200Response.md) |  | 
**auth** | [**AuthorizeUser200ResponseAuth**](AuthorizeUser200ResponseAuth.md) |  | 

## Example

```python
from client.models.authorize_user200_response import AuthorizeUser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizeUser200Response from a JSON string
authorize_user200_response_instance = AuthorizeUser200Response.from_json(json)
# print the JSON string representation of the object
print(AuthorizeUser200Response.to_json())

# convert the object into a dict
authorize_user200_response_dict = authorize_user200_response_instance.to_dict()
# create an instance of AuthorizeUser200Response from a dict
authorize_user200_response_from_dict = AuthorizeUser200Response.from_dict(authorize_user200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


