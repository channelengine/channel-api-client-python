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

from channelengine_channel_api_client.models.channel_references_request import ChannelReferencesRequest  # noqa: F401,E501


class ChannelProcessedChangesRequest(object):
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
        'created': 'list[ChannelReferencesRequest]',
        'updated': 'list[str]',
        'removed': 'list[str]'
    }

    attribute_map = {
        'created': 'Created',
        'updated': 'Updated',
        'removed': 'Removed'
    }

    def __init__(self, created=None, updated=None, removed=None):  # noqa: E501
        """ChannelProcessedChangesRequest - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._updated = None
        self._removed = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if removed is not None:
            self.removed = removed

    @property
    def created(self):
        """Gets the created of this ChannelProcessedChangesRequest.  # noqa: E501

        A collection of pairs of merchant and channel references  of the products which are successfully created. The channel references  are saved such that in subsequent calls these can be used instead of the   merchant references.  # noqa: E501

        :return: The created of this ChannelProcessedChangesRequest.  # noqa: E501
        :rtype: list[ChannelReferencesRequest]
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ChannelProcessedChangesRequest.

        A collection of pairs of merchant and channel references  of the products which are successfully created. The channel references  are saved such that in subsequent calls these can be used instead of the   merchant references.  # noqa: E501

        :param created: The created of this ChannelProcessedChangesRequest.  # noqa: E501
        :type: list[ChannelReferencesRequest]
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ChannelProcessedChangesRequest.  # noqa: E501

        The channel references of the products which are successfully updated.  # noqa: E501

        :return: The updated of this ChannelProcessedChangesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ChannelProcessedChangesRequest.

        The channel references of the products which are successfully updated.  # noqa: E501

        :param updated: The updated of this ChannelProcessedChangesRequest.  # noqa: E501
        :type: list[str]
        """

        self._updated = updated

    @property
    def removed(self):
        """Gets the removed of this ChannelProcessedChangesRequest.  # noqa: E501

        The channel references of the products which are successfully removed.  # noqa: E501

        :return: The removed of this ChannelProcessedChangesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._removed

    @removed.setter
    def removed(self, removed):
        """Sets the removed of this ChannelProcessedChangesRequest.

        The channel references of the products which are successfully removed.  # noqa: E501

        :param removed: The removed of this ChannelProcessedChangesRequest.  # noqa: E501
        :type: list[str]
        """

        self._removed = removed

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
        if not isinstance(other, ChannelProcessedChangesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
