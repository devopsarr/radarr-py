# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.18.4.9674
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from radarr.models.custom_format_resource import CustomFormatResource
from radarr.models.download_protocol import DownloadProtocol
from radarr.models.language import Language
from radarr.models.quality_model import QualityModel
from typing import Optional, Set
from typing_extensions import Self

class ReleaseResource(BaseModel):
    """
    ReleaseResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    guid: Optional[StrictStr] = None
    quality: Optional[QualityModel] = None
    custom_formats: Optional[List[CustomFormatResource]] = Field(default=None, alias="customFormats")
    custom_format_score: Optional[StrictInt] = Field(default=None, alias="customFormatScore")
    quality_weight: Optional[StrictInt] = Field(default=None, alias="qualityWeight")
    age: Optional[StrictInt] = None
    age_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ageHours")
    age_minutes: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ageMinutes")
    size: Optional[StrictInt] = None
    indexer_id: Optional[StrictInt] = Field(default=None, alias="indexerId")
    indexer: Optional[StrictStr] = None
    release_group: Optional[StrictStr] = Field(default=None, alias="releaseGroup")
    sub_group: Optional[StrictStr] = Field(default=None, alias="subGroup")
    release_hash: Optional[StrictStr] = Field(default=None, alias="releaseHash")
    title: Optional[StrictStr] = None
    scene_source: Optional[StrictBool] = Field(default=None, alias="sceneSource")
    movie_titles: Optional[List[StrictStr]] = Field(default=None, alias="movieTitles")
    languages: Optional[List[Language]] = None
    mapped_movie_id: Optional[StrictInt] = Field(default=None, alias="mappedMovieId")
    approved: Optional[StrictBool] = None
    temporarily_rejected: Optional[StrictBool] = Field(default=None, alias="temporarilyRejected")
    rejected: Optional[StrictBool] = None
    tmdb_id: Optional[StrictInt] = Field(default=None, alias="tmdbId")
    imdb_id: Optional[StrictInt] = Field(default=None, alias="imdbId")
    rejections: Optional[List[StrictStr]] = None
    publish_date: Optional[datetime] = Field(default=None, alias="publishDate")
    comment_url: Optional[StrictStr] = Field(default=None, alias="commentUrl")
    download_url: Optional[StrictStr] = Field(default=None, alias="downloadUrl")
    info_url: Optional[StrictStr] = Field(default=None, alias="infoUrl")
    download_allowed: Optional[StrictBool] = Field(default=None, alias="downloadAllowed")
    release_weight: Optional[StrictInt] = Field(default=None, alias="releaseWeight")
    edition: Optional[StrictStr] = None
    magnet_url: Optional[StrictStr] = Field(default=None, alias="magnetUrl")
    info_hash: Optional[StrictStr] = Field(default=None, alias="infoHash")
    seeders: Optional[StrictInt] = None
    leechers: Optional[StrictInt] = None
    protocol: Optional[DownloadProtocol] = None
    indexer_flags: Optional[Any] = Field(default=None, alias="indexerFlags")
    movie_id: Optional[StrictInt] = Field(default=None, alias="movieId")
    download_client_id: Optional[StrictInt] = Field(default=None, alias="downloadClientId")
    download_client: Optional[StrictStr] = Field(default=None, alias="downloadClient")
    should_override: Optional[StrictBool] = Field(default=None, alias="shouldOverride")
    __properties: ClassVar[List[str]] = ["id", "guid", "quality", "customFormats", "customFormatScore", "qualityWeight", "age", "ageHours", "ageMinutes", "size", "indexerId", "indexer", "releaseGroup", "subGroup", "releaseHash", "title", "sceneSource", "movieTitles", "languages", "mappedMovieId", "approved", "temporarilyRejected", "rejected", "tmdbId", "imdbId", "rejections", "publishDate", "commentUrl", "downloadUrl", "infoUrl", "downloadAllowed", "releaseWeight", "edition", "magnetUrl", "infoHash", "seeders", "leechers", "protocol", "indexerFlags", "movieId", "downloadClientId", "downloadClient", "shouldOverride"]

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
        """Create an instance of ReleaseResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item_languages in self.languages:
                if _item_languages:
                    _items.append(_item_languages.to_dict())
            _dict['languages'] = _items
        # set to None if guid (nullable) is None
        # and model_fields_set contains the field
        if self.guid is None and "guid" in self.model_fields_set:
            _dict['guid'] = None

        # set to None if custom_formats (nullable) is None
        # and model_fields_set contains the field
        if self.custom_formats is None and "custom_formats" in self.model_fields_set:
            _dict['customFormats'] = None

        # set to None if indexer (nullable) is None
        # and model_fields_set contains the field
        if self.indexer is None and "indexer" in self.model_fields_set:
            _dict['indexer'] = None

        # set to None if release_group (nullable) is None
        # and model_fields_set contains the field
        if self.release_group is None and "release_group" in self.model_fields_set:
            _dict['releaseGroup'] = None

        # set to None if sub_group (nullable) is None
        # and model_fields_set contains the field
        if self.sub_group is None and "sub_group" in self.model_fields_set:
            _dict['subGroup'] = None

        # set to None if release_hash (nullable) is None
        # and model_fields_set contains the field
        if self.release_hash is None and "release_hash" in self.model_fields_set:
            _dict['releaseHash'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if movie_titles (nullable) is None
        # and model_fields_set contains the field
        if self.movie_titles is None and "movie_titles" in self.model_fields_set:
            _dict['movieTitles'] = None

        # set to None if languages (nullable) is None
        # and model_fields_set contains the field
        if self.languages is None and "languages" in self.model_fields_set:
            _dict['languages'] = None

        # set to None if mapped_movie_id (nullable) is None
        # and model_fields_set contains the field
        if self.mapped_movie_id is None and "mapped_movie_id" in self.model_fields_set:
            _dict['mappedMovieId'] = None

        # set to None if rejections (nullable) is None
        # and model_fields_set contains the field
        if self.rejections is None and "rejections" in self.model_fields_set:
            _dict['rejections'] = None

        # set to None if comment_url (nullable) is None
        # and model_fields_set contains the field
        if self.comment_url is None and "comment_url" in self.model_fields_set:
            _dict['commentUrl'] = None

        # set to None if download_url (nullable) is None
        # and model_fields_set contains the field
        if self.download_url is None and "download_url" in self.model_fields_set:
            _dict['downloadUrl'] = None

        # set to None if info_url (nullable) is None
        # and model_fields_set contains the field
        if self.info_url is None and "info_url" in self.model_fields_set:
            _dict['infoUrl'] = None

        # set to None if edition (nullable) is None
        # and model_fields_set contains the field
        if self.edition is None and "edition" in self.model_fields_set:
            _dict['edition'] = None

        # set to None if magnet_url (nullable) is None
        # and model_fields_set contains the field
        if self.magnet_url is None and "magnet_url" in self.model_fields_set:
            _dict['magnetUrl'] = None

        # set to None if info_hash (nullable) is None
        # and model_fields_set contains the field
        if self.info_hash is None and "info_hash" in self.model_fields_set:
            _dict['infoHash'] = None

        # set to None if seeders (nullable) is None
        # and model_fields_set contains the field
        if self.seeders is None and "seeders" in self.model_fields_set:
            _dict['seeders'] = None

        # set to None if leechers (nullable) is None
        # and model_fields_set contains the field
        if self.leechers is None and "leechers" in self.model_fields_set:
            _dict['leechers'] = None

        # set to None if indexer_flags (nullable) is None
        # and model_fields_set contains the field
        if self.indexer_flags is None and "indexer_flags" in self.model_fields_set:
            _dict['indexerFlags'] = None

        # set to None if movie_id (nullable) is None
        # and model_fields_set contains the field
        if self.movie_id is None and "movie_id" in self.model_fields_set:
            _dict['movieId'] = None

        # set to None if download_client_id (nullable) is None
        # and model_fields_set contains the field
        if self.download_client_id is None and "download_client_id" in self.model_fields_set:
            _dict['downloadClientId'] = None

        # set to None if download_client (nullable) is None
        # and model_fields_set contains the field
        if self.download_client is None and "download_client" in self.model_fields_set:
            _dict['downloadClient'] = None

        # set to None if should_override (nullable) is None
        # and model_fields_set contains the field
        if self.should_override is None and "should_override" in self.model_fields_set:
            _dict['shouldOverride'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReleaseResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "guid": obj.get("guid"),
            "quality": QualityModel.from_dict(obj["quality"]) if obj.get("quality") is not None else None,
            "customFormats": [CustomFormatResource.from_dict(_item) for _item in obj["customFormats"]] if obj.get("customFormats") is not None else None,
            "customFormatScore": obj.get("customFormatScore"),
            "qualityWeight": obj.get("qualityWeight"),
            "age": obj.get("age"),
            "ageHours": obj.get("ageHours"),
            "ageMinutes": obj.get("ageMinutes"),
            "size": obj.get("size"),
            "indexerId": obj.get("indexerId"),
            "indexer": obj.get("indexer"),
            "releaseGroup": obj.get("releaseGroup"),
            "subGroup": obj.get("subGroup"),
            "releaseHash": obj.get("releaseHash"),
            "title": obj.get("title"),
            "sceneSource": obj.get("sceneSource"),
            "movieTitles": obj.get("movieTitles"),
            "languages": [Language.from_dict(_item) for _item in obj["languages"]] if obj.get("languages") is not None else None,
            "mappedMovieId": obj.get("mappedMovieId"),
            "approved": obj.get("approved"),
            "temporarilyRejected": obj.get("temporarilyRejected"),
            "rejected": obj.get("rejected"),
            "tmdbId": obj.get("tmdbId"),
            "imdbId": obj.get("imdbId"),
            "rejections": obj.get("rejections"),
            "publishDate": obj.get("publishDate"),
            "commentUrl": obj.get("commentUrl"),
            "downloadUrl": obj.get("downloadUrl"),
            "infoUrl": obj.get("infoUrl"),
            "downloadAllowed": obj.get("downloadAllowed"),
            "releaseWeight": obj.get("releaseWeight"),
            "edition": obj.get("edition"),
            "magnetUrl": obj.get("magnetUrl"),
            "infoHash": obj.get("infoHash"),
            "seeders": obj.get("seeders"),
            "leechers": obj.get("leechers"),
            "protocol": obj.get("protocol"),
            "indexerFlags": obj.get("indexerFlags"),
            "movieId": obj.get("movieId"),
            "downloadClientId": obj.get("downloadClientId"),
            "downloadClient": obj.get("downloadClient"),
            "shouldOverride": obj.get("shouldOverride")
        })
        return _obj


