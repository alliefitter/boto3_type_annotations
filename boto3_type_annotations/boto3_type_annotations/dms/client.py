from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def add_tags_to_resource(self, ResourceArn: str, Tags: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_endpoint(self, EndpointIdentifier: str, EndpointType: str, EngineName: str, Username: str = None, Password: str = None, ServerName: str = None, Port: int = None, DatabaseName: str = None, ExtraConnectionAttributes: str = None, KmsKeyId: str = None, Tags: List = None, CertificateArn: str = None, SslMode: str = None, ServiceAccessRoleArn: str = None, ExternalTableDefinition: str = None, DynamoDbSettings: Dict = None, S3Settings: Dict = None, DmsTransferSettings: Dict = None, MongoDbSettings: Dict = None) -> Dict:
        pass

    def create_event_subscription(self, SubscriptionName: str, SnsTopicArn: str, SourceType: str = None, EventCategories: List = None, SourceIds: List = None, Enabled: bool = None, Tags: List = None) -> Dict:
        pass

    def create_replication_instance(self, ReplicationInstanceIdentifier: str, ReplicationInstanceClass: str, AllocatedStorage: int = None, VpcSecurityGroupIds: List = None, AvailabilityZone: str = None, ReplicationSubnetGroupIdentifier: str = None, PreferredMaintenanceWindow: str = None, MultiAZ: bool = None, EngineVersion: str = None, AutoMinorVersionUpgrade: bool = None, Tags: List = None, KmsKeyId: str = None, PubliclyAccessible: bool = None) -> Dict:
        pass

    def create_replication_subnet_group(self, ReplicationSubnetGroupIdentifier: str, ReplicationSubnetGroupDescription: str, SubnetIds: List, Tags: List = None) -> Dict:
        pass

    def create_replication_task(self, ReplicationTaskIdentifier: str, SourceEndpointArn: str, TargetEndpointArn: str, ReplicationInstanceArn: str, MigrationType: str, TableMappings: str, ReplicationTaskSettings: str = None, CdcStartTime: datetime = None, CdcStartPosition: str = None, CdcStopPosition: str = None, Tags: List = None) -> Dict:
        pass

    def delete_certificate(self, CertificateArn: str) -> Dict:
        pass

    def delete_endpoint(self, EndpointArn: str) -> Dict:
        pass

    def delete_event_subscription(self, SubscriptionName: str) -> Dict:
        pass

    def delete_replication_instance(self, ReplicationInstanceArn: str) -> Dict:
        pass

    def delete_replication_subnet_group(self, ReplicationSubnetGroupIdentifier: str) -> Dict:
        pass

    def delete_replication_task(self, ReplicationTaskArn: str) -> Dict:
        pass

    def describe_account_attributes(self) -> Dict:
        pass

    def describe_certificates(self, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_connections(self, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_endpoint_types(self, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_endpoints(self, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_event_categories(self, SourceType: str = None, Filters: List = None) -> Dict:
        pass

    def describe_event_subscriptions(self, SubscriptionName: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_events(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, EventCategories: List = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_orderable_replication_instances(self, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_refresh_schemas_status(self, EndpointArn: str) -> Dict:
        pass

    def describe_replication_instance_task_logs(self, ReplicationInstanceArn: str, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_replication_instances(self, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_replication_subnet_groups(self, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_replication_task_assessment_results(self, ReplicationTaskArn: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_replication_tasks(self, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_schemas(self, EndpointArn: str, MaxRecords: int = None, Marker: str = None) -> Dict:
        pass

    def describe_table_statistics(self, ReplicationTaskArn: str, MaxRecords: int = None, Marker: str = None, Filters: List = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def import_certificate(self, CertificateIdentifier: str, CertificatePem: str = None, CertificateWallet: bytes = None, Tags: List = None) -> Dict:
        pass

    def list_tags_for_resource(self, ResourceArn: str) -> Dict:
        pass

    def modify_endpoint(self, EndpointArn: str, EndpointIdentifier: str = None, EndpointType: str = None, EngineName: str = None, Username: str = None, Password: str = None, ServerName: str = None, Port: int = None, DatabaseName: str = None, ExtraConnectionAttributes: str = None, CertificateArn: str = None, SslMode: str = None, ServiceAccessRoleArn: str = None, ExternalTableDefinition: str = None, DynamoDbSettings: Dict = None, S3Settings: Dict = None, DmsTransferSettings: Dict = None, MongoDbSettings: Dict = None) -> Dict:
        pass

    def modify_event_subscription(self, SubscriptionName: str, SnsTopicArn: str = None, SourceType: str = None, EventCategories: List = None, Enabled: bool = None) -> Dict:
        pass

    def modify_replication_instance(self, ReplicationInstanceArn: str, AllocatedStorage: int = None, ApplyImmediately: bool = None, ReplicationInstanceClass: str = None, VpcSecurityGroupIds: List = None, PreferredMaintenanceWindow: str = None, MultiAZ: bool = None, EngineVersion: str = None, AllowMajorVersionUpgrade: bool = None, AutoMinorVersionUpgrade: bool = None, ReplicationInstanceIdentifier: str = None) -> Dict:
        pass

    def modify_replication_subnet_group(self, ReplicationSubnetGroupIdentifier: str, SubnetIds: List, ReplicationSubnetGroupDescription: str = None) -> Dict:
        pass

    def modify_replication_task(self, ReplicationTaskArn: str, ReplicationTaskIdentifier: str = None, MigrationType: str = None, TableMappings: str = None, ReplicationTaskSettings: str = None, CdcStartTime: datetime = None, CdcStartPosition: str = None, CdcStopPosition: str = None) -> Dict:
        pass

    def reboot_replication_instance(self, ReplicationInstanceArn: str, ForceFailover: bool = None) -> Dict:
        pass

    def refresh_schemas(self, EndpointArn: str, ReplicationInstanceArn: str) -> Dict:
        pass

    def reload_tables(self, ReplicationTaskArn: str, TablesToReload: List, ReloadOption: str = None) -> Dict:
        pass

    def remove_tags_from_resource(self, ResourceArn: str, TagKeys: List) -> Dict:
        pass

    def start_replication_task(self, ReplicationTaskArn: str, StartReplicationTaskType: str, CdcStartTime: datetime = None, CdcStartPosition: str = None, CdcStopPosition: str = None) -> Dict:
        pass

    def start_replication_task_assessment(self, ReplicationTaskArn: str) -> Dict:
        pass

    def stop_replication_task(self, ReplicationTaskArn: str) -> Dict:
        pass

    def test_connection(self, ReplicationInstanceArn: str, EndpointArn: str) -> Dict:
        pass
