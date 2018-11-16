from typing import Dict
from botocore.waiter import Waiter


class InstanceProfileExists(Waiter):
    def wait(self, InstanceProfileName: str, WaiterConfig: Dict = None):
        pass


class UserExists(Waiter):
    def wait(self, UserName: str = None, WaiterConfig: Dict = None):
        pass
