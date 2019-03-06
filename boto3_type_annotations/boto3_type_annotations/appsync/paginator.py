from typing import Dict
from botocore.paginate import Paginator


class ListApiKeys(Paginator):
    def paginate(self, apiId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDataSources(Paginator):
    def paginate(self, apiId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListFunctions(Paginator):
    def paginate(self, apiId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListGraphqlApis(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListResolvers(Paginator):
    def paginate(self, apiId: str, typeName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListResolversByFunction(Paginator):
    def paginate(self, apiId: str, functionId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTypes(Paginator):
    def paginate(self, apiId: str, format: str, PaginationConfig: Dict = None) -> Dict:
        pass
