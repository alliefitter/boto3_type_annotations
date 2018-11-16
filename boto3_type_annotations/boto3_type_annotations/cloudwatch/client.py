from datetime import datetime
from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def delete_alarms(self, AlarmNames: List) -> NoReturn:
        pass

    def delete_dashboards(self, DashboardNames: List) -> Dict:
        pass

    def describe_alarm_history(self, AlarmName: str = None, HistoryItemType: str = None, StartDate: datetime = None, EndDate: datetime = None, MaxRecords: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_alarms(self, AlarmNames: List = None, AlarmNamePrefix: str = None, StateValue: str = None, ActionPrefix: str = None, MaxRecords: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_alarms_for_metric(self, MetricName: str, Namespace: str, Statistic: str = None, ExtendedStatistic: str = None, Dimensions: List = None, Period: int = None, Unit: str = None) -> Dict:
        pass

    def disable_alarm_actions(self, AlarmNames: List) -> NoReturn:
        pass

    def enable_alarm_actions(self, AlarmNames: List) -> NoReturn:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
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

    def put_dashboard(self, DashboardName: str, DashboardBody: str) -> Dict:
        pass

    def put_metric_alarm(self, AlarmName: str, MetricName: str, Namespace: str, Period: int, EvaluationPeriods: int, Threshold: float, ComparisonOperator: str, AlarmDescription: str = None, ActionsEnabled: bool = None, OKActions: List = None, AlarmActions: List = None, InsufficientDataActions: List = None, Statistic: str = None, ExtendedStatistic: str = None, Dimensions: List = None, Unit: str = None, DatapointsToAlarm: int = None, TreatMissingData: str = None, EvaluateLowSampleCountPercentile: str = None) -> NoReturn:
        pass

    def put_metric_data(self, Namespace: str, MetricData: List) -> NoReturn:
        pass

    def set_alarm_state(self, AlarmName: str, StateValue: str, StateReason: str, StateReasonData: str = None) -> NoReturn:
        pass
