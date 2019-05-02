from typing import Dict
from typing import List
from datetime import datetime
from botocore.paginate import Paginator


class DescribeAlarmHistory(Paginator):
    def paginate(self, AlarmName: str = None, HistoryItemType: str = None, StartDate: datetime = None, EndDate: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudWatch.Client.describe_alarm_history`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarmHistory>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AlarmName='string',
              HistoryItemType='ConfigurationUpdate'|'StateUpdate'|'Action',
              StartDate=datetime(2015, 1, 1),
              EndDate=datetime(2015, 1, 1),
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'AlarmHistoryItems': [
                    {
                        'AlarmName': 'string',
                        'Timestamp': datetime(2015, 1, 1),
                        'HistoryItemType': 'ConfigurationUpdate'|'StateUpdate'|'Action',
                        'HistorySummary': 'string',
                        'HistoryData': 'string'
                    },
                ],
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
        :type AlarmName: string
        :param AlarmName:
          The name of the alarm.
        :type HistoryItemType: string
        :param HistoryItemType:
          The type of alarm histories to retrieve.
        :type StartDate: datetime
        :param StartDate:
          The starting date to retrieve alarm history.
        :type EndDate: datetime
        :param EndDate:
          The ending date to retrieve alarm history.
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeAlarms(Paginator):
    def paginate(self, AlarmNames: List = None, AlarmNamePrefix: str = None, StateValue: str = None, ActionPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudWatch.Client.describe_alarms`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AlarmNames=[
                  'string',
              ],
              AlarmNamePrefix='string',
              StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
              ActionPrefix='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'MetricAlarms': [
                    {
                        'AlarmName': 'string',
                        'AlarmArn': 'string',
                        'AlarmDescription': 'string',
                        'AlarmConfigurationUpdatedTimestamp': datetime(2015, 1, 1),
                        'ActionsEnabled': True|False,
                        'OKActions': [
                            'string',
                        ],
                        'AlarmActions': [
                            'string',
                        ],
                        'InsufficientDataActions': [
                            'string',
                        ],
                        'StateValue': 'OK'|'ALARM'|'INSUFFICIENT_DATA',
                        'StateReason': 'string',
                        'StateReasonData': 'string',
                        'StateUpdatedTimestamp': datetime(2015, 1, 1),
                        'MetricName': 'string',
                        'Namespace': 'string',
                        'Statistic': 'SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
                        'ExtendedStatistic': 'string',
                        'Dimensions': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ],
                        'Period': 123,
                        'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
                        'EvaluationPeriods': 123,
                        'DatapointsToAlarm': 123,
                        'Threshold': 123.0,
                        'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
                        'TreatMissingData': 'string',
                        'EvaluateLowSampleCountPercentile': 'string',
                        'Metrics': [
                            {
                                'Id': 'string',
                                'MetricStat': {
                                    'Metric': {
                                        'Namespace': 'string',
                                        'MetricName': 'string',
                                        'Dimensions': [
                                            {
                                                'Name': 'string',
                                                'Value': 'string'
                                            },
                                        ]
                                    },
                                    'Period': 123,
                                    'Stat': 'string',
                                    'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
                                },
                                'Expression': 'string',
                                'Label': 'string',
                                'ReturnData': True|False
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **MetricAlarms** *(list) --* 
              The information for the specified alarms.
              - *(dict) --* 
                Represents an alarm.
                - **AlarmName** *(string) --* 
                  The name of the alarm.
                - **AlarmArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the alarm.
                - **AlarmDescription** *(string) --* 
                  The description of the alarm.
                - **AlarmConfigurationUpdatedTimestamp** *(datetime) --* 
                  The time stamp of the last update to the alarm configuration.
                - **ActionsEnabled** *(boolean) --* 
                  Indicates whether actions should be executed during any changes to the alarm state.
                - **OKActions** *(list) --* 
                  The actions to execute when this alarm transitions to the ``OK`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
                  - *(string) --* 
                - **AlarmActions** *(list) --* 
                  The actions to execute when this alarm transitions to the ``ALARM`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
                  - *(string) --* 
                - **InsufficientDataActions** *(list) --* 
                  The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
                  - *(string) --* 
                - **StateValue** *(string) --* 
                  The state value for the alarm.
                - **StateReason** *(string) --* 
                  An explanation for the alarm state, in text format.
                - **StateReasonData** *(string) --* 
                  An explanation for the alarm state, in JSON format.
                - **StateUpdatedTimestamp** *(datetime) --* 
                  The time stamp of the last update to the alarm state.
                - **MetricName** *(string) --* 
                  The name of the metric associated with the alarm.
                - **Namespace** *(string) --* 
                  The namespace of the metric associated with the alarm.
                - **Statistic** *(string) --* 
                  The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ``ExtendedStatistic`` .
                - **ExtendedStatistic** *(string) --* 
                  The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.
                - **Dimensions** *(list) --* 
                  The dimensions for the metric associated with the alarm.
                  - *(dict) --* 
                    Expands the identity of a metric.
                    - **Name** *(string) --* 
                      The name of the dimension.
                    - **Value** *(string) --* 
                      The value representing the dimension measurement.
                - **Period** *(integer) --* 
                  The period, in seconds, over which the statistic is applied.
                - **Unit** *(string) --* 
                  The unit of the metric associated with the alarm.
                - **EvaluationPeriods** *(integer) --* 
                  The number of periods over which data is compared to the specified threshold.
                - **DatapointsToAlarm** *(integer) --* 
                  The number of datapoints that must be breaching to trigger the alarm.
                - **Threshold** *(float) --* 
                  The value to compare with the specified statistic.
                - **ComparisonOperator** *(string) --* 
                  The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.
                - **TreatMissingData** *(string) --* 
                  Sets how this alarm is to handle missing data points. If this parameter is omitted, the default behavior of ``missing`` is used.
                - **EvaluateLowSampleCountPercentile** *(string) --* 
                  Used only for alarms based on percentiles. If ``ignore`` , the alarm state does not change during periods with too few data points to be statistically significant. If ``evaluate`` or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.
                - **Metrics** *(list) --* 
                  - *(dict) --* 
                    This structure is used in both ``GetMetricData`` and ``PutMetricAlarm`` . The supported use of this structure is different for those two operations.
                    When used in ``GetMetricData`` , it indicates the metric data to return, and whether this call is just retrieving a batch set of data for one metric, or is performing a math expression on metric data. A single ``GetMetricData`` call can include up to 100 ``MetricDataQuery`` structures.
                    When used in ``PutMetricAlarm`` , it enables you to create an alarm based on a metric math expression. Each ``MetricDataQuery`` in the array specifies either a metric to retrieve, or a math expression to be performed on retrieved metrics. A single ``PutMetricAlarm`` call can include up to 20 ``MetricDataQuery`` structures in the array. The 20 structures can include as many as 10 structures that contain a ``MetricStat`` parameter to retrieve a metric, and as many as 10 structures that contain the ``Expression`` parameter to perform a math expression. Of those ``Expression`` structures, one must have ``True`` as the value for ``ReturnData`` . The result of this expression is the value the alarm watches.
                    Any expression used in a ``PutMetricAlarm`` operation must return a single time series. For more information, see `Metric Math Syntax and Functions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__ in the *Amazon CloudWatch User Guide* .
                    Some of the parameters of this structure also have different uses whether you are using this structure in a ``GetMetricData`` operation or a ``PutMetricAlarm`` operation. These differences are explained in the following parameter list.
                    - **Id** *(string) --* 
                      A short name used to tie this object to the results in the response. This name must be unique within a single call to ``GetMetricData`` . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
                    - **MetricStat** *(dict) --* 
                      The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.
                      Within one MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.
                      - **Metric** *(dict) --* 
                        The metric to return, including the metric name, namespace, and dimensions.
                        - **Namespace** *(string) --* 
                          The namespace of the metric.
                        - **MetricName** *(string) --* 
                          The name of the metric. This is a required field.
                        - **Dimensions** *(list) --* 
                          The dimensions for the metric.
                          - *(dict) --* 
                            Expands the identity of a metric.
                            - **Name** *(string) --* 
                              The name of the dimension.
                            - **Value** *(string) --* 
                              The value representing the dimension measurement.
                      - **Period** *(integer) --* 
                        The period, in seconds, to use when retrieving the metric.
                      - **Stat** *(string) --* 
                        The statistic to return. It can include any CloudWatch statistic or extended statistic.
                      - **Unit** *(string) --* 
                        The unit to use for the returned data points.
                    - **Expression** *(string) --* 
                      The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the ``Id`` of the other metrics to refer to those metrics, and can also use the ``Id`` of other expressions to use the result of those expressions. For more information about metric math expressions, see `Metric Math Syntax and Functions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__ in the *Amazon CloudWatch User Guide* .
                      Within each MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.
                    - **Label** *(string) --* 
                      A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch generates a default.
                    - **ReturnData** *(boolean) --* 
                      When used in ``GetMetricData`` , this option indicates whether to return the timestamps and raw data values of this metric. If you are performing this call just to do math expressions and do not also need the raw data returned, you can specify ``False`` . If you omit this, the default of ``True`` is used.
                      When used in ``PutMetricAlarm`` , specify ``True`` for the one expression result to use as the alarm. For all other metrics and expressions in the same ``PutMetricAlarm`` operation, specify ``ReturnData`` as False.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class GetMetricData(Paginator):
    def paginate(self, MetricDataQueries: List, StartTime: datetime, EndTime: datetime, ScanBy: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudWatch.Client.get_metric_data`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/GetMetricData>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              MetricDataQueries=[
                  {
                      'Id': 'string',
                      'MetricStat': {
                          'Metric': {
                              'Namespace': 'string',
                              'MetricName': 'string',
                              'Dimensions': [
                                  {
                                      'Name': 'string',
                                      'Value': 'string'
                                  },
                              ]
                          },
                          'Period': 123,
                          'Stat': 'string',
                          'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
                      },
                      'Expression': 'string',
                      'Label': 'string',
                      'ReturnData': True|False
                  },
              ],
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              ScanBy='TimestampDescending'|'TimestampAscending',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'MetricDataResults': [
                    {
                        'Id': 'string',
                        'Label': 'string',
                        'Timestamps': [
                            datetime(2015, 1, 1),
                        ],
                        'Values': [
                            123.0,
                        ],
                        'StatusCode': 'Complete'|'InternalError'|'PartialData',
                        'Messages': [
                            {
                                'Code': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
                'Messages': [
                    {
                        'Code': 'string',
                        'Value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **MetricDataResults** *(list) --* 
              The metrics that are returned, including the metric name, namespace, and dimensions.
              - *(dict) --* 
                A ``GetMetricData`` call returns an array of ``MetricDataResult`` structures. Each of these structures includes the data points for that metric, along with the timestamps of those data points and other identifying information.
                - **Id** *(string) --* 
                  The short name you specified to represent this metric.
                - **Label** *(string) --* 
                  The human-readable label associated with the data.
                - **Timestamps** *(list) --* 
                  The timestamps for the data points, formatted in Unix timestamp format. The number of timestamps always matches the number of values and the value for Timestamps[x] is Values[x].
                  - *(datetime) --* 
                - **Values** *(list) --* 
                  The data points for the metric corresponding to ``Timestamps`` . The number of values always matches the number of timestamps and the timestamp for Values[x] is Timestamps[x].
                  - *(float) --* 
                - **StatusCode** *(string) --* 
                  The status of the returned data. ``Complete`` indicates that all data points in the requested time range were returned. ``PartialData`` means that an incomplete set of data points were returned. You can use the ``NextToken`` value that was returned and repeat your request to get more data points. ``NextToken`` is not returned if you are performing a math expression. ``InternalError`` indicates that an error occurred. Retry your request using ``NextToken`` , if present.
                - **Messages** *(list) --* 
                  A list of messages with additional information about the data returned.
                  - *(dict) --* 
                    A message returned by the ``GetMetricData`` API, including a code and a description.
                    - **Code** *(string) --* 
                      The error code or status code associated with the message.
                    - **Value** *(string) --* 
                      The message text.
            - **Messages** *(list) --* 
              Contains a message about this ``GetMetricData`` operation, if the operation results in such a message. An example of a message that may be returned is ``Maximum number of allowed metrics exceeded`` . If there is a message, as much of the operation as possible is still executed.
              A message appears here only if it is related to the global ``GetMetricData`` operation. Any message about a specific metric returned by the operation appears in the ``MetricDataResult`` object returned for that metric.
              - *(dict) --* 
                A message returned by the ``GetMetricData`` API, including a code and a description.
                - **Code** *(string) --* 
                  The error code or status code associated with the message.
                - **Value** *(string) --* 
                  The message text.
        :type MetricDataQueries: list
        :param MetricDataQueries: **[REQUIRED]**
          The metric queries to be returned. A single ``GetMetricData`` call can include as many as 100 ``MetricDataQuery`` structures. Each of these structures can specify either a metric to retrieve, or a math expression to perform on retrieved data.
          - *(dict) --*
            This structure is used in both ``GetMetricData`` and ``PutMetricAlarm`` . The supported use of this structure is different for those two operations.
            When used in ``GetMetricData`` , it indicates the metric data to return, and whether this call is just retrieving a batch set of data for one metric, or is performing a math expression on metric data. A single ``GetMetricData`` call can include up to 100 ``MetricDataQuery`` structures.
            When used in ``PutMetricAlarm`` , it enables you to create an alarm based on a metric math expression. Each ``MetricDataQuery`` in the array specifies either a metric to retrieve, or a math expression to be performed on retrieved metrics. A single ``PutMetricAlarm`` call can include up to 20 ``MetricDataQuery`` structures in the array. The 20 structures can include as many as 10 structures that contain a ``MetricStat`` parameter to retrieve a metric, and as many as 10 structures that contain the ``Expression`` parameter to perform a math expression. Of those ``Expression`` structures, one must have ``True`` as the value for ``ReturnData`` . The result of this expression is the value the alarm watches.
            Any expression used in a ``PutMetricAlarm`` operation must return a single time series. For more information, see `Metric Math Syntax and Functions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__ in the *Amazon CloudWatch User Guide* .
            Some of the parameters of this structure also have different uses whether you are using this structure in a ``GetMetricData`` operation or a ``PutMetricAlarm`` operation. These differences are explained in the following parameter list.
            - **Id** *(string) --* **[REQUIRED]**
              A short name used to tie this object to the results in the response. This name must be unique within a single call to ``GetMetricData`` . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
            - **MetricStat** *(dict) --*
              The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.
              Within one MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.
              - **Metric** *(dict) --* **[REQUIRED]**
                The metric to return, including the metric name, namespace, and dimensions.
                - **Namespace** *(string) --*
                  The namespace of the metric.
                - **MetricName** *(string) --*
                  The name of the metric. This is a required field.
                - **Dimensions** *(list) --*
                  The dimensions for the metric.
                  - *(dict) --*
                    Expands the identity of a metric.
                    - **Name** *(string) --* **[REQUIRED]**
                      The name of the dimension.
                    - **Value** *(string) --* **[REQUIRED]**
                      The value representing the dimension measurement.
              - **Period** *(integer) --* **[REQUIRED]**
                The period, in seconds, to use when retrieving the metric.
              - **Stat** *(string) --* **[REQUIRED]**
                The statistic to return. It can include any CloudWatch statistic or extended statistic.
              - **Unit** *(string) --*
                The unit to use for the returned data points.
            - **Expression** *(string) --*
              The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the ``Id`` of the other metrics to refer to those metrics, and can also use the ``Id`` of other expressions to use the result of those expressions. For more information about metric math expressions, see `Metric Math Syntax and Functions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__ in the *Amazon CloudWatch User Guide* .
              Within each MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.
            - **Label** *(string) --*
              A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch generates a default.
            - **ReturnData** *(boolean) --*
              When used in ``GetMetricData`` , this option indicates whether to return the timestamps and raw data values of this metric. If you are performing this call just to do math expressions and do not also need the raw data returned, you can specify ``False`` . If you omit this, the default of ``True`` is used.
              When used in ``PutMetricAlarm`` , specify ``True`` for the one expression result to use as the alarm. For all other metrics and expressions in the same ``PutMetricAlarm`` operation, specify ``ReturnData`` as False.
        :type StartTime: datetime
        :param StartTime: **[REQUIRED]**
          The time stamp indicating the earliest data to be returned.
          For better performance, specify ``StartTime`` and ``EndTime`` values that align with the value of the metric\'s ``Period`` and sync up with the beginning and end of an hour. For example, if the ``Period`` of a metric is 5 minutes, specifying 12:05 or 12:30 as ``StartTime`` can get a faster response from CloudWatch than setting 12:07 or 12:29 as the ``StartTime`` .
        :type EndTime: datetime
        :param EndTime: **[REQUIRED]**
          The time stamp indicating the latest data to be returned.
          For better performance, specify ``StartTime`` and ``EndTime`` values that align with the value of the metric\'s ``Period`` and sync up with the beginning and end of an hour. For example, if the ``Period`` of a metric is 5 minutes, specifying 12:05 or 12:30 as ``EndTime`` can get a faster response from CloudWatch than setting 12:07 or 12:29 as the ``EndTime`` .
        :type ScanBy: string
        :param ScanBy:
          The order in which data points should be returned. ``TimestampDescending`` returns the newest data first and paginates when the ``MaxDatapoints`` limit is reached. ``TimestampAscending`` returns the oldest data first and paginates when the ``MaxDatapoints`` limit is reached.
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class ListDashboards(Paginator):
    def paginate(self, DashboardNamePrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudWatch.Client.list_dashboards`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListDashboards>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DashboardNamePrefix='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'DashboardEntries': [
                    {
                        'DashboardName': 'string',
                        'DashboardArn': 'string',
                        'LastModified': datetime(2015, 1, 1),
                        'Size': 123
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DashboardEntries** *(list) --* 
              The list of matching dashboards.
              - *(dict) --* 
                Represents a specific dashboard.
                - **DashboardName** *(string) --* 
                  The name of the dashboard.
                - **DashboardArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the dashboard.
                - **LastModified** *(datetime) --* 
                  The time stamp of when the dashboard was last modified, either by an API call or through the console. This number is expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.
                - **Size** *(integer) --* 
                  The size of the dashboard, in bytes.
        :type DashboardNamePrefix: string
        :param DashboardNamePrefix:
          If you specify this parameter, only the dashboards with names starting with the specified string are listed. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, \".\", \"-\", and \"_\".
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class ListMetrics(Paginator):
    def paginate(self, Namespace: str = None, MetricName: str = None, Dimensions: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudWatch.Client.list_metrics`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListMetrics>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Namespace='string',
              MetricName='string',
              Dimensions=[
                  {
                      'Name': 'string',
                      'Value': 'string'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Metrics': [
                    {
                        'Namespace': 'string',
                        'MetricName': 'string',
                        'Dimensions': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Metrics** *(list) --* 
              The metrics.
              - *(dict) --* 
                Represents a specific metric.
                - **Namespace** *(string) --* 
                  The namespace of the metric.
                - **MetricName** *(string) --* 
                  The name of the metric. This is a required field.
                - **Dimensions** *(list) --* 
                  The dimensions for the metric.
                  - *(dict) --* 
                    Expands the identity of a metric.
                    - **Name** *(string) --* 
                      The name of the dimension.
                    - **Value** *(string) --* 
                      The value representing the dimension measurement.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass
