# SearchSymbolResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | 
**full_name** | **str** |  | 
**description** | **str** |  | 
**exchange** | **str** |  | 
**ticker** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from client.models.search_symbol_response import SearchSymbolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSymbolResponse from a JSON string
search_symbol_response_instance = SearchSymbolResponse.from_json(json)
# print the JSON string representation of the object
print(SearchSymbolResponse.to_json())

# convert the object into a dict
search_symbol_response_dict = search_symbol_response_instance.to_dict()
# create an instance of SearchSymbolResponse from a dict
search_symbol_response_from_dict = SearchSymbolResponse.from_dict(search_symbol_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


