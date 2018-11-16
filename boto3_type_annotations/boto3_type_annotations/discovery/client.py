from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def associate_configuration_items_to_application(self, applicationConfigurationId: str, configurationIds: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_application(self, name: str, description: str = None) -> Dict:
        pass

    def create_tags(self, configurationIds: List, tags: List) -> Dict:
        pass

    def delete_applications(self, configurationIds: List) -> Dict:
        pass

    def delete_tags(self, configurationIds: List, tags: List = None) -> Dict:
        pass

    def describe_agents(self, agentIds: List = None, filters: List = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def describe_configurations(self, configurationIds: List) -> Dict:
        pass

    def describe_continuous_exports(self, exportIds: List = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def describe_export_configurations(self, exportIds: List = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def describe_export_tasks(self, exportIds: List = None, filters: List = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def describe_tags(self, filters: List = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def disassociate_configuration_items_from_application(self, applicationConfigurationId: str, configurationIds: List) -> Dict:
        pass

    def export_configurations(self) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_discovery_summary(self) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_configurations(self, configurationType: str, filters: List = None, maxResults: int = None, nextToken: str = None, orderBy: List = None) -> Dict:
        pass

    def list_server_neighbors(self, configurationId: str, portInformationNeeded: bool = None, neighborConfigurationIds: List = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def start_continuous_export(self) -> Dict:
        pass

    def start_data_collection_by_agent_ids(self, agentIds: List) -> Dict:
        pass

    def start_export_task(self, exportDataFormat: List = None, filters: List = None, startTime: datetime = None, endTime: datetime = None) -> Dict:
        pass

    def stop_continuous_export(self, exportId: str) -> Dict:
        pass

    def stop_data_collection_by_agent_ids(self, agentIds: List) -> Dict:
        pass

    def update_application(self, configurationId: str, name: str = None, description: str = None) -> Dict:
        pass
