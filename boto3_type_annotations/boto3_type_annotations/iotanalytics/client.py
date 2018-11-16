from datetime import datetime
from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def batch_put_message(self, channelName: str, messages: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def cancel_pipeline_reprocessing(self, pipelineName: str, reprocessingId: str) -> Dict:
        pass

    def create_channel(self, channelName: str, retentionPeriod: Dict = None, tags: List = None) -> Dict:
        pass

    def create_dataset(self, datasetName: str, actions: List, triggers: List = None, retentionPeriod: Dict = None, tags: List = None) -> Dict:
        pass

    def create_dataset_content(self, datasetName: str) -> Dict:
        pass

    def create_datastore(self, datastoreName: str, retentionPeriod: Dict = None, tags: List = None) -> Dict:
        pass

    def create_pipeline(self, pipelineName: str, pipelineActivities: List, tags: List = None) -> Dict:
        pass

    def delete_channel(self, channelName: str) -> NoReturn:
        pass

    def delete_dataset(self, datasetName: str) -> NoReturn:
        pass

    def delete_dataset_content(self, datasetName: str, versionId: str = None) -> NoReturn:
        pass

    def delete_datastore(self, datastoreName: str) -> NoReturn:
        pass

    def delete_pipeline(self, pipelineName: str) -> NoReturn:
        pass

    def describe_channel(self, channelName: str, includeStatistics: bool = None) -> Dict:
        pass

    def describe_dataset(self, datasetName: str) -> Dict:
        pass

    def describe_datastore(self, datastoreName: str, includeStatistics: bool = None) -> Dict:
        pass

    def describe_logging_options(self) -> Dict:
        pass

    def describe_pipeline(self, pipelineName: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_dataset_content(self, datasetName: str, versionId: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_channels(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_dataset_contents(self, datasetName: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_datasets(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_datastores(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_pipelines(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_tags_for_resource(self, resourceArn: str) -> Dict:
        pass

    def put_logging_options(self, loggingOptions: Dict) -> NoReturn:
        pass

    def run_pipeline_activity(self, pipelineActivity: Dict, payloads: List) -> Dict:
        pass

    def sample_channel_data(self, channelName: str, maxMessages: int = None, startTime: datetime = None, endTime: datetime = None) -> Dict:
        pass

    def start_pipeline_reprocessing(self, pipelineName: str, startTime: datetime = None, endTime: datetime = None) -> Dict:
        pass

    def tag_resource(self, resourceArn: str, tags: List) -> Dict:
        pass

    def untag_resource(self, resourceArn: str, tagKeys: List) -> Dict:
        pass

    def update_channel(self, channelName: str, retentionPeriod: Dict = None) -> NoReturn:
        pass

    def update_dataset(self, datasetName: str, actions: List, triggers: List = None, retentionPeriod: Dict = None) -> NoReturn:
        pass

    def update_datastore(self, datastoreName: str, retentionPeriod: Dict = None) -> NoReturn:
        pass

    def update_pipeline(self, pipelineName: str, pipelineActivities: List) -> NoReturn:
        pass
