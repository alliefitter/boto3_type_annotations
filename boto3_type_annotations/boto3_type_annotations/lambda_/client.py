from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient
from typing import IO


class Client(BaseClient):
    def add_permission(self, FunctionName: str, StatementId: str, Action: str, Principal: str, SourceArn: str = None, SourceAccount: str = None, EventSourceToken: str = None, Qualifier: str = None, RevisionId: str = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_alias(self, FunctionName: str, Name: str, FunctionVersion: str, Description: str = None, RoutingConfig: Dict = None) -> Dict:
        pass

    def create_event_source_mapping(self, EventSourceArn: str, FunctionName: str, Enabled: bool = None, BatchSize: int = None, StartingPosition: str = None, StartingPositionTimestamp: datetime = None) -> Dict:
        pass

    def create_function(self, FunctionName: str, Runtime: str, Role: str, Handler: str, Code: Dict, Description: str = None, Timeout: int = None, MemorySize: int = None, Publish: bool = None, VpcConfig: Dict = None, DeadLetterConfig: Dict = None, Environment: Dict = None, KMSKeyArn: str = None, TracingConfig: Dict = None, Tags: Dict = None) -> Dict:
        pass

    def delete_alias(self, FunctionName: str, Name: str):
        pass

    def delete_event_source_mapping(self, UUID: str) -> Dict:
        pass

    def delete_function(self, FunctionName: str, Qualifier: str = None):
        pass

    def delete_function_concurrency(self, FunctionName: str):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_account_settings(self) -> Dict:
        pass

    def get_alias(self, FunctionName: str, Name: str) -> Dict:
        pass

    def get_event_source_mapping(self, UUID: str) -> Dict:
        pass

    def get_function(self, FunctionName: str, Qualifier: str = None) -> Dict:
        pass

    def get_function_configuration(self, FunctionName: str, Qualifier: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_policy(self, FunctionName: str, Qualifier: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def invoke(self, FunctionName: str, InvocationType: str = None, LogType: str = None, ClientContext: str = None, Payload: Union[bytes, IO] = None, Qualifier: str = None) -> Dict:
        pass

    def invoke_async(self, FunctionName: str, InvokeArgs: Union[bytes, IO]) -> Dict:
        pass

    def list_aliases(self, FunctionName: str, FunctionVersion: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    def list_event_source_mappings(self, EventSourceArn: str = None, FunctionName: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    def list_functions(self, MasterRegion: str = None, FunctionVersion: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    def list_tags(self, Resource: str) -> Dict:
        pass

    def list_versions_by_function(self, FunctionName: str, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    def publish_version(self, FunctionName: str, CodeSha256: str = None, Description: str = None, RevisionId: str = None) -> Dict:
        pass

    def put_function_concurrency(self, FunctionName: str, ReservedConcurrentExecutions: int) -> Dict:
        pass

    def remove_permission(self, FunctionName: str, StatementId: str, Qualifier: str = None, RevisionId: str = None):
        pass

    def tag_resource(self, Resource: str, Tags: Dict):
        pass

    def untag_resource(self, Resource: str, TagKeys: List):
        pass

    def update_alias(self, FunctionName: str, Name: str, FunctionVersion: str = None, Description: str = None, RoutingConfig: Dict = None, RevisionId: str = None) -> Dict:
        pass

    def update_event_source_mapping(self, UUID: str, FunctionName: str = None, Enabled: bool = None, BatchSize: int = None) -> Dict:
        pass

    def update_function_code(self, FunctionName: str, ZipFile: bytes = None, S3Bucket: str = None, S3Key: str = None, S3ObjectVersion: str = None, Publish: bool = None, DryRun: bool = None, RevisionId: str = None) -> Dict:
        pass

    def update_function_configuration(self, FunctionName: str, Role: str = None, Handler: str = None, Description: str = None, Timeout: int = None, MemorySize: int = None, VpcConfig: Dict = None, Environment: Dict = None, Runtime: str = None, DeadLetterConfig: Dict = None, KMSKeyArn: str = None, TracingConfig: Dict = None, RevisionId: str = None) -> Dict:
        pass
