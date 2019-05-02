from typing import Dict
from botocore.waiter import Waiter


class InstanceProfileExists(Waiter):
    def wait(self, InstanceProfileName: str, WaiterConfig: Dict = None):
        pass


class PolicyExists(Waiter):
    def wait(self, PolicyArn: str, WaiterConfig: Dict = None):
        pass


class RoleExists(Waiter):
    def wait(self, RoleName: str, WaiterConfig: Dict = None):
        pass


class UserExists(Waiter):
    def wait(self, UserName: str = None, WaiterConfig: Dict = None):
        pass
