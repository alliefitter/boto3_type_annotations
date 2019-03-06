from typing import Dict
from botocore.paginate import Paginator


class ListClusters(Paginator):
    def paginate(self, ClusterNameFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListNodes(Paginator):
    def paginate(self, ClusterArn: str, PaginationConfig: Dict = None) -> Dict:
        pass
