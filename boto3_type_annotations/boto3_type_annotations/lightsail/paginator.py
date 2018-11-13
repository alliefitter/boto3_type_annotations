from typing import Dict
from botocore.paginate import Paginator


class GetActiveNames(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetBlueprints(Paginator):
    def paginate(self, includeInactive: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetBundles(Paginator):
    def paginate(self, includeInactive: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetDomains(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetInstanceSnapshots(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetInstances(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetKeyPairs(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetOperations(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetStaticIps(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
