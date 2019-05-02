from typing import Dict
from typing import List
from botocore.paginate import Paginator


class DescribeDestinations(Paginator):
    def paginate(self, DestinationNamePrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeExportTasks(Paginator):
    def paginate(self, taskId: str = None, statusCode: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeLogGroups(Paginator):
    def paginate(self, logGroupNamePrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeLogStreams(Paginator):
    def paginate(self, logGroupName: str, logStreamNamePrefix: str = None, orderBy: str = None, descending: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeMetricFilters(Paginator):
    def paginate(self, logGroupName: str = None, filterNamePrefix: str = None, metricName: str = None, metricNamespace: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeQueries(Paginator):
    def paginate(self, logGroupName: str = None, status: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeResourcePolicies(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeSubscriptionFilters(Paginator):
    def paginate(self, logGroupName: str, filterNamePrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class FilterLogEvents(Paginator):
    def paginate(self, logGroupName: str, logStreamNames: List = None, logStreamNamePrefix: str = None, startTime: int = None, endTime: int = None, filterPattern: str = None, interleaved: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass
