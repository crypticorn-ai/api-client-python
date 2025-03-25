# FundingRateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | 
**timestamp** | **datetime** |  | 
**funding_rate** | **float** |  | 

## Example

```python
from client.models.funding_rate_response import FundingRateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FundingRateResponse from a JSON string
funding_rate_response_instance = FundingRateResponse.from_json(json)
# print the JSON string representation of the object
print(FundingRateResponse.to_json())

# convert the object into a dict
funding_rate_response_dict = funding_rate_response_instance.to_dict()
# create an instance of FundingRateResponse from a dict
funding_rate_response_from_dict = FundingRateResponse.from_dict(funding_rate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


