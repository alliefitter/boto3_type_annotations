from typing import Dict
from botocore.paginate import Paginator


class ListElasticsearchInstanceTypes(Paginator):
    def paginate(self, ElasticsearchVersion: str, DomainName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListElasticsearchVersions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
