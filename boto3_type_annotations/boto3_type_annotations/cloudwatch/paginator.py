from typing import Dict
from typing import List
from datetime import datetime
from botocore.paginate import Paginator


class DescribeAlarmHistory(Paginator):
    def paginate(self, AlarmName: str = None, HistoryItemType: str = None, StartDate: datetime = None, EndDate: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeAlarms(Paginator):
    def paginate(self, AlarmNames: List = None, AlarmNamePrefix: str = None, StateValue: str = None, ActionPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetMetricData(Paginator):
    def paginate(self, MetricDataQueries: List, StartTime: datetime, EndTime: datetime, ScanBy: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDashboards(Paginator):
    def paginate(self, DashboardNamePrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListMetrics(Paginator):
    def paginate(self, Namespace: str = None, MetricName: str = None, Dimensions: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
