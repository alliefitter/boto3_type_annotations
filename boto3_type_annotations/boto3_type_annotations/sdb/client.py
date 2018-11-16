from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def batch_delete_attributes(self, DomainName: str, Items: List) -> NoReturn:
        pass

    def batch_put_attributes(self, DomainName: str, Items: List) -> NoReturn:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_domain(self, DomainName: str) -> NoReturn:
        pass

    def delete_attributes(self, DomainName: str, ItemName: str, Attributes: List = None, Expected: Dict = None) -> NoReturn:
        pass

    def delete_domain(self, DomainName: str) -> NoReturn:
        pass

    def domain_metadata(self, DomainName: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_attributes(self, DomainName: str, ItemName: str, AttributeNames: List = None, ConsistentRead: bool = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_domains(self, MaxNumberOfDomains: int = None, NextToken: str = None) -> Dict:
        pass

    def put_attributes(self, DomainName: str, ItemName: str, Attributes: List, Expected: Dict = None) -> NoReturn:
        pass

    def select(self, SelectExpression: str, NextToken: str = None, ConsistentRead: bool = None) -> Dict:
        pass
