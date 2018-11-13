from typing import Dict
from botocore.paginate import Paginator


class DescribeBatchPredictions(Paginator):
    def paginate(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDataSources(Paginator):
    def paginate(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEvaluations(Paginator):
    def paginate(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeMLModels(Paginator):
    def paginate(self, FilterVariable: str = None, EQ: str = None, GT: str = None, LT: str = None, GE: str = None, LE: str = None, NE: str = None, Prefix: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
