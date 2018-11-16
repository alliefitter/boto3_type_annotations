from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def approve_skill(self, SkillId: str) -> Dict:
        pass

    def associate_contact_with_address_book(self, ContactArn: str, AddressBookArn: str) -> Dict:
        pass

    def associate_device_with_room(self, DeviceArn: str = None, RoomArn: str = None) -> Dict:
        pass

    def associate_skill_group_with_room(self, SkillGroupArn: str = None, RoomArn: str = None) -> Dict:
        pass

    def associate_skill_with_skill_group(self, SkillId: str, SkillGroupArn: str = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_address_book(self, Name: str, Description: str = None, ClientRequestToken: str = None) -> Dict:
        pass

    def create_conference_provider(self, ConferenceProviderName: str, ConferenceProviderType: str, MeetingSetting: Dict, IPDialIn: Dict = None, PSTNDialIn: Dict = None, ClientRequestToken: str = None) -> Dict:
        pass

    def create_contact(self, FirstName: str, PhoneNumber: str, DisplayName: str = None, LastName: str = None, ClientRequestToken: str = None) -> Dict:
        pass

    def create_profile(self, ProfileName: str, Timezone: str, Address: str, DistanceUnit: str, TemperatureUnit: str, WakeWord: str, ClientRequestToken: str = None, SetupModeDisabled: bool = None, MaxVolumeLimit: int = None, PSTNEnabled: bool = None) -> Dict:
        pass

    def create_room(self, RoomName: str, Description: str = None, ProfileArn: str = None, ProviderCalendarId: str = None, ClientRequestToken: str = None, Tags: List = None) -> Dict:
        pass

    def create_skill_group(self, SkillGroupName: str, Description: str = None, ClientRequestToken: str = None) -> Dict:
        pass

    def create_user(self, UserId: str, FirstName: str = None, LastName: str = None, Email: str = None, ClientRequestToken: str = None, Tags: List = None) -> Dict:
        pass

    def delete_address_book(self, AddressBookArn: str) -> Dict:
        pass

    def delete_conference_provider(self, ConferenceProviderArn: str) -> Dict:
        pass

    def delete_contact(self, ContactArn: str) -> Dict:
        pass

    def delete_device(self, DeviceArn: str) -> Dict:
        pass

    def delete_profile(self, ProfileArn: str = None) -> Dict:
        pass

    def delete_room(self, RoomArn: str = None) -> Dict:
        pass

    def delete_room_skill_parameter(self, SkillId: str, ParameterKey: str, RoomArn: str = None) -> Dict:
        pass

    def delete_skill_authorization(self, SkillId: str, RoomArn: str = None) -> Dict:
        pass

    def delete_skill_group(self, SkillGroupArn: str = None) -> Dict:
        pass

    def delete_user(self, EnrollmentId: str, UserArn: str = None) -> Dict:
        pass

    def disassociate_contact_from_address_book(self, ContactArn: str, AddressBookArn: str) -> Dict:
        pass

    def disassociate_device_from_room(self, DeviceArn: str = None) -> Dict:
        pass

    def disassociate_skill_from_skill_group(self, SkillId: str, SkillGroupArn: str = None) -> Dict:
        pass

    def disassociate_skill_group_from_room(self, SkillGroupArn: str = None, RoomArn: str = None) -> Dict:
        pass

    def forget_smart_home_appliances(self, RoomArn: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_address_book(self, AddressBookArn: str) -> Dict:
        pass

    def get_conference_preference(self) -> Dict:
        pass

    def get_conference_provider(self, ConferenceProviderArn: str) -> Dict:
        pass

    def get_contact(self, ContactArn: str) -> Dict:
        pass

    def get_device(self, DeviceArn: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_profile(self, ProfileArn: str = None) -> Dict:
        pass

    def get_room(self, RoomArn: str = None) -> Dict:
        pass

    def get_room_skill_parameter(self, SkillId: str, ParameterKey: str, RoomArn: str = None) -> Dict:
        pass

    def get_skill_group(self, SkillGroupArn: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_conference_providers(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_device_events(self, DeviceArn: str, EventType: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_skills(self, SkillGroupArn: str = None, EnablementType: str = None, SkillType: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_skills_store_categories(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_skills_store_skills_by_category(self, CategoryId: int, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_smart_home_appliances(self, RoomArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_tags(self, Arn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def put_conference_preference(self, ConferencePreference: Dict) -> Dict:
        pass

    def put_room_skill_parameter(self, SkillId: str, RoomSkillParameter: Dict, RoomArn: str = None) -> Dict:
        pass

    def put_skill_authorization(self, AuthorizationResult: Dict, SkillId: str, RoomArn: str = None) -> Dict:
        pass

    def register_avs_device(self, ClientId: str, UserCode: str, ProductId: str, DeviceSerialNumber: str, AmazonId: str) -> Dict:
        pass

    def reject_skill(self, SkillId: str) -> Dict:
        pass

    def resolve_room(self, UserId: str, SkillId: str) -> Dict:
        pass

    def revoke_invitation(self, UserArn: str = None, EnrollmentId: str = None) -> Dict:
        pass

    def search_address_books(self, Filters: List = None, SortCriteria: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def search_contacts(self, Filters: List = None, SortCriteria: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def search_devices(self, NextToken: str = None, MaxResults: int = None, Filters: List = None, SortCriteria: List = None) -> Dict:
        pass

    def search_profiles(self, NextToken: str = None, MaxResults: int = None, Filters: List = None, SortCriteria: List = None) -> Dict:
        pass

    def search_rooms(self, NextToken: str = None, MaxResults: int = None, Filters: List = None, SortCriteria: List = None) -> Dict:
        pass

    def search_skill_groups(self, NextToken: str = None, MaxResults: int = None, Filters: List = None, SortCriteria: List = None) -> Dict:
        pass

    def search_users(self, NextToken: str = None, MaxResults: int = None, Filters: List = None, SortCriteria: List = None) -> Dict:
        pass

    def send_invitation(self, UserArn: str = None) -> Dict:
        pass

    def start_device_sync(self, Features: List, RoomArn: str = None, DeviceArn: str = None) -> Dict:
        pass

    def start_smart_home_appliance_discovery(self, RoomArn: str) -> Dict:
        pass

    def tag_resource(self, Arn: str, Tags: List) -> Dict:
        pass

    def untag_resource(self, Arn: str, TagKeys: List) -> Dict:
        pass

    def update_address_book(self, AddressBookArn: str, Name: str = None, Description: str = None) -> Dict:
        pass

    def update_conference_provider(self, ConferenceProviderArn: str, ConferenceProviderType: str, MeetingSetting: Dict, IPDialIn: Dict = None, PSTNDialIn: Dict = None) -> Dict:
        pass

    def update_contact(self, ContactArn: str, DisplayName: str = None, FirstName: str = None, LastName: str = None, PhoneNumber: str = None) -> Dict:
        pass

    def update_device(self, DeviceArn: str = None, DeviceName: str = None) -> Dict:
        pass

    def update_profile(self, ProfileArn: str = None, ProfileName: str = None, IsDefault: bool = None, Timezone: str = None, Address: str = None, DistanceUnit: str = None, TemperatureUnit: str = None, WakeWord: str = None, SetupModeDisabled: bool = None, MaxVolumeLimit: int = None, PSTNEnabled: bool = None) -> Dict:
        pass

    def update_room(self, RoomArn: str = None, RoomName: str = None, Description: str = None, ProviderCalendarId: str = None, ProfileArn: str = None) -> Dict:
        pass

    def update_skill_group(self, SkillGroupArn: str = None, SkillGroupName: str = None, Description: str = None) -> Dict:
        pass
