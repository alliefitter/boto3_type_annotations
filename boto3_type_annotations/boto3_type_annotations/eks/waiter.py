from typing import NoReturn
from typing import Dict
from botocore.waiter import Waiter


class ClusterActive(Waiter):
    def wait(self, name: str, WaiterConfig: Dict = None) -> NoReturn:
        pass


class ClusterDeleted(Waiter):
    def wait(self, name: str, WaiterConfig: Dict = None) -> NoReturn:
        pass
