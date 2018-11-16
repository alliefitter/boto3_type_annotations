from datetime import datetime
from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def add_instance_fleet(self, ClusterId: str, InstanceFleet: Dict) -> Dict:
        pass

    def add_instance_groups(self, InstanceGroups: List, JobFlowId: str) -> Dict:
        pass

    def add_job_flow_steps(self, JobFlowId: str, Steps: List) -> Dict:
        pass

    def add_tags(self, ResourceId: str, Tags: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def cancel_steps(self, ClusterId: str = None, StepIds: List = None) -> Dict:
        pass

    def create_security_configuration(self, Name: str, SecurityConfiguration: str) -> Dict:
        pass

    def delete_security_configuration(self, Name: str) -> Dict:
        pass

    def describe_cluster(self, ClusterId: str) -> Dict:
        pass

    def describe_job_flows(self, CreatedAfter: datetime = None, CreatedBefore: datetime = None, JobFlowIds: List = None, JobFlowStates: List = None) -> Dict:
        pass

    def describe_security_configuration(self, Name: str) -> Dict:
        pass

    def describe_step(self, ClusterId: str, StepId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_bootstrap_actions(self, ClusterId: str, Marker: str = None) -> Dict:
        pass

    def list_clusters(self, CreatedAfter: datetime = None, CreatedBefore: datetime = None, ClusterStates: List = None, Marker: str = None) -> Dict:
        pass

    def list_instance_fleets(self, ClusterId: str, Marker: str = None) -> Dict:
        pass

    def list_instance_groups(self, ClusterId: str, Marker: str = None) -> Dict:
        pass

    def list_instances(self, ClusterId: str, InstanceGroupId: str = None, InstanceGroupTypes: List = None, InstanceFleetId: str = None, InstanceFleetType: str = None, InstanceStates: List = None, Marker: str = None) -> Dict:
        pass

    def list_security_configurations(self, Marker: str = None) -> Dict:
        pass

    def list_steps(self, ClusterId: str, StepStates: List = None, StepIds: List = None, Marker: str = None) -> Dict:
        pass

    def modify_instance_fleet(self, ClusterId: str, InstanceFleet: Dict) -> NoReturn:
        pass

    def modify_instance_groups(self, ClusterId: str = None, InstanceGroups: List = None) -> NoReturn:
        pass

    def put_auto_scaling_policy(self, ClusterId: str, InstanceGroupId: str, AutoScalingPolicy: Dict) -> Dict:
        pass

    def remove_auto_scaling_policy(self, ClusterId: str, InstanceGroupId: str) -> Dict:
        pass

    def remove_tags(self, ResourceId: str, TagKeys: List) -> Dict:
        pass

    def run_job_flow(self, Name: str, Instances: Dict, LogUri: str = None, AdditionalInfo: str = None, AmiVersion: str = None, ReleaseLabel: str = None, Steps: List = None, BootstrapActions: List = None, SupportedProducts: List = None, NewSupportedProducts: List = None, Applications: List = None, Configurations: List = None, VisibleToAllUsers: bool = None, JobFlowRole: str = None, ServiceRole: str = None, Tags: List = None, SecurityConfiguration: str = None, AutoScalingRole: str = None, ScaleDownBehavior: str = None, CustomAmiId: str = None, EbsRootVolumeSize: int = None, RepoUpgradeOnBoot: str = None, KerberosAttributes: Dict = None) -> Dict:
        pass

    def set_termination_protection(self, JobFlowIds: List, TerminationProtected: bool) -> NoReturn:
        pass

    def set_visible_to_all_users(self, JobFlowIds: List, VisibleToAllUsers: bool) -> NoReturn:
        pass

    def terminate_job_flows(self, JobFlowIds: List) -> NoReturn:
        pass
