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


from typing import List, Optional
from pydantic import BaseModel

class RestrictionResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    required: Optional[str]
    preferred: Optional[str]
    ignored: Optional[str]
    tags: Optional[List]
    __properties = ["id", "required", "preferred", "ignored", "tags"]

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
    def from_json(cls, json_str: str) -> RestrictionResource:
        """Create an instance of RestrictionResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if required (nullable) is None
        if self.required is None:
            _dict['required'] = None

        # set to None if preferred (nullable) is None
        if self.preferred is None:
            _dict['preferred'] = None

        # set to None if ignored (nullable) is None
        if self.ignored is None:
            _dict['ignored'] = None

        # set to None if tags (nullable) is None
        if self.tags is None:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RestrictionResource:
        """Create an instance of RestrictionResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RestrictionResource.parse_obj(obj)

        _obj = RestrictionResource.parse_obj({
            "id": obj.get("id"),
            "required": obj.get("required"),
            "preferred": obj.get("preferred"),
            "ignored": obj.get("ignored"),
            "tags": obj.get("tags")
        })
        return _obj

