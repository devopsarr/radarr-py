# coding: utf-8

"""
    Radarr

    Radarr API docs  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel

class HttpUri(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    full_uri: Optional[str]
    scheme: Optional[str]
    host: Optional[str]
    port: Optional[int]
    path: Optional[str]
    query: Optional[str]
    fragment: Optional[str]
    __properties = ["fullUri", "scheme", "host", "port", "path", "query", "fragment"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        alias_generator = lambda x: x.split("_")[0] + "".join(word.capitalize() for word in x.split("_")[1:])

    def __getitem__(self, item):
        return getattr(self, item)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> HttpUri:
        """Create an instance of HttpUri from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "full_uri",
                            "scheme",
                            "host",
                            "port",
                            "path",
                            "query",
                            "fragment",
                          },
                          exclude_none=True)
        # set to None if full_uri (nullable) is None
        if self.full_uri is None:
            _dict['fullUri'] = None

        # set to None if scheme (nullable) is None
        if self.scheme is None:
            _dict['scheme'] = None

        # set to None if host (nullable) is None
        if self.host is None:
            _dict['host'] = None

        # set to None if port (nullable) is None
        if self.port is None:
            _dict['port'] = None

        # set to None if path (nullable) is None
        if self.path is None:
            _dict['path'] = None

        # set to None if query (nullable) is None
        if self.query is None:
            _dict['query'] = None

        # set to None if fragment (nullable) is None
        if self.fragment is None:
            _dict['fragment'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HttpUri:
        """Create an instance of HttpUri from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return HttpUri.parse_obj(obj)

        _obj = HttpUri.parse_obj({
            "full_uri": obj.get("fullUri"),
            "scheme": obj.get("scheme"),
            "host": obj.get("host"),
            "port": obj.get("port"),
            "path": obj.get("path"),
            "query": obj.get("query"),
            "fragment": obj.get("fragment")
        })
        return _obj

