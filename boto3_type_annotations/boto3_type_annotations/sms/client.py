from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from datetime import datetime
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_app(self, name: str = None, description: str = None, roleName: str = None, clientToken: str = None, serverGroups: List = None, tags: List = None) -> Dict:
        pass

    def create_replication_job(self, serverId: str, seedReplicationTime: datetime, frequency: int = None, runOnce: bool = None, licenseType: str = None, roleName: str = None, description: str = None, numberOfRecentAmisToKeep: int = None, encrypted: bool = None, kmsKeyId: str = None) -> Dict:
        pass

    def delete_app(self, appId: str = None, forceStopAppReplication: bool = None, forceTerminateApp: bool = None) -> Dict:
        pass

    def delete_app_launch_configuration(self, appId: str = None) -> Dict:
        pass

    def delete_app_replication_configuration(self, appId: str = None) -> Dict:
        pass

    def delete_replication_job(self, replicationJobId: str) -> Dict:
        pass

    def delete_server_catalog(self) -> Dict:
        pass

    def disassociate_connector(self, connectorId: str) -> Dict:
        pass

    def generate_change_set(self, appId: str = None, changesetFormat: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def generate_template(self, appId: str = None, templateFormat: str = None) -> Dict:
        pass

    def get_app(self, appId: str = None) -> Dict:
        pass

    def get_app_launch_configuration(self, appId: str = None) -> Dict:
        pass

    def get_app_replication_configuration(self, appId: str = None) -> Dict:
        pass

    def get_connectors(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_replication_jobs(self, replicationJobId: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_replication_runs(self, replicationJobId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_servers(self, nextToken: str = None, maxResults: int = None, vmServerAddressList: List = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def import_server_catalog(self) -> Dict:
        pass

    def launch_app(self, appId: str = None) -> Dict:
        pass

    def list_apps(self, appIds: List = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def put_app_launch_configuration(self, appId: str = None, roleName: str = None, serverGroupLaunchConfigurations: List = None) -> Dict:
        pass

    def put_app_replication_configuration(self, appId: str = None, serverGroupReplicationConfigurations: List = None) -> Dict:
        pass

    def start_app_replication(self, appId: str = None) -> Dict:
        pass

    def start_on_demand_replication_run(self, replicationJobId: str, description: str = None) -> Dict:
        pass

    def stop_app_replication(self, appId: str = None) -> Dict:
        pass

    def terminate_app(self, appId: str = None) -> Dict:
        pass

    def update_app(self, appId: str = None, name: str = None, description: str = None, roleName: str = None, serverGroups: List = None, tags: List = None) -> Dict:
        pass

    def update_replication_job(self, replicationJobId: str, frequency: int = None, nextReplicationRunStartTime: datetime = None, licenseType: str = None, roleName: str = None, description: str = None, numberOfRecentAmisToKeep: int = None, encrypted: bool = None, kmsKeyId: str = None) -> Dict:
        pass
