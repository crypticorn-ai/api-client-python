# UDFConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_resolutions** | **List[str]** |  | 
**supports_group_request** | **bool** |  | [optional] [default to False]
**supports_marks** | **bool** |  | [optional] [default to False]
**supports_search** | **bool** |  | [optional] [default to True]
**supports_timescale_marks** | **bool** |  | [optional] [default to False]
**supports_time** | **bool** |  | [optional] [default to True]
**exchanges** | **List[str]** |  | 
**symbols_types** | [**List[SymbolType]**](SymbolType.md) |  | 
**currency_codes** | **List[str]** |  | 
**supported_markets** | **List[str]** |  | 

## Example

```python
from client.models.udf_config import UDFConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UDFConfig from a JSON string
udf_config_instance = UDFConfig.from_json(json)
# print the JSON string representation of the object
print(UDFConfig.to_json())

# convert the object into a dict
udf_config_dict = udf_config_instance.to_dict()
# create an instance of UDFConfig from a dict
udf_config_from_dict = UDFConfig.from_dict(udf_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


