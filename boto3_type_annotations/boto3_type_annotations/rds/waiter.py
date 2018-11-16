from typing import NoReturn
from typing import List
from typing import Dict
from botocore.waiter import Waiter


class DBInstanceAvailable(Waiter):
    def wait(self, DBInstanceIdentifier: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class DBInstanceDeleted(Waiter):
    def wait(self, DBInstanceIdentifier: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class DBSnapshotAvailable(Waiter):
    def wait(self, DBInstanceIdentifier: str = None, DBSnapshotIdentifier: str = None, SnapshotType: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, IncludeShared: bool = None, IncludePublic: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class DBSnapshotCompleted(Waiter):
    def wait(self, DBInstanceIdentifier: str = None, DBSnapshotIdentifier: str = None, SnapshotType: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, IncludeShared: bool = None, IncludePublic: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class DBSnapshotDeleted(Waiter):
    def wait(self, DBInstanceIdentifier: str = None, DBSnapshotIdentifier: str = None, SnapshotType: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, IncludeShared: bool = None, IncludePublic: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        pass
