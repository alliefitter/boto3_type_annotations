from typing import List
from typing import Dict
from botocore.waiter import Waiter


class DBInstanceAvailable(Waiter):
    def wait(self, DBInstanceIdentifier: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, WaiterConfig: Dict = None):
        pass


class DBInstanceDeleted(Waiter):
    def wait(self, DBInstanceIdentifier: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, WaiterConfig: Dict = None):
        pass
