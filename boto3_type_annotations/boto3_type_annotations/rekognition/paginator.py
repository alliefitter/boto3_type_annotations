from typing import Dict
from botocore.paginate import Paginator


class ListCollections(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListFaces(Paginator):
    def paginate(self, CollectionId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListStreamProcessors(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
