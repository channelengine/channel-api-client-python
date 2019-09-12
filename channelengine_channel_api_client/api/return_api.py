# coding: utf-8

"""
    ChannelEngine Channel API

    ChannelEngine API for channels  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from channelengine_channel_api_client.api_client import ApiClient


class ReturnApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def return_declare_for_channel(self, model, **kwargs):  # noqa: E501
        """Create Return  # noqa: E501

        Mark (part of) an order as returned by the customer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.return_declare_for_channel(model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChannelReturnRequest model:  (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.return_declare_for_channel_with_http_info(model, **kwargs)  # noqa: E501
        else:
            (data) = self.return_declare_for_channel_with_http_info(model, **kwargs)  # noqa: E501
            return data

    def return_declare_for_channel_with_http_info(self, model, **kwargs):  # noqa: E501
        """Create Return  # noqa: E501

        Mark (part of) an order as returned by the customer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.return_declare_for_channel_with_http_info(model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChannelReturnRequest model:  (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method return_declare_for_channel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model' is set
        if ('model' not in params or
                params['model'] is None):
            raise ValueError("Missing the required parameter `model` when calling `return_declare_for_channel`")  # noqa: E501

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
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/returns/channel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def return_get_declared_by_merchant(self, **kwargs):  # noqa: E501
        """Get Returns  # noqa: E501

        Get all returns created by the merchant. This call is supposed  to be used by channels. Merchants should use the 'GET /v2/returns/merchant'  call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.return_get_declared_by_merchant(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime created_since: Deprecated, please use FromDate instead.
        :param list[str] statuses: Return status(es) to filter on
        :param list[str] reasons: Return reason(s) to filter on
        :param datetime from_date: Filter on the creation date, starting from this date. This date is inclusive.
        :param datetime to_date: Filter on the creation date, until this date. This date is exclusive.
        :param int page: The page to filter on. Starts at 1.
        :return: CollectionOfChannelReturnResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.return_get_declared_by_merchant_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.return_get_declared_by_merchant_with_http_info(**kwargs)  # noqa: E501
            return data

    def return_get_declared_by_merchant_with_http_info(self, **kwargs):  # noqa: E501
        """Get Returns  # noqa: E501

        Get all returns created by the merchant. This call is supposed  to be used by channels. Merchants should use the 'GET /v2/returns/merchant'  call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.return_get_declared_by_merchant_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime created_since: Deprecated, please use FromDate instead.
        :param list[str] statuses: Return status(es) to filter on
        :param list[str] reasons: Return reason(s) to filter on
        :param datetime from_date: Filter on the creation date, starting from this date. This date is inclusive.
        :param datetime to_date: Filter on the creation date, until this date. This date is exclusive.
        :param int page: The page to filter on. Starts at 1.
        :return: CollectionOfChannelReturnResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['created_since', 'statuses', 'reasons', 'from_date', 'to_date', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method return_get_declared_by_merchant" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'created_since' in params:
            query_params.append(('createdSince', params['created_since']))  # noqa: E501
        if 'statuses' in params:
            query_params.append(('statuses', params['statuses']))  # noqa: E501
            collection_formats['statuses'] = 'multi'  # noqa: E501
        if 'reasons' in params:
            query_params.append(('reasons', params['reasons']))  # noqa: E501
            collection_formats['reasons'] = 'multi'  # noqa: E501
        if 'from_date' in params:
            query_params.append(('fromDate', params['from_date']))  # noqa: E501
        if 'to_date' in params:
            query_params.append(('toDate', params['to_date']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/returns/channel', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionOfChannelReturnResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
