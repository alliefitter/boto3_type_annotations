from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def accept_invitation(self, DetectorId: str, InvitationId: str, MasterId: str) -> Dict:
        pass

    def archive_findings(self, DetectorId: str, FindingIds: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_detector(self, Enable: bool, ClientToken: str = None, FindingPublishingFrequency: str = None) -> Dict:
        pass

    def create_filter(self, DetectorId: str, FindingCriteria: Dict, Name: str, Action: str = None, ClientToken: str = None, Description: str = None, Rank: int = None) -> Dict:
        pass

    def create_ip_set(self, Activate: bool, DetectorId: str, Format: str, Location: str, Name: str, ClientToken: str = None) -> Dict:
        pass

    def create_members(self, AccountDetails: List, DetectorId: str) -> Dict:
        pass

    def create_sample_findings(self, DetectorId: str, FindingTypes: List = None) -> Dict:
        pass

    def create_threat_intel_set(self, Activate: bool, DetectorId: str, Format: str, Location: str, Name: str, ClientToken: str = None) -> Dict:
        pass

    def decline_invitations(self, AccountIds: List) -> Dict:
        pass

    def delete_detector(self, DetectorId: str) -> Dict:
        pass

    def delete_filter(self, DetectorId: str, FilterName: str) -> Dict:
        pass

    def delete_invitations(self, AccountIds: List) -> Dict:
        pass

    def delete_ip_set(self, DetectorId: str, IpSetId: str) -> Dict:
        pass

    def delete_members(self, AccountIds: List, DetectorId: str) -> Dict:
        pass

    def delete_threat_intel_set(self, DetectorId: str, ThreatIntelSetId: str) -> Dict:
        pass

    def disassociate_from_master_account(self, DetectorId: str) -> Dict:
        pass

    def disassociate_members(self, AccountIds: List, DetectorId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_detector(self, DetectorId: str) -> Dict:
        pass

    def get_filter(self, DetectorId: str, FilterName: str) -> Dict:
        pass

    def get_findings(self, DetectorId: str, FindingIds: List, SortCriteria: Dict = None) -> Dict:
        pass

    def get_findings_statistics(self, DetectorId: str, FindingStatisticTypes: List, FindingCriteria: Dict = None) -> Dict:
        pass

    def get_invitations_count(self) -> Dict:
        pass

    def get_ip_set(self, DetectorId: str, IpSetId: str) -> Dict:
        pass

    def get_master_account(self, DetectorId: str) -> Dict:
        pass

    def get_members(self, AccountIds: List, DetectorId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_threat_intel_set(self, DetectorId: str, ThreatIntelSetId: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def invite_members(self, AccountIds: List, DetectorId: str, DisableEmailNotification: bool = None, Message: str = None) -> Dict:
        pass

    def list_detectors(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_filters(self, DetectorId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_findings(self, DetectorId: str, FindingCriteria: Dict = None, MaxResults: int = None, NextToken: str = None, SortCriteria: Dict = None) -> Dict:
        pass

    def list_invitations(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_ip_sets(self, DetectorId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_members(self, DetectorId: str, MaxResults: int = None, NextToken: str = None, OnlyAssociated: str = None) -> Dict:
        pass

    def list_threat_intel_sets(self, DetectorId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def start_monitoring_members(self, AccountIds: List, DetectorId: str) -> Dict:
        pass

    def stop_monitoring_members(self, AccountIds: List, DetectorId: str) -> Dict:
        pass

    def unarchive_findings(self, DetectorId: str, FindingIds: List) -> Dict:
        pass

    def update_detector(self, DetectorId: str, Enable: bool = None, FindingPublishingFrequency: str = None) -> Dict:
        pass

    def update_filter(self, DetectorId: str, FilterName: str, Action: str = None, Description: str = None, FindingCriteria: Dict = None, Rank: int = None) -> Dict:
        pass

    def update_findings_feedback(self, DetectorId: str, Feedback: str, FindingIds: List, Comments: str = None) -> Dict:
        pass

    def update_ip_set(self, DetectorId: str, IpSetId: str, Activate: bool = None, Location: str = None, Name: str = None) -> Dict:
        pass

    def update_threat_intel_set(self, DetectorId: str, ThreatIntelSetId: str, Activate: bool = None, Location: str = None, Name: str = None) -> Dict:
        pass
