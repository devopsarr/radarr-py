# coding: utf-8

"""
    Radarr

    Radarr API docs  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import StrictBool, StrictInt, StrictStr

from typing import Optional

from radarr.models.colon_replacement_format import ColonReplacementFormat
from radarr.models.naming_config_resource import NamingConfigResource

from radarr.api_client import ApiClient
from radarr.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class NamingConfigApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_naming_config(self, **kwargs) -> NamingConfigResource:  # noqa: E501
        """get_naming_config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_naming_config(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NamingConfigResource
        """
        kwargs['_return_http_data_only'] = True
        return self.get_naming_config_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_naming_config_with_http_info(self, **kwargs):  # noqa: E501
        """get_naming_config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_naming_config_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NamingConfigResource, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_naming_config" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['apikey', 'X-Api-Key']  # noqa: E501

        _response_types_map = {
            '200': "NamingConfigResource",
        }

        return self.api_client.call_api(
            '/api/v3/config/naming', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_naming_config_by_id(self, id : StrictInt, **kwargs) -> NamingConfigResource:  # noqa: E501
        """get_naming_config_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_naming_config_by_id(id, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NamingConfigResource
        """
        kwargs['_return_http_data_only'] = True
        return self.get_naming_config_by_id_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_naming_config_by_id_with_http_info(self, id : StrictInt, **kwargs):  # noqa: E501
        """get_naming_config_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_naming_config_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NamingConfigResource, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_naming_config_by_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['apikey', 'X-Api-Key']  # noqa: E501

        _response_types_map = {
            '200': "NamingConfigResource",
        }

        return self.api_client.call_api(
            '/api/v3/config/naming/{id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_naming_config_examples(self, rename_movies : Optional[StrictBool] = None, replace_illegal_characters : Optional[StrictBool] = None, colon_replacement_format : Optional[ColonReplacementFormat] = None, standard_movie_format : Optional[StrictStr] = None, movie_folder_format : Optional[StrictStr] = None, include_quality : Optional[StrictBool] = None, replace_spaces : Optional[StrictBool] = None, separator : Optional[StrictStr] = None, number_style : Optional[StrictStr] = None, id : Optional[StrictInt] = None, resource_name : Optional[StrictStr] = None, **kwargs) -> None:  # noqa: E501
        """get_naming_config_examples  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_naming_config_examples(rename_movies, replace_illegal_characters, colon_replacement_format, standard_movie_format, movie_folder_format, include_quality, replace_spaces, separator, number_style, id, resource_name, async_req=True)
        >>> result = thread.get()

        :param rename_movies:
        :type rename_movies: bool
        :param replace_illegal_characters:
        :type replace_illegal_characters: bool
        :param colon_replacement_format:
        :type colon_replacement_format: ColonReplacementFormat
        :param standard_movie_format:
        :type standard_movie_format: str
        :param movie_folder_format:
        :type movie_folder_format: str
        :param include_quality:
        :type include_quality: bool
        :param replace_spaces:
        :type replace_spaces: bool
        :param separator:
        :type separator: str
        :param number_style:
        :type number_style: str
        :param id:
        :type id: int
        :param resource_name:
        :type resource_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.get_naming_config_examples_with_http_info(rename_movies, replace_illegal_characters, colon_replacement_format, standard_movie_format, movie_folder_format, include_quality, replace_spaces, separator, number_style, id, resource_name, **kwargs)  # noqa: E501

    @validate_arguments
    def get_naming_config_examples_with_http_info(self, rename_movies : Optional[StrictBool] = None, replace_illegal_characters : Optional[StrictBool] = None, colon_replacement_format : Optional[ColonReplacementFormat] = None, standard_movie_format : Optional[StrictStr] = None, movie_folder_format : Optional[StrictStr] = None, include_quality : Optional[StrictBool] = None, replace_spaces : Optional[StrictBool] = None, separator : Optional[StrictStr] = None, number_style : Optional[StrictStr] = None, id : Optional[StrictInt] = None, resource_name : Optional[StrictStr] = None, **kwargs):  # noqa: E501
        """get_naming_config_examples  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_naming_config_examples_with_http_info(rename_movies, replace_illegal_characters, colon_replacement_format, standard_movie_format, movie_folder_format, include_quality, replace_spaces, separator, number_style, id, resource_name, async_req=True)
        >>> result = thread.get()

        :param rename_movies:
        :type rename_movies: bool
        :param replace_illegal_characters:
        :type replace_illegal_characters: bool
        :param colon_replacement_format:
        :type colon_replacement_format: ColonReplacementFormat
        :param standard_movie_format:
        :type standard_movie_format: str
        :param movie_folder_format:
        :type movie_folder_format: str
        :param include_quality:
        :type include_quality: bool
        :param replace_spaces:
        :type replace_spaces: bool
        :param separator:
        :type separator: str
        :param number_style:
        :type number_style: str
        :param id:
        :type id: int
        :param resource_name:
        :type resource_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'rename_movies',
            'replace_illegal_characters',
            'colon_replacement_format',
            'standard_movie_format',
            'movie_folder_format',
            'include_quality',
            'replace_spaces',
            'separator',
            'number_style',
            'id',
            'resource_name'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_naming_config_examples" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('rename_movies') is not None:  # noqa: E501
            _query_params.append(('renameMovies', _params['rename_movies']))
        if _params.get('replace_illegal_characters') is not None:  # noqa: E501
            _query_params.append(('replaceIllegalCharacters', _params['replace_illegal_characters']))
        if _params.get('colon_replacement_format') is not None:  # noqa: E501
            _query_params.append(('colonReplacementFormat', _params['colon_replacement_format']))
        if _params.get('standard_movie_format') is not None:  # noqa: E501
            _query_params.append(('standardMovieFormat', _params['standard_movie_format']))
        if _params.get('movie_folder_format') is not None:  # noqa: E501
            _query_params.append(('movieFolderFormat', _params['movie_folder_format']))
        if _params.get('include_quality') is not None:  # noqa: E501
            _query_params.append(('includeQuality', _params['include_quality']))
        if _params.get('replace_spaces') is not None:  # noqa: E501
            _query_params.append(('replaceSpaces', _params['replace_spaces']))
        if _params.get('separator') is not None:  # noqa: E501
            _query_params.append(('separator', _params['separator']))
        if _params.get('number_style') is not None:  # noqa: E501
            _query_params.append(('numberStyle', _params['number_style']))
        if _params.get('id') is not None:  # noqa: E501
            _query_params.append(('id', _params['id']))
        if _params.get('resource_name') is not None:  # noqa: E501
            _query_params.append(('resourceName', _params['resource_name']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # authentication setting
        _auth_settings = ['apikey', 'X-Api-Key']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v3/config/naming/examples', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def update_naming_config(self, id : StrictStr, naming_config_resource : Optional[NamingConfigResource] = None, **kwargs) -> NamingConfigResource:  # noqa: E501
        """update_naming_config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_naming_config(id, naming_config_resource, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param naming_config_resource:
        :type naming_config_resource: NamingConfigResource
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NamingConfigResource
        """
        kwargs['_return_http_data_only'] = True
        return self.update_naming_config_with_http_info(id, naming_config_resource, **kwargs)  # noqa: E501

    @validate_arguments
    def update_naming_config_with_http_info(self, id : StrictStr, naming_config_resource : Optional[NamingConfigResource] = None, **kwargs):  # noqa: E501
        """update_naming_config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_naming_config_with_http_info(id, naming_config_resource, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param naming_config_resource:
        :type naming_config_resource: NamingConfigResource
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NamingConfigResource, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'naming_config_resource'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_naming_config" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None
        if _params['naming_config_resource']:
            _body_params = _params['naming_config_resource']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json', 'text/json', 'application/*+json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['apikey', 'X-Api-Key']  # noqa: E501

        _response_types_map = {
            '200': "NamingConfigResource",
        }

        return self.api_client.call_api(
            '/api/v3/config/naming/{id}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
