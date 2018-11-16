from typing import Optional
from typing import Union
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient
from typing import IO


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def delete_object(self, Path: str) -> Dict:
        pass

    def describe_object(self, Path: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_object(self, Path: str, Range: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_items(self, Path: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def put_object(self, Body: Union[bytes, IO], Path: str, ContentType: str = None, CacheControl: str = None, StorageClass: str = None) -> Dict:
        pass
