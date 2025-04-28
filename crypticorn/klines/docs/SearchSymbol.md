# SearchSymbol


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | 
**description** | **str** |  | 
**exchange** | **str** | All exchanges we are using, including public (Exchange) | 
**type** | **str** |  | 

## Example

```python
from client.models.search_symbol import SearchSymbol

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSymbol from a JSON string
search_symbol_instance = SearchSymbol.from_json(json)
# print the JSON string representation of the object
print(SearchSymbol.to_json())

# convert the object into a dict
search_symbol_dict = search_symbol_instance.to_dict()
# create an instance of SearchSymbol from a dict
search_symbol_from_dict = SearchSymbol.from_dict(search_symbol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


