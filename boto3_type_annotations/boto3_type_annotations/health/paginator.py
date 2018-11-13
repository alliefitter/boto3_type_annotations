from typing import Dict
from botocore.paginate import Paginator


class DescribeAffectedEntities(Paginator):
    def paginate(self, filter: Dict, locale: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEventAggregates(Paginator):
    def paginate(self, aggregateField: str, filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEventTypes(Paginator):
    def paginate(self, filter: Dict = None, locale: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEvents(Paginator):
    def paginate(self, filter: Dict = None, locale: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
