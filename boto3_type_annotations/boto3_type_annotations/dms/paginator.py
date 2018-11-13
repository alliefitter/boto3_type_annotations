from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeCertificates(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeConnections(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEndpointTypes(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEndpoints(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEventSubscriptions(Paginator):
    def paginate(self, SubscriptionName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEvents(Paginator):
    def paginate(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, EventCategories: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeOrderableReplicationInstances(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeReplicationInstances(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeReplicationSubnetGroups(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeReplicationTaskAssessmentResults(Paginator):
    def paginate(self, ReplicationTaskArn: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeReplicationTasks(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeSchemas(Paginator):
    def paginate(self, EndpointArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeTableStatistics(Paginator):
    def paginate(self, ReplicationTaskArn: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
