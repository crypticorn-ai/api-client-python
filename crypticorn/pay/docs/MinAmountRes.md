# MinAmountRes

Response for the minimum payment amount for a specific currency pair. https://documenter.getpostman.com/view/7907941/2s93JusNJt#ce3fe3a3-00cd-4df2-bfba-641fde741da7

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_from** | **str** | Payin currency | 
**currency_to** | **str** | Outcome currency | 
**min_amount** | **float** | Minimal amount for payment using mentioned currencies | 
**fiat_equivalent** | **float** |  | [optional] 

## Example

```python
from client.models.min_amount_res import MinAmountRes

# TODO update the JSON string below
json = "{}"
# create an instance of MinAmountRes from a JSON string
min_amount_res_instance = MinAmountRes.from_json(json)
# print the JSON string representation of the object
print(MinAmountRes.to_json())

# convert the object into a dict
min_amount_res_dict = min_amount_res_instance.to_dict()
# create an instance of MinAmountRes from a dict
min_amount_res_from_dict = MinAmountRes.from_dict(min_amount_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


