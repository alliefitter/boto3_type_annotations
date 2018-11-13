from typing import NoReturn
from typing import Dict
from botocore.waiter import Waiter


class StreamExists(Waiter):
    def wait(self, StreamName: str, Limit: int = None, ExclusiveStartShardId: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class StreamNotExists(Waiter):
    def wait(self, StreamName: str, Limit: int = None, ExclusiveStartShardId: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass
