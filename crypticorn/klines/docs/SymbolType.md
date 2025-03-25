# SymbolType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from client.models.symbol_type import SymbolType

# TODO update the JSON string below
json = "{}"
# create an instance of SymbolType from a JSON string
symbol_type_instance = SymbolType.from_json(json)
# print the JSON string representation of the object
print(SymbolType.to_json())

# convert the object into a dict
symbol_type_dict = symbol_type_instance.to_dict()
# create an instance of SymbolType from a dict
symbol_type_from_dict = SymbolType.from_dict(symbol_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


