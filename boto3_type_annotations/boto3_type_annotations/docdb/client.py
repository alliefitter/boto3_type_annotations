from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from datetime import datetime
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def add_tags_to_resource(self, ResourceName: str, Tags: List):
        pass

    def apply_pending_maintenance_action(self, ResourceIdentifier: str, ApplyAction: str, OptInType: str) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def copy_db_cluster_parameter_group(self, SourceDBClusterParameterGroupIdentifier: str, TargetDBClusterParameterGroupIdentifier: str, TargetDBClusterParameterGroupDescription: str, Tags: List = None) -> Dict:
        pass

    def copy_db_cluster_snapshot(self, SourceDBClusterSnapshotIdentifier: str, TargetDBClusterSnapshotIdentifier: str, KmsKeyId: str = None, PreSignedUrl: str = None, CopyTags: bool = None, Tags: List = None) -> Dict:
        pass

    def create_db_cluster(self, DBClusterIdentifier: str, Engine: str, AvailabilityZones: List = None, BackupRetentionPeriod: int = None, DBClusterParameterGroupName: str = None, VpcSecurityGroupIds: List = None, DBSubnetGroupName: str = None, EngineVersion: str = None, Port: int = None, MasterUsername: str = None, MasterUserPassword: str = None, PreferredBackupWindow: str = None, PreferredMaintenanceWindow: str = None, Tags: List = None, StorageEncrypted: bool = None, KmsKeyId: str = None, EnableCloudwatchLogsExports: List = None) -> Dict:
        pass

    def create_db_cluster_parameter_group(self, DBClusterParameterGroupName: str, DBParameterGroupFamily: str, Description: str, Tags: List = None) -> Dict:
        pass

    def create_db_cluster_snapshot(self, DBClusterSnapshotIdentifier: str, DBClusterIdentifier: str, Tags: List = None) -> Dict:
        pass

    def create_db_instance(self, DBInstanceIdentifier: str, DBInstanceClass: str, Engine: str, DBClusterIdentifier: str, AvailabilityZone: str = None, PreferredMaintenanceWindow: str = None, AutoMinorVersionUpgrade: bool = None, Tags: List = None, PromotionTier: int = None) -> Dict:
        pass

    def create_db_subnet_group(self, DBSubnetGroupName: str, DBSubnetGroupDescription: str, SubnetIds: List, Tags: List = None) -> Dict:
        pass

    def delete_db_cluster(self, DBClusterIdentifier: str, SkipFinalSnapshot: bool = None, FinalDBSnapshotIdentifier: str = None) -> Dict:
        pass

    def delete_db_cluster_parameter_group(self, DBClusterParameterGroupName: str):
        pass

    def delete_db_cluster_snapshot(self, DBClusterSnapshotIdentifier: str) -> Dict:
        pass

    def delete_db_instance(self, DBInstanceIdentifier: str) -> Dict:
        pass

    def delete_db_subnet_group(self, DBSubnetGroupName: str):
        pass

    def describe_db_cluster_parameter_groups(self, DBClusterParameterGroupName: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_db_cluster_parameters(self, DBClusterParameterGroupName: str, Source: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_db_cluster_snapshot_attributes(self, DBClusterSnapshotIdentifier: str) -> Dict:
        pass

    def describe_db_cluster_snapshots(self, DBClusterIdentifier: str = None, DBClusterSnapshotIdentifier: str = None, SnapshotType: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, IncludeShared: bool = None, IncludePublic: bool = None) -> Dict:
        pass

    def describe_db_clusters(self, DBClusterIdentifier: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_db_engine_versions(self, Engine: str = None, EngineVersion: str = None, DBParameterGroupFamily: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, DefaultOnly: bool = None, ListSupportedCharacterSets: bool = None, ListSupportedTimezones: bool = None) -> Dict:
        pass

    def describe_db_instances(self, DBInstanceIdentifier: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_db_subnet_groups(self, DBSubnetGroupName: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_engine_default_cluster_parameters(self, DBParameterGroupFamily: str, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_event_categories(self, SourceType: str = None, Filters: List = None) -> Dict:
        pass

    def describe_events(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, EventCategories: List = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_orderable_db_instance_options(self, Engine: str, EngineVersion: str = None, DBInstanceClass: str = None, LicenseModel: str = None, Vpc: bool = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_pending_maintenance_actions(self, ResourceIdentifier: str = None, Filters: List = None, Marker: str = None, MaxRecords: int = None) -> Dict:
        pass

    def failover_db_cluster(self, DBClusterIdentifier: str = None, TargetDBInstanceIdentifier: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_tags_for_resource(self, ResourceName: str, Filters: List = None) -> Dict:
        pass

    def modify_db_cluster(self, DBClusterIdentifier: str, NewDBClusterIdentifier: str = None, ApplyImmediately: bool = None, BackupRetentionPeriod: int = None, DBClusterParameterGroupName: str = None, VpcSecurityGroupIds: List = None, Port: int = None, MasterUserPassword: str = None, PreferredBackupWindow: str = None, PreferredMaintenanceWindow: str = None, CloudwatchLogsExportConfiguration: Dict = None, EngineVersion: str = None) -> Dict:
        pass

    def modify_db_cluster_parameter_group(self, DBClusterParameterGroupName: str, Parameters: List) -> Dict:
        pass

    def modify_db_cluster_snapshot_attribute(self, DBClusterSnapshotIdentifier: str, AttributeName: str, ValuesToAdd: List = None, ValuesToRemove: List = None) -> Dict:
        pass

    def modify_db_instance(self, DBInstanceIdentifier: str, DBInstanceClass: str = None, ApplyImmediately: bool = None, PreferredMaintenanceWindow: str = None, AutoMinorVersionUpgrade: bool = None, NewDBInstanceIdentifier: str = None, PromotionTier: int = None) -> Dict:
        pass

    def modify_db_subnet_group(self, DBSubnetGroupName: str, SubnetIds: List, DBSubnetGroupDescription: str = None) -> Dict:
        pass

    def reboot_db_instance(self, DBInstanceIdentifier: str, ForceFailover: bool = None) -> Dict:
        pass

    def remove_tags_from_resource(self, ResourceName: str, TagKeys: List):
        pass

    def reset_db_cluster_parameter_group(self, DBClusterParameterGroupName: str, ResetAllParameters: bool = None, Parameters: List = None) -> Dict:
        pass

    def restore_db_cluster_from_snapshot(self, DBClusterIdentifier: str, SnapshotIdentifier: str, Engine: str, AvailabilityZones: List = None, EngineVersion: str = None, Port: int = None, DBSubnetGroupName: str = None, VpcSecurityGroupIds: List = None, Tags: List = None, KmsKeyId: str = None, EnableCloudwatchLogsExports: List = None) -> Dict:
        pass

    def restore_db_cluster_to_point_in_time(self, DBClusterIdentifier: str, SourceDBClusterIdentifier: str, RestoreToTime: datetime = None, UseLatestRestorableTime: bool = None, Port: int = None, DBSubnetGroupName: str = None, VpcSecurityGroupIds: List = None, Tags: List = None, KmsKeyId: str = None, EnableCloudwatchLogsExports: List = None) -> Dict:
        pass
