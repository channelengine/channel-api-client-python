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

from channelengine_channel_api_client.models.address import Address  # noqa: F401,E501
from channelengine_channel_api_client.models.channel_order_line_request import ChannelOrderLineRequest  # noqa: F401,E501


class ChannelOrderRequest(object):
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
        'lines': 'list[ChannelOrderLineRequest]',
        'phone': 'str',
        'email': 'str',
        'company_registration_no': 'str',
        'vat_no': 'str',
        'payment_method': 'str',
        'shipping_costs_incl_vat': 'float',
        'currency_code': 'str',
        'order_date': 'datetime',
        'channel_customer_no': 'str',
        'billing_address': 'Address',
        'shipping_address': 'Address',
        'extra_data': 'dict(str, str)'
    }

    attribute_map = {
        'channel_order_no': 'ChannelOrderNo',
        'lines': 'Lines',
        'phone': 'Phone',
        'email': 'Email',
        'company_registration_no': 'CompanyRegistrationNo',
        'vat_no': 'VatNo',
        'payment_method': 'PaymentMethod',
        'shipping_costs_incl_vat': 'ShippingCostsInclVat',
        'currency_code': 'CurrencyCode',
        'order_date': 'OrderDate',
        'channel_customer_no': 'ChannelCustomerNo',
        'billing_address': 'BillingAddress',
        'shipping_address': 'ShippingAddress',
        'extra_data': 'ExtraData'
    }

    def __init__(self, channel_order_no=None, lines=None, phone=None, email=None, company_registration_no=None, vat_no=None, payment_method=None, shipping_costs_incl_vat=None, currency_code=None, order_date=None, channel_customer_no=None, billing_address=None, shipping_address=None, extra_data=None):  # noqa: E501
        """ChannelOrderRequest - a model defined in Swagger"""  # noqa: E501

        self._channel_order_no = None
        self._lines = None
        self._phone = None
        self._email = None
        self._company_registration_no = None
        self._vat_no = None
        self._payment_method = None
        self._shipping_costs_incl_vat = None
        self._currency_code = None
        self._order_date = None
        self._channel_customer_no = None
        self._billing_address = None
        self._shipping_address = None
        self._extra_data = None
        self.discriminator = None

        self.channel_order_no = channel_order_no
        self.lines = lines
        if phone is not None:
            self.phone = phone
        self.email = email
        if company_registration_no is not None:
            self.company_registration_no = company_registration_no
        if vat_no is not None:
            self.vat_no = vat_no
        if payment_method is not None:
            self.payment_method = payment_method
        self.shipping_costs_incl_vat = shipping_costs_incl_vat
        self.currency_code = currency_code
        self.order_date = order_date
        if channel_customer_no is not None:
            self.channel_customer_no = channel_customer_no
        self.billing_address = billing_address
        self.shipping_address = shipping_address
        if extra_data is not None:
            self.extra_data = extra_data

    @property
    def channel_order_no(self):
        """Gets the channel_order_no of this ChannelOrderRequest.  # noqa: E501

        The unique order reference used by the Channel  # noqa: E501

        :return: The channel_order_no of this ChannelOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._channel_order_no

    @channel_order_no.setter
    def channel_order_no(self, channel_order_no):
        """Sets the channel_order_no of this ChannelOrderRequest.

        The unique order reference used by the Channel  # noqa: E501

        :param channel_order_no: The channel_order_no of this ChannelOrderRequest.  # noqa: E501
        :type: str
        """
        if channel_order_no is None:
            raise ValueError("Invalid value for `channel_order_no`, must not be `None`")  # noqa: E501
        if channel_order_no is not None and len(channel_order_no) > 50:
            raise ValueError("Invalid value for `channel_order_no`, length must be less than or equal to `50`")  # noqa: E501
        if channel_order_no is not None and len(channel_order_no) < 0:
            raise ValueError("Invalid value for `channel_order_no`, length must be greater than or equal to `0`")  # noqa: E501

        self._channel_order_no = channel_order_no

    @property
    def lines(self):
        """Gets the lines of this ChannelOrderRequest.  # noqa: E501

        The order lines  # noqa: E501

        :return: The lines of this ChannelOrderRequest.  # noqa: E501
        :rtype: list[ChannelOrderLineRequest]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this ChannelOrderRequest.

        The order lines  # noqa: E501

        :param lines: The lines of this ChannelOrderRequest.  # noqa: E501
        :type: list[ChannelOrderLineRequest]
        """
        if lines is None:
            raise ValueError("Invalid value for `lines`, must not be `None`")  # noqa: E501

        self._lines = lines

    @property
    def phone(self):
        """Gets the phone of this ChannelOrderRequest.  # noqa: E501

        The customer's telephone number  # noqa: E501

        :return: The phone of this ChannelOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ChannelOrderRequest.

        The customer's telephone number  # noqa: E501

        :param phone: The phone of this ChannelOrderRequest.  # noqa: E501
        :type: str
        """
        if phone is not None and len(phone) > 20:
            raise ValueError("Invalid value for `phone`, length must be less than or equal to `20`")  # noqa: E501
        if phone is not None and len(phone) < 0:
            raise ValueError("Invalid value for `phone`, length must be greater than or equal to `0`")  # noqa: E501

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this ChannelOrderRequest.  # noqa: E501

        The customer's email  # noqa: E501

        :return: The email of this ChannelOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ChannelOrderRequest.

        The customer's email  # noqa: E501

        :param email: The email of this ChannelOrderRequest.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if email is not None and len(email) > 250:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `250`")  # noqa: E501
        if email is not None and len(email) < 0:
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `0`")  # noqa: E501

        self._email = email

    @property
    def company_registration_no(self):
        """Gets the company_registration_no of this ChannelOrderRequest.  # noqa: E501

        Optional. A company's chamber of commerce number  # noqa: E501

        :return: The company_registration_no of this ChannelOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_registration_no

    @company_registration_no.setter
    def company_registration_no(self, company_registration_no):
        """Sets the company_registration_no of this ChannelOrderRequest.

        Optional. A company's chamber of commerce number  # noqa: E501

        :param company_registration_no: The company_registration_no of this ChannelOrderRequest.  # noqa: E501
        :type: str
        """
        if company_registration_no is not None and len(company_registration_no) > 50:
            raise ValueError("Invalid value for `company_registration_no`, length must be less than or equal to `50`")  # noqa: E501
        if company_registration_no is not None and len(company_registration_no) < 0:
            raise ValueError("Invalid value for `company_registration_no`, length must be greater than or equal to `0`")  # noqa: E501

        self._company_registration_no = company_registration_no

    @property
    def vat_no(self):
        """Gets the vat_no of this ChannelOrderRequest.  # noqa: E501

        Optional. A company's VAT number  # noqa: E501

        :return: The vat_no of this ChannelOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._vat_no

    @vat_no.setter
    def vat_no(self, vat_no):
        """Sets the vat_no of this ChannelOrderRequest.

        Optional. A company's VAT number  # noqa: E501

        :param vat_no: The vat_no of this ChannelOrderRequest.  # noqa: E501
        :type: str
        """
        if vat_no is not None and len(vat_no) > 50:
            raise ValueError("Invalid value for `vat_no`, length must be less than or equal to `50`")  # noqa: E501
        if vat_no is not None and len(vat_no) < 0:
            raise ValueError("Invalid value for `vat_no`, length must be greater than or equal to `0`")  # noqa: E501

        self._vat_no = vat_no

    @property
    def payment_method(self):
        """Gets the payment_method of this ChannelOrderRequest.  # noqa: E501

        The payment method used on the order  # noqa: E501

        :return: The payment_method of this ChannelOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this ChannelOrderRequest.

        The payment method used on the order  # noqa: E501

        :param payment_method: The payment_method of this ChannelOrderRequest.  # noqa: E501
        :type: str
        """
        if payment_method is not None and len(payment_method) > 50:
            raise ValueError("Invalid value for `payment_method`, length must be less than or equal to `50`")  # noqa: E501
        if payment_method is not None and len(payment_method) < 0:
            raise ValueError("Invalid value for `payment_method`, length must be greater than or equal to `0`")  # noqa: E501

        self._payment_method = payment_method

    @property
    def shipping_costs_incl_vat(self):
        """Gets the shipping_costs_incl_vat of this ChannelOrderRequest.  # noqa: E501

        The shipping fee including VAT  (in the shop's base currency calculated using the exchange rate at the time of ordering).  # noqa: E501

        :return: The shipping_costs_incl_vat of this ChannelOrderRequest.  # noqa: E501
        :rtype: float
        """
        return self._shipping_costs_incl_vat

    @shipping_costs_incl_vat.setter
    def shipping_costs_incl_vat(self, shipping_costs_incl_vat):
        """Sets the shipping_costs_incl_vat of this ChannelOrderRequest.

        The shipping fee including VAT  (in the shop's base currency calculated using the exchange rate at the time of ordering).  # noqa: E501

        :param shipping_costs_incl_vat: The shipping_costs_incl_vat of this ChannelOrderRequest.  # noqa: E501
        :type: float
        """
        if shipping_costs_incl_vat is None:
            raise ValueError("Invalid value for `shipping_costs_incl_vat`, must not be `None`")  # noqa: E501

        self._shipping_costs_incl_vat = shipping_costs_incl_vat

    @property
    def currency_code(self):
        """Gets the currency_code of this ChannelOrderRequest.  # noqa: E501

        The currency code for the amounts of the order  # noqa: E501

        :return: The currency_code of this ChannelOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this ChannelOrderRequest.

        The currency code for the amounts of the order  # noqa: E501

        :param currency_code: The currency_code of this ChannelOrderRequest.  # noqa: E501
        :type: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")  # noqa: E501
        if currency_code is not None and len(currency_code) > 3:
            raise ValueError("Invalid value for `currency_code`, length must be less than or equal to `3`")  # noqa: E501

        self._currency_code = currency_code

    @property
    def order_date(self):
        """Gets the order_date of this ChannelOrderRequest.  # noqa: E501

        The date the order was done  # noqa: E501

        :return: The order_date of this ChannelOrderRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        """Sets the order_date of this ChannelOrderRequest.

        The date the order was done  # noqa: E501

        :param order_date: The order_date of this ChannelOrderRequest.  # noqa: E501
        :type: datetime
        """
        if order_date is None:
            raise ValueError("Invalid value for `order_date`, must not be `None`")  # noqa: E501

        self._order_date = order_date

    @property
    def channel_customer_no(self):
        """Gets the channel_customer_no of this ChannelOrderRequest.  # noqa: E501

        The unique customer reference used by the channel  # noqa: E501

        :return: The channel_customer_no of this ChannelOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._channel_customer_no

    @channel_customer_no.setter
    def channel_customer_no(self, channel_customer_no):
        """Sets the channel_customer_no of this ChannelOrderRequest.

        The unique customer reference used by the channel  # noqa: E501

        :param channel_customer_no: The channel_customer_no of this ChannelOrderRequest.  # noqa: E501
        :type: str
        """
        if channel_customer_no is not None and len(channel_customer_no) > 50:
            raise ValueError("Invalid value for `channel_customer_no`, length must be less than or equal to `50`")  # noqa: E501
        if channel_customer_no is not None and len(channel_customer_no) < 0:
            raise ValueError("Invalid value for `channel_customer_no`, length must be greater than or equal to `0`")  # noqa: E501

        self._channel_customer_no = channel_customer_no

    @property
    def billing_address(self):
        """Gets the billing_address of this ChannelOrderRequest.  # noqa: E501

        The billing or invoice address  # noqa: E501

        :return: The billing_address of this ChannelOrderRequest.  # noqa: E501
        :rtype: Address
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this ChannelOrderRequest.

        The billing or invoice address  # noqa: E501

        :param billing_address: The billing_address of this ChannelOrderRequest.  # noqa: E501
        :type: Address
        """
        if billing_address is None:
            raise ValueError("Invalid value for `billing_address`, must not be `None`")  # noqa: E501

        self._billing_address = billing_address

    @property
    def shipping_address(self):
        """Gets the shipping_address of this ChannelOrderRequest.  # noqa: E501

        The shipping address  # noqa: E501

        :return: The shipping_address of this ChannelOrderRequest.  # noqa: E501
        :rtype: Address
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this ChannelOrderRequest.

        The shipping address  # noqa: E501

        :param shipping_address: The shipping_address of this ChannelOrderRequest.  # noqa: E501
        :type: Address
        """
        if shipping_address is None:
            raise ValueError("Invalid value for `shipping_address`, must not be `None`")  # noqa: E501

        self._shipping_address = shipping_address

    @property
    def extra_data(self):
        """Gets the extra_data of this ChannelOrderRequest.  # noqa: E501

        Extra data on the order  # noqa: E501

        :return: The extra_data of this ChannelOrderRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extra_data

    @extra_data.setter
    def extra_data(self, extra_data):
        """Sets the extra_data of this ChannelOrderRequest.

        Extra data on the order  # noqa: E501

        :param extra_data: The extra_data of this ChannelOrderRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._extra_data = extra_data

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
        if not isinstance(other, ChannelOrderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
