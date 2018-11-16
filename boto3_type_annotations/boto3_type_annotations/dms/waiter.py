from typing import NoReturn
from typing import List
from typing import Dict
from botocore.waiter import Waiter


class EndpointDeleted(Waiter):
    def wait(self, Filters: List = None, MaxRecords: int = None, Marker: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class ReplicationInstanceAvailable(Waiter):
    def wait(self, Filters: List = None, MaxRecords: int = None, Marker: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class ReplicationInstanceDeleted(Waiter):
    def wait(self, Filters: List = None, MaxRecords: int = None, Marker: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class ReplicationTaskDeleted(Waiter):
    def wait(self, Filters: List = None, MaxRecords: int = None, Marker: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class ReplicationTaskReady(Waiter):
    def wait(self, Filters: List = None, MaxRecords: int = None, Marker: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class ReplicationTaskRunning(Waiter):
    def wait(self, Filters: List = None, MaxRecords: int = None, Marker: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class ReplicationTaskStopped(Waiter):
    def wait(self, Filters: List = None, MaxRecords: int = None, Marker: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class TestConnectionSucceeds(Waiter):
    def wait(self, Filters: List = None, MaxRecords: int = None, Marker: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass
