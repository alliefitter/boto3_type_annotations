from typing import Dict
from typing import List
from botocore.paginate import Paginator


class GetEnabledStandards(Paginator):
    def paginate(self, StandardsSubscriptionArns: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetFindings(Paginator):
    def paginate(self, Filters: Dict = None, SortCriteria: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetInsights(Paginator):
    def paginate(self, InsightArns: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListEnabledProductsForImport(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListInvitations(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListMembers(Paginator):
    def paginate(self, OnlyAssociated: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass
