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


class NetInfoState(object):
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
        'protection': 'str',
        'upgrade': 'str'
    }

    attribute_map = {
        'protection': 'protection',
        'upgrade': 'upgrade'
    }

    def __init__(self, protection=None, upgrade=None):  # noqa: E501
        """NetInfoState - a model defined in Swagger"""  # noqa: E501

        self._protection = None
        self._upgrade = None
        self.discriminator = None

        if protection is not None:
            self.protection = protection
        if upgrade is not None:
            self.upgrade = upgrade

    @property
    def protection(self):
        """Gets the protection of this NetInfoState.  # noqa: E501

        BloxOne Endpoint protection state.  # noqa: E501

        :return: The protection of this NetInfoState.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this NetInfoState.

        BloxOne Endpoint protection state.  # noqa: E501

        :param protection: The protection of this NetInfoState.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN_SUB_STATUS", "MISSING_CUSTOMER_ID", "PENDING_REGISTRATION", "INVALID_CUSTOMER_ID", "FAILED_REGISTRATION", "ACCOUNT_ERROR", "CAPTIVE_PORTAL", "PORTAL_ERROR", "PERMANENT_DEACTIVATION", "TEMP_DEACTIVATION", "DNS_PROVIDING_SOFTWARE", "DNS_TESTING", "DNS_ERROR", "NO_ACTIVE_CARD", "PROXY_ERROR", "PENDING_ACCOUNT_CHECK", "NO_DNS_SERVER", "PORTAL_FQDN_NOT_RESOLVED", "ON_PREMISE_TESTING", "ON_PREMISE_SUCCESS", "DETECTED_INTERCEPTION", "DETECTED_F5_VPN", "NOT_FOUND", "CLOUD"]  # noqa: E501
        if protection not in allowed_values:
            raise ValueError(
                "Invalid value for `protection` ({0}), must be one of {1}"  # noqa: E501
                .format(protection, allowed_values)
            )

        self._protection = protection

    @property
    def upgrade(self):
        """Gets the upgrade of this NetInfoState.  # noqa: E501

        BloxOne Endpoint client software upgrade state.  # noqa: E501

        :return: The upgrade of this NetInfoState.  # noqa: E501
        :rtype: str
        """
        return self._upgrade

    @upgrade.setter
    def upgrade(self, upgrade):
        """Sets the upgrade of this NetInfoState.

        BloxOne Endpoint client software upgrade state.  # noqa: E501

        :param upgrade: The upgrade of this NetInfoState.  # noqa: E501
        :type: str
        """
        allowed_values = ["NO_OPERATION", "NEW_VERSION_AVAILABLE", "INITIATE_DOWNLOAD", "DOWNLOADING", "DELAY_RESTART", "UPGRADE_PENDING", "UPGRADING"]  # noqa: E501
        if upgrade not in allowed_values:
            raise ValueError(
                "Invalid value for `upgrade` ({0}), must be one of {1}"  # noqa: E501
                .format(upgrade, allowed_values)
            )

        self._upgrade = upgrade

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
        if issubclass(NetInfoState, dict):
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
        if not isinstance(other, NetInfoState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
