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


class ChannelOfferResponse(object):
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
        'channel_product_no': 'str',
        'price': 'float',
        'stock': 'int'
    }

    attribute_map = {
        'channel_product_no': 'ChannelProductNo',
        'price': 'Price',
        'stock': 'Stock'
    }

    def __init__(self, channel_product_no=None, price=None, stock=None):  # noqa: E501
        """ChannelOfferResponse - a model defined in Swagger"""  # noqa: E501

        self._channel_product_no = None
        self._price = None
        self._stock = None
        self.discriminator = None

        if channel_product_no is not None:
            self.channel_product_no = channel_product_no
        if price is not None:
            self.price = price
        if stock is not None:
            self.stock = stock

    @property
    def channel_product_no(self):
        """Gets the channel_product_no of this ChannelOfferResponse.  # noqa: E501

        The unique product reference used by the Channel  # noqa: E501

        :return: The channel_product_no of this ChannelOfferResponse.  # noqa: E501
        :rtype: str
        """
        return self._channel_product_no

    @channel_product_no.setter
    def channel_product_no(self, channel_product_no):
        """Sets the channel_product_no of this ChannelOfferResponse.

        The unique product reference used by the Channel  # noqa: E501

        :param channel_product_no: The channel_product_no of this ChannelOfferResponse.  # noqa: E501
        :type: str
        """

        self._channel_product_no = channel_product_no

    @property
    def price(self):
        """Gets the price of this ChannelOfferResponse.  # noqa: E501


        :return: The price of this ChannelOfferResponse.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ChannelOfferResponse.


        :param price: The price of this ChannelOfferResponse.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def stock(self):
        """Gets the stock of this ChannelOfferResponse.  # noqa: E501


        :return: The stock of this ChannelOfferResponse.  # noqa: E501
        :rtype: int
        """
        return self._stock

    @stock.setter
    def stock(self, stock):
        """Sets the stock of this ChannelOfferResponse.


        :param stock: The stock of this ChannelOfferResponse.  # noqa: E501
        :type: int
        """

        self._stock = stock

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
        if issubclass(ChannelOfferResponse, dict):
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
        if not isinstance(other, ChannelOfferResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
