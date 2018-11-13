from typing import Dict
from botocore.paginate import Paginator


class ListBundles(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListProjects(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
