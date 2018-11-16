from typing import Dict
from botocore.waiter import Waiter


class ChangeSetCreateComplete(Waiter):
    def wait(self, ChangeSetName: str, StackName: str = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class StackCreateComplete(Waiter):
    def wait(self, StackName: str = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class StackDeleteComplete(Waiter):
    def wait(self, StackName: str = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class StackExists(Waiter):
    def wait(self, StackName: str = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class StackUpdateComplete(Waiter):
    def wait(self, StackName: str = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass
