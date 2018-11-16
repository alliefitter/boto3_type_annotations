from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def add_role_to_db_cluster(self, DBClusterIdentifier: str, RoleArn: str):
        pass

    def add_source_identifier_to_subscription(self, SubscriptionName: str, SourceIdentifier: str) -> Dict:
        pass

    def add_tags_to_resource(self, ResourceName: str, Tags: List):
        pass

    def apply_pending_maintenance_action(self, ResourceIdentifier: str, ApplyAction: str, OptInType: str) -> Dict:
        pass

    def authorize_db_security_group_ingress(self, DBSecurityGroupName: str, CIDRIP: str = None, EC2SecurityGroupName: str = None, EC2SecurityGroupId: str = None, EC2SecurityGroupOwnerId: str = None) -> Dict:
        pass

    def backtrack_db_cluster(self, DBClusterIdentifier: str, BacktrackTo: datetime, Force: bool = None, UseEarliestTimeOnPointInTimeUnavailable: bool = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def copy_db_cluster_parameter_group(self, SourceDBClusterParameterGroupIdentifier: str, TargetDBClusterParameterGroupIdentifier: str, TargetDBClusterParameterGroupDescription: str, Tags: List = None) -> Dict:
        pass

    def copy_db_cluster_snapshot(self, SourceDBClusterSnapshotIdentifier: str, TargetDBClusterSnapshotIdentifier: str, KmsKeyId: str = None, PreSignedUrl: str = None, CopyTags: bool = None, Tags: List = None, SourceRegion: str = None) -> Dict:
        pass

    def copy_db_parameter_group(self, SourceDBParameterGroupIdentifier: str, TargetDBParameterGroupIdentifier: str, TargetDBParameterGroupDescription: str, Tags: List = None) -> Dict:
        pass

    def copy_db_snapshot(self, SourceDBSnapshotIdentifier: str, TargetDBSnapshotIdentifier: str, KmsKeyId: str = None, Tags: List = None, CopyTags: bool = None, PreSignedUrl: str = None, OptionGroupName: str = None, SourceRegion: str = None) -> Dict:
        pass

    def copy_option_group(self, SourceOptionGroupIdentifier: str, TargetOptionGroupIdentifier: str, TargetOptionGroupDescription: str, Tags: List = None) -> Dict:
        pass

    def create_db_cluster(self, DBClusterIdentifier: str, Engine: str, AvailabilityZones: List = None, BackupRetentionPeriod: int = None, CharacterSetName: str = None, DatabaseName: str = None, DBClusterParameterGroupName: str = None, VpcSecurityGroupIds: List = None, DBSubnetGroupName: str = None, EngineVersion: str = None, Port: int = None, MasterUsername: str = None, MasterUserPassword: str = None, OptionGroupName: str = None, PreferredBackupWindow: str = None, PreferredMaintenanceWindow: str = None, ReplicationSourceIdentifier: str = None, Tags: List = None, StorageEncrypted: bool = None, KmsKeyId: str = None, PreSignedUrl: str = None, EnableIAMDatabaseAuthentication: bool = None, BacktrackWindow: int = None, EnableCloudwatchLogsExports: List = None, EngineMode: str = None, ScalingConfiguration: Dict = None, DeletionProtection: bool = None, SourceRegion: str = None) -> Dict:
        pass

    def create_db_cluster_endpoint(self, DBClusterIdentifier: str, DBClusterEndpointIdentifier: str, EndpointType: str, StaticMembers: List = None, ExcludedMembers: List = None) -> Dict:
        pass

    def create_db_cluster_parameter_group(self, DBClusterParameterGroupName: str, DBParameterGroupFamily: str, Description: str, Tags: List = None) -> Dict:
        pass

    def create_db_cluster_snapshot(self, DBClusterSnapshotIdentifier: str, DBClusterIdentifier: str, Tags: List = None) -> Dict:
        pass

    def create_db_instance(self, DBInstanceIdentifier: str, DBInstanceClass: str, Engine: str, DBName: str = None, AllocatedStorage: int = None, MasterUsername: str = None, MasterUserPassword: str = None, DBSecurityGroups: List = None, VpcSecurityGroupIds: List = None, AvailabilityZone: str = None, DBSubnetGroupName: str = None, PreferredMaintenanceWindow: str = None, DBParameterGroupName: str = None, BackupRetentionPeriod: int = None, PreferredBackupWindow: str = None, Port: int = None, MultiAZ: bool = None, EngineVersion: str = None, AutoMinorVersionUpgrade: bool = None, LicenseModel: str = None, Iops: int = None, OptionGroupName: str = None, CharacterSetName: str = None, PubliclyAccessible: bool = None, Tags: List = None, DBClusterIdentifier: str = None, StorageType: str = None, TdeCredentialArn: str = None, TdeCredentialPassword: str = None, StorageEncrypted: bool = None, KmsKeyId: str = None, Domain: str = None, CopyTagsToSnapshot: bool = None, MonitoringInterval: int = None, MonitoringRoleArn: str = None, DomainIAMRoleName: str = None, PromotionTier: int = None, Timezone: str = None, EnableIAMDatabaseAuthentication: bool = None, EnablePerformanceInsights: bool = None, PerformanceInsightsKMSKeyId: str = None, PerformanceInsightsRetentionPeriod: int = None, EnableCloudwatchLogsExports: List = None, ProcessorFeatures: List = None, DeletionProtection: bool = None) -> Dict:
        pass

    def create_db_instance_read_replica(self, DBInstanceIdentifier: str, SourceDBInstanceIdentifier: str, DBInstanceClass: str = None, AvailabilityZone: str = None, Port: int = None, MultiAZ: bool = None, AutoMinorVersionUpgrade: bool = None, Iops: int = None, OptionGroupName: str = None, PubliclyAccessible: bool = None, Tags: List = None, DBSubnetGroupName: str = None, StorageType: str = None, CopyTagsToSnapshot: bool = None, MonitoringInterval: int = None, MonitoringRoleArn: str = None, KmsKeyId: str = None, PreSignedUrl: str = None, EnableIAMDatabaseAuthentication: bool = None, EnablePerformanceInsights: bool = None, PerformanceInsightsKMSKeyId: str = None, PerformanceInsightsRetentionPeriod: int = None, EnableCloudwatchLogsExports: List = None, ProcessorFeatures: List = None, UseDefaultProcessorFeatures: bool = None, DeletionProtection: bool = None, SourceRegion: str = None) -> Dict:
        pass

    def create_db_parameter_group(self, DBParameterGroupName: str, DBParameterGroupFamily: str, Description: str, Tags: List = None) -> Dict:
        pass

    def create_db_security_group(self, DBSecurityGroupName: str, DBSecurityGroupDescription: str, Tags: List = None) -> Dict:
        pass

    def create_db_snapshot(self, DBSnapshotIdentifier: str, DBInstanceIdentifier: str, Tags: List = None) -> Dict:
        pass

    def create_db_subnet_group(self, DBSubnetGroupName: str, DBSubnetGroupDescription: str, SubnetIds: List, Tags: List = None) -> Dict:
        pass

    def create_event_subscription(self, SubscriptionName: str, SnsTopicArn: str, SourceType: str = None, EventCategories: List = None, SourceIds: List = None, Enabled: bool = None, Tags: List = None) -> Dict:
        pass

    def create_option_group(self, OptionGroupName: str, EngineName: str, MajorEngineVersion: str, OptionGroupDescription: str, Tags: List = None) -> Dict:
        pass

    def delete_db_cluster(self, DBClusterIdentifier: str, SkipFinalSnapshot: bool = None, FinalDBSnapshotIdentifier: str = None) -> Dict:
        pass

    def delete_db_cluster_endpoint(self, DBClusterEndpointIdentifier: str) -> Dict:
        pass

    def delete_db_cluster_parameter_group(self, DBClusterParameterGroupName: str):
        pass

    def delete_db_cluster_snapshot(self, DBClusterSnapshotIdentifier: str) -> Dict:
        pass

    def delete_db_instance(self, DBInstanceIdentifier: str, SkipFinalSnapshot: bool = None, FinalDBSnapshotIdentifier: str = None) -> Dict:
        pass

    def delete_db_parameter_group(self, DBParameterGroupName: str):
        pass

    def delete_db_security_group(self, DBSecurityGroupName: str):
        pass

    def delete_db_snapshot(self, DBSnapshotIdentifier: str) -> Dict:
        pass

    def delete_db_subnet_group(self, DBSubnetGroupName: str):
        pass

    def delete_event_subscription(self, SubscriptionName: str) -> Dict:
        pass

    def delete_option_group(self, OptionGroupName: str):
        pass

    def describe_account_attributes(self) -> Dict:
        pass

    def describe_certificates(self, CertificateIdentifier: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_db_cluster_backtracks(self, DBClusterIdentifier: str, BacktrackIdentifier: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_db_cluster_endpoints(self, DBClusterIdentifier: str = None, DBClusterEndpointIdentifier: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
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

    def describe_db_log_files(self, DBInstanceIdentifier: str, FilenameContains: str = None, FileLastWritten: int = None, FileSize: int = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_db_parameter_groups(self, DBParameterGroupName: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_db_parameters(self, DBParameterGroupName: str, Source: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_db_security_groups(self, DBSecurityGroupName: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_db_snapshot_attributes(self, DBSnapshotIdentifier: str) -> Dict:
        pass

    def describe_db_snapshots(self, DBInstanceIdentifier: str = None, DBSnapshotIdentifier: str = None, SnapshotType: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, IncludeShared: bool = None, IncludePublic: bool = None) -> Dict:
        pass

    def describe_db_subnet_groups(self, DBSubnetGroupName: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_engine_default_cluster_parameters(self, DBParameterGroupFamily: str, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_engine_default_parameters(self, DBParameterGroupFamily: str, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_event_categories(self, SourceType: str = None, Filters: List = None) -> Dict:
        pass

    def describe_event_subscriptions(self, SubscriptionName: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_events(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, EventCategories: List = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_option_group_options(self, EngineName: str, MajorEngineVersion: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_option_groups(self, OptionGroupName: str = None, Filters: List = None, Marker: str = None, MaxRecords: int = None, EngineName: str = None, MajorEngineVersion: str = None) -> Dict:
        pass

    def describe_orderable_db_instance_options(self, Engine: str, EngineVersion: str = None, DBInstanceClass: str = None, LicenseModel: str = None, Vpc: bool = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_pending_maintenance_actions(self, ResourceIdentifier: str = None, Filters: List = None, Marker: str = None, MaxRecords: int = None) -> Dict:
        pass

    def describe_reserved_db_instances(self, ReservedDBInstanceId: str = None, ReservedDBInstancesOfferingId: str = None, DBInstanceClass: str = None, Duration: str = None, ProductDescription: str = None, OfferingType: str = None, MultiAZ: bool = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_reserved_db_instances_offerings(self, ReservedDBInstancesOfferingId: str = None, DBInstanceClass: str = None, Duration: str = None, ProductDescription: str = None, OfferingType: str = None, MultiAZ: bool = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_source_regions(self, RegionName: str = None, MaxRecords: int = None, Marker: str = None, Filters: List = None) -> Dict:
        pass

    def describe_valid_db_instance_modifications(self, DBInstanceIdentifier: str) -> Dict:
        pass

    def download_db_log_file_portion(self, DBInstanceIdentifier: str, LogFileName: str, Marker: str = None, NumberOfLines: int = None) -> Dict:
        pass

    def failover_db_cluster(self, DBClusterIdentifier: str = None, TargetDBInstanceIdentifier: str = None) -> Dict:
        pass

    def generate_db_auth_token(self, DBHostname: str = None, Port: int = None, DBUsername: str = None, Region: str = None):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_tags_for_resource(self, ResourceName: str, Filters: List = None) -> Dict:
        pass

    def modify_current_db_cluster_capacity(self, DBClusterIdentifier: str, Capacity: int = None, SecondsBeforeTimeout: int = None, TimeoutAction: str = None) -> Dict:
        pass

    def modify_db_cluster(self, DBClusterIdentifier: str, NewDBClusterIdentifier: str = None, ApplyImmediately: bool = None, BackupRetentionPeriod: int = None, DBClusterParameterGroupName: str = None, VpcSecurityGroupIds: List = None, Port: int = None, MasterUserPassword: str = None, OptionGroupName: str = None, PreferredBackupWindow: str = None, PreferredMaintenanceWindow: str = None, EnableIAMDatabaseAuthentication: bool = None, BacktrackWindow: int = None, CloudwatchLogsExportConfiguration: Dict = None, EngineVersion: str = None, ScalingConfiguration: Dict = None, DeletionProtection: bool = None) -> Dict:
        pass

    def modify_db_cluster_endpoint(self, DBClusterEndpointIdentifier: str, EndpointType: str = None, StaticMembers: List = None, ExcludedMembers: List = None) -> Dict:
        pass

    def modify_db_cluster_parameter_group(self, DBClusterParameterGroupName: str, Parameters: List) -> Dict:
        pass

    def modify_db_cluster_snapshot_attribute(self, DBClusterSnapshotIdentifier: str, AttributeName: str, ValuesToAdd: List = None, ValuesToRemove: List = None) -> Dict:
        pass

    def modify_db_instance(self, DBInstanceIdentifier: str, AllocatedStorage: int = None, DBInstanceClass: str = None, DBSubnetGroupName: str = None, DBSecurityGroups: List = None, VpcSecurityGroupIds: List = None, ApplyImmediately: bool = None, MasterUserPassword: str = None, DBParameterGroupName: str = None, BackupRetentionPeriod: int = None, PreferredBackupWindow: str = None, PreferredMaintenanceWindow: str = None, MultiAZ: bool = None, EngineVersion: str = None, AllowMajorVersionUpgrade: bool = None, AutoMinorVersionUpgrade: bool = None, LicenseModel: str = None, Iops: int = None, OptionGroupName: str = None, NewDBInstanceIdentifier: str = None, StorageType: str = None, TdeCredentialArn: str = None, TdeCredentialPassword: str = None, CACertificateIdentifier: str = None, Domain: str = None, CopyTagsToSnapshot: bool = None, MonitoringInterval: int = None, DBPortNumber: int = None, PubliclyAccessible: bool = None, MonitoringRoleArn: str = None, DomainIAMRoleName: str = None, PromotionTier: int = None, EnableIAMDatabaseAuthentication: bool = None, EnablePerformanceInsights: bool = None, PerformanceInsightsKMSKeyId: str = None, PerformanceInsightsRetentionPeriod: int = None, CloudwatchLogsExportConfiguration: Dict = None, ProcessorFeatures: List = None, UseDefaultProcessorFeatures: bool = None, DeletionProtection: bool = None) -> Dict:
        pass

    def modify_db_parameter_group(self, DBParameterGroupName: str, Parameters: List) -> Dict:
        pass

    def modify_db_snapshot(self, DBSnapshotIdentifier: str, EngineVersion: str = None, OptionGroupName: str = None) -> Dict:
        pass

    def modify_db_snapshot_attribute(self, DBSnapshotIdentifier: str, AttributeName: str, ValuesToAdd: List = None, ValuesToRemove: List = None) -> Dict:
        pass

    def modify_db_subnet_group(self, DBSubnetGroupName: str, SubnetIds: List, DBSubnetGroupDescription: str = None) -> Dict:
        pass

    def modify_event_subscription(self, SubscriptionName: str, SnsTopicArn: str = None, SourceType: str = None, EventCategories: List = None, Enabled: bool = None) -> Dict:
        pass

    def modify_option_group(self, OptionGroupName: str, OptionsToInclude: List = None, OptionsToRemove: List = None, ApplyImmediately: bool = None) -> Dict:
        pass

    def promote_read_replica(self, DBInstanceIdentifier: str, BackupRetentionPeriod: int = None, PreferredBackupWindow: str = None) -> Dict:
        pass

    def promote_read_replica_db_cluster(self, DBClusterIdentifier: str) -> Dict:
        pass

    def purchase_reserved_db_instances_offering(self, ReservedDBInstancesOfferingId: str, ReservedDBInstanceId: str = None, DBInstanceCount: int = None, Tags: List = None) -> Dict:
        pass

    def reboot_db_instance(self, DBInstanceIdentifier: str, ForceFailover: bool = None) -> Dict:
        pass

    def remove_role_from_db_cluster(self, DBClusterIdentifier: str, RoleArn: str):
        pass

    def remove_source_identifier_from_subscription(self, SubscriptionName: str, SourceIdentifier: str) -> Dict:
        pass

    def remove_tags_from_resource(self, ResourceName: str, TagKeys: List):
        pass

    def reset_db_cluster_parameter_group(self, DBClusterParameterGroupName: str, ResetAllParameters: bool = None, Parameters: List = None) -> Dict:
        pass

    def reset_db_parameter_group(self, DBParameterGroupName: str, ResetAllParameters: bool = None, Parameters: List = None) -> Dict:
        pass

    def restore_db_cluster_from_s3(self, DBClusterIdentifier: str, Engine: str, MasterUsername: str, MasterUserPassword: str, SourceEngine: str, SourceEngineVersion: str, S3BucketName: str, S3IngestionRoleArn: str, AvailabilityZones: List = None, BackupRetentionPeriod: int = None, CharacterSetName: str = None, DatabaseName: str = None, DBClusterParameterGroupName: str = None, VpcSecurityGroupIds: List = None, DBSubnetGroupName: str = None, EngineVersion: str = None, Port: int = None, OptionGroupName: str = None, PreferredBackupWindow: str = None, PreferredMaintenanceWindow: str = None, Tags: List = None, StorageEncrypted: bool = None, KmsKeyId: str = None, EnableIAMDatabaseAuthentication: bool = None, S3Prefix: str = None, BacktrackWindow: int = None, EnableCloudwatchLogsExports: List = None, DeletionProtection: bool = None) -> Dict:
        pass

    def restore_db_cluster_from_snapshot(self, DBClusterIdentifier: str, SnapshotIdentifier: str, Engine: str, AvailabilityZones: List = None, EngineVersion: str = None, Port: int = None, DBSubnetGroupName: str = None, DatabaseName: str = None, OptionGroupName: str = None, VpcSecurityGroupIds: List = None, Tags: List = None, KmsKeyId: str = None, EnableIAMDatabaseAuthentication: bool = None, BacktrackWindow: int = None, EnableCloudwatchLogsExports: List = None, EngineMode: str = None, ScalingConfiguration: Dict = None, DBClusterParameterGroupName: str = None, DeletionProtection: bool = None) -> Dict:
        pass

    def restore_db_cluster_to_point_in_time(self, DBClusterIdentifier: str, SourceDBClusterIdentifier: str, RestoreType: str = None, RestoreToTime: datetime = None, UseLatestRestorableTime: bool = None, Port: int = None, DBSubnetGroupName: str = None, OptionGroupName: str = None, VpcSecurityGroupIds: List = None, Tags: List = None, KmsKeyId: str = None, EnableIAMDatabaseAuthentication: bool = None, BacktrackWindow: int = None, EnableCloudwatchLogsExports: List = None, DBClusterParameterGroupName: str = None, DeletionProtection: bool = None) -> Dict:
        pass

    def restore_db_instance_from_db_snapshot(self, DBInstanceIdentifier: str, DBSnapshotIdentifier: str, DBInstanceClass: str = None, Port: int = None, AvailabilityZone: str = None, DBSubnetGroupName: str = None, MultiAZ: bool = None, PubliclyAccessible: bool = None, AutoMinorVersionUpgrade: bool = None, LicenseModel: str = None, DBName: str = None, Engine: str = None, Iops: int = None, OptionGroupName: str = None, Tags: List = None, StorageType: str = None, TdeCredentialArn: str = None, TdeCredentialPassword: str = None, Domain: str = None, CopyTagsToSnapshot: bool = None, DomainIAMRoleName: str = None, EnableIAMDatabaseAuthentication: bool = None, EnableCloudwatchLogsExports: List = None, ProcessorFeatures: List = None, UseDefaultProcessorFeatures: bool = None, DBParameterGroupName: str = None, DeletionProtection: bool = None) -> Dict:
        pass

    def restore_db_instance_from_s3(self, DBInstanceIdentifier: str, DBInstanceClass: str, Engine: str, SourceEngine: str, SourceEngineVersion: str, S3BucketName: str, S3IngestionRoleArn: str, DBName: str = None, AllocatedStorage: int = None, MasterUsername: str = None, MasterUserPassword: str = None, DBSecurityGroups: List = None, VpcSecurityGroupIds: List = None, AvailabilityZone: str = None, DBSubnetGroupName: str = None, PreferredMaintenanceWindow: str = None, DBParameterGroupName: str = None, BackupRetentionPeriod: int = None, PreferredBackupWindow: str = None, Port: int = None, MultiAZ: bool = None, EngineVersion: str = None, AutoMinorVersionUpgrade: bool = None, LicenseModel: str = None, Iops: int = None, OptionGroupName: str = None, PubliclyAccessible: bool = None, Tags: List = None, StorageType: str = None, StorageEncrypted: bool = None, KmsKeyId: str = None, CopyTagsToSnapshot: bool = None, MonitoringInterval: int = None, MonitoringRoleArn: str = None, EnableIAMDatabaseAuthentication: bool = None, S3Prefix: str = None, EnablePerformanceInsights: bool = None, PerformanceInsightsKMSKeyId: str = None, PerformanceInsightsRetentionPeriod: int = None, EnableCloudwatchLogsExports: List = None, ProcessorFeatures: List = None, UseDefaultProcessorFeatures: bool = None, DeletionProtection: bool = None) -> Dict:
        pass

    def restore_db_instance_to_point_in_time(self, SourceDBInstanceIdentifier: str, TargetDBInstanceIdentifier: str, RestoreTime: datetime = None, UseLatestRestorableTime: bool = None, DBInstanceClass: str = None, Port: int = None, AvailabilityZone: str = None, DBSubnetGroupName: str = None, MultiAZ: bool = None, PubliclyAccessible: bool = None, AutoMinorVersionUpgrade: bool = None, LicenseModel: str = None, DBName: str = None, Engine: str = None, Iops: int = None, OptionGroupName: str = None, CopyTagsToSnapshot: bool = None, Tags: List = None, StorageType: str = None, TdeCredentialArn: str = None, TdeCredentialPassword: str = None, Domain: str = None, DomainIAMRoleName: str = None, EnableIAMDatabaseAuthentication: bool = None, EnableCloudwatchLogsExports: List = None, ProcessorFeatures: List = None, UseDefaultProcessorFeatures: bool = None, DBParameterGroupName: str = None, DeletionProtection: bool = None) -> Dict:
        pass

    def revoke_db_security_group_ingress(self, DBSecurityGroupName: str, CIDRIP: str = None, EC2SecurityGroupName: str = None, EC2SecurityGroupId: str = None, EC2SecurityGroupOwnerId: str = None) -> Dict:
        pass

    def start_db_cluster(self, DBClusterIdentifier: str) -> Dict:
        pass

    def start_db_instance(self, DBInstanceIdentifier: str) -> Dict:
        pass

    def stop_db_cluster(self, DBClusterIdentifier: str) -> Dict:
        pass

    def stop_db_instance(self, DBInstanceIdentifier: str, DBSnapshotIdentifier: str = None) -> Dict:
        pass
