from boto3.resources.collection import ResourceCollection
from typing import List
from typing import Optional
from typing import Union
from datetime import datetime
from typing import Dict
from boto3.resources import base


class ServiceResource(base.ServiceResource):
    groups: 'groups'
    instance_profiles: 'instance_profiles'
    policies: 'policies'
    roles: 'roles'
    saml_providers: 'saml_providers'
    server_certificates: 'server_certificates'
    users: 'users'
    virtual_mfa_devices: 'virtual_mfa_devices'

    def AccessKey(self, user_name: str = None, id: str = None) -> 'AccessKey':
        pass

    def AccessKeyPair(self, user_name: str = None, id: str = None, secret: str = None) -> 'AccessKeyPair':
        pass

    def AccountPasswordPolicy(self) -> 'AccountPasswordPolicy':
        pass

    def AccountSummary(self) -> 'AccountSummary':
        pass

    def AssumeRolePolicy(self, role_name: str = None) -> 'AssumeRolePolicy':
        pass

    def CurrentUser(self) -> 'CurrentUser':
        pass

    def Group(self, name: str = None) -> 'Group':
        pass

    def GroupPolicy(self, group_name: str = None, name: str = None) -> 'GroupPolicy':
        pass

    def InstanceProfile(self, name: str = None) -> 'InstanceProfile':
        pass

    def LoginProfile(self, user_name: str = None) -> 'LoginProfile':
        pass

    def MfaDevice(self, user_name: str = None, serial_number: str = None) -> 'MfaDevice':
        pass

    def Policy(self, policy_arn: str = None) -> 'Policy':
        pass

    def PolicyVersion(self, arn: str = None, version_id: str = None) -> 'PolicyVersion':
        pass

    def Role(self, name: str = None) -> 'Role':
        pass

    def RolePolicy(self, role_name: str = None, name: str = None) -> 'RolePolicy':
        pass

    def SamlProvider(self, arn: str = None) -> 'SamlProvider':
        pass

    def ServerCertificate(self, name: str = None) -> 'ServerCertificate':
        pass

    def SigningCertificate(self, user_name: str = None, id: str = None) -> 'SigningCertificate':
        pass

    def User(self, name: str = None) -> 'User':
        pass

    def UserPolicy(self, user_name: str = None, name: str = None) -> 'UserPolicy':
        pass

    def VirtualMfaDevice(self, serial_number: str = None) -> 'VirtualMfaDevice':
        pass

    def change_password(self, OldPassword: str, NewPassword: str):
        pass

    def create_account_alias(self, AccountAlias: str):
        pass

    def create_account_password_policy(self, MinimumPasswordLength: int = None, RequireSymbols: bool = None, RequireNumbers: bool = None, RequireUppercaseCharacters: bool = None, RequireLowercaseCharacters: bool = None, AllowUsersToChangePassword: bool = None, MaxPasswordAge: int = None, PasswordReusePrevention: int = None, HardExpiry: bool = None) -> 'AccountPasswordPolicy':
        pass

    def create_group(self, GroupName: str, Path: str = None) -> List['Group']:
        pass

    def create_instance_profile(self, InstanceProfileName: str, Path: str = None) -> 'InstanceProfile':
        pass

    def create_policy(self, PolicyName: str, PolicyDocument: str, Path: str = None, Description: str = None) -> 'Policy':
        pass

    def create_role(self, RoleName: str, AssumeRolePolicyDocument: str, Path: str = None, Description: str = None, MaxSessionDuration: int = None, PermissionsBoundary: str = None) -> 'Role':
        pass

    def create_saml_provider(self, SAMLMetadataDocument: str, Name: str) -> 'SamlProvider':
        pass

    def create_server_certificate(self, ServerCertificateName: str, CertificateBody: str, PrivateKey: str, Path: str = None, CertificateChain: str = None) -> 'ServerCertificate':
        pass

    def create_signing_certificate(self, CertificateBody: str, UserName: str = None) -> 'SigningCertificate':
        pass

    def create_user(self, UserName: str, Path: str = None, PermissionsBoundary: str = None) -> 'User':
        pass

    def create_virtual_mfa_device(self, VirtualMFADeviceName: str, Path: str = None) -> 'VirtualMfaDevice':
        pass

    def get_available_subresources(self) -> List[str]:
        pass


class AccessKey(base.ServiceResource):
    access_key_id: str
    status: str
    create_date: datetime
    user_name: str
    id: str

    def activate(self):
        pass

    def deactivate(self):
        pass

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass


