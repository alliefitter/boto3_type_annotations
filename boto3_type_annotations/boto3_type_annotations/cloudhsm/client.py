from typing import Optional
from typing import Union
from typing import List
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def add_tags_to_resource(self, ResourceArn: str, TagList: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_hapg(self, Label: str) -> Dict:
        pass

    def create_hsm(self, SubnetId: str, SshKey: str, IamRoleArn: str, SubscriptionType: str, EniIp: str = None, ExternalId: str = None, ClientToken: str = None, SyslogIp: str = None) -> Dict:
        pass

    def create_luna_client(self, Certificate: str, Label: str = None) -> Dict:
        pass

    def delete_hapg(self, HapgArn: str) -> Dict:
        pass

    def delete_hsm(self, HsmArn: str) -> Dict:
        pass

    def delete_luna_client(self, ClientArn: str) -> Dict:
        pass

    def describe_hapg(self, HapgArn: str) -> Dict:
        pass

    def describe_hsm(self, HsmArn: str = None, HsmSerialNumber: str = None) -> Dict:
        pass

    def describe_luna_client(self, ClientArn: str = None, CertificateFingerprint: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_config(self, ClientArn: str, ClientVersion: str, HapgList: List) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_available_zones(self) -> Dict:
        pass

    def list_hapgs(self, NextToken: str = None) -> Dict:
        pass

    def list_hsms(self, NextToken: str = None) -> Dict:
        pass

    def list_luna_clients(self, NextToken: str = None) -> Dict:
        pass

    def list_tags_for_resource(self, ResourceArn: str) -> Dict:
        pass

    def modify_hapg(self, HapgArn: str, Label: str = None, PartitionSerialList: List = None) -> Dict:
        pass

    def modify_hsm(self, HsmArn: str, SubnetId: str = None, EniIp: str = None, IamRoleArn: str = None, ExternalId: str = None, SyslogIp: str = None) -> Dict:
        pass

    def modify_luna_client(self, ClientArn: str, Certificate: str) -> Dict:
        pass

    def remove_tags_from_resource(self, ResourceArn: str, TagKeyList: List) -> Dict:
        pass
