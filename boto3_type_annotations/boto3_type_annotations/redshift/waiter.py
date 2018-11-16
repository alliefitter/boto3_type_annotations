from datetime import datetime
from typing import NoReturn
from typing import List
from typing import Dict
from botocore.waiter import Waiter


class ClusterAvailable(Waiter):
    def wait(self, ClusterIdentifier: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class ClusterDeleted(Waiter):
    def wait(self, ClusterIdentifier: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class ClusterRestored(Waiter):
    def wait(self, ClusterIdentifier: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class SnapshotAvailable(Waiter):
    def wait(self, ClusterIdentifier: str = None, SnapshotIdentifier: str = None, SnapshotType: str = None, StartTime: datetime = None, EndTime: datetime = None, MaxRecords: int = None, Marker: str = None, OwnerAccount: str = None, TagKeys: List = None, TagValues: List = None, ClusterExists: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass
