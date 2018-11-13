from typing import Dict
from botocore.paginate import Paginator


class GetQueryResults(Paginator):
    def paginate(self, QueryExecutionId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListNamedQueries(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListQueryExecutions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
