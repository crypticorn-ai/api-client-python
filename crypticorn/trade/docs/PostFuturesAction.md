# PostFuturesAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Action ID. | 
**execution_ids** | [**ExecutionIds**](ExecutionIds.md) | Execution IDs for the action. | 

## Example

```python
from client.models.post_futures_action import PostFuturesAction

# TODO update the JSON string below
json = "{}"
# create an instance of PostFuturesAction from a JSON string
post_futures_action_instance = PostFuturesAction.from_json(json)
# print the JSON string representation of the object
print(PostFuturesAction.to_json())

# convert the object into a dict
post_futures_action_dict = post_futures_action_instance.to_dict()
# create an instance of PostFuturesAction from a dict
post_futures_action_from_dict = PostFuturesAction.from_dict(post_futures_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


