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
from radarr.models.custom_format_resource import CustomFormatResource
from radarr.models.language import Language
from radarr.models.movie_resource import MovieResource
from radarr.models.quality_model import QualityModel
from radarr.models.rejection import Rejection

class ManualImportResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    path: Optional[str]
    relative_path: Optional[str]
    folder_name: Optional[str]
    name: Optional[str]
    size: Optional[int]
    movie: Optional[MovieResource]
    quality: Optional[QualityModel]
    languages: Optional[List]
    release_group: Optional[str]
    quality_weight: Optional[int]
    download_id: Optional[str]
    custom_formats: Optional[List]
    rejections: Optional[List]
    __properties = ["id", "path", "relativePath", "folderName", "name", "size", "movie", "quality", "languages", "releaseGroup", "qualityWeight", "downloadId", "customFormats", "rejections"]

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
    def from_json(cls, json_str: str) -> ManualImportResource:
        """Create an instance of ManualImportResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of movie
        if self.movie:
            _dict['movie'] = self.movie.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item in self.languages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['languages'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_formats (list)
        _items = []
        if self.custom_formats:
            for _item in self.custom_formats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFormats'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rejections (list)
        _items = []
        if self.rejections:
            for _item in self.rejections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rejections'] = _items
        # set to None if path (nullable) is None
        if self.path is None:
            _dict['path'] = None

        # set to None if relative_path (nullable) is None
        if self.relative_path is None:
            _dict['relativePath'] = None

        # set to None if folder_name (nullable) is None
        if self.folder_name is None:
            _dict['folderName'] = None

        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if languages (nullable) is None
        if self.languages is None:
            _dict['languages'] = None

        # set to None if release_group (nullable) is None
        if self.release_group is None:
            _dict['releaseGroup'] = None

        # set to None if download_id (nullable) is None
        if self.download_id is None:
            _dict['downloadId'] = None

        # set to None if custom_formats (nullable) is None
        if self.custom_formats is None:
            _dict['customFormats'] = None

        # set to None if rejections (nullable) is None
        if self.rejections is None:
            _dict['rejections'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ManualImportResource:
        """Create an instance of ManualImportResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ManualImportResource.parse_obj(obj)

        _obj = ManualImportResource.parse_obj({
            "id": obj.get("id"),
            "path": obj.get("path"),
            "relative_path": obj.get("relativePath"),
            "folder_name": obj.get("folderName"),
            "name": obj.get("name"),
            "size": obj.get("size"),
            "movie": MovieResource.from_dict(obj.get("movie")) if obj.get("movie") is not None else None,
            "quality": QualityModel.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "languages": [Language.from_dict(_item) for _item in obj.get("languages")] if obj.get("languages") is not None else None,
            "release_group": obj.get("releaseGroup"),
            "quality_weight": obj.get("qualityWeight"),
            "download_id": obj.get("downloadId"),
            "custom_formats": [CustomFormatResource.from_dict(_item) for _item in obj.get("customFormats")] if obj.get("customFormats") is not None else None,
            "rejections": [Rejection.from_dict(_item) for _item in obj.get("rejections")] if obj.get("rejections") is not None else None
        })
        return _obj
