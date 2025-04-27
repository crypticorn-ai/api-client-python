# SymbolGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **List[str]** |  | [optional] [default to []]

## Example

```python
from client.models.symbol_group import SymbolGroup

# TODO update the JSON string below
json = "{}"
# create an instance of SymbolGroup from a JSON string
symbol_group_instance = SymbolGroup.from_json(json)
# print the JSON string representation of the object
print(SymbolGroup.to_json())

# convert the object into a dict
symbol_group_dict = symbol_group_instance.to_dict()
# create an instance of SymbolGroup from a dict
symbol_group_from_dict = SymbolGroup.from_dict(symbol_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


