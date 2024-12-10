# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.15.1.9463
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class QualitySource(str, Enum):
    """
    QualitySource
    """

    """
    allowed enum values
    """
    UNKNOWN = 'unknown'
    CAM = 'cam'
    TELESYNC = 'telesync'
    TELECINE = 'telecine'
    WORKPRINT = 'workprint'
    DVD = 'dvd'
    TV = 'tv'
    WEBDL = 'webdl'
    WEBRIP = 'webrip'
    BLURAY = 'bluray'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of QualitySource from a JSON string"""
        return cls(json.loads(json_str))


