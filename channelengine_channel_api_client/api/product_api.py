"""
    ChannelEngine Channel API

    ChannelEngine API for channels  # noqa: E501

    The version of the OpenAPI document: 2.9.12
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from channelengine_channel_api_client.api_client import ApiClient, Endpoint as _Endpoint
from channelengine_channel_api_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from channelengine_channel_api_client.model.api_response import ApiResponse
from channelengine_channel_api_client.model.channel_processed_changes_request import ChannelProcessedChangesRequest
from channelengine_channel_api_client.model.collection_of_channel_offer_response import CollectionOfChannelOfferResponse
from channelengine_channel_api_client.model.data_changes_product_type import DataChangesProductType
from channelengine_channel_api_client.model.single_of_channel_product_changes_response import SingleOfChannelProductChangesResponse


class ProductApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __product_acknowledge_data_changes(
            self,
            **kwargs
        ):
            """Acknowledge Product Data Changes.  # noqa: E501

            This endpoint should be called after a call to GET 'v2/products/data'. After a call to<br />this endpoint ChannelEngine 'knows' which products are known to the channel (and the last<br />time they have been updated) and is therefore able to only return the products<br />that really have changed since the last call to POST 'v2/products/data'.<br />The supplied ChannelReturnNo will be saved<br />in our database and is supposed to be unique, the 'Updated' and 'Removed'<br />fields consist of ChannelReferences which are sent in a previous call<br />within the field 'Created'.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.product_acknowledge_data_changes(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                channel_processed_changes_request (ChannelProcessedChangesRequest): The merchant references of the products which have been<br /> successfully created, updated or deleted (after a call to 'GetDataChanges').. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ApiResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.product_acknowledge_data_changes = _Endpoint(
            settings={
                'response_type': (ApiResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/products/data',
                'operation_id': 'product_acknowledge_data_changes',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'channel_processed_changes_request',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'channel_processed_changes_request':
                        (ChannelProcessedChangesRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'channel_processed_changes_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__product_acknowledge_data_changes
        )

        def __product_acknowledge_offer_changes(
            self,
            **kwargs
        ):
            """Acknowledge Product Offer Changes.  # noqa: E501

            After a call to GET 'v2/products/offers' this endpoint should be called with the<br />ChannelProductNo of the products that are successfully updated.<br />Please see 'v2/products/data' and 'v2/products/data' for documentation.<br />In advanced cases, the MerchantProductNo is used for this.<br />In that case, bool keyIsMpn should be true.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.product_acknowledge_offer_changes(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                key_is_mpn (bool): If set to true, changes has to be a list of merchant references instead of channel references.. [optional] if omitted the server will use the default value of False
                request_body ([str]): The channel references of the updated products.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ApiResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.product_acknowledge_offer_changes = _Endpoint(
            settings={
                'response_type': (ApiResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/products/offers',
                'operation_id': 'product_acknowledge_offer_changes',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'key_is_mpn',
                    'request_body',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'key_is_mpn':
                        (bool,),
                    'request_body':
                        ([str],),
                },
                'attribute_map': {
                    'key_is_mpn': 'keyIsMpn',
                },
                'location_map': {
                    'key_is_mpn': 'query',
                    'request_body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__product_acknowledge_offer_changes
        )

        def __product_get_data_changes(
            self,
            **kwargs
        ):
            """Get Product Data Changes.  # noqa: E501

            Get all products which have changes since the post http call to POST 'v2/products/data'.<br />The response contains the products which should be created, updated or removed from the channel.<br />After the products have been received and processed successfully 'v2/products/data' should<br />be called with the merchant references of the products which have been processed (see POST 'v2/products/data').<br />ChannelEngine will save this information to make sure that the next call to GET 'v2/products/data' only returns the<br />products that really have changes (and therefore should be created, updated or deleted).<br />A channel willing to integrate with channelengine should therefore only do the following things:<br /> 1. Periodically poll 'v2/products/data' for changes.<br /> 2. If any products are returned, save, update or remove these products.<br /> 3. Send the merchant references of the products that have succesfully been processed<br /> in step 2 to POST 'v2/products/data'.<br /> <br />These three simple steps will make sure that the products on the channel will be synchronized<br />with the products on ChannelEngine. ChannelEngine will use the API key to determine the customer<br />whose products should be returned. Note that child products are only returned if their parent product<br />has been acknowledged in a previous transaction. This way ChannelEngine knows the value of<br />'ChannelParentReference'.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.product_get_data_changes(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                max_count (int): Optional - limit the amount of products returned for each field<br /> (ToBeCreated, ToBeUpdated, ToBeRemoved) to this number.. [optional]
                strip_html (bool): Optional - strips html by default on all fields. [optional] if omitted the server will use the default value of True
                page (int): [optional]
                page_size (int): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                SingleOfChannelProductChangesResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.product_get_data_changes = _Endpoint(
            settings={
                'response_type': (SingleOfChannelProductChangesResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/products/data',
                'operation_id': 'product_get_data_changes',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'max_count',
                    'strip_html',
                    'page',
                    'page_size',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'max_count':
                        (int,),
                    'strip_html':
                        (bool,),
                    'page':
                        (int,),
                    'page_size':
                        (int,),
                },
                'attribute_map': {
                    'max_count': 'maxCount',
                    'strip_html': 'stripHtml',
                    'page': 'page',
                    'page_size': 'pageSize',
                },
                'location_map': {
                    'max_count': 'query',
                    'strip_html': 'query',
                    'page': 'query',
                    'page_size': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__product_get_data_changes
        )

        def __product_get_data_changes_full(
            self,
            **kwargs
        ):
            """Get Product Data Changes with an optional product type filter. If you select product type products will be filtered by it.  If you won't pass product type you will get products with types: CHILD, PARENT, GRANDPARENT, SINGLE  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.product_get_data_changes_full(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                product_type (DataChangesProductType): Optional - Type of products. [optional]
                max_count (int): Optional - limit the amount of products returned for each field<br /> (ToBeCreated, ToBeUpdated, ToBeRemoved) to this number.. [optional]
                strip_html (bool): Optional - strips html by default on all fields. [optional] if omitted the server will use the default value of True
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                SingleOfChannelProductChangesResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.product_get_data_changes_full = _Endpoint(
            settings={
                'response_type': (SingleOfChannelProductChangesResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/products/data/full',
                'operation_id': 'product_get_data_changes_full',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'product_type',
                    'max_count',
                    'strip_html',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'product_type':
                        (DataChangesProductType,),
                    'max_count':
                        (int,),
                    'strip_html':
                        (bool,),
                },
                'attribute_map': {
                    'product_type': 'productType',
                    'max_count': 'maxCount',
                    'strip_html': 'stripHtml',
                },
                'location_map': {
                    'product_type': 'query',
                    'max_count': 'query',
                    'strip_html': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__product_get_data_changes_full
        )

        def __product_get_offer_changes(
            self,
            **kwargs
        ):
            """Get Product Offer Changes.  # noqa: E501

            GET 'v2/products/offers' and POST 'v2/products/offers' closely resemble GET 'v2/products/data' and POST 'v2/products/data'. See the 'v2/products/data'<br />endpoints for documentation. The difference between both endpoints is that 'v2/products/offers' only returns Price and Stock updates and can (and should)<br />therefore be called more often to keep this information (which might change frequently) up to date.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.product_get_offer_changes(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CollectionOfChannelOfferResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.product_get_offer_changes = _Endpoint(
            settings={
                'response_type': (CollectionOfChannelOfferResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/products/offers',
                'operation_id': 'product_get_offer_changes',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__product_get_offer_changes
        )
