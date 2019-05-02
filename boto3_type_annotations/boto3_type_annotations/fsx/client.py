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

    def create_backup(self, FileSystemId: str, ClientRequestToken: str = None, Tags: List = None) -> Dict:
        pass

    def create_file_system(self, FileSystemType: str, StorageCapacity: int, SubnetIds: List, ClientRequestToken: str = None, SecurityGroupIds: List = None, Tags: List = None, KmsKeyId: str = None, WindowsConfiguration: Dict = None, LustreConfiguration: Dict = None) -> Dict:
        pass

    def create_file_system_from_backup(self, BackupId: str, SubnetIds: List, ClientRequestToken: str = None, SecurityGroupIds: List = None, Tags: List = None, WindowsConfiguration: Dict = None) -> Dict:
        pass

    def delete_backup(self, BackupId: str, ClientRequestToken: str = None) -> Dict:
        pass

    def delete_file_system(self, FileSystemId: str, ClientRequestToken: str = None, WindowsConfiguration: Dict = None) -> Dict:
        pass

    def describe_backups(self, BackupIds: List = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_file_systems(self, FileSystemIds: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_tags_for_resource(self, ResourceARN: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def tag_resource(self, ResourceARN: str, Tags: List) -> Dict:
        pass

    def untag_resource(self, ResourceARN: str, TagKeys: List) -> Dict:
        pass

    def update_file_system(self, FileSystemId: str, ClientRequestToken: str = None, WindowsConfiguration: Dict = None, LustreConfiguration: Dict = None) -> Dict:
        pass