class AccessKeyPair(base.ServiceResource):
    access_key_id: str
    status: str
    secret_access_key: str
    create_date: datetime
    user_name: str
    id: str
    secret: str

    def activate(self):
        pass

    def deactivate(self):
        pass

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass


class AccountPasswordPolicy(base.ServiceResource):
    minimum_password_length: int
    require_symbols: bool
    require_numbers: bool
    require_uppercase_characters: bool
    require_lowercase_characters: bool
    allow_users_to_change_password: bool
    expire_passwords: bool
    max_password_age: int
    password_reuse_prevention: int
    hard_expiry: bool

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass

    def update(self, MinimumPasswordLength: int = None, RequireSymbols: bool = None, RequireNumbers: bool = None, RequireUppercaseCharacters: bool = None, RequireLowercaseCharacters: bool = None, AllowUsersToChangePassword: bool = None, MaxPasswordAge: int = None, PasswordReusePrevention: int = None, HardExpiry: bool = None):
        pass


class AccountSummary(base.ServiceResource):
    summary_map: Dict

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass


class AssumeRolePolicy(base.ServiceResource):
    role_name: str

    def get_available_subresources(self) -> List[str]:
        pass

    def update(self, PolicyDocument: str):
        pass


class CurrentUser(base.ServiceResource):
    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: Dict
    access_keys: 'access_keys'
    mfa_devices: 'mfa_devices'
    signing_certificates: 'signing_certificates'

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass


class Group(base.ServiceResource):
    path: str
    group_name: str
    group_id: str
    arn: str
    create_date: datetime
    name: str
    attached_policies: 'attached_policies'
    policies: 'policies'
    users: 'users'

    def add_user(self, UserName: str):
        pass

    def attach_policy(self, PolicyArn: str):
        pass

    def create(self, Path: str = None) -> List['Group']:
        pass

    def create_policy(self, PolicyName: str, PolicyDocument: str) -> 'GroupPolicy':
        pass

    def delete(self):
        pass

    def detach_policy(self, PolicyArn: str):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass

    def remove_user(self, UserName: str):
        pass

    def update(self, NewPath: str = None, NewGroupName: str = None) -> List['Group']:
        pass


class GroupPolicy(base.ServiceResource):
    policy_name: str
    policy_document: str
    group_name: str
    name: str

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def put(self, PolicyDocument: str):
        pass

    def reload(self):
        pass


class InstanceProfile(base.ServiceResource):
    path: str
    instance_profile_name: str
    instance_profile_id: str
    arn: str
    create_date: datetime
    roles_attribute: List
    name: str

    def add_role(self, RoleName: str):
        pass

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass

    def remove_role(self, RoleName: str):
        pass


class LoginProfile(base.ServiceResource):
    create_date: datetime
    password_reset_required: bool
    user_name: str

    def create(self, Password: str, PasswordResetRequired: bool = None) -> 'LoginProfile':
        pass

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass

    def update(self, Password: str = None, PasswordResetRequired: bool = None):
        pass


