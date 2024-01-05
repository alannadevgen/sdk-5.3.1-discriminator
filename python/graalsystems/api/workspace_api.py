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
from graalsystems.model.error import Error
from graalsystems.model.log_entry import LogEntry
from graalsystems.model.patch import Patch
from graalsystems.model.workspace import Workspace
from graalsystems.model.workspace_page import WorkspacePage


class WorkspaceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_workspace_endpoint = _Endpoint(
            settings={
                'response_type': (Workspace,),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/workspaces',
                'operation_id': 'create_workspace',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'workspace',
                ],
                'required': [
                    'x_tenant',
                    'workspace',
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
                    'workspace':
                        (Workspace,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'workspace': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.workspace+json'
                ],
                'content_type': [
                    'application/vnd.graal.systems.v1.workspace+json'
                ]
            },
            api_client=api_client
        )
        self.delete_workspace_by_id_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/workspaces/{workspaceId}',
                'operation_id': 'delete_workspace_by_id',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'workspace_id',
                ],
                'required': [
                    'x_tenant',
                    'workspace_id',
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
                    'workspace_id':
                        (str,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'workspace_id': 'workspaceId',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'workspace_id': 'path',
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
        self.find_workspace_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (Workspace,),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/workspaces/{workspaceId}',
                'operation_id': 'find_workspace_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'workspace_id',
                ],
                'required': [
                    'x_tenant',
                    'workspace_id',
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
                    'workspace_id':
                        (str,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'workspace_id': 'workspaceId',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'workspace_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.workspace+json',
                    'application/vnd.graal.systems.v1.error+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.find_workspaces_endpoint = _Endpoint(
            settings={
                'response_type': (WorkspacePage,),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/workspaces',
                'operation_id': 'find_workspaces',
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
                    'application/vnd.graal.systems.v1.workspace+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_logs_for_workspace_endpoint = _Endpoint(
            settings={
                'response_type': ([LogEntry],),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/workspaces/{workspaceId}/logs',
                'operation_id': 'get_logs_for_workspace',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'workspace_id',
                    'cursor',
                ],
                'required': [
                    'x_tenant',
                    'workspace_id',
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
                    'workspace_id':
                        (str,),
                    'cursor':
                        (str,),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'workspace_id': 'workspaceId',
                    'cursor': 'cursor',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'workspace_id': 'path',
                    'cursor': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.log+json',
                    'application/vnd.graal.systems.v1.error+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_workspace_endpoint = _Endpoint(
            settings={
                'response_type': (Workspace,),
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/workspaces/{workspaceId}',
                'operation_id': 'update_workspace',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'workspace_id',
                    'patch',
                ],
                'required': [
                    'x_tenant',
                    'workspace_id',
                    'patch',
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
                    'workspace_id':
                        (str,),
                    'patch':
                        ([Patch],),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'workspace_id': 'workspaceId',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'workspace_id': 'path',
                    'patch': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.graal.systems.v1.workspace+json',
                    'application/vnd.graal.systems.v1.error+json'
                ],
                'content_type': [
                    'application/json-patch+json;charset=UTF-8'
                ]
            },
            api_client=api_client
        )
        self.upload_file_in_workspace_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'internal'
                ],
                'endpoint_path': '/workspaces/{workspaceId}/files',
                'operation_id': 'upload_file_in_workspace',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_tenant',
                    'workspace_id',
                    'path',
                    'filename',
                ],
                'required': [
                    'x_tenant',
                    'workspace_id',
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
                    'workspace_id':
                        (str,),
                    'path':
                        (str,),
                    'filename':
                        ([file_type],),
                },
                'attribute_map': {
                    'x_tenant': 'X-Tenant',
                    'workspace_id': 'workspaceId',
                    'path': 'path',
                    'filename': 'filename',
                },
                'location_map': {
                    'x_tenant': 'header',
                    'workspace_id': 'path',
                    'path': 'query',
                    'filename': 'form',
                },
                'collection_format_map': {
                    'filename': 'csv',
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'multipart/form-data'
                ]
            },
            api_client=api_client
        )

    def create_workspace(
        self,
        x_tenant,
        workspace,
        **kwargs
    ):
        """Create workspace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_workspace(x_tenant, workspace, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            workspace (Workspace): The workspace to be created

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
            Workspace
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
        kwargs['workspace'] = \
            workspace
        return self.create_workspace_endpoint.call_with_http_info(**kwargs)

    def delete_workspace_by_id(
        self,
        x_tenant,
        workspace_id,
        **kwargs
    ):
        """Delete a workspace by an id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_workspace_by_id(x_tenant, workspace_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            workspace_id (str): Id of the workspace

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
        kwargs['workspace_id'] = \
            workspace_id
        return self.delete_workspace_by_id_endpoint.call_with_http_info(**kwargs)

    def find_workspace_by_id(
        self,
        x_tenant,
        workspace_id,
        **kwargs
    ):
        """Find workspace by Id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_workspace_by_id(x_tenant, workspace_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            workspace_id (str): Id of the workspace

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
            Workspace
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
        kwargs['workspace_id'] = \
            workspace_id
        return self.find_workspace_by_id_endpoint.call_with_http_info(**kwargs)

    def find_workspaces(
        self,
        x_tenant,
        **kwargs
    ):
        """Retrieve all workspaces  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_workspaces(x_tenant, async_req=True)
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
            WorkspacePage
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
        return self.find_workspaces_endpoint.call_with_http_info(**kwargs)

    def get_logs_for_workspace(
        self,
        x_tenant,
        workspace_id,
        **kwargs
    ):
        """Get logs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_logs_for_workspace(x_tenant, workspace_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            workspace_id (str): Id of the workspace

        Keyword Args:
            cursor (str): The cursor. [optional]
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
            [LogEntry]
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
        kwargs['workspace_id'] = \
            workspace_id
        return self.get_logs_for_workspace_endpoint.call_with_http_info(**kwargs)

    def update_workspace(
        self,
        x_tenant,
        workspace_id,
        patch,
        **kwargs
    ):
        """Update a workspace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_workspace(x_tenant, workspace_id, patch, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            workspace_id (str): Id of the workspace
            patch ([Patch]): The patch

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
            Workspace
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
        kwargs['workspace_id'] = \
            workspace_id
        kwargs['patch'] = \
            patch
        return self.update_workspace_endpoint.call_with_http_info(**kwargs)

    def upload_file_in_workspace(
        self,
        x_tenant,
        workspace_id,
        **kwargs
    ):
        """Upload files in a workspace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_file_in_workspace(x_tenant, workspace_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_tenant (str):
            workspace_id (str): Id of the bucket

        Keyword Args:
            path (str): path. [optional]
            filename ([file_type]): [optional]
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
        kwargs['workspace_id'] = \
            workspace_id
        return self.upload_file_in_workspace_endpoint.call_with_http_info(**kwargs)

