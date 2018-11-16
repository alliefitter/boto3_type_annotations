from typing import Dict
from botocore.waiter import Waiter


class ResourceRecordSetsChanged(Waiter):
    def wait(self, Id: str, WaiterConfig: Dict = None):
        pass
