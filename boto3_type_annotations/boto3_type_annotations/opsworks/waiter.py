from typing import NoReturn
from typing import List
from typing import Dict
from botocore.waiter import Waiter


class AppExists(Waiter):
    def wait(self, StackId: str = None, AppIds: List = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class DeploymentSuccessful(Waiter):
    def wait(self, StackId: str = None, AppId: str = None, DeploymentIds: List = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class InstanceOnline(Waiter):
    def wait(self, StackId: str = None, LayerId: str = None, InstanceIds: List = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class InstanceRegistered(Waiter):
    def wait(self, StackId: str = None, LayerId: str = None, InstanceIds: List = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class InstanceStopped(Waiter):
    def wait(self, StackId: str = None, LayerId: str = None, InstanceIds: List = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class InstanceTerminated(Waiter):
    def wait(self, StackId: str = None, LayerId: str = None, InstanceIds: List = None, WaiterConfig: Dict = None) -> NoReturn:
        pass
