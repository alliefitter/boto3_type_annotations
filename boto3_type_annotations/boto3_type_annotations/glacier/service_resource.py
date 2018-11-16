from typing import Optional
from typing import Union
from boto3.resources.collection import ResourceCollection
from typing import List
from typing import Dict
from typing import IO
from boto3.resources import base


class ServiceResource(base.ServiceResource):
    vaults: 'vaults'

    def Account(self, id: str = None) -> 'Account':
        pass

    def Archive(self, account_id: str = None, vault_name: str = None, id: str = None) -> 'Archive':
        pass

    def Job(self, account_id: str = None, vault_name: str = None, id: str = None) -> 'Job':
        pass

    def MultipartUpload(self, account_id: str = None, vault_name: str = None, id: str = None) -> 'MultipartUpload':
        pass

    def Notification(self, account_id: str = None, vault_name: str = None) -> 'Notification':
        pass

    def Vault(self, account_id: str = None, name: str = None) -> 'Vault':
        pass

    def create_vault(self, vaultName: str) -> 'Vault':
        pass

    def get_available_subresources(self) -> List[str]:
        pass


class Account(base.ServiceResource):
    id: str
    vaults: 'vaults'

    def create_vault(self, vaultName: str) -> 'Vault':
        pass

    def get_available_subresources(self) -> List[str]:
        pass


class Archive(base.ServiceResource):
    account_id: str
    vault_name: str
    id: str

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def initiate_archive_retrieval(self) -> 'Job':
        pass


class Job(base.ServiceResource):
    job_id: str
    job_description: str
    action: str
    archive_id: str
    vault_arn: str
    creation_date: str
    completed: bool
    status_code: str
    status_message: str
    archive_size_in_bytes: int
    inventory_size_in_bytes: int
    sns_topic: str
    completion_date: str
    sha256_tree_hash: str
    archive_sha256_tree_hash: str
    retrieval_byte_range: str
    tier: str
    inventory_retrieval_parameters: Dict
    job_output_path: str
    select_parameters: Dict
    output_location: Dict
    account_id: str
    vault_name: str
    id: str

    def get_available_subresources(self) -> List[str]:
        pass

    def get_output(self, range: str = None) -> Dict:
        pass

    def load(self):
        pass

    def reload(self):
        pass


class MultipartUpload(base.ServiceResource):
    multipart_upload_id: str
    vault_arn: str
    archive_description: str
    part_size_in_bytes: int
    creation_date: str
    account_id: str
    vault_name: str
    id: str

    def abort(self):
        pass

    def complete(self, archiveSize: str = None, checksum: str = None) -> Dict:
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def parts(self, marker: str = None, limit: str = None) -> Dict:
        pass

    def upload_part(self, checksum: str = None, range: str = None, body: Union[bytes, IO] = None) -> Dict:
        pass


class Notification(base.ServiceResource):
    sns_topic: str
    events: List
    account_id: str
    vault_name: str

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass

    def set(self, vaultNotificationConfig: Dict = None):
        pass


class Vault(base.ServiceResource):
    vault_arn: str
    vault_name: str
    creation_date: str
    last_inventory_date: str
    number_of_archives: int
    size_in_bytes: int
    account_id: str
    name: str
    completed_jobs: 'completed_jobs'
    failed_jobs: 'failed_jobs'
    jobs: 'jobs'
    jobs_in_progress: 'jobs_in_progress'
    multipart_uplaods: 'multipart_uplaods'
    multipart_uploads: 'multipart_uploads'
    succeeded_jobs: 'succeeded_jobs'

    def create(self) -> Dict:
        pass

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def initiate_inventory_retrieval(self) -> 'Job':
        pass

    def initiate_multipart_upload(self, archiveDescription: str = None, partSize: str = None) -> 'MultipartUpload':
        pass

    def load(self):
        pass

    def reload(self):
        pass

    def upload_archive(self, archiveDescription: str = None, checksum: str = None, body: Union[bytes, IO] = None) -> 'Archive':
        pass


class vaults(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Vault']:
        pass

    
    @classmethod
    def filter(cls, marker: str = None, limit: str = None) -> List['Vault']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Vault']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Vault']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass
