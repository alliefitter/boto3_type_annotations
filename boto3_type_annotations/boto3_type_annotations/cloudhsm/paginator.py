from typing import Dict
from botocore.paginate import Paginator


class ListHapgs(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListHsms(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListLunaClients(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
