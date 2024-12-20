# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.16.3.9541
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class MonitorTypes(str, Enum):
    """
    MonitorTypes
    """

    """
    allowed enum values
    """
    MOVIEONLY = 'movieOnly'
    MOVIEANDCOLLECTION = 'movieAndCollection'
    NONE = 'none'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MonitorTypes from a JSON string"""
        return cls(json.loads(json_str))


