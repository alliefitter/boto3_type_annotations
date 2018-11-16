from typing import Dict
from botocore.waiter import Waiter


class DistributionDeployed(Waiter):
    def wait(self, Id: str, WaiterConfig: Dict = None):
        pass


class InvalidationCompleted(Waiter):
    def wait(self, DistributionId: str, Id: str, WaiterConfig: Dict = None):
        pass


class StreamingDistributionDeployed(Waiter):
    def wait(self, Id: str, WaiterConfig: Dict = None):
        pass
