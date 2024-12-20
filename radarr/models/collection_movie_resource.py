# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.16.3.9541
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from radarr.models.media_cover import MediaCover
from radarr.models.movie_status_type import MovieStatusType
from radarr.models.ratings import Ratings
from typing import Optional, Set
from typing_extensions import Self

class CollectionMovieResource(BaseModel):
    """
    CollectionMovieResource
    """ # noqa: E501
    tmdb_id: Optional[StrictInt] = Field(default=None, alias="tmdbId")
    imdb_id: Optional[StrictStr] = Field(default=None, alias="imdbId")
    title: Optional[StrictStr] = None
    clean_title: Optional[StrictStr] = Field(default=None, alias="cleanTitle")
    sort_title: Optional[StrictStr] = Field(default=None, alias="sortTitle")
    status: Optional[MovieStatusType] = None
    overview: Optional[StrictStr] = None
    runtime: Optional[StrictInt] = None
    images: Optional[List[MediaCover]] = None
    year: Optional[StrictInt] = None
    ratings: Optional[Ratings] = None
    genres: Optional[List[StrictStr]] = None
    folder: Optional[StrictStr] = None
    is_existing: Optional[StrictBool] = Field(default=None, alias="isExisting")
    is_excluded: Optional[StrictBool] = Field(default=None, alias="isExcluded")
    __properties: ClassVar[List[str]] = ["tmdbId", "imdbId", "title", "cleanTitle", "sortTitle", "status", "overview", "runtime", "images", "year", "ratings", "genres", "folder", "isExisting", "isExcluded"]

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
        """Create an instance of CollectionMovieResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item_images in self.images:
                if _item_images:
                    _items.append(_item_images.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of ratings
        if self.ratings:
            _dict['ratings'] = self.ratings.to_dict()
        # set to None if imdb_id (nullable) is None
        # and model_fields_set contains the field
        if self.imdb_id is None and "imdb_id" in self.model_fields_set:
            _dict['imdbId'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if clean_title (nullable) is None
        # and model_fields_set contains the field
        if self.clean_title is None and "clean_title" in self.model_fields_set:
            _dict['cleanTitle'] = None

        # set to None if sort_title (nullable) is None
        # and model_fields_set contains the field
        if self.sort_title is None and "sort_title" in self.model_fields_set:
            _dict['sortTitle'] = None

        # set to None if overview (nullable) is None
        # and model_fields_set contains the field
        if self.overview is None and "overview" in self.model_fields_set:
            _dict['overview'] = None

        # set to None if images (nullable) is None
        # and model_fields_set contains the field
        if self.images is None and "images" in self.model_fields_set:
            _dict['images'] = None

        # set to None if genres (nullable) is None
        # and model_fields_set contains the field
        if self.genres is None and "genres" in self.model_fields_set:
            _dict['genres'] = None

        # set to None if folder (nullable) is None
        # and model_fields_set contains the field
        if self.folder is None and "folder" in self.model_fields_set:
            _dict['folder'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CollectionMovieResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tmdbId": obj.get("tmdbId"),
            "imdbId": obj.get("imdbId"),
            "title": obj.get("title"),
            "cleanTitle": obj.get("cleanTitle"),
            "sortTitle": obj.get("sortTitle"),
            "status": obj.get("status"),
            "overview": obj.get("overview"),
            "runtime": obj.get("runtime"),
            "images": [MediaCover.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "year": obj.get("year"),
            "ratings": Ratings.from_dict(obj["ratings"]) if obj.get("ratings") is not None else None,
            "genres": obj.get("genres"),
            "folder": obj.get("folder"),
            "isExisting": obj.get("isExisting"),
            "isExcluded": obj.get("isExcluded")
        })
        return _obj


