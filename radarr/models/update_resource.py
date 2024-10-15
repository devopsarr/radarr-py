# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.12.2.9335
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from radarr.models.update_changes import UpdateChanges
from typing import Optional, Set
from typing_extensions import Self

class UpdateResource(BaseModel):
    """
    UpdateResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    version: Optional[StrictStr] = None
    branch: Optional[StrictStr] = None
    release_date: Optional[datetime] = Field(default=None, alias="releaseDate")
    file_name: Optional[StrictStr] = Field(default=None, alias="fileName")
    url: Optional[StrictStr] = None
    installed: Optional[StrictBool] = None
    installed_on: Optional[datetime] = Field(default=None, alias="installedOn")
    installable: Optional[StrictBool] = None
    latest: Optional[StrictBool] = None
    changes: Optional[UpdateChanges] = None
    hash: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "version", "branch", "releaseDate", "fileName", "url", "installed", "installedOn", "installable", "latest", "changes", "hash"]

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
        """Create an instance of UpdateResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of changes
        if self.changes:
            _dict['changes'] = self.changes.to_dict()
        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        # set to None if branch (nullable) is None
        # and model_fields_set contains the field
        if self.branch is None and "branch" in self.model_fields_set:
            _dict['branch'] = None

        # set to None if file_name (nullable) is None
        # and model_fields_set contains the field
        if self.file_name is None and "file_name" in self.model_fields_set:
            _dict['fileName'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if installed_on (nullable) is None
        # and model_fields_set contains the field
        if self.installed_on is None and "installed_on" in self.model_fields_set:
            _dict['installedOn'] = None

        # set to None if hash (nullable) is None
        # and model_fields_set contains the field
        if self.hash is None and "hash" in self.model_fields_set:
            _dict['hash'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "version": obj.get("version"),
            "branch": obj.get("branch"),
            "releaseDate": obj.get("releaseDate"),
            "fileName": obj.get("fileName"),
            "url": obj.get("url"),
            "installed": obj.get("installed"),
            "installedOn": obj.get("installedOn"),
            "installable": obj.get("installable"),
            "latest": obj.get("latest"),
            "changes": UpdateChanges.from_dict(obj["changes"]) if obj.get("changes") is not None else None,
            "hash": obj.get("hash")
        })
        return _obj


