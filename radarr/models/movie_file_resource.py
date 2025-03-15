# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.19.3.9730
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from radarr.models.custom_format_resource import CustomFormatResource
from radarr.models.language import Language
from radarr.models.media_info_resource import MediaInfoResource
from radarr.models.quality_model import QualityModel
from typing import Optional, Set
from typing_extensions import Self

class MovieFileResource(BaseModel):
    """
    MovieFileResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    movie_id: Optional[StrictInt] = Field(default=None, alias="movieId")
    relative_path: Optional[StrictStr] = Field(default=None, alias="relativePath")
    path: Optional[StrictStr] = None
    size: Optional[StrictInt] = None
    date_added: Optional[datetime] = Field(default=None, alias="dateAdded")
    scene_name: Optional[StrictStr] = Field(default=None, alias="sceneName")
    release_group: Optional[StrictStr] = Field(default=None, alias="releaseGroup")
    edition: Optional[StrictStr] = None
    languages: Optional[List[Language]] = None
    quality: Optional[QualityModel] = None
    custom_formats: Optional[List[CustomFormatResource]] = Field(default=None, alias="customFormats")
    custom_format_score: Optional[StrictInt] = Field(default=None, alias="customFormatScore")
    indexer_flags: Optional[StrictInt] = Field(default=None, alias="indexerFlags")
    media_info: Optional[MediaInfoResource] = Field(default=None, alias="mediaInfo")
    original_file_path: Optional[StrictStr] = Field(default=None, alias="originalFilePath")
    quality_cutoff_not_met: Optional[StrictBool] = Field(default=None, alias="qualityCutoffNotMet")
    __properties: ClassVar[List[str]] = ["id", "movieId", "relativePath", "path", "size", "dateAdded", "sceneName", "releaseGroup", "edition", "languages", "quality", "customFormats", "customFormatScore", "indexerFlags", "mediaInfo", "originalFilePath", "qualityCutoffNotMet"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MovieFileResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item_languages in self.languages:
                if _item_languages:
                    _items.append(_item_languages.to_dict())
            _dict['languages'] = _items
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in custom_formats (list)
        _items = []
        if self.custom_formats:
            for _item_custom_formats in self.custom_formats:
                if _item_custom_formats:
                    _items.append(_item_custom_formats.to_dict())
            _dict['customFormats'] = _items
        # override the default output from pydantic by calling `to_dict()` of media_info
        if self.media_info:
            _dict['mediaInfo'] = self.media_info.to_dict()
        # set to None if relative_path (nullable) is None
        # and model_fields_set contains the field
        if self.relative_path is None and "relative_path" in self.model_fields_set:
            _dict['relativePath'] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if scene_name (nullable) is None
        # and model_fields_set contains the field
        if self.scene_name is None and "scene_name" in self.model_fields_set:
            _dict['sceneName'] = None

        # set to None if release_group (nullable) is None
        # and model_fields_set contains the field
        if self.release_group is None and "release_group" in self.model_fields_set:
            _dict['releaseGroup'] = None

        # set to None if edition (nullable) is None
        # and model_fields_set contains the field
        if self.edition is None and "edition" in self.model_fields_set:
            _dict['edition'] = None

        # set to None if languages (nullable) is None
        # and model_fields_set contains the field
        if self.languages is None and "languages" in self.model_fields_set:
            _dict['languages'] = None

        # set to None if custom_formats (nullable) is None
        # and model_fields_set contains the field
        if self.custom_formats is None and "custom_formats" in self.model_fields_set:
            _dict['customFormats'] = None

        # set to None if indexer_flags (nullable) is None
        # and model_fields_set contains the field
        if self.indexer_flags is None and "indexer_flags" in self.model_fields_set:
            _dict['indexerFlags'] = None

        # set to None if original_file_path (nullable) is None
        # and model_fields_set contains the field
        if self.original_file_path is None and "original_file_path" in self.model_fields_set:
            _dict['originalFilePath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MovieFileResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "movieId": obj.get("movieId"),
            "relativePath": obj.get("relativePath"),
            "path": obj.get("path"),
            "size": obj.get("size"),
            "dateAdded": obj.get("dateAdded"),
            "sceneName": obj.get("sceneName"),
            "releaseGroup": obj.get("releaseGroup"),
            "edition": obj.get("edition"),
            "languages": [Language.from_dict(_item) for _item in obj["languages"]] if obj.get("languages") is not None else None,
            "quality": QualityModel.from_dict(obj["quality"]) if obj.get("quality") is not None else None,
            "customFormats": [CustomFormatResource.from_dict(_item) for _item in obj["customFormats"]] if obj.get("customFormats") is not None else None,
            "customFormatScore": obj.get("customFormatScore"),
            "indexerFlags": obj.get("indexerFlags"),
            "mediaInfo": MediaInfoResource.from_dict(obj["mediaInfo"]) if obj.get("mediaInfo") is not None else None,
            "originalFilePath": obj.get("originalFilePath"),
            "qualityCutoffNotMet": obj.get("qualityCutoffNotMet")
        })
        return _obj


