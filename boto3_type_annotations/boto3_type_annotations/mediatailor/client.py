from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def delete_playback_configuration(self, Name: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_playback_configuration(self, Name: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_playback_configurations(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def put_playback_configuration(self, AdDecisionServerUrl: str = None, CdnConfiguration: Dict = None, Name: str = None, SlateAdUrl: str = None, VideoContentSourceUrl: str = None) -> Dict:
        pass
