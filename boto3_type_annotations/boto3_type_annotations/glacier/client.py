from typing import Union
from botocore.paginate import Paginator
from typing import IO
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def abort_multipart_upload(self, vaultName: str, uploadId: str, accountId: str = None) -> NoReturn:
        pass

    def abort_vault_lock(self, vaultName: str, accountId: str = None) -> NoReturn:
        pass

    def add_tags_to_vault(self, vaultName: str, accountId: str = None, Tags: Dict = None) -> NoReturn:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def complete_multipart_upload(self, vaultName: str, uploadId: str, accountId: str = None, archiveSize: str = None, checksum: str = None) -> Dict:
        pass

    def complete_vault_lock(self, vaultName: str, lockId: str, accountId: str = None) -> NoReturn:
        pass

    def create_vault(self, vaultName: str, accountId: str = None) -> Dict:
        pass

    def delete_archive(self, vaultName: str, archiveId: str, accountId: str = None) -> NoReturn:
        pass

    def delete_vault(self, vaultName: str, accountId: str = None) -> NoReturn:
        pass

    def delete_vault_access_policy(self, vaultName: str, accountId: str = None) -> NoReturn:
        pass

    def delete_vault_notifications(self, vaultName: str, accountId: str = None) -> NoReturn:
        pass

    def describe_job(self, vaultName: str, jobId: str, accountId: str = None) -> Dict:
        pass

    def describe_vault(self, vaultName: str, accountId: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_data_retrieval_policy(self, accountId: str = None) -> Dict:
        pass

    def get_job_output(self, vaultName: str, jobId: str, accountId: str = None, range: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_vault_access_policy(self, vaultName: str, accountId: str = None) -> Dict:
        pass

    def get_vault_lock(self, vaultName: str, accountId: str = None) -> Dict:
        pass

    def get_vault_notifications(self, vaultName: str, accountId: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def initiate_job(self, vaultName: str, accountId: str = None, jobParameters: Dict = None) -> Dict:
        pass

    def initiate_multipart_upload(self, vaultName: str, accountId: str = None, archiveDescription: str = None, partSize: str = None) -> Dict:
        pass

    def initiate_vault_lock(self, vaultName: str, accountId: str = None, policy: Dict = None) -> Dict:
        pass

    def list_jobs(self, vaultName: str, accountId: str = None, limit: str = None, marker: str = None, statuscode: str = None, completed: str = None) -> Dict:
        pass

    def list_multipart_uploads(self, vaultName: str, accountId: str = None, marker: str = None, limit: str = None) -> Dict:
        pass

    def list_parts(self, vaultName: str, uploadId: str, accountId: str = None, marker: str = None, limit: str = None) -> Dict:
        pass

    def list_provisioned_capacity(self, accountId: str = None) -> Dict:
        pass

    def list_tags_for_vault(self, vaultName: str, accountId: str = None) -> Dict:
        pass

    def list_vaults(self, accountId: str = None, marker: str = None, limit: str = None) -> Dict:
        pass

    def purchase_provisioned_capacity(self, accountId: str = None) -> Dict:
        pass

    def remove_tags_from_vault(self, vaultName: str, accountId: str = None, TagKeys: List = None) -> NoReturn:
        pass

    def set_data_retrieval_policy(self, accountId: str = None, Policy: Dict = None) -> NoReturn:
        pass

    def set_vault_access_policy(self, vaultName: str, accountId: str = None, policy: Dict = None) -> NoReturn:
        pass

    def set_vault_notifications(self, vaultName: str, accountId: str = None, vaultNotificationConfig: Dict = None) -> NoReturn:
        pass

    def upload_archive(self, vaultName: str, accountId: str = None, archiveDescription: str = None, checksum: str = None, body: Union[bytes, IO] = None) -> Dict:
        pass

    def upload_multipart_part(self, vaultName: str, uploadId: str, accountId: str = None, checksum: str = None, range: str = None, body: Union[bytes, IO] = None) -> Dict:
        pass
