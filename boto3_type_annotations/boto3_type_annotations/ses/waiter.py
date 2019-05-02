from typing import Dict
from typing import List
from botocore.waiter import Waiter


class IdentityExists(Waiter):
    def wait(self, Identities: List, WaiterConfig: Dict = None):
        pass
