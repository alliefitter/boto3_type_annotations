from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def describe_services(self, ServiceCode: str = None, FormatVersion: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_attribute_values(self, ServiceCode: str, AttributeName: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_products(self, ServiceCode: str = None, Filters: List = None, FormatVersion: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass
