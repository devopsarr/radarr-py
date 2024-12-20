# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.16.3.9541
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class IndexerConfigResource(BaseModel):
    """
    IndexerConfigResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    minimum_age: Optional[StrictInt] = Field(default=None, alias="minimumAge")
    maximum_size: Optional[StrictInt] = Field(default=None, alias="maximumSize")
    retention: Optional[StrictInt] = None
    rss_sync_interval: Optional[StrictInt] = Field(default=None, alias="rssSyncInterval")
    prefer_indexer_flags: Optional[StrictBool] = Field(default=None, alias="preferIndexerFlags")
    availability_delay: Optional[StrictInt] = Field(default=None, alias="availabilityDelay")
    allow_hardcoded_subs: Optional[StrictBool] = Field(default=None, alias="allowHardcodedSubs")
    whitelisted_hardcoded_subs: Optional[StrictStr] = Field(default=None, alias="whitelistedHardcodedSubs")
    __properties: ClassVar[List[str]] = ["id", "minimumAge", "maximumSize", "retention", "rssSyncInterval", "preferIndexerFlags", "availabilityDelay", "allowHardcodedSubs", "whitelistedHardcodedSubs"]

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
        """Create an instance of IndexerConfigResource from a JSON string"""
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
        # set to None if whitelisted_hardcoded_subs (nullable) is None
        # and model_fields_set contains the field
        if self.whitelisted_hardcoded_subs is None and "whitelisted_hardcoded_subs" in self.model_fields_set:
            _dict['whitelistedHardcodedSubs'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndexerConfigResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "minimumAge": obj.get("minimumAge"),
            "maximumSize": obj.get("maximumSize"),
            "retention": obj.get("retention"),
            "rssSyncInterval": obj.get("rssSyncInterval"),
            "preferIndexerFlags": obj.get("preferIndexerFlags"),
            "availabilityDelay": obj.get("availabilityDelay"),
            "allowHardcodedSubs": obj.get("allowHardcodedSubs"),
            "whitelistedHardcodedSubs": obj.get("whitelistedHardcodedSubs")
        })
        return _obj


