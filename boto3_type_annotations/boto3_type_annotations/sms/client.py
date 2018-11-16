from datetime import datetime
from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_replication_job(self, serverId: str, seedReplicationTime: datetime, frequency: int, licenseType: str = None, roleName: str = None, description: str = None) -> Dict:
        pass

    def delete_replication_job(self, replicationJobId: str) -> Dict:
        pass

    def delete_server_catalog(self) -> Dict:
        pass

    def disassociate_connector(self, connectorId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_connectors(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_replication_jobs(self, replicationJobId: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_replication_runs(self, replicationJobId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_servers(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def import_server_catalog(self) -> Dict:
        pass

    def start_on_demand_replication_run(self, replicationJobId: str, description: str = None) -> Dict:
        pass

    def update_replication_job(self, replicationJobId: str, frequency: int = None, nextReplicationRunStartTime: datetime = None, licenseType: str = None, roleName: str = None, description: str = None) -> Dict:
        pass
