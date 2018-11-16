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

    def delete_thing_shadow(self, thingName: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_thing_shadow(self, thingName: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def publish(self, topic: str, qos: int = None, payload: Union[bytes, IO] = None) -> NoReturn:
        pass

    def update_thing_shadow(self, thingName: str, payload: Union[bytes, IO]) -> Dict:
        pass
