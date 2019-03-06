from typing import Dict
from botocore.paginate import Paginator


class ListClusters(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListUpdates(Paginator):
    def paginate(self, name: str, PaginationConfig: Dict = None) -> Dict:
        pass
