from typing import Optional
from typing import Union
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient
from typing import IO


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def search(self, query: str, cursor: str = None, expr: str = None, facet: str = None, filterQuery: str = None, highlight: str = None, partial: bool = None, queryOptions: str = None, queryParser: str = None, returnFields: str = None, size: int = None, sort: str = None, start: int = None, stats: str = None) -> Dict:
        pass

    def suggest(self, query: str, suggester: str, size: int = None) -> Dict:
        pass

    def upload_documents(self, documents: Union[bytes, IO], contentType: str) -> Dict:
        pass
