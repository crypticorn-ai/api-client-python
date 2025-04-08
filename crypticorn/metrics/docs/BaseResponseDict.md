# BaseResponseDict


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**message** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from client.models.base_response_dict import BaseResponseDict

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseDict from a JSON string
base_response_dict_instance = BaseResponseDict.from_json(json)
# print the JSON string representation of the object
print(BaseResponseDict.to_json())

# convert the object into a dict
base_response_dict_dict = base_response_dict_instance.to_dict()
# create an instance of BaseResponseDict from a dict
base_response_dict_from_dict = BaseResponseDict.from_dict(base_response_dict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


