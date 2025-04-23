# ResponseGetUdfHistory


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
from client.models.response_get_udf_history import ResponseGetUdfHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetUdfHistory from a JSON string
response_get_udf_history_instance = ResponseGetUdfHistory.from_json(json)
# print the JSON string representation of the object
print(ResponseGetUdfHistory.to_json())

# convert the object into a dict
response_get_udf_history_dict = response_get_udf_history_instance.to_dict()
# create an instance of ResponseGetUdfHistory from a dict
response_get_udf_history_from_dict = ResponseGetUdfHistory.from_dict(response_get_udf_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


