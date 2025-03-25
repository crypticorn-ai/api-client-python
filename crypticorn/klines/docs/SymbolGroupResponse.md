# SymbolGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **List[str]** |  | [optional] [default to []]

## Example

```python
from client.models.symbol_group_response import SymbolGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SymbolGroupResponse from a JSON string
symbol_group_response_instance = SymbolGroupResponse.from_json(json)
# print the JSON string representation of the object
print(SymbolGroupResponse.to_json())

# convert the object into a dict
symbol_group_response_dict = symbol_group_response_instance.to_dict()
# create an instance of SymbolGroupResponse from a dict
symbol_group_response_from_dict = SymbolGroupResponse.from_dict(symbol_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


