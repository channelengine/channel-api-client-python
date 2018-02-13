# coding: utf-8

"""
    ChannelEngine Channel API

    ChannelEngine API for channels  # noqa: E501

    OpenAPI spec version: 2.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from channelengine_channel_api_client.models.channel_cancellation_line_response import ChannelCancellationLineResponse  # noqa: F401,E501


class ChannelCancellationResponse(object):
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
        'channel_order_no': 'str',
        'lines': 'list[ChannelCancellationLineResponse]',
        'reason': 'str'
    }

    attribute_map = {
        'channel_order_no': 'ChannelOrderNo',
        'lines': 'Lines',
        'reason': 'Reason'
    }

    def __init__(self, channel_order_no=None, lines=None, reason=None):  # noqa: E501
        """ChannelCancellationResponse - a model defined in Swagger"""  # noqa: E501

        self._channel_order_no = None
        self._lines = None
        self._reason = None
        self.discriminator = None

        self.channel_order_no = channel_order_no
        self.lines = lines
        if reason is not None:
            self.reason = reason

    @property
    def channel_order_no(self):
        """Gets the channel_order_no of this ChannelCancellationResponse.  # noqa: E501


        :return: The channel_order_no of this ChannelCancellationResponse.  # noqa: E501
        :rtype: str
        """
        return self._channel_order_no

    @channel_order_no.setter
    def channel_order_no(self, channel_order_no):
        """Sets the channel_order_no of this ChannelCancellationResponse.


        :param channel_order_no: The channel_order_no of this ChannelCancellationResponse.  # noqa: E501
        :type: str
        """
        if channel_order_no is None:
            raise ValueError("Invalid value for `channel_order_no`, must not be `None`")  # noqa: E501

        self._channel_order_no = channel_order_no

    @property
    def lines(self):
        """Gets the lines of this ChannelCancellationResponse.  # noqa: E501


        :return: The lines of this ChannelCancellationResponse.  # noqa: E501
        :rtype: list[ChannelCancellationLineResponse]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this ChannelCancellationResponse.


        :param lines: The lines of this ChannelCancellationResponse.  # noqa: E501
        :type: list[ChannelCancellationLineResponse]
        """
        if lines is None:
            raise ValueError("Invalid value for `lines`, must not be `None`")  # noqa: E501

        self._lines = lines

    @property
    def reason(self):
        """Gets the reason of this ChannelCancellationResponse.  # noqa: E501


        :return: The reason of this ChannelCancellationResponse.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ChannelCancellationResponse.


        :param reason: The reason of this ChannelCancellationResponse.  # noqa: E501
        :type: str
        """

        self._reason = reason

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
        if not isinstance(other, ChannelCancellationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
