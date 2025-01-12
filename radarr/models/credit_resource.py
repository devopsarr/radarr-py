# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.17.2.9580
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from radarr.models.credit_type import CreditType
from radarr.models.media_cover import MediaCover
from typing import Optional, Set
from typing_extensions import Self

class CreditResource(BaseModel):
    """
    CreditResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    person_name: Optional[StrictStr] = Field(default=None, alias="personName")
    credit_tmdb_id: Optional[StrictStr] = Field(default=None, alias="creditTmdbId")
    person_tmdb_id: Optional[StrictInt] = Field(default=None, alias="personTmdbId")
    movie_metadata_id: Optional[StrictInt] = Field(default=None, alias="movieMetadataId")
    images: Optional[List[MediaCover]] = None
    department: Optional[StrictStr] = None
    job: Optional[StrictStr] = None
    character: Optional[StrictStr] = None
    order: Optional[StrictInt] = None
    type: Optional[CreditType] = None
    __properties: ClassVar[List[str]] = ["id", "personName", "creditTmdbId", "personTmdbId", "movieMetadataId", "images", "department", "job", "character", "order", "type"]

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
        """Create an instance of CreditResource from a JSON string"""
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
        # set to None if person_name (nullable) is None
        # and model_fields_set contains the field
        if self.person_name is None and "person_name" in self.model_fields_set:
            _dict['personName'] = None

        # set to None if credit_tmdb_id (nullable) is None
        # and model_fields_set contains the field
        if self.credit_tmdb_id is None and "credit_tmdb_id" in self.model_fields_set:
            _dict['creditTmdbId'] = None

        # set to None if images (nullable) is None
        # and model_fields_set contains the field
        if self.images is None and "images" in self.model_fields_set:
            _dict['images'] = None

        # set to None if department (nullable) is None
        # and model_fields_set contains the field
        if self.department is None and "department" in self.model_fields_set:
            _dict['department'] = None

        # set to None if job (nullable) is None
        # and model_fields_set contains the field
        if self.job is None and "job" in self.model_fields_set:
            _dict['job'] = None

        # set to None if character (nullable) is None
        # and model_fields_set contains the field
        if self.character is None and "character" in self.model_fields_set:
            _dict['character'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreditResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "personName": obj.get("personName"),
            "creditTmdbId": obj.get("creditTmdbId"),
            "personTmdbId": obj.get("personTmdbId"),
            "movieMetadataId": obj.get("movieMetadataId"),
            "images": [MediaCover.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "department": obj.get("department"),
            "job": obj.get("job"),
            "character": obj.get("character"),
            "order": obj.get("order"),
            "type": obj.get("type")
        })
        return _obj


