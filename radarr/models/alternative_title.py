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
from radarr.models.language import Language
from radarr.models.source_type import SourceType

class AlternativeTitle(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    source_type: Optional[SourceType]
    movie_metadata_id: Optional[int]
    title: Optional[str]
    clean_title: Optional[str]
    source_id: Optional[int]
    votes: Optional[int]
    vote_count: Optional[int]
    language: Optional[Language]
    __properties = ["id", "sourceType", "movieMetadataId", "title", "cleanTitle", "sourceId", "votes", "voteCount", "language"]

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
    def from_json(cls, json_str: str) -> AlternativeTitle:
        """Create an instance of AlternativeTitle from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of language
        if self.language:
            _dict['language'] = self.language.to_dict()
        # set to None if title (nullable) is None
        if self.title is None:
            _dict['title'] = None

        # set to None if clean_title (nullable) is None
        if self.clean_title is None:
            _dict['cleanTitle'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AlternativeTitle:
        """Create an instance of AlternativeTitle from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AlternativeTitle.parse_obj(obj)

        _obj = AlternativeTitle.parse_obj({
            "id": obj.get("id"),
            "source_type": obj.get("sourceType"),
            "movie_metadata_id": obj.get("movieMetadataId"),
            "title": obj.get("title"),
            "clean_title": obj.get("cleanTitle"),
            "source_id": obj.get("sourceId"),
            "votes": obj.get("votes"),
            "vote_count": obj.get("voteCount"),
            "language": Language.from_dict(obj.get("language")) if obj.get("language") is not None else None
        })
        return _obj

