from typing import Optional
from typing import Union
from typing import List
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def batch_suspend_user(self, AccountId: str, UserIdList: List) -> Dict:
        pass

    def batch_unsuspend_user(self, AccountId: str, UserIdList: List) -> Dict:
        pass

    def batch_update_user(self, AccountId: str, UpdateUserRequestItems: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_account(self, Name: str) -> Dict:
        pass

    def delete_account(self, AccountId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_account(self, AccountId: str) -> Dict:
        pass

    def get_account_settings(self, AccountId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_user(self, AccountId: str, UserId: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def invite_users(self, AccountId: str, UserEmailList: List) -> Dict:
        pass

    def list_accounts(self, Name: str = None, UserEmail: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_users(self, AccountId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def logout_user(self, AccountId: str, UserId: str) -> Dict:
        pass

    def reset_personal_pin(self, AccountId: str, UserId: str) -> Dict:
        pass

    def update_account(self, AccountId: str, Name: str = None) -> Dict:
        pass

    def update_account_settings(self, AccountId: str, AccountSettings: Dict) -> Dict:
        pass

    def update_user(self, AccountId: str, UserId: str, LicenseType: str = None) -> Dict:
        pass
