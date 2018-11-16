from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def associate_admin_account(self, AdminAccount: str) -> NoReturn:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def delete_notification_channel(self) -> NoReturn:
        pass

    def delete_policy(self, PolicyId: str) -> NoReturn:
        pass

    def disassociate_admin_account(self) -> NoReturn:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_admin_account(self) -> Dict:
        pass

    def get_compliance_detail(self, PolicyId: str, MemberAccount: str) -> Dict:
        pass

    def get_notification_channel(self) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_policy(self, PolicyId: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_compliance_status(self, PolicyId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_member_accounts(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_policies(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def put_notification_channel(self, SnsTopicArn: str, SnsRoleName: str) -> NoReturn:
        pass

    def put_policy(self, Policy: Dict) -> Dict:
        pass
