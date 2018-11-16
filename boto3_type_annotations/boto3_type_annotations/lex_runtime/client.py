from typing import Union
from botocore.paginate import Paginator
from typing import IO
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def post_content(self, botName: str, botAlias: str, userId: str, contentType: str, inputStream: Union[bytes, IO], sessionAttributes: str = None, requestAttributes: str = None, accept: str = None) -> Dict:
        pass

    def post_text(self, botName: str, botAlias: str, userId: str, inputText: str, sessionAttributes: Dict = None, requestAttributes: Dict = None) -> Dict:
        pass
