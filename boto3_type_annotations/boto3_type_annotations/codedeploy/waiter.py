from typing import Dict
from botocore.waiter import Waiter


class DeploymentSuccessful(Waiter):
    def wait(self, deploymentId: str, WaiterConfig: Dict = None):
        pass
