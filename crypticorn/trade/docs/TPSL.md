# TPSL

Model for take profit and stop loss targets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_delta** | **float** |  | [optional] 
**price** | **float** |  | [optional] 
**allocation** | **float** | Percentage of the order to sell | 
**execution_id** | **str** |  | [optional] 
**client_order_id** | **str** |  | [optional] 

## Example

```python
from client.models.tpsl import TPSL

# TODO update the JSON string below
json = "{}"
# create an instance of TPSL from a JSON string
tpsl_instance = TPSL.from_json(json)
# print the JSON string representation of the object
print(TPSL.to_json())

# convert the object into a dict
tpsl_dict = tpsl_instance.to_dict()
# create an instance of TPSL from a dict
tpsl_from_dict = TPSL.from_dict(tpsl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


