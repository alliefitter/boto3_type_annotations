from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def batch_update_schedule(self, ChannelId: str, Creates: Dict = None, Deletes: Dict = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_channel(self, Destinations: List = None, EncoderSettings: Dict = None, InputAttachments: List = None, InputSpecification: Dict = None, LogLevel: str = None, Name: str = None, RequestId: str = None, Reserved: str = None, RoleArn: str = None) -> Dict:
        pass

    def create_input(self, Destinations: List = None, InputSecurityGroups: List = None, Name: str = None, RequestId: str = None, Sources: List = None, Type: str = None) -> Dict:
        pass

    def create_input_security_group(self, WhitelistRules: List = None) -> Dict:
        pass

    def delete_channel(self, ChannelId: str) -> Dict:
        pass

    def delete_input(self, InputId: str) -> Dict:
        pass

    def delete_input_security_group(self, InputSecurityGroupId: str) -> Dict:
        pass

    def delete_reservation(self, ReservationId: str) -> Dict:
        pass

    def describe_channel(self, ChannelId: str) -> Dict:
        pass

    def describe_input(self, InputId: str) -> Dict:
        pass

    def describe_input_security_group(self, InputSecurityGroupId: str) -> Dict:
        pass

    def describe_offering(self, OfferingId: str) -> Dict:
        pass

    def describe_reservation(self, ReservationId: str) -> Dict:
        pass

    def describe_schedule(self, ChannelId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_channels(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_input_security_groups(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_inputs(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_offerings(self, ChannelConfiguration: str = None, Codec: str = None, MaxResults: int = None, MaximumBitrate: str = None, MaximumFramerate: str = None, NextToken: str = None, Resolution: str = None, ResourceType: str = None, SpecialFeature: str = None, VideoQuality: str = None) -> Dict:
        pass

    def list_reservations(self, Codec: str = None, MaxResults: int = None, MaximumBitrate: str = None, MaximumFramerate: str = None, NextToken: str = None, Resolution: str = None, ResourceType: str = None, SpecialFeature: str = None, VideoQuality: str = None) -> Dict:
        pass

    def purchase_offering(self, Count: int, OfferingId: str, Name: str = None, RequestId: str = None, Start: str = None) -> Dict:
        pass

    def start_channel(self, ChannelId: str) -> Dict:
        pass

    def stop_channel(self, ChannelId: str) -> Dict:
        pass

    def update_channel(self, ChannelId: str, Destinations: List = None, EncoderSettings: Dict = None, InputAttachments: List = None, InputSpecification: Dict = None, LogLevel: str = None, Name: str = None, RoleArn: str = None) -> Dict:
        pass

    def update_input(self, InputId: str, Destinations: List = None, InputSecurityGroups: List = None, Name: str = None, Sources: List = None) -> Dict:
        pass

    def update_input_security_group(self, InputSecurityGroupId: str, WhitelistRules: List = None) -> Dict:
        pass
