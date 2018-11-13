from typing import NoReturn
from typing import Dict
from botocore.waiter import Waiter


class DistributionDeployed(Waiter):
    def wait(self, Id: str, WaiterConfig: Dict = None) -> NoReturn:
        pass


class InvalidationCompleted(Waiter):
    def wait(self, DistributionId: str, Id: str, WaiterConfig: Dict = None) -> NoReturn:
        pass


class StreamingDistributionDeployed(Waiter):
    def wait(self, Id: str, WaiterConfig: Dict = None) -> NoReturn:
        pass
