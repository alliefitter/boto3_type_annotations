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
    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_user(self, Username: str, PhoneConfig: Dict, SecurityProfileIds: List, RoutingProfileId: str, InstanceId: str, Password: str = None, IdentityInfo: Dict = None, DirectoryUserId: str = None, HierarchyGroupId: str = None) -> Dict:
        pass

    def delete_user(self, InstanceId: str, UserId: str) -> NoReturn:
        pass

    def describe_user(self, UserId: str, InstanceId: str) -> Dict:
        pass

    def describe_user_hierarchy_group(self, HierarchyGroupId: str, InstanceId: str) -> Dict:
        pass

    def describe_user_hierarchy_structure(self, InstanceId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_current_metric_data(self, InstanceId: str, Filters: Dict, CurrentMetrics: List, Groupings: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def get_federation_token(self, InstanceId: str) -> Dict:
        pass

    def get_metric_data(self, InstanceId: str, StartTime: datetime, EndTime: datetime, Filters: Dict, HistoricalMetrics: List, Groupings: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_routing_profiles(self, InstanceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_security_profiles(self, InstanceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_user_hierarchy_groups(self, InstanceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_users(self, InstanceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def start_outbound_voice_contact(self, DestinationPhoneNumber: str, ContactFlowId: str, InstanceId: str, ClientToken: str = None, SourcePhoneNumber: str = None, QueueId: str = None, Attributes: Dict = None) -> Dict:
        pass

    def stop_contact(self, ContactId: str, InstanceId: str) -> Dict:
        pass

    def update_contact_attributes(self, InitialContactId: str, InstanceId: str, Attributes: Dict) -> Dict:
        pass

    def update_user_hierarchy(self, UserId: str, InstanceId: str, HierarchyGroupId: str = None) -> NoReturn:
        pass

    def update_user_identity_info(self, IdentityInfo: Dict, UserId: str, InstanceId: str) -> NoReturn:
        pass

    def update_user_phone_config(self, PhoneConfig: Dict, UserId: str, InstanceId: str) -> NoReturn:
        pass

    def update_user_routing_profile(self, RoutingProfileId: str, UserId: str, InstanceId: str) -> NoReturn:
        pass

    def update_user_security_profiles(self, SecurityProfileIds: List, UserId: str, InstanceId: str) -> NoReturn:
        pass
