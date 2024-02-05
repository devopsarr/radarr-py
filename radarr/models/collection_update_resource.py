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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from radarr.models.movie_status_type import MovieStatusType

class CollectionUpdateResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    collection_ids: Optional[List]
    monitored: Optional[bool]
    monitor_movies: Optional[bool]
    quality_profile_id: Optional[int]
    root_folder_path: Optional[str]
    minimum_availability: Optional[MovieStatusType]
    __properties = ["collectionIds", "monitored", "monitorMovies", "qualityProfileId", "rootFolderPath", "minimumAvailability"]

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
    def from_json(cls, json_str: str) -> CollectionUpdateResource:
        """Create an instance of CollectionUpdateResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if collection_ids (nullable) is None
        if self.collection_ids is None:
            _dict['collectionIds'] = None

        # set to None if monitored (nullable) is None
        if self.monitored is None:
            _dict['monitored'] = None

        # set to None if monitor_movies (nullable) is None
        if self.monitor_movies is None:
            _dict['monitorMovies'] = None

        # set to None if quality_profile_id (nullable) is None
        if self.quality_profile_id is None:
            _dict['qualityProfileId'] = None

        # set to None if root_folder_path (nullable) is None
        if self.root_folder_path is None:
            _dict['rootFolderPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CollectionUpdateResource:
        """Create an instance of CollectionUpdateResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CollectionUpdateResource.parse_obj(obj)

        _obj = CollectionUpdateResource.parse_obj({
            "collection_ids": obj.get("collectionIds"),
            "monitored": obj.get("monitored"),
            "monitor_movies": obj.get("monitorMovies"),
            "quality_profile_id": obj.get("qualityProfileId"),
            "root_folder_path": obj.get("rootFolderPath"),
            "minimum_availability": obj.get("minimumAvailability")
        })
        return _obj

