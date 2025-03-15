# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.19.3.9730
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class MediaCoverTypes(str, Enum):
    """
    MediaCoverTypes
    """

    """
    allowed enum values
    """
    UNKNOWN = 'unknown'
    POSTER = 'poster'
    BANNER = 'banner'
    FANART = 'fanart'
    SCREENSHOT = 'screenshot'
    HEADSHOT = 'headshot'
    CLEARLOGO = 'clearlogo'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MediaCoverTypes from a JSON string"""
        return cls(json.loads(json_str))


