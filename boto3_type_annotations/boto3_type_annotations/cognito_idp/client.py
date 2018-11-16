from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def add_custom_attributes(self, UserPoolId: str, CustomAttributes: List) -> Dict:
        pass

    def admin_add_user_to_group(self, UserPoolId: str, Username: str, GroupName: str) -> NoReturn:
        pass

    def admin_confirm_sign_up(self, UserPoolId: str, Username: str) -> Dict:
        pass

    def admin_create_user(self, UserPoolId: str, Username: str, UserAttributes: List = None, ValidationData: List = None, TemporaryPassword: str = None, ForceAliasCreation: bool = None, MessageAction: str = None, DesiredDeliveryMediums: List = None) -> Dict:
        pass

    def admin_delete_user(self, UserPoolId: str, Username: str) -> NoReturn:
        pass

    def admin_delete_user_attributes(self, UserPoolId: str, Username: str, UserAttributeNames: List) -> Dict:
        pass

    def admin_disable_provider_for_user(self, UserPoolId: str, User: Dict) -> Dict:
        pass

    def admin_disable_user(self, UserPoolId: str, Username: str) -> Dict:
        pass

    def admin_enable_user(self, UserPoolId: str, Username: str) -> Dict:
        pass

    def admin_forget_device(self, UserPoolId: str, Username: str, DeviceKey: str) -> NoReturn:
        pass

    def admin_get_device(self, DeviceKey: str, UserPoolId: str, Username: str) -> Dict:
        pass

    def admin_get_user(self, UserPoolId: str, Username: str) -> Dict:
        pass

    def admin_initiate_auth(self, UserPoolId: str, ClientId: str, AuthFlow: str, AuthParameters: Dict = None, ClientMetadata: Dict = None, AnalyticsMetadata: Dict = None, ContextData: Dict = None) -> Dict:
        pass

    def admin_link_provider_for_user(self, UserPoolId: str, DestinationUser: Dict, SourceUser: Dict) -> Dict:
        pass

    def admin_list_devices(self, UserPoolId: str, Username: str, Limit: int = None, PaginationToken: str = None) -> Dict:
        pass

    def admin_list_groups_for_user(self, Username: str, UserPoolId: str, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def admin_list_user_auth_events(self, UserPoolId: str, Username: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def admin_remove_user_from_group(self, UserPoolId: str, Username: str, GroupName: str) -> NoReturn:
        pass

    def admin_reset_user_password(self, UserPoolId: str, Username: str) -> Dict:
        pass

    def admin_respond_to_auth_challenge(self, UserPoolId: str, ClientId: str, ChallengeName: str, ChallengeResponses: Dict = None, Session: str = None, AnalyticsMetadata: Dict = None, ContextData: Dict = None) -> Dict:
        pass

    def admin_set_user_mfa_preference(self, Username: str, UserPoolId: str, SMSMfaSettings: Dict = None, SoftwareTokenMfaSettings: Dict = None) -> Dict:
        pass

    def admin_set_user_settings(self, UserPoolId: str, Username: str, MFAOptions: List) -> Dict:
        pass

    def admin_update_auth_event_feedback(self, UserPoolId: str, Username: str, EventId: str, FeedbackValue: str) -> Dict:
        pass

    def admin_update_device_status(self, UserPoolId: str, Username: str, DeviceKey: str, DeviceRememberedStatus: str = None) -> Dict:
        pass

    def admin_update_user_attributes(self, UserPoolId: str, Username: str, UserAttributes: List) -> Dict:
        pass

    def admin_user_global_sign_out(self, UserPoolId: str, Username: str) -> Dict:
        pass

    def associate_software_token(self, AccessToken: str = None, Session: str = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def change_password(self, PreviousPassword: str, ProposedPassword: str, AccessToken: str) -> Dict:
        pass

    def confirm_device(self, AccessToken: str, DeviceKey: str, DeviceSecretVerifierConfig: Dict = None, DeviceName: str = None) -> Dict:
        pass

    def confirm_forgot_password(self, ClientId: str, Username: str, ConfirmationCode: str, Password: str, SecretHash: str = None, AnalyticsMetadata: Dict = None, UserContextData: Dict = None) -> Dict:
        pass

    def confirm_sign_up(self, ClientId: str, Username: str, ConfirmationCode: str, SecretHash: str = None, ForceAliasCreation: bool = None, AnalyticsMetadata: Dict = None, UserContextData: Dict = None) -> Dict:
        pass

    def create_group(self, GroupName: str, UserPoolId: str, Description: str = None, RoleArn: str = None, Precedence: int = None) -> Dict:
        pass

    def create_identity_provider(self, UserPoolId: str, ProviderName: str, ProviderType: str, ProviderDetails: Dict, AttributeMapping: Dict = None, IdpIdentifiers: List = None) -> Dict:
        pass

    def create_resource_server(self, UserPoolId: str, Identifier: str, Name: str, Scopes: List = None) -> Dict:
        pass

    def create_user_import_job(self, JobName: str, UserPoolId: str, CloudWatchLogsRoleArn: str) -> Dict:
        pass

    def create_user_pool(self, PoolName: str, Policies: Dict = None, LambdaConfig: Dict = None, AutoVerifiedAttributes: List = None, AliasAttributes: List = None, UsernameAttributes: List = None, SmsVerificationMessage: str = None, EmailVerificationMessage: str = None, EmailVerificationSubject: str = None, VerificationMessageTemplate: Dict = None, SmsAuthenticationMessage: str = None, MfaConfiguration: str = None, DeviceConfiguration: Dict = None, EmailConfiguration: Dict = None, SmsConfiguration: Dict = None, UserPoolTags: Dict = None, AdminCreateUserConfig: Dict = None, Schema: List = None, UserPoolAddOns: Dict = None) -> Dict:
        pass

    def create_user_pool_client(self, UserPoolId: str, ClientName: str, GenerateSecret: bool = None, RefreshTokenValidity: int = None, ReadAttributes: List = None, WriteAttributes: List = None, ExplicitAuthFlows: List = None, SupportedIdentityProviders: List = None, CallbackURLs: List = None, LogoutURLs: List = None, DefaultRedirectURI: str = None, AllowedOAuthFlows: List = None, AllowedOAuthScopes: List = None, AllowedOAuthFlowsUserPoolClient: bool = None, AnalyticsConfiguration: Dict = None) -> Dict:
        pass

    def create_user_pool_domain(self, Domain: str, UserPoolId: str, CustomDomainConfig: Dict = None) -> Dict:
        pass

    def delete_group(self, GroupName: str, UserPoolId: str) -> NoReturn:
        pass

    def delete_identity_provider(self, UserPoolId: str, ProviderName: str) -> NoReturn:
        pass

    def delete_resource_server(self, UserPoolId: str, Identifier: str) -> NoReturn:
        pass

    def delete_user(self, AccessToken: str) -> NoReturn:
        pass

    def delete_user_attributes(self, UserAttributeNames: List, AccessToken: str) -> Dict:
        pass

    def delete_user_pool(self, UserPoolId: str) -> NoReturn:
        pass

    def delete_user_pool_client(self, UserPoolId: str, ClientId: str) -> NoReturn:
        pass

    def delete_user_pool_domain(self, Domain: str, UserPoolId: str) -> Dict:
        pass

    def describe_identity_provider(self, UserPoolId: str, ProviderName: str) -> Dict:
        pass

    def describe_resource_server(self, UserPoolId: str, Identifier: str) -> Dict:
        pass

    def describe_risk_configuration(self, UserPoolId: str, ClientId: str = None) -> Dict:
        pass

    def describe_user_import_job(self, UserPoolId: str, JobId: str) -> Dict:
        pass

    def describe_user_pool(self, UserPoolId: str) -> Dict:
        pass

    def describe_user_pool_client(self, UserPoolId: str, ClientId: str) -> Dict:
        pass

    def describe_user_pool_domain(self, Domain: str) -> Dict:
        pass

    def forget_device(self, DeviceKey: str, AccessToken: str = None) -> NoReturn:
        pass

    def forgot_password(self, ClientId: str, Username: str, SecretHash: str = None, UserContextData: Dict = None, AnalyticsMetadata: Dict = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_csv_header(self, UserPoolId: str) -> Dict:
        pass

    def get_device(self, DeviceKey: str, AccessToken: str = None) -> Dict:
        pass

    def get_group(self, GroupName: str, UserPoolId: str) -> Dict:
        pass

    def get_identity_provider_by_identifier(self, UserPoolId: str, IdpIdentifier: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_signing_certificate(self, UserPoolId: str) -> Dict:
        pass

    def get_ui_customization(self, UserPoolId: str, ClientId: str = None) -> Dict:
        pass

    def get_user(self, AccessToken: str) -> Dict:
        pass

    def get_user_attribute_verification_code(self, AccessToken: str, AttributeName: str) -> Dict:
        pass

    def get_user_pool_mfa_config(self, UserPoolId: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def global_sign_out(self, AccessToken: str) -> Dict:
        pass

    def initiate_auth(self, AuthFlow: str, ClientId: str, AuthParameters: Dict = None, ClientMetadata: Dict = None, AnalyticsMetadata: Dict = None, UserContextData: Dict = None) -> Dict:
        pass

    def list_devices(self, AccessToken: str, Limit: int = None, PaginationToken: str = None) -> Dict:
        pass

    def list_groups(self, UserPoolId: str, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def list_identity_providers(self, UserPoolId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_resource_servers(self, UserPoolId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_user_import_jobs(self, UserPoolId: str, MaxResults: int, PaginationToken: str = None) -> Dict:
        pass

    def list_user_pool_clients(self, UserPoolId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_user_pools(self, MaxResults: int, NextToken: str = None) -> Dict:
        pass

    def list_users(self, UserPoolId: str, AttributesToGet: List = None, Limit: int = None, PaginationToken: str = None, Filter: str = None) -> Dict:
        pass

    def list_users_in_group(self, UserPoolId: str, GroupName: str, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def resend_confirmation_code(self, ClientId: str, Username: str, SecretHash: str = None, UserContextData: Dict = None, AnalyticsMetadata: Dict = None) -> Dict:
        pass

    def respond_to_auth_challenge(self, ClientId: str, ChallengeName: str, Session: str = None, ChallengeResponses: Dict = None, AnalyticsMetadata: Dict = None, UserContextData: Dict = None) -> Dict:
        pass

    def set_risk_configuration(self, UserPoolId: str, ClientId: str = None, CompromisedCredentialsRiskConfiguration: Dict = None, AccountTakeoverRiskConfiguration: Dict = None, RiskExceptionConfiguration: Dict = None) -> Dict:
        pass

    def set_ui_customization(self, UserPoolId: str, ClientId: str = None, CSS: str = None, ImageFile: bytes = None) -> Dict:
        pass

    def set_user_mfa_preference(self, AccessToken: str, SMSMfaSettings: Dict = None, SoftwareTokenMfaSettings: Dict = None) -> Dict:
        pass

    def set_user_pool_mfa_config(self, UserPoolId: str, SmsMfaConfiguration: Dict = None, SoftwareTokenMfaConfiguration: Dict = None, MfaConfiguration: str = None) -> Dict:
        pass

    def set_user_settings(self, AccessToken: str, MFAOptions: List) -> Dict:
        pass

    def sign_up(self, ClientId: str, Username: str, Password: str, SecretHash: str = None, UserAttributes: List = None, ValidationData: List = None, AnalyticsMetadata: Dict = None, UserContextData: Dict = None) -> Dict:
        pass

    def start_user_import_job(self, UserPoolId: str, JobId: str) -> Dict:
        pass

    def stop_user_import_job(self, UserPoolId: str, JobId: str) -> Dict:
        pass

    def update_auth_event_feedback(self, UserPoolId: str, Username: str, EventId: str, FeedbackToken: str, FeedbackValue: str) -> Dict:
        pass

    def update_device_status(self, AccessToken: str, DeviceKey: str, DeviceRememberedStatus: str = None) -> Dict:
        pass

    def update_group(self, GroupName: str, UserPoolId: str, Description: str = None, RoleArn: str = None, Precedence: int = None) -> Dict:
        pass

    def update_identity_provider(self, UserPoolId: str, ProviderName: str, ProviderDetails: Dict = None, AttributeMapping: Dict = None, IdpIdentifiers: List = None) -> Dict:
        pass

    def update_resource_server(self, UserPoolId: str, Identifier: str, Name: str, Scopes: List = None) -> Dict:
        pass

    def update_user_attributes(self, UserAttributes: List, AccessToken: str) -> Dict:
        pass

    def update_user_pool(self, UserPoolId: str, Policies: Dict = None, LambdaConfig: Dict = None, AutoVerifiedAttributes: List = None, SmsVerificationMessage: str = None, EmailVerificationMessage: str = None, EmailVerificationSubject: str = None, VerificationMessageTemplate: Dict = None, SmsAuthenticationMessage: str = None, MfaConfiguration: str = None, DeviceConfiguration: Dict = None, EmailConfiguration: Dict = None, SmsConfiguration: Dict = None, UserPoolTags: Dict = None, AdminCreateUserConfig: Dict = None, UserPoolAddOns: Dict = None) -> Dict:
        pass

    def update_user_pool_client(self, UserPoolId: str, ClientId: str, ClientName: str = None, RefreshTokenValidity: int = None, ReadAttributes: List = None, WriteAttributes: List = None, ExplicitAuthFlows: List = None, SupportedIdentityProviders: List = None, CallbackURLs: List = None, LogoutURLs: List = None, DefaultRedirectURI: str = None, AllowedOAuthFlows: List = None, AllowedOAuthScopes: List = None, AllowedOAuthFlowsUserPoolClient: bool = None, AnalyticsConfiguration: Dict = None) -> Dict:
        pass

    def verify_software_token(self, UserCode: str, AccessToken: str = None, Session: str = None, FriendlyDeviceName: str = None) -> Dict:
        pass

    def verify_user_attribute(self, AccessToken: str, AttributeName: str, Code: str) -> Dict:
        pass
