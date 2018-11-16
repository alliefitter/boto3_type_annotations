from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def attach_instances(self, AutoScalingGroupName: str, InstanceIds: List = None):
        pass

    def attach_load_balancer_target_groups(self, AutoScalingGroupName: str, TargetGroupARNs: List) -> Dict:
        pass

    def attach_load_balancers(self, AutoScalingGroupName: str, LoadBalancerNames: List) -> Dict:
        pass

    def batch_delete_scheduled_action(self, AutoScalingGroupName: str, ScheduledActionNames: List) -> Dict:
        pass

    def batch_put_scheduled_update_group_action(self, AutoScalingGroupName: str, ScheduledUpdateGroupActions: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def complete_lifecycle_action(self, LifecycleHookName: str, AutoScalingGroupName: str, LifecycleActionResult: str, LifecycleActionToken: str = None, InstanceId: str = None) -> Dict:
        pass

    def create_auto_scaling_group(self, AutoScalingGroupName: str, MinSize: int, MaxSize: int, LaunchConfigurationName: str = None, LaunchTemplate: Dict = None, InstanceId: str = None, DesiredCapacity: int = None, DefaultCooldown: int = None, AvailabilityZones: List = None, LoadBalancerNames: List = None, TargetGroupARNs: List = None, HealthCheckType: str = None, HealthCheckGracePeriod: int = None, PlacementGroup: str = None, VPCZoneIdentifier: str = None, TerminationPolicies: List = None, NewInstancesProtectedFromScaleIn: bool = None, LifecycleHookSpecificationList: List = None, Tags: List = None, ServiceLinkedRoleARN: str = None):
        pass

    def create_launch_configuration(self, LaunchConfigurationName: str, ImageId: str = None, KeyName: str = None, SecurityGroups: List = None, ClassicLinkVPCId: str = None, ClassicLinkVPCSecurityGroups: List = None, UserData: str = None, InstanceId: str = None, InstanceType: str = None, KernelId: str = None, RamdiskId: str = None, BlockDeviceMappings: List = None, InstanceMonitoring: Dict = None, SpotPrice: str = None, IamInstanceProfile: str = None, EbsOptimized: bool = None, AssociatePublicIpAddress: bool = None, PlacementTenancy: str = None):
        pass

    def create_or_update_tags(self, Tags: List):
        pass

    def delete_auto_scaling_group(self, AutoScalingGroupName: str, ForceDelete: bool = None):
        pass

    def delete_launch_configuration(self, LaunchConfigurationName: str):
        pass

    def delete_lifecycle_hook(self, LifecycleHookName: str, AutoScalingGroupName: str) -> Dict:
        pass

    def delete_notification_configuration(self, AutoScalingGroupName: str, TopicARN: str):
        pass

    def delete_policy(self, PolicyName: str, AutoScalingGroupName: str = None):
        pass

    def delete_scheduled_action(self, AutoScalingGroupName: str, ScheduledActionName: str):
        pass

    def delete_tags(self, Tags: List):
        pass

    def describe_account_limits(self) -> Dict:
        pass

    def describe_adjustment_types(self) -> Dict:
        pass

    def describe_auto_scaling_groups(self, AutoScalingGroupNames: List = None, NextToken: str = None, MaxRecords: int = None) -> Dict:
        pass

    def describe_auto_scaling_instances(self, InstanceIds: List = None, MaxRecords: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_auto_scaling_notification_types(self) -> Dict:
        pass

    def describe_launch_configurations(self, LaunchConfigurationNames: List = None, NextToken: str = None, MaxRecords: int = None) -> Dict:
        pass

    def describe_lifecycle_hook_types(self) -> Dict:
        pass

    def describe_lifecycle_hooks(self, AutoScalingGroupName: str, LifecycleHookNames: List = None) -> Dict:
        pass

    def describe_load_balancer_target_groups(self, AutoScalingGroupName: str, NextToken: str = None, MaxRecords: int = None) -> Dict:
        pass

    def describe_load_balancers(self, AutoScalingGroupName: str, NextToken: str = None, MaxRecords: int = None) -> Dict:
        pass

    def describe_metric_collection_types(self) -> Dict:
        pass

    def describe_notification_configurations(self, AutoScalingGroupNames: List = None, NextToken: str = None, MaxRecords: int = None) -> Dict:
        pass

    def describe_policies(self, AutoScalingGroupName: str = None, PolicyNames: List = None, PolicyTypes: List = None, NextToken: str = None, MaxRecords: int = None) -> Dict:
        pass

    def describe_scaling_activities(self, ActivityIds: List = None, AutoScalingGroupName: str = None, MaxRecords: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_scaling_process_types(self) -> Dict:
        pass

    def describe_scheduled_actions(self, AutoScalingGroupName: str = None, ScheduledActionNames: List = None, StartTime: datetime = None, EndTime: datetime = None, NextToken: str = None, MaxRecords: int = None) -> Dict:
        pass

    def describe_tags(self, Filters: List = None, NextToken: str = None, MaxRecords: int = None) -> Dict:
        pass

    def describe_termination_policy_types(self) -> Dict:
        pass

    def detach_instances(self, AutoScalingGroupName: str, ShouldDecrementDesiredCapacity: bool, InstanceIds: List = None) -> Dict:
        pass

    def detach_load_balancer_target_groups(self, AutoScalingGroupName: str, TargetGroupARNs: List) -> Dict:
        pass

    def detach_load_balancers(self, AutoScalingGroupName: str, LoadBalancerNames: List) -> Dict:
        pass

    def disable_metrics_collection(self, AutoScalingGroupName: str, Metrics: List = None):
        pass

    def enable_metrics_collection(self, AutoScalingGroupName: str, Granularity: str, Metrics: List = None):
        pass

    def enter_standby(self, AutoScalingGroupName: str, ShouldDecrementDesiredCapacity: bool, InstanceIds: List = None) -> Dict:
        pass

    def execute_policy(self, PolicyName: str, AutoScalingGroupName: str = None, HonorCooldown: bool = None, MetricValue: float = None, BreachThreshold: float = None):
        pass

    def exit_standby(self, AutoScalingGroupName: str, InstanceIds: List = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def put_lifecycle_hook(self, LifecycleHookName: str, AutoScalingGroupName: str, LifecycleTransition: str = None, RoleARN: str = None, NotificationTargetARN: str = None, NotificationMetadata: str = None, HeartbeatTimeout: int = None, DefaultResult: str = None) -> Dict:
        pass

    def put_notification_configuration(self, AutoScalingGroupName: str, TopicARN: str, NotificationTypes: List):
        pass

    def put_scaling_policy(self, AutoScalingGroupName: str, PolicyName: str, PolicyType: str = None, AdjustmentType: str = None, MinAdjustmentStep: int = None, MinAdjustmentMagnitude: int = None, ScalingAdjustment: int = None, Cooldown: int = None, MetricAggregationType: str = None, StepAdjustments: List = None, EstimatedInstanceWarmup: int = None, TargetTrackingConfiguration: Dict = None) -> Dict:
        pass

    def put_scheduled_update_group_action(self, AutoScalingGroupName: str, ScheduledActionName: str, Time: datetime = None, StartTime: datetime = None, EndTime: datetime = None, Recurrence: str = None, MinSize: int = None, MaxSize: int = None, DesiredCapacity: int = None):
        pass

    def record_lifecycle_action_heartbeat(self, LifecycleHookName: str, AutoScalingGroupName: str, LifecycleActionToken: str = None, InstanceId: str = None) -> Dict:
        pass

    def resume_processes(self, AutoScalingGroupName: str, ScalingProcesses: List = None):
        pass

    def set_desired_capacity(self, AutoScalingGroupName: str, DesiredCapacity: int, HonorCooldown: bool = None):
        pass

    def set_instance_health(self, InstanceId: str, HealthStatus: str, ShouldRespectGracePeriod: bool = None):
        pass

    def set_instance_protection(self, InstanceIds: List, AutoScalingGroupName: str, ProtectedFromScaleIn: bool) -> Dict:
        pass

    def suspend_processes(self, AutoScalingGroupName: str, ScalingProcesses: List = None):
        pass

    def terminate_instance_in_auto_scaling_group(self, InstanceId: str, ShouldDecrementDesiredCapacity: bool) -> Dict:
        pass

    def update_auto_scaling_group(self, AutoScalingGroupName: str, LaunchConfigurationName: str = None, LaunchTemplate: Dict = None, MinSize: int = None, MaxSize: int = None, DesiredCapacity: int = None, DefaultCooldown: int = None, AvailabilityZones: List = None, HealthCheckType: str = None, HealthCheckGracePeriod: int = None, PlacementGroup: str = None, VPCZoneIdentifier: str = None, TerminationPolicies: List = None, NewInstancesProtectedFromScaleIn: bool = None, ServiceLinkedRoleARN: str = None):
        pass
