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


class AuthenticationType(str, Enum):
    """
    AuthenticationType
    """

    """
    allowed enum values
    """
    NONE = 'none'
    BASIC = 'basic'
    FORMS = 'forms'
    EXTERNAL = 'external'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AuthenticationType from a JSON string"""
        return cls(json.loads(json_str))


