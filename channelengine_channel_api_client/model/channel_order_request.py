"""
    ChannelEngine Channel API

    ChannelEngine API for channels  # noqa: E501

    The version of the OpenAPI document: 2.13.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from channelengine_channel_api_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from channelengine_channel_api_client.exceptions import ApiAttributeError


def lazy_import():
    from channelengine_channel_api_client.model.channel_address_request import ChannelAddressRequest
    from channelengine_channel_api_client.model.channel_order_line_request import ChannelOrderLineRequest
    globals()['ChannelAddressRequest'] = ChannelAddressRequest
    globals()['ChannelOrderLineRequest'] = ChannelOrderLineRequest


class ChannelOrderRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('channel_order_no',): {
            'max_length': 60,
            'min_length': 0,
        },
        ('email',): {
            'max_length': 250,
            'min_length': 0,
        },
        ('shipping_costs_incl_vat',): {
            'inclusive_minimum': 0,
        },
        ('currency_code',): {
            'max_length': 3,
        },
        ('phone',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('company_registration_no',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('vat_no',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('payment_method',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('payment_reference_no',): {
            'max_length': 250,
            'min_length': 0,
        },
        ('channel_customer_no',): {
            'max_length': 50,
            'min_length': 0,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'billing_address': (ChannelAddressRequest,),  # noqa: E501
            'shipping_address': (ChannelAddressRequest,),  # noqa: E501
            'channel_order_no': (str,),  # noqa: E501
            'lines': ([ChannelOrderLineRequest],),  # noqa: E501
            'email': (str,),  # noqa: E501
            'shipping_costs_incl_vat': (float,),  # noqa: E501
            'currency_code': (str,),  # noqa: E501
            'order_date': (datetime,),  # noqa: E501
            'is_business_order': (bool, none_type,),  # noqa: E501
            'key_is_merchant_product_no': (bool,),  # noqa: E501
            'phone': (str, none_type,),  # noqa: E501
            'company_registration_no': (str, none_type,),  # noqa: E501
            'vat_no': (str, none_type,),  # noqa: E501
            'payment_method': (str, none_type,),  # noqa: E501
            'payment_reference_no': (str, none_type,),  # noqa: E501
            'channel_customer_no': (str, none_type,),  # noqa: E501
            'extra_data': ({str: (str,)}, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'billing_address': 'BillingAddress',  # noqa: E501
        'shipping_address': 'ShippingAddress',  # noqa: E501
        'channel_order_no': 'ChannelOrderNo',  # noqa: E501
        'lines': 'Lines',  # noqa: E501
        'email': 'Email',  # noqa: E501
        'shipping_costs_incl_vat': 'ShippingCostsInclVat',  # noqa: E501
        'currency_code': 'CurrencyCode',  # noqa: E501
        'order_date': 'OrderDate',  # noqa: E501
        'is_business_order': 'IsBusinessOrder',  # noqa: E501
        'key_is_merchant_product_no': 'KeyIsMerchantProductNo',  # noqa: E501
        'phone': 'Phone',  # noqa: E501
        'company_registration_no': 'CompanyRegistrationNo',  # noqa: E501
        'vat_no': 'VatNo',  # noqa: E501
        'payment_method': 'PaymentMethod',  # noqa: E501
        'payment_reference_no': 'PaymentReferenceNo',  # noqa: E501
        'channel_customer_no': 'ChannelCustomerNo',  # noqa: E501
        'extra_data': 'ExtraData',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, billing_address, shipping_address, channel_order_no, lines, email, shipping_costs_incl_vat, currency_code, order_date, *args, **kwargs):  # noqa: E501
        """ChannelOrderRequest - a model defined in OpenAPI

        Args:
            billing_address (ChannelAddressRequest):
            shipping_address (ChannelAddressRequest):
            channel_order_no (str): The unique order reference used by the Channel.
            lines ([ChannelOrderLineRequest]): The order lines.
            email (str): The customer's email.
            shipping_costs_incl_vat (float): The shipping fee including VAT  (in the shop's base currency calculated using the exchange rate at the time of ordering).
            currency_code (str): The currency code for the amounts of the order.
            order_date (datetime): The date the order was created at the channel.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            is_business_order (bool, none_type): Optional. Is a business order (default value is false).  If not provided the VAT Number will be checked. If a VAT Number is found, IsBusinessOrder will be set to true.  No VAT will be calculated when set to true.. [optional]  # noqa: E501
            key_is_merchant_product_no (bool): Optional. Is the MPN used as key for the product (default value is false).. [optional]  # noqa: E501
            phone (str, none_type): The customer's telephone number.. [optional]  # noqa: E501
            company_registration_no (str, none_type): Optional. A company's chamber of commerce number.. [optional]  # noqa: E501
            vat_no (str, none_type): Optional. A company's VAT number.. [optional]  # noqa: E501
            payment_method (str, none_type): The payment method used on the order.. [optional]  # noqa: E501
            payment_reference_no (str, none_type): Reference or transaction id for the payment. [optional]  # noqa: E501
            channel_customer_no (str, none_type): The unique customer reference used by the channel.. [optional]  # noqa: E501
            extra_data ({str: (str,)}, none_type): Extra data on the order.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.billing_address = billing_address
        self.shipping_address = shipping_address
        self.channel_order_no = channel_order_no
        self.lines = lines
        self.email = email
        self.shipping_costs_incl_vat = shipping_costs_incl_vat
        self.currency_code = currency_code
        self.order_date = order_date
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, billing_address, shipping_address, channel_order_no, lines, email, shipping_costs_incl_vat, currency_code, order_date, *args, **kwargs):  # noqa: E501
        """ChannelOrderRequest - a model defined in OpenAPI

        Args:
            billing_address (ChannelAddressRequest):
            shipping_address (ChannelAddressRequest):
            channel_order_no (str): The unique order reference used by the Channel.
            lines ([ChannelOrderLineRequest]): The order lines.
            email (str): The customer's email.
            shipping_costs_incl_vat (float): The shipping fee including VAT  (in the shop's base currency calculated using the exchange rate at the time of ordering).
            currency_code (str): The currency code for the amounts of the order.
            order_date (datetime): The date the order was created at the channel.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            is_business_order (bool, none_type): Optional. Is a business order (default value is false).  If not provided the VAT Number will be checked. If a VAT Number is found, IsBusinessOrder will be set to true.  No VAT will be calculated when set to true.. [optional]  # noqa: E501
            key_is_merchant_product_no (bool): Optional. Is the MPN used as key for the product (default value is false).. [optional]  # noqa: E501
            phone (str, none_type): The customer's telephone number.. [optional]  # noqa: E501
            company_registration_no (str, none_type): Optional. A company's chamber of commerce number.. [optional]  # noqa: E501
            vat_no (str, none_type): Optional. A company's VAT number.. [optional]  # noqa: E501
            payment_method (str, none_type): The payment method used on the order.. [optional]  # noqa: E501
            payment_reference_no (str, none_type): Reference or transaction id for the payment. [optional]  # noqa: E501
            channel_customer_no (str, none_type): The unique customer reference used by the channel.. [optional]  # noqa: E501
            extra_data ({str: (str,)}, none_type): Extra data on the order.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.billing_address = billing_address
        self.shipping_address = shipping_address
        self.channel_order_no = channel_order_no
        self.lines = lines
        self.email = email
        self.shipping_costs_incl_vat = shipping_costs_incl_vat
        self.currency_code = currency_code
        self.order_date = order_date
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
