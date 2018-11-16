from datetime import datetime
from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def claim_devices_by_claim_code(self, ClaimCode: str) -> Dict:
        pass

    def describe_device(self, DeviceId: str) -> Dict:
        pass

    def finalize_device_claim(self, DeviceId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_device_methods(self, DeviceId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def initiate_device_claim(self, DeviceId: str) -> Dict:
        pass

    def invoke_device_method(self, DeviceId: str, DeviceMethod: Dict = None, DeviceMethodParameters: str = None) -> Dict:
        pass

    def list_device_events(self, DeviceId: str, FromTimeStamp: datetime, ToTimeStamp: datetime, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_devices(self, DeviceType: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def unclaim_device(self, DeviceId: str) -> Dict:
        pass

    def update_device_state(self, DeviceId: str, Enabled: bool = None) -> Dict:
        pass
