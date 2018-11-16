from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def associate_drt_log_bucket(self, LogBucket: str) -> Dict:
        pass

    def associate_drt_role(self, RoleArn: str) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_protection(self, Name: str, ResourceArn: str) -> Dict:
        pass

    def create_subscription(self) -> Dict:
        pass

    def delete_protection(self, ProtectionId: str) -> Dict:
        pass

    def delete_subscription(self) -> Dict:
        pass

    def describe_attack(self, AttackId: str) -> Dict:
        pass

    def describe_drt_access(self) -> Dict:
        pass

    def describe_emergency_contact_settings(self) -> Dict:
        pass

    def describe_protection(self, ProtectionId: str) -> Dict:
        pass

    def describe_subscription(self) -> Dict:
        pass

    def disassociate_drt_log_bucket(self, LogBucket: str) -> Dict:
        pass

    def disassociate_drt_role(self) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_subscription_state(self) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_attacks(self, ResourceArns: List = None, StartTime: Dict = None, EndTime: Dict = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_protections(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def update_emergency_contact_settings(self, EmergencyContactList: List = None) -> Dict:
        pass

    def update_subscription(self, AutoRenew: str = None) -> Dict:
        pass
