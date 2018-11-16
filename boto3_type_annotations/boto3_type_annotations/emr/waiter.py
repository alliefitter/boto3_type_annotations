from typing import Dict
from botocore.waiter import Waiter


class ClusterRunning(Waiter):
    def wait(self, ClusterId: str, WaiterConfig: Dict = None):
        pass


class ClusterTerminated(Waiter):
    def wait(self, ClusterId: str, WaiterConfig: Dict = None):
        pass


class StepComplete(Waiter):
    def wait(self, ClusterId: str, StepId: str, WaiterConfig: Dict = None):
        pass
