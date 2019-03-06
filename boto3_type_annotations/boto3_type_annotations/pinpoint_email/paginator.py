from typing import Dict
from botocore.paginate import Paginator


class GetDedicatedIps(Paginator):
    def paginate(self, PoolName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListConfigurationSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDedicatedIpPools(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDeliverabilityTestReports(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListEmailIdentities(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
