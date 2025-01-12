# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.17.2.9580
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class MovieHistoryEventType(str, Enum):
    """
    MovieHistoryEventType
    """

    """
    allowed enum values
    """
    UNKNOWN = 'unknown'
    GRABBED = 'grabbed'
    DOWNLOADFOLDERIMPORTED = 'downloadFolderImported'
    DOWNLOADFAILED = 'downloadFailed'
    MOVIEFILEDELETED = 'movieFileDeleted'
    MOVIEFOLDERIMPORTED = 'movieFolderImported'
    MOVIEFILERENAMED = 'movieFileRenamed'
    DOWNLOADIGNORED = 'downloadIgnored'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MovieHistoryEventType from a JSON string"""
        return cls(json.loads(json_str))


