from typing import NoReturn
from typing import Dict
from botocore.waiter import Waiter


class SuccessfulSigningJob(Waiter):
    def wait(self, jobId: str, WaiterConfig: Dict = None) -> NoReturn:
        pass
