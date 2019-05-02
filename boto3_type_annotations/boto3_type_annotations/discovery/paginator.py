from typing import Dict
from typing import List
from botocore.paginate import Paginator


class DescribeAgents(Paginator):
    def paginate(self, agentIds: List = None, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeContinuousExports(Paginator):
    def paginate(self, exportIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeExportConfigurations(Paginator):
    def paginate(self, exportIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeExportTasks(Paginator):
    def paginate(self, exportIds: List = None, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeTags(Paginator):
    def paginate(self, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListConfigurations(Paginator):
    def paginate(self, configurationType: str, filters: List = None, orderBy: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
