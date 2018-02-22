# coding: utf-8

"""
    ChannelEngine Channel API

    ChannelEngine API for channels  # noqa: E501

    OpenAPI spec version: 2.5.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from channelengine_channel_api_client.api_client import ApiClient


class ProductApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def product_acknowledge_data_changes(self, changes, **kwargs):  # noqa: E501
        """Acknowledge Product Data Changes  # noqa: E501

        This endpoint should be called after a call to GET 'v2/products/data'. After a call to  this endpoint ChannelEngine 'knows' which products are known to the channel (and the last  time they have been updated) and is therefore able to only return the products  that really have changed since the last call to POST 'v2/products/data'.  The supplied ChannelReturnNo will be saved  in our database and is supposed to be unique, the 'Updated' and 'Removed'  fields consist of ChannelReferences which are sent in a previous call  within the field 'Created'.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.product_acknowledge_data_changes(changes, async=True)
        >>> result = thread.get()

        :param async bool
        :param ChannelProcessedChangesRequest changes: The merchant references of the products which have been               successfully created, updated or deleted (after a call to 'GetDataChanges') (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.product_acknowledge_data_changes_with_http_info(changes, **kwargs)  # noqa: E501
        else:
            (data) = self.product_acknowledge_data_changes_with_http_info(changes, **kwargs)  # noqa: E501
            return data

    def product_acknowledge_data_changes_with_http_info(self, changes, **kwargs):  # noqa: E501
        """Acknowledge Product Data Changes  # noqa: E501

        This endpoint should be called after a call to GET 'v2/products/data'. After a call to  this endpoint ChannelEngine 'knows' which products are known to the channel (and the last  time they have been updated) and is therefore able to only return the products  that really have changed since the last call to POST 'v2/products/data'.  The supplied ChannelReturnNo will be saved  in our database and is supposed to be unique, the 'Updated' and 'Removed'  fields consist of ChannelReferences which are sent in a previous call  within the field 'Created'.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.product_acknowledge_data_changes_with_http_info(changes, async=True)
        >>> result = thread.get()

        :param async bool
        :param ChannelProcessedChangesRequest changes: The merchant references of the products which have been               successfully created, updated or deleted (after a call to 'GetDataChanges') (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['changes']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_acknowledge_data_changes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'changes' is set
        if ('changes' not in params or
                params['changes'] is None):
            raise ValueError("Missing the required parameter `changes` when calling `product_acknowledge_data_changes`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'changes' in params:
            body_params = params['changes']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/products/data', 'POST',
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

    def product_acknowledge_offer_changes(self, changes, **kwargs):  # noqa: E501
        """Acknowledge Product Offer Changes  # noqa: E501

        After a call to GET 'v2/products/offers' this endpoint should be called with the  ChannelReturnNo of the products that are successfully updated.  Please see 'v2/products/data' and 'v2/products/data' for documentation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.product_acknowledge_offer_changes(changes, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] changes: The channel references of the updated products (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.product_acknowledge_offer_changes_with_http_info(changes, **kwargs)  # noqa: E501
        else:
            (data) = self.product_acknowledge_offer_changes_with_http_info(changes, **kwargs)  # noqa: E501
            return data

    def product_acknowledge_offer_changes_with_http_info(self, changes, **kwargs):  # noqa: E501
        """Acknowledge Product Offer Changes  # noqa: E501

        After a call to GET 'v2/products/offers' this endpoint should be called with the  ChannelReturnNo of the products that are successfully updated.  Please see 'v2/products/data' and 'v2/products/data' for documentation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.product_acknowledge_offer_changes_with_http_info(changes, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] changes: The channel references of the updated products (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['changes']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_acknowledge_offer_changes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'changes' is set
        if ('changes' not in params or
                params['changes'] is None):
            raise ValueError("Missing the required parameter `changes` when calling `product_acknowledge_offer_changes`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'changes' in params:
            body_params = params['changes']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/products/offers', 'POST',
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

    def product_get_data_changes(self, **kwargs):  # noqa: E501
        """Get Product Data Changes  # noqa: E501

        Get all products which have changes since the post http call to POST 'v2/products/data'.  The response contains the products which should be created, updated or removed from the channel.  After the products have been received and processed successfully 'v2/products/data' should  be called with the merchant references of the products which have been processed (see POST 'v2/products/data').   ChannelEnginewill save this information to make sure that the next call to GET 'v2/products/data' only returns the  products that really have changes (and therefore should be created, updated or deleted).  A channel willing to integrate with channelengine should therefore only do the following things:      1. Periodically poll 'v2/products/data' for changes.      2. If any products are returned, save, update or remove these products.      3. Send the merchant references of the products that have succesfully been processed      in step 2 to POST 'v2/products/data'.       These three simple steps will make sure that the products on the channel will be synchronized   with the products on ChannelEngine. ChannelEngine will use the API key to determine the customer  whose products should be returned. Note that child products are only returned if their parent product  has been acknowledged in a previous transaction. This way ChannelEngine knows the value of   'ChannelParentReference'.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.product_get_data_changes(async=True)
        >>> result = thread.get()

        :param async bool
        :param int max_count: Optional - limit the amount of products returned for each field              (ToBeCreated, ToBeUpdated, ToBeRemoved) to this number.
        :return: SingleOfChannelProductChangesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.product_get_data_changes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.product_get_data_changes_with_http_info(**kwargs)  # noqa: E501
            return data

    def product_get_data_changes_with_http_info(self, **kwargs):  # noqa: E501
        """Get Product Data Changes  # noqa: E501

        Get all products which have changes since the post http call to POST 'v2/products/data'.  The response contains the products which should be created, updated or removed from the channel.  After the products have been received and processed successfully 'v2/products/data' should  be called with the merchant references of the products which have been processed (see POST 'v2/products/data').   ChannelEnginewill save this information to make sure that the next call to GET 'v2/products/data' only returns the  products that really have changes (and therefore should be created, updated or deleted).  A channel willing to integrate with channelengine should therefore only do the following things:      1. Periodically poll 'v2/products/data' for changes.      2. If any products are returned, save, update or remove these products.      3. Send the merchant references of the products that have succesfully been processed      in step 2 to POST 'v2/products/data'.       These three simple steps will make sure that the products on the channel will be synchronized   with the products on ChannelEngine. ChannelEngine will use the API key to determine the customer  whose products should be returned. Note that child products are only returned if their parent product  has been acknowledged in a previous transaction. This way ChannelEngine knows the value of   'ChannelParentReference'.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.product_get_data_changes_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int max_count: Optional - limit the amount of products returned for each field              (ToBeCreated, ToBeUpdated, ToBeRemoved) to this number.
        :return: SingleOfChannelProductChangesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['max_count']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_get_data_changes" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'max_count' in params:
            query_params.append(('maxCount', params['max_count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/products/data', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SingleOfChannelProductChangesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def product_get_offer_changes(self, **kwargs):  # noqa: E501
        """Get Product Offer Changes  # noqa: E501

        GET 'v2/products/offers' and POST 'v2/products/offers' closely resemble GET 'v2/products/data' and POST 'v2/products/data'. See the 'v2/products/data'  endpoints for documentation. The difference between both endpoints is that 'v2/products/offers' only returns Price and Stock updates and can (and should)  therefore be called more often to keep this information (which might change frequently) up to date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.product_get_offer_changes(async=True)
        >>> result = thread.get()

        :param async bool
        :return: CollectionOfChannelOfferResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.product_get_offer_changes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.product_get_offer_changes_with_http_info(**kwargs)  # noqa: E501
            return data

    def product_get_offer_changes_with_http_info(self, **kwargs):  # noqa: E501
        """Get Product Offer Changes  # noqa: E501

        GET 'v2/products/offers' and POST 'v2/products/offers' closely resemble GET 'v2/products/data' and POST 'v2/products/data'. See the 'v2/products/data'  endpoints for documentation. The difference between both endpoints is that 'v2/products/offers' only returns Price and Stock updates and can (and should)  therefore be called more often to keep this information (which might change frequently) up to date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.product_get_offer_changes_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: CollectionOfChannelOfferResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_get_offer_changes" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/products/offers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionOfChannelOfferResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
