from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListAssignmentsForHIT(Paginator):
    def paginate(self, HITId: str, AssignmentStatuses: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListBonusPayments(Paginator):
    def paginate(self, HITId: str = None, AssignmentId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListHITs(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListHITsForQualificationType(Paginator):
    def paginate(self, QualificationTypeId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListQualificationRequests(Paginator):
    def paginate(self, QualificationTypeId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListQualificationTypes(Paginator):
    def paginate(self, MustBeRequestable: bool, Query: str = None, MustBeOwnedByCaller: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListReviewableHITs(Paginator):
    def paginate(self, HITTypeId: str = None, Status: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListWorkerBlocks(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListWorkersWithQualificationType(Paginator):
    def paginate(self, QualificationTypeId: str, Status: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
