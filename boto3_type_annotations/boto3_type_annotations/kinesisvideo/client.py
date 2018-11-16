from typing import Optional
from typing import Union
from typing import List
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_stream(self, StreamName: str, DeviceName: str = None, MediaType: str = None, KmsKeyId: str = None, DataRetentionInHours: int = None) -> Dict:
        pass

    def delete_stream(self, StreamARN: str, CurrentVersion: str = None) -> Dict:
        pass

    def describe_stream(self, StreamName: str = None, StreamARN: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_data_endpoint(self, APIName: str, StreamName: str = None, StreamARN: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_streams(self, MaxResults: int = None, NextToken: str = None, StreamNameCondition: Dict = None) -> Dict:
        pass

    def list_tags_for_stream(self, NextToken: str = None, StreamARN: str = None, StreamName: str = None) -> Dict:
        pass

    def tag_stream(self, Tags: Dict, StreamARN: str = None, StreamName: str = None) -> Dict:
        pass

    def untag_stream(self, TagKeyList: List, StreamARN: str = None, StreamName: str = None) -> Dict:
        pass

    def update_data_retention(self, CurrentVersion: str, Operation: str, DataRetentionChangeInHours: int, StreamName: str = None, StreamARN: str = None) -> Dict:
        pass

    def update_stream(self, CurrentVersion: str, StreamName: str = None, StreamARN: str = None, DeviceName: str = None, MediaType: str = None) -> Dict:
        pass
