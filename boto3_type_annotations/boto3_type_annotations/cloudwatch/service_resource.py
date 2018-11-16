from typing import Optional
from typing import Union
from boto3.resources.collection import ResourceCollection
from typing import List
from datetime import datetime
from typing import Dict
from boto3.resources import base


class ServiceResource(base.ServiceResource):
    alarms: 'alarms'
    metrics: 'metrics'

    def Alarm(self, name: str = None) -> 'Alarm':
        pass

    def Metric(self, namespace: str = None, name: str = None) -> 'Metric':
        pass

    def get_available_subresources(self) -> List[str]:
        pass


class Alarm(base.ServiceResource):
    alarm_name: str
    alarm_arn: str
    alarm_description: str
    alarm_configuration_updated_timestamp: datetime
    actions_enabled: bool
    ok_actions: List
    alarm_actions: List
    insufficient_data_actions: List
    state_value: str
    state_reason: str
    state_reason_data: str
    state_updated_timestamp: datetime
    metric_name: str
    namespace: str
    statistic: str
    extended_statistic: str
    dimensions: List
    period: int
    unit: str
    evaluation_periods: int
    datapoints_to_alarm: int
    threshold: float
    comparison_operator: str
    treat_missing_data: str
    evaluate_low_sample_count_percentile: str
    name: str

    def delete(self):
        pass

    def describe_history(self, HistoryItemType: str = None, StartDate: datetime = None, EndDate: datetime = None, MaxRecords: int = None, NextToken: str = None) -> Dict:
        pass

    def disable_actions(self):
        pass

    def enable_actions(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass

    def set_state(self, StateValue: str, StateReason: str, StateReasonData: str = None):
        pass


class Metric(base.ServiceResource):
    metric_name: str
    dimensions: List
    namespace: str
    name: str
    alarms: 'alarms'

    def get_available_subresources(self) -> List[str]:
        pass

    def get_statistics(self, StartTime: datetime, EndTime: datetime, Period: int, Dimensions: List = None, Statistics: List = None, ExtendedStatistics: List = None, Unit: str = None) -> Dict:
        pass

    def load(self):
        pass

    def put_alarm(self, AlarmName: str, Period: int, EvaluationPeriods: int, Threshold: float, ComparisonOperator: str, AlarmDescription: str = None, ActionsEnabled: bool = None, OKActions: List = None, AlarmActions: List = None, InsufficientDataActions: List = None, Statistic: str = None, ExtendedStatistic: str = None, Dimensions: List = None, Unit: str = None, DatapointsToAlarm: int = None, TreatMissingData: str = None, EvaluateLowSampleCountPercentile: str = None) -> 'Alarm':
        pass

    def put_data(self):
        pass

    def reload(self):
        pass


class alarms(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Alarm']:
        pass

    
    @classmethod
    def delete(cls):
        pass

    
    @classmethod
    def disable_actions(cls):
        pass

    
    @classmethod
    def enable_actions(cls):
        pass

    
    @classmethod
    def filter(cls, AlarmNames: List = None, AlarmNamePrefix: str = None, StateValue: str = None, ActionPrefix: str = None, MaxRecords: int = None, NextToken: str = None) -> List['Alarm']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Alarm']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Alarm']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class metrics(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Metric']:
        pass

    
    @classmethod
    def filter(cls, Namespace: str = None, MetricName: str = None, Dimensions: List = None, NextToken: str = None) -> List['Metric']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Metric']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Metric']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass
