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
        """
        Creates a Alarm resource.::
        
          alarm = cloudwatch.Alarm(\'name\')
        
        :type name: string
        :param name: The Alarm\'s name identifier. This **must** be set.
        
        :rtype: :py:class:`CloudWatch.Alarm`
        :returns: A Alarm resource
        """
        pass

    def Metric(self, namespace: str = None, name: str = None) -> 'Metric':
        """
        Creates a Metric resource.::
        
          metric = cloudwatch.Metric(\'namespace\',\'name\')
        
        :type namespace: string
        :param namespace: The Metric\'s namespace identifier. This **must** be set.
        :type name: string
        :param name: The Metric\'s name identifier. This **must** be set.
        
        :rtype: :py:class:`CloudWatch.Metric`
        :returns: A Metric resource
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
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
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DeleteAlarms>`_
        
        **Request Syntax** 
        ::
        
          response = alarm.delete()
          
        :returns: None
        """
        pass

    def describe_history(self, HistoryItemType: str = None, StartDate: datetime = None, EndDate: datetime = None, MaxRecords: int = None, NextToken: str = None) -> Dict:
        """
        
        CloudWatch retains the history of an alarm even if you delete the alarm.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarmHistory>`_
        
        **Request Syntax** 
        ::
        
          response = alarm.describe_history(
              HistoryItemType=\'ConfigurationUpdate\'|\'StateUpdate\'|\'Action\',
              StartDate=datetime(2015, 1, 1),
              EndDate=datetime(2015, 1, 1),
              MaxRecords=123,
              NextToken=\'string\'
          )
        :type HistoryItemType: string
        :param HistoryItemType: 
        
          The type of alarm histories to retrieve.
        
        :type StartDate: datetime
        :param StartDate: 
        
          The starting date to retrieve alarm history.
        
        :type EndDate: datetime
        :param EndDate: 
        
          The ending date to retrieve alarm history.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of alarm history records to retrieve.
        
        :type NextToken: string
        :param NextToken: 
        
          The token returned by a previous call to indicate that there is more data available.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AlarmHistoryItems\': [
                    {
                        \'AlarmName\': \'string\',
                        \'Timestamp\': datetime(2015, 1, 1),
                        \'HistoryItemType\': \'ConfigurationUpdate\'|\'StateUpdate\'|\'Action\',
                        \'HistorySummary\': \'string\',
                        \'HistoryData\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AlarmHistoryItems** *(list) --* 
        
              The alarm histories, in JSON format.
        
              - *(dict) --* 
        
                Represents the history of a specific alarm.
        
                - **AlarmName** *(string) --* 
        
                  The descriptive name for the alarm.
        
                - **Timestamp** *(datetime) --* 
        
                  The time stamp for the alarm history item.
        
                - **HistoryItemType** *(string) --* 
        
                  The type of alarm history item.
        
                - **HistorySummary** *(string) --* 
        
                  A summary of the alarm history, in text format.
        
                - **HistoryData** *(string) --* 
        
                  Data about the alarm, in JSON format.
        
            - **NextToken** *(string) --* 
        
              The token that marks the start of the next batch of returned results.
        
        """
        pass

    def disable_actions(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DisableAlarmActions>`_
        
        **Request Syntax** 
        ::
        
          response = alarm.disable_actions()
          
        :returns: None
        """
        pass

    def enable_actions(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/EnableAlarmActions>`_
        
        **Request Syntax** 
        ::
        
          response = alarm.enable_actions()
          
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          alarm.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          alarm.load()
        :returns: None
        """
        pass

    def set_state(self, StateValue: str, StateReason: str, StateReasonData: str = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/SetAlarmState>`_
        
        **Request Syntax** 
        ::
        
          response = alarm.set_state(
              StateValue=\'OK\'|\'ALARM\'|\'INSUFFICIENT_DATA\',
              StateReason=\'string\',
              StateReasonData=\'string\'
          )
        :type StateValue: string
        :param StateValue: **[REQUIRED]** 
        
          The value of the state.
        
        :type StateReason: string
        :param StateReason: **[REQUIRED]** 
        
          The reason that this alarm is set to this specific state, in text format.
        
        :type StateReasonData: string
        :param StateReasonData: 
        
          The reason that this alarm is set to this specific state, in JSON format.
        
        :returns: None
        """
        pass


class Metric(base.ServiceResource):
    metric_name: str
    dimensions: List
    namespace: str
    name: str
    alarms: 'alarms'

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def get_statistics(self, StartTime: datetime, EndTime: datetime, Period: int, Dimensions: List = None, Statistics: List = None, ExtendedStatistics: List = None, Unit: str = None) -> Dict:
        """
        
        The maximum number of data points returned from a single call is 1,440. If you request more than 1,440 data points, CloudWatch returns an error. To reduce the number of data points, you can narrow the specified time range and make multiple requests across adjacent time ranges, or you can increase the specified period. Data points are not returned in chronological order.
        
        CloudWatch aggregates data points based on the length of the period that you specify. For example, if you request statistics with a one-hour period, CloudWatch aggregates all data points with time stamps that fall within each one-hour period. Therefore, the number of values aggregated by CloudWatch is larger than the number of data points returned.
        
        CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:
        
        * The SampleCount value of the statistic set is 1. 
         
        * The Min and the Max values of the statistic set are equal. 
         
        Percentile statistics are not available for metrics when any of the metric values are negative numbers.
        
        Amazon CloudWatch retains metric data as follows:
        
        * Data points with a period of less than 60 seconds are available for 3 hours. These data points are high-resolution metrics and are available only for custom metrics that have been defined with a ``StorageResolution`` of 1. 
         
        * Data points with a period of 60 seconds (1-minute) are available for 15 days. 
         
        * Data points with a period of 300 seconds (5-minute) are available for 63 days. 
         
        * Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months). 
         
        Data points that are initially published with a shorter period are aggregated together for long-term storage. For example, if you collect data using a period of 1 minute, the data remains available for 15 days with 1-minute resolution. After 15 days, this data is still available, but is aggregated and retrievable only with a resolution of 5 minutes. After 63 days, the data is further aggregated and is available with a resolution of 1 hour.
        
        CloudWatch started retaining 5-minute and 1-hour metric data as of July 9, 2016.
        
        For information about metrics and dimensions supported by AWS services, see the `Amazon CloudWatch Metrics and Dimensions Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html>`__ in the *Amazon CloudWatch User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/GetMetricStatistics>`_
        
        **Request Syntax** 
        ::
        
          response = metric.get_statistics(
              Dimensions=[
                  {
                      \'Name\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Period=123,
              Statistics=[
                  \'SampleCount\'|\'Average\'|\'Sum\'|\'Minimum\'|\'Maximum\',
              ],
              ExtendedStatistics=[
                  \'string\',
              ],
              Unit=\'Seconds\'|\'Microseconds\'|\'Milliseconds\'|\'Bytes\'|\'Kilobytes\'|\'Megabytes\'|\'Gigabytes\'|\'Terabytes\'|\'Bits\'|\'Kilobits\'|\'Megabits\'|\'Gigabits\'|\'Terabits\'|\'Percent\'|\'Count\'|\'Bytes/Second\'|\'Kilobytes/Second\'|\'Megabytes/Second\'|\'Gigabytes/Second\'|\'Terabytes/Second\'|\'Bits/Second\'|\'Kilobits/Second\'|\'Megabits/Second\'|\'Gigabits/Second\'|\'Terabits/Second\'|\'Count/Second\'|\'None\'
          )
        :type Dimensions: list
        :param Dimensions: 
        
          The dimensions. If the metric contains multiple dimensions, you must include a value for each dimension. CloudWatch treats each unique combination of dimensions as a separate metric. If a specific combination of dimensions was not published, you can\'t retrieve statistics for it. You must specify the same dimensions that were used when the metrics were created. For an example, see `Dimension Combinations <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#dimension-combinations>`__ in the *Amazon CloudWatch User Guide* . For more information about specifying dimensions, see `Publishing Metrics <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html>`__ in the *Amazon CloudWatch User Guide* .
        
          - *(dict) --* 
        
            Expands the identity of a metric.
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the dimension.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The value representing the dimension measurement.
        
        :type StartTime: datetime
        :param StartTime: **[REQUIRED]** 
        
          The time stamp that determines the first data point to return. Start times are evaluated relative to the time that CloudWatch receives the request.
        
          The value specified is inclusive; results include data points with the specified time stamp. The time stamp must be in ISO 8601 UTC format (for example, 2016-10-03T23:00:00Z).
        
          CloudWatch rounds the specified time stamp as follows:
        
          * Start time less than 15 days ago - Round down to the nearest whole minute. For example, 12:32:34 is rounded down to 12:32:00. 
           
          * Start time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For example, 12:32:34 is rounded down to 12:30:00. 
           
          * Start time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For example, 12:32:34 is rounded down to 12:00:00. 
           
          If you set ``Period`` to 5, 10, or 30, the start time of your request is rounded down to the nearest time that corresponds to even 5-, 10-, or 30-second divisions of a minute. For example, if you make a query at (HH:mm:ss) 01:05:23 for the previous 10-second period, the start time of your request is rounded down and you receive data from 01:05:10 to 01:05:20. If you make a query at 15:07:17 for the previous 5 minutes of data, using a period of 5 seconds, you receive data timestamped between 15:02:15 and 15:07:15. 
        
        :type EndTime: datetime
        :param EndTime: **[REQUIRED]** 
        
          The time stamp that determines the last data point to return.
        
          The value specified is exclusive; results include data points up to the specified time stamp. The time stamp must be in ISO 8601 UTC format (for example, 2016-10-10T23:00:00Z).
        
        :type Period: integer
        :param Period: **[REQUIRED]** 
        
          The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` call that includes a ``StorageResolution`` of 1 second.
        
          If the ``StartTime`` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:
        
          * Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute). 
           
          * Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes). 
           
          * Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour). 
           
        :type Statistics: list
        :param Statistics: 
        
          The metric statistics, other than percentile. For percentile statistics, use ``ExtendedStatistics`` . When calling ``GetMetricStatistics`` , you must specify either ``Statistics`` or ``ExtendedStatistics`` , but not both.
        
          - *(string) --* 
        
        :type ExtendedStatistics: list
        :param ExtendedStatistics: 
        
          The percentile statistics. Specify values between p0.0 and p100. When calling ``GetMetricStatistics`` , you must specify either ``Statistics`` or ``ExtendedStatistics`` , but not both. Percentile statistics are not available for metrics when any of the metric values are negative numbers.
        
          - *(string) --* 
        
        :type Unit: string
        :param Unit: 
        
          The unit for a given metric. Metrics may be reported in multiple units. Not supplying a unit results in all units being returned. If you specify only a unit that the metric does not report, the results of the call are null.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Label\': \'string\',
                \'Datapoints\': [
                    {
                        \'Timestamp\': datetime(2015, 1, 1),
                        \'SampleCount\': 123.0,
                        \'Average\': 123.0,
                        \'Sum\': 123.0,
                        \'Minimum\': 123.0,
                        \'Maximum\': 123.0,
                        \'Unit\': \'Seconds\'|\'Microseconds\'|\'Milliseconds\'|\'Bytes\'|\'Kilobytes\'|\'Megabytes\'|\'Gigabytes\'|\'Terabytes\'|\'Bits\'|\'Kilobits\'|\'Megabits\'|\'Gigabits\'|\'Terabits\'|\'Percent\'|\'Count\'|\'Bytes/Second\'|\'Kilobytes/Second\'|\'Megabytes/Second\'|\'Gigabytes/Second\'|\'Terabytes/Second\'|\'Bits/Second\'|\'Kilobits/Second\'|\'Megabits/Second\'|\'Gigabits/Second\'|\'Terabits/Second\'|\'Count/Second\'|\'None\',
                        \'ExtendedStatistics\': {
                            \'string\': 123.0
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Label** *(string) --* 
        
              A label for the specified metric.
        
            - **Datapoints** *(list) --* 
        
              The data points for the specified metric.
        
              - *(dict) --* 
        
                Encapsulates the statistical data that CloudWatch computes from metric data.
        
                - **Timestamp** *(datetime) --* 
        
                  The time stamp used for the data point.
        
                - **SampleCount** *(float) --* 
        
                  The number of metric values that contributed to the aggregate value of this data point.
        
                - **Average** *(float) --* 
        
                  The average of the metric values that correspond to the data point.
        
                - **Sum** *(float) --* 
        
                  The sum of the metric values for the data point.
        
                - **Minimum** *(float) --* 
        
                  The minimum metric value for the data point.
        
                - **Maximum** *(float) --* 
        
                  The maximum metric value for the data point.
        
                - **Unit** *(string) --* 
        
                  The standard unit for the data point.
        
                - **ExtendedStatistics** *(dict) --* 
        
                  The percentile statistic for the data point.
        
                  - *(string) --* 
                    
                    - *(float) --* 
              
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          metric.load()
        :returns: None
        """
        pass

    def put_alarm(self, AlarmName: str, Period: int, EvaluationPeriods: int, Threshold: float, ComparisonOperator: str, AlarmDescription: str = None, ActionsEnabled: bool = None, OKActions: List = None, AlarmActions: List = None, InsufficientDataActions: List = None, Statistic: str = None, ExtendedStatistic: str = None, Dimensions: List = None, Unit: str = None, DatapointsToAlarm: int = None, TreatMissingData: str = None, EvaluateLowSampleCountPercentile: str = None) -> 'Alarm':
        """
        
        When this operation creates an alarm, the alarm state is immediately set to ``INSUFFICIENT_DATA`` . The alarm is evaluated and its state is set appropriately. Any actions associated with the state are then executed.
        
        When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.
        
        If you are an IAM user, you must have Amazon EC2 permissions for some operations:
        
        * ``iam:CreateServiceLinkedRole`` for all alarms with EC2 actions 
         
        * ``ec2:DescribeInstanceStatus`` and ``ec2:DescribeInstances`` for all alarms on EC2 instance status metrics 
         
        * ``ec2:StopInstances`` for alarms with stop actions 
         
        * ``ec2:TerminateInstances`` for alarms with terminate actions 
         
        * ``ec2:DescribeInstanceRecoveryAttribute`` and ``ec2:RecoverInstances`` for alarms with recover actions 
         
        If you have read/write permissions for Amazon CloudWatch but not for Amazon EC2, you can still create an alarm, but the stop or terminate actions are not performed. However, if you are later granted the required permissions, the alarm actions that you created earlier are performed.
        
        If you are using an IAM role (for example, an EC2 instance profile), you cannot stop or terminate the instance using alarm actions. However, you can still see the alarm state and perform any other actions such as Amazon SNS notifications or Auto Scaling policies.
        
        If you are using temporary security credentials granted using AWS STS, you cannot stop or terminate an EC2 instance using alarm actions.
        
        The first time you create an alarm in the AWS Management Console, the CLI, or by using the PutMetricAlarm API, CloudWatch creates the necessary service-linked role for you. The service-linked role is called ``AWSServiceRoleForCloudWatchEvents`` . For more information about service-linked roles, see `AWS service-linked role <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/PutMetricAlarm>`_
        
        **Request Syntax** 
        ::
        
          alarm = metric.put_alarm(
              AlarmName=\'string\',
              AlarmDescription=\'string\',
              ActionsEnabled=True|False,
              OKActions=[
                  \'string\',
              ],
              AlarmActions=[
                  \'string\',
              ],
              InsufficientDataActions=[
                  \'string\',
              ],
              Statistic=\'SampleCount\'|\'Average\'|\'Sum\'|\'Minimum\'|\'Maximum\',
              ExtendedStatistic=\'string\',
              Dimensions=[
                  {
                      \'Name\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              Period=123,
              Unit=\'Seconds\'|\'Microseconds\'|\'Milliseconds\'|\'Bytes\'|\'Kilobytes\'|\'Megabytes\'|\'Gigabytes\'|\'Terabytes\'|\'Bits\'|\'Kilobits\'|\'Megabits\'|\'Gigabits\'|\'Terabits\'|\'Percent\'|\'Count\'|\'Bytes/Second\'|\'Kilobytes/Second\'|\'Megabytes/Second\'|\'Gigabytes/Second\'|\'Terabytes/Second\'|\'Bits/Second\'|\'Kilobits/Second\'|\'Megabits/Second\'|\'Gigabits/Second\'|\'Terabits/Second\'|\'Count/Second\'|\'None\',
              EvaluationPeriods=123,
              DatapointsToAlarm=123,
              Threshold=123.0,
              ComparisonOperator=\'GreaterThanOrEqualToThreshold\'|\'GreaterThanThreshold\'|\'LessThanThreshold\'|\'LessThanOrEqualToThreshold\',
              TreatMissingData=\'string\',
              EvaluateLowSampleCountPercentile=\'string\'
          )
        :type AlarmName: string
        :param AlarmName: **[REQUIRED]** 
        
          The name for the alarm. This name must be unique within the AWS account.
        
        :type AlarmDescription: string
        :param AlarmDescription: 
        
          The description for the alarm.
        
        :type ActionsEnabled: boolean
        :param ActionsEnabled: 
        
          Indicates whether actions should be executed during any changes to the alarm state.
        
        :type OKActions: list
        :param OKActions: 
        
          The actions to execute when this alarm transitions to an ``OK`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        
          Valid Values: ``arn:aws:automate:*region* :ec2:stop`` | ``arn:aws:automate:*region* :ec2:terminate`` | ``arn:aws:automate:*region* :ec2:recover`` | ``arn:aws:sns:*region* :*account-id* :*sns-topic-name* `` | ``arn:aws:autoscaling:*region* :*account-id* :scalingPolicy:*policy-id* autoScalingGroupName/*group-friendly-name* :policyName/*policy-friendly-name* ``  
        
          Valid Values (for use with IAM roles): ``arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Stop/1.0`` | ``arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Terminate/1.0`` | ``arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Reboot/1.0``  
        
          - *(string) --* 
        
        :type AlarmActions: list
        :param AlarmActions: 
        
          The actions to execute when this alarm transitions to the ``ALARM`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        
          Valid Values: ``arn:aws:automate:*region* :ec2:stop`` | ``arn:aws:automate:*region* :ec2:terminate`` | ``arn:aws:automate:*region* :ec2:recover`` | ``arn:aws:sns:*region* :*account-id* :*sns-topic-name* `` | ``arn:aws:autoscaling:*region* :*account-id* :scalingPolicy:*policy-id* autoScalingGroupName/*group-friendly-name* :policyName/*policy-friendly-name* ``  
        
          Valid Values (for use with IAM roles): ``arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Stop/1.0`` | ``arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Terminate/1.0`` | ``arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Reboot/1.0``  
        
          - *(string) --* 
        
        :type InsufficientDataActions: list
        :param InsufficientDataActions: 
        
          The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        
          Valid Values: ``arn:aws:automate:*region* :ec2:stop`` | ``arn:aws:automate:*region* :ec2:terminate`` | ``arn:aws:automate:*region* :ec2:recover`` | ``arn:aws:sns:*region* :*account-id* :*sns-topic-name* `` | ``arn:aws:autoscaling:*region* :*account-id* :scalingPolicy:*policy-id* autoScalingGroupName/*group-friendly-name* :policyName/*policy-friendly-name* ``  
        
          Valid Values (for use with IAM roles): ``>arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Stop/1.0`` | ``arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Terminate/1.0`` | ``arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Reboot/1.0``  
        
          - *(string) --* 
        
        :type Statistic: string
        :param Statistic: 
        
          The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ``ExtendedStatistic`` . When you call ``PutMetricAlarm`` , you must specify either ``Statistic`` or ``ExtendedStatistic,`` but not both.
        
        :type ExtendedStatistic: string
        :param ExtendedStatistic: 
        
          The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100. When you call ``PutMetricAlarm`` , you must specify either ``Statistic`` or ``ExtendedStatistic,`` but not both.
        
        :type Dimensions: list
        :param Dimensions: 
        
          The dimensions for the metric associated with the alarm.
        
          - *(dict) --* 
        
            Expands the identity of a metric.
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the dimension.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The value representing the dimension measurement.
        
        :type Period: integer
        :param Period: **[REQUIRED]** 
        
          The period, in seconds, over which the specified statistic is applied. Valid values are 10, 30, and any multiple of 60.
        
          Be sure to specify 10 or 30 only for metrics that are stored by a ``PutMetricData`` call with a ``StorageResolution`` of 1. If you specify a period of 10 or 30 for a metric that does not have sub-minute resolution, the alarm still attempts to gather data at the period rate that you specify. In this case, it does not receive data for the attempts that do not correspond to a one-minute data resolution, and the alarm may often lapse into INSUFFICENT_DATA status. Specifying 10 or 30 also sets this alarm as a high-resolution alarm, which has a higher charge than other alarms. For more information about pricing, see `Amazon CloudWatch Pricing <https://aws.amazon.com/cloudwatch/pricing/>`__ .
        
          An alarm\'s total current evaluation period can be no longer than one day, so ``Period`` multiplied by ``EvaluationPeriods`` cannot be more than 86,400 seconds.
        
        :type Unit: string
        :param Unit: 
        
          The unit of measure for the statistic. For example, the units for the Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network interfaces. You can also specify a unit when you create a custom metric. Units help provide conceptual meaning to your data. Metric data points that specify a unit of measure, such as Percent, are aggregated separately.
        
          If you specify a unit, you must use a unit that is appropriate for the metric. Otherwise, the CloudWatch alarm can get stuck in the ``INSUFFICIENT DATA`` state. 
        
        :type EvaluationPeriods: integer
        :param EvaluationPeriods: **[REQUIRED]** 
        
          The number of periods over which data is compared to the specified threshold. If you are setting an alarm which requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an \"M out of N\" alarm, this value is the N.
        
          An alarm\'s total current evaluation period can be no longer than one day, so this number multiplied by ``Period`` cannot be more than 86,400 seconds.
        
        :type DatapointsToAlarm: integer
        :param DatapointsToAlarm: 
        
          The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an \"M out of N\" alarm. In that case, this value is the M. For more information, see `Evaluating an Alarm <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation>`__ in the *Amazon CloudWatch User Guide* .
        
        :type Threshold: float
        :param Threshold: **[REQUIRED]** 
        
          The value against which the specified statistic is compared.
        
        :type ComparisonOperator: string
        :param ComparisonOperator: **[REQUIRED]** 
        
          The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.
        
        :type TreatMissingData: string
        :param TreatMissingData: 
        
          Sets how this alarm is to handle missing data points. If ``TreatMissingData`` is omitted, the default behavior of ``missing`` is used. For more information, see `Configuring How CloudWatch Alarms Treats Missing Data <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data>`__ .
        
          Valid Values: ``breaching | notBreaching | ignore | missing``  
        
        :type EvaluateLowSampleCountPercentile: string
        :param EvaluateLowSampleCountPercentile: 
        
          Used only for alarms based on percentiles. If you specify ``ignore`` , the alarm state does not change during periods with too few data points to be statistically significant. If you specify ``evaluate`` or omit this parameter, the alarm is always evaluated and possibly changes state no matter how many data points are available. For more information, see `Percentile-Based CloudWatch Alarms and Low Data Samples <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#percentiles-with-low-samples>`__ .
        
          Valid Values: ``evaluate | ignore``  
        
        :rtype: :py:class:`cloudwatch.Alarm`
        :returns: Alarm resource
        """
        pass

    def put_data(self):
        """
        
        You can publish either individual data points in the ``Value`` field, or arrays of values and the number of times each value occurred during the period by using the ``Values`` and ``Counts`` fields in the ``MetricDatum`` structure. Using the ``Values`` and ``Counts`` method enables you to publish up to 150 values per metric with one ``PutMetricData`` request, and supports retrieving percentile statistics on this data.
        
        Each ``PutMetricData`` request is limited to 40 KB in size for HTTP POST requests. You can send a payload compressed by gzip. Each request is also limited to no more than 20 different metrics.
        
        Although the ``Value`` parameter accepts numbers of type ``Double`` , CloudWatch rejects values that are either too small or too large. Values must be in the range of 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2). In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.
        
        You can use up to 10 dimensions per metric to further clarify what data the metric collects. For more information about specifying dimensions, see `Publishing Metrics <http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html>`__ in the *Amazon CloudWatch User Guide* .
        
        Data points with time stamps from 24 hours ago or longer can take at least 48 hours to become available for  GetMetricData or  GetMetricStatistics from the time they are submitted.
        
        CloudWatch needs raw data points to calculate percentile statistics. These raw data points could be published individually or as part of ``Values`` and ``Counts`` arrays. If you publish data using statistic sets in the ``StatisticValues`` field instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:
        
        * The ``SampleCount`` value of the statistic set is 1 and ``Min`` , ``Max`` , and ``Sum`` are all equal. 
         
        * The ``Min`` and ``Max`` are equal, and ``Sum`` is equal to ``Min`` multiplied by ``SampleCount`` . 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/PutMetricData>`_
        
        **Request Syntax** 
        ::
        
          response = metric.put_data()
          
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          metric.load()
        :returns: None
        """
        pass


class alarms(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Alarm']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_
        
        **Request Syntax** 
        ::
        
          alarm_iterator = cloudwatch.alarms.all()
          
        :rtype: list(:py:class:`cloudwatch.Alarm`)
        :returns: A list of Alarm resources
        """
        pass

    
    @classmethod
    def delete(cls):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DeleteAlarms>`_
        
        **Request Syntax** 
        ::
        
          response = cloudwatch.alarms.delete()
          
        :returns: None
        """
        pass

    
    @classmethod
    def disable_actions(cls):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DisableAlarmActions>`_
        
        **Request Syntax** 
        ::
        
          response = cloudwatch.alarms.disable_actions()
          
        :returns: None
        """
        pass

    
    @classmethod
    def enable_actions(cls):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/EnableAlarmActions>`_
        
        **Request Syntax** 
        ::
        
          response = cloudwatch.alarms.enable_actions()
          
        :returns: None
        """
        pass

    
    @classmethod
    def filter(cls, AlarmNames: List = None, AlarmNamePrefix: str = None, StateValue: str = None, ActionPrefix: str = None, MaxRecords: int = None, NextToken: str = None) -> List['Alarm']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_
        
        **Request Syntax** 
        ::
        
          alarm_iterator = cloudwatch.alarms.filter(
              AlarmNames=[
                  \'string\',
              ],
              AlarmNamePrefix=\'string\',
              StateValue=\'OK\'|\'ALARM\'|\'INSUFFICIENT_DATA\',
              ActionPrefix=\'string\',
              MaxRecords=123,
              NextToken=\'string\'
          )
        :type AlarmNames: list
        :param AlarmNames: 
        
          The names of the alarms.
        
          - *(string) --* 
        
        :type AlarmNamePrefix: string
        :param AlarmNamePrefix: 
        
          The alarm name prefix. If this parameter is specified, you cannot specify ``AlarmNames`` .
        
        :type StateValue: string
        :param StateValue: 
        
          The state value to be used in matching alarms.
        
        :type ActionPrefix: string
        :param ActionPrefix: 
        
          The action name prefix.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of alarm descriptions to retrieve.
        
        :type NextToken: string
        :param NextToken: 
        
          The token returned by a previous call to indicate that there is more data available.
        
        :rtype: list(:py:class:`cloudwatch.Alarm`)
        :returns: A list of Alarm resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Alarm']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_
        
        **Request Syntax** 
        ::
        
          alarm_iterator = cloudwatch.alarms.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`cloudwatch.Alarm`)
        :returns: A list of Alarm resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Alarm']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_
        
        **Request Syntax** 
        ::
        
          alarm_iterator = cloudwatch.alarms.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`cloudwatch.Alarm`)
        :returns: A list of Alarm resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass


class metrics(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Metric']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListMetrics>`_
        
        **Request Syntax** 
        ::
        
          metric_iterator = cloudwatch.metrics.all()
          
        :rtype: list(:py:class:`cloudwatch.Metric`)
        :returns: A list of Metric resources
        """
        pass

    
    @classmethod
    def filter(cls, Namespace: str = None, MetricName: str = None, Dimensions: List = None, NextToken: str = None) -> List['Metric']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListMetrics>`_
        
        **Request Syntax** 
        ::
        
          metric_iterator = cloudwatch.metrics.filter(
              Namespace=\'string\',
              MetricName=\'string\',
              Dimensions=[
                  {
                      \'Name\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              NextToken=\'string\'
          )
        :type Namespace: string
        :param Namespace: 
        
          The namespace to filter against.
        
        :type MetricName: string
        :param MetricName: 
        
          The name of the metric to filter against.
        
        :type Dimensions: list
        :param Dimensions: 
        
          The dimensions to filter against.
        
          - *(dict) --* 
        
            Represents filters for a dimension.
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The dimension name to be matched.
        
            - **Value** *(string) --* 
        
              The value of the dimension to be matched.
        
        :type NextToken: string
        :param NextToken: 
        
          The token returned by a previous call to indicate that there is more data available.
        
        :rtype: list(:py:class:`cloudwatch.Metric`)
        :returns: A list of Metric resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Metric']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListMetrics>`_
        
        **Request Syntax** 
        ::
        
          metric_iterator = cloudwatch.metrics.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`cloudwatch.Metric`)
        :returns: A list of Metric resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Metric']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListMetrics>`_
        
        **Request Syntax** 
        ::
        
          metric_iterator = cloudwatch.metrics.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`cloudwatch.Metric`)
        :returns: A list of Metric resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass
