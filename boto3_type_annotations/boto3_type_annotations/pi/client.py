from datetime import datetime
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

    def describe_dimension_keys(self, ServiceType: str, Identifier: str, StartTime: datetime, EndTime: datetime, Metric: str, GroupBy: Dict, PeriodInSeconds: int = None, PartitionBy: Dict = None, Filter: Dict = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_resource_metrics(self, ServiceType: str, Identifier: str, MetricQueries: List, StartTime: datetime, EndTime: datetime, PeriodInSeconds: int = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass
