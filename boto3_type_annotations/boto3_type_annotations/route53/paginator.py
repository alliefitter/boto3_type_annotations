from typing import Dict
from botocore.paginate import Paginator


class ListHealthChecks(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListHostedZones(Paginator):
    def paginate(self, DelegationSetId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListQueryLoggingConfigs(Paginator):
    def paginate(self, HostedZoneId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListResourceRecordSets(Paginator):
    def paginate(self, HostedZoneId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListVPCAssociationAuthorizations(Paginator):
    def paginate(self, HostedZoneId: str, MaxResults: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
