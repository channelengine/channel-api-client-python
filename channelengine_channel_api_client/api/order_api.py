# coding: utf-8

"""
    ChannelEngine Channel API

    ChannelEngine API for channels  # noqa: E501

    OpenAPI spec version: 2.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from channelengine_channel_api_client.api_client import ApiClient


class OrderApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def order_create(self, model, **kwargs):  # noqa: E501
        """Create Order  # noqa: E501

        Create a new order in ChannelEngine.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.order_create(model, async=True)
        >>> result = thread.get()

        :param async bool
        :param ChannelOrderRequest model:  (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.order_create_with_http_info(model, **kwargs)  # noqa: E501
        else:
            (data) = self.order_create_with_http_info(model, **kwargs)  # noqa: E501
            return data

    def order_create_with_http_info(self, model, **kwargs):  # noqa: E501
        """Create Order  # noqa: E501

        Create a new order in ChannelEngine.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.order_create_with_http_info(model, async=True)
        >>> result = thread.get()

        :param async bool
        :param ChannelOrderRequest model:  (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method order_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model' is set
        if ('model' not in params or
                params['model'] is None):
            raise ValueError("Missing the required parameter `model` when calling `order_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'model' in params:
            body_params = params['model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/orders', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def order_invoice(self, merchant_order_no, **kwargs):  # noqa: E501
        """Download Invoice  # noqa: E501

        Generates the ChannelEngine VAT invoice for this order in PDF  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.order_invoice(merchant_order_no, async=True)
        >>> result = thread.get()

        :param async bool
        :param str merchant_order_no: The unique order reference as used by the merchant (required)
        :param bool use_customer_culture: Generate the invoice in the billing address' country's language
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.order_invoice_with_http_info(merchant_order_no, **kwargs)  # noqa: E501
        else:
            (data) = self.order_invoice_with_http_info(merchant_order_no, **kwargs)  # noqa: E501
            return data

    def order_invoice_with_http_info(self, merchant_order_no, **kwargs):  # noqa: E501
        """Download Invoice  # noqa: E501

        Generates the ChannelEngine VAT invoice for this order in PDF  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.order_invoice_with_http_info(merchant_order_no, async=True)
        >>> result = thread.get()

        :param async bool
        :param str merchant_order_no: The unique order reference as used by the merchant (required)
        :param bool use_customer_culture: Generate the invoice in the billing address' country's language
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['merchant_order_no', 'use_customer_culture']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method order_invoice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'merchant_order_no' is set
        if ('merchant_order_no' not in params or
                params['merchant_order_no'] is None):
            raise ValueError("Missing the required parameter `merchant_order_no` when calling `order_invoice`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'merchant_order_no' in params:
            path_params['merchantOrderNo'] = params['merchant_order_no']  # noqa: E501

        query_params = []
        if 'use_customer_culture' in params:
            query_params.append(('useCustomerCulture', params['use_customer_culture']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/pdf'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/orders/{merchantOrderNo}/invoice', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def order_packing_slip(self, merchant_order_no, **kwargs):  # noqa: E501
        """Download Packing Slip  # noqa: E501

        Generates the ChannelEngine packing slip for this order in PDF  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.order_packing_slip(merchant_order_no, async=True)
        >>> result = thread.get()

        :param async bool
        :param str merchant_order_no: The unique order reference as used by the merchant (required)
        :param bool use_customer_culture: Generate the invoice in the billing address' country's language
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.order_packing_slip_with_http_info(merchant_order_no, **kwargs)  # noqa: E501
        else:
            (data) = self.order_packing_slip_with_http_info(merchant_order_no, **kwargs)  # noqa: E501
            return data

    def order_packing_slip_with_http_info(self, merchant_order_no, **kwargs):  # noqa: E501
        """Download Packing Slip  # noqa: E501

        Generates the ChannelEngine packing slip for this order in PDF  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.order_packing_slip_with_http_info(merchant_order_no, async=True)
        >>> result = thread.get()

        :param async bool
        :param str merchant_order_no: The unique order reference as used by the merchant (required)
        :param bool use_customer_culture: Generate the invoice in the billing address' country's language
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['merchant_order_no', 'use_customer_culture']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method order_packing_slip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'merchant_order_no' is set
        if ('merchant_order_no' not in params or
                params['merchant_order_no'] is None):
            raise ValueError("Missing the required parameter `merchant_order_no` when calling `order_packing_slip`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'merchant_order_no' in params:
            path_params['merchantOrderNo'] = params['merchant_order_no']  # noqa: E501

        query_params = []
        if 'use_customer_culture' in params:
            query_params.append(('useCustomerCulture', params['use_customer_culture']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/pdf'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/orders/{merchantOrderNo}/packingslip', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)