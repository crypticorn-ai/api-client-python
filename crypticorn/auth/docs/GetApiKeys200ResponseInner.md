# GetApiKeys200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the API key | 
**user_id** | **str** | User ID of the API key | 
**scopes** | **List[str]** | Scopes of the API key | 
**name** | **str** | Name of the API key | 
**expires_at** | **datetime** | Expiration time of the API key as a date | [optional] 
**created_at** | **datetime** | Creation time of the API key as a date | 
**ip_whitelist** | **List[str]** | IP addresses that can access the API key. If empty, the API key will be accessible from any IP address. | [optional] 

## Example

```python
from client.models.get_api_keys200_response_inner import GetApiKeys200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiKeys200ResponseInner from a JSON string
get_api_keys200_response_inner_instance = GetApiKeys200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetApiKeys200ResponseInner.to_json())

# convert the object into a dict
get_api_keys200_response_inner_dict = get_api_keys200_response_inner_instance.to_dict()
# create an instance of GetApiKeys200ResponseInner from a dict
get_api_keys200_response_inner_from_dict = GetApiKeys200ResponseInner.from_dict(get_api_keys200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


