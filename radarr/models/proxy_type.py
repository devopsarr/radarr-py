# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.4.6.8723
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ProxyType(str, Enum):
    """
    ProxyType
    """

    """
    allowed enum values
    """
    HTTP = 'http'
    SOCKS4 = 'socks4'
    SOCKS5 = 'socks5'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProxyType from a JSON string"""
        return cls(json.loads(json_str))


