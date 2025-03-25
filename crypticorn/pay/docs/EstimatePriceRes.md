# EstimatePriceRes

Response for the estimate price calculation.  Contains the source currency and amount, target currency, and the estimated conversion amount. https://documenter.getpostman.com/view/7907941/2s93JusNJt#3c86a16e-94ad-4230-a470-4e833766a4c7

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_from** | **str** | Source currency | 
**amount_from** | **float** | Original amount in source currency | 
**currency_to** | **str** | Target cryptocurrency | 
**estimated_amount** | **float** | Estimated amount in target cryptocurrency | 

## Example

```python
from client.models.estimate_price_res import EstimatePriceRes

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatePriceRes from a JSON string
estimate_price_res_instance = EstimatePriceRes.from_json(json)
# print the JSON string representation of the object
print(EstimatePriceRes.to_json())

# convert the object into a dict
estimate_price_res_dict = estimate_price_res_instance.to_dict()
# create an instance of EstimatePriceRes from a dict
estimate_price_res_from_dict = EstimatePriceRes.from_dict(estimate_price_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


