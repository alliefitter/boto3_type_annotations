from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from boto3.resources.collection import ResourceCollection
from typing import Dict
from boto3.resources import base


class ServiceResource(base.ServiceResource):
    tables: 'tables'

    def Table(self, name: str = None) -> 'Table':
        pass

    def batch_get_item(self, RequestItems: Dict, ReturnConsumedCapacity: str = None) -> Dict:
        pass

    def batch_write_item(self, RequestItems: Dict, ReturnConsumedCapacity: str = None, ReturnItemCollectionMetrics: str = None) -> Dict:
        pass

    def create_table(self, AttributeDefinitions: List, TableName: str, KeySchema: List, ProvisionedThroughput: Dict, LocalSecondaryIndexes: List = None, GlobalSecondaryIndexes: List = None, StreamSpecification: Dict = None, SSESpecification: Dict = None) -> 'Table':
        pass

    def get_available_subresources(self) -> List[str]:
        pass


class Table(base.ServiceResource):
    attribute_definitions: List
    table_name: str
    key_schema: List
    table_status: str
    creation_date_time: datetime
    provisioned_throughput: Dict
    table_size_bytes: int
    item_count: int
    table_arn: str
    table_id: str
    local_secondary_indexes: List
    global_secondary_indexes: List
    stream_specification: Dict
    latest_stream_label: str
    latest_stream_arn: str
    restore_summary: Dict
    sse_description: Dict
    name: str

    def batch_writer(self, overwrite_by_pkeys: List[str] = None):
        pass

    def delete(self) -> Dict:
        pass

    def delete_item(self, Key: Dict, Expected: Dict = None, ConditionalOperator: str = None, ReturnValues: str = None, ReturnConsumedCapacity: str = None, ReturnItemCollectionMetrics: str = None, ConditionExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None) -> Dict:
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def get_item(self, Key: Dict, AttributesToGet: List = None, ConsistentRead: bool = None, ReturnConsumedCapacity: str = None, ProjectionExpression: str = None, ExpressionAttributeNames: Dict = None) -> Dict:
        pass

    def load(self):
        pass

    def put_item(self, Item: Dict, Expected: Dict = None, ReturnValues: str = None, ReturnConsumedCapacity: str = None, ReturnItemCollectionMetrics: str = None, ConditionalOperator: str = None, ConditionExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None) -> Dict:
        pass

    def query(self, IndexName: str = None, Select: str = None, AttributesToGet: List = None, Limit: int = None, ConsistentRead: bool = None, KeyConditions: Dict = None, QueryFilter: Dict = None, ConditionalOperator: str = None, ScanIndexForward: bool = None, ExclusiveStartKey: Dict = None, ReturnConsumedCapacity: str = None, ProjectionExpression: str = None, FilterExpression: str = None, KeyConditionExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None) -> Dict:
        pass

    def reload(self):
        pass

    def scan(self, IndexName: str = None, AttributesToGet: List = None, Limit: int = None, Select: str = None, ScanFilter: Dict = None, ConditionalOperator: str = None, ExclusiveStartKey: Dict = None, ReturnConsumedCapacity: str = None, TotalSegments: int = None, Segment: int = None, ProjectionExpression: str = None, FilterExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None, ConsistentRead: bool = None) -> Dict:
        pass

    def update(self, AttributeDefinitions: List = None, ProvisionedThroughput: Dict = None, GlobalSecondaryIndexUpdates: List = None, StreamSpecification: Dict = None, SSESpecification: Dict = None) -> 'Table':
        pass

    def update_item(self, Key: Dict, AttributeUpdates: Dict = None, Expected: Dict = None, ConditionalOperator: str = None, ReturnValues: str = None, ReturnConsumedCapacity: str = None, ReturnItemCollectionMetrics: str = None, UpdateExpression: str = None, ConditionExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None) -> Dict:
        pass

    def wait_until_exists(self):
        pass

    def wait_until_not_exists(self):
        pass


class tables(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Table']:
        pass

    
    @classmethod
    def filter(cls, ExclusiveStartTableName: str = None, Limit: int = None) -> List['Table']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Table']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Table']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass
