from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def cancel_job(self, Id: str) -> Dict:
        pass

    def create_job(self, PipelineId: str, Input: Dict = None, Inputs: List = None, Output: Dict = None, Outputs: List = None, OutputKeyPrefix: str = None, Playlists: List = None, UserMetadata: Dict = None) -> Dict:
        pass

    def create_pipeline(self, Name: str, InputBucket: str, Role: str, OutputBucket: str = None, AwsKmsKeyArn: str = None, Notifications: Dict = None, ContentConfig: Dict = None, ThumbnailConfig: Dict = None) -> Dict:
        pass

    def create_preset(self, Name: str, Container: str, Description: str = None, Video: Dict = None, Audio: Dict = None, Thumbnails: Dict = None) -> Dict:
        pass

    def delete_pipeline(self, Id: str) -> Dict:
        pass

    def delete_preset(self, Id: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_jobs_by_pipeline(self, PipelineId: str, Ascending: str = None, PageToken: str = None) -> Dict:
        pass

    def list_jobs_by_status(self, Status: str, Ascending: str = None, PageToken: str = None) -> Dict:
        pass

    def list_pipelines(self, Ascending: str = None, PageToken: str = None) -> Dict:
        pass

    def list_presets(self, Ascending: str = None, PageToken: str = None) -> Dict:
        pass

    def read_job(self, Id: str) -> Dict:
        pass

    def read_pipeline(self, Id: str) -> Dict:
        pass

    def read_preset(self, Id: str) -> Dict:
        pass

    def test_role(self, Role: str, InputBucket: str, OutputBucket: str, Topics: List) -> Dict:
        pass

    def update_pipeline(self, Id: str, Name: str = None, InputBucket: str = None, Role: str = None, AwsKmsKeyArn: str = None, Notifications: Dict = None, ContentConfig: Dict = None, ThumbnailConfig: Dict = None) -> Dict:
        pass

    def update_pipeline_notifications(self, Id: str, Notifications: Dict) -> Dict:
        pass

    def update_pipeline_status(self, Id: str, Status: str) -> Dict:
        pass
