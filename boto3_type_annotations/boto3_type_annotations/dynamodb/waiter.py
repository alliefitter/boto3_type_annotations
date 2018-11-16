from typing import Dict
from botocore.waiter import Waiter


class TableExists(Waiter):
    def wait(self, TableName: str, WaiterConfig: Dict = None):
        pass


class TableNotExists(Waiter):
    def wait(self, TableName: str, WaiterConfig: Dict = None):
        pass
