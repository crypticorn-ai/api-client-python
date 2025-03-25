# APIStatusRes

Response for the API status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | API status message | 

## Example

```python
from client.models.api_status_res import APIStatusRes

# TODO update the JSON string below
json = "{}"
# create an instance of APIStatusRes from a JSON string
api_status_res_instance = APIStatusRes.from_json(json)
# print the JSON string representation of the object
print(APIStatusRes.to_json())

# convert the object into a dict
api_status_res_dict = api_status_res_instance.to_dict()
# create an instance of APIStatusRes from a dict
api_status_res_from_dict = APIStatusRes.from_dict(api_status_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


