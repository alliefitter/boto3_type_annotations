from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListGroupResources(Paginator):
    def paginate(self, GroupName: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListGroups(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class SearchResources(Paginator):
    def paginate(self, ResourceQuery: Dict, PaginationConfig: Dict = None) -> Dict:
        pass
