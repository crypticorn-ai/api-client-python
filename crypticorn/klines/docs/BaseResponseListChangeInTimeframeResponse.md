# BaseResponseListChangeInTimeframeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**message** | **str** |  | [optional] 
**data** | [**List[ChangeInTimeframeResponse]**](ChangeInTimeframeResponse.md) |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from client.models.base_response_list_change_in_timeframe_response import BaseResponseListChangeInTimeframeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseListChangeInTimeframeResponse from a JSON string
base_response_list_change_in_timeframe_response_instance = BaseResponseListChangeInTimeframeResponse.from_json(json)
# print the JSON string representation of the object
print(BaseResponseListChangeInTimeframeResponse.to_json())

# convert the object into a dict
base_response_list_change_in_timeframe_response_dict = base_response_list_change_in_timeframe_response_instance.to_dict()
# create an instance of BaseResponseListChangeInTimeframeResponse from a dict
base_response_list_change_in_timeframe_response_from_dict = BaseResponseListChangeInTimeframeResponse.from_dict(base_response_list_change_in_timeframe_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


