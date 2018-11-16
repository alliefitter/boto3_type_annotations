from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def batch_get_traces(self, TraceIds: List, NextToken: str = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_sampling_rule(self, SamplingRule: Dict) -> Dict:
        pass

    def delete_sampling_rule(self, RuleName: str = None, RuleARN: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_encryption_config(self) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_sampling_rules(self, NextToken: str = None) -> Dict:
        pass

    def get_sampling_statistic_summaries(self, NextToken: str = None) -> Dict:
        pass

    def get_sampling_targets(self, SamplingStatisticsDocuments: List) -> Dict:
        pass

    def get_service_graph(self, StartTime: datetime, EndTime: datetime, NextToken: str = None) -> Dict:
        pass

    def get_trace_graph(self, TraceIds: List, NextToken: str = None) -> Dict:
        pass

    def get_trace_summaries(self, StartTime: datetime, EndTime: datetime, Sampling: bool = None, FilterExpression: str = None, NextToken: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def put_encryption_config(self, Type: str, KeyId: str = None) -> Dict:
        pass

    def put_telemetry_records(self, TelemetryRecords: List, EC2InstanceId: str = None, Hostname: str = None, ResourceARN: str = None) -> Dict:
        pass

    def put_trace_segments(self, TraceSegmentDocuments: List) -> Dict:
        pass

    def update_sampling_rule(self, SamplingRuleUpdate: Dict) -> Dict:
        pass
