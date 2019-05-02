from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def associate_domain(self, FleetArn: str, DomainName: str, AcmCertificateArn: str, DisplayName: str = None) -> Dict:
        pass

    def associate_website_certificate_authority(self, FleetArn: str, Certificate: str, DisplayName: str = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_fleet(self, FleetName: str, DisplayName: str = None, OptimizeForEndUserLocation: bool = None) -> Dict:
        pass

    def delete_fleet(self, FleetArn: str) -> Dict:
        pass

    def describe_audit_stream_configuration(self, FleetArn: str) -> Dict:
        pass

    def describe_company_network_configuration(self, FleetArn: str) -> Dict:
        pass

    def describe_device(self, FleetArn: str, DeviceId: str) -> Dict:
        pass

    def describe_device_policy_configuration(self, FleetArn: str) -> Dict:
        pass

    def describe_domain(self, FleetArn: str, DomainName: str) -> Dict:
        pass

    def describe_fleet_metadata(self, FleetArn: str) -> Dict:
        pass

    def describe_identity_provider_configuration(self, FleetArn: str) -> Dict:
        pass

    def describe_website_certificate_authority(self, FleetArn: str, WebsiteCaId: str) -> Dict:
        pass

    def disassociate_domain(self, FleetArn: str, DomainName: str) -> Dict:
        pass

    def disassociate_website_certificate_authority(self, FleetArn: str, WebsiteCaId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_devices(self, FleetArn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_domains(self, FleetArn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_fleets(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_website_certificate_authorities(self, FleetArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def restore_domain_access(self, FleetArn: str, DomainName: str) -> Dict:
        pass

    def revoke_domain_access(self, FleetArn: str, DomainName: str) -> Dict:
        pass

    def sign_out_user(self, FleetArn: str, Username: str) -> Dict:
        pass

    def update_audit_stream_configuration(self, FleetArn: str, AuditStreamArn: str = None) -> Dict:
        pass

    def update_company_network_configuration(self, FleetArn: str, VpcId: str, SubnetIds: List, SecurityGroupIds: List) -> Dict:
        pass

    def update_device_policy_configuration(self, FleetArn: str, DeviceCaCertificate: str = None) -> Dict:
        pass

    def update_domain_metadata(self, FleetArn: str, DomainName: str, DisplayName: str = None) -> Dict:
        pass

    def update_fleet_metadata(self, FleetArn: str, DisplayName: str = None, OptimizeForEndUserLocation: bool = None) -> Dict:
        pass

    def update_identity_provider_configuration(self, FleetArn: str, IdentityProviderType: str, IdentityProviderSamlMetadata: str = None) -> Dict:
        pass
