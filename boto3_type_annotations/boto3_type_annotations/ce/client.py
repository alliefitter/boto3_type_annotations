from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_cost_and_usage(self, TimePeriod: Dict, Granularity: str = None, Filter: Dict = None, Metrics: List = None, GroupBy: List = None, NextPageToken: str = None) -> Dict:
        pass

    def get_cost_forecast(self, TimePeriod: Dict, Metric: str, Granularity: str, Filter: Dict = None, PredictionIntervalLevel: int = None) -> Dict:
        pass

    def get_dimension_values(self, TimePeriod: Dict, Dimension: str, SearchString: str = None, Context: str = None, NextPageToken: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_reservation_coverage(self, TimePeriod: Dict, GroupBy: List = None, Granularity: str = None, Filter: Dict = None, Metrics: List = None, NextPageToken: str = None) -> Dict:
        pass

    def get_reservation_purchase_recommendation(self, Service: str, AccountId: str = None, AccountScope: str = None, LookbackPeriodInDays: str = None, TermInYears: str = None, PaymentOption: str = None, ServiceSpecification: Dict = None, PageSize: int = None, NextPageToken: str = None) -> Dict:
        pass

    def get_reservation_utilization(self, TimePeriod: Dict, GroupBy: List = None, Granularity: str = None, Filter: Dict = None, NextPageToken: str = None) -> Dict:
        pass

    def get_tags(self, TimePeriod: Dict, SearchString: str = None, TagKey: str = None, NextPageToken: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass
