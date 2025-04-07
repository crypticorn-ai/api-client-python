# OauthCallback200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**OauthCallback200ResponseUser**](OauthCallback200ResponseUser.md) |  | 
**auth** | [**AuthorizeUser200ResponseAuth**](AuthorizeUser200ResponseAuth.md) |  | 

## Example

```python
from client.models.oauth_callback200_response import OauthCallback200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OauthCallback200Response from a JSON string
oauth_callback200_response_instance = OauthCallback200Response.from_json(json)
# print the JSON string representation of the object
print(OauthCallback200Response.to_json())

# convert the object into a dict
oauth_callback200_response_dict = oauth_callback200_response_instance.to_dict()
# create an instance of OauthCallback200Response from a dict
oauth_callback200_response_from_dict = OauthCallback200Response.from_dict(oauth_callback200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


