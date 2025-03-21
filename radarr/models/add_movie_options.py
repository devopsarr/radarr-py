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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, Optional
from radarr.models.add_movie_method import AddMovieMethod
from radarr.models.monitor_types import MonitorTypes
from typing import Optional, Set
from typing_extensions import Self

class AddMovieOptions(BaseModel):
    """
    AddMovieOptions
    """ # noqa: E501
    ignore_episodes_with_files: Optional[StrictBool] = Field(default=None, alias="ignoreEpisodesWithFiles")
    ignore_episodes_without_files: Optional[StrictBool] = Field(default=None, alias="ignoreEpisodesWithoutFiles")
    monitor: Optional[MonitorTypes] = None
    search_for_movie: Optional[StrictBool] = Field(default=None, alias="searchForMovie")
    add_method: Optional[AddMovieMethod] = Field(default=None, alias="addMethod")
    __properties: ClassVar[List[str]] = ["ignoreEpisodesWithFiles", "ignoreEpisodesWithoutFiles", "monitor", "searchForMovie", "addMethod"]

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
        """Create an instance of AddMovieOptions from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddMovieOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ignoreEpisodesWithFiles": obj.get("ignoreEpisodesWithFiles"),
            "ignoreEpisodesWithoutFiles": obj.get("ignoreEpisodesWithoutFiles"),
            "monitor": obj.get("monitor"),
            "searchForMovie": obj.get("searchForMovie"),
            "addMethod": obj.get("addMethod")
        })
        return _obj


