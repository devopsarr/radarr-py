# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from radarr.api.alternative_title_api import AlternativeTitleApi
    from radarr.api.api_info_api import ApiInfoApi
    from radarr.api.authentication_api import AuthenticationApi
    from radarr.api.auto_tagging_api import AutoTaggingApi
    from radarr.api.backup_api import BackupApi
    from radarr.api.blocklist_api import BlocklistApi
    from radarr.api.calendar_api import CalendarApi
    from radarr.api.calendar_feed_api import CalendarFeedApi
    from radarr.api.collection_api import CollectionApi
    from radarr.api.command_api import CommandApi
    from radarr.api.credit_api import CreditApi
    from radarr.api.custom_filter_api import CustomFilterApi
    from radarr.api.custom_format_api import CustomFormatApi
    from radarr.api.cutoff_api import CutoffApi
    from radarr.api.delay_profile_api import DelayProfileApi
    from radarr.api.disk_space_api import DiskSpaceApi
    from radarr.api.download_client_api import DownloadClientApi
    from radarr.api.download_client_config_api import DownloadClientConfigApi
    from radarr.api.extra_file_api import ExtraFileApi
    from radarr.api.file_system_api import FileSystemApi
    from radarr.api.health_api import HealthApi
    from radarr.api.history_api import HistoryApi
    from radarr.api.host_config_api import HostConfigApi
    from radarr.api.import_list_api import ImportListApi
    from radarr.api.import_list_config_api import ImportListConfigApi
    from radarr.api.import_list_exclusion_api import ImportListExclusionApi
    from radarr.api.import_list_movies_api import ImportListMoviesApi
    from radarr.api.indexer_api import IndexerApi
    from radarr.api.indexer_config_api import IndexerConfigApi
    from radarr.api.indexer_flag_api import IndexerFlagApi
    from radarr.api.language_api import LanguageApi
    from radarr.api.localization_api import LocalizationApi
    from radarr.api.log_api import LogApi
    from radarr.api.log_file_api import LogFileApi
    from radarr.api.manual_import_api import ManualImportApi
    from radarr.api.media_cover_api import MediaCoverApi
    from radarr.api.media_management_config_api import MediaManagementConfigApi
    from radarr.api.metadata_api import MetadataApi
    from radarr.api.metadata_config_api import MetadataConfigApi
    from radarr.api.missing_api import MissingApi
    from radarr.api.movie_api import MovieApi
    from radarr.api.movie_editor_api import MovieEditorApi
    from radarr.api.movie_file_api import MovieFileApi
    from radarr.api.movie_folder_api import MovieFolderApi
    from radarr.api.movie_import_api import MovieImportApi
    from radarr.api.movie_lookup_api import MovieLookupApi
    from radarr.api.naming_config_api import NamingConfigApi
    from radarr.api.notification_api import NotificationApi
    from radarr.api.parse_api import ParseApi
    from radarr.api.ping_api import PingApi
    from radarr.api.quality_definition_api import QualityDefinitionApi
    from radarr.api.quality_profile_api import QualityProfileApi
    from radarr.api.quality_profile_schema_api import QualityProfileSchemaApi
    from radarr.api.queue_api import QueueApi
    from radarr.api.queue_action_api import QueueActionApi
    from radarr.api.queue_details_api import QueueDetailsApi
    from radarr.api.queue_status_api import QueueStatusApi
    from radarr.api.release_api import ReleaseApi
    from radarr.api.release_profile_api import ReleaseProfileApi
    from radarr.api.release_push_api import ReleasePushApi
    from radarr.api.remote_path_mapping_api import RemotePathMappingApi
    from radarr.api.rename_movie_api import RenameMovieApi
    from radarr.api.root_folder_api import RootFolderApi
    from radarr.api.static_resource_api import StaticResourceApi
    from radarr.api.system_api import SystemApi
    from radarr.api.tag_api import TagApi
    from radarr.api.tag_details_api import TagDetailsApi
    from radarr.api.task_api import TaskApi
    from radarr.api.ui_config_api import UiConfigApi
    from radarr.api.update_api import UpdateApi
    from radarr.api.update_log_file_api import UpdateLogFileApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from radarr.api.alternative_title_api import AlternativeTitleApi
