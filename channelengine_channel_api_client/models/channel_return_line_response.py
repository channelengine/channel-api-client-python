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


class ChannelReturnLineResponse(object):
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
        'channel_product_no': 'str',
        'merchant_product_no': 'str',
        'accepted_quantity': 'int',
        'rejected_quantity': 'int',
        'order_line': 'ChannelOrderLineResponse',
        'shipment_status': 'ShipmentLineStatus',
        'quantity': 'int'
    }

    attribute_map = {
        'channel_product_no': 'ChannelProductNo',
        'merchant_product_no': 'MerchantProductNo',
        'accepted_quantity': 'AcceptedQuantity',
        'rejected_quantity': 'RejectedQuantity',
        'order_line': 'OrderLine',
        'shipment_status': 'ShipmentStatus',
        'quantity': 'Quantity'
    }

    def __init__(self, channel_product_no=None, merchant_product_no=None, accepted_quantity=None, rejected_quantity=None, order_line=None, shipment_status=None, quantity=None, local_vars_configuration=None):  # noqa: E501
        """ChannelReturnLineResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._channel_product_no = None
        self._merchant_product_no = None
        self._accepted_quantity = None
        self._rejected_quantity = None
        self._order_line = None
        self._shipment_status = None
        self._quantity = None
        self.discriminator = None

        self.channel_product_no = channel_product_no
        self.merchant_product_no = merchant_product_no
        self.accepted_quantity = accepted_quantity
        self.rejected_quantity = rejected_quantity
        self.order_line = order_line
        self.shipment_status = shipment_status
        self.quantity = quantity

    @property
    def channel_product_no(self):
        """Gets the channel_product_no of this ChannelReturnLineResponse.  # noqa: E501

        The unique product reference used by the Channel.  # noqa: E501

        :return: The channel_product_no of this ChannelReturnLineResponse.  # noqa: E501
        :rtype: str
        """
        return self._channel_product_no

    @channel_product_no.setter
    def channel_product_no(self, channel_product_no):
        """Sets the channel_product_no of this ChannelReturnLineResponse.

        The unique product reference used by the Channel.  # noqa: E501

        :param channel_product_no: The channel_product_no of this ChannelReturnLineResponse.  # noqa: E501
        :type channel_product_no: str
        """
        if self.local_vars_configuration.client_side_validation and channel_product_no is None:  # noqa: E501
            raise ValueError("Invalid value for `channel_product_no`, must not be `None`")  # noqa: E501

        self._channel_product_no = channel_product_no

    @property
    def merchant_product_no(self):
        """Gets the merchant_product_no of this ChannelReturnLineResponse.  # noqa: E501

        The unique product reference used by the Merchant.  # noqa: E501

        :return: The merchant_product_no of this ChannelReturnLineResponse.  # noqa: E501
        :rtype: str
        """
        return self._merchant_product_no

    @merchant_product_no.setter
    def merchant_product_no(self, merchant_product_no):
        """Sets the merchant_product_no of this ChannelReturnLineResponse.

        The unique product reference used by the Merchant.  # noqa: E501

        :param merchant_product_no: The merchant_product_no of this ChannelReturnLineResponse.  # noqa: E501
        :type merchant_product_no: str
        """

        self._merchant_product_no = merchant_product_no

    @property
    def accepted_quantity(self):
        """Gets the accepted_quantity of this ChannelReturnLineResponse.  # noqa: E501

        The number of accepted items of the product in this return (should normally be refunded).  # noqa: E501

        :return: The accepted_quantity of this ChannelReturnLineResponse.  # noqa: E501
        :rtype: int
        """
        return self._accepted_quantity

    @accepted_quantity.setter
    def accepted_quantity(self, accepted_quantity):
        """Sets the accepted_quantity of this ChannelReturnLineResponse.

        The number of accepted items of the product in this return (should normally be refunded).  # noqa: E501

        :param accepted_quantity: The accepted_quantity of this ChannelReturnLineResponse.  # noqa: E501
        :type accepted_quantity: int
        """

        self._accepted_quantity = accepted_quantity

    @property
    def rejected_quantity(self):
        """Gets the rejected_quantity of this ChannelReturnLineResponse.  # noqa: E501

        The number of rejected items of the product in this return (should normally not be refunded).  # noqa: E501

        :return: The rejected_quantity of this ChannelReturnLineResponse.  # noqa: E501
        :rtype: int
        """
        return self._rejected_quantity

    @rejected_quantity.setter
    def rejected_quantity(self, rejected_quantity):
        """Sets the rejected_quantity of this ChannelReturnLineResponse.

        The number of rejected items of the product in this return (should normally not be refunded).  # noqa: E501

        :param rejected_quantity: The rejected_quantity of this ChannelReturnLineResponse.  # noqa: E501
        :type rejected_quantity: int
        """

        self._rejected_quantity = rejected_quantity

    @property
    def order_line(self):
        """Gets the order_line of this ChannelReturnLineResponse.  # noqa: E501

        The order line of the product for the return line.  # noqa: E501

        :return: The order_line of this ChannelReturnLineResponse.  # noqa: E501
        :rtype: ChannelOrderLineResponse
        """
        return self._order_line

    @order_line.setter
    def order_line(self, order_line):
        """Sets the order_line of this ChannelReturnLineResponse.

        The order line of the product for the return line.  # noqa: E501

        :param order_line: The order_line of this ChannelReturnLineResponse.  # noqa: E501
        :type order_line: ChannelOrderLineResponse
        """

        self._order_line = order_line

    @property
    def shipment_status(self):
        """Gets the shipment_status of this ChannelReturnLineResponse.  # noqa: E501

        The status of the product in relation to the shipment.  # noqa: E501

        :return: The shipment_status of this ChannelReturnLineResponse.  # noqa: E501
        :rtype: ShipmentLineStatus
        """
        return self._shipment_status

    @shipment_status.setter
    def shipment_status(self, shipment_status):
        """Sets the shipment_status of this ChannelReturnLineResponse.

        The status of the product in relation to the shipment.  # noqa: E501

        :param shipment_status: The shipment_status of this ChannelReturnLineResponse.  # noqa: E501
        :type shipment_status: ShipmentLineStatus
        """

        self._shipment_status = shipment_status

    @property
    def quantity(self):
        """Gets the quantity of this ChannelReturnLineResponse.  # noqa: E501

        Number of items of the product in this return.  # noqa: E501

        :return: The quantity of this ChannelReturnLineResponse.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ChannelReturnLineResponse.

        Number of items of the product in this return.  # noqa: E501

        :param quantity: The quantity of this ChannelReturnLineResponse.  # noqa: E501
        :type quantity: int
        """
        if self.local_vars_configuration.client_side_validation and quantity is None:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                quantity is not None and quantity < 0):  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._quantity = quantity

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
        if not isinstance(other, ChannelReturnLineResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChannelReturnLineResponse):
            return True

        return self.to_dict() != other.to_dict()