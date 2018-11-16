from typing import Dict
from botocore.waiter import Waiter


class ClusterActive(Waiter):
    def wait(self, name: str, WaiterConfig: Dict = None):
        pass


class ClusterDeleted(Waiter):
    def wait(self, name: str, WaiterConfig: Dict = None):
        pass
