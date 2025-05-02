# DownloadLinks

The download links for the data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**y_train** | **str** | The download link for the y_train data | 
**x_test** | **str** | The download link for the X_test data | 
**x_train** | **str** | The download link for the X_train data | 

## Example

```python
from client.models.download_links import DownloadLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadLinks from a JSON string
download_links_instance = DownloadLinks.from_json(json)
# print the JSON string representation of the object
print(DownloadLinks.to_json())

# convert the object into a dict
download_links_dict = download_links_instance.to_dict()
# create an instance of DownloadLinks from a dict
download_links_from_dict = DownloadLinks.from_dict(download_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


