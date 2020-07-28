# swagger_client.RoamingDeviceGroupsApi

All URIs are relative to *https://localhost/api/atcep/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**roaming_device_groups_create_roaming_device_group**](RoamingDeviceGroupsApi.md#roaming_device_groups_create_roaming_device_group) | **POST** /roaming_device_groups | Create Roaming Device Group.
[**roaming_device_groups_delete_roaming_device_group**](RoamingDeviceGroupsApi.md#roaming_device_groups_delete_roaming_device_group) | **DELETE** /roaming_device_groups | Delete Roaming Device Groups.
[**roaming_device_groups_list_roaming_device_groups**](RoamingDeviceGroupsApi.md#roaming_device_groups_list_roaming_device_groups) | **GET** /roaming_device_groups | List Roaming Device Groups.
[**roaming_device_groups_read_roaming_device_group**](RoamingDeviceGroupsApi.md#roaming_device_groups_read_roaming_device_group) | **GET** /roaming_device_groups/{id} | Read Roaming Device Group.
[**roaming_device_groups_update_partial_roaming_device_group**](RoamingDeviceGroupsApi.md#roaming_device_groups_update_partial_roaming_device_group) | **PATCH** /roaming_device_groups/{id} | Update Roaming Device Group partially.
[**roaming_device_groups_update_roaming_device_group**](RoamingDeviceGroupsApi.md#roaming_device_groups_update_roaming_device_group) | **PUT** /roaming_device_groups/{id} | Update Roaming Device Group.


# **roaming_device_groups_create_roaming_device_group**
> AtcepRoamingDeviceGroupCreateResponse roaming_device_groups_create_roaming_device_group(body)

Create Roaming Device Group.

Use this method to create a Roaming Device Group object.  The Roaming Device Group object represents an BloxOne Endpoint group. When applying security policies to multiple BloxOne Endpoint devices, you can make the process more efficient by organizing the endpoint devices into BloxOne Endpoint groups, and then add the groups to the network scope when you create a security policy.  Required: - name 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoamingDeviceGroupsApi()
body = swagger_client.AtcepRoamingDeviceGroup() # AtcepRoamingDeviceGroup | The Roaming Device Group object.

try:
    # Create Roaming Device Group.
    api_response = api_instance.roaming_device_groups_create_roaming_device_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoamingDeviceGroupsApi->roaming_device_groups_create_roaming_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AtcepRoamingDeviceGroup**](AtcepRoamingDeviceGroup.md)| The Roaming Device Group object. | 

### Return type

[**AtcepRoamingDeviceGroupCreateResponse**](AtcepRoamingDeviceGroupCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roaming_device_groups_delete_roaming_device_group**
> roaming_device_groups_delete_roaming_device_group(body)

Delete Roaming Device Groups.

Use this method to delete the Roaming Device Group objects. Deletion of multiple lists is an all-or-nothing operation (if any of the specified lists can not be deleted then none of the specified lists will be deleted).  The Roaming Device Group object represents an BloxOne Endpoint group. When applying security policies to multiple BloxOne Endpoint devices, you can make the process more efficient by organizing the endpoint devices into BloxOne Endpoint groups, and then add the groups to the network scope when you create a security policy.  Required: - ids 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoamingDeviceGroupsApi()
body = swagger_client.AtcepRoamingDeviceGroupDeleteRequest() # AtcepRoamingDeviceGroupDeleteRequest | 

try:
    # Delete Roaming Device Groups.
    api_instance.roaming_device_groups_delete_roaming_device_group(body)
except ApiException as e:
    print("Exception when calling RoamingDeviceGroupsApi->roaming_device_groups_delete_roaming_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AtcepRoamingDeviceGroupDeleteRequest**](AtcepRoamingDeviceGroupDeleteRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roaming_device_groups_list_roaming_device_groups**
> AtcepRoamingDeviceGroupsMultiResponse roaming_device_groups_list_roaming_device_groups(filter=filter, fields=fields)

List Roaming Device Groups.

Use this method to retrieve information on all Roaming Device Group objects for the account.  Note that endpoint devices are not displayed for this operation.  The Roaming Device Group object represents an BloxOne Endpoint group. When applying security policies to multiple BloxOne Endpoint devices, you can make the process more efficient by organizing the endpoint devices into BloxOne Endpoint groups, and then add the groups to the network scope when you create a security policy. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoamingDeviceGroupsApi()
filter = 'filter_example' # str | A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'.  You can filter by following fields:  | Name                    | type   | Supported Op  | | ----------------------- | ------ | ------------- | | policy_id               | int32  | !=, ==        | | default_security_policy | bool   | !=, ==        |  In addition groupping operators are supported:  | Op  | Description          | | --- | -------------------- | | and | Logical AND          | | or  | Logical OR           | | not | Logical NOT          | | ()  | Groupping Operators  |  Example: ``` ?_filter=\"((policy_id==53123)or(policy_id==null))and(default_security_policy!='true')\" ```  (optional)
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

try:
    # List Roaming Device Groups.
    api_response = api_instance.roaming_device_groups_list_roaming_device_groups(filter=filter, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoamingDeviceGroupsApi->roaming_device_groups_list_roaming_device_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;.  You can filter by following fields:  | Name                    | type   | Supported Op  | | ----------------------- | ------ | ------------- | | policy_id               | int32  | !&#x3D;, &#x3D;&#x3D;        | | default_security_policy | bool   | !&#x3D;, &#x3D;&#x3D;        |  In addition groupping operators are supported:  | Op  | Description          | | --- | -------------------- | | and | Logical AND          | | or  | Logical OR           | | not | Logical NOT          | | ()  | Groupping Operators  |  Example: &#x60;&#x60;&#x60; ?_filter&#x3D;\&quot;((policy_id&#x3D;&#x3D;53123)or(policy_id&#x3D;&#x3D;null))and(default_security_policy!&#x3D;&#39;true&#39;)\&quot; &#x60;&#x60;&#x60;  | [optional] 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**AtcepRoamingDeviceGroupsMultiResponse**](AtcepRoamingDeviceGroupsMultiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roaming_device_groups_read_roaming_device_group**
> AtcepRoamingDeviceGroupReadResponse roaming_device_groups_read_roaming_device_group(id, fields=fields)

Read Roaming Device Group.

Use this method to retrieve information on the specified Roaming Device object.  The Roaming Device Group object represents an BloxOne Endpoint group. When applying security policies to multiple BloxOne Endpoint devices, you can make the process more efficient by organizing the endpoint devices into BloxOne Endpoint groups, and then add the groups to the network scope when you create a security policy. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoamingDeviceGroupsApi()
id = 56 # int | The Roaming Device Group object identifier.
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

try:
    # Read Roaming Device Group.
    api_response = api_instance.roaming_device_groups_read_roaming_device_group(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoamingDeviceGroupsApi->roaming_device_groups_read_roaming_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Roaming Device Group object identifier. | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**AtcepRoamingDeviceGroupReadResponse**](AtcepRoamingDeviceGroupReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roaming_device_groups_update_partial_roaming_device_group**
> AtcepRoamingDeviceGroupUpdateResponse roaming_device_groups_update_partial_roaming_device_group(id, body)

Update Roaming Device Group partially.

Use this method to partially update a specific Roaming Device Group object with specific roaming_devices only.  Required: - name 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoamingDeviceGroupsApi()
id = 56 # int | The Roaming Device Group object identifier.
body = swagger_client.AtcepRoamingDeviceGroupUpdate() # AtcepRoamingDeviceGroupUpdate | The Roaming Device Group object.

try:
    # Update Roaming Device Group partially.
    api_response = api_instance.roaming_device_groups_update_partial_roaming_device_group(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoamingDeviceGroupsApi->roaming_device_groups_update_partial_roaming_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Roaming Device Group object identifier. | 
 **body** | [**AtcepRoamingDeviceGroupUpdate**](AtcepRoamingDeviceGroupUpdate.md)| The Roaming Device Group object. | 

### Return type

[**AtcepRoamingDeviceGroupUpdateResponse**](AtcepRoamingDeviceGroupUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roaming_device_groups_update_roaming_device_group**
> AtcepRoamingDeviceGroupUpdateResponse roaming_device_groups_update_roaming_device_group(id, body)

Update Roaming Device Group.

Use this method to update a specific Roaming Device Group object.  The Roaming Device Group object represents an BloxOne Endpoint group. When applying security policies to multiple BloxOne Endpoint devices, you can make the process more efficient by organizing the endpoint devices into BloxOne Endpoint groups, and then add the groups to the network scope when you create a security policy.  Required: - name  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoamingDeviceGroupsApi()
id = 56 # int | The Roaming Device Group object identifier.
body = swagger_client.AtcepRoamingDeviceGroup() # AtcepRoamingDeviceGroup | The Roaming Device Group object.

try:
    # Update Roaming Device Group.
    api_response = api_instance.roaming_device_groups_update_roaming_device_group(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoamingDeviceGroupsApi->roaming_device_groups_update_roaming_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Roaming Device Group object identifier. | 
 **body** | [**AtcepRoamingDeviceGroup**](AtcepRoamingDeviceGroup.md)| The Roaming Device Group object. | 

### Return type

[**AtcepRoamingDeviceGroupUpdateResponse**](AtcepRoamingDeviceGroupUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

