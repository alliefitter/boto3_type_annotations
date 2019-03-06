from typing import Dict
from botocore.waiter import Waiter


class AuditReportCreated(Waiter):
    def wait(self, CertificateAuthorityArn: str, AuditReportId: str, WaiterConfig: Dict = None):
        pass


class CertificateAuthorityCSRCreated(Waiter):
    def wait(self, CertificateAuthorityArn: str, WaiterConfig: Dict = None):
        pass


class CertificateIssued(Waiter):
    def wait(self, CertificateAuthorityArn: str, CertificateArn: str, WaiterConfig: Dict = None):
        pass
