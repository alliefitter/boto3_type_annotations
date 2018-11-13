from typing import Dict
from botocore.paginate import Paginator


class GetWorkflowExecutionHistory(Paginator):
    def paginate(self, domain: str, execution: Dict, reverseOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListActivityTypes(Paginator):
    def paginate(self, domain: str, registrationStatus: str, name: str = None, reverseOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListClosedWorkflowExecutions(Paginator):
    def paginate(self, domain: str, startTimeFilter: Dict = None, closeTimeFilter: Dict = None, executionFilter: Dict = None, closeStatusFilter: Dict = None, typeFilter: Dict = None, tagFilter: Dict = None, reverseOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDomains(Paginator):
    def paginate(self, registrationStatus: str, reverseOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListOpenWorkflowExecutions(Paginator):
    def paginate(self, domain: str, startTimeFilter: Dict, typeFilter: Dict = None, tagFilter: Dict = None, reverseOrder: bool = None, executionFilter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListWorkflowTypes(Paginator):
    def paginate(self, domain: str, registrationStatus: str, name: str = None, reverseOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class PollForDecisionTask(Paginator):
    def paginate(self, domain: str, taskList: Dict, identity: str = None, reverseOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass
