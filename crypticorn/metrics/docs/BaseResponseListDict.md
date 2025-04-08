# BaseResponseListDict


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**message** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from client.models.base_response_list_dict import BaseResponseListDict

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseListDict from a JSON string
base_response_list_dict_instance = BaseResponseListDict.from_json(json)
# print the JSON string representation of the object
print(BaseResponseListDict.to_json())

# convert the object into a dict
base_response_list_dict_dict = base_response_list_dict_instance.to_dict()
# create an instance of BaseResponseListDict from a dict
base_response_list_dict_from_dict = BaseResponseListDict.from_dict(base_response_list_dict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


