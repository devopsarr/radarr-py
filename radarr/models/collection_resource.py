# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.8.3.8933
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from radarr.models.collection_movie_resource import CollectionMovieResource
from radarr.models.media_cover import MediaCover
from radarr.models.movie_status_type import MovieStatusType
from typing import Optional, Set
from typing_extensions import Self

class CollectionResource(BaseModel):
    """
    CollectionResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    sort_title: Optional[StrictStr] = Field(default=None, alias="sortTitle")
    tmdb_id: Optional[StrictInt] = Field(default=None, alias="tmdbId")
    images: Optional[List[MediaCover]] = None
    overview: Optional[StrictStr] = None
    monitored: Optional[StrictBool] = None
    root_folder_path: Optional[StrictStr] = Field(default=None, alias="rootFolderPath")
    quality_profile_id: Optional[StrictInt] = Field(default=None, alias="qualityProfileId")
    search_on_add: Optional[StrictBool] = Field(default=None, alias="searchOnAdd")
    minimum_availability: Optional[MovieStatusType] = Field(default=None, alias="minimumAvailability")
    movies: Optional[List[CollectionMovieResource]] = None
    missing_movies: Optional[StrictInt] = Field(default=None, alias="missingMovies")
    tags: Optional[List[StrictInt]] = None
    __properties: ClassVar[List[str]] = ["id", "title", "sortTitle", "tmdbId", "images", "overview", "monitored", "rootFolderPath", "qualityProfileId", "searchOnAdd", "minimumAvailability", "movies", "missingMovies", "tags"]

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
        """Create an instance of CollectionResource from a JSON string"""
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
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in movies (list)
        _items = []
        if self.movies:
            for _item in self.movies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['movies'] = _items
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if sort_title (nullable) is None
        # and model_fields_set contains the field
        if self.sort_title is None and "sort_title" in self.model_fields_set:
            _dict['sortTitle'] = None

        # set to None if images (nullable) is None
        # and model_fields_set contains the field
        if self.images is None and "images" in self.model_fields_set:
            _dict['images'] = None

        # set to None if overview (nullable) is None
        # and model_fields_set contains the field
        if self.overview is None and "overview" in self.model_fields_set:
            _dict['overview'] = None

        # set to None if root_folder_path (nullable) is None
        # and model_fields_set contains the field
        if self.root_folder_path is None and "root_folder_path" in self.model_fields_set:
            _dict['rootFolderPath'] = None

        # set to None if movies (nullable) is None
        # and model_fields_set contains the field
        if self.movies is None and "movies" in self.model_fields_set:
            _dict['movies'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CollectionResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "sortTitle": obj.get("sortTitle"),
            "tmdbId": obj.get("tmdbId"),
            "images": [MediaCover.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "overview": obj.get("overview"),
            "monitored": obj.get("monitored"),
            "rootFolderPath": obj.get("rootFolderPath"),
            "qualityProfileId": obj.get("qualityProfileId"),
            "searchOnAdd": obj.get("searchOnAdd"),
            "minimumAvailability": obj.get("minimumAvailability"),
            "movies": [CollectionMovieResource.from_dict(_item) for _item in obj["movies"]] if obj.get("movies") is not None else None,
            "missingMovies": obj.get("missingMovies"),
            "tags": obj.get("tags")
        })
        return _obj


