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

    def copy_backup_to_region(self, DestinationRegion: str, BackupId: str) -> Dict:
        pass

    def create_cluster(self, SubnetIds: List, HsmType: str, SourceBackupId: str = None) -> Dict:
        pass

    def create_hsm(self, ClusterId: str, AvailabilityZone: str, IpAddress: str = None) -> Dict:
        pass

    def delete_backup(self, BackupId: str) -> Dict:
        pass

    def delete_cluster(self, ClusterId: str) -> Dict:
        pass

    def delete_hsm(self, ClusterId: str, HsmId: str = None, EniId: str = None, EniIp: str = None) -> Dict:
        pass

    def describe_backups(self, NextToken: str = None, MaxResults: int = None, Filters: Dict = None, SortAscending: bool = None) -> Dict:
        pass

    def describe_clusters(self, Filters: Dict = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def initialize_cluster(self, ClusterId: str, SignedCert: str, TrustAnchor: str) -> Dict:
        pass

    def list_tags(self, ResourceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def restore_backup(self, BackupId: str) -> Dict:
        pass

    def tag_resource(self, ResourceId: str, TagList: List) -> Dict:
        pass

    def untag_resource(self, ResourceId: str, TagKeyList: List) -> Dict:
        pass
