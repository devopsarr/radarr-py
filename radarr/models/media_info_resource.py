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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class MediaInfoResource(BaseModel):
    """
    MediaInfoResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    audio_bitrate: Optional[StrictInt] = Field(default=None, alias="audioBitrate")
    audio_channels: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="audioChannels")
    audio_codec: Optional[StrictStr] = Field(default=None, alias="audioCodec")
    audio_languages: Optional[StrictStr] = Field(default=None, alias="audioLanguages")
    audio_stream_count: Optional[StrictInt] = Field(default=None, alias="audioStreamCount")
    video_bit_depth: Optional[StrictInt] = Field(default=None, alias="videoBitDepth")
    video_bitrate: Optional[StrictInt] = Field(default=None, alias="videoBitrate")
    video_codec: Optional[StrictStr] = Field(default=None, alias="videoCodec")
    video_fps: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="videoFps")
    video_dynamic_range: Optional[StrictStr] = Field(default=None, alias="videoDynamicRange")
    video_dynamic_range_type: Optional[StrictStr] = Field(default=None, alias="videoDynamicRangeType")
    resolution: Optional[StrictStr] = None
    run_time: Optional[StrictStr] = Field(default=None, alias="runTime")
    scan_type: Optional[StrictStr] = Field(default=None, alias="scanType")
    subtitles: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "audioBitrate", "audioChannels", "audioCodec", "audioLanguages", "audioStreamCount", "videoBitDepth", "videoBitrate", "videoCodec", "videoFps", "videoDynamicRange", "videoDynamicRangeType", "resolution", "runTime", "scanType", "subtitles"]

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
        """Create an instance of MediaInfoResource from a JSON string"""
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
        # set to None if audio_codec (nullable) is None
        # and model_fields_set contains the field
        if self.audio_codec is None and "audio_codec" in self.model_fields_set:
            _dict['audioCodec'] = None

        # set to None if audio_languages (nullable) is None
        # and model_fields_set contains the field
        if self.audio_languages is None and "audio_languages" in self.model_fields_set:
            _dict['audioLanguages'] = None

        # set to None if video_codec (nullable) is None
        # and model_fields_set contains the field
        if self.video_codec is None and "video_codec" in self.model_fields_set:
            _dict['videoCodec'] = None

        # set to None if video_dynamic_range (nullable) is None
        # and model_fields_set contains the field
        if self.video_dynamic_range is None and "video_dynamic_range" in self.model_fields_set:
            _dict['videoDynamicRange'] = None

        # set to None if video_dynamic_range_type (nullable) is None
        # and model_fields_set contains the field
        if self.video_dynamic_range_type is None and "video_dynamic_range_type" in self.model_fields_set:
            _dict['videoDynamicRangeType'] = None

        # set to None if resolution (nullable) is None
        # and model_fields_set contains the field
        if self.resolution is None and "resolution" in self.model_fields_set:
            _dict['resolution'] = None

        # set to None if run_time (nullable) is None
        # and model_fields_set contains the field
        if self.run_time is None and "run_time" in self.model_fields_set:
            _dict['runTime'] = None

        # set to None if scan_type (nullable) is None
        # and model_fields_set contains the field
        if self.scan_type is None and "scan_type" in self.model_fields_set:
            _dict['scanType'] = None

        # set to None if subtitles (nullable) is None
        # and model_fields_set contains the field
        if self.subtitles is None and "subtitles" in self.model_fields_set:
            _dict['subtitles'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MediaInfoResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "audioBitrate": obj.get("audioBitrate"),
            "audioChannels": obj.get("audioChannels"),
            "audioCodec": obj.get("audioCodec"),
            "audioLanguages": obj.get("audioLanguages"),
            "audioStreamCount": obj.get("audioStreamCount"),
            "videoBitDepth": obj.get("videoBitDepth"),
            "videoBitrate": obj.get("videoBitrate"),
            "videoCodec": obj.get("videoCodec"),
            "videoFps": obj.get("videoFps"),
            "videoDynamicRange": obj.get("videoDynamicRange"),
            "videoDynamicRangeType": obj.get("videoDynamicRangeType"),
            "resolution": obj.get("resolution"),
            "runTime": obj.get("runTime"),
            "scanType": obj.get("scanType"),
            "subtitles": obj.get("subtitles")
        })
        return _obj


