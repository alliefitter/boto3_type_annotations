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

    def create_lifecycle_policy(self, ExecutionRoleArn: str, Description: str, State: str, PolicyDetails: Dict) -> Dict:
        pass

    def delete_lifecycle_policy(self, PolicyId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_lifecycle_policies(self, PolicyIds: List = None, State: str = None, ResourceTypes: List = None, TargetTags: List = None, TagsToAdd: List = None) -> Dict:
        pass

    def get_lifecycle_policy(self, PolicyId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def update_lifecycle_policy(self, PolicyId: str, ExecutionRoleArn: str = None, State: str = None, Description: str = None, PolicyDetails: Dict = None) -> Dict:
        pass
