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
from radarr.models.apply_tags import ApplyTags
from radarr.models.movie_status_type import MovieStatusType
from typing import Optional, Set
from typing_extensions import Self

class ImportListBulkResource(BaseModel):
    """
    ImportListBulkResource
    """ # noqa: E501
    ids: Optional[List[StrictInt]] = None
    tags: Optional[List[StrictInt]] = None
    apply_tags: Optional[ApplyTags] = Field(default=None, alias="applyTags")
    enabled: Optional[StrictBool] = None
    enable_auto: Optional[StrictBool] = Field(default=None, alias="enableAuto")
    root_folder_path: Optional[StrictStr] = Field(default=None, alias="rootFolderPath")
    quality_profile_id: Optional[StrictInt] = Field(default=None, alias="qualityProfileId")
    minimum_availability: Optional[MovieStatusType] = Field(default=None, alias="minimumAvailability")
    __properties: ClassVar[List[str]] = ["ids", "tags", "applyTags", "enabled", "enableAuto", "rootFolderPath", "qualityProfileId", "minimumAvailability"]

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
        """Create an instance of ImportListBulkResource from a JSON string"""
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
        # set to None if ids (nullable) is None
        # and model_fields_set contains the field
        if self.ids is None and "ids" in self.model_fields_set:
            _dict['ids'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if enabled (nullable) is None
        # and model_fields_set contains the field
        if self.enabled is None and "enabled" in self.model_fields_set:
            _dict['enabled'] = None

        # set to None if enable_auto (nullable) is None
        # and model_fields_set contains the field
        if self.enable_auto is None and "enable_auto" in self.model_fields_set:
            _dict['enableAuto'] = None

        # set to None if root_folder_path (nullable) is None
        # and model_fields_set contains the field
        if self.root_folder_path is None and "root_folder_path" in self.model_fields_set:
            _dict['rootFolderPath'] = None

        # set to None if quality_profile_id (nullable) is None
        # and model_fields_set contains the field
        if self.quality_profile_id is None and "quality_profile_id" in self.model_fields_set:
            _dict['qualityProfileId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ImportListBulkResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ids": obj.get("ids"),
            "tags": obj.get("tags"),
            "applyTags": obj.get("applyTags"),
            "enabled": obj.get("enabled"),
            "enableAuto": obj.get("enableAuto"),
            "rootFolderPath": obj.get("rootFolderPath"),
            "qualityProfileId": obj.get("qualityProfileId"),
            "minimumAvailability": obj.get("minimumAvailability")
        })
        return _obj


