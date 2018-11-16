from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def activate_gateway(self, ActivationKey: str, GatewayName: str, GatewayTimezone: str, GatewayRegion: str, GatewayType: str = None, TapeDriveType: str = None, MediumChangerType: str = None) -> Dict:
        pass

    def add_cache(self, GatewayARN: str, DiskIds: List) -> Dict:
        pass

    def add_tags_to_resource(self, ResourceARN: str, Tags: List) -> Dict:
        pass

    def add_upload_buffer(self, GatewayARN: str, DiskIds: List) -> Dict:
        pass

    def add_working_storage(self, GatewayARN: str, DiskIds: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def cancel_archival(self, GatewayARN: str, TapeARN: str) -> Dict:
        pass

    def cancel_retrieval(self, GatewayARN: str, TapeARN: str) -> Dict:
        pass

    def create_cached_iscsi_volume(self, GatewayARN: str, VolumeSizeInBytes: int, TargetName: str, NetworkInterfaceId: str, ClientToken: str, SnapshotId: str = None, SourceVolumeARN: str = None, KMSEncrypted: bool = None, KMSKey: str = None) -> Dict:
        pass

    def create_nfs_file_share(self, ClientToken: str, GatewayARN: str, Role: str, LocationARN: str, NFSFileShareDefaults: Dict = None, KMSEncrypted: bool = None, KMSKey: str = None, DefaultStorageClass: str = None, ObjectACL: str = None, ClientList: List = None, Squash: str = None, ReadOnly: bool = None, GuessMIMETypeEnabled: bool = None, RequesterPays: bool = None) -> Dict:
        pass

    def create_smb_file_share(self, ClientToken: str, GatewayARN: str, Role: str, LocationARN: str, KMSEncrypted: bool = None, KMSKey: str = None, DefaultStorageClass: str = None, ObjectACL: str = None, ReadOnly: bool = None, GuessMIMETypeEnabled: bool = None, RequesterPays: bool = None, ValidUserList: List = None, InvalidUserList: List = None, Authentication: str = None) -> Dict:
        pass

    def create_snapshot(self, VolumeARN: str, SnapshotDescription: str) -> Dict:
        pass

    def create_snapshot_from_volume_recovery_point(self, VolumeARN: str, SnapshotDescription: str) -> Dict:
        pass

    def create_stored_iscsi_volume(self, GatewayARN: str, DiskId: str, PreserveExistingData: bool, TargetName: str, NetworkInterfaceId: str, SnapshotId: str = None, KMSEncrypted: bool = None, KMSKey: str = None) -> Dict:
        pass

    def create_tape_with_barcode(self, GatewayARN: str, TapeSizeInBytes: int, TapeBarcode: str, KMSEncrypted: bool = None, KMSKey: str = None) -> Dict:
        pass

    def create_tapes(self, GatewayARN: str, TapeSizeInBytes: int, ClientToken: str, NumTapesToCreate: int, TapeBarcodePrefix: str, KMSEncrypted: bool = None, KMSKey: str = None) -> Dict:
        pass

    def delete_bandwidth_rate_limit(self, GatewayARN: str, BandwidthType: str) -> Dict:
        pass

    def delete_chap_credentials(self, TargetARN: str, InitiatorName: str) -> Dict:
        pass

    def delete_file_share(self, FileShareARN: str, ForceDelete: bool = None) -> Dict:
        pass

    def delete_gateway(self, GatewayARN: str) -> Dict:
        pass

    def delete_snapshot_schedule(self, VolumeARN: str) -> Dict:
        pass

    def delete_tape(self, GatewayARN: str, TapeARN: str) -> Dict:
        pass

    def delete_tape_archive(self, TapeARN: str) -> Dict:
        pass

    def delete_volume(self, VolumeARN: str) -> Dict:
        pass

    def describe_bandwidth_rate_limit(self, GatewayARN: str) -> Dict:
        pass

    def describe_cache(self, GatewayARN: str) -> Dict:
        pass

    def describe_cached_iscsi_volumes(self, VolumeARNs: List) -> Dict:
        pass

    def describe_chap_credentials(self, TargetARN: str) -> Dict:
        pass

    def describe_gateway_information(self, GatewayARN: str) -> Dict:
        pass

    def describe_maintenance_start_time(self, GatewayARN: str) -> Dict:
        pass

    def describe_nfs_file_shares(self, FileShareARNList: List) -> Dict:
        pass

    def describe_smb_file_shares(self, FileShareARNList: List) -> Dict:
        pass

    def describe_smb_settings(self, GatewayARN: str) -> Dict:
        pass

    def describe_snapshot_schedule(self, VolumeARN: str) -> Dict:
        pass

    def describe_stored_iscsi_volumes(self, VolumeARNs: List) -> Dict:
        pass

    def describe_tape_archives(self, TapeARNs: List = None, Marker: str = None, Limit: int = None) -> Dict:
        pass

    def describe_tape_recovery_points(self, GatewayARN: str, Marker: str = None, Limit: int = None) -> Dict:
        pass

    def describe_tapes(self, GatewayARN: str, TapeARNs: List = None, Marker: str = None, Limit: int = None) -> Dict:
        pass

    def describe_upload_buffer(self, GatewayARN: str) -> Dict:
        pass

    def describe_vtl_devices(self, GatewayARN: str, VTLDeviceARNs: List = None, Marker: str = None, Limit: int = None) -> Dict:
        pass

    def describe_working_storage(self, GatewayARN: str) -> Dict:
        pass

    def disable_gateway(self, GatewayARN: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def join_domain(self, GatewayARN: str, DomainName: str, UserName: str, Password: str) -> Dict:
        pass

    def list_file_shares(self, GatewayARN: str = None, Limit: int = None, Marker: str = None) -> Dict:
        pass

    def list_gateways(self, Marker: str = None, Limit: int = None) -> Dict:
        pass

    def list_local_disks(self, GatewayARN: str) -> Dict:
        pass

    def list_tags_for_resource(self, ResourceARN: str, Marker: str = None, Limit: int = None) -> Dict:
        pass

    def list_tapes(self, TapeARNs: List = None, Marker: str = None, Limit: int = None) -> Dict:
        pass

    def list_volume_initiators(self, VolumeARN: str) -> Dict:
        pass

    def list_volume_recovery_points(self, GatewayARN: str) -> Dict:
        pass

    def list_volumes(self, GatewayARN: str = None, Marker: str = None, Limit: int = None) -> Dict:
        pass

    def notify_when_uploaded(self, FileShareARN: str) -> Dict:
        pass

    def refresh_cache(self, FileShareARN: str, FolderList: List = None, Recursive: bool = None) -> Dict:
        pass

    def remove_tags_from_resource(self, ResourceARN: str, TagKeys: List) -> Dict:
        pass

    def reset_cache(self, GatewayARN: str) -> Dict:
        pass

    def retrieve_tape_archive(self, TapeARN: str, GatewayARN: str) -> Dict:
        pass

    def retrieve_tape_recovery_point(self, TapeARN: str, GatewayARN: str) -> Dict:
        pass

    def set_local_console_password(self, GatewayARN: str, LocalConsolePassword: str) -> Dict:
        pass

    def set_smb_guest_password(self, GatewayARN: str, Password: str) -> Dict:
        pass

    def shutdown_gateway(self, GatewayARN: str) -> Dict:
        pass

    def start_gateway(self, GatewayARN: str) -> Dict:
        pass

    def update_bandwidth_rate_limit(self, GatewayARN: str, AverageUploadRateLimitInBitsPerSec: int = None, AverageDownloadRateLimitInBitsPerSec: int = None) -> Dict:
        pass

    def update_chap_credentials(self, TargetARN: str, SecretToAuthenticateInitiator: str, InitiatorName: str, SecretToAuthenticateTarget: str = None) -> Dict:
        pass

    def update_gateway_information(self, GatewayARN: str, GatewayName: str = None, GatewayTimezone: str = None) -> Dict:
        pass

    def update_gateway_software_now(self, GatewayARN: str) -> Dict:
        pass

    def update_maintenance_start_time(self, GatewayARN: str, HourOfDay: int, MinuteOfHour: int, DayOfWeek: int) -> Dict:
        pass

    def update_nfs_file_share(self, FileShareARN: str, KMSEncrypted: bool = None, KMSKey: str = None, NFSFileShareDefaults: Dict = None, DefaultStorageClass: str = None, ObjectACL: str = None, ClientList: List = None, Squash: str = None, ReadOnly: bool = None, GuessMIMETypeEnabled: bool = None, RequesterPays: bool = None) -> Dict:
        pass

    def update_smb_file_share(self, FileShareARN: str, KMSEncrypted: bool = None, KMSKey: str = None, DefaultStorageClass: str = None, ObjectACL: str = None, ReadOnly: bool = None, GuessMIMETypeEnabled: bool = None, RequesterPays: bool = None, ValidUserList: List = None, InvalidUserList: List = None) -> Dict:
        pass

    def update_snapshot_schedule(self, VolumeARN: str, StartAt: int, RecurrenceInHours: int, Description: str = None) -> Dict:
        pass

    def update_vtl_device_type(self, VTLDeviceARN: str, DeviceType: str) -> Dict:
        pass
