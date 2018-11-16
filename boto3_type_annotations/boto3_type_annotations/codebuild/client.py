from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def batch_delete_builds(self, ids: List) -> Dict:
        pass

    def batch_get_builds(self, ids: List) -> Dict:
        pass

    def batch_get_projects(self, names: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_project(self, name: str, source: Dict, artifacts: Dict, environment: Dict, serviceRole: str, description: str = None, secondarySources: List = None, secondaryArtifacts: List = None, cache: Dict = None, timeoutInMinutes: int = None, encryptionKey: str = None, tags: List = None, vpcConfig: Dict = None, badgeEnabled: bool = None, logsConfig: Dict = None) -> Dict:
        pass

    def create_webhook(self, projectName: str, branchFilter: str = None) -> Dict:
        pass

    def delete_project(self, name: str) -> Dict:
        pass

    def delete_webhook(self, projectName: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def invalidate_project_cache(self, projectName: str) -> Dict:
        pass

    def list_builds(self, sortOrder: str = None, nextToken: str = None) -> Dict:
        pass

    def list_builds_for_project(self, projectName: str, sortOrder: str = None, nextToken: str = None) -> Dict:
        pass

    def list_curated_environment_images(self) -> Dict:
        pass

    def list_projects(self, sortBy: str = None, sortOrder: str = None, nextToken: str = None) -> Dict:
        pass

    def start_build(self, projectName: str, secondarySourcesOverride: List = None, secondarySourcesVersionOverride: List = None, sourceVersion: str = None, artifactsOverride: Dict = None, secondaryArtifactsOverride: List = None, environmentVariablesOverride: List = None, sourceTypeOverride: str = None, sourceLocationOverride: str = None, sourceAuthOverride: Dict = None, gitCloneDepthOverride: int = None, buildspecOverride: str = None, insecureSslOverride: bool = None, reportBuildStatusOverride: bool = None, environmentTypeOverride: str = None, imageOverride: str = None, computeTypeOverride: str = None, certificateOverride: str = None, cacheOverride: Dict = None, serviceRoleOverride: str = None, privilegedModeOverride: bool = None, timeoutInMinutesOverride: int = None, idempotencyToken: str = None, logsConfigOverride: Dict = None) -> Dict:
        pass

    def stop_build(self, id: str) -> Dict:
        pass

    def update_project(self, name: str, description: str = None, source: Dict = None, secondarySources: List = None, artifacts: Dict = None, secondaryArtifacts: List = None, cache: Dict = None, environment: Dict = None, serviceRole: str = None, timeoutInMinutes: int = None, encryptionKey: str = None, tags: List = None, vpcConfig: Dict = None, badgeEnabled: bool = None, logsConfig: Dict = None) -> Dict:
        pass

    def update_webhook(self, projectName: str, branchFilter: str = None, rotateSecret: bool = None) -> Dict:
        pass