from radarr.api.api_info_api import ApiInfoApi
from radarr.api.authentication_api import AuthenticationApi
from radarr.api.auto_tagging_api import AutoTaggingApi
from radarr.api.backup_api import BackupApi
from radarr.api.blocklist_api import BlocklistApi
from radarr.api.calendar_api import CalendarApi
from radarr.api.calendar_feed_api import CalendarFeedApi
from radarr.api.collection_api import CollectionApi
from radarr.api.command_api import CommandApi
from radarr.api.credit_api import CreditApi
from radarr.api.custom_filter_api import CustomFilterApi
from radarr.api.custom_format_api import CustomFormatApi
from radarr.api.cutoff_api import CutoffApi
from radarr.api.delay_profile_api import DelayProfileApi
from radarr.api.disk_space_api import DiskSpaceApi
from radarr.api.download_client_api import DownloadClientApi
from radarr.api.download_client_config_api import DownloadClientConfigApi
from radarr.api.extra_file_api import ExtraFileApi
from radarr.api.file_system_api import FileSystemApi
from radarr.api.health_api import HealthApi
from radarr.api.history_api import HistoryApi
from radarr.api.host_config_api import HostConfigApi
from radarr.api.import_list_api import ImportListApi
from radarr.api.import_list_config_api import ImportListConfigApi
from radarr.api.import_list_exclusion_api import ImportListExclusionApi
from radarr.api.import_list_movies_api import ImportListMoviesApi
from radarr.api.indexer_api import IndexerApi
from radarr.api.indexer_config_api import IndexerConfigApi
from radarr.api.indexer_flag_api import IndexerFlagApi
from radarr.api.language_api import LanguageApi
from radarr.api.localization_api import LocalizationApi
from radarr.api.log_api import LogApi
from radarr.api.log_file_api import LogFileApi
from radarr.api.manual_import_api import ManualImportApi
from radarr.api.media_cover_api import MediaCoverApi
from radarr.api.media_management_config_api import MediaManagementConfigApi
from radarr.api.metadata_api import MetadataApi
from radarr.api.metadata_config_api import MetadataConfigApi
from radarr.api.missing_api import MissingApi
from radarr.api.movie_api import MovieApi
from radarr.api.movie_editor_api import MovieEditorApi
from radarr.api.movie_file_api import MovieFileApi
from radarr.api.movie_folder_api import MovieFolderApi
from radarr.api.movie_import_api import MovieImportApi
from radarr.api.movie_lookup_api import MovieLookupApi
from radarr.api.naming_config_api import NamingConfigApi
from radarr.api.notification_api import NotificationApi
from radarr.api.parse_api import ParseApi
from radarr.api.ping_api import PingApi
from radarr.api.quality_definition_api import QualityDefinitionApi
from radarr.api.quality_profile_api import QualityProfileApi
from radarr.api.quality_profile_schema_api import QualityProfileSchemaApi
from radarr.api.queue_api import QueueApi
from radarr.api.queue_action_api import QueueActionApi
from radarr.api.queue_details_api import QueueDetailsApi
from radarr.api.queue_status_api import QueueStatusApi
from radarr.api.release_api import ReleaseApi
from radarr.api.release_profile_api import ReleaseProfileApi
from radarr.api.release_push_api import ReleasePushApi
from radarr.api.remote_path_mapping_api import RemotePathMappingApi
from radarr.api.rename_movie_api import RenameMovieApi
from radarr.api.root_folder_api import RootFolderApi
from radarr.api.static_resource_api import StaticResourceApi
from radarr.api.system_api import SystemApi
from radarr.api.tag_api import TagApi
from radarr.api.tag_details_api import TagDetailsApi
from radarr.api.task_api import TaskApi
from radarr.api.ui_config_api import UiConfigApi
from radarr.api.update_api import UpdateApi
from radarr.api.update_log_file_api import UpdateLogFileApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
