# ListWallets200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**name** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**verified_at** | **datetime** |  | [optional] 

## Example

```python
from client.models.list_wallets200_response_data_inner import ListWallets200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListWallets200ResponseDataInner from a JSON string
list_wallets200_response_data_inner_instance = ListWallets200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ListWallets200ResponseDataInner.to_json())

# convert the object into a dict
list_wallets200_response_data_inner_dict = list_wallets200_response_data_inner_instance.to_dict()
# create an instance of ListWallets200ResponseDataInner from a dict
list_wallets200_response_data_inner_from_dict = ListWallets200ResponseDataInner.from_dict(list_wallets200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


