# NowAPIStatusRes

Response for the API status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | API status message | 

## Example

```python
from client.models.now_api_status_res import NowAPIStatusRes

# TODO update the JSON string below
json = "{}"
# create an instance of NowAPIStatusRes from a JSON string
now_api_status_res_instance = NowAPIStatusRes.from_json(json)
# print the JSON string representation of the object
print(NowAPIStatusRes.to_json())

# convert the object into a dict
now_api_status_res_dict = now_api_status_res_instance.to_dict()
# create an instance of NowAPIStatusRes from a dict
now_api_status_res_from_dict = NowAPIStatusRes.from_dict(now_api_status_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


