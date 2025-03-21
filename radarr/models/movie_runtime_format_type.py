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


class MovieRuntimeFormatType(str, Enum):
    """
    MovieRuntimeFormatType
    """

    """
    allowed enum values
    """
    HOURSMINUTES = 'hoursMinutes'
    MINUTES = 'minutes'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MovieRuntimeFormatType from a JSON string"""
        return cls(json.loads(json_str))


