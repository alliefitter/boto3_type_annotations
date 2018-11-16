from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def add_tags_to_resource(self, ResourceName: str, Tags: List) -> Dict:
        pass

    def authorize_cache_security_group_ingress(self, CacheSecurityGroupName: str, EC2SecurityGroupName: str, EC2SecurityGroupOwnerId: str) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def copy_snapshot(self, SourceSnapshotName: str, TargetSnapshotName: str, TargetBucket: str = None) -> Dict:
        pass

    def create_cache_cluster(self, CacheClusterId: str, ReplicationGroupId: str = None, AZMode: str = None, PreferredAvailabilityZone: str = None, PreferredAvailabilityZones: List = None, NumCacheNodes: int = None, CacheNodeType: str = None, Engine: str = None, EngineVersion: str = None, CacheParameterGroupName: str = None, CacheSubnetGroupName: str = None, CacheSecurityGroupNames: List = None, SecurityGroupIds: List = None, Tags: List = None, SnapshotArns: List = None, SnapshotName: str = None, PreferredMaintenanceWindow: str = None, Port: int = None, NotificationTopicArn: str = None, AutoMinorVersionUpgrade: bool = None, SnapshotRetentionLimit: int = None, SnapshotWindow: str = None, AuthToken: str = None) -> Dict:
        pass

    def create_cache_parameter_group(self, CacheParameterGroupName: str, CacheParameterGroupFamily: str, Description: str) -> Dict:
        pass

    def create_cache_security_group(self, CacheSecurityGroupName: str, Description: str) -> Dict:
        pass

    def create_cache_subnet_group(self, CacheSubnetGroupName: str, CacheSubnetGroupDescription: str, SubnetIds: List) -> Dict:
        pass

    def create_replication_group(self, ReplicationGroupId: str, ReplicationGroupDescription: str, PrimaryClusterId: str = None, AutomaticFailoverEnabled: bool = None, NumCacheClusters: int = None, PreferredCacheClusterAZs: List = None, NumNodeGroups: int = None, ReplicasPerNodeGroup: int = None, NodeGroupConfiguration: List = None, CacheNodeType: str = None, Engine: str = None, EngineVersion: str = None, CacheParameterGroupName: str = None, CacheSubnetGroupName: str = None, CacheSecurityGroupNames: List = None, SecurityGroupIds: List = None, Tags: List = None, SnapshotArns: List = None, SnapshotName: str = None, PreferredMaintenanceWindow: str = None, Port: int = None, NotificationTopicArn: str = None, AutoMinorVersionUpgrade: bool = None, SnapshotRetentionLimit: int = None, SnapshotWindow: str = None, AuthToken: str = None, TransitEncryptionEnabled: bool = None, AtRestEncryptionEnabled: bool = None) -> Dict:
        pass

    def create_snapshot(self, SnapshotName: str, ReplicationGroupId: str = None, CacheClusterId: str = None) -> Dict:
        pass

    def decrease_replica_count(self, ReplicationGroupId: str, ApplyImmediately: bool, NewReplicaCount: int = None, ReplicaConfiguration: List = None, ReplicasToRemove: List = None) -> Dict:
        pass

    def delete_cache_cluster(self, CacheClusterId: str, FinalSnapshotIdentifier: str = None) -> Dict:
        pass

    def delete_cache_parameter_group(self, CacheParameterGroupName: str):
        pass

    def delete_cache_security_group(self, CacheSecurityGroupName: str):
        pass

    def delete_cache_subnet_group(self, CacheSubnetGroupName: str):
        pass

    def delete_replication_group(self, ReplicationGroupId: str, RetainPrimaryCluster: bool = None, FinalSnapshotIdentifier: str = None) -> Dict:
        pass

    def delete_snapshot(self, SnapshotName: str) -> Dict:
        pass

    def describe_cache_clusters(self, CacheClusterId: str = None, MaxRecords: int = None, Marker: str = None, ShowCacheNodeInfo: bool = None, ShowCacheClustersNotInReplicationGroups: bool = None) -> Dict:
        pass

    def describe_cache_engine_versions(self, Engine: str = None, EngineVersion: str = None, CacheParameterGroupFamily: str = None, MaxRecords: int = None, Marker: str = None, DefaultOnly: bool = None) -> Dict:
        pass

    def describe_cache_parameter_groups(self, CacheParameterGroupName: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_cache_parameters(self, CacheParameterGroupName: str, Source: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_cache_security_groups(self, CacheSecurityGroupName: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_cache_subnet_groups(self, CacheSubnetGroupName: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_engine_default_parameters(self, CacheParameterGroupFamily: str, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_events(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_replication_groups(self, ReplicationGroupId: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_reserved_cache_nodes(self, ReservedCacheNodeId: str = None, ReservedCacheNodesOfferingId: str = None, CacheNodeType: str = None, Duration: str = None, ProductDescription: str = None, OfferingType: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_reserved_cache_nodes_offerings(self, ReservedCacheNodesOfferingId: str = None, CacheNodeType: str = None, Duration: str = None, ProductDescription: str = None, OfferingType: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_snapshots(self, ReplicationGroupId: str = None, CacheClusterId: str = None, SnapshotName: str = None, SnapshotSource: str = None, Marker: str = None, MaxRecords: int = None, ShowNodeGroupConfig: bool = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def increase_replica_count(self, ReplicationGroupId: str, ApplyImmediately: bool, NewReplicaCount: int = None, ReplicaConfiguration: List = None) -> Dict:
        pass

    def list_allowed_node_type_modifications(self, CacheClusterId: str = None, ReplicationGroupId: str = None) -> Dict:
        pass

    def list_tags_for_resource(self, ResourceName: str) -> Dict:
        pass

    def modify_cache_cluster(self, CacheClusterId: str, NumCacheNodes: int = None, CacheNodeIdsToRemove: List = None, AZMode: str = None, NewAvailabilityZones: List = None, CacheSecurityGroupNames: List = None, SecurityGroupIds: List = None, PreferredMaintenanceWindow: str = None, NotificationTopicArn: str = None, CacheParameterGroupName: str = None, NotificationTopicStatus: str = None, ApplyImmediately: bool = None, EngineVersion: str = None, AutoMinorVersionUpgrade: bool = None, SnapshotRetentionLimit: int = None, SnapshotWindow: str = None, CacheNodeType: str = None) -> Dict:
        pass

    def modify_cache_parameter_group(self, CacheParameterGroupName: str, ParameterNameValues: List) -> Dict:
        pass

    def modify_cache_subnet_group(self, CacheSubnetGroupName: str, CacheSubnetGroupDescription: str = None, SubnetIds: List = None) -> Dict:
        pass

    def modify_replication_group(self, ReplicationGroupId: str, ReplicationGroupDescription: str = None, PrimaryClusterId: str = None, SnapshottingClusterId: str = None, AutomaticFailoverEnabled: bool = None, CacheSecurityGroupNames: List = None, SecurityGroupIds: List = None, PreferredMaintenanceWindow: str = None, NotificationTopicArn: str = None, CacheParameterGroupName: str = None, NotificationTopicStatus: str = None, ApplyImmediately: bool = None, EngineVersion: str = None, AutoMinorVersionUpgrade: bool = None, SnapshotRetentionLimit: int = None, SnapshotWindow: str = None, CacheNodeType: str = None, NodeGroupId: str = None) -> Dict:
        pass

    def modify_replication_group_shard_configuration(self, ReplicationGroupId: str, NodeGroupCount: int, ApplyImmediately: bool, ReshardingConfiguration: List = None, NodeGroupsToRemove: List = None, NodeGroupsToRetain: List = None) -> Dict:
        pass

    def purchase_reserved_cache_nodes_offering(self, ReservedCacheNodesOfferingId: str, ReservedCacheNodeId: str = None, CacheNodeCount: int = None) -> Dict:
        pass

    def reboot_cache_cluster(self, CacheClusterId: str, CacheNodeIdsToReboot: List) -> Dict:
        pass

    def remove_tags_from_resource(self, ResourceName: str, TagKeys: List) -> Dict:
        pass

    def reset_cache_parameter_group(self, CacheParameterGroupName: str, ResetAllParameters: bool = None, ParameterNameValues: List = None) -> Dict:
        pass

    def revoke_cache_security_group_ingress(self, CacheSecurityGroupName: str, EC2SecurityGroupName: str, EC2SecurityGroupOwnerId: str) -> Dict:
        pass

    def test_failover(self, ReplicationGroupId: str, NodeGroupId: str) -> Dict:
        pass
