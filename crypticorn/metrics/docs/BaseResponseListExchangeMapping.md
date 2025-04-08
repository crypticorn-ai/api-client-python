# BaseResponseListExchangeMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**message** | **str** |  | [optional] 
**data** | [**List[ExchangeMapping]**](ExchangeMapping.md) |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from client.models.base_response_list_exchange_mapping import BaseResponseListExchangeMapping

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseListExchangeMapping from a JSON string
base_response_list_exchange_mapping_instance = BaseResponseListExchangeMapping.from_json(json)
# print the JSON string representation of the object
print(BaseResponseListExchangeMapping.to_json())

# convert the object into a dict
base_response_list_exchange_mapping_dict = base_response_list_exchange_mapping_instance.to_dict()
# create an instance of BaseResponseListExchangeMapping from a dict
base_response_list_exchange_mapping_from_dict = BaseResponseListExchangeMapping.from_dict(base_response_list_exchange_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


