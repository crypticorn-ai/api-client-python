# BaseResponseListStr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**message** | **str** |  | [optional] 
**data** | **List[str]** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from client.models.base_response_list_str import BaseResponseListStr

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseListStr from a JSON string
base_response_list_str_instance = BaseResponseListStr.from_json(json)
# print the JSON string representation of the object
print(BaseResponseListStr.to_json())

# convert the object into a dict
base_response_list_str_dict = base_response_list_str_instance.to_dict()
# create an instance of BaseResponseListStr from a dict
base_response_list_str_from_dict = BaseResponseListStr.from_dict(base_response_list_str_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


