from typing import Dict
from botocore.waiter import Waiter


class VaultExists(Waiter):
    def wait(self, vaultName: str, accountId: str = None, WaiterConfig: Dict = None):
        pass


class VaultNotExists(Waiter):
    def wait(self, vaultName: str, accountId: str = None, WaiterConfig: Dict = None):
        pass
