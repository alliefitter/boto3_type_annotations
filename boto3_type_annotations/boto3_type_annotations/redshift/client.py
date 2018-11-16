from datetime import datetime
from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def accept_reserved_node_exchange(self, ReservedNodeId: str, TargetReservedNodeOfferingId: str) -> Dict:
        pass

    def authorize_cluster_security_group_ingress(self, ClusterSecurityGroupName: str, CIDRIP: str = None, EC2SecurityGroupName: str = None, EC2SecurityGroupOwnerId: str = None) -> Dict:
        pass

    def authorize_snapshot_access(self, SnapshotIdentifier: str, AccountWithRestoreAccess: str, SnapshotClusterIdentifier: str = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def copy_cluster_snapshot(self, SourceSnapshotIdentifier: str, TargetSnapshotIdentifier: str, SourceSnapshotClusterIdentifier: str = None) -> Dict:
        pass

    def create_cluster(self, ClusterIdentifier: str, NodeType: str, MasterUsername: str, MasterUserPassword: str, DBName: str = None, ClusterType: str = None, ClusterSecurityGroups: List = None, VpcSecurityGroupIds: List = None, ClusterSubnetGroupName: str = None, AvailabilityZone: str = None, PreferredMaintenanceWindow: str = None, ClusterParameterGroupName: str = None, AutomatedSnapshotRetentionPeriod: int = None, Port: int = None, ClusterVersion: str = None, AllowVersionUpgrade: bool = None, NumberOfNodes: int = None, PubliclyAccessible: bool = None, Encrypted: bool = None, HsmClientCertificateIdentifier: str = None, HsmConfigurationIdentifier: str = None, ElasticIp: str = None, Tags: List = None, KmsKeyId: str = None, EnhancedVpcRouting: bool = None, AdditionalInfo: str = None, IamRoles: List = None, MaintenanceTrackName: str = None) -> Dict:
        pass

    def create_cluster_parameter_group(self, ParameterGroupName: str, ParameterGroupFamily: str, Description: str, Tags: List = None) -> Dict:
        pass

    def create_cluster_security_group(self, ClusterSecurityGroupName: str, Description: str, Tags: List = None) -> Dict:
        pass

    def create_cluster_snapshot(self, SnapshotIdentifier: str, ClusterIdentifier: str, Tags: List = None) -> Dict:
        pass

    def create_cluster_subnet_group(self, ClusterSubnetGroupName: str, Description: str, SubnetIds: List, Tags: List = None) -> Dict:
        pass

    def create_event_subscription(self, SubscriptionName: str, SnsTopicArn: str, SourceType: str = None, SourceIds: List = None, EventCategories: List = None, Severity: str = None, Enabled: bool = None, Tags: List = None) -> Dict:
        pass

    def create_hsm_client_certificate(self, HsmClientCertificateIdentifier: str, Tags: List = None) -> Dict:
        pass

    def create_hsm_configuration(self, HsmConfigurationIdentifier: str, Description: str, HsmIpAddress: str, HsmPartitionName: str, HsmPartitionPassword: str, HsmServerPublicCertificate: str, Tags: List = None) -> Dict:
        pass

    def create_snapshot_copy_grant(self, SnapshotCopyGrantName: str, KmsKeyId: str = None, Tags: List = None) -> Dict:
        pass

    def create_tags(self, ResourceName: str, Tags: List) -> NoReturn:
        pass

    def delete_cluster(self, ClusterIdentifier: str, SkipFinalClusterSnapshot: bool = None, FinalClusterSnapshotIdentifier: str = None) -> Dict:
        pass

    def delete_cluster_parameter_group(self, ParameterGroupName: str) -> NoReturn:
        pass

    def delete_cluster_security_group(self, ClusterSecurityGroupName: str) -> NoReturn:
        pass

    def delete_cluster_snapshot(self, SnapshotIdentifier: str, SnapshotClusterIdentifier: str = None) -> Dict:
        pass

    def delete_cluster_subnet_group(self, ClusterSubnetGroupName: str) -> NoReturn:
        pass

    def delete_event_subscription(self, SubscriptionName: str) -> NoReturn:
        pass

    def delete_hsm_client_certificate(self, HsmClientCertificateIdentifier: str) -> NoReturn:
        pass

    def delete_hsm_configuration(self, HsmConfigurationIdentifier: str) -> NoReturn:
        pass

    def delete_snapshot_copy_grant(self, SnapshotCopyGrantName: str) -> NoReturn:
        pass

    def delete_tags(self, ResourceName: str, TagKeys: List) -> NoReturn:
        pass

    def describe_cluster_db_revisions(self, ClusterIdentifier: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_cluster_parameter_groups(self, ParameterGroupName: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None) -> Dict:
        pass

    def describe_cluster_parameters(self, ParameterGroupName: str, Source: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_cluster_security_groups(self, ClusterSecurityGroupName: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None) -> Dict:
        pass

    def describe_cluster_snapshots(self, ClusterIdentifier: str = None, SnapshotIdentifier: str = None, SnapshotType: str = None, StartTime: datetime = None, EndTime: datetime = None, MaxRecords: int = None, Marker: str = None, OwnerAccount: str = None, TagKeys: List = None, TagValues: List = None, ClusterExists: bool = None) -> Dict:
        pass

    def describe_cluster_subnet_groups(self, ClusterSubnetGroupName: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None) -> Dict:
        pass

    def describe_cluster_tracks(self, MaintenanceTrackName: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_cluster_versions(self, ClusterVersion: str = None, ClusterParameterGroupFamily: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_clusters(self, ClusterIdentifier: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None) -> Dict:
        pass

    def describe_default_cluster_parameters(self, ParameterGroupFamily: str, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_event_categories(self, SourceType: str = None) -> Dict:
        pass

    def describe_event_subscriptions(self, SubscriptionName: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None) -> Dict:
        pass

    def describe_events(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_hsm_client_certificates(self, HsmClientCertificateIdentifier: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None) -> Dict:
        pass

    def describe_hsm_configurations(self, HsmConfigurationIdentifier: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None) -> Dict:
        pass

    def describe_logging_status(self, ClusterIdentifier: str) -> Dict:
        pass

    def describe_orderable_cluster_options(self, ClusterVersion: str = None, NodeType: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_reserved_node_offerings(self, ReservedNodeOfferingId: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_reserved_nodes(self, ReservedNodeId: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_resize(self, ClusterIdentifier: str) -> Dict:
        pass

    def describe_snapshot_copy_grants(self, SnapshotCopyGrantName: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None) -> Dict:
        pass

    def describe_table_restore_status(self, ClusterIdentifier: str = None, TableRestoreRequestId: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_tags(self, ResourceName: str = None, ResourceType: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None) -> Dict:
        pass

    def disable_logging(self, ClusterIdentifier: str) -> Dict:
        pass

    def disable_snapshot_copy(self, ClusterIdentifier: str) -> Dict:
        pass

    def enable_logging(self, ClusterIdentifier: str, BucketName: str, S3KeyPrefix: str = None) -> Dict:
        pass

    def enable_snapshot_copy(self, ClusterIdentifier: str, DestinationRegion: str, RetentionPeriod: int = None, SnapshotCopyGrantName: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_cluster_credentials(self, DbUser: str, ClusterIdentifier: str, DbName: str = None, DurationSeconds: int = None, AutoCreate: bool = None, DbGroups: List = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_reserved_node_exchange_offerings(self, ReservedNodeId: str, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def modify_cluster(self, ClusterIdentifier: str, ClusterType: str = None, NodeType: str = None, NumberOfNodes: int = None, ClusterSecurityGroups: List = None, VpcSecurityGroupIds: List = None, MasterUserPassword: str = None, ClusterParameterGroupName: str = None, AutomatedSnapshotRetentionPeriod: int = None, PreferredMaintenanceWindow: str = None, ClusterVersion: str = None, AllowVersionUpgrade: bool = None, HsmClientCertificateIdentifier: str = None, HsmConfigurationIdentifier: str = None, NewClusterIdentifier: str = None, PubliclyAccessible: bool = None, ElasticIp: str = None, EnhancedVpcRouting: bool = None, MaintenanceTrackName: str = None, Encrypted: bool = None, KmsKeyId: str = None) -> Dict:
        pass

    def modify_cluster_db_revision(self, ClusterIdentifier: str, RevisionTarget: str) -> Dict:
        pass

    def modify_cluster_iam_roles(self, ClusterIdentifier: str, AddIamRoles: List = None, RemoveIamRoles: List = None) -> Dict:
        pass

    def modify_cluster_parameter_group(self, ParameterGroupName: str, Parameters: List) -> Dict:
        pass

    def modify_cluster_subnet_group(self, ClusterSubnetGroupName: str, SubnetIds: List, Description: str = None) -> Dict:
        pass

    def modify_event_subscription(self, SubscriptionName: str, SnsTopicArn: str = None, SourceType: str = None, SourceIds: List = None, EventCategories: List = None, Severity: str = None, Enabled: bool = None) -> Dict:
        pass

    def modify_snapshot_copy_retention_period(self, ClusterIdentifier: str, RetentionPeriod: int) -> Dict:
        pass

    def purchase_reserved_node_offering(self, ReservedNodeOfferingId: str, NodeCount: int = None) -> Dict:
        pass

    def reboot_cluster(self, ClusterIdentifier: str) -> Dict:
        pass

    def reset_cluster_parameter_group(self, ParameterGroupName: str, ResetAllParameters: bool = None, Parameters: List = None) -> Dict:
        pass

    def resize_cluster(self, ClusterIdentifier: str, NumberOfNodes: int, ClusterType: str = None, NodeType: str = None, Classic: bool = None) -> Dict:
        pass

    def restore_from_cluster_snapshot(self, ClusterIdentifier: str, SnapshotIdentifier: str, SnapshotClusterIdentifier: str = None, Port: int = None, AvailabilityZone: str = None, AllowVersionUpgrade: bool = None, ClusterSubnetGroupName: str = None, PubliclyAccessible: bool = None, OwnerAccount: str = None, HsmClientCertificateIdentifier: str = None, HsmConfigurationIdentifier: str = None, ElasticIp: str = None, ClusterParameterGroupName: str = None, ClusterSecurityGroups: List = None, VpcSecurityGroupIds: List = None, PreferredMaintenanceWindow: str = None, AutomatedSnapshotRetentionPeriod: int = None, KmsKeyId: str = None, NodeType: str = None, EnhancedVpcRouting: bool = None, AdditionalInfo: str = None, IamRoles: List = None, MaintenanceTrackName: str = None) -> Dict:
        pass

    def restore_table_from_cluster_snapshot(self, ClusterIdentifier: str, SnapshotIdentifier: str, SourceDatabaseName: str, SourceTableName: str, NewTableName: str, SourceSchemaName: str = None, TargetDatabaseName: str = None, TargetSchemaName: str = None) -> Dict:
        pass

    def revoke_cluster_security_group_ingress(self, ClusterSecurityGroupName: str, CIDRIP: str = None, EC2SecurityGroupName: str = None, EC2SecurityGroupOwnerId: str = None) -> Dict:
        pass

    def revoke_snapshot_access(self, SnapshotIdentifier: str, AccountWithRestoreAccess: str, SnapshotClusterIdentifier: str = None) -> Dict:
        pass

    def rotate_encryption_key(self, ClusterIdentifier: str) -> Dict:
        pass
