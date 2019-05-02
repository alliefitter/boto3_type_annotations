from typing import Dict
from botocore.waiter import Waiter


class FunctionExists(Waiter):
    def wait(self, FunctionName: str, Qualifier: str = None, WaiterConfig: Dict = None):
        pass
