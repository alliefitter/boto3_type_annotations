from typing import NoReturn
from typing import List
from typing import Dict
from botocore.waiter import Waiter


class FleetStarted(Waiter):
    def wait(self, Names: List = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class FleetStopped(Waiter):
    def wait(self, Names: List = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        pass
