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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from radarr.models.source_type import SourceType
from typing import Optional, Set
from typing_extensions import Self

class AlternativeTitleResource(BaseModel):
    """
    AlternativeTitleResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    source_type: Optional[SourceType] = Field(default=None, alias="sourceType")
    movie_metadata_id: Optional[StrictInt] = Field(default=None, alias="movieMetadataId")
    title: Optional[StrictStr] = None
    clean_title: Optional[StrictStr] = Field(default=None, alias="cleanTitle")
    __properties: ClassVar[List[str]] = ["id", "sourceType", "movieMetadataId", "title", "cleanTitle"]

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
        """Create an instance of AlternativeTitleResource from a JSON string"""
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
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if clean_title (nullable) is None
        # and model_fields_set contains the field
        if self.clean_title is None and "clean_title" in self.model_fields_set:
            _dict['cleanTitle'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlternativeTitleResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "sourceType": obj.get("sourceType"),
            "movieMetadataId": obj.get("movieMetadataId"),
            "title": obj.get("title"),
            "cleanTitle": obj.get("cleanTitle")
        })
        return _obj


