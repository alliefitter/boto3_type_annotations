from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def cancel_job(self, JobId: str, APIVersion: str = None) -> Dict:
        pass

    def create_job(self, JobType: str, Manifest: str, ValidateOnly: bool, ManifestAddendum: str = None, APIVersion: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_shipping_label(self, jobIds: List, name: str = None, company: str = None, phoneNumber: str = None, country: str = None, stateOrProvince: str = None, city: str = None, postalCode: str = None, street1: str = None, street2: str = None, street3: str = None, APIVersion: str = None) -> Dict:
        pass

    def get_status(self, JobId: str, APIVersion: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_jobs(self, MaxJobs: int = None, Marker: str = None, APIVersion: str = None) -> Dict:
        pass

    def update_job(self, JobId: str, Manifest: str, JobType: str, ValidateOnly: bool, APIVersion: str = None) -> Dict:
        pass
