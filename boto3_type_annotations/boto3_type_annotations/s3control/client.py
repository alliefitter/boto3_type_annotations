from typing import Optional
from typing import Union
from botocore.waiter import Waiter
from botocore.client import BaseClient
from botocore.paginate import Paginator
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def delete_public_access_block(self, AccountId: str):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_public_access_block(self, AccountId: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def put_public_access_block(self, PublicAccessBlockConfiguration: Dict, AccountId: str):
        pass
