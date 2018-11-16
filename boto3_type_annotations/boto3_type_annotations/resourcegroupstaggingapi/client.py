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

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_resources(self, PaginationToken: str = None, TagFilters: List = None, ResourcesPerPage: int = None, TagsPerPage: int = None, ResourceTypeFilters: List = None) -> Dict:
        pass

    def get_tag_keys(self, PaginationToken: str = None) -> Dict:
        pass

    def get_tag_values(self, Key: str, PaginationToken: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def tag_resources(self, ResourceARNList: List, Tags: Dict) -> Dict:
        pass

    def untag_resources(self, ResourceARNList: List, TagKeys: List) -> Dict:
        pass
