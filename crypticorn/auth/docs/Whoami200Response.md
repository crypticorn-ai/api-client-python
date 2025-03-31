# Whoami200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**picture** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from client.models.whoami200_response import Whoami200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Whoami200Response from a JSON string
whoami200_response_instance = Whoami200Response.from_json(json)
# print the JSON string representation of the object
print(Whoami200Response.to_json())

# convert the object into a dict
whoami200_response_dict = whoami200_response_instance.to_dict()
# create an instance of Whoami200Response from a dict
whoami200_response_from_dict = Whoami200Response.from_dict(whoami200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


