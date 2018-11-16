from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def add_attachments_to_set(self, attachments: List, attachmentSetId: str = None) -> Dict:
        pass

    def add_communication_to_case(self, communicationBody: str, caseId: str = None, ccEmailAddresses: List = None, attachmentSetId: str = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_case(self, subject: str, communicationBody: str, serviceCode: str = None, severityCode: str = None, categoryCode: str = None, ccEmailAddresses: List = None, language: str = None, issueType: str = None, attachmentSetId: str = None) -> Dict:
        pass

    def describe_attachment(self, attachmentId: str) -> Dict:
        pass

    def describe_cases(self, caseIdList: List = None, displayId: str = None, afterTime: str = None, beforeTime: str = None, includeResolvedCases: bool = None, nextToken: str = None, maxResults: int = None, language: str = None, includeCommunications: bool = None) -> Dict:
        pass

    def describe_communications(self, caseId: str, beforeTime: str = None, afterTime: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def describe_services(self, serviceCodeList: List = None, language: str = None) -> Dict:
        pass

    def describe_severity_levels(self, language: str = None) -> Dict:
        pass

    def describe_trusted_advisor_check_refresh_statuses(self, checkIds: List) -> Dict:
        pass

    def describe_trusted_advisor_check_result(self, checkId: str, language: str = None) -> Dict:
        pass

    def describe_trusted_advisor_check_summaries(self, checkIds: List) -> Dict:
        pass

    def describe_trusted_advisor_checks(self, language: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def refresh_trusted_advisor_check(self, checkId: str) -> Dict:
        pass

    def resolve_case(self, caseId: str = None) -> Dict:
        pass
