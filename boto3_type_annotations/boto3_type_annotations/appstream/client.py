from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def associate_fleet(self, FleetName: str, StackName: str) -> Dict:
        pass

    def batch_associate_user_stack(self, UserStackAssociations: List) -> Dict:
        pass

    def batch_disassociate_user_stack(self, UserStackAssociations: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def copy_image(self, SourceImageName: str, DestinationImageName: str, DestinationRegion: str, DestinationImageDescription: str = None) -> Dict:
        pass

    def create_directory_config(self, DirectoryName: str, OrganizationalUnitDistinguishedNames: List, ServiceAccountCredentials: Dict) -> Dict:
        pass

    def create_fleet(self, Name: str, InstanceType: str, ComputeCapacity: Dict, ImageName: str = None, ImageArn: str = None, FleetType: str = None, VpcConfig: Dict = None, MaxUserDurationInSeconds: int = None, DisconnectTimeoutInSeconds: int = None, Description: str = None, DisplayName: str = None, EnableDefaultInternetAccess: bool = None, DomainJoinInfo: Dict = None) -> Dict:
        pass

    def create_image_builder(self, Name: str, InstanceType: str, ImageName: str = None, ImageArn: str = None, Description: str = None, DisplayName: str = None, VpcConfig: Dict = None, EnableDefaultInternetAccess: bool = None, DomainJoinInfo: Dict = None, AppstreamAgentVersion: str = None) -> Dict:
        pass

    def create_image_builder_streaming_url(self, Name: str, Validity: int = None) -> Dict:
        pass

    def create_stack(self, Name: str, Description: str = None, DisplayName: str = None, StorageConnectors: List = None, RedirectURL: str = None, FeedbackURL: str = None, UserSettings: List = None, ApplicationSettings: Dict = None) -> Dict:
        pass

    def create_streaming_url(self, StackName: str, FleetName: str, UserId: str, ApplicationId: str = None, Validity: int = None, SessionContext: str = None) -> Dict:
        pass

    def create_user(self, UserName: str, AuthenticationType: str, MessageAction: str = None, FirstName: str = None, LastName: str = None) -> Dict:
        pass

    def delete_directory_config(self, DirectoryName: str) -> Dict:
        pass

    def delete_fleet(self, Name: str) -> Dict:
        pass

    def delete_image(self, Name: str) -> Dict:
        pass

    def delete_image_builder(self, Name: str) -> Dict:
        pass

    def delete_image_permissions(self, Name: str, SharedAccountId: str) -> Dict:
        pass

    def delete_stack(self, Name: str) -> Dict:
        pass

    def delete_user(self, UserName: str, AuthenticationType: str) -> Dict:
        pass

    def describe_directory_configs(self, DirectoryNames: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_fleets(self, Names: List = None, NextToken: str = None) -> Dict:
        pass

    def describe_image_builders(self, Names: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_image_permissions(self, Name: str, MaxResults: int = None, SharedAwsAccountIds: List = None, NextToken: str = None) -> Dict:
        pass

    def describe_images(self, Names: List = None, Arns: List = None, Type: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def describe_sessions(self, StackName: str, FleetName: str, UserId: str = None, NextToken: str = None, Limit: int = None, AuthenticationType: str = None) -> Dict:
        pass

    def describe_stacks(self, Names: List = None, NextToken: str = None) -> Dict:
        pass

    def describe_user_stack_associations(self, StackName: str = None, UserName: str = None, AuthenticationType: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_users(self, AuthenticationType: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def disable_user(self, UserName: str, AuthenticationType: str) -> Dict:
        pass

    def disassociate_fleet(self, FleetName: str, StackName: str) -> Dict:
        pass

    def enable_user(self, UserName: str, AuthenticationType: str) -> Dict:
        pass

    def expire_session(self, SessionId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_associated_fleets(self, StackName: str, NextToken: str = None) -> Dict:
        pass

    def list_associated_stacks(self, FleetName: str, NextToken: str = None) -> Dict:
        pass

    def list_tags_for_resource(self, ResourceArn: str) -> Dict:
        pass

    def start_fleet(self, Name: str) -> Dict:
        pass

    def start_image_builder(self, Name: str, AppstreamAgentVersion: str = None) -> Dict:
        pass

    def stop_fleet(self, Name: str) -> Dict:
        pass

    def stop_image_builder(self, Name: str) -> Dict:
        pass

    def tag_resource(self, ResourceArn: str, Tags: Dict) -> Dict:
        pass

    def untag_resource(self, ResourceArn: str, TagKeys: List) -> Dict:
        pass

    def update_directory_config(self, DirectoryName: str, OrganizationalUnitDistinguishedNames: List = None, ServiceAccountCredentials: Dict = None) -> Dict:
        pass

    def update_fleet(self, ImageName: str = None, ImageArn: str = None, Name: str = None, InstanceType: str = None, ComputeCapacity: Dict = None, VpcConfig: Dict = None, MaxUserDurationInSeconds: int = None, DisconnectTimeoutInSeconds: int = None, DeleteVpcConfig: bool = None, Description: str = None, DisplayName: str = None, EnableDefaultInternetAccess: bool = None, DomainJoinInfo: Dict = None, AttributesToDelete: List = None) -> Dict:
        pass

    def update_image_permissions(self, Name: str, SharedAccountId: str, ImagePermissions: Dict) -> Dict:
        pass

    def update_stack(self, Name: str, DisplayName: str = None, Description: str = None, StorageConnectors: List = None, DeleteStorageConnectors: bool = None, RedirectURL: str = None, FeedbackURL: str = None, AttributesToDelete: List = None, UserSettings: List = None, ApplicationSettings: Dict = None) -> Dict:
        pass
