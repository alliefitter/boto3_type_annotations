from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_budget(self, AccountId: str, Budget: Dict, NotificationsWithSubscribers: List = None) -> Dict:
        pass

    def create_notification(self, AccountId: str, BudgetName: str, Notification: Dict, Subscribers: List) -> Dict:
        pass

    def create_subscriber(self, AccountId: str, BudgetName: str, Notification: Dict, Subscriber: Dict) -> Dict:
        pass

    def delete_budget(self, AccountId: str, BudgetName: str) -> Dict:
        pass

    def delete_notification(self, AccountId: str, BudgetName: str, Notification: Dict) -> Dict:
        pass

    def delete_subscriber(self, AccountId: str, BudgetName: str, Notification: Dict, Subscriber: Dict) -> Dict:
        pass

    def describe_budget(self, AccountId: str, BudgetName: str) -> Dict:
        pass

    def describe_budget_performance_history(self, AccountId: str, BudgetName: str, TimePeriod: Dict = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_budgets(self, AccountId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_notifications_for_budget(self, AccountId: str, BudgetName: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_subscribers_for_notification(self, AccountId: str, BudgetName: str, Notification: Dict, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def update_budget(self, AccountId: str, NewBudget: Dict) -> Dict:
        pass

    def update_notification(self, AccountId: str, BudgetName: str, OldNotification: Dict, NewNotification: Dict) -> Dict:
        pass

    def update_subscriber(self, AccountId: str, BudgetName: str, Notification: Dict, OldSubscriber: Dict, NewSubscriber: Dict) -> Dict:
        pass
