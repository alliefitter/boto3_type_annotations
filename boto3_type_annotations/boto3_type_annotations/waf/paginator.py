from typing import Dict
from botocore.paginate import Paginator


class ListByteMatchSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListIPSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListRules(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSizeConstraintSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSqlInjectionMatchSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListWebACLs(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListXssMatchSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
