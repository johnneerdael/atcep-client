# coding: utf-8

"""
    BloxOne Cloud EP API

    BloxOne Endpoint is a lightweight mobile agent that redirects DNS traffic from your remote devices to the BloxOne Cloud. It allows you to apply applicable security policies to your roaming end users in remote sites and branch offices.  In order for end users to connect to Infoblox cloud services, you must download and install BloxOne Endpoint on their devices. The client enforces security policies that you apply to the remote networks, regardless of where your end users are and which networks they are connected to. BloxOne Endpoint listens on port 53 of the device. If other software listens on the same port, DNS traffic cannot be redirected to BloxOne Cloud, and your device will not be protected by BloxOne Endpoint.  When you use the BloxOne Endpoint, DNS queries are sent to BloxOne Cloud directly except for (1) queries that target the bypassed domains and (2) internal domains collected through the DHCP server. If you have internal domains that are served by your local DNS servers and you want to reach them without interruptions, you should consider adding them to the bypassed internal domains list so that DNS queries for these internal domains are sent to the local DNS servers instead of BloxOne Cloud.  BloxOne Endpoint supports dual-stack IPv4 and IPv6 DNS configurations, thereby protecting all devices regardless of their network environments. BloxOne Endpoint in a dual-stack environment is able to proxy IPv6 DNS queries and forward them to BloxOne Cloud over IPv4.   # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class RoamingDevicesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def roaming_devices_list_roaming_devices(self, **kwargs):  # noqa: E501
        """List Roaming Devices.  # noqa: E501

        Use this method to retrieve information on all Roaming Device objects for the account.  The Roaming Device object represents the device with BloxOne Endpoint client installed. In order for end users to connect to Infoblox cloud services, you must download and install BloxOne Endpoint on their devices. The client enforces security policies that you apply to the remote networks, regardless of where your end users are and which networks they are connected to. BloxOne Endpoint listens on port 53 of the device. If other software listens on the same port, DNS traffic cannot be redirected to BloxOne Cloud, and your device will not be protected by BloxOne Endpoint.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.roaming_devices_list_roaming_devices(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter: A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'.  You can filter by following fields:  | Name          | type   | Supported Op | | ------------- | ------ | ------------ | | client_id     | string | ==           | | group_id      | int32  | ==           | | default_group | bool   | ==           |  Groupping operators (and, or, not, ()) are not supported.   Example: ``` ?_filter=\"client_id=='abc12345abc'\" ``` 
        :param str fields:   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.        
        :param int offset:   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.         
        :param int limit:   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.         
        :param str page_token:   The service-defined string used to identify a page of resources. A null value indicates the first page.         
        :param str order_by:   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.        
        :return: AtcepRoamingDeviceMultiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.roaming_devices_list_roaming_devices_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.roaming_devices_list_roaming_devices_with_http_info(**kwargs)  # noqa: E501
            return data

    def roaming_devices_list_roaming_devices_with_http_info(self, **kwargs):  # noqa: E501
        """List Roaming Devices.  # noqa: E501

        Use this method to retrieve information on all Roaming Device objects for the account.  The Roaming Device object represents the device with BloxOne Endpoint client installed. In order for end users to connect to Infoblox cloud services, you must download and install BloxOne Endpoint on their devices. The client enforces security policies that you apply to the remote networks, regardless of where your end users are and which networks they are connected to. BloxOne Endpoint listens on port 53 of the device. If other software listens on the same port, DNS traffic cannot be redirected to BloxOne Cloud, and your device will not be protected by BloxOne Endpoint.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.roaming_devices_list_roaming_devices_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter: A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'.  You can filter by following fields:  | Name          | type   | Supported Op | | ------------- | ------ | ------------ | | client_id     | string | ==           | | group_id      | int32  | ==           | | default_group | bool   | ==           |  Groupping operators (and, or, not, ()) are not supported.   Example: ``` ?_filter=\"client_id=='abc12345abc'\" ``` 
        :param str fields:   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.        
        :param int offset:   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.         
        :param int limit:   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.         
        :param str page_token:   The service-defined string used to identify a page of resources. A null value indicates the first page.         
        :param str order_by:   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.        
        :return: AtcepRoamingDeviceMultiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter', 'fields', 'offset', 'limit', 'page_token', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method roaming_devices_list_roaming_devices" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('_filter', params['filter']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('_fields', params['fields']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('_offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('_limit', params['limit']))  # noqa: E501
        if 'page_token' in params:
            query_params.append(('_page_token', params['page_token']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('_order_by', params['order_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/roaming_devices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AtcepRoamingDeviceMultiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def roaming_devices_list_roaming_devices_csv(self, **kwargs):  # noqa: E501
        """List RoamingDevices in CSV format Use this method to download the selected list of roaming devices in CSV (comma-separate values) format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.roaming_devices_list_roaming_devices_csv(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter:   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |        
        :param str order_by:   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.        
        :return: AtcepRoamingDevicesCSVListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.roaming_devices_list_roaming_devices_csv_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.roaming_devices_list_roaming_devices_csv_with_http_info(**kwargs)  # noqa: E501
            return data

    def roaming_devices_list_roaming_devices_csv_with_http_info(self, **kwargs):  # noqa: E501
        """List RoamingDevices in CSV format Use this method to download the selected list of roaming devices in CSV (comma-separate values) format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.roaming_devices_list_roaming_devices_csv_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter:   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |        
        :param str order_by:   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.        
        :return: AtcepRoamingDevicesCSVListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method roaming_devices_list_roaming_devices_csv" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('_filter', params['filter']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('_order_by', params['order_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/roaming_devices_download', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AtcepRoamingDevicesCSVListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def roaming_devices_read_roaming_device(self, client_id, **kwargs):  # noqa: E501
        """Read Roaming Device.  # noqa: E501

        Use this method to retrieve information on the specified Roaming Device object.  The Roaming Device object represents the device with BloxOne Endpoint client installed. In order for end users to connect to Infoblox cloud services, you must download and install BloxOne Endpoint on their devices. The client enforces security policies that you apply to the remote networks, regardless of where your end users are and which networks they are connected to. BloxOne Endpoint listens on port 53 of the device. If other software listens on the same port, DNS traffic cannot be redirected to BloxOne Cloud, and your device will not be protected by BloxOne Endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.roaming_devices_read_roaming_device(client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: The unique identifier of the endpoint device. (required)
        :param str fields:   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.        
        :return: AtcepRoamingDeviceReadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.roaming_devices_read_roaming_device_with_http_info(client_id, **kwargs)  # noqa: E501
        else:
            (data) = self.roaming_devices_read_roaming_device_with_http_info(client_id, **kwargs)  # noqa: E501
            return data

    def roaming_devices_read_roaming_device_with_http_info(self, client_id, **kwargs):  # noqa: E501
        """Read Roaming Device.  # noqa: E501

        Use this method to retrieve information on the specified Roaming Device object.  The Roaming Device object represents the device with BloxOne Endpoint client installed. In order for end users to connect to Infoblox cloud services, you must download and install BloxOne Endpoint on their devices. The client enforces security policies that you apply to the remote networks, regardless of where your end users are and which networks they are connected to. BloxOne Endpoint listens on port 53 of the device. If other software listens on the same port, DNS traffic cannot be redirected to BloxOne Cloud, and your device will not be protected by BloxOne Endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.roaming_devices_read_roaming_device_with_http_info(client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: The unique identifier of the endpoint device. (required)
        :param str fields:   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.        
        :return: AtcepRoamingDeviceReadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_id', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method roaming_devices_read_roaming_device" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `roaming_devices_read_roaming_device`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'client_id' in params:
            path_params['client_id'] = params['client_id']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('_fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/roaming_devices/{client_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AtcepRoamingDeviceReadResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def roaming_devices_update_roaming_device(self, body, **kwargs):  # noqa: E501
        """Update Roaming Device.  # noqa: E501

        Use this method to update the status for the Roaming Device objects. Depending on the last connection timestamp and administrative status the final status is determined using the table below:  | administrative_status | connected | calculated_status | | --------------------- | --------- | ----------------- | | enabled               | true      | active            | | enabled               | false     | inactive          | | disabled              | *         | disabled          | | deleted               | *         | deleted           |  The Roaming Device object is treated as connected when the last login timestamp (connection timestamp) is less than 15 minutes from time of the update.  The Roaming Device object represents the device with BloxOne Endpoint client installed. In order for end users to connect to Infoblox cloud services, you must download and install BloxOne Endpoint on their devices. The client enforces security policies that you apply to the remote networks, regardless of where your end users are and which networks they are connected to. BloxOne Endpoint listens on port 53 of the device. If other software listens on the same port, DNS traffic cannot be redirected to BloxOne Cloud, and your device will not be protected by BloxOne Endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.roaming_devices_update_roaming_device(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AtcepRoamingDeviceUpdateRequest body: (required)
        :return: AtcepRoamingDeviceUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.roaming_devices_update_roaming_device_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.roaming_devices_update_roaming_device_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def roaming_devices_update_roaming_device_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update Roaming Device.  # noqa: E501

        Use this method to update the status for the Roaming Device objects. Depending on the last connection timestamp and administrative status the final status is determined using the table below:  | administrative_status | connected | calculated_status | | --------------------- | --------- | ----------------- | | enabled               | true      | active            | | enabled               | false     | inactive          | | disabled              | *         | disabled          | | deleted               | *         | deleted           |  The Roaming Device object is treated as connected when the last login timestamp (connection timestamp) is less than 15 minutes from time of the update.  The Roaming Device object represents the device with BloxOne Endpoint client installed. In order for end users to connect to Infoblox cloud services, you must download and install BloxOne Endpoint on their devices. The client enforces security policies that you apply to the remote networks, regardless of where your end users are and which networks they are connected to. BloxOne Endpoint listens on port 53 of the device. If other software listens on the same port, DNS traffic cannot be redirected to BloxOne Cloud, and your device will not be protected by BloxOne Endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.roaming_devices_update_roaming_device_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AtcepRoamingDeviceUpdateRequest body: (required)
        :return: AtcepRoamingDeviceUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method roaming_devices_update_roaming_device" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `roaming_devices_update_roaming_device`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/roaming_devices', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AtcepRoamingDeviceUpdateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
