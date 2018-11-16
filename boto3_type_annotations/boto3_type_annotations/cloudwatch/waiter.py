from typing import List
from typing import Dict
from botocore.waiter import Waiter


class AlarmExists(Waiter):
    def wait(self, AlarmNames: List = None, AlarmNamePrefix: str = None, StateValue: str = None, ActionPrefix: str = None, MaxRecords: int = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass
