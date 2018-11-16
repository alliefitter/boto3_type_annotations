from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def assign_instance(self, InstanceId: str, LayerIds: List):
        pass

    def assign_volume(self, VolumeId: str, InstanceId: str = None):
        pass

    def associate_elastic_ip(self, ElasticIp: str, InstanceId: str = None):
        pass

    def attach_elastic_load_balancer(self, ElasticLoadBalancerName: str, LayerId: str):
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def clone_stack(self, SourceStackId: str, ServiceRoleArn: str, Name: str = None, Region: str = None, VpcId: str = None, Attributes: Dict = None, DefaultInstanceProfileArn: str = None, DefaultOs: str = None, HostnameTheme: str = None, DefaultAvailabilityZone: str = None, DefaultSubnetId: str = None, CustomJson: str = None, ConfigurationManager: Dict = None, ChefConfiguration: Dict = None, UseCustomCookbooks: bool = None, UseOpsworksSecurityGroups: bool = None, CustomCookbooksSource: Dict = None, DefaultSshKeyName: str = None, ClonePermissions: bool = None, CloneAppIds: List = None, DefaultRootDeviceType: str = None, AgentVersion: str = None) -> Dict:
        pass

    def create_app(self, StackId: str, Name: str, Type: str, Shortname: str = None, Description: str = None, DataSources: List = None, AppSource: Dict = None, Domains: List = None, EnableSsl: bool = None, SslConfiguration: Dict = None, Attributes: Dict = None, Environment: List = None) -> Dict:
        pass

    def create_deployment(self, StackId: str, Command: Dict, AppId: str = None, InstanceIds: List = None, LayerIds: List = None, Comment: str = None, CustomJson: str = None) -> Dict:
        pass

    def create_instance(self, StackId: str, LayerIds: List, InstanceType: str, AutoScalingType: str = None, Hostname: str = None, Os: str = None, AmiId: str = None, SshKeyName: str = None, AvailabilityZone: str = None, VirtualizationType: str = None, SubnetId: str = None, Architecture: str = None, RootDeviceType: str = None, BlockDeviceMappings: List = None, InstallUpdatesOnBoot: bool = None, EbsOptimized: bool = None, AgentVersion: str = None, Tenancy: str = None) -> Dict:
        pass

    def create_layer(self, StackId: str, Type: str, Name: str, Shortname: str, Attributes: Dict = None, CloudWatchLogsConfiguration: Dict = None, CustomInstanceProfileArn: str = None, CustomJson: str = None, CustomSecurityGroupIds: List = None, Packages: List = None, VolumeConfigurations: List = None, EnableAutoHealing: bool = None, AutoAssignElasticIps: bool = None, AutoAssignPublicIps: bool = None, CustomRecipes: Dict = None, InstallUpdatesOnBoot: bool = None, UseEbsOptimizedInstances: bool = None, LifecycleEventConfiguration: Dict = None) -> Dict:
        pass

    def create_stack(self, Name: str, Region: str, ServiceRoleArn: str, DefaultInstanceProfileArn: str, VpcId: str = None, Attributes: Dict = None, DefaultOs: str = None, HostnameTheme: str = None, DefaultAvailabilityZone: str = None, DefaultSubnetId: str = None, CustomJson: str = None, ConfigurationManager: Dict = None, ChefConfiguration: Dict = None, UseCustomCookbooks: bool = None, UseOpsworksSecurityGroups: bool = None, CustomCookbooksSource: Dict = None, DefaultSshKeyName: str = None, DefaultRootDeviceType: str = None, AgentVersion: str = None) -> Dict:
        pass

    def create_user_profile(self, IamUserArn: str, SshUsername: str = None, SshPublicKey: str = None, AllowSelfManagement: bool = None) -> Dict:
        pass

    def delete_app(self, AppId: str):
        pass

    def delete_instance(self, InstanceId: str, DeleteElasticIp: bool = None, DeleteVolumes: bool = None):
        pass

    def delete_layer(self, LayerId: str):
        pass

    def delete_stack(self, StackId: str):
        pass

    def delete_user_profile(self, IamUserArn: str):
        pass

    def deregister_ecs_cluster(self, EcsClusterArn: str):
        pass

    def deregister_elastic_ip(self, ElasticIp: str):
        pass

    def deregister_instance(self, InstanceId: str):
        pass

    def deregister_rds_db_instance(self, RdsDbInstanceArn: str):
        pass

    def deregister_volume(self, VolumeId: str):
        pass

    def describe_agent_versions(self, StackId: str = None, ConfigurationManager: Dict = None) -> Dict:
        pass

    def describe_apps(self, StackId: str = None, AppIds: List = None) -> Dict:
        pass

    def describe_commands(self, DeploymentId: str = None, InstanceId: str = None, CommandIds: List = None) -> Dict:
        pass

    def describe_deployments(self, StackId: str = None, AppId: str = None, DeploymentIds: List = None) -> Dict:
        pass

    def describe_ecs_clusters(self, EcsClusterArns: List = None, StackId: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def describe_elastic_ips(self, InstanceId: str = None, StackId: str = None, Ips: List = None) -> Dict:
        pass

    def describe_elastic_load_balancers(self, StackId: str = None, LayerIds: List = None) -> Dict:
        pass

    def describe_instances(self, StackId: str = None, LayerId: str = None, InstanceIds: List = None) -> Dict:
        pass

    def describe_layers(self, StackId: str = None, LayerIds: List = None) -> Dict:
        pass

    def describe_load_based_auto_scaling(self, LayerIds: List) -> Dict:
        pass

    def describe_my_user_profile(self) -> Dict:
        pass

    def describe_operating_systems(self) -> Dict:
        pass

    def describe_permissions(self, IamUserArn: str = None, StackId: str = None) -> Dict:
        pass

    def describe_raid_arrays(self, InstanceId: str = None, StackId: str = None, RaidArrayIds: List = None) -> Dict:
        pass

    def describe_rds_db_instances(self, StackId: str, RdsDbInstanceArns: List = None) -> Dict:
        pass

    def describe_service_errors(self, StackId: str = None, InstanceId: str = None, ServiceErrorIds: List = None) -> Dict:
        pass

    def describe_stack_provisioning_parameters(self, StackId: str) -> Dict:
        pass

    def describe_stack_summary(self, StackId: str) -> Dict:
        pass

    def describe_stacks(self, StackIds: List = None) -> Dict:
        pass

    def describe_time_based_auto_scaling(self, InstanceIds: List) -> Dict:
        pass

    def describe_user_profiles(self, IamUserArns: List = None) -> Dict:
        pass

    def describe_volumes(self, InstanceId: str = None, StackId: str = None, RaidArrayId: str = None, VolumeIds: List = None) -> Dict:
        pass

    def detach_elastic_load_balancer(self, ElasticLoadBalancerName: str, LayerId: str):
        pass

    def disassociate_elastic_ip(self, ElasticIp: str):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_hostname_suggestion(self, LayerId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def grant_access(self, InstanceId: str, ValidForInMinutes: int = None) -> Dict:
        pass

    def list_tags(self, ResourceArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def reboot_instance(self, InstanceId: str):
        pass

    def register_ecs_cluster(self, EcsClusterArn: str, StackId: str) -> Dict:
        pass

    def register_elastic_ip(self, ElasticIp: str, StackId: str) -> Dict:
        pass

    def register_instance(self, StackId: str, Hostname: str = None, PublicIp: str = None, PrivateIp: str = None, RsaPublicKey: str = None, RsaPublicKeyFingerprint: str = None, InstanceIdentity: Dict = None) -> Dict:
        pass

    def register_rds_db_instance(self, StackId: str, RdsDbInstanceArn: str, DbUser: str, DbPassword: str):
        pass

    def register_volume(self, StackId: str, Ec2VolumeId: str = None) -> Dict:
        pass

    def set_load_based_auto_scaling(self, LayerId: str, Enable: bool = None, UpScaling: Dict = None, DownScaling: Dict = None):
        pass

    def set_permission(self, StackId: str, IamUserArn: str, AllowSsh: bool = None, AllowSudo: bool = None, Level: str = None):
        pass

    def set_time_based_auto_scaling(self, InstanceId: str, AutoScalingSchedule: Dict = None):
        pass

    def start_instance(self, InstanceId: str):
        pass

    def start_stack(self, StackId: str):
        pass

    def stop_instance(self, InstanceId: str, Force: bool = None):
        pass

    def stop_stack(self, StackId: str):
        pass

    def tag_resource(self, ResourceArn: str, Tags: Dict):
        pass

    def unassign_instance(self, InstanceId: str):
        pass

    def unassign_volume(self, VolumeId: str):
        pass

    def untag_resource(self, ResourceArn: str, TagKeys: List):
        pass

    def update_app(self, AppId: str, Name: str = None, Description: str = None, DataSources: List = None, Type: str = None, AppSource: Dict = None, Domains: List = None, EnableSsl: bool = None, SslConfiguration: Dict = None, Attributes: Dict = None, Environment: List = None):
        pass

    def update_elastic_ip(self, ElasticIp: str, Name: str = None):
        pass

    def update_instance(self, InstanceId: str, LayerIds: List = None, InstanceType: str = None, AutoScalingType: str = None, Hostname: str = None, Os: str = None, AmiId: str = None, SshKeyName: str = None, Architecture: str = None, InstallUpdatesOnBoot: bool = None, EbsOptimized: bool = None, AgentVersion: str = None):
        pass

    def update_layer(self, LayerId: str, Name: str = None, Shortname: str = None, Attributes: Dict = None, CloudWatchLogsConfiguration: Dict = None, CustomInstanceProfileArn: str = None, CustomJson: str = None, CustomSecurityGroupIds: List = None, Packages: List = None, VolumeConfigurations: List = None, EnableAutoHealing: bool = None, AutoAssignElasticIps: bool = None, AutoAssignPublicIps: bool = None, CustomRecipes: Dict = None, InstallUpdatesOnBoot: bool = None, UseEbsOptimizedInstances: bool = None, LifecycleEventConfiguration: Dict = None):
        pass

    def update_my_user_profile(self, SshPublicKey: str = None):
        pass

    def update_rds_db_instance(self, RdsDbInstanceArn: str, DbUser: str = None, DbPassword: str = None):
        pass

    def update_stack(self, StackId: str, Name: str = None, Attributes: Dict = None, ServiceRoleArn: str = None, DefaultInstanceProfileArn: str = None, DefaultOs: str = None, HostnameTheme: str = None, DefaultAvailabilityZone: str = None, DefaultSubnetId: str = None, CustomJson: str = None, ConfigurationManager: Dict = None, ChefConfiguration: Dict = None, UseCustomCookbooks: bool = None, CustomCookbooksSource: Dict = None, DefaultSshKeyName: str = None, DefaultRootDeviceType: str = None, UseOpsworksSecurityGroups: bool = None, AgentVersion: str = None):
        pass

    def update_user_profile(self, IamUserArn: str, SshUsername: str = None, SshPublicKey: str = None, AllowSelfManagement: bool = None):
        pass

    def update_volume(self, VolumeId: str, Name: str = None, MountPoint: str = None):
        pass
