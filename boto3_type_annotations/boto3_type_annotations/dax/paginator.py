from typing import Dict
from typing import List
from datetime import datetime
from botocore.paginate import Paginator


class DescribeClusters(Paginator):
    def paginate(self, ClusterNames: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDefaultParameters(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEvents(Paginator):
    def paginate(self, SourceName: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeParameterGroups(Paginator):
    def paginate(self, ParameterGroupNames: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeParameters(Paginator):
    def paginate(self, ParameterGroupName: str, Source: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeSubnetGroups(Paginator):
    def paginate(self, SubnetGroupNames: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTags(Paginator):
    def paginate(self, ResourceName: str, PaginationConfig: Dict = None) -> Dict:
        pass
