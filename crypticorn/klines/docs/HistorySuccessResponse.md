# HistorySuccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s** | **str** |  | [optional] [default to 'ok']
**t** | **List[int]** |  | 
**o** | **List[float]** |  | 
**h** | **List[float]** |  | 
**l** | **List[float]** |  | 
**c** | **List[float]** |  | 
**v** | **List[float]** |  | 

## Example

```python
from client.models.history_success_response import HistorySuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HistorySuccessResponse from a JSON string
history_success_response_instance = HistorySuccessResponse.from_json(json)
# print the JSON string representation of the object
print(HistorySuccessResponse.to_json())

# convert the object into a dict
history_success_response_dict = history_success_response_instance.to_dict()
# create an instance of HistorySuccessResponse from a dict
history_success_response_from_dict = HistorySuccessResponse.from_dict(history_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


