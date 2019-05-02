from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def associate_phone_number_with_user(self, AccountId: str, UserId: str, E164PhoneNumber: str) -> Dict:
        pass

    def associate_phone_numbers_with_voice_connector(self, VoiceConnectorId: str, E164PhoneNumbers: List = None) -> Dict:
        pass

    def batch_delete_phone_number(self, PhoneNumberIds: List) -> Dict:
        pass

    def batch_suspend_user(self, AccountId: str, UserIdList: List) -> Dict:
        pass

    def batch_unsuspend_user(self, AccountId: str, UserIdList: List) -> Dict:
        pass

    def batch_update_phone_number(self, UpdatePhoneNumberRequestItems: List) -> Dict:
        pass

    def batch_update_user(self, AccountId: str, UpdateUserRequestItems: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_account(self, Name: str) -> Dict:
        pass

    def create_phone_number_order(self, ProductType: str, E164PhoneNumbers: List) -> Dict:
        pass

    def create_voice_connector(self, Name: str, RequireEncryption: bool) -> Dict:
        pass

    def delete_account(self, AccountId: str) -> Dict:
        pass

    def delete_phone_number(self, PhoneNumberId: str):
        pass

    def delete_voice_connector(self, VoiceConnectorId: str):
        pass

    def delete_voice_connector_origination(self, VoiceConnectorId: str):
        pass

    def delete_voice_connector_termination(self, VoiceConnectorId: str):
        pass

    def delete_voice_connector_termination_credentials(self, VoiceConnectorId: str, Usernames: List = None):
        pass

    def disassociate_phone_number_from_user(self, AccountId: str, UserId: str) -> Dict:
        pass

    def disassociate_phone_numbers_from_voice_connector(self, VoiceConnectorId: str, E164PhoneNumbers: List = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_account(self, AccountId: str) -> Dict:
        pass

    def get_account_settings(self, AccountId: str) -> Dict:
        pass

    def get_global_settings(self) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_phone_number(self, PhoneNumberId: str) -> Dict:
        pass

    def get_phone_number_order(self, PhoneNumberOrderId: str) -> Dict:
        pass

    def get_user(self, AccountId: str, UserId: str) -> Dict:
        pass

    def get_user_settings(self, AccountId: str, UserId: str) -> Dict:
        pass

    def get_voice_connector(self, VoiceConnectorId: str) -> Dict:
        pass

    def get_voice_connector_origination(self, VoiceConnectorId: str) -> Dict:
        pass

    def get_voice_connector_termination(self, VoiceConnectorId: str) -> Dict:
        pass

    def get_voice_connector_termination_health(self, VoiceConnectorId: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def invite_users(self, AccountId: str, UserEmailList: List) -> Dict:
        pass

    def list_accounts(self, Name: str = None, UserEmail: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_phone_number_orders(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_phone_numbers(self, Status: str = None, ProductType: str = None, FilterName: str = None, FilterValue: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_users(self, AccountId: str, UserEmail: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_voice_connector_termination_credentials(self, VoiceConnectorId: str) -> Dict:
        pass

    def list_voice_connectors(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def logout_user(self, AccountId: str, UserId: str) -> Dict:
        pass

    def put_voice_connector_origination(self, VoiceConnectorId: str, Origination: Dict) -> Dict:
        pass

    def put_voice_connector_termination(self, VoiceConnectorId: str, Termination: Dict) -> Dict:
        pass

    def put_voice_connector_termination_credentials(self, VoiceConnectorId: str, Credentials: List = None):
        pass

    def reset_personal_pin(self, AccountId: str, UserId: str) -> Dict:
        pass

    def restore_phone_number(self, PhoneNumberId: str) -> Dict:
        pass

    def search_available_phone_numbers(self, AreaCode: str = None, City: str = None, Country: str = None, State: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def update_account(self, AccountId: str, Name: str = None) -> Dict:
        pass

    def update_account_settings(self, AccountId: str, AccountSettings: Dict) -> Dict:
        pass

    def update_global_settings(self, BusinessCalling: Dict, VoiceConnector: Dict):
        pass

    def update_phone_number(self, PhoneNumberId: str, ProductType: str = None) -> Dict:
        pass

    def update_user(self, AccountId: str, UserId: str, LicenseType: str = None) -> Dict:
        pass

    def update_user_settings(self, AccountId: str, UserId: str, UserSettings: Dict):
        pass

    def update_voice_connector(self, VoiceConnectorId: str, Name: str, RequireEncryption: bool) -> Dict:
        pass
