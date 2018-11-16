from typing import Optional
from typing import Union
from typing import List
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_certificate_authority(self, CertificateAuthorityConfiguration: Dict, CertificateAuthorityType: str, RevocationConfiguration: Dict = None, IdempotencyToken: str = None) -> Dict:
        pass

    def create_certificate_authority_audit_report(self, CertificateAuthorityArn: str, S3BucketName: str, AuditReportResponseFormat: str) -> Dict:
        pass

    def delete_certificate_authority(self, CertificateAuthorityArn: str, PermanentDeletionTimeInDays: int = None):
        pass

    def describe_certificate_authority(self, CertificateAuthorityArn: str) -> Dict:
        pass

    def describe_certificate_authority_audit_report(self, CertificateAuthorityArn: str, AuditReportId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_certificate(self, CertificateAuthorityArn: str, CertificateArn: str) -> Dict:
        pass

    def get_certificate_authority_certificate(self, CertificateAuthorityArn: str) -> Dict:
        pass

    def get_certificate_authority_csr(self, CertificateAuthorityArn: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def import_certificate_authority_certificate(self, CertificateAuthorityArn: str, Certificate: bytes, CertificateChain: bytes):
        pass

    def issue_certificate(self, CertificateAuthorityArn: str, Csr: bytes, SigningAlgorithm: str, Validity: Dict, IdempotencyToken: str = None) -> Dict:
        pass

    def list_certificate_authorities(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_tags(self, CertificateAuthorityArn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def restore_certificate_authority(self, CertificateAuthorityArn: str):
        pass

    def revoke_certificate(self, CertificateAuthorityArn: str, CertificateSerial: str, RevocationReason: str):
        pass

    def tag_certificate_authority(self, CertificateAuthorityArn: str, Tags: List):
        pass

    def untag_certificate_authority(self, CertificateAuthorityArn: str, Tags: List):
        pass

    def update_certificate_authority(self, CertificateAuthorityArn: str, RevocationConfiguration: Dict = None, Status: str = None):
        pass
