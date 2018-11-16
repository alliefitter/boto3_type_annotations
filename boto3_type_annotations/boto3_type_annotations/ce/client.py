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

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_cost_and_usage(self, TimePeriod: Dict = None, Granularity: str = None, Filter: Dict = None, Metrics: List = None, GroupBy: List = None, NextPageToken: str = None) -> Dict:
        pass

    def get_dimension_values(self, TimePeriod: Dict, Dimension: str, SearchString: str = None, Context: str = None, NextPageToken: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_reservation_coverage(self, TimePeriod: Dict, GroupBy: List = None, Granularity: str = None, Filter: Dict = None, NextPageToken: str = None) -> Dict:
        pass

    def get_reservation_purchase_recommendation(self, Service: str, AccountId: str = None, AccountScope: str = None, LookbackPeriodInDays: str = None, TermInYears: str = None, PaymentOption: str = None, ServiceSpecification: Dict = None, PageSize: int = None, NextPageToken: str = None) -> Dict:
        pass

    def get_reservation_utilization(self, TimePeriod: Dict, GroupBy: List = None, Granularity: str = None, Filter: Dict = None, NextPageToken: str = None) -> Dict:
        pass

    def get_tags(self, TimePeriod: Dict, SearchString: str = None, TagKey: str = None, NextPageToken: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass
