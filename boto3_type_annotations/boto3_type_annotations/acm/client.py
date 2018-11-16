from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def add_tags_to_certificate(self, CertificateArn: str, Tags: List) -> NoReturn:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def delete_certificate(self, CertificateArn: str) -> NoReturn:
        pass

    def describe_certificate(self, CertificateArn: str) -> Dict:
        pass

    def export_certificate(self, CertificateArn: str, Passphrase: bytes) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_certificate(self, CertificateArn: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def import_certificate(self, Certificate: bytes, PrivateKey: bytes, CertificateArn: str = None, CertificateChain: bytes = None) -> Dict:
        pass

    def list_certificates(self, CertificateStatuses: List = None, Includes: Dict = None, NextToken: str = None, MaxItems: int = None) -> Dict:
        pass

    def list_tags_for_certificate(self, CertificateArn: str) -> Dict:
        pass

    def remove_tags_from_certificate(self, CertificateArn: str, Tags: List) -> NoReturn:
        pass

    def request_certificate(self, DomainName: str, ValidationMethod: str = None, SubjectAlternativeNames: List = None, IdempotencyToken: str = None, DomainValidationOptions: List = None, Options: Dict = None, CertificateAuthorityArn: str = None) -> Dict:
        pass

    def resend_validation_email(self, CertificateArn: str, Domain: str, ValidationDomain: str) -> NoReturn:
        pass

    def update_certificate_options(self, CertificateArn: str, Options: Dict) -> NoReturn:
        pass
