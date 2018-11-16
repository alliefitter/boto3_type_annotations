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

    def cancel_key_deletion(self, KeyId: str) -> Dict:
        pass

    def create_alias(self, AliasName: str, TargetKeyId: str):
        pass

    def create_grant(self, KeyId: str, GranteePrincipal: str, Operations: List, RetiringPrincipal: str = None, Constraints: Dict = None, GrantTokens: List = None, Name: str = None) -> Dict:
        pass

    def create_key(self, Policy: str = None, Description: str = None, KeyUsage: str = None, Origin: str = None, BypassPolicyLockoutSafetyCheck: bool = None, Tags: List = None) -> Dict:
        pass

    def decrypt(self, CiphertextBlob: bytes, EncryptionContext: Dict = None, GrantTokens: List = None) -> Dict:
        pass

    def delete_alias(self, AliasName: str):
        pass

    def delete_imported_key_material(self, KeyId: str):
        pass

    def describe_key(self, KeyId: str, GrantTokens: List = None) -> Dict:
        pass

    def disable_key(self, KeyId: str):
        pass

    def disable_key_rotation(self, KeyId: str):
        pass

    def enable_key(self, KeyId: str):
        pass

    def enable_key_rotation(self, KeyId: str):
        pass

    def encrypt(self, KeyId: str, Plaintext: bytes, EncryptionContext: Dict = None, GrantTokens: List = None) -> Dict:
        pass

    def generate_data_key(self, KeyId: str, EncryptionContext: Dict = None, NumberOfBytes: int = None, KeySpec: str = None, GrantTokens: List = None) -> Dict:
        pass

    def generate_data_key_without_plaintext(self, KeyId: str, EncryptionContext: Dict = None, KeySpec: str = None, NumberOfBytes: int = None, GrantTokens: List = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def generate_random(self, NumberOfBytes: int = None) -> Dict:
        pass

    def get_key_policy(self, KeyId: str, PolicyName: str) -> Dict:
        pass

    def get_key_rotation_status(self, KeyId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_parameters_for_import(self, KeyId: str, WrappingAlgorithm: str, WrappingKeySpec: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def import_key_material(self, KeyId: str, ImportToken: bytes, EncryptedKeyMaterial: bytes, ValidTo: datetime = None, ExpirationModel: str = None) -> Dict:
        pass

    def list_aliases(self, KeyId: str = None, Limit: int = None, Marker: str = None) -> Dict:
        pass

    def list_grants(self, KeyId: str, Limit: int = None, Marker: str = None) -> Dict:
        pass

    def list_key_policies(self, KeyId: str, Limit: int = None, Marker: str = None) -> Dict:
        pass

    def list_keys(self, Limit: int = None, Marker: str = None) -> Dict:
        pass

    def list_resource_tags(self, KeyId: str, Limit: int = None, Marker: str = None) -> Dict:
        pass

    def list_retirable_grants(self, RetiringPrincipal: str, Limit: int = None, Marker: str = None) -> Dict:
        pass

    def put_key_policy(self, KeyId: str, PolicyName: str, Policy: str, BypassPolicyLockoutSafetyCheck: bool = None):
        pass

    def re_encrypt(self, CiphertextBlob: bytes, DestinationKeyId: str, SourceEncryptionContext: Dict = None, DestinationEncryptionContext: Dict = None, GrantTokens: List = None) -> Dict:
        pass

    def retire_grant(self, GrantToken: str = None, KeyId: str = None, GrantId: str = None):
        pass

    def revoke_grant(self, KeyId: str, GrantId: str):
        pass

    def schedule_key_deletion(self, KeyId: str, PendingWindowInDays: int = None) -> Dict:
        pass

    def tag_resource(self, KeyId: str, Tags: List):
        pass

    def untag_resource(self, KeyId: str, TagKeys: List):
        pass

    def update_alias(self, AliasName: str, TargetKeyId: str):
        pass

    def update_key_description(self, KeyId: str, Description: str):
        pass
