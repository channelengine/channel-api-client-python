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

from channelengine_channel_api_client.models.extra_data_item import ExtraDataItem  # noqa: F401,E501


class ChannelProductResponse(object):
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
        'id': 'int',
        'parent_channel_product_no': 'str',
        'mapped_fields': 'dict(str, str)',
        'name': 'str',
        'description': 'str',
        'brand': 'str',
        'size': 'str',
        'color': 'str',
        'ean': 'str',
        'manufacturer_product_number': 'str',
        'stock': 'int',
        'price': 'float',
        'msrp': 'float',
        'purchase_price': 'float',
        'vat_rate_type': 'str',
        'shipping_cost': 'float',
        'shipping_time': 'str',
        'url': 'str',
        'image_url': 'str',
        'extra_image_url1': 'str',
        'extra_image_url2': 'str',
        'extra_image_url3': 'str',
        'extra_image_url4': 'str',
        'extra_image_url5': 'str',
        'extra_image_url6': 'str',
        'extra_image_url7': 'str',
        'extra_image_url8': 'str',
        'extra_image_url9': 'str',
        'category_trail': 'str',
        'extra_data': 'list[ExtraDataItem]'
    }

    attribute_map = {
        'id': 'Id',
        'parent_channel_product_no': 'ParentChannelProductNo',
        'mapped_fields': 'MappedFields',
        'name': 'Name',
        'description': 'Description',
        'brand': 'Brand',
        'size': 'Size',
        'color': 'Color',
        'ean': 'Ean',
        'manufacturer_product_number': 'ManufacturerProductNumber',
        'stock': 'Stock',
        'price': 'Price',
        'msrp': 'MSRP',
        'purchase_price': 'PurchasePrice',
        'vat_rate_type': 'VatRateType',
        'shipping_cost': 'ShippingCost',
        'shipping_time': 'ShippingTime',
        'url': 'Url',
        'image_url': 'ImageUrl',
        'extra_image_url1': 'ExtraImageUrl1',
        'extra_image_url2': 'ExtraImageUrl2',
        'extra_image_url3': 'ExtraImageUrl3',
        'extra_image_url4': 'ExtraImageUrl4',
        'extra_image_url5': 'ExtraImageUrl5',
        'extra_image_url6': 'ExtraImageUrl6',
        'extra_image_url7': 'ExtraImageUrl7',
        'extra_image_url8': 'ExtraImageUrl8',
        'extra_image_url9': 'ExtraImageUrl9',
        'category_trail': 'CategoryTrail',
        'extra_data': 'ExtraData'
    }

    def __init__(self, id=None, parent_channel_product_no=None, mapped_fields=None, name=None, description=None, brand=None, size=None, color=None, ean=None, manufacturer_product_number=None, stock=None, price=None, msrp=None, purchase_price=None, vat_rate_type=None, shipping_cost=None, shipping_time=None, url=None, image_url=None, extra_image_url1=None, extra_image_url2=None, extra_image_url3=None, extra_image_url4=None, extra_image_url5=None, extra_image_url6=None, extra_image_url7=None, extra_image_url8=None, extra_image_url9=None, category_trail=None, extra_data=None):  # noqa: E501
        """ChannelProductResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._parent_channel_product_no = None
        self._mapped_fields = None
        self._name = None
        self._description = None
        self._brand = None
        self._size = None
        self._color = None
        self._ean = None
        self._manufacturer_product_number = None
        self._stock = None
        self._price = None
        self._msrp = None
        self._purchase_price = None
        self._vat_rate_type = None
        self._shipping_cost = None
        self._shipping_time = None
        self._url = None
        self._image_url = None
        self._extra_image_url1 = None
        self._extra_image_url2 = None
        self._extra_image_url3 = None
        self._extra_image_url4 = None
        self._extra_image_url5 = None
        self._extra_image_url6 = None
        self._extra_image_url7 = None
        self._extra_image_url8 = None
        self._extra_image_url9 = None
        self._category_trail = None
        self._extra_data = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if parent_channel_product_no is not None:
            self.parent_channel_product_no = parent_channel_product_no
        if mapped_fields is not None:
            self.mapped_fields = mapped_fields
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if brand is not None:
            self.brand = brand
        if size is not None:
            self.size = size
        if color is not None:
            self.color = color
        if ean is not None:
            self.ean = ean
        if manufacturer_product_number is not None:
            self.manufacturer_product_number = manufacturer_product_number
        if stock is not None:
            self.stock = stock
        if price is not None:
            self.price = price
        if msrp is not None:
            self.msrp = msrp
        if purchase_price is not None:
            self.purchase_price = purchase_price
        if vat_rate_type is not None:
            self.vat_rate_type = vat_rate_type
        if shipping_cost is not None:
            self.shipping_cost = shipping_cost
        if shipping_time is not None:
            self.shipping_time = shipping_time
        if url is not None:
            self.url = url
        if image_url is not None:
            self.image_url = image_url
        if extra_image_url1 is not None:
            self.extra_image_url1 = extra_image_url1
        if extra_image_url2 is not None:
            self.extra_image_url2 = extra_image_url2
        if extra_image_url3 is not None:
            self.extra_image_url3 = extra_image_url3
        if extra_image_url4 is not None:
            self.extra_image_url4 = extra_image_url4
        if extra_image_url5 is not None:
            self.extra_image_url5 = extra_image_url5
        if extra_image_url6 is not None:
            self.extra_image_url6 = extra_image_url6
        if extra_image_url7 is not None:
            self.extra_image_url7 = extra_image_url7
        if extra_image_url8 is not None:
            self.extra_image_url8 = extra_image_url8
        if extra_image_url9 is not None:
            self.extra_image_url9 = extra_image_url9
        if category_trail is not None:
            self.category_trail = category_trail
        if extra_data is not None:
            self.extra_data = extra_data

    @property
    def id(self):
        """Gets the id of this ChannelProductResponse.  # noqa: E501

        An unique identifier which ChannelEngine uses to identify the product.  Needed in the call 'POST /v2/products/data'  # noqa: E501

        :return: The id of this ChannelProductResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChannelProductResponse.

        An unique identifier which ChannelEngine uses to identify the product.  Needed in the call 'POST /v2/products/data'  # noqa: E501

        :param id: The id of this ChannelProductResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def parent_channel_product_no(self):
        """Gets the parent_channel_product_no of this ChannelProductResponse.  # noqa: E501


        :return: The parent_channel_product_no of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._parent_channel_product_no

    @parent_channel_product_no.setter
    def parent_channel_product_no(self, parent_channel_product_no):
        """Sets the parent_channel_product_no of this ChannelProductResponse.


        :param parent_channel_product_no: The parent_channel_product_no of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._parent_channel_product_no = parent_channel_product_no

    @property
    def mapped_fields(self):
        """Gets the mapped_fields of this ChannelProductResponse.  # noqa: E501

        A channel can require certain fields to be available. The channel  can provide ChannelEngine with this fields after which the merchants  will be able to fill in this field using custom conditions in ChannelEngine.  # noqa: E501

        :return: The mapped_fields of this ChannelProductResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._mapped_fields

    @mapped_fields.setter
    def mapped_fields(self, mapped_fields):
        """Sets the mapped_fields of this ChannelProductResponse.

        A channel can require certain fields to be available. The channel  can provide ChannelEngine with this fields after which the merchants  will be able to fill in this field using custom conditions in ChannelEngine.  # noqa: E501

        :param mapped_fields: The mapped_fields of this ChannelProductResponse.  # noqa: E501
        :type: dict(str, str)
        """

        self._mapped_fields = mapped_fields

    @property
    def name(self):
        """Gets the name of this ChannelProductResponse.  # noqa: E501


        :return: The name of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChannelProductResponse.


        :param name: The name of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ChannelProductResponse.  # noqa: E501


        :return: The description of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChannelProductResponse.


        :param description: The description of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def brand(self):
        """Gets the brand of this ChannelProductResponse.  # noqa: E501


        :return: The brand of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this ChannelProductResponse.


        :param brand: The brand of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def size(self):
        """Gets the size of this ChannelProductResponse.  # noqa: E501


        :return: The size of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ChannelProductResponse.


        :param size: The size of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def color(self):
        """Gets the color of this ChannelProductResponse.  # noqa: E501


        :return: The color of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ChannelProductResponse.


        :param color: The color of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def ean(self):
        """Gets the ean of this ChannelProductResponse.  # noqa: E501


        :return: The ean of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._ean

    @ean.setter
    def ean(self, ean):
        """Sets the ean of this ChannelProductResponse.


        :param ean: The ean of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._ean = ean

    @property
    def manufacturer_product_number(self):
        """Gets the manufacturer_product_number of this ChannelProductResponse.  # noqa: E501


        :return: The manufacturer_product_number of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_product_number

    @manufacturer_product_number.setter
    def manufacturer_product_number(self, manufacturer_product_number):
        """Sets the manufacturer_product_number of this ChannelProductResponse.


        :param manufacturer_product_number: The manufacturer_product_number of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._manufacturer_product_number = manufacturer_product_number

    @property
    def stock(self):
        """Gets the stock of this ChannelProductResponse.  # noqa: E501


        :return: The stock of this ChannelProductResponse.  # noqa: E501
        :rtype: int
        """
        return self._stock

    @stock.setter
    def stock(self, stock):
        """Sets the stock of this ChannelProductResponse.


        :param stock: The stock of this ChannelProductResponse.  # noqa: E501
        :type: int
        """

        self._stock = stock

    @property
    def price(self):
        """Gets the price of this ChannelProductResponse.  # noqa: E501

        Price, including VAT.  # noqa: E501

        :return: The price of this ChannelProductResponse.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ChannelProductResponse.

        Price, including VAT.  # noqa: E501

        :param price: The price of this ChannelProductResponse.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def msrp(self):
        """Gets the msrp of this ChannelProductResponse.  # noqa: E501

        Manufacturer's suggested retail price  # noqa: E501

        :return: The msrp of this ChannelProductResponse.  # noqa: E501
        :rtype: float
        """
        return self._msrp

    @msrp.setter
    def msrp(self, msrp):
        """Sets the msrp of this ChannelProductResponse.

        Manufacturer's suggested retail price  # noqa: E501

        :param msrp: The msrp of this ChannelProductResponse.  # noqa: E501
        :type: float
        """

        self._msrp = msrp

    @property
    def purchase_price(self):
        """Gets the purchase_price of this ChannelProductResponse.  # noqa: E501


        :return: The purchase_price of this ChannelProductResponse.  # noqa: E501
        :rtype: float
        """
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, purchase_price):
        """Sets the purchase_price of this ChannelProductResponse.


        :param purchase_price: The purchase_price of this ChannelProductResponse.  # noqa: E501
        :type: float
        """

        self._purchase_price = purchase_price

    @property
    def vat_rate_type(self):
        """Gets the vat_rate_type of this ChannelProductResponse.  # noqa: E501

        The type of VAT which applies to this product.  See: http://ec.europa.eu/taxation_customs/taxation/vat/topics/rates_en.htm  # noqa: E501

        :return: The vat_rate_type of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._vat_rate_type

    @vat_rate_type.setter
    def vat_rate_type(self, vat_rate_type):
        """Sets the vat_rate_type of this ChannelProductResponse.

        The type of VAT which applies to this product.  See: http://ec.europa.eu/taxation_customs/taxation/vat/topics/rates_en.htm  # noqa: E501

        :param vat_rate_type: The vat_rate_type of this ChannelProductResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["STANDARD", "REDUCED", "SUPER_REDUCED"]  # noqa: E501
        if vat_rate_type not in allowed_values:
            raise ValueError(
                "Invalid value for `vat_rate_type` ({0}), must be one of {1}"  # noqa: E501
                .format(vat_rate_type, allowed_values)
            )

        self._vat_rate_type = vat_rate_type

    @property
    def shipping_cost(self):
        """Gets the shipping_cost of this ChannelProductResponse.  # noqa: E501


        :return: The shipping_cost of this ChannelProductResponse.  # noqa: E501
        :rtype: float
        """
        return self._shipping_cost

    @shipping_cost.setter
    def shipping_cost(self, shipping_cost):
        """Sets the shipping_cost of this ChannelProductResponse.


        :param shipping_cost: The shipping_cost of this ChannelProductResponse.  # noqa: E501
        :type: float
        """

        self._shipping_cost = shipping_cost

    @property
    def shipping_time(self):
        """Gets the shipping_time of this ChannelProductResponse.  # noqa: E501

        A textual representation of the shippingtime.  For example, in Dutch: 'Op werkdagen voor 22:00 uur besteld, morgen in huis'  # noqa: E501

        :return: The shipping_time of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._shipping_time

    @shipping_time.setter
    def shipping_time(self, shipping_time):
        """Sets the shipping_time of this ChannelProductResponse.

        A textual representation of the shippingtime.  For example, in Dutch: 'Op werkdagen voor 22:00 uur besteld, morgen in huis'  # noqa: E501

        :param shipping_time: The shipping_time of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._shipping_time = shipping_time

    @property
    def url(self):
        """Gets the url of this ChannelProductResponse.  # noqa: E501

        A URL pointing to the merchant's webpage  which displays this product.  # noqa: E501

        :return: The url of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ChannelProductResponse.

        A URL pointing to the merchant's webpage  which displays this product.  # noqa: E501

        :param url: The url of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def image_url(self):
        """Gets the image_url of this ChannelProductResponse.  # noqa: E501

        A URL at which an image of this product  can be found.  # noqa: E501

        :return: The image_url of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this ChannelProductResponse.

        A URL at which an image of this product  can be found.  # noqa: E501

        :param image_url: The image_url of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def extra_image_url1(self):
        """Gets the extra_image_url1 of this ChannelProductResponse.  # noqa: E501


        :return: The extra_image_url1 of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._extra_image_url1

    @extra_image_url1.setter
    def extra_image_url1(self, extra_image_url1):
        """Sets the extra_image_url1 of this ChannelProductResponse.


        :param extra_image_url1: The extra_image_url1 of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._extra_image_url1 = extra_image_url1

    @property
    def extra_image_url2(self):
        """Gets the extra_image_url2 of this ChannelProductResponse.  # noqa: E501


        :return: The extra_image_url2 of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._extra_image_url2

    @extra_image_url2.setter
    def extra_image_url2(self, extra_image_url2):
        """Sets the extra_image_url2 of this ChannelProductResponse.


        :param extra_image_url2: The extra_image_url2 of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._extra_image_url2 = extra_image_url2

    @property
    def extra_image_url3(self):
        """Gets the extra_image_url3 of this ChannelProductResponse.  # noqa: E501


        :return: The extra_image_url3 of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._extra_image_url3

    @extra_image_url3.setter
    def extra_image_url3(self, extra_image_url3):
        """Sets the extra_image_url3 of this ChannelProductResponse.


        :param extra_image_url3: The extra_image_url3 of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._extra_image_url3 = extra_image_url3

    @property
    def extra_image_url4(self):
        """Gets the extra_image_url4 of this ChannelProductResponse.  # noqa: E501


        :return: The extra_image_url4 of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._extra_image_url4

    @extra_image_url4.setter
    def extra_image_url4(self, extra_image_url4):
        """Sets the extra_image_url4 of this ChannelProductResponse.


        :param extra_image_url4: The extra_image_url4 of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._extra_image_url4 = extra_image_url4

    @property
    def extra_image_url5(self):
        """Gets the extra_image_url5 of this ChannelProductResponse.  # noqa: E501


        :return: The extra_image_url5 of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._extra_image_url5

    @extra_image_url5.setter
    def extra_image_url5(self, extra_image_url5):
        """Sets the extra_image_url5 of this ChannelProductResponse.


        :param extra_image_url5: The extra_image_url5 of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._extra_image_url5 = extra_image_url5

    @property
    def extra_image_url6(self):
        """Gets the extra_image_url6 of this ChannelProductResponse.  # noqa: E501


        :return: The extra_image_url6 of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._extra_image_url6

    @extra_image_url6.setter
    def extra_image_url6(self, extra_image_url6):
        """Sets the extra_image_url6 of this ChannelProductResponse.


        :param extra_image_url6: The extra_image_url6 of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._extra_image_url6 = extra_image_url6

    @property
    def extra_image_url7(self):
        """Gets the extra_image_url7 of this ChannelProductResponse.  # noqa: E501


        :return: The extra_image_url7 of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._extra_image_url7

    @extra_image_url7.setter
    def extra_image_url7(self, extra_image_url7):
        """Sets the extra_image_url7 of this ChannelProductResponse.


        :param extra_image_url7: The extra_image_url7 of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._extra_image_url7 = extra_image_url7

    @property
    def extra_image_url8(self):
        """Gets the extra_image_url8 of this ChannelProductResponse.  # noqa: E501


        :return: The extra_image_url8 of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._extra_image_url8

    @extra_image_url8.setter
    def extra_image_url8(self, extra_image_url8):
        """Sets the extra_image_url8 of this ChannelProductResponse.


        :param extra_image_url8: The extra_image_url8 of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._extra_image_url8 = extra_image_url8

    @property
    def extra_image_url9(self):
        """Gets the extra_image_url9 of this ChannelProductResponse.  # noqa: E501


        :return: The extra_image_url9 of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._extra_image_url9

    @extra_image_url9.setter
    def extra_image_url9(self, extra_image_url9):
        """Sets the extra_image_url9 of this ChannelProductResponse.


        :param extra_image_url9: The extra_image_url9 of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._extra_image_url9 = extra_image_url9

    @property
    def category_trail(self):
        """Gets the category_trail of this ChannelProductResponse.  # noqa: E501

        The category to which this product belongs.  Please supply this field in the following format:  'maincategory &gt; category &gt; subcategory'  For example:  'vehicles &gt; bikes &gt; mountainbike'  # noqa: E501

        :return: The category_trail of this ChannelProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._category_trail

    @category_trail.setter
    def category_trail(self, category_trail):
        """Sets the category_trail of this ChannelProductResponse.

        The category to which this product belongs.  Please supply this field in the following format:  'maincategory &gt; category &gt; subcategory'  For example:  'vehicles &gt; bikes &gt; mountainbike'  # noqa: E501

        :param category_trail: The category_trail of this ChannelProductResponse.  # noqa: E501
        :type: str
        """

        self._category_trail = category_trail

    @property
    def extra_data(self):
        """Gets the extra_data of this ChannelProductResponse.  # noqa: E501

        An optional list of key-value pairs containing  extra data about this product. This data can be  sent to channels or used for filtering products.  # noqa: E501

        :return: The extra_data of this ChannelProductResponse.  # noqa: E501
        :rtype: list[ExtraDataItem]
        """
        return self._extra_data

    @extra_data.setter
    def extra_data(self, extra_data):
        """Sets the extra_data of this ChannelProductResponse.

        An optional list of key-value pairs containing  extra data about this product. This data can be  sent to channels or used for filtering products.  # noqa: E501

        :param extra_data: The extra_data of this ChannelProductResponse.  # noqa: E501
        :type: list[ExtraDataItem]
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
        if not isinstance(other, ChannelProductResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
