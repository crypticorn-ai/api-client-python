# NowFeeStructure

Fee structure for the payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency of the fee | 
**deposit_fee** | **float** | Deposit fee amount | 
**service_fee** | **float** | Service fee amount | 
**withdrawal_fee** | **float** | Withdrawal fee amount | 

## Example

```python
from client.models.now_fee_structure import NowFeeStructure

# TODO update the JSON string below
json = "{}"
# create an instance of NowFeeStructure from a JSON string
now_fee_structure_instance = NowFeeStructure.from_json(json)
# print the JSON string representation of the object
print(NowFeeStructure.to_json())

# convert the object into a dict
now_fee_structure_dict = now_fee_structure_instance.to_dict()
# create an instance of NowFeeStructure from a dict
now_fee_structure_from_dict = NowFeeStructure.from_dict(now_fee_structure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


