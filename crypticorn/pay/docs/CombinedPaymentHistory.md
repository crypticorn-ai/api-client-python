# CombinedPaymentHistory

Combined payment history across all services

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**now** | [**List[NowPaymentModel]**](NowPaymentModel.md) | NOWPayments payment history | [optional] 

## Example

```python
from client.models.combined_payment_history import CombinedPaymentHistory

# TODO update the JSON string below
json = "{}"
# create an instance of CombinedPaymentHistory from a JSON string
combined_payment_history_instance = CombinedPaymentHistory.from_json(json)
# print the JSON string representation of the object
print(CombinedPaymentHistory.to_json())

# convert the object into a dict
combined_payment_history_dict = combined_payment_history_instance.to_dict()
# create an instance of CombinedPaymentHistory from a dict
combined_payment_history_from_dict = CombinedPaymentHistory.from_dict(combined_payment_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


