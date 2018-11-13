from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeObjects(Paginator):
    def paginate(self, pipelineId: str, objectIds: List, evaluateExpressions: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPipelines(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class QueryObjects(Paginator):
    def paginate(self, pipelineId: str, sphere: str, query: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass
