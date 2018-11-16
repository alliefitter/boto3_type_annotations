from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def associate_member_account(self, memberAccountId: str):
        pass

    def associate_s3_resources(self, s3Resources: List, memberAccountId: str = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def disassociate_member_account(self, memberAccountId: str):
        pass

    def disassociate_s3_resources(self, associatedS3Resources: List, memberAccountId: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_member_accounts(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_s3_resources(self, memberAccountId: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def update_s3_resources(self, s3ResourcesUpdate: List, memberAccountId: str = None) -> Dict:
        pass
