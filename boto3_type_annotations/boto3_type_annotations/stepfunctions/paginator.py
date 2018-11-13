from typing import Dict
from botocore.paginate import Paginator


class GetExecutionHistory(Paginator):
    def paginate(self, executionArn: str, reverseOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListActivities(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListExecutions(Paginator):
    def paginate(self, stateMachineArn: str, statusFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListStateMachines(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
