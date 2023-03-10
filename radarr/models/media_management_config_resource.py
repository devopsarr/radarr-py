# coding: utf-8

"""
    Radarr

    Radarr API docs  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel
from radarr.models.file_date_type import FileDateType
from radarr.models.proper_download_types import ProperDownloadTypes
from radarr.models.rescan_after_refresh_type import RescanAfterRefreshType

class MediaManagementConfigResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    auto_unmonitor_previously_downloaded_movies: Optional[bool]
    recycle_bin: Optional[str]
    recycle_bin_cleanup_days: Optional[int]
    download_propers_and_repacks: Optional[ProperDownloadTypes]
    create_empty_movie_folders: Optional[bool]
    delete_empty_folders: Optional[bool]
    file_date: Optional[FileDateType]
    rescan_after_refresh: Optional[RescanAfterRefreshType]
    auto_rename_folders: Optional[bool]
    paths_default_static: Optional[bool]
    set_permissions_linux: Optional[bool]
    chmod_folder: Optional[str]
    chown_group: Optional[str]
    skip_free_space_check_when_importing: Optional[bool]
    minimum_free_space_when_importing: Optional[int]
    copy_using_hardlinks: Optional[bool]
    import_extra_files: Optional[bool]
    extra_file_extensions: Optional[str]
    enable_media_info: Optional[bool]
    __properties = ["id", "autoUnmonitorPreviouslyDownloadedMovies", "recycleBin", "recycleBinCleanupDays", "downloadPropersAndRepacks", "createEmptyMovieFolders", "deleteEmptyFolders", "fileDate", "rescanAfterRefresh", "autoRenameFolders", "pathsDefaultStatic", "setPermissionsLinux", "chmodFolder", "chownGroup", "skipFreeSpaceCheckWhenImporting", "minimumFreeSpaceWhenImporting", "copyUsingHardlinks", "importExtraFiles", "extraFileExtensions", "enableMediaInfo"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        alias_generator = lambda x: x.split("_")[0] + "".join(word.capitalize() for word in x.split("_")[1:])

    def __getitem__(self, item):
        return getattr(self, item)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> MediaManagementConfigResource:
        """Create an instance of MediaManagementConfigResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if recycle_bin (nullable) is None
        if self.recycle_bin is None:
            _dict['recycleBin'] = None

        # set to None if chmod_folder (nullable) is None
        if self.chmod_folder is None:
            _dict['chmodFolder'] = None

        # set to None if chown_group (nullable) is None
        if self.chown_group is None:
            _dict['chownGroup'] = None

        # set to None if extra_file_extensions (nullable) is None
        if self.extra_file_extensions is None:
            _dict['extraFileExtensions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MediaManagementConfigResource:
        """Create an instance of MediaManagementConfigResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MediaManagementConfigResource.parse_obj(obj)

        _obj = MediaManagementConfigResource.parse_obj({
            "id": obj.get("id"),
            "auto_unmonitor_previously_downloaded_movies": obj.get("autoUnmonitorPreviouslyDownloadedMovies"),
            "recycle_bin": obj.get("recycleBin"),
            "recycle_bin_cleanup_days": obj.get("recycleBinCleanupDays"),
            "download_propers_and_repacks": obj.get("downloadPropersAndRepacks"),
            "create_empty_movie_folders": obj.get("createEmptyMovieFolders"),
            "delete_empty_folders": obj.get("deleteEmptyFolders"),
            "file_date": obj.get("fileDate"),
            "rescan_after_refresh": obj.get("rescanAfterRefresh"),
            "auto_rename_folders": obj.get("autoRenameFolders"),
            "paths_default_static": obj.get("pathsDefaultStatic"),
            "set_permissions_linux": obj.get("setPermissionsLinux"),
            "chmod_folder": obj.get("chmodFolder"),
            "chown_group": obj.get("chownGroup"),
            "skip_free_space_check_when_importing": obj.get("skipFreeSpaceCheckWhenImporting"),
            "minimum_free_space_when_importing": obj.get("minimumFreeSpaceWhenImporting"),
            "copy_using_hardlinks": obj.get("copyUsingHardlinks"),
            "import_extra_files": obj.get("importExtraFiles"),
            "extra_file_extensions": obj.get("extraFileExtensions"),
            "enable_media_info": obj.get("enableMediaInfo")
        })
        return _obj

