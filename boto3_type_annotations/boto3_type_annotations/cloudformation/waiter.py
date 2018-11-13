from typing import NoReturn
from typing import Dict
from botocore.waiter import Waiter


class ChangeSetCreateComplete(Waiter):
    def wait(self, ChangeSetName: str, StackName: str = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class StackCreateComplete(Waiter):
    def wait(self, StackName: str = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class StackDeleteComplete(Waiter):
    def wait(self, StackName: str = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class StackExists(Waiter):
    def wait(self, StackName: str = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class StackUpdateComplete(Waiter):
    def wait(self, StackName: str = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass
