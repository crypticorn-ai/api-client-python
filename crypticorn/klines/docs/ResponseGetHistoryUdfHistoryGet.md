# ResponseGetHistoryUdfHistoryGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s** | **str** |  | [optional] [default to 'error']
**t** | **List[int]** |  | [default to []]
**o** | **List[float]** |  | [default to []]
**h** | **List[float]** |  | [default to []]
**l** | **List[float]** |  | [default to []]
**c** | **List[float]** |  | [default to []]
**v** | **List[float]** |  | [default to []]
**errmsg** | **str** |  | 

## Example

```python
from client.models.response_get_history_udf_history_get import ResponseGetHistoryUdfHistoryGet

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetHistoryUdfHistoryGet from a JSON string
response_get_history_udf_history_get_instance = ResponseGetHistoryUdfHistoryGet.from_json(json)
# print the JSON string representation of the object
print(ResponseGetHistoryUdfHistoryGet.to_json())

# convert the object into a dict
response_get_history_udf_history_get_dict = response_get_history_udf_history_get_instance.to_dict()
# create an instance of ResponseGetHistoryUdfHistoryGet from a dict
response_get_history_udf_history_get_from_dict = ResponseGetHistoryUdfHistoryGet.from_dict(response_get_history_udf_history_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


