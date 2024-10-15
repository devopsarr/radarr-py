# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.12.2.9335
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ColonReplacementFormat(str, Enum):
    """
    ColonReplacementFormat
    """

    """
    allowed enum values
    """
    DELETE = 'delete'
    DASH = 'dash'
    SPACEDASH = 'spaceDash'
    SPACEDASHSPACE = 'spaceDashSpace'
    SMART = 'smart'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ColonReplacementFormat from a JSON string"""
        return cls(json.loads(json_str))


