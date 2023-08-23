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

from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel
from radarr.models.custom_format_resource import CustomFormatResource
from radarr.models.download_protocol import DownloadProtocol
from radarr.models.language import Language
from radarr.models.quality_model import QualityModel

class ReleaseResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    guid: Optional[str]
    quality: Optional[QualityModel]
    custom_formats: Optional[List]
    custom_format_score: Optional[int]
    quality_weight: Optional[int]
    age: Optional[int]
    age_hours: Optional[float]
    age_minutes: Optional[float]
    size: Optional[int]
    indexer_id: Optional[int]
    indexer: Optional[str]
    release_group: Optional[str]
    sub_group: Optional[str]
    release_hash: Optional[str]
    title: Optional[str]
    scene_source: Optional[bool]
    movie_titles: Optional[List]
    languages: Optional[List]
    mapped_movie_id: Optional[int]
    approved: Optional[bool]
    temporarily_rejected: Optional[bool]
    rejected: Optional[bool]
    tmdb_id: Optional[int]
    imdb_id: Optional[int]
    rejections: Optional[List]
    publish_date: Optional[datetime]
    comment_url: Optional[str]
    download_url: Optional[str]
    info_url: Optional[str]
    download_allowed: Optional[bool]
    release_weight: Optional[int]
    indexer_flags: Optional[List]
    edition: Optional[str]
    magnet_url: Optional[str]
    info_hash: Optional[str]
    seeders: Optional[int]
    leechers: Optional[int]
    protocol: Optional[DownloadProtocol]
    movie_id: Optional[int]
    download_client_id: Optional[int]
    should_override: Optional[bool]
    __properties = ["id", "guid", "quality", "customFormats", "customFormatScore", "qualityWeight", "age", "ageHours", "ageMinutes", "size", "indexerId", "indexer", "releaseGroup", "subGroup", "releaseHash", "title", "sceneSource", "movieTitles", "languages", "mappedMovieId", "approved", "temporarilyRejected", "rejected", "tmdbId", "imdbId", "rejections", "publishDate", "commentUrl", "downloadUrl", "infoUrl", "downloadAllowed", "releaseWeight", "indexerFlags", "edition", "magnetUrl", "infoHash", "seeders", "leechers", "protocol", "movieId", "downloadClientId", "shouldOverride"]

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
    def from_json(cls, json_str: str) -> ReleaseResource:
        """Create an instance of ReleaseResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in custom_formats (list)
        _items = []
        if self.custom_formats:
            for _item in self.custom_formats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFormats'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item in self.languages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['languages'] = _items
        # set to None if guid (nullable) is None
        if self.guid is None:
            _dict['guid'] = None

        # set to None if custom_formats (nullable) is None
        if self.custom_formats is None:
            _dict['customFormats'] = None

        # set to None if indexer (nullable) is None
        if self.indexer is None:
            _dict['indexer'] = None

        # set to None if release_group (nullable) is None
        if self.release_group is None:
            _dict['releaseGroup'] = None

        # set to None if sub_group (nullable) is None
        if self.sub_group is None:
            _dict['subGroup'] = None

        # set to None if release_hash (nullable) is None
        if self.release_hash is None:
            _dict['releaseHash'] = None

        # set to None if title (nullable) is None
        if self.title is None:
            _dict['title'] = None

        # set to None if movie_titles (nullable) is None
        if self.movie_titles is None:
            _dict['movieTitles'] = None

        # set to None if languages (nullable) is None
        if self.languages is None:
            _dict['languages'] = None

        # set to None if mapped_movie_id (nullable) is None
        if self.mapped_movie_id is None:
            _dict['mappedMovieId'] = None

        # set to None if rejections (nullable) is None
        if self.rejections is None:
            _dict['rejections'] = None

        # set to None if comment_url (nullable) is None
        if self.comment_url is None:
            _dict['commentUrl'] = None

        # set to None if download_url (nullable) is None
        if self.download_url is None:
            _dict['downloadUrl'] = None

        # set to None if info_url (nullable) is None
        if self.info_url is None:
            _dict['infoUrl'] = None

        # set to None if indexer_flags (nullable) is None
        if self.indexer_flags is None:
            _dict['indexerFlags'] = None

        # set to None if edition (nullable) is None
        if self.edition is None:
            _dict['edition'] = None

        # set to None if magnet_url (nullable) is None
        if self.magnet_url is None:
            _dict['magnetUrl'] = None

        # set to None if info_hash (nullable) is None
        if self.info_hash is None:
            _dict['infoHash'] = None

        # set to None if seeders (nullable) is None
        if self.seeders is None:
            _dict['seeders'] = None

        # set to None if leechers (nullable) is None
        if self.leechers is None:
            _dict['leechers'] = None

        # set to None if movie_id (nullable) is None
        if self.movie_id is None:
            _dict['movieId'] = None

        # set to None if download_client_id (nullable) is None
        if self.download_client_id is None:
            _dict['downloadClientId'] = None

        # set to None if should_override (nullable) is None
        if self.should_override is None:
            _dict['shouldOverride'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReleaseResource:
        """Create an instance of ReleaseResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ReleaseResource.parse_obj(obj)

        _obj = ReleaseResource.parse_obj({
            "id": obj.get("id"),
            "guid": obj.get("guid"),
            "quality": QualityModel.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "custom_formats": [CustomFormatResource.from_dict(_item) for _item in obj.get("customFormats")] if obj.get("customFormats") is not None else None,
            "custom_format_score": obj.get("customFormatScore"),
            "quality_weight": obj.get("qualityWeight"),
            "age": obj.get("age"),
            "age_hours": obj.get("ageHours"),
            "age_minutes": obj.get("ageMinutes"),
            "size": obj.get("size"),
            "indexer_id": obj.get("indexerId"),
            "indexer": obj.get("indexer"),
            "release_group": obj.get("releaseGroup"),
            "sub_group": obj.get("subGroup"),
            "release_hash": obj.get("releaseHash"),
            "title": obj.get("title"),
            "scene_source": obj.get("sceneSource"),
            "movie_titles": obj.get("movieTitles"),
            "languages": [Language.from_dict(_item) for _item in obj.get("languages")] if obj.get("languages") is not None else None,
            "mapped_movie_id": obj.get("mappedMovieId"),
            "approved": obj.get("approved"),
            "temporarily_rejected": obj.get("temporarilyRejected"),
            "rejected": obj.get("rejected"),
            "tmdb_id": obj.get("tmdbId"),
            "imdb_id": obj.get("imdbId"),
            "rejections": obj.get("rejections"),
            "publish_date": obj.get("publishDate"),
            "comment_url": obj.get("commentUrl"),
            "download_url": obj.get("downloadUrl"),
            "info_url": obj.get("infoUrl"),
            "download_allowed": obj.get("downloadAllowed"),
            "release_weight": obj.get("releaseWeight"),
            "indexer_flags": obj.get("indexerFlags"),
            "edition": obj.get("edition"),
            "magnet_url": obj.get("magnetUrl"),
            "info_hash": obj.get("infoHash"),
            "seeders": obj.get("seeders"),
            "leechers": obj.get("leechers"),
            "protocol": obj.get("protocol"),
            "movie_id": obj.get("movieId"),
            "download_client_id": obj.get("downloadClientId"),
            "should_override": obj.get("shouldOverride")
        })
        return _obj

