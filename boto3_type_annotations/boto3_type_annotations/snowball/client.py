from typing import Optional
from typing import Union
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def cancel_cluster(self, ClusterId: str) -> Dict:
        pass

    def cancel_job(self, JobId: str) -> Dict:
        pass

    def create_address(self, Address: Dict) -> Dict:
        pass

    def create_cluster(self, JobType: str, Resources: Dict, AddressId: str, RoleARN: str, ShippingOption: str, Description: str = None, KmsKeyARN: str = None, SnowballType: str = None, Notification: Dict = None, ForwardingAddressId: str = None) -> Dict:
        pass

    def create_job(self, JobType: str = None, Resources: Dict = None, Description: str = None, AddressId: str = None, KmsKeyARN: str = None, RoleARN: str = None, SnowballCapacityPreference: str = None, ShippingOption: str = None, Notification: Dict = None, ClusterId: str = None, SnowballType: str = None, ForwardingAddressId: str = None) -> Dict:
        pass

    def describe_address(self, AddressId: str) -> Dict:
        pass

    def describe_addresses(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_cluster(self, ClusterId: str) -> Dict:
        pass

    def describe_job(self, JobId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_job_manifest(self, JobId: str) -> Dict:
        pass

    def get_job_unlock_code(self, JobId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_snowball_usage(self) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_cluster_jobs(self, ClusterId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_clusters(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_compatible_images(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_jobs(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def update_cluster(self, ClusterId: str, RoleARN: str = None, Description: str = None, Resources: Dict = None, AddressId: str = None, ShippingOption: str = None, Notification: Dict = None, ForwardingAddressId: str = None) -> Dict:
        pass

    def update_job(self, JobId: str, RoleARN: str = None, Notification: Dict = None, Resources: Dict = None, AddressId: str = None, ShippingOption: str = None, Description: str = None, SnowballCapacityPreference: str = None, ForwardingAddressId: str = None) -> Dict:
        pass
