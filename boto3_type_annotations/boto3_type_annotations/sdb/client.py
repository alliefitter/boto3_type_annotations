from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def batch_delete_attributes(self, DomainName: str, Items: List):
        pass

    def batch_put_attributes(self, DomainName: str, Items: List):
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_domain(self, DomainName: str):
        pass

    def delete_attributes(self, DomainName: str, ItemName: str, Attributes: List = None, Expected: Dict = None):
        pass

    def delete_domain(self, DomainName: str):
        pass

    def domain_metadata(self, DomainName: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_attributes(self, DomainName: str, ItemName: str, AttributeNames: List = None, ConsistentRead: bool = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_domains(self, MaxNumberOfDomains: int = None, NextToken: str = None) -> Dict:
        pass

    def put_attributes(self, DomainName: str, ItemName: str, Attributes: List, Expected: Dict = None):
        pass

    def select(self, SelectExpression: str, NextToken: str = None, ConsistentRead: bool = None) -> Dict:
        pass
