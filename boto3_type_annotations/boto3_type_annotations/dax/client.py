from datetime import datetime
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

    def create_cluster(self, ClusterName: str, NodeType: str, ReplicationFactor: int, IamRoleArn: str, Description: str = None, AvailabilityZones: List = None, SubnetGroupName: str = None, SecurityGroupIds: List = None, PreferredMaintenanceWindow: str = None, NotificationTopicArn: str = None, ParameterGroupName: str = None, Tags: List = None, SSESpecification: Dict = None) -> Dict:
        pass

    def create_parameter_group(self, ParameterGroupName: str, Description: str = None) -> Dict:
        pass

    def create_subnet_group(self, SubnetGroupName: str, SubnetIds: List, Description: str = None) -> Dict:
        pass

    def decrease_replication_factor(self, ClusterName: str, NewReplicationFactor: int, AvailabilityZones: List = None, NodeIdsToRemove: List = None) -> Dict:
        pass

    def delete_cluster(self, ClusterName: str) -> Dict:
        pass

    def delete_parameter_group(self, ParameterGroupName: str) -> Dict:
        pass

    def delete_subnet_group(self, SubnetGroupName: str) -> Dict:
        pass

    def describe_clusters(self, ClusterNames: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_default_parameters(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_events(self, SourceName: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_parameter_groups(self, ParameterGroupNames: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_parameters(self, ParameterGroupName: str, Source: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_subnet_groups(self, SubnetGroupNames: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def increase_replication_factor(self, ClusterName: str, NewReplicationFactor: int, AvailabilityZones: List = None) -> Dict:
        pass

    def list_tags(self, ResourceName: str, NextToken: str = None) -> Dict:
        pass

    def reboot_node(self, ClusterName: str, NodeId: str) -> Dict:
        pass

    def tag_resource(self, ResourceName: str, Tags: List) -> Dict:
        pass

    def untag_resource(self, ResourceName: str, TagKeys: List) -> Dict:
        pass

    def update_cluster(self, ClusterName: str, Description: str = None, PreferredMaintenanceWindow: str = None, NotificationTopicArn: str = None, NotificationTopicStatus: str = None, ParameterGroupName: str = None, SecurityGroupIds: List = None) -> Dict:
        pass

    def update_parameter_group(self, ParameterGroupName: str, ParameterNameValues: List) -> Dict:
        pass

    def update_subnet_group(self, SubnetGroupName: str, Description: str = None, SubnetIds: List = None) -> Dict:
        pass
