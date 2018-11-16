from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def accept_match(self, TicketId: str, PlayerIds: List, AcceptanceType: str) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_alias(self, Name: str, RoutingStrategy: Dict, Description: str = None) -> Dict:
        pass

    def create_build(self, Name: str = None, Version: str = None, StorageLocation: Dict = None, OperatingSystem: str = None) -> Dict:
        pass

    def create_fleet(self, Name: str, BuildId: str, EC2InstanceType: str, Description: str = None, ServerLaunchPath: str = None, ServerLaunchParameters: str = None, LogPaths: List = None, EC2InboundPermissions: List = None, NewGameSessionProtectionPolicy: str = None, RuntimeConfiguration: Dict = None, ResourceCreationLimitPolicy: Dict = None, MetricGroups: List = None, PeerVpcAwsAccountId: str = None, PeerVpcId: str = None, FleetType: str = None) -> Dict:
        pass

    def create_game_session(self, MaximumPlayerSessionCount: int, FleetId: str = None, AliasId: str = None, Name: str = None, GameProperties: List = None, CreatorId: str = None, GameSessionId: str = None, IdempotencyToken: str = None, GameSessionData: str = None) -> Dict:
        pass

    def create_game_session_queue(self, Name: str, TimeoutInSeconds: int = None, PlayerLatencyPolicies: List = None, Destinations: List = None) -> Dict:
        pass

    def create_matchmaking_configuration(self, Name: str, GameSessionQueueArns: List, RequestTimeoutSeconds: int, AcceptanceRequired: bool, RuleSetName: str, Description: str = None, AcceptanceTimeoutSeconds: int = None, NotificationTarget: str = None, AdditionalPlayerCount: int = None, CustomEventData: str = None, GameProperties: List = None, GameSessionData: str = None) -> Dict:
        pass

    def create_matchmaking_rule_set(self, Name: str, RuleSetBody: str) -> Dict:
        pass

    def create_player_session(self, GameSessionId: str, PlayerId: str, PlayerData: str = None) -> Dict:
        pass

    def create_player_sessions(self, GameSessionId: str, PlayerIds: List, PlayerDataMap: Dict = None) -> Dict:
        pass

    def create_vpc_peering_authorization(self, GameLiftAwsAccountId: str, PeerVpcId: str) -> Dict:
        pass

    def create_vpc_peering_connection(self, FleetId: str, PeerVpcAwsAccountId: str, PeerVpcId: str) -> Dict:
        pass

    def delete_alias(self, AliasId: str):
        pass

    def delete_build(self, BuildId: str):
        pass

    def delete_fleet(self, FleetId: str):
        pass

    def delete_game_session_queue(self, Name: str) -> Dict:
        pass

    def delete_matchmaking_configuration(self, Name: str) -> Dict:
        pass

    def delete_scaling_policy(self, Name: str, FleetId: str):
        pass

    def delete_vpc_peering_authorization(self, GameLiftAwsAccountId: str, PeerVpcId: str) -> Dict:
        pass

    def delete_vpc_peering_connection(self, FleetId: str, VpcPeeringConnectionId: str) -> Dict:
        pass

    def describe_alias(self, AliasId: str) -> Dict:
        pass

    def describe_build(self, BuildId: str) -> Dict:
        pass

    def describe_ec2_instance_limits(self, EC2InstanceType: str = None) -> Dict:
        pass

    def describe_fleet_attributes(self, FleetIds: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_fleet_capacity(self, FleetIds: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_fleet_events(self, FleetId: str, StartTime: datetime = None, EndTime: datetime = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_fleet_port_settings(self, FleetId: str) -> Dict:
        pass

    def describe_fleet_utilization(self, FleetIds: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_game_session_details(self, FleetId: str = None, GameSessionId: str = None, AliasId: str = None, StatusFilter: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_game_session_placement(self, PlacementId: str) -> Dict:
        pass

    def describe_game_session_queues(self, Names: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_game_sessions(self, FleetId: str = None, GameSessionId: str = None, AliasId: str = None, StatusFilter: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_instances(self, FleetId: str, InstanceId: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_matchmaking(self, TicketIds: List) -> Dict:
        pass

    def describe_matchmaking_configurations(self, Names: List = None, RuleSetName: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_matchmaking_rule_sets(self, Names: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_player_sessions(self, GameSessionId: str = None, PlayerId: str = None, PlayerSessionId: str = None, PlayerSessionStatusFilter: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_runtime_configuration(self, FleetId: str) -> Dict:
        pass

    def describe_scaling_policies(self, FleetId: str, StatusFilter: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_vpc_peering_authorizations(self) -> Dict:
        pass

    def describe_vpc_peering_connections(self, FleetId: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_game_session_log_url(self, GameSessionId: str) -> Dict:
        pass

    def get_instance_access(self, FleetId: str, InstanceId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_aliases(self, RoutingStrategyType: str = None, Name: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def list_builds(self, Status: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def list_fleets(self, BuildId: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def put_scaling_policy(self, Name: str, FleetId: str, MetricName: str, ScalingAdjustment: int = None, ScalingAdjustmentType: str = None, Threshold: float = None, ComparisonOperator: str = None, EvaluationPeriods: int = None, PolicyType: str = None, TargetConfiguration: Dict = None) -> Dict:
        pass

    def request_upload_credentials(self, BuildId: str) -> Dict:
        pass

    def resolve_alias(self, AliasId: str) -> Dict:
        pass

    def search_game_sessions(self, FleetId: str = None, AliasId: str = None, FilterExpression: str = None, SortExpression: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def start_fleet_actions(self, FleetId: str, Actions: List) -> Dict:
        pass

    def start_game_session_placement(self, PlacementId: str, GameSessionQueueName: str, MaximumPlayerSessionCount: int, GameProperties: List = None, GameSessionName: str = None, PlayerLatencies: List = None, DesiredPlayerSessions: List = None, GameSessionData: str = None) -> Dict:
        pass

    def start_match_backfill(self, ConfigurationName: str, GameSessionArn: str, Players: List, TicketId: str = None) -> Dict:
        pass

    def start_matchmaking(self, ConfigurationName: str, Players: List, TicketId: str = None) -> Dict:
        pass

    def stop_fleet_actions(self, FleetId: str, Actions: List) -> Dict:
        pass

    def stop_game_session_placement(self, PlacementId: str) -> Dict:
        pass

    def stop_matchmaking(self, TicketId: str) -> Dict:
        pass

    def update_alias(self, AliasId: str, Name: str = None, Description: str = None, RoutingStrategy: Dict = None) -> Dict:
        pass

    def update_build(self, BuildId: str, Name: str = None, Version: str = None) -> Dict:
        pass

    def update_fleet_attributes(self, FleetId: str, Name: str = None, Description: str = None, NewGameSessionProtectionPolicy: str = None, ResourceCreationLimitPolicy: Dict = None, MetricGroups: List = None) -> Dict:
        pass

    def update_fleet_capacity(self, FleetId: str, DesiredInstances: int = None, MinSize: int = None, MaxSize: int = None) -> Dict:
        pass

    def update_fleet_port_settings(self, FleetId: str, InboundPermissionAuthorizations: List = None, InboundPermissionRevocations: List = None) -> Dict:
        pass

    def update_game_session(self, GameSessionId: str, MaximumPlayerSessionCount: int = None, Name: str = None, PlayerSessionCreationPolicy: str = None, ProtectionPolicy: str = None) -> Dict:
        pass

    def update_game_session_queue(self, Name: str, TimeoutInSeconds: int = None, PlayerLatencyPolicies: List = None, Destinations: List = None) -> Dict:
        pass

    def update_matchmaking_configuration(self, Name: str, Description: str = None, GameSessionQueueArns: List = None, RequestTimeoutSeconds: int = None, AcceptanceTimeoutSeconds: int = None, AcceptanceRequired: bool = None, RuleSetName: str = None, NotificationTarget: str = None, AdditionalPlayerCount: int = None, CustomEventData: str = None, GameProperties: List = None, GameSessionData: str = None) -> Dict:
        pass

    def update_runtime_configuration(self, FleetId: str, RuntimeConfiguration: Dict) -> Dict:
        pass

    def validate_matchmaking_rule_set(self, RuleSetBody: str) -> Dict:
        pass
