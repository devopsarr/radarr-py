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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from radarr.models.contract_field import ContractField
from typing import Optional, Set
from typing_extensions import Self

class AutoTaggingSpecificationSchema(BaseModel):
    """
    AutoTaggingSpecificationSchema
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    implementation: Optional[StrictStr] = None
    implementation_name: Optional[StrictStr] = Field(default=None, alias="implementationName")
    negate: Optional[StrictBool] = None
    required: Optional[StrictBool] = None
    fields: Optional[List[ContractField]] = None
    __properties: ClassVar[List[str]] = ["id", "name", "implementation", "implementationName", "negate", "required", "fields"]

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
        """Create an instance of AutoTaggingSpecificationSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item_fields in self.fields:
                if _item_fields:
                    _items.append(_item_fields.to_dict())
            _dict['fields'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if implementation (nullable) is None
        # and model_fields_set contains the field
        if self.implementation is None and "implementation" in self.model_fields_set:
            _dict['implementation'] = None

        # set to None if implementation_name (nullable) is None
        # and model_fields_set contains the field
        if self.implementation_name is None and "implementation_name" in self.model_fields_set:
            _dict['implementationName'] = None

        # set to None if fields (nullable) is None
        # and model_fields_set contains the field
        if self.fields is None and "fields" in self.model_fields_set:
            _dict['fields'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AutoTaggingSpecificationSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "implementation": obj.get("implementation"),
            "implementationName": obj.get("implementationName"),
            "negate": obj.get("negate"),
            "required": obj.get("required"),
            "fields": [ContractField.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None
        })
        return _obj


