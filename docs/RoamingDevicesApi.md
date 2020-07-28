# swagger_client.RoamingDevicesApi

All URIs are relative to *https://localhost/api/atcep/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**roaming_devices_list_roaming_devices**](RoamingDevicesApi.md#roaming_devices_list_roaming_devices) | **GET** /roaming_devices | List Roaming Devices.
[**roaming_devices_list_roaming_devices_csv**](RoamingDevicesApi.md#roaming_devices_list_roaming_devices_csv) | **GET** /roaming_devices_download | List RoamingDevices in CSV format Use this method to download the selected list of roaming devices in CSV (comma-separate values) format.
[**roaming_devices_read_roaming_device**](RoamingDevicesApi.md#roaming_devices_read_roaming_device) | **GET** /roaming_devices/{client_id} | Read Roaming Device.
[**roaming_devices_update_roaming_device**](RoamingDevicesApi.md#roaming_devices_update_roaming_device) | **PUT** /roaming_devices | Update Roaming Device.


# **roaming_devices_list_roaming_devices**
> AtcepRoamingDeviceMultiResponse roaming_devices_list_roaming_devices(filter=filter, fields=fields, offset=offset, limit=limit, page_token=page_token, order_by=order_by)

List Roaming Devices.

Use this method to retrieve information on all Roaming Device objects for the account.  The Roaming Device object represents the device with BloxOne Endpoint client installed. In order for end users to connect to Infoblox cloud services, you must download and install BloxOne Endpoint on their devices. The client enforces security policies that you apply to the remote networks, regardless of where your end users are and which networks they are connected to. BloxOne Endpoint listens on port 53 of the device. If other software listens on the same port, DNS traffic cannot be redirected to BloxOne Cloud, and your device will not be protected by BloxOne Endpoint. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoamingDevicesApi()
filter = 'filter_example' # str | A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'.  You can filter by following fields:  | Name          | type   | Supported Op | | ------------- | ------ | ------------ | | client_id     | string | ==           | | group_id      | int32  | ==           | | default_group | bool   | ==           |  Groupping operators (and, or, not, ()) are not supported.   Example: ``` ?_filter=\"client_id=='abc12345abc'\" ```  (optional)
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)
order_by = 'order_by_example' # str |   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         (optional)

try:
    # List Roaming Devices.
    api_response = api_instance.roaming_devices_list_roaming_devices(filter=filter, fields=fields, offset=offset, limit=limit, page_token=page_token, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoamingDevicesApi->roaming_devices_list_roaming_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;.  You can filter by following fields:  | Name          | type   | Supported Op | | ------------- | ------ | ------------ | | client_id     | string | &#x3D;&#x3D;           | | group_id      | int32  | &#x3D;&#x3D;           | | default_group | bool   | &#x3D;&#x3D;           |  Groupping operators (and, or, not, ()) are not supported.   Example: &#x60;&#x60;&#x60; ?_filter&#x3D;\&quot;client_id&#x3D;&#x3D;&#39;abc12345abc&#39;\&quot; &#x60;&#x60;&#x60;  | [optional] 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 

### Return type

[**AtcepRoamingDeviceMultiResponse**](AtcepRoamingDeviceMultiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roaming_devices_list_roaming_devices_csv**
> AtcepRoamingDevicesCSVListResponse roaming_devices_list_roaming_devices_csv(filter=filter, order_by=order_by)

List RoamingDevices in CSV format Use this method to download the selected list of roaming devices in CSV (comma-separate values) format.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoamingDevicesApi()
filter = 'filter_example' # str |   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         (optional)
order_by = 'order_by_example' # str |   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         (optional)

try:
    # List RoamingDevices in CSV format Use this method to download the selected list of roaming devices in CSV (comma-separate values) format.
    api_response = api_instance.roaming_devices_list_roaming_devices_csv(filter=filter, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoamingDevicesApi->roaming_devices_list_roaming_devices_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**|   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  &#x3D;&#x3D;   |  Equal                     |  |  !&#x3D;   |  Not Equal                 |  |  &gt;    |  Greater Than              |  |   &gt;&#x3D;  |  Greater Than or Equal To  |  |  &lt;    |  Less Than                 |  |  &lt;&#x3D;   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         | [optional] 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 

### Return type

[**AtcepRoamingDevicesCSVListResponse**](AtcepRoamingDevicesCSVListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roaming_devices_read_roaming_device**
> AtcepRoamingDeviceReadResponse roaming_devices_read_roaming_device(client_id, fields=fields)

Read Roaming Device.

Use this method to retrieve information on the specified Roaming Device object.  The Roaming Device object represents the device with BloxOne Endpoint client installed. In order for end users to connect to Infoblox cloud services, you must download and install BloxOne Endpoint on their devices. The client enforces security policies that you apply to the remote networks, regardless of where your end users are and which networks they are connected to. BloxOne Endpoint listens on port 53 of the device. If other software listens on the same port, DNS traffic cannot be redirected to BloxOne Cloud, and your device will not be protected by BloxOne Endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoamingDevicesApi()
client_id = 'client_id_example' # str | The unique identifier of the endpoint device.
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

try:
    # Read Roaming Device.
    api_response = api_instance.roaming_devices_read_roaming_device(client_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoamingDevicesApi->roaming_devices_read_roaming_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The unique identifier of the endpoint device. | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**AtcepRoamingDeviceReadResponse**](AtcepRoamingDeviceReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roaming_devices_update_roaming_device**
> AtcepRoamingDeviceUpdateResponse roaming_devices_update_roaming_device(body)

Update Roaming Device.

Use this method to update the status for the Roaming Device objects. Depending on the last connection timestamp and administrative status the final status is determined using the table below:  | administrative_status | connected | calculated_status | | --------------------- | --------- | ----------------- | | enabled               | true      | active            | | enabled               | false     | inactive          | | disabled              | *         | disabled          | | deleted               | *         | deleted           |  The Roaming Device object is treated as connected when the last login timestamp (connection timestamp) is less than 15 minutes from time of the update.  The Roaming Device object represents the device with BloxOne Endpoint client installed. In order for end users to connect to Infoblox cloud services, you must download and install BloxOne Endpoint on their devices. The client enforces security policies that you apply to the remote networks, regardless of where your end users are and which networks they are connected to. BloxOne Endpoint listens on port 53 of the device. If other software listens on the same port, DNS traffic cannot be redirected to BloxOne Cloud, and your device will not be protected by BloxOne Endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoamingDevicesApi()
body = swagger_client.AtcepRoamingDeviceUpdateRequest() # AtcepRoamingDeviceUpdateRequest | 

try:
    # Update Roaming Device.
    api_response = api_instance.roaming_devices_update_roaming_device(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoamingDevicesApi->roaming_devices_update_roaming_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AtcepRoamingDeviceUpdateRequest**](AtcepRoamingDeviceUpdateRequest.md)|  | 

### Return type

[**AtcepRoamingDeviceUpdateResponse**](AtcepRoamingDeviceUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

