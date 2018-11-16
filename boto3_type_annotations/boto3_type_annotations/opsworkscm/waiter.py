from typing import Dict
from botocore.waiter import Waiter


class NodeAssociated(Waiter):
    def wait(self, NodeAssociationStatusToken: str, ServerName: str, WaiterConfig: Dict = None):
        pass
