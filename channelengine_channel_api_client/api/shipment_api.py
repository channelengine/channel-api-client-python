"""
    ChannelEngine Channel API

    ChannelEngine API for channels  # noqa: E501

    The version of the OpenAPI document: 2.9.10
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
from channelengine_channel_api_client.model.collection_of_channel_shipment_response import CollectionOfChannelShipmentResponse


class ShipmentApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __shipment_index(
            self,
            **kwargs
        ):
            """Get Shipments.  # noqa: E501

            Gets all shipments created since the supplied date with status CLOSED.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.shipment_index(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                from_date (datetime, none_type): Filter on the creation date, starting from this date. This date is inclusive.. [optional]
                to_date (datetime, none_type): Filter on the creation date, until this date. This date is exclusive.. [optional]
                channel_order_nos ([str], none_type): Filter on the unique references (ids) as used by the channel.. [optional]
                page (int, none_type): The page to filter on. Starts at 1.. [optional]
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
                CollectionOfChannelShipmentResponse
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

        self.shipment_index = _Endpoint(
            settings={
                'response_type': (CollectionOfChannelShipmentResponse,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/shipments',
                'operation_id': 'shipment_index',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'from_date',
                    'to_date',
                    'channel_order_nos',
                    'page',
                ],
                'required': [],
                'nullable': [
                    'from_date',
                    'to_date',
                    'channel_order_nos',
                    'page',
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
                    'from_date':
                        (datetime, none_type,),
                    'to_date':
                        (datetime, none_type,),
                    'channel_order_nos':
                        ([str], none_type,),
                    'page':
                        (int, none_type,),
                },
                'attribute_map': {
                    'from_date': 'fromDate',
                    'to_date': 'toDate',
                    'channel_order_nos': 'channelOrderNos',
                    'page': 'page',
                },
                'location_map': {
                    'from_date': 'query',
                    'to_date': 'query',
                    'channel_order_nos': 'query',
                    'page': 'query',
                },
                'collection_format_map': {
                    'channel_order_nos': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__shipment_index
        )

        def __shipment_shipping_label(
            self,
            merchant_shipment_no,
            **kwargs
        ):
            """Download shipping label.  # noqa: E501

            Downloads the shipping label for the shipment. There may pass some time between creating the shipment<br />and the availability of the label. So '404 Not Found' might incidate it is not available yet.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.shipment_shipping_label(merchant_shipment_no, async_req=True)
            >>> result = thread.get()

            Args:
                merchant_shipment_no (str, none_type): The unique shipment reference as used by the merchant.

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
                file
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
            kwargs['merchant_shipment_no'] = \
                merchant_shipment_no
            return self.call_with_http_info(**kwargs)

        self.shipment_shipping_label = _Endpoint(
            settings={
                'response_type': (file,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/v2/orders/{merchantShipmentNo}/shippinglabel',
                'operation_id': 'shipment_shipping_label',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'merchant_shipment_no',
                ],
                'required': [
                    'merchant_shipment_no',
                ],
                'nullable': [
                    'merchant_shipment_no',
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
                    'merchant_shipment_no':
                        (str, none_type,),
                },
                'attribute_map': {
                    'merchant_shipment_no': 'merchantShipmentNo',
                },
                'location_map': {
                    'merchant_shipment_no': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.shippingLabel',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__shipment_shipping_label
        )
