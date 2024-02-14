# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.2.6.8376
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from radarr.models.alternative_title import AlternativeTitle
from radarr.models.language import Language
from radarr.models.media_cover import MediaCover
from radarr.models.movie_status_type import MovieStatusType
from radarr.models.movie_translation import MovieTranslation
from radarr.models.ratings import Ratings
from typing import Optional, Set
from typing_extensions import Self

class MovieMetadata(BaseModel):
    """
    MovieMetadata
    """ # noqa: E501
    id: Optional[StrictInt] = None
    tmdb_id: Optional[StrictInt] = Field(default=None, alias="tmdbId")
    images: Optional[List[MediaCover]] = None
    genres: Optional[List[StrictStr]] = None
    in_cinemas: Optional[datetime] = Field(default=None, alias="inCinemas")
    physical_release: Optional[datetime] = Field(default=None, alias="physicalRelease")
    digital_release: Optional[datetime] = Field(default=None, alias="digitalRelease")
    certification: Optional[StrictStr] = None
    year: Optional[StrictInt] = None
    ratings: Optional[Ratings] = None
    collection_tmdb_id: Optional[StrictInt] = Field(default=None, alias="collectionTmdbId")
    collection_title: Optional[StrictStr] = Field(default=None, alias="collectionTitle")
    last_info_sync: Optional[datetime] = Field(default=None, alias="lastInfoSync")
    runtime: Optional[StrictInt] = None
    website: Optional[StrictStr] = None
    imdb_id: Optional[StrictStr] = Field(default=None, alias="imdbId")
    title: Optional[StrictStr] = None
    clean_title: Optional[StrictStr] = Field(default=None, alias="cleanTitle")
    sort_title: Optional[StrictStr] = Field(default=None, alias="sortTitle")
    status: Optional[MovieStatusType] = None
    overview: Optional[StrictStr] = None
    alternative_titles: Optional[List[AlternativeTitle]] = Field(default=None, alias="alternativeTitles")
    translations: Optional[List[MovieTranslation]] = None
    secondary_year: Optional[StrictInt] = Field(default=None, alias="secondaryYear")
    you_tube_trailer_id: Optional[StrictStr] = Field(default=None, alias="youTubeTrailerId")
    studio: Optional[StrictStr] = None
    original_title: Optional[StrictStr] = Field(default=None, alias="originalTitle")
    clean_original_title: Optional[StrictStr] = Field(default=None, alias="cleanOriginalTitle")
    original_language: Optional[Language] = Field(default=None, alias="originalLanguage")
    recommendations: Optional[List[StrictInt]] = None
    popularity: Optional[Union[StrictFloat, StrictInt]] = None
    is_recent_movie: Optional[StrictBool] = Field(default=None, alias="isRecentMovie")
    __properties: ClassVar[List[str]] = ["id", "tmdbId", "images", "genres", "inCinemas", "physicalRelease", "digitalRelease", "certification", "year", "ratings", "collectionTmdbId", "collectionTitle", "lastInfoSync", "runtime", "website", "imdbId", "title", "cleanTitle", "sortTitle", "status", "overview", "alternativeTitles", "translations", "secondaryYear", "youTubeTrailerId", "studio", "originalTitle", "cleanOriginalTitle", "originalLanguage", "recommendations", "popularity", "isRecentMovie"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MovieMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "is_recent_movie",
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
        # override the default output from pydantic by calling `to_dict()` of ratings
        if self.ratings:
            _dict['ratings'] = self.ratings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in alternative_titles (list)
        _items = []
        if self.alternative_titles:
            for _item in self.alternative_titles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['alternativeTitles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in translations (list)
        _items = []
        if self.translations:
            for _item in self.translations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['translations'] = _items
        # override the default output from pydantic by calling `to_dict()` of original_language
        if self.original_language:
            _dict['originalLanguage'] = self.original_language.to_dict()
        # set to None if images (nullable) is None
        # and model_fields_set contains the field
        if self.images is None and "images" in self.model_fields_set:
            _dict['images'] = None

        # set to None if genres (nullable) is None
        # and model_fields_set contains the field
        if self.genres is None and "genres" in self.model_fields_set:
            _dict['genres'] = None

        # set to None if in_cinemas (nullable) is None
        # and model_fields_set contains the field
        if self.in_cinemas is None and "in_cinemas" in self.model_fields_set:
            _dict['inCinemas'] = None

        # set to None if physical_release (nullable) is None
        # and model_fields_set contains the field
        if self.physical_release is None and "physical_release" in self.model_fields_set:
            _dict['physicalRelease'] = None

        # set to None if digital_release (nullable) is None
        # and model_fields_set contains the field
        if self.digital_release is None and "digital_release" in self.model_fields_set:
            _dict['digitalRelease'] = None

        # set to None if certification (nullable) is None
        # and model_fields_set contains the field
        if self.certification is None and "certification" in self.model_fields_set:
            _dict['certification'] = None

        # set to None if collection_title (nullable) is None
        # and model_fields_set contains the field
        if self.collection_title is None and "collection_title" in self.model_fields_set:
            _dict['collectionTitle'] = None

        # set to None if last_info_sync (nullable) is None
        # and model_fields_set contains the field
        if self.last_info_sync is None and "last_info_sync" in self.model_fields_set:
            _dict['lastInfoSync'] = None

        # set to None if website (nullable) is None
        # and model_fields_set contains the field
        if self.website is None and "website" in self.model_fields_set:
            _dict['website'] = None

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

        # set to None if alternative_titles (nullable) is None
        # and model_fields_set contains the field
        if self.alternative_titles is None and "alternative_titles" in self.model_fields_set:
            _dict['alternativeTitles'] = None

        # set to None if translations (nullable) is None
        # and model_fields_set contains the field
        if self.translations is None and "translations" in self.model_fields_set:
            _dict['translations'] = None

        # set to None if secondary_year (nullable) is None
        # and model_fields_set contains the field
        if self.secondary_year is None and "secondary_year" in self.model_fields_set:
            _dict['secondaryYear'] = None

        # set to None if you_tube_trailer_id (nullable) is None
        # and model_fields_set contains the field
        if self.you_tube_trailer_id is None and "you_tube_trailer_id" in self.model_fields_set:
            _dict['youTubeTrailerId'] = None

        # set to None if studio (nullable) is None
        # and model_fields_set contains the field
        if self.studio is None and "studio" in self.model_fields_set:
            _dict['studio'] = None

        # set to None if original_title (nullable) is None
        # and model_fields_set contains the field
        if self.original_title is None and "original_title" in self.model_fields_set:
            _dict['originalTitle'] = None

        # set to None if clean_original_title (nullable) is None
        # and model_fields_set contains the field
        if self.clean_original_title is None and "clean_original_title" in self.model_fields_set:
            _dict['cleanOriginalTitle'] = None

        # set to None if recommendations (nullable) is None
        # and model_fields_set contains the field
        if self.recommendations is None and "recommendations" in self.model_fields_set:
            _dict['recommendations'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MovieMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "tmdbId": obj.get("tmdbId"),
            "images": [MediaCover.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "genres": obj.get("genres"),
            "inCinemas": obj.get("inCinemas"),
            "physicalRelease": obj.get("physicalRelease"),
            "digitalRelease": obj.get("digitalRelease"),
            "certification": obj.get("certification"),
            "year": obj.get("year"),
            "ratings": Ratings.from_dict(obj["ratings"]) if obj.get("ratings") is not None else None,
            "collectionTmdbId": obj.get("collectionTmdbId"),
            "collectionTitle": obj.get("collectionTitle"),
            "lastInfoSync": obj.get("lastInfoSync"),
            "runtime": obj.get("runtime"),
            "website": obj.get("website"),
            "imdbId": obj.get("imdbId"),
            "title": obj.get("title"),
            "cleanTitle": obj.get("cleanTitle"),
            "sortTitle": obj.get("sortTitle"),
            "status": obj.get("status"),
            "overview": obj.get("overview"),
            "alternativeTitles": [AlternativeTitle.from_dict(_item) for _item in obj["alternativeTitles"]] if obj.get("alternativeTitles") is not None else None,
            "translations": [MovieTranslation.from_dict(_item) for _item in obj["translations"]] if obj.get("translations") is not None else None,
            "secondaryYear": obj.get("secondaryYear"),
            "youTubeTrailerId": obj.get("youTubeTrailerId"),
            "studio": obj.get("studio"),
            "originalTitle": obj.get("originalTitle"),
            "cleanOriginalTitle": obj.get("cleanOriginalTitle"),
            "originalLanguage": Language.from_dict(obj["originalLanguage"]) if obj.get("originalLanguage") is not None else None,
            "recommendations": obj.get("recommendations"),
            "popularity": obj.get("popularity"),
            "isRecentMovie": obj.get("isRecentMovie")
        })
        return _obj


