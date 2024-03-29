"""
    Tenant API

    Tenant API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from graalsystems.api_client import ApiClient, Endpoint as _Endpoint
from graalsystems.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from graalsystems.model.enrollment import Enrollment
from graalsystems.model.enrollment_page import EnrollmentPage
from graalsystems.model.error import Error


class EnrollmentApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_enrollment_endpoint = _Endpoint(
            settings={
                'response_type': (Enrollment,),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/enrollments',
                'operation_id': 'create_enrollment',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'enrollment',
                ],
                'required': [
                    'x_tenant',
                    'enrollment',
                ],
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
                    'x_tenant':
                        (str,),
                    'enrollment':
                        (Enrollment,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'enrollment': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.enrollment+json'
                ],
                'content_type': [
                    'application/vnd.graal.systems.v1.enrollment+json'
                ]
            },
            api_client=api_client
        )
        self.delete_enrollment_by_id_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/enrollments/{enrollmentId}',
                'operation_id': 'delete_enrollment_by_id',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'enrollment_id',
                ],
                'required': [
                    'x_tenant',
                    'enrollment_id',
                ],
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
                    'x_tenant':
                        (str,),
                    'enrollment_id':
                        (str,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'enrollment_id': 'enrollmentId',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'enrollment_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.error+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.find_enrollment_by_enrollment_id_endpoint = _Endpoint(
            settings={
                'response_type': (Enrollment,),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/enrollments/{enrollmentId}',
                'operation_id': 'find_enrollment_by_enrollment_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'enrollment_id',
                ],
                'required': [
                    'x_tenant',
                    'enrollment_id',
                ],
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
                    'x_tenant':
                        (str,),
                    'enrollment_id':
                        (str,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'enrollment_id': 'enrollmentId',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'enrollment_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.enrollment+json',
                    'application/vnd.graal.systems.v1.error+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.find_enrollments_endpoint = _Endpoint(
            settings={
                'response_type': (EnrollmentPage,),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/enrollments',
                'operation_id': 'find_enrollments',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'page',
                    'size',
                ],
                'required': [
                    'x_tenant',
                ],
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
                    'x_tenant':
                        (str,),
                    'page':
                        (int,),
                    'size':
                        (int,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'page': 'page',
                    'size': 'size',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'page': 'query',
                    'size': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.enrollment+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def create_enrollment(
        self,
        x_tenant,
        enrollment,
        **kwargs
    ):
        """Create enrollment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_enrollment(x_tenant, enrollment, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            enrollment (Enrollment): The enrollment to be created

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Enrollment
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_tenant'] = \
            x_tenant
        kwargs['enrollment'] = \
            enrollment
        return self.create_enrollment_endpoint.call_with_http_info(**kwargs)

    def delete_enrollment_by_id(
        self,
        x_tenant,
        enrollment_id,
        **kwargs
    ):
        """Delete a enrollment by an id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_enrollment_by_id(x_tenant, enrollment_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            enrollment_id (str): Id of the enrollment

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_tenant'] = \
            x_tenant
        kwargs['enrollment_id'] = \
            enrollment_id
        return self.delete_enrollment_by_id_endpoint.call_with_http_info(**kwargs)

    def find_enrollment_by_enrollment_id(
        self,
        x_tenant,
        enrollment_id,
        **kwargs
    ):
        """Find enrollment by Id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_enrollment_by_enrollment_id(x_tenant, enrollment_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            enrollment_id (str): Id of the enrollment

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Enrollment
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_tenant'] = \
            x_tenant
        kwargs['enrollment_id'] = \
            enrollment_id
        return self.find_enrollment_by_enrollment_id_endpoint.call_with_http_info(**kwargs)

    def find_enrollments(
        self,
        x_tenant,
        **kwargs
    ):
        """Retrieve all enrollment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_enrollments(x_tenant, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):

        Keyword Args:
            page (int): [optional] if omitted the server will use the default value of 0
            size (int): [optional] if omitted the server will use the default value of 200
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            EnrollmentPage
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_tenant'] = \
            x_tenant
        return self.find_enrollments_endpoint.call_with_http_info(**kwargs)

