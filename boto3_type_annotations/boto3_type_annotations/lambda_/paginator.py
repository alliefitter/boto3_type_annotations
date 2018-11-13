from typing import Dict
from botocore.paginate import Paginator


class ListAliases(Paginator):
    def paginate(self, FunctionName: str, FunctionVersion: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListEventSourceMappings(Paginator):
    def paginate(self, EventSourceArn: str = None, FunctionName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListFunctions(Paginator):
    def paginate(self, MasterRegion: str = None, FunctionVersion: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
