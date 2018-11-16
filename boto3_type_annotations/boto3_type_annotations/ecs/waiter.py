from typing import List
from typing import Dict
from botocore.waiter import Waiter


class ServicesInactive(Waiter):
    def wait(self, services: List, cluster: str = None, WaiterConfig: Dict = None):
        pass


class ServicesStable(Waiter):
    def wait(self, services: List, cluster: str = None, WaiterConfig: Dict = None):
        pass


class TasksRunning(Waiter):
    def wait(self, tasks: List, cluster: str = None, WaiterConfig: Dict = None):
        pass


class TasksStopped(Waiter):
    def wait(self, tasks: List, cluster: str = None, WaiterConfig: Dict = None):
        pass
