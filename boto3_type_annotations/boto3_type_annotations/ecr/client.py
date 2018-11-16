from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def batch_check_layer_availability(self, repositoryName: str, layerDigests: List, registryId: str = None) -> Dict:
        pass

    def batch_delete_image(self, repositoryName: str, imageIds: List, registryId: str = None) -> Dict:
        pass

    def batch_get_image(self, repositoryName: str, imageIds: List, registryId: str = None, acceptedMediaTypes: List = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def complete_layer_upload(self, repositoryName: str, uploadId: str, layerDigests: List, registryId: str = None) -> Dict:
        pass

    def create_repository(self, repositoryName: str) -> Dict:
        pass

    def delete_lifecycle_policy(self, repositoryName: str, registryId: str = None) -> Dict:
        pass

    def delete_repository(self, repositoryName: str, registryId: str = None, force: bool = None) -> Dict:
        pass

    def delete_repository_policy(self, repositoryName: str, registryId: str = None) -> Dict:
        pass

    def describe_images(self, repositoryName: str, registryId: str = None, imageIds: List = None, nextToken: str = None, maxResults: int = None, filter: Dict = None) -> Dict:
        pass

    def describe_repositories(self, registryId: str = None, repositoryNames: List = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_authorization_token(self, registryIds: List = None) -> Dict:
        pass

    def get_download_url_for_layer(self, repositoryName: str, layerDigest: str, registryId: str = None) -> Dict:
        pass

    def get_lifecycle_policy(self, repositoryName: str, registryId: str = None) -> Dict:
        pass

    def get_lifecycle_policy_preview(self, repositoryName: str, registryId: str = None, imageIds: List = None, nextToken: str = None, maxResults: int = None, filter: Dict = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_repository_policy(self, repositoryName: str, registryId: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def initiate_layer_upload(self, repositoryName: str, registryId: str = None) -> Dict:
        pass

    def list_images(self, repositoryName: str, registryId: str = None, nextToken: str = None, maxResults: int = None, filter: Dict = None) -> Dict:
        pass

    def put_image(self, repositoryName: str, imageManifest: str, registryId: str = None, imageTag: str = None) -> Dict:
        pass

    def put_lifecycle_policy(self, repositoryName: str, lifecyclePolicyText: str, registryId: str = None) -> Dict:
        pass

    def set_repository_policy(self, repositoryName: str, policyText: str, registryId: str = None, force: bool = None) -> Dict:
        pass

    def start_lifecycle_policy_preview(self, repositoryName: str, registryId: str = None, lifecyclePolicyText: str = None) -> Dict:
        pass

    def upload_layer_part(self, repositoryName: str, uploadId: str, partFirstByte: int, partLastByte: int, layerPartBlob: bytes, registryId: str = None) -> Dict:
        pass
