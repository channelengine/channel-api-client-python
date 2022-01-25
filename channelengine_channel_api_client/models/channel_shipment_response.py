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


class ChannelShipmentResponse(object):
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
        'channel_order_no': 'str',
        'lines': 'list[ChannelShipmentLineResponse]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'extra_data': 'dict(str, str)',
        'track_trace_no': 'str',
        'track_trace_url': 'str',
        'return_track_trace_no': 'str',
        'method': 'str',
        'shipped_from_country_code': 'str'
    }

    attribute_map = {
        'channel_order_no': 'ChannelOrderNo',
        'lines': 'Lines',
        'created_at': 'CreatedAt',
        'updated_at': 'UpdatedAt',
        'extra_data': 'ExtraData',
        'track_trace_no': 'TrackTraceNo',
        'track_trace_url': 'TrackTraceUrl',
        'return_track_trace_no': 'ReturnTrackTraceNo',
        'method': 'Method',
        'shipped_from_country_code': 'ShippedFromCountryCode'
    }

    def __init__(self, channel_order_no=None, lines=None, created_at=None, updated_at=None, extra_data=None, track_trace_no=None, track_trace_url=None, return_track_trace_no=None, method=None, shipped_from_country_code=None, local_vars_configuration=None):  # noqa: E501
        """ChannelShipmentResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._channel_order_no = None
        self._lines = None
        self._created_at = None
        self._updated_at = None
        self._extra_data = None
        self._track_trace_no = None
        self._track_trace_url = None
        self._return_track_trace_no = None
        self._method = None
        self._shipped_from_country_code = None
        self.discriminator = None

        self.channel_order_no = channel_order_no
        self.lines = lines
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.extra_data = extra_data
        self.track_trace_no = track_trace_no
        self.track_trace_url = track_trace_url
        self.return_track_trace_no = return_track_trace_no
        self.method = method
        self.shipped_from_country_code = shipped_from_country_code

    @property
    def channel_order_no(self):
        """Gets the channel_order_no of this ChannelShipmentResponse.  # noqa: E501

        The unique order reference used by the Channel.  # noqa: E501

        :return: The channel_order_no of this ChannelShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._channel_order_no

    @channel_order_no.setter
    def channel_order_no(self, channel_order_no):
        """Sets the channel_order_no of this ChannelShipmentResponse.

        The unique order reference used by the Channel.  # noqa: E501

        :param channel_order_no: The channel_order_no of this ChannelShipmentResponse.  # noqa: E501
        :type channel_order_no: str
        """
        if self.local_vars_configuration.client_side_validation and channel_order_no is None:  # noqa: E501
            raise ValueError("Invalid value for `channel_order_no`, must not be `None`")  # noqa: E501

        self._channel_order_no = channel_order_no

    @property
    def lines(self):
        """Gets the lines of this ChannelShipmentResponse.  # noqa: E501


        :return: The lines of this ChannelShipmentResponse.  # noqa: E501
        :rtype: list[ChannelShipmentLineResponse]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this ChannelShipmentResponse.


        :param lines: The lines of this ChannelShipmentResponse.  # noqa: E501
        :type lines: list[ChannelShipmentLineResponse]
        """
        if self.local_vars_configuration.client_side_validation and lines is None:  # noqa: E501
            raise ValueError("Invalid value for `lines`, must not be `None`")  # noqa: E501

        self._lines = lines

    @property
    def created_at(self):
        """Gets the created_at of this ChannelShipmentResponse.  # noqa: E501

        The date at which the shipment was created in ChannelEngine.  # noqa: E501

        :return: The created_at of this ChannelShipmentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ChannelShipmentResponse.

        The date at which the shipment was created in ChannelEngine.  # noqa: E501

        :param created_at: The created_at of this ChannelShipmentResponse.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ChannelShipmentResponse.  # noqa: E501

        The date at which the shipment was last modified in ChannelEngine.  # noqa: E501

        :return: The updated_at of this ChannelShipmentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ChannelShipmentResponse.

        The date at which the shipment was last modified in ChannelEngine.  # noqa: E501

        :param updated_at: The updated_at of this ChannelShipmentResponse.  # noqa: E501
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def extra_data(self):
        """Gets the extra_data of this ChannelShipmentResponse.  # noqa: E501

        Extra data on the order. Each item must have an unqiue key  # noqa: E501

        :return: The extra_data of this ChannelShipmentResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extra_data

    @extra_data.setter
    def extra_data(self, extra_data):
        """Sets the extra_data of this ChannelShipmentResponse.

        Extra data on the order. Each item must have an unqiue key  # noqa: E501

        :param extra_data: The extra_data of this ChannelShipmentResponse.  # noqa: E501
        :type extra_data: dict(str, str)
        """

        self._extra_data = extra_data

    @property
    def track_trace_no(self):
        """Gets the track_trace_no of this ChannelShipmentResponse.  # noqa: E501

        The unique shipping reference used by the Shipping carrier (track&trace number).  # noqa: E501

        :return: The track_trace_no of this ChannelShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._track_trace_no

    @track_trace_no.setter
    def track_trace_no(self, track_trace_no):
        """Sets the track_trace_no of this ChannelShipmentResponse.

        The unique shipping reference used by the Shipping carrier (track&trace number).  # noqa: E501

        :param track_trace_no: The track_trace_no of this ChannelShipmentResponse.  # noqa: E501
        :type track_trace_no: str
        """
        if (self.local_vars_configuration.client_side_validation and
                track_trace_no is not None and len(track_trace_no) > 50):
            raise ValueError("Invalid value for `track_trace_no`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                track_trace_no is not None and len(track_trace_no) < 0):
            raise ValueError("Invalid value for `track_trace_no`, length must be greater than or equal to `0`")  # noqa: E501

        self._track_trace_no = track_trace_no

    @property
    def track_trace_url(self):
        """Gets the track_trace_url of this ChannelShipmentResponse.  # noqa: E501

        A link to a page of the carrier where the customer can track the shipping of her package.  # noqa: E501

        :return: The track_trace_url of this ChannelShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._track_trace_url

    @track_trace_url.setter
    def track_trace_url(self, track_trace_url):
        """Sets the track_trace_url of this ChannelShipmentResponse.

        A link to a page of the carrier where the customer can track the shipping of her package.  # noqa: E501

        :param track_trace_url: The track_trace_url of this ChannelShipmentResponse.  # noqa: E501
        :type track_trace_url: str
        """
        if (self.local_vars_configuration.client_side_validation and
                track_trace_url is not None and len(track_trace_url) > 250):
            raise ValueError("Invalid value for `track_trace_url`, length must be less than or equal to `250`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                track_trace_url is not None and len(track_trace_url) < 0):
            raise ValueError("Invalid value for `track_trace_url`, length must be greater than or equal to `0`")  # noqa: E501

        self._track_trace_url = track_trace_url

    @property
    def return_track_trace_no(self):
        """Gets the return_track_trace_no of this ChannelShipmentResponse.  # noqa: E501

        The unique return shipping reference that may be used by the Shipping carrier (track & trace number) if the shipment is returned.  # noqa: E501

        :return: The return_track_trace_no of this ChannelShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._return_track_trace_no

    @return_track_trace_no.setter
    def return_track_trace_no(self, return_track_trace_no):
        """Sets the return_track_trace_no of this ChannelShipmentResponse.

        The unique return shipping reference that may be used by the Shipping carrier (track & trace number) if the shipment is returned.  # noqa: E501

        :param return_track_trace_no: The return_track_trace_no of this ChannelShipmentResponse.  # noqa: E501
        :type return_track_trace_no: str
        """
        if (self.local_vars_configuration.client_side_validation and
                return_track_trace_no is not None and len(return_track_trace_no) > 50):
            raise ValueError("Invalid value for `return_track_trace_no`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                return_track_trace_no is not None and len(return_track_trace_no) < 0):
            raise ValueError("Invalid value for `return_track_trace_no`, length must be greater than or equal to `0`")  # noqa: E501

        self._return_track_trace_no = return_track_trace_no

    @property
    def method(self):
        """Gets the method of this ChannelShipmentResponse.  # noqa: E501

        Shipment method: the carrier used for shipping the package. E.g. DHL, postNL.  # noqa: E501

        :return: The method of this ChannelShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ChannelShipmentResponse.

        Shipment method: the carrier used for shipping the package. E.g. DHL, postNL.  # noqa: E501

        :param method: The method of this ChannelShipmentResponse.  # noqa: E501
        :type method: str
        """
        if (self.local_vars_configuration.client_side_validation and
                method is not None and len(method) > 50):
            raise ValueError("Invalid value for `method`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                method is not None and len(method) < 0):
            raise ValueError("Invalid value for `method`, length must be greater than or equal to `0`")  # noqa: E501

        self._method = method

    @property
    def shipped_from_country_code(self):
        """Gets the shipped_from_country_code of this ChannelShipmentResponse.  # noqa: E501

        The code of the country from where the package is being shipped.  # noqa: E501

        :return: The shipped_from_country_code of this ChannelShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._shipped_from_country_code

    @shipped_from_country_code.setter
    def shipped_from_country_code(self, shipped_from_country_code):
        """Sets the shipped_from_country_code of this ChannelShipmentResponse.

        The code of the country from where the package is being shipped.  # noqa: E501

        :param shipped_from_country_code: The shipped_from_country_code of this ChannelShipmentResponse.  # noqa: E501
        :type shipped_from_country_code: str
        """
        if (self.local_vars_configuration.client_side_validation and
                shipped_from_country_code is not None and len(shipped_from_country_code) > 3):
            raise ValueError("Invalid value for `shipped_from_country_code`, length must be less than or equal to `3`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                shipped_from_country_code is not None and len(shipped_from_country_code) < 0):
            raise ValueError("Invalid value for `shipped_from_country_code`, length must be greater than or equal to `0`")  # noqa: E501

        self._shipped_from_country_code = shipped_from_country_code

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
        if not isinstance(other, ChannelShipmentResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChannelShipmentResponse):
            return True

        return self.to_dict() != other.to_dict()
