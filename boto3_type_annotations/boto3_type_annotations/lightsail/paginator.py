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


class GetCloudFormationStackRecords(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetDiskSnapshots(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetDisks(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetDomains(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetExportSnapshotRecords(Paginator):
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


class GetLoadBalancers(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetOperations(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetRelationalDatabaseBlueprints(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetRelationalDatabaseBundles(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetRelationalDatabaseEvents(Paginator):
    def paginate(self, relationalDatabaseName: str, durationInMinutes: int = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetRelationalDatabaseParameters(Paginator):
    def paginate(self, relationalDatabaseName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class GetRelationalDatabaseSnapshots(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetRelationalDatabases(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetStaticIps(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
