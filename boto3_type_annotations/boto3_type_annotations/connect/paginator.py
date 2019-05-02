from typing import Dict
from typing import List
from datetime import datetime
from botocore.paginate import Paginator


class GetMetricData(Paginator):
    def paginate(self, InstanceId: str, StartTime: datetime, EndTime: datetime, Filters: Dict, HistoricalMetrics: List, Groupings: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListRoutingProfiles(Paginator):
    def paginate(self, InstanceId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSecurityProfiles(Paginator):
    def paginate(self, InstanceId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListUserHierarchyGroups(Paginator):
    def paginate(self, InstanceId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListUsers(Paginator):
    def paginate(self, InstanceId: str, PaginationConfig: Dict = None) -> Dict:
        pass
