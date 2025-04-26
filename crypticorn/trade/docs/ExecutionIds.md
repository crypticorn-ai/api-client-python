# ExecutionIds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**main** | **str** | Main execution ID. | 
**sl** | **List[str]** | Stop loss execution IDs. List with multiple items ordered by the next stop loss, e.g. price &#x3D; 10000 &#x3D;&gt; SLs: [&#39;900&#39;, &#39;700&#39;, &#39;500&#39;]. | 
**tp** | **List[str]** | Take profit execution IDs. List with multiple items ordered by the next take profit, e.g. price &#x3D; 10000 &#x3D;&gt; TPs: [&#39;1100&#39;, &#39;1300&#39;, &#39;1500&#39;]. | 

## Example

```python
from client.models.execution_ids import ExecutionIds

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionIds from a JSON string
execution_ids_instance = ExecutionIds.from_json(json)
# print the JSON string representation of the object
print(ExecutionIds.to_json())

# convert the object into a dict
execution_ids_dict = execution_ids_instance.to_dict()
# create an instance of ExecutionIds from a dict
execution_ids_from_dict = ExecutionIds.from_dict(execution_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


