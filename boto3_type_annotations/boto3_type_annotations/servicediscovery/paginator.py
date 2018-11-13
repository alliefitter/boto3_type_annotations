from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListInstances(Paginator):
    def paginate(self, ServiceId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListNamespaces(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListOperations(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListServices(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
