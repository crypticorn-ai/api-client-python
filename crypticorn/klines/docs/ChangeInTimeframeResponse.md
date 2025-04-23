# ChangeInTimeframeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pair** | **str** |  | 
**change** | **float** |  | 

## Example

```python
from client.models.change_in_timeframe_response import ChangeInTimeframeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeInTimeframeResponse from a JSON string
change_in_timeframe_response_instance = ChangeInTimeframeResponse.from_json(json)
# print the JSON string representation of the object
print(ChangeInTimeframeResponse.to_json())

# convert the object into a dict
change_in_timeframe_response_dict = change_in_timeframe_response_instance.to_dict()
# create an instance of ChangeInTimeframeResponse from a dict
change_in_timeframe_response_from_dict = ChangeInTimeframeResponse.from_dict(change_in_timeframe_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


