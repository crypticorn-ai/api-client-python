# HistoryErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s** | **str** |  | [optional] [default to 'error']
**errmsg** | **str** |  | 

## Example

```python
from client.models.history_error_response import HistoryErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryErrorResponse from a JSON string
history_error_response_instance = HistoryErrorResponse.from_json(json)
# print the JSON string representation of the object
print(HistoryErrorResponse.to_json())

# convert the object into a dict
history_error_response_dict = history_error_response_instance.to_dict()
# create an instance of HistoryErrorResponse from a dict
history_error_response_from_dict = HistoryErrorResponse.from_dict(history_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


