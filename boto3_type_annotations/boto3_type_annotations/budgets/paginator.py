from typing import Dict
from botocore.paginate import Paginator


class DescribeBudgets(Paginator):
    def paginate(self, AccountId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeNotificationsForBudget(Paginator):
    def paginate(self, AccountId: str, BudgetName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeSubscribersForNotification(Paginator):
    def paginate(self, AccountId: str, BudgetName: str, Notification: Dict, PaginationConfig: Dict = None) -> Dict:
        pass
