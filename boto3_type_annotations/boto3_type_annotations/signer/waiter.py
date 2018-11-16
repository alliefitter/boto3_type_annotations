from typing import Dict
from botocore.waiter import Waiter


class SuccessfulSigningJob(Waiter):
    def wait(self, jobId: str, WaiterConfig: Dict = None):
        pass
