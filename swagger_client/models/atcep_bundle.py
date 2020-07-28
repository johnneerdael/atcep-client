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


class AtcepBundle(object):
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
        'bundle_url': 'str',
        'checksum_url': 'str',
        'platform': 'str'
    }

    attribute_map = {
        'bundle_url': 'bundle_url',
        'checksum_url': 'checksum_url',
        'platform': 'platform'
    }

    def __init__(self, bundle_url=None, checksum_url=None, platform=None):  # noqa: E501
        """AtcepBundle - a model defined in Swagger"""  # noqa: E501

        self._bundle_url = None
        self._checksum_url = None
        self._platform = None
        self.discriminator = None

        if bundle_url is not None:
            self.bundle_url = bundle_url
        if checksum_url is not None:
            self.checksum_url = checksum_url
        if platform is not None:
            self.platform = platform

    @property
    def bundle_url(self):
        """Gets the bundle_url of this AtcepBundle.  # noqa: E501

        The download URL of the endpoint logs.  # noqa: E501

        :return: The bundle_url of this AtcepBundle.  # noqa: E501
        :rtype: str
        """
        return self._bundle_url

    @bundle_url.setter
    def bundle_url(self, bundle_url):
        """Sets the bundle_url of this AtcepBundle.

        The download URL of the endpoint logs.  # noqa: E501

        :param bundle_url: The bundle_url of this AtcepBundle.  # noqa: E501
        :type: str
        """

        self._bundle_url = bundle_url

    @property
    def checksum_url(self):
        """Gets the checksum_url of this AtcepBundle.  # noqa: E501

        The URL of the bundle checksum.  # noqa: E501

        :return: The checksum_url of this AtcepBundle.  # noqa: E501
        :rtype: str
        """
        return self._checksum_url

    @checksum_url.setter
    def checksum_url(self, checksum_url):
        """Sets the checksum_url of this AtcepBundle.

        The URL of the bundle checksum.  # noqa: E501

        :param checksum_url: The checksum_url of this AtcepBundle.  # noqa: E501
        :type: str
        """

        self._checksum_url = checksum_url

    @property
    def platform(self):
        """Gets the platform of this AtcepBundle.  # noqa: E501

        The operating system on which endpoint is installed.  # noqa: E501

        :return: The platform of this AtcepBundle.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this AtcepBundle.

        The operating system on which endpoint is installed.  # noqa: E501

        :param platform: The platform of this AtcepBundle.  # noqa: E501
        :type: str
        """

        self._platform = platform

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
        if issubclass(AtcepBundle, dict):
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
        if not isinstance(other, AtcepBundle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
