from typing import Optional
from typing import Union
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def cancel_signing_profile(self, profileName: str):
        pass

    def describe_signing_job(self, jobId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_signing_platform(self, platformId: str) -> Dict:
        pass

    def get_signing_profile(self, profileName: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_signing_jobs(self, status: str = None, platformId: str = None, requestedBy: str = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def list_signing_platforms(self, category: str = None, partner: str = None, target: str = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def list_signing_profiles(self, includeCanceled: bool = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def put_signing_profile(self, profileName: str, signingMaterial: Dict, platformId: str, overrides: Dict = None, signingParameters: Dict = None) -> Dict:
        pass

    def start_signing_job(self, source: Dict, destination: Dict, clientRequestToken: str, profileName: str = None) -> Dict:
        pass
