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

    def post_content(self, botName: str, botAlias: str, userId: str, contentType: str, inputStream: Union[bytes, IO], sessionAttributes: str = None, requestAttributes: str = None, accept: str = None) -> Dict:
        pass

    def post_text(self, botName: str, botAlias: str, userId: str, inputText: str, sessionAttributes: Dict = None, requestAttributes: Dict = None) -> Dict:
        pass
