from datetime import datetime
from typing import Dict
from botocore.paginate import Paginator


class ListDeviceEvents(Paginator):
    def paginate(self, DeviceId: str, FromTimeStamp: datetime, ToTimeStamp: datetime, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDevices(Paginator):
    def paginate(self, DeviceType: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
