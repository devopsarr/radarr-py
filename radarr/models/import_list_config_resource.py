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

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class ImportListConfigResource(BaseModel):
    """
    ImportListConfigResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    list_sync_level: Optional[StrictStr] = Field(default=None, alias="listSyncLevel")
    import_exclusions: Optional[StrictStr] = Field(default=None, alias="importExclusions")
    __properties: ClassVar[List[str]] = ["id", "listSyncLevel", "importExclusions"]

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
        """Create an instance of ImportListConfigResource from a JSON string"""
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
        # set to None if list_sync_level (nullable) is None
        # and model_fields_set contains the field
        if self.list_sync_level is None and "list_sync_level" in self.model_fields_set:
            _dict['listSyncLevel'] = None

        # set to None if import_exclusions (nullable) is None
        # and model_fields_set contains the field
        if self.import_exclusions is None and "import_exclusions" in self.model_fields_set:
            _dict['importExclusions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ImportListConfigResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "listSyncLevel": obj.get("listSyncLevel"),
            "importExclusions": obj.get("importExclusions")
        })
        return _obj


