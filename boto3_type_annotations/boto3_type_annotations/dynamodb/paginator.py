from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListBackups(Paginator):
    def paginate(self, TableName: str = None, TimeRangeLowerBound: datetime = None, TimeRangeUpperBound: datetime = None, BackupType: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTables(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class Query(Paginator):
    def paginate(self, TableName: str, IndexName: str = None, Select: str = None, AttributesToGet: List = None, ConsistentRead: bool = None, KeyConditions: Dict = None, QueryFilter: Dict = None, ConditionalOperator: str = None, ScanIndexForward: bool = None, ReturnConsumedCapacity: str = None, ProjectionExpression: str = None, FilterExpression: str = None, KeyConditionExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class Scan(Paginator):
    def paginate(self, TableName: str, IndexName: str = None, AttributesToGet: List = None, Select: str = None, ScanFilter: Dict = None, ConditionalOperator: str = None, ReturnConsumedCapacity: str = None, TotalSegments: int = None, Segment: int = None, ProjectionExpression: str = None, FilterExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None, ConsistentRead: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass
