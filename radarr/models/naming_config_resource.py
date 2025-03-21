# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.19.3.9730
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from radarr.models.colon_replacement_format import ColonReplacementFormat
from typing import Optional, Set
from typing_extensions import Self

class NamingConfigResource(BaseModel):
    """
    NamingConfigResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    rename_movies: Optional[StrictBool] = Field(default=None, alias="renameMovies")
    replace_illegal_characters: Optional[StrictBool] = Field(default=None, alias="replaceIllegalCharacters")
    colon_replacement_format: Optional[ColonReplacementFormat] = Field(default=None, alias="colonReplacementFormat")
    standard_movie_format: Optional[StrictStr] = Field(default=None, alias="standardMovieFormat")
    movie_folder_format: Optional[StrictStr] = Field(default=None, alias="movieFolderFormat")
    __properties: ClassVar[List[str]] = ["id", "renameMovies", "replaceIllegalCharacters", "colonReplacementFormat", "standardMovieFormat", "movieFolderFormat"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of NamingConfigResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if standard_movie_format (nullable) is None
        # and model_fields_set contains the field
        if self.standard_movie_format is None and "standard_movie_format" in self.model_fields_set:
            _dict['standardMovieFormat'] = None

        # set to None if movie_folder_format (nullable) is None
        # and model_fields_set contains the field
        if self.movie_folder_format is None and "movie_folder_format" in self.model_fields_set:
            _dict['movieFolderFormat'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NamingConfigResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "renameMovies": obj.get("renameMovies"),
            "replaceIllegalCharacters": obj.get("replaceIllegalCharacters"),
            "colonReplacementFormat": obj.get("colonReplacementFormat"),
            "standardMovieFormat": obj.get("standardMovieFormat"),
            "movieFolderFormat": obj.get("movieFolderFormat")
        })
        return _obj


