from typing import List
from datetime import datetime
from typing import Dict
from botocore.paginate import Paginator


class BatchGetTraces(Paginator):
    def paginate(self, TraceIds: List, PaginationConfig: Dict = None) -> Dict:
        pass


class GetGroups(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetSamplingRules(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetSamplingStatisticSummaries(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetServiceGraph(Paginator):
    def paginate(self, StartTime: datetime, EndTime: datetime, GroupName: str = None, GroupARN: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetTraceGraph(Paginator):
    def paginate(self, TraceIds: List, PaginationConfig: Dict = None) -> Dict:
        pass


class GetTraceSummaries(Paginator):
    def paginate(self, StartTime: datetime, EndTime: datetime, Sampling: bool = None, FilterExpression: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
