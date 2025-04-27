# OHLCVHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamps** | **List[datetime]** | Timestamps in seconds | 
**open** | **List[float]** | Open prices | 
**high** | **List[float]** | High prices | 
**low** | **List[float]** | Low prices | 
**close** | **List[float]** | Close prices | 
**volume** | **List[float]** | Volume | 

## Example

```python
from client.models.ohlcv_history import OHLCVHistory

# TODO update the JSON string below
json = "{}"
# create an instance of OHLCVHistory from a JSON string
ohlcv_history_instance = OHLCVHistory.from_json(json)
# print the JSON string representation of the object
print(OHLCVHistory.to_json())

# convert the object into a dict
ohlcv_history_dict = ohlcv_history_instance.to_dict()
# create an instance of OHLCVHistory from a dict
ohlcv_history_from_dict = OHLCVHistory.from_dict(ohlcv_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


