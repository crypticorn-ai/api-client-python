# CreateApiKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the API key | 
**scopes** | **List[str]** | Scopes of the API key | 
**expires_at** | **datetime** | Expiration time of the API key as a date | [optional] 
**ip_whitelist** | **List[str]** | IP addresses that can access the API key. If empty, the API key will be accessible from any IP address. | [optional] 

## Example

```python
from client.models.create_api_key_request import CreateApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApiKeyRequest from a JSON string
create_api_key_request_instance = CreateApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateApiKeyRequest.to_json())

# convert the object into a dict
create_api_key_request_dict = create_api_key_request_instance.to_dict()
# create an instance of CreateApiKeyRequest from a dict
create_api_key_request_from_dict = CreateApiKeyRequest.from_dict(create_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


