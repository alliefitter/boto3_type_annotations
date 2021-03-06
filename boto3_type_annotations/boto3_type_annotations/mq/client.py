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

    def create_broker(self, AutoMinorVersionUpgrade: bool = None, BrokerName: str = None, Configuration: Dict = None, CreatorRequestId: str = None, DeploymentMode: str = None, EngineType: str = None, EngineVersion: str = None, HostInstanceType: str = None, Logs: Dict = None, MaintenanceWindowStartTime: Dict = None, PubliclyAccessible: bool = None, SecurityGroups: List = None, SubnetIds: List = None, Tags: Dict = None, Users: List = None) -> Dict:
        pass

    def create_configuration(self, EngineType: str = None, EngineVersion: str = None, Name: str = None, Tags: Dict = None) -> Dict:
        pass

    def create_tags(self, ResourceArn: str, Tags: Dict = None):
        pass

    def create_user(self, BrokerId: str, Username: str, ConsoleAccess: bool = None, Groups: List = None, Password: str = None) -> Dict:
        pass

    def delete_broker(self, BrokerId: str) -> Dict:
        pass

    def delete_tags(self, ResourceArn: str, TagKeys: List):
        pass

    def delete_user(self, BrokerId: str, Username: str) -> Dict:
        pass

    def describe_broker(self, BrokerId: str) -> Dict:
        pass

    def describe_broker_engine_types(self, EngineType: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_broker_instance_options(self, EngineType: str = None, HostInstanceType: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_configuration(self, ConfigurationId: str) -> Dict:
        pass

    def describe_configuration_revision(self, ConfigurationId: str, ConfigurationRevision: str) -> Dict:
        pass

    def describe_user(self, BrokerId: str, Username: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_brokers(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_configuration_revisions(self, ConfigurationId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_configurations(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_tags(self, ResourceArn: str) -> Dict:
        pass

    def list_users(self, BrokerId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def reboot_broker(self, BrokerId: str) -> Dict:
        pass

    def update_broker(self, BrokerId: str, AutoMinorVersionUpgrade: bool = None, Configuration: Dict = None, EngineVersion: str = None, Logs: Dict = None) -> Dict:
        pass

    def update_configuration(self, ConfigurationId: str, Data: str = None, Description: str = None) -> Dict:
        pass

    def update_user(self, BrokerId: str, Username: str, ConsoleAccess: bool = None, Groups: List = None, Password: str = None) -> Dict:
        pass
