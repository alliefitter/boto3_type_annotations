from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeImages(Paginator):
    def paginate(self, repositoryName: str, registryId: str = None, imageIds: List = None, filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeRepositories(Paginator):
    def paginate(self, registryId: str = None, repositoryNames: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListImages(Paginator):
    def paginate(self, repositoryName: str, registryId: str = None, filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass
