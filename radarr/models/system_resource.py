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

from datetime import datetime
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from radarr.models.authentication_type import AuthenticationType
from radarr.models.database_type import DatabaseType
from radarr.models.runtime_mode import RuntimeMode
from radarr.models.update_mechanism import UpdateMechanism
from typing import Optional, Set
from typing_extensions import Self

class SystemResource(BaseModel):
    """
    SystemResource
    """ # noqa: E501
    app_name: Optional[StrictStr] = Field(default=None, alias="appName")
    instance_name: Optional[StrictStr] = Field(default=None, alias="instanceName")
    version: Optional[StrictStr] = None
    build_time: Optional[datetime] = Field(default=None, alias="buildTime")
    is_debug: Optional[StrictBool] = Field(default=None, alias="isDebug")
    is_production: Optional[StrictBool] = Field(default=None, alias="isProduction")
    is_admin: Optional[StrictBool] = Field(default=None, alias="isAdmin")
    is_user_interactive: Optional[StrictBool] = Field(default=None, alias="isUserInteractive")
    startup_path: Optional[StrictStr] = Field(default=None, alias="startupPath")
    app_data: Optional[StrictStr] = Field(default=None, alias="appData")
    os_name: Optional[StrictStr] = Field(default=None, alias="osName")
    os_version: Optional[StrictStr] = Field(default=None, alias="osVersion")
    is_net_core: Optional[StrictBool] = Field(default=None, alias="isNetCore")
    is_linux: Optional[StrictBool] = Field(default=None, alias="isLinux")
    is_osx: Optional[StrictBool] = Field(default=None, alias="isOsx")
    is_windows: Optional[StrictBool] = Field(default=None, alias="isWindows")
    is_docker: Optional[StrictBool] = Field(default=None, alias="isDocker")
    mode: Optional[RuntimeMode] = None
    branch: Optional[StrictStr] = None
    database_type: Optional[DatabaseType] = Field(default=None, alias="databaseType")
    database_version: Optional[StrictStr] = Field(default=None, alias="databaseVersion")
    authentication: Optional[AuthenticationType] = None
    migration_version: Optional[StrictInt] = Field(default=None, alias="migrationVersion")
    url_base: Optional[StrictStr] = Field(default=None, alias="urlBase")
    runtime_version: Optional[StrictStr] = Field(default=None, alias="runtimeVersion")
    runtime_name: Optional[StrictStr] = Field(default=None, alias="runtimeName")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    package_version: Optional[StrictStr] = Field(default=None, alias="packageVersion")
    package_author: Optional[StrictStr] = Field(default=None, alias="packageAuthor")
    package_update_mechanism: Optional[UpdateMechanism] = Field(default=None, alias="packageUpdateMechanism")
    package_update_mechanism_message: Optional[StrictStr] = Field(default=None, alias="packageUpdateMechanismMessage")
    __properties: ClassVar[List[str]] = ["appName", "instanceName", "version", "buildTime", "isDebug", "isProduction", "isAdmin", "isUserInteractive", "startupPath", "appData", "osName", "osVersion", "isNetCore", "isLinux", "isOsx", "isWindows", "isDocker", "mode", "branch", "databaseType", "databaseVersion", "authentication", "migrationVersion", "urlBase", "runtimeVersion", "runtimeName", "startTime", "packageVersion", "packageAuthor", "packageUpdateMechanism", "packageUpdateMechanismMessage"]

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
        """Create an instance of SystemResource from a JSON string"""
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
        # set to None if app_name (nullable) is None
        # and model_fields_set contains the field
        if self.app_name is None and "app_name" in self.model_fields_set:
            _dict['appName'] = None

        # set to None if instance_name (nullable) is None
        # and model_fields_set contains the field
        if self.instance_name is None and "instance_name" in self.model_fields_set:
            _dict['instanceName'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        # set to None if startup_path (nullable) is None
        # and model_fields_set contains the field
        if self.startup_path is None and "startup_path" in self.model_fields_set:
            _dict['startupPath'] = None

        # set to None if app_data (nullable) is None
        # and model_fields_set contains the field
        if self.app_data is None and "app_data" in self.model_fields_set:
            _dict['appData'] = None

        # set to None if os_name (nullable) is None
        # and model_fields_set contains the field
        if self.os_name is None and "os_name" in self.model_fields_set:
            _dict['osName'] = None

        # set to None if os_version (nullable) is None
        # and model_fields_set contains the field
        if self.os_version is None and "os_version" in self.model_fields_set:
            _dict['osVersion'] = None

        # set to None if branch (nullable) is None
        # and model_fields_set contains the field
        if self.branch is None and "branch" in self.model_fields_set:
            _dict['branch'] = None

        # set to None if url_base (nullable) is None
        # and model_fields_set contains the field
        if self.url_base is None and "url_base" in self.model_fields_set:
            _dict['urlBase'] = None

        # set to None if runtime_name (nullable) is None
        # and model_fields_set contains the field
        if self.runtime_name is None and "runtime_name" in self.model_fields_set:
            _dict['runtimeName'] = None

        # set to None if package_version (nullable) is None
        # and model_fields_set contains the field
        if self.package_version is None and "package_version" in self.model_fields_set:
            _dict['packageVersion'] = None

        # set to None if package_author (nullable) is None
        # and model_fields_set contains the field
        if self.package_author is None and "package_author" in self.model_fields_set:
            _dict['packageAuthor'] = None

        # set to None if package_update_mechanism_message (nullable) is None
        # and model_fields_set contains the field
        if self.package_update_mechanism_message is None and "package_update_mechanism_message" in self.model_fields_set:
            _dict['packageUpdateMechanismMessage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SystemResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "appName": obj.get("appName"),
            "instanceName": obj.get("instanceName"),
            "version": obj.get("version"),
            "buildTime": obj.get("buildTime"),
            "isDebug": obj.get("isDebug"),
            "isProduction": obj.get("isProduction"),
            "isAdmin": obj.get("isAdmin"),
            "isUserInteractive": obj.get("isUserInteractive"),
            "startupPath": obj.get("startupPath"),
            "appData": obj.get("appData"),
            "osName": obj.get("osName"),
            "osVersion": obj.get("osVersion"),
            "isNetCore": obj.get("isNetCore"),
            "isLinux": obj.get("isLinux"),
            "isOsx": obj.get("isOsx"),
            "isWindows": obj.get("isWindows"),
            "isDocker": obj.get("isDocker"),
            "mode": obj.get("mode"),
            "branch": obj.get("branch"),
            "databaseType": obj.get("databaseType"),
            "databaseVersion": obj.get("databaseVersion"),
            "authentication": obj.get("authentication"),
            "migrationVersion": obj.get("migrationVersion"),
            "urlBase": obj.get("urlBase"),
            "runtimeVersion": obj.get("runtimeVersion"),
            "runtimeName": obj.get("runtimeName"),
            "startTime": obj.get("startTime"),
            "packageVersion": obj.get("packageVersion"),
            "packageAuthor": obj.get("packageAuthor"),
            "packageUpdateMechanism": obj.get("packageUpdateMechanism"),
            "packageUpdateMechanismMessage": obj.get("packageUpdateMechanismMessage")
        })
        return _obj


