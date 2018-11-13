from datetime import datetime
from typing import NoReturn
from typing import Dict
from botocore.waiter import Waiter


class BucketExists(Waiter):
    def wait(self, Bucket: str, WaiterConfig: Dict = None) -> NoReturn:
        pass


class BucketNotExists(Waiter):
    def wait(self, Bucket: str, WaiterConfig: Dict = None) -> NoReturn:
        pass


class ObjectExists(Waiter):
    def wait(self, Bucket: str, Key: str, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None, WaiterConfig: Dict = None) -> NoReturn:
        pass


class ObjectNotExists(Waiter):
    def wait(self, Bucket: str, Key: str, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None, WaiterConfig: Dict = None) -> NoReturn:
        pass
