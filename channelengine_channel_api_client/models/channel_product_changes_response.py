# coding: utf-8

"""
    ChannelEngine Channel API

    ChannelEngine API for channels  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from channelengine_channel_api_client.models.channel_product_response import ChannelProductResponse  # noqa: F401,E501


class ChannelProductChangesResponse(object):
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
        'to_be_created': 'list[ChannelProductResponse]',
        'to_be_updated': 'list[ChannelProductResponse]',
        'to_be_removed': 'list[str]'
    }

    attribute_map = {
        'to_be_created': 'ToBeCreated',
        'to_be_updated': 'ToBeUpdated',
        'to_be_removed': 'ToBeRemoved'
    }

    def __init__(self, to_be_created=None, to_be_updated=None, to_be_removed=None):  # noqa: E501
        """ChannelProductChangesResponse - a model defined in Swagger"""  # noqa: E501

        self._to_be_created = None
        self._to_be_updated = None
        self._to_be_removed = None
        self.discriminator = None

        if to_be_created is not None:
            self.to_be_created = to_be_created
        if to_be_updated is not None:
            self.to_be_updated = to_be_updated
        if to_be_removed is not None:
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
        :type: list[ChannelProductResponse]
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
        :type: list[ChannelProductResponse]
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
        :type: list[str]
        """

        self._to_be_removed = to_be_removed

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

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
