from typing import Dict
from typing import List
from botocore.paginate import Paginator


class DescribeAccountLimits(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeChangeSet(Paginator):
    def paginate(self, ChangeSetName: str, StackName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeStackEvents(Paginator):
    def paginate(self, StackName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeStacks(Paginator):
    def paginate(self, StackName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListChangeSets(Paginator):
    def paginate(self, StackName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListExports(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListImports(Paginator):
    def paginate(self, ExportName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListStackInstances(Paginator):
    def paginate(self, StackSetName: str, StackInstanceAccount: str = None, StackInstanceRegion: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListStackResources(Paginator):
    def paginate(self, StackName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListStackSetOperationResults(Paginator):
    def paginate(self, StackSetName: str, OperationId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListStackSetOperations(Paginator):
    def paginate(self, StackSetName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListStackSets(Paginator):
    def paginate(self, Status: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListStacks(Paginator):
    def paginate(self, StackStatusFilter: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
