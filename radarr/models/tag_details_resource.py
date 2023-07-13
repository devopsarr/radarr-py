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


from typing import List, Optional
from pydantic import BaseModel

class TagDetailsResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    label: Optional[str]
    delay_profile_ids: Optional[List]
    notification_ids: Optional[List]
    restriction_ids: Optional[List]
    import_list_ids: Optional[List]
    movie_ids: Optional[List]
    indexer_ids: Optional[List]
    download_client_ids: Optional[List]
    __properties = ["id", "label", "delayProfileIds", "notificationIds", "restrictionIds", "importListIds", "movieIds", "indexerIds", "downloadClientIds"]

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
    def from_json(cls, json_str: str) -> TagDetailsResource:
        """Create an instance of TagDetailsResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if label (nullable) is None
        if self.label is None:
            _dict['label'] = None

        # set to None if delay_profile_ids (nullable) is None
        if self.delay_profile_ids is None:
            _dict['delayProfileIds'] = None

        # set to None if notification_ids (nullable) is None
        if self.notification_ids is None:
            _dict['notificationIds'] = None

        # set to None if restriction_ids (nullable) is None
        if self.restriction_ids is None:
            _dict['restrictionIds'] = None

        # set to None if import_list_ids (nullable) is None
        if self.import_list_ids is None:
            _dict['importListIds'] = None

        # set to None if movie_ids (nullable) is None
        if self.movie_ids is None:
            _dict['movieIds'] = None

        # set to None if indexer_ids (nullable) is None
        if self.indexer_ids is None:
            _dict['indexerIds'] = None

        # set to None if download_client_ids (nullable) is None
        if self.download_client_ids is None:
            _dict['downloadClientIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TagDetailsResource:
        """Create an instance of TagDetailsResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TagDetailsResource.parse_obj(obj)

        _obj = TagDetailsResource.parse_obj({
            "id": obj.get("id"),
            "label": obj.get("label"),
            "delay_profile_ids": obj.get("delayProfileIds"),
            "notification_ids": obj.get("notificationIds"),
            "restriction_ids": obj.get("restrictionIds"),
            "import_list_ids": obj.get("importListIds"),
            "movie_ids": obj.get("movieIds"),
            "indexer_ids": obj.get("indexerIds"),
            "download_client_ids": obj.get("downloadClientIds")
        })
        return _obj