class MfaDevice(base.ServiceResource):
    enable_date: datetime
    user_name: str
    serial_number: str

    def associate(self, AuthenticationCode1: str, AuthenticationCode2: str):
        pass

    def disassociate(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def resync(self, AuthenticationCode1: str, AuthenticationCode2: str):
        pass


class Policy(base.ServiceResource):
    policy_name: str
    policy_id: str
    path: str
    default_version_id: str
    attachment_count: int
    permissions_boundary_usage_count: int
    is_attachable: bool
    description: str
    create_date: datetime
    update_date: datetime
    arn: str
    attached_groups: 'attached_groups'
    attached_roles: 'attached_roles'
    attached_users: 'attached_users'
    versions: 'versions'

    def attach_group(self, GroupName: str):
        pass

    def attach_role(self, RoleName: str):
        pass

    def attach_user(self, UserName: str):
        pass

    def create_version(self, PolicyDocument: str, SetAsDefault: bool = None) -> 'PolicyVersion':
        pass

    def delete(self):
        pass

    def detach_group(self, GroupName: str):
        pass

    def detach_role(self, RoleName: str):
        pass

    def detach_user(self, UserName: str):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass


class PolicyVersion(base.ServiceResource):
    document: str
    is_default_version: bool
    create_date: datetime
    arn: str
    version_id: str

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass

    def set_as_default(self):
        pass


class Role(base.ServiceResource):
    path: str
    role_name: str
    role_id: str
    arn: str
    create_date: datetime
    assume_role_policy_document: str
    description: str
    max_session_duration: int
    permissions_boundary: Dict
    name: str
    attached_policies: 'attached_policies'
    instance_profiles: 'instance_profiles'
    policies: 'policies'

    def attach_policy(self, PolicyArn: str):
        pass

    def delete(self):
        pass

    def detach_policy(self, PolicyArn: str):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass


class RolePolicy(base.ServiceResource):
    policy_name: str
    policy_document: str
    role_name: str
    name: str

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def put(self, PolicyDocument: str):
        pass

    def reload(self):
        pass


class SamlProvider(base.ServiceResource):
    saml_metadata_document: str
    create_date: datetime
    valid_until: datetime
    arn: str

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass

    def update(self, SAMLMetadataDocument: str) -> Dict:
        pass


class ServerCertificate(base.ServiceResource):
    server_certificate_metadata: Dict
    certificate_body: str
    certificate_chain: str
    name: str

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass

    def update(self, NewPath: str = None, NewServerCertificateName: str = None) -> 'ServerCertificate':
        pass


class SigningCertificate(base.ServiceResource):
    certificate_id: str
    certificate_body: str
    status: str
    upload_date: datetime
    user_name: str
    id: str

    def activate(self):
        pass

    def deactivate(self):
        pass

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass


class User(base.ServiceResource):
    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: Dict
    name: str
    access_keys: 'access_keys'
    attached_policies: 'attached_policies'
    groups: 'groups'
    mfa_devices: 'mfa_devices'
    policies: 'policies'
    signing_certificates: 'signing_certificates'

    def add_group(self, GroupName: str):
        pass

    def attach_policy(self, PolicyArn: str):
        pass

    def create(self, Path: str = None, PermissionsBoundary: str = None) -> 'User':
        pass

    def create_access_key_pair(self) -> 'AccessKeyPair':
        pass

    def create_login_profile(self, Password: str, PasswordResetRequired: bool = None) -> 'LoginProfile':
        pass

    def create_policy(self, PolicyName: str, PolicyDocument: str) -> 'UserPolicy':
        pass

    def delete(self):
        pass

    def detach_policy(self, PolicyArn: str):
        pass

    def enable_mfa(self, SerialNumber: str, AuthenticationCode1: str, AuthenticationCode2: str) -> 'MfaDevice':
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass

    def remove_group(self, GroupName: str):
        pass

    def update(self, NewPath: str = None, NewUserName: str = None) -> 'User':
        pass


class UserPolicy(base.ServiceResource):
    policy_name: str
    policy_document: str
    user_name: str
    name: str

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def put(self, PolicyDocument: str):
        pass

    def reload(self):
        pass


class VirtualMfaDevice(base.ServiceResource):
    base32_string_seed: bytes
    qr_code_png: bytes
    user_attribute: Dict
    enable_date: datetime
    serial_number: str

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass


class groups(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Group']:
        pass

    
    @classmethod
    def filter(cls, PathPrefix: str = None, Marker: str = None, MaxItems: int = None) -> List['Group']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Group']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Group']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class instance_profiles(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['InstanceProfile']:
        pass

    
    @classmethod
    def filter(cls, PathPrefix: str = None, Marker: str = None, MaxItems: int = None) -> List['InstanceProfile']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['InstanceProfile']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['InstanceProfile']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class policies(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Policy']:
        pass

    
    @classmethod
    def filter(cls, Scope: str = None, OnlyAttached: bool = None, PathPrefix: str = None, PolicyUsageFilter: str = None, Marker: str = None, MaxItems: int = None) -> List['Policy']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Policy']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Policy']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class roles(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Role']:
        pass

    
    @classmethod
    def filter(cls, PathPrefix: str = None, Marker: str = None, MaxItems: int = None) -> List['Role']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Role']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Role']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class saml_providers(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['SamlProvider']:
        pass

    
    @classmethod
    def filter(cls) -> List['SamlProvider']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['SamlProvider']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['SamlProvider']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class server_certificates(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['ServerCertificate']:
        pass

    
    @classmethod
    def filter(cls, PathPrefix: str = None, Marker: str = None, MaxItems: int = None) -> List['ServerCertificate']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['ServerCertificate']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['ServerCertificate']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class users(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['User']:
        pass

    
    @classmethod
    def filter(cls, PathPrefix: str = None, Marker: str = None, MaxItems: int = None) -> List['User']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['User']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['User']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class virtual_mfa_devices(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['VirtualMfaDevice']:
        pass

    
    @classmethod
    def filter(cls, AssignmentStatus: str = None, Marker: str = None, MaxItems: int = None) -> List['VirtualMfaDevice']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['VirtualMfaDevice']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['VirtualMfaDevice']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass
