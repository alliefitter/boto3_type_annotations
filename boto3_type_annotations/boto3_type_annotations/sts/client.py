from typing import Optional
from typing import Union
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def assume_role(self, RoleArn: str, RoleSessionName: str, Policy: str = None, DurationSeconds: int = None, ExternalId: str = None, SerialNumber: str = None, TokenCode: str = None) -> Dict:
        pass

    def assume_role_with_saml(self, RoleArn: str, PrincipalArn: str, SAMLAssertion: str, Policy: str = None, DurationSeconds: int = None) -> Dict:
        pass

    def assume_role_with_web_identity(self, RoleArn: str, RoleSessionName: str, WebIdentityToken: str, ProviderId: str = None, Policy: str = None, DurationSeconds: int = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def decode_authorization_message(self, EncodedMessage: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_caller_identity(self) -> Dict:
        pass

    def get_federation_token(self, Name: str, Policy: str = None, DurationSeconds: int = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_session_token(self, DurationSeconds: int = None, SerialNumber: str = None, TokenCode: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass
