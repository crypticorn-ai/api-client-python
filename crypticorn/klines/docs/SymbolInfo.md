# SymbolInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**exchange_traded** | **str** |  | 
**exchange_listed** | **str** |  | 
**timezone** | **str** |  | 
**minmov** | **int** |  | 
**minmov2** | **int** |  | 
**pointvalue** | **int** |  | 
**session** | **str** |  | 
**has_intraday** | **bool** |  | 
**has_no_volume** | **bool** |  | 
**description** | **str** |  | 
**type** | **str** |  | 
**supported_resolutions** | **List[str]** |  | 
**pricescale** | **int** |  | 
**ticker** | **str** |  | 

## Example

```python
from client.models.symbol_info import SymbolInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SymbolInfo from a JSON string
symbol_info_instance = SymbolInfo.from_json(json)
# print the JSON string representation of the object
print(SymbolInfo.to_json())

# convert the object into a dict
symbol_info_dict = symbol_info_instance.to_dict()
# create an instance of SymbolInfo from a dict
symbol_info_from_dict = SymbolInfo.from_dict(symbol_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


