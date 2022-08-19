"""
    ChannelEngine Channel API

    ChannelEngine API for channels  # noqa: E501

    The version of the OpenAPI document: 2.11.0
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
    from channelengine_channel_api_client.model.channel_order_line_response import ChannelOrderLineResponse
    from channelengine_channel_api_client.model.shipment_line_status import ShipmentLineStatus
    globals()['ChannelOrderLineResponse'] = ChannelOrderLineResponse
    globals()['ShipmentLineStatus'] = ShipmentLineStatus


class ChannelReturnLineResponse(ModelNormal):
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
        ('quantity',): {
            'inclusive_minimum': 0,
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
            'channel_product_no': (str,),  # noqa: E501
            'quantity': (int,),  # noqa: E501
            'merchant_product_no': (str, none_type,),  # noqa: E501
            'accepted_quantity': (int, none_type,),  # noqa: E501
            'rejected_quantity': (int, none_type,),  # noqa: E501
            'order_line': (ChannelOrderLineResponse,),  # noqa: E501
            'shipment_status': (ShipmentLineStatus,),  # noqa: E501
            'extra_data': ({str: (str,)}, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'channel_product_no': 'ChannelProductNo',  # noqa: E501
        'quantity': 'Quantity',  # noqa: E501
        'merchant_product_no': 'MerchantProductNo',  # noqa: E501
        'accepted_quantity': 'AcceptedQuantity',  # noqa: E501
        'rejected_quantity': 'RejectedQuantity',  # noqa: E501
        'order_line': 'OrderLine',  # noqa: E501
        'shipment_status': 'ShipmentStatus',  # noqa: E501
        'extra_data': 'ExtraData',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, channel_product_no, quantity, *args, **kwargs):  # noqa: E501
        """ChannelReturnLineResponse - a model defined in OpenAPI

        Args:
            channel_product_no (str): The unique product reference used by the Channel.
            quantity (int): Number of items of the product in this return.

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
            merchant_product_no (str, none_type): The unique product reference used by the Merchant.. [optional]  # noqa: E501
            accepted_quantity (int, none_type): The number of accepted items of the product in this return (should normally be refunded).. [optional]  # noqa: E501
            rejected_quantity (int, none_type): The number of rejected items of the product in this return (should normally not be refunded).. [optional]  # noqa: E501
            order_line (ChannelOrderLineResponse): [optional]  # noqa: E501
            shipment_status (ShipmentLineStatus): [optional]  # noqa: E501
            extra_data ({str: (str,)}, none_type): Extra data on the returnline. Each item must have an unqiue key. [optional]  # noqa: E501
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

        self.channel_product_no = channel_product_no
        self.quantity = quantity
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
    def __init__(self, channel_product_no, quantity, *args, **kwargs):  # noqa: E501
        """ChannelReturnLineResponse - a model defined in OpenAPI

        Args:
            channel_product_no (str): The unique product reference used by the Channel.
            quantity (int): Number of items of the product in this return.

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
            merchant_product_no (str, none_type): The unique product reference used by the Merchant.. [optional]  # noqa: E501
            accepted_quantity (int, none_type): The number of accepted items of the product in this return (should normally be refunded).. [optional]  # noqa: E501
            rejected_quantity (int, none_type): The number of rejected items of the product in this return (should normally not be refunded).. [optional]  # noqa: E501
            order_line (ChannelOrderLineResponse): [optional]  # noqa: E501
            shipment_status (ShipmentLineStatus): [optional]  # noqa: E501
            extra_data ({str: (str,)}, none_type): Extra data on the returnline. Each item must have an unqiue key. [optional]  # noqa: E501
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

        self.channel_product_no = channel_product_no
        self.quantity = quantity
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
