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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class DownloadClientConfigResource(BaseModel):
    """
    DownloadClientConfigResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    download_client_working_folders: Optional[StrictStr] = Field(default=None, alias="downloadClientWorkingFolders")
    enable_completed_download_handling: Optional[StrictBool] = Field(default=None, alias="enableCompletedDownloadHandling")
    check_for_finished_download_interval: Optional[StrictInt] = Field(default=None, alias="checkForFinishedDownloadInterval")
    auto_redownload_failed: Optional[StrictBool] = Field(default=None, alias="autoRedownloadFailed")
    auto_redownload_failed_from_interactive_search: Optional[StrictBool] = Field(default=None, alias="autoRedownloadFailedFromInteractiveSearch")
    __properties: ClassVar[List[str]] = ["id", "downloadClientWorkingFolders", "enableCompletedDownloadHandling", "checkForFinishedDownloadInterval", "autoRedownloadFailed", "autoRedownloadFailedFromInteractiveSearch"]

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
        """Create an instance of DownloadClientConfigResource from a JSON string"""
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
        # set to None if download_client_working_folders (nullable) is None
        # and model_fields_set contains the field
        if self.download_client_working_folders is None and "download_client_working_folders" in self.model_fields_set:
            _dict['downloadClientWorkingFolders'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DownloadClientConfigResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "downloadClientWorkingFolders": obj.get("downloadClientWorkingFolders"),
            "enableCompletedDownloadHandling": obj.get("enableCompletedDownloadHandling"),
            "checkForFinishedDownloadInterval": obj.get("checkForFinishedDownloadInterval"),
            "autoRedownloadFailed": obj.get("autoRedownloadFailed"),
            "autoRedownloadFailedFromInteractiveSearch": obj.get("autoRedownloadFailedFromInteractiveSearch")
        })
        return _obj


