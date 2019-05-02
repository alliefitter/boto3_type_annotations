from typing import Dict
from typing import List
from botocore.paginate import Paginator


class GetConnectors(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetReplicationJobs(Paginator):
    def paginate(self, replicationJobId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetReplicationRuns(Paginator):
    def paginate(self, replicationJobId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class GetServers(Paginator):
    def paginate(self, vmServerAddressList: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListApps(Paginator):
    def paginate(self, appIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
