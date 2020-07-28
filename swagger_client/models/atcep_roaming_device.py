# coding: utf-8

"""
    BloxOne Cloud EP API

    BloxOne Endpoint is a lightweight mobile agent that redirects DNS traffic from your remote devices to the BloxOne Cloud. It allows you to apply applicable security policies to your roaming end users in remote sites and branch offices.  In order for end users to connect to Infoblox cloud services, you must download and install BloxOne Endpoint on their devices. The client enforces security policies that you apply to the remote networks, regardless of where your end users are and which networks they are connected to. BloxOne Endpoint listens on port 53 of the device. If other software listens on the same port, DNS traffic cannot be redirected to BloxOne Cloud, and your device will not be protected by BloxOne Endpoint.  When you use the BloxOne Endpoint, DNS queries are sent to BloxOne Cloud directly except for (1) queries that target the bypassed domains and (2) internal domains collected through the DHCP server. If you have internal domains that are served by your local DNS servers and you want to reach them without interruptions, you should consider adding them to the bypassed internal domains list so that DNS queries for these internal domains are sent to the local DNS servers instead of BloxOne Cloud.  BloxOne Endpoint supports dual-stack IPv4 and IPv6 DNS configurations, thereby protecting all devices regardless of their network environments. BloxOne Endpoint in a dual-stack environment is able to proxy IPv6 DNS queries and forward them to BloxOne Cloud over IPv4.   # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AtcepRoamingDevice(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'calculated_status': 'str',
        'client_id': 'str',
        'connected_time': 'datetime',
        'created_time': 'datetime',
        'device_info': 'str',
        'group_id': 'int',
        'group_name': 'str',
        'name': 'str',
        'net_info': 'AtcepNetInfo',
        'os_platform': 'str',
        'updated_time': 'datetime',
        'user_id': 'str',
        'version': 'str'
    }

    attribute_map = {
        'calculated_status': 'calculated_status',
        'client_id': 'client_id',
        'connected_time': 'connected_time',
        'created_time': 'created_time',
        'device_info': 'device_info',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'name': 'name',
        'net_info': 'net_info',
        'os_platform': 'os_platform',
        'updated_time': 'updated_time',
        'user_id': 'user_id',
        'version': 'version'
    }

    def __init__(self, calculated_status=None, client_id=None, connected_time=None, created_time=None, device_info=None, group_id=None, group_name=None, name=None, net_info=None, os_platform=None, updated_time=None, user_id=None, version=None):  # noqa: E501
        """AtcepRoamingDevice - a model defined in Swagger"""  # noqa: E501

        self._calculated_status = None
        self._client_id = None
        self._connected_time = None
        self._created_time = None
        self._device_info = None
        self._group_id = None
        self._group_name = None
        self._name = None
        self._net_info = None
        self._os_platform = None
        self._updated_time = None
        self._user_id = None
        self._version = None
        self.discriminator = None

        if calculated_status is not None:
            self.calculated_status = calculated_status
        if client_id is not None:
            self.client_id = client_id
        if connected_time is not None:
            self.connected_time = connected_time
        if created_time is not None:
            self.created_time = created_time
        if device_info is not None:
            self.device_info = device_info
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if name is not None:
            self.name = name
        if net_info is not None:
            self.net_info = net_info
        if os_platform is not None:
            self.os_platform = os_platform
        if updated_time is not None:
            self.updated_time = updated_time
        if user_id is not None:
            self.user_id = user_id
        if version is not None:
            self.version = version

    @property
    def calculated_status(self):
        """Gets the calculated_status of this AtcepRoamingDevice.  # noqa: E501

        The operational state of the endpoint device that can be \"ACTIVE\", \"INACTIVE\", \"DISABLED\" or \"DELETED\".  # noqa: E501

        :return: The calculated_status of this AtcepRoamingDevice.  # noqa: E501
        :rtype: str
        """
        return self._calculated_status

    @calculated_status.setter
    def calculated_status(self, calculated_status):
        """Sets the calculated_status of this AtcepRoamingDevice.

        The operational state of the endpoint device that can be \"ACTIVE\", \"INACTIVE\", \"DISABLED\" or \"DELETED\".  # noqa: E501

        :param calculated_status: The calculated_status of this AtcepRoamingDevice.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "DISABLED", "DELETED"]  # noqa: E501
        if calculated_status not in allowed_values:
            raise ValueError(
                "Invalid value for `calculated_status` ({0}), must be one of {1}"  # noqa: E501
                .format(calculated_status, allowed_values)
            )

        self._calculated_status = calculated_status

    @property
    def client_id(self):
        """Gets the client_id of this AtcepRoamingDevice.  # noqa: E501

        The unique identifier of the endpoint device.  # noqa: E501

        :return: The client_id of this AtcepRoamingDevice.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AtcepRoamingDevice.

        The unique identifier of the endpoint device.  # noqa: E501

        :param client_id: The client_id of this AtcepRoamingDevice.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def connected_time(self):
        """Gets the connected_time of this AtcepRoamingDevice.  # noqa: E501

        The time when the Roaming Device object was last updated from login call.  # noqa: E501

        :return: The connected_time of this AtcepRoamingDevice.  # noqa: E501
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time):
        """Sets the connected_time of this AtcepRoamingDevice.

        The time when the Roaming Device object was last updated from login call.  # noqa: E501

        :param connected_time: The connected_time of this AtcepRoamingDevice.  # noqa: E501
        :type: datetime
        """

        self._connected_time = connected_time

    @property
    def created_time(self):
        """Gets the created_time of this AtcepRoamingDevice.  # noqa: E501

        The time when the Roaming Device object was created.  # noqa: E501

        :return: The created_time of this AtcepRoamingDevice.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this AtcepRoamingDevice.

        The time when the Roaming Device object was created.  # noqa: E501

        :param created_time: The created_time of this AtcepRoamingDevice.  # noqa: E501
        :type: datetime
        """

        self._created_time = created_time

    @property
    def device_info(self):
        """Gets the device_info of this AtcepRoamingDevice.  # noqa: E501

        The information about the endpoint device.  # noqa: E501

        :return: The device_info of this AtcepRoamingDevice.  # noqa: E501
        :rtype: str
        """
        return self._device_info

    @device_info.setter
    def device_info(self, device_info):
        """Sets the device_info of this AtcepRoamingDevice.

        The information about the endpoint device.  # noqa: E501

        :param device_info: The device_info of this AtcepRoamingDevice.  # noqa: E501
        :type: str
        """

        self._device_info = device_info

    @property
    def group_id(self):
        """Gets the group_id of this AtcepRoamingDevice.  # noqa: E501

        The identifier of the endpoint group with which the device is associated.  # noqa: E501

        :return: The group_id of this AtcepRoamingDevice.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AtcepRoamingDevice.

        The identifier of the endpoint group with which the device is associated.  # noqa: E501

        :param group_id: The group_id of this AtcepRoamingDevice.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this AtcepRoamingDevice.  # noqa: E501

        The name of the endpoint group with which the device is associated.  # noqa: E501

        :return: The group_name of this AtcepRoamingDevice.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this AtcepRoamingDevice.

        The name of the endpoint group with which the device is associated.  # noqa: E501

        :param group_name: The group_name of this AtcepRoamingDevice.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def name(self):
        """Gets the name of this AtcepRoamingDevice.  # noqa: E501

        The name of the endpoint device.  # noqa: E501

        :return: The name of this AtcepRoamingDevice.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AtcepRoamingDevice.

        The name of the endpoint device.  # noqa: E501

        :param name: The name of this AtcepRoamingDevice.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def net_info(self):
        """Gets the net_info of this AtcepRoamingDevice.  # noqa: E501

        The networking information related to the endpoint device.  # noqa: E501

        :return: The net_info of this AtcepRoamingDevice.  # noqa: E501
        :rtype: AtcepNetInfo
        """
        return self._net_info

    @net_info.setter
    def net_info(self, net_info):
        """Sets the net_info of this AtcepRoamingDevice.

        The networking information related to the endpoint device.  # noqa: E501

        :param net_info: The net_info of this AtcepRoamingDevice.  # noqa: E501
        :type: AtcepNetInfo
        """

        self._net_info = net_info

    @property
    def os_platform(self):
        """Gets the os_platform of this AtcepRoamingDevice.  # noqa: E501

        The operating system of the endpoint device.  # noqa: E501

        :return: The os_platform of this AtcepRoamingDevice.  # noqa: E501
        :rtype: str
        """
        return self._os_platform

    @os_platform.setter
    def os_platform(self, os_platform):
        """Sets the os_platform of this AtcepRoamingDevice.

        The operating system of the endpoint device.  # noqa: E501

        :param os_platform: The os_platform of this AtcepRoamingDevice.  # noqa: E501
        :type: str
        """

        self._os_platform = os_platform

    @property
    def updated_time(self):
        """Gets the updated_time of this AtcepRoamingDevice.  # noqa: E501

        The time when the Roaming Device object was last updated.  # noqa: E501

        :return: The updated_time of this AtcepRoamingDevice.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this AtcepRoamingDevice.

        The time when the Roaming Device object was last updated.  # noqa: E501

        :param updated_time: The updated_time of this AtcepRoamingDevice.  # noqa: E501
        :type: datetime
        """

        self._updated_time = updated_time

    @property
    def user_id(self):
        """Gets the user_id of this AtcepRoamingDevice.  # noqa: E501

        The user identifier of the endpoint device.  # noqa: E501

        :return: The user_id of this AtcepRoamingDevice.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AtcepRoamingDevice.

        The user identifier of the endpoint device.  # noqa: E501

        :param user_id: The user_id of this AtcepRoamingDevice.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def version(self):
        """Gets the version of this AtcepRoamingDevice.  # noqa: E501

        The version of the BloxOne Endpoint client installed on the endpoint device.  # noqa: E501

        :return: The version of this AtcepRoamingDevice.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AtcepRoamingDevice.

        The version of the BloxOne Endpoint client installed on the endpoint device.  # noqa: E501

        :param version: The version of this AtcepRoamingDevice.  # noqa: E501
        :type: str
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AtcepRoamingDevice, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AtcepRoamingDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other