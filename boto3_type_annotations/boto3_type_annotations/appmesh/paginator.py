from typing import Dict
from botocore.paginate import Paginator


class ListMeshes(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListRoutes(Paginator):
    def paginate(self, meshName: str, virtualRouterName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTagsForResource(Paginator):
    def paginate(self, resourceArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListVirtualNodes(Paginator):
    def paginate(self, meshName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListVirtualRouters(Paginator):
    def paginate(self, meshName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListVirtualServices(Paginator):
    def paginate(self, meshName: str, PaginationConfig: Dict = None) -> Dict:
        pass
