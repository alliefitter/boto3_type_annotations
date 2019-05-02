from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def delete_playback_configuration(self, Name: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_playback_configuration(self, Name: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_playback_configurations(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_tags_for_resource(self, ResourceArn: str) -> Dict:
        pass

    def put_playback_configuration(self, AdDecisionServerUrl: str = None, CdnConfiguration: Dict = None, DashConfiguration: Dict = None, Name: str = None, SlateAdUrl: str = None, Tags: Dict = None, TranscodeProfileName: str = None, VideoContentSourceUrl: str = None) -> Dict:
        pass

    def tag_resource(self, ResourceArn: str, Tags: Dict):
        pass

    def untag_resource(self, ResourceArn: str, TagKeys: List):
        pass
