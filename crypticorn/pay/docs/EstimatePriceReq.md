# EstimatePriceReq

Method for calculating the approximate price in cryptocurrency for a given value.  This endpoint estimates the cryptocurrency amount for a given fiat currency value, or estimates crypto-to-crypto conversions. https://documenter.getpostman.com/view/7907941/2s93JusNJt#3c86a16e-94ad-4230-a470-4e833766a4c7

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Cost value | 
**currency_from** | **str** | Fiat currency | 
**currency_to** | **str** | Cryptocurrency | 

## Example

```python
from client.models.estimate_price_req import EstimatePriceReq

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatePriceReq from a JSON string
estimate_price_req_instance = EstimatePriceReq.from_json(json)
# print the JSON string representation of the object
print(EstimatePriceReq.to_json())

# convert the object into a dict
estimate_price_req_dict = estimate_price_req_instance.to_dict()
# create an instance of EstimatePriceReq from a dict
estimate_price_req_from_dict = EstimatePriceReq.from_dict(estimate_price_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


