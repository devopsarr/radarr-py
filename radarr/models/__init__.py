# coding: utf-8

# flake8: noqa
"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.2.6.8376
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from radarr.models.add_movie_method import AddMovieMethod
from radarr.models.add_movie_options import AddMovieOptions
from radarr.models.alternative_title import AlternativeTitle
from radarr.models.alternative_title_resource import AlternativeTitleResource
from radarr.models.api_info_resource import ApiInfoResource
from radarr.models.apply_tags import ApplyTags
from radarr.models.authentication_required_type import AuthenticationRequiredType
from radarr.models.authentication_type import AuthenticationType
from radarr.models.auto_tagging_resource import AutoTaggingResource
from radarr.models.auto_tagging_specification_schema import AutoTaggingSpecificationSchema
from radarr.models.backup_resource import BackupResource
from radarr.models.backup_type import BackupType
from radarr.models.blocklist_bulk_resource import BlocklistBulkResource
from radarr.models.blocklist_resource import BlocklistResource
from radarr.models.blocklist_resource_paging_resource import BlocklistResourcePagingResource
from radarr.models.certificate_validation_type import CertificateValidationType
from radarr.models.collection_movie_resource import CollectionMovieResource
from radarr.models.collection_resource import CollectionResource
from radarr.models.collection_update_resource import CollectionUpdateResource
from radarr.models.colon_replacement_format import ColonReplacementFormat
from radarr.models.command import Command
from radarr.models.command_priority import CommandPriority
from radarr.models.command_resource import CommandResource
from radarr.models.command_result import CommandResult
from radarr.models.command_status import CommandStatus
from radarr.models.command_trigger import CommandTrigger
from radarr.models.credit_resource import CreditResource
from radarr.models.credit_type import CreditType
from radarr.models.custom_filter_resource import CustomFilterResource
from radarr.models.custom_format_resource import CustomFormatResource
from radarr.models.custom_format_specification_schema import CustomFormatSpecificationSchema
from radarr.models.database_type import DatabaseType
from radarr.models.delay_profile_resource import DelayProfileResource
from radarr.models.disk_space_resource import DiskSpaceResource
from radarr.models.download_client_bulk_resource import DownloadClientBulkResource
from radarr.models.download_client_config_resource import DownloadClientConfigResource
from radarr.models.download_client_resource import DownloadClientResource
from radarr.models.download_protocol import DownloadProtocol
from radarr.models.extra_file_resource import ExtraFileResource
from radarr.models.extra_file_type import ExtraFileType
from radarr.models.field import Field
from radarr.models.file_date_type import FileDateType
from radarr.models.health_check_result import HealthCheckResult
from radarr.models.health_resource import HealthResource
from radarr.models.history_resource import HistoryResource
from radarr.models.history_resource_paging_resource import HistoryResourcePagingResource
from radarr.models.host_config_resource import HostConfigResource
from radarr.models.import_exclusions_resource import ImportExclusionsResource
from radarr.models.import_list_bulk_resource import ImportListBulkResource
from radarr.models.import_list_config_resource import ImportListConfigResource
from radarr.models.import_list_resource import ImportListResource
from radarr.models.import_list_type import ImportListType
from radarr.models.indexer_bulk_resource import IndexerBulkResource
from radarr.models.indexer_config_resource import IndexerConfigResource
from radarr.models.indexer_flag_resource import IndexerFlagResource
from radarr.models.indexer_resource import IndexerResource
from radarr.models.language import Language
from radarr.models.language_resource import LanguageResource
from radarr.models.localization_language_resource import LocalizationLanguageResource
from radarr.models.log_file_resource import LogFileResource
from radarr.models.log_resource import LogResource
from radarr.models.log_resource_paging_resource import LogResourcePagingResource
from radarr.models.manual_import_reprocess_resource import ManualImportReprocessResource
from radarr.models.manual_import_resource import ManualImportResource
from radarr.models.media_cover import MediaCover
from radarr.models.media_cover_types import MediaCoverTypes
from radarr.models.media_info_resource import MediaInfoResource
from radarr.models.media_management_config_resource import MediaManagementConfigResource
from radarr.models.metadata_config_resource import MetadataConfigResource
from radarr.models.metadata_resource import MetadataResource
from radarr.models.modifier import Modifier
from radarr.models.monitor_types import MonitorTypes
from radarr.models.movie_collection import MovieCollection
from radarr.models.movie_editor_resource import MovieEditorResource
from radarr.models.movie_file_list_resource import MovieFileListResource
from radarr.models.movie_file_resource import MovieFileResource
from radarr.models.movie_history_event_type import MovieHistoryEventType
from radarr.models.movie_metadata import MovieMetadata
from radarr.models.movie_resource import MovieResource
from radarr.models.movie_runtime_format_type import MovieRuntimeFormatType
from radarr.models.movie_status_type import MovieStatusType
from radarr.models.movie_translation import MovieTranslation
from radarr.models.naming_config_resource import NamingConfigResource
from radarr.models.notification_resource import NotificationResource
from radarr.models.parse_resource import ParseResource
from radarr.models.parsed_movie_info import ParsedMovieInfo
from radarr.models.ping_resource import PingResource
from radarr.models.privacy_level import PrivacyLevel
from radarr.models.profile_format_item_resource import ProfileFormatItemResource
from radarr.models.proper_download_types import ProperDownloadTypes
from radarr.models.provider_message import ProviderMessage
from radarr.models.provider_message_type import ProviderMessageType
from radarr.models.proxy_type import ProxyType
from radarr.models.quality import Quality
from radarr.models.quality_definition_resource import QualityDefinitionResource
from radarr.models.quality_model import QualityModel
from radarr.models.quality_profile_quality_item_resource import QualityProfileQualityItemResource
from radarr.models.quality_profile_resource import QualityProfileResource
from radarr.models.quality_source import QualitySource
from radarr.models.queue_bulk_resource import QueueBulkResource
from radarr.models.queue_resource import QueueResource
from radarr.models.queue_resource_paging_resource import QueueResourcePagingResource
from radarr.models.queue_status_resource import QueueStatusResource
from radarr.models.rating_child import RatingChild
from radarr.models.rating_type import RatingType
from radarr.models.ratings import Ratings
from radarr.models.rejection import Rejection
from radarr.models.rejection_type import RejectionType
from radarr.models.release_profile_resource import ReleaseProfileResource
from radarr.models.release_resource import ReleaseResource
from radarr.models.remote_path_mapping_resource import RemotePathMappingResource
from radarr.models.rename_movie_resource import RenameMovieResource
from radarr.models.rescan_after_refresh_type import RescanAfterRefreshType
from radarr.models.revision import Revision
from radarr.models.root_folder_resource import RootFolderResource
from radarr.models.runtime_mode import RuntimeMode
from radarr.models.select_option import SelectOption
from radarr.models.sort_direction import SortDirection
from radarr.models.source_type import SourceType
from radarr.models.system_resource import SystemResource
from radarr.models.tmdb_country_code import TMDbCountryCode
from radarr.models.tag_details_resource import TagDetailsResource
from radarr.models.tag_resource import TagResource
from radarr.models.task_resource import TaskResource
from radarr.models.tracked_download_state import TrackedDownloadState
from radarr.models.tracked_download_status import TrackedDownloadStatus
from radarr.models.tracked_download_status_message import TrackedDownloadStatusMessage
from radarr.models.ui_config_resource import UiConfigResource
from radarr.models.unmapped_folder import UnmappedFolder
from radarr.models.update_changes import UpdateChanges
from radarr.models.update_mechanism import UpdateMechanism
from radarr.models.update_resource import UpdateResource
