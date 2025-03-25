# GetPaymentStatusRes

Response model for the payment status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **int** | Unique payment identifier | 
**invoice_id** | **int** |  | [optional] 
**payment_status** | **str** | Current payment status (waiting, confirming, confirmed, sending, partially_paid, finished, failed, refunded, expired) | 
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
**burning_percent** | **str** |  | [optional] 
**type** | **str** | Type of payment (e.g., crypto2crypto) | 
**payment_extra_ids** | **List[int]** |  | [optional] 

## Example

```python
from client.models.get_payment_status_res import GetPaymentStatusRes

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentStatusRes from a JSON string
get_payment_status_res_instance = GetPaymentStatusRes.from_json(json)
# print the JSON string representation of the object
print(GetPaymentStatusRes.to_json())

# convert the object into a dict
get_payment_status_res_dict = get_payment_status_res_instance.to_dict()
# create an instance of GetPaymentStatusRes from a dict
get_payment_status_res_from_dict = GetPaymentStatusRes.from_dict(get_payment_status_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


