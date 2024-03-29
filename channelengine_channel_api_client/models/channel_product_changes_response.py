# coding: utf-8

"""
    ChannelEngine Channel API

    ChannelEngine API for channels  # noqa: E501

    The version of the OpenAPI document: 2.9.10
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from channelengine_channel_api_client.configuration import Configuration


class ChannelProductChangesResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'to_be_created': 'list[ChannelProductResponse]',
        'to_be_updated': 'list[ChannelProductResponse]',
        'to_be_removed': 'list[str]'
    }

    attribute_map = {
        'to_be_created': 'ToBeCreated',
        'to_be_updated': 'ToBeUpdated',
        'to_be_removed': 'ToBeRemoved'
    }

    def __init__(self, to_be_created=None, to_be_updated=None, to_be_removed=None, local_vars_configuration=None):  # noqa: E501
        """ChannelProductChangesResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._to_be_created = None
        self._to_be_updated = None
        self._to_be_removed = None
        self.discriminator = None

        self.to_be_created = to_be_created
        self.to_be_updated = to_be_updated
        self.to_be_removed = to_be_removed

    @property
    def to_be_created(self):
        """Gets the to_be_created of this ChannelProductChangesResponse.  # noqa: E501


        :return: The to_be_created of this ChannelProductChangesResponse.  # noqa: E501
        :rtype: list[ChannelProductResponse]
        """
        return self._to_be_created

    @to_be_created.setter
    def to_be_created(self, to_be_created):
        """Sets the to_be_created of this ChannelProductChangesResponse.


        :param to_be_created: The to_be_created of this ChannelProductChangesResponse.  # noqa: E501
        :type to_be_created: list[ChannelProductResponse]
        """

        self._to_be_created = to_be_created

    @property
    def to_be_updated(self):
        """Gets the to_be_updated of this ChannelProductChangesResponse.  # noqa: E501


        :return: The to_be_updated of this ChannelProductChangesResponse.  # noqa: E501
        :rtype: list[ChannelProductResponse]
        """
        return self._to_be_updated

    @to_be_updated.setter
    def to_be_updated(self, to_be_updated):
        """Sets the to_be_updated of this ChannelProductChangesResponse.


        :param to_be_updated: The to_be_updated of this ChannelProductChangesResponse.  # noqa: E501
        :type to_be_updated: list[ChannelProductResponse]
        """

        self._to_be_updated = to_be_updated

    @property
    def to_be_removed(self):
        """Gets the to_be_removed of this ChannelProductChangesResponse.  # noqa: E501


        :return: The to_be_removed of this ChannelProductChangesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._to_be_removed

    @to_be_removed.setter
    def to_be_removed(self, to_be_removed):
        """Sets the to_be_removed of this ChannelProductChangesResponse.


        :param to_be_removed: The to_be_removed of this ChannelProductChangesResponse.  # noqa: E501
        :type to_be_removed: list[str]
        """

        self._to_be_removed = to_be_removed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChannelProductChangesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChannelProductChangesResponse):
            return True

        return self.to_dict() != other.to_dict()
