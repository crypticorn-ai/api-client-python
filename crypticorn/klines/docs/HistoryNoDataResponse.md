# HistoryNoDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s** | **str** |  | [optional] [default to 'no_data']
**t** | **List[int]** |  | [optional] [default to []]
**o** | **List[float]** |  | [optional] [default to []]
**h** | **List[float]** |  | [optional] [default to []]
**l** | **List[float]** |  | [optional] [default to []]
**c** | **List[float]** |  | [optional] [default to []]
**v** | **List[float]** |  | [optional] [default to []]

## Example

```python
from client.models.history_no_data_response import HistoryNoDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryNoDataResponse from a JSON string
history_no_data_response_instance = HistoryNoDataResponse.from_json(json)
# print the JSON string representation of the object
print(HistoryNoDataResponse.to_json())

# convert the object into a dict
history_no_data_response_dict = history_no_data_response_instance.to_dict()
# create an instance of HistoryNoDataResponse from a dict
history_no_data_response_from_dict = HistoryNoDataResponse.from_dict(history_no_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


