from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeStackEvents(Paginator):
    def paginate(self, StackName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeStacks(Paginator):
    def paginate(self, StackName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListExports(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListImports(Paginator):
    def paginate(self, ExportName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListStackResources(Paginator):
    def paginate(self, StackName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListStacks(Paginator):
    def paginate(self, StackStatusFilter: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
