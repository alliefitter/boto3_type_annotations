from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def associate_node(self, ServerName: str, NodeName: str, EngineAttributes: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_backup(self, ServerName: str, Description: str = None) -> Dict:
        pass

    def create_server(self, ServerName: str, InstanceProfileArn: str, InstanceType: str, ServiceRoleArn: str, AssociatePublicIpAddress: bool = None, DisableAutomatedBackup: bool = None, Engine: str = None, EngineModel: str = None, EngineVersion: str = None, EngineAttributes: List = None, BackupRetentionCount: int = None, KeyPair: str = None, PreferredMaintenanceWindow: str = None, PreferredBackupWindow: str = None, SecurityGroupIds: List = None, SubnetIds: List = None, BackupId: str = None) -> Dict:
        pass

    def delete_backup(self, BackupId: str) -> Dict:
        pass

    def delete_server(self, ServerName: str) -> Dict:
        pass

    def describe_account_attributes(self) -> Dict:
        pass

    def describe_backups(self, BackupId: str = None, ServerName: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def describe_events(self, ServerName: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def describe_node_association_status(self, NodeAssociationStatusToken: str, ServerName: str) -> Dict:
        pass

    def describe_servers(self, ServerName: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def disassociate_node(self, ServerName: str, NodeName: str, EngineAttributes: List = None) -> Dict:
        pass

    def export_server_engine_attribute(self, ExportAttributeName: str, ServerName: str, InputAttributes: List = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def restore_server(self, BackupId: str, ServerName: str, InstanceType: str = None, KeyPair: str = None) -> Dict:
        pass

    def start_maintenance(self, ServerName: str, EngineAttributes: List = None) -> Dict:
        pass

    def update_server(self, ServerName: str, DisableAutomatedBackup: bool = None, BackupRetentionCount: int = None, PreferredMaintenanceWindow: str = None, PreferredBackupWindow: str = None) -> Dict:
        pass

    def update_server_engine_attributes(self, ServerName: str, AttributeName: str, AttributeValue: str = None) -> Dict:
        pass
