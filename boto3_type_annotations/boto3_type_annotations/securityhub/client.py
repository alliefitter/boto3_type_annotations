from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def accept_invitation(self, MasterId: str = None, InvitationId: str = None) -> Dict:
        pass

    def batch_disable_standards(self, StandardsSubscriptionArns: List) -> Dict:
        pass

    def batch_enable_standards(self, StandardsSubscriptionRequests: List) -> Dict:
        pass

    def batch_import_findings(self, Findings: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_insight(self, Name: str, Filters: Dict, GroupByAttribute: str) -> Dict:
        pass

    def create_members(self, AccountDetails: List = None) -> Dict:
        pass

    def decline_invitations(self, AccountIds: List = None) -> Dict:
        pass

    def delete_insight(self, InsightArn: str) -> Dict:
        pass

    def delete_invitations(self, AccountIds: List = None) -> Dict:
        pass

    def delete_members(self, AccountIds: List = None) -> Dict:
        pass

    def disable_import_findings_for_product(self, ProductSubscriptionArn: str) -> Dict:
        pass

    def disable_security_hub(self) -> Dict:
        pass

    def disassociate_from_master_account(self) -> Dict:
        pass

    def disassociate_members(self, AccountIds: List = None) -> Dict:
        pass

    def enable_import_findings_for_product(self, ProductArn: str) -> Dict:
        pass

    def enable_security_hub(self) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_enabled_standards(self, StandardsSubscriptionArns: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def get_findings(self, Filters: Dict = None, SortCriteria: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def get_insight_results(self, InsightArn: str) -> Dict:
        pass

    def get_insights(self, InsightArns: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def get_invitations_count(self) -> Dict:
        pass

    def get_master_account(self) -> Dict:
        pass

    def get_members(self, AccountIds: List) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def invite_members(self, AccountIds: List = None) -> Dict:
        pass

    def list_enabled_products_for_import(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_invitations(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_members(self, OnlyAssociated: bool = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def update_findings(self, Filters: Dict, Note: Dict = None, RecordState: str = None) -> Dict:
        pass

    def update_insight(self, InsightArn: str, Name: str = None, Filters: Dict = None, GroupByAttribute: str = None) -> Dict:
        pass
