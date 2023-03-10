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
from radarr.models.extra_file_type import ExtraFileType

class ExtraFileResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    movie_id: Optional[int]
    movie_file_id: Optional[int]
    relative_path: Optional[str]
    extension: Optional[str]
    type: Optional[ExtraFileType]
    __properties = ["id", "movieId", "movieFileId", "relativePath", "extension", "type"]

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
    def from_json(cls, json_str: str) -> ExtraFileResource:
        """Create an instance of ExtraFileResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if movie_file_id (nullable) is None
        if self.movie_file_id is None:
            _dict['movieFileId'] = None

        # set to None if relative_path (nullable) is None
        if self.relative_path is None:
            _dict['relativePath'] = None

        # set to None if extension (nullable) is None
        if self.extension is None:
            _dict['extension'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExtraFileResource:
        """Create an instance of ExtraFileResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ExtraFileResource.parse_obj(obj)

        _obj = ExtraFileResource.parse_obj({
            "id": obj.get("id"),
            "movie_id": obj.get("movieId"),
            "movie_file_id": obj.get("movieFileId"),
            "relative_path": obj.get("relativePath"),
            "extension": obj.get("extension"),
            "type": obj.get("type")
        })
        return _obj

