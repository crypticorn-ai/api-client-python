# Payment

Model representing a single payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **int** | Unique payment identifier | 
**invoice_id** | **int** |  | [optional] 
**payment_status** | **str** | Current payment status | 
**pay_address** | **str** | Payment destination address | 
**payin_extra_id** | **str** |  | [optional] 
**price_amount** | **float** | Original price amount | 
**price_currency** | **str** | Original price currency | 
**pay_amount** | **float** | Amount to pay | 
**actually_paid** | **float** | Actually paid amount | 
**pay_currency** | **str** | Payment currency | 
**order_id** | **str** |  | [optional] 
**order_description** | **str** |  | [optional] 
**purchase_id** | **int** |  | [optional] 
**outcome_amount** | **float** |  | [optional] 
**outcome_currency** | **str** |  | [optional] 
**payout_hash** | **str** |  | [optional] 
**payin_hash** | **str** |  | [optional] 
**created_at** | **str** | Payment creation timestamp | 
**updated_at** | **str** | Payment last update timestamp | 
**type** | **str** | Type of payment (e.g., crypto2crypto) | 
**payment_extra_ids** | **List[int]** |  | [optional] 
**parent_payment_id** | **int** |  | [optional] 
**origin_type** | **str** |  | [optional] 

## Example

```python
from client.models.payment import Payment

# TODO update the JSON string below
json = "{}"
# create an instance of Payment from a JSON string
payment_instance = Payment.from_json(json)
# print the JSON string representation of the object
print(Payment.to_json())

# convert the object into a dict
payment_dict = payment_instance.to_dict()
# create an instance of Payment from a dict
payment_from_dict = Payment.from_dict(payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


