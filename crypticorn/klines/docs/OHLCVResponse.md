# OHLCVResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **List[datetime]** |  | 
**open** | **List[float]** |  | 
**high** | **List[float]** |  | 
**low** | **List[float]** |  | 
**close** | **List[float]** |  | 
**volume** | **List[float]** |  | 

## Example

```python
from client.models.ohlcv_response import OHLCVResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OHLCVResponse from a JSON string
ohlcv_response_instance = OHLCVResponse.from_json(json)
# print the JSON string representation of the object
print(OHLCVResponse.to_json())

# convert the object into a dict
ohlcv_response_dict = ohlcv_response_instance.to_dict()
# create an instance of OHLCVResponse from a dict
ohlcv_response_from_dict = OHLCVResponse.from_dict(ohlcv_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


