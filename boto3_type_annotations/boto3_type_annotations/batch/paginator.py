from typing import Dict
from typing import List
from botocore.paginate import Paginator


class DescribeComputeEnvironments(Paginator):
    def paginate(self, computeEnvironments: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeJobDefinitions(Paginator):
    def paginate(self, jobDefinitions: List = None, jobDefinitionName: str = None, status: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeJobQueues(Paginator):
    def paginate(self, jobQueues: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListJobs(Paginator):
    def paginate(self, jobQueue: str = None, arrayJobId: str = None, multiNodeJobId: str = None, jobStatus: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
