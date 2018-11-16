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

    def cancel_job(self, Id: str) -> Dict:
        pass

    def create_job(self, Role: str, Settings: Dict, BillingTagsSource: str = None, ClientRequestToken: str = None, JobTemplate: str = None, Queue: str = None, UserMetadata: Dict = None) -> Dict:
        pass

    def create_job_template(self, Name: str, Settings: Dict, Category: str = None, Description: str = None, Queue: str = None, Tags: Dict = None) -> Dict:
        pass

    def create_preset(self, Name: str, Settings: Dict, Category: str = None, Description: str = None, Tags: Dict = None) -> Dict:
        pass

    def create_queue(self, Name: str, Description: str = None, PricingPlan: str = None, ReservationPlanSettings: Dict = None, Tags: Dict = None) -> Dict:
        pass

    def delete_job_template(self, Name: str) -> Dict:
        pass

    def delete_preset(self, Name: str) -> Dict:
        pass

    def delete_queue(self, Name: str) -> Dict:
        pass

    def describe_endpoints(self, MaxResults: int = None, Mode: str = None, NextToken: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_job(self, Id: str) -> Dict:
        pass

    def get_job_template(self, Name: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_preset(self, Name: str) -> Dict:
        pass

    def get_queue(self, Name: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_job_templates(self, Category: str = None, ListBy: str = None, MaxResults: int = None, NextToken: str = None, Order: str = None) -> Dict:
        pass

    def list_jobs(self, MaxResults: int = None, NextToken: str = None, Order: str = None, Queue: str = None, Status: str = None) -> Dict:
        pass

    def list_presets(self, Category: str = None, ListBy: str = None, MaxResults: int = None, NextToken: str = None, Order: str = None) -> Dict:
        pass

    def list_queues(self, ListBy: str = None, MaxResults: int = None, NextToken: str = None, Order: str = None) -> Dict:
        pass

    def list_tags_for_resource(self, Arn: str) -> Dict:
        pass

    def tag_resource(self, Arn: str, Tags: Dict) -> Dict:
        pass

    def untag_resource(self, Arn: str, TagKeys: List = None) -> Dict:
        pass

    def update_job_template(self, Name: str, Category: str = None, Description: str = None, Queue: str = None, Settings: Dict = None) -> Dict:
        pass

    def update_preset(self, Name: str, Category: str = None, Description: str = None, Settings: Dict = None) -> Dict:
        pass

    def update_queue(self, Name: str, Description: str = None, ReservationPlanSettings: Dict = None, Status: str = None) -> Dict:
        pass
