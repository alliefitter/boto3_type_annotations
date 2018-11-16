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

    def check_domain_availability(self, DomainName: str, IdnLangCode: str = None) -> Dict:
        pass

    def check_domain_transferability(self, DomainName: str, AuthCode: str = None) -> Dict:
        pass

    def delete_tags_for_domain(self, DomainName: str, TagsToDelete: List) -> Dict:
        pass

    def disable_domain_auto_renew(self, DomainName: str) -> Dict:
        pass

    def disable_domain_transfer_lock(self, DomainName: str) -> Dict:
        pass

    def enable_domain_auto_renew(self, DomainName: str) -> Dict:
        pass

    def enable_domain_transfer_lock(self, DomainName: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_contact_reachability_status(self, domainName: str = None) -> Dict:
        pass

    def get_domain_detail(self, DomainName: str) -> Dict:
        pass

    def get_domain_suggestions(self, DomainName: str, SuggestionCount: int, OnlyAvailable: bool) -> Dict:
        pass

    def get_operation_detail(self, OperationId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_domains(self, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    def list_operations(self, SubmittedSince: datetime = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    def list_tags_for_domain(self, DomainName: str) -> Dict:
        pass

    def register_domain(self, DomainName: str, DurationInYears: int, AdminContact: Dict, RegistrantContact: Dict, TechContact: Dict, IdnLangCode: str = None, AutoRenew: bool = None, PrivacyProtectAdminContact: bool = None, PrivacyProtectRegistrantContact: bool = None, PrivacyProtectTechContact: bool = None) -> Dict:
        pass

    def renew_domain(self, DomainName: str, CurrentExpiryYear: int, DurationInYears: int = None) -> Dict:
        pass

    def resend_contact_reachability_email(self, domainName: str = None) -> Dict:
        pass

    def retrieve_domain_auth_code(self, DomainName: str) -> Dict:
        pass

    def transfer_domain(self, DomainName: str, DurationInYears: int, AdminContact: Dict, RegistrantContact: Dict, TechContact: Dict, IdnLangCode: str = None, Nameservers: List = None, AuthCode: str = None, AutoRenew: bool = None, PrivacyProtectAdminContact: bool = None, PrivacyProtectRegistrantContact: bool = None, PrivacyProtectTechContact: bool = None) -> Dict:
        pass

    def update_domain_contact(self, DomainName: str, AdminContact: Dict = None, RegistrantContact: Dict = None, TechContact: Dict = None) -> Dict:
        pass

    def update_domain_contact_privacy(self, DomainName: str, AdminPrivacy: bool = None, RegistrantPrivacy: bool = None, TechPrivacy: bool = None) -> Dict:
        pass

    def update_domain_nameservers(self, DomainName: str, Nameservers: List, FIAuthKey: str = None) -> Dict:
        pass

    def update_tags_for_domain(self, DomainName: str, TagsToUpdate: List = None) -> Dict:
        pass

    def view_billing(self, Start: datetime = None, End: datetime = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass
