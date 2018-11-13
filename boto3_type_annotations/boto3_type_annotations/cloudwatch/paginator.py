from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeAlarmHistory(Paginator):
    def paginate(self, AlarmName: str = None, HistoryItemType: str = None, StartDate: datetime = None, EndDate: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeAlarms(Paginator):
    def paginate(self, AlarmNames: List = None, AlarmNamePrefix: str = None, StateValue: str = None, ActionPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDashboards(Paginator):
    def paginate(self, DashboardNamePrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListMetrics(Paginator):
    def paginate(self, Namespace: str = None, MetricName: str = None, Dimensions: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
