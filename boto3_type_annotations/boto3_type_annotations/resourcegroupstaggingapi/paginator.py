from typing import List
from typing import Dict
from botocore.paginate import Paginator


class GetResources(Paginator):
    def paginate(self, TagFilters: List = None, TagsPerPage: int = None, ResourceTypeFilters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetTagKeys(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetTagValues(Paginator):
    def paginate(self, Key: str, PaginationConfig: Dict = None) -> Dict:
        pass
