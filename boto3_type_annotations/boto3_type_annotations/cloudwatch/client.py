from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from datetime import datetime
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def delete_alarms(self, AlarmNames: List):
        pass

    def delete_dashboards(self, DashboardNames: List) -> Dict:
        pass

    def describe_alarm_history(self, AlarmName: str = None, HistoryItemType: str = None, StartDate: datetime = None, EndDate: datetime = None, MaxRecords: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_alarms(self, AlarmNames: List = None, AlarmNamePrefix: str = None, StateValue: str = None, ActionPrefix: str = None, MaxRecords: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_alarms_for_metric(self, MetricName: str, Namespace: str, Statistic: str = None, ExtendedStatistic: str = None, Dimensions: List = None, Period: int = None, Unit: str = None) -> Dict:
        pass

    def disable_alarm_actions(self, AlarmNames: List):
        pass

    def enable_alarm_actions(self, AlarmNames: List):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_dashboard(self, DashboardName: str) -> Dict:
        pass

    def get_metric_data(self, MetricDataQueries: List, StartTime: datetime, EndTime: datetime, NextToken: str = None, ScanBy: str = None, MaxDatapoints: int = None) -> Dict:
        pass

    def get_metric_statistics(self, Namespace: str, MetricName: str, StartTime: datetime, EndTime: datetime, Period: int, Dimensions: List = None, Statistics: List = None, ExtendedStatistics: List = None, Unit: str = None) -> Dict:
        pass

    def get_metric_widget_image(self, MetricWidget: str, OutputFormat: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_dashboards(self, DashboardNamePrefix: str = None, NextToken: str = None) -> Dict:
        pass

    def list_metrics(self, Namespace: str = None, MetricName: str = None, Dimensions: List = None, NextToken: str = None) -> Dict:
        pass

    def list_tags_for_resource(self, ResourceARN: str) -> Dict:
        pass

    def put_dashboard(self, DashboardName: str, DashboardBody: str) -> Dict:
        pass

    def put_metric_alarm(self, AlarmName: str, EvaluationPeriods: int, Threshold: float, ComparisonOperator: str, AlarmDescription: str = None, ActionsEnabled: bool = None, OKActions: List = None, AlarmActions: List = None, InsufficientDataActions: List = None, MetricName: str = None, Namespace: str = None, Statistic: str = None, ExtendedStatistic: str = None, Dimensions: List = None, Period: int = None, Unit: str = None, DatapointsToAlarm: int = None, TreatMissingData: str = None, EvaluateLowSampleCountPercentile: str = None, Metrics: List = None, Tags: List = None):
        pass

    def put_metric_data(self, Namespace: str, MetricData: List):
        pass

    def set_alarm_state(self, AlarmName: str, StateValue: str, StateReason: str, StateReasonData: str = None):
        pass

    def tag_resource(self, ResourceARN: str, Tags: List) -> Dict:
        pass

    def untag_resource(self, ResourceARN: str, TagKeys: List) -> Dict:
        pass
