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


class AtcepNetInfo(object):
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
        'fqdn': 'str',
        'ipv4_addr_list': 'list[str]',
        'mac_addr': 'list[str]',
        'state': 'NetInfoState'
    }

    attribute_map = {
        'fqdn': 'fqdn',
        'ipv4_addr_list': 'ipv4_addr_list',
        'mac_addr': 'mac_addr',
        'state': 'state'
    }

    def __init__(self, fqdn=None, ipv4_addr_list=None, mac_addr=None, state=None):  # noqa: E501
        """AtcepNetInfo - a model defined in Swagger"""  # noqa: E501

        self._fqdn = None
        self._ipv4_addr_list = None
        self._mac_addr = None
        self._state = None
        self.discriminator = None

        if fqdn is not None:
            self.fqdn = fqdn
        if ipv4_addr_list is not None:
            self.ipv4_addr_list = ipv4_addr_list
        if mac_addr is not None:
            self.mac_addr = mac_addr
        if state is not None:
            self.state = state

    @property
    def fqdn(self):
        """Gets the fqdn of this AtcepNetInfo.  # noqa: E501

        The FQDN of the endpoint device.  # noqa: E501

        :return: The fqdn of this AtcepNetInfo.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this AtcepNetInfo.

        The FQDN of the endpoint device.  # noqa: E501

        :param fqdn: The fqdn of this AtcepNetInfo.  # noqa: E501
        :type: str
        """

        self._fqdn = fqdn

    @property
    def ipv4_addr_list(self):
        """Gets the ipv4_addr_list of this AtcepNetInfo.  # noqa: E501

        The list of IPv4 addresses of the endpoint device.  # noqa: E501

        :return: The ipv4_addr_list of this AtcepNetInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._ipv4_addr_list

    @ipv4_addr_list.setter
    def ipv4_addr_list(self, ipv4_addr_list):
        """Sets the ipv4_addr_list of this AtcepNetInfo.

        The list of IPv4 addresses of the endpoint device.  # noqa: E501

        :param ipv4_addr_list: The ipv4_addr_list of this AtcepNetInfo.  # noqa: E501
        :type: list[str]
        """

        self._ipv4_addr_list = ipv4_addr_list

    @property
    def mac_addr(self):
        """Gets the mac_addr of this AtcepNetInfo.  # noqa: E501

        The list of MAC addresses of the endpoint device.  # noqa: E501

        :return: The mac_addr of this AtcepNetInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._mac_addr

    @mac_addr.setter
    def mac_addr(self, mac_addr):
        """Sets the mac_addr of this AtcepNetInfo.

        The list of MAC addresses of the endpoint device.  # noqa: E501

        :param mac_addr: The mac_addr of this AtcepNetInfo.  # noqa: E501
        :type: list[str]
        """

        self._mac_addr = mac_addr

    @property
    def state(self):
        """Gets the state of this AtcepNetInfo.  # noqa: E501

        The state of the BloxOne Endpoint client software of the endpoint device. That can be either \"protection\" or \"upgrade\".  # noqa: E501

        :return: The state of this AtcepNetInfo.  # noqa: E501
        :rtype: NetInfoState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AtcepNetInfo.

        The state of the BloxOne Endpoint client software of the endpoint device. That can be either \"protection\" or \"upgrade\".  # noqa: E501

        :param state: The state of this AtcepNetInfo.  # noqa: E501
        :type: NetInfoState
        """

        self._state = state

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
        if issubclass(AtcepNetInfo, dict):
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
        if not isinstance(other, AtcepNetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
