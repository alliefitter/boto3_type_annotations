from typing import Dict
from botocore.paginate import Paginator


class ListDetectors(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListFilters(Paginator):
    def paginate(self, DetectorId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListFindings(Paginator):
    def paginate(self, DetectorId: str, FindingCriteria: Dict = None, SortCriteria: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListIPSets(Paginator):
    def paginate(self, DetectorId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListInvitations(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListMembers(Paginator):
    def paginate(self, DetectorId: str, OnlyAssociated: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListThreatIntelSets(Paginator):
    def paginate(self, DetectorId: str, PaginationConfig: Dict = None) -> Dict:
        pass
