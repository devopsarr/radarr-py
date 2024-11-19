# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.15.1.9463
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, Optional
from radarr.models.rating_child import RatingChild
from typing import Optional, Set
from typing_extensions import Self

class Ratings(BaseModel):
    """
    Ratings
    """ # noqa: E501
    imdb: Optional[RatingChild] = None
    tmdb: Optional[RatingChild] = None
    metacritic: Optional[RatingChild] = None
    rotten_tomatoes: Optional[RatingChild] = Field(default=None, alias="rottenTomatoes")
    trakt: Optional[RatingChild] = None
    __properties: ClassVar[List[str]] = ["imdb", "tmdb", "metacritic", "rottenTomatoes", "trakt"]

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
        """Create an instance of Ratings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of imdb
        if self.imdb:
            _dict['imdb'] = self.imdb.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tmdb
        if self.tmdb:
            _dict['tmdb'] = self.tmdb.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metacritic
        if self.metacritic:
            _dict['metacritic'] = self.metacritic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rotten_tomatoes
        if self.rotten_tomatoes:
            _dict['rottenTomatoes'] = self.rotten_tomatoes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trakt
        if self.trakt:
            _dict['trakt'] = self.trakt.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Ratings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "imdb": RatingChild.from_dict(obj["imdb"]) if obj.get("imdb") is not None else None,
            "tmdb": RatingChild.from_dict(obj["tmdb"]) if obj.get("tmdb") is not None else None,
            "metacritic": RatingChild.from_dict(obj["metacritic"]) if obj.get("metacritic") is not None else None,
            "rottenTomatoes": RatingChild.from_dict(obj["rottenTomatoes"]) if obj.get("rottenTomatoes") is not None else None,
            "trakt": RatingChild.from_dict(obj["trakt"]) if obj.get("trakt") is not None else None
        })
        return _obj


