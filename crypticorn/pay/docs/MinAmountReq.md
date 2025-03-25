# MinAmountReq

Get the minimum payment amount for a specific currency pair. https://documenter.getpostman.com/view/7907941/2s93JusNJt#ce3fe3a3-00cd-4df2-bfba-641fde741da7  You can provide both currencies in the pair or just currency_from. If only currency_from is provided, the minimum payment amount will be calculated for currency_from and the default currency specified in Payment Settings.  You can specify a fiat currency in currency_from to calculate the minimum payment in that fiat currency.  The fiat_equivalent field can be added to get the fiat equivalent of the minimum amount.  The is_fixed_rate and is_fee_paid_by_user parameters allow you to see current minimal amounts for corresponding flows, which may differ from the standard flow.  For multiple outcome wallets, the minimum amount is calculated based on the payment routing logic.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_from** | **str** | Payin currency | 
**currency_to** | **str** |  | [optional] 
**fiat_equivalent** | **str** |  | [optional] 
**is_fixed_rate** | **bool** |  | [optional] 
**is_fee_paid_by_user** | **bool** |  | [optional] 

## Example

```python
from client.models.min_amount_req import MinAmountReq

# TODO update the JSON string below
json = "{}"
# create an instance of MinAmountReq from a JSON string
min_amount_req_instance = MinAmountReq.from_json(json)
# print the JSON string representation of the object
print(MinAmountReq.to_json())

# convert the object into a dict
min_amount_req_dict = min_amount_req_instance.to_dict()
# create an instance of MinAmountReq from a dict
min_amount_req_from_dict = MinAmountReq.from_dict(min_amount_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


