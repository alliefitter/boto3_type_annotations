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
    def batch_get_item(self, RequestItems: Dict, ReturnConsumedCapacity: str = None) -> Dict:
        pass

    def batch_write_item(self, RequestItems: Dict, ReturnConsumedCapacity: str = None, ReturnItemCollectionMetrics: str = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_backup(self, TableName: str, BackupName: str) -> Dict:
        pass

    def create_global_table(self, GlobalTableName: str, ReplicationGroup: List) -> Dict:
        pass

    def create_table(self, AttributeDefinitions: List, TableName: str, KeySchema: List, ProvisionedThroughput: Dict, LocalSecondaryIndexes: List = None, GlobalSecondaryIndexes: List = None, StreamSpecification: Dict = None, SSESpecification: Dict = None) -> Dict:
        pass

    def delete_backup(self, BackupArn: str) -> Dict:
        pass

    def delete_item(self, TableName: str, Key: Dict, Expected: Dict = None, ConditionalOperator: str = None, ReturnValues: str = None, ReturnConsumedCapacity: str = None, ReturnItemCollectionMetrics: str = None, ConditionExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None) -> Dict:
        pass

    def delete_table(self, TableName: str) -> Dict:
        pass

    def describe_backup(self, BackupArn: str) -> Dict:
        pass

    def describe_continuous_backups(self, TableName: str) -> Dict:
        pass

    def describe_endpoints(self) -> Dict:
        pass

    def describe_global_table(self, GlobalTableName: str) -> Dict:
        pass

    def describe_global_table_settings(self, GlobalTableName: str) -> Dict:
        pass

    def describe_limits(self) -> Dict:
        pass

    def describe_table(self, TableName: str) -> Dict:
        pass

    def describe_time_to_live(self, TableName: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_item(self, TableName: str, Key: Dict, AttributesToGet: List = None, ConsistentRead: bool = None, ReturnConsumedCapacity: str = None, ProjectionExpression: str = None, ExpressionAttributeNames: Dict = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_backups(self, TableName: str = None, Limit: int = None, TimeRangeLowerBound: datetime = None, TimeRangeUpperBound: datetime = None, ExclusiveStartBackupArn: str = None, BackupType: str = None) -> Dict:
        pass

    def list_global_tables(self, ExclusiveStartGlobalTableName: str = None, Limit: int = None, RegionName: str = None) -> Dict:
        pass

    def list_tables(self, ExclusiveStartTableName: str = None, Limit: int = None) -> Dict:
        pass

    def list_tags_of_resource(self, ResourceArn: str, NextToken: str = None) -> Dict:
        pass

    def put_item(self, TableName: str, Item: Dict, Expected: Dict = None, ReturnValues: str = None, ReturnConsumedCapacity: str = None, ReturnItemCollectionMetrics: str = None, ConditionalOperator: str = None, ConditionExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None) -> Dict:
        pass

    def query(self, TableName: str, IndexName: str = None, Select: str = None, AttributesToGet: List = None, Limit: int = None, ConsistentRead: bool = None, KeyConditions: Dict = None, QueryFilter: Dict = None, ConditionalOperator: str = None, ScanIndexForward: bool = None, ExclusiveStartKey: Dict = None, ReturnConsumedCapacity: str = None, ProjectionExpression: str = None, FilterExpression: str = None, KeyConditionExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None) -> Dict:
        pass

    def restore_table_from_backup(self, TargetTableName: str, BackupArn: str) -> Dict:
        pass

    def restore_table_to_point_in_time(self, SourceTableName: str, TargetTableName: str, UseLatestRestorableTime: bool = None, RestoreDateTime: datetime = None) -> Dict:
        pass

    def scan(self, TableName: str, IndexName: str = None, AttributesToGet: List = None, Limit: int = None, Select: str = None, ScanFilter: Dict = None, ConditionalOperator: str = None, ExclusiveStartKey: Dict = None, ReturnConsumedCapacity: str = None, TotalSegments: int = None, Segment: int = None, ProjectionExpression: str = None, FilterExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None, ConsistentRead: bool = None) -> Dict:
        pass

    def tag_resource(self, ResourceArn: str, Tags: List) -> NoReturn:
        pass

    def untag_resource(self, ResourceArn: str, TagKeys: List) -> NoReturn:
        pass

    def update_continuous_backups(self, TableName: str, PointInTimeRecoverySpecification: Dict) -> Dict:
        pass

    def update_global_table(self, GlobalTableName: str, ReplicaUpdates: List) -> Dict:
        pass

    def update_global_table_settings(self, GlobalTableName: str, GlobalTableProvisionedWriteCapacityUnits: int = None, GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate: Dict = None, GlobalTableGlobalSecondaryIndexSettingsUpdate: List = None, ReplicaSettingsUpdate: List = None) -> Dict:
        pass

    def update_item(self, TableName: str, Key: Dict, AttributeUpdates: Dict = None, Expected: Dict = None, ConditionalOperator: str = None, ReturnValues: str = None, ReturnConsumedCapacity: str = None, ReturnItemCollectionMetrics: str = None, UpdateExpression: str = None, ConditionExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None) -> Dict:
        pass

    def update_table(self, TableName: str, AttributeDefinitions: List = None, ProvisionedThroughput: Dict = None, GlobalSecondaryIndexUpdates: List = None, StreamSpecification: Dict = None, SSESpecification: Dict = None) -> Dict:
        pass

    def update_time_to_live(self, TableName: str, TimeToLiveSpecification: Dict) -> Dict:
        pass
