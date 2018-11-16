from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def associate_created_artifact(self, ProgressUpdateStream: str, MigrationTaskName: str, CreatedArtifact: Dict, DryRun: bool = None) -> Dict:
        pass

    def associate_discovered_resource(self, ProgressUpdateStream: str, MigrationTaskName: str, DiscoveredResource: Dict, DryRun: bool = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_progress_update_stream(self, ProgressUpdateStreamName: str, DryRun: bool = None) -> Dict:
        pass

    def delete_progress_update_stream(self, ProgressUpdateStreamName: str, DryRun: bool = None) -> Dict:
        pass

    def describe_application_state(self, ApplicationId: str) -> Dict:
        pass

    def describe_migration_task(self, ProgressUpdateStream: str, MigrationTaskName: str) -> Dict:
        pass

    def disassociate_created_artifact(self, ProgressUpdateStream: str, MigrationTaskName: str, CreatedArtifactName: str, DryRun: bool = None) -> Dict:
        pass

    def disassociate_discovered_resource(self, ProgressUpdateStream: str, MigrationTaskName: str, ConfigurationId: str, DryRun: bool = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def import_migration_task(self, ProgressUpdateStream: str, MigrationTaskName: str, DryRun: bool = None) -> Dict:
        pass

    def list_created_artifacts(self, ProgressUpdateStream: str, MigrationTaskName: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_discovered_resources(self, ProgressUpdateStream: str, MigrationTaskName: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_migration_tasks(self, NextToken: str = None, MaxResults: int = None, ResourceName: str = None) -> Dict:
        pass

    def list_progress_update_streams(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def notify_application_state(self, ApplicationId: str, Status: str, DryRun: bool = None) -> Dict:
        pass

    def notify_migration_task_state(self, ProgressUpdateStream: str, MigrationTaskName: str, Task: Dict, UpdateDateTime: datetime, NextUpdateSeconds: int, DryRun: bool = None) -> Dict:
        pass

    def put_resource_attributes(self, ProgressUpdateStream: str, MigrationTaskName: str, ResourceAttributeList: List, DryRun: bool = None) -> Dict:
        pass
