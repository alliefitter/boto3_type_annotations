from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeAlarmHistory(Paginator):
    def paginate(self, AlarmName: str = None, HistoryItemType: str = None, StartDate: datetime = None, EndDate: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarmHistory>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AlarmName=\'string\',
              HistoryItemType=\'ConfigurationUpdate\'|\'StateUpdate\'|\'Action\',
              StartDate=datetime(2015, 1, 1),
              EndDate=datetime(2015, 1, 1),
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
        
        """
        pass


class DescribeAlarms(Paginator):
    def paginate(self, AlarmNames: List = None, AlarmNamePrefix: str = None, StateValue: str = None, ActionPrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AlarmNames=[
                  \'string\',
              ],
              AlarmNamePrefix=\'string\',
              StateValue=\'OK\'|\'ALARM\'|\'INSUFFICIENT_DATA\',
              ActionPrefix=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'MetricAlarms\': [
                    {
                        \'AlarmName\': \'string\',
                        \'AlarmArn\': \'string\',
                        \'AlarmDescription\': \'string\',
                        \'AlarmConfigurationUpdatedTimestamp\': datetime(2015, 1, 1),
                        \'ActionsEnabled\': True|False,
                        \'OKActions\': [
                            \'string\',
                        ],
                        \'AlarmActions\': [
                            \'string\',
                        ],
                        \'InsufficientDataActions\': [
                            \'string\',
                        ],
                        \'StateValue\': \'OK\'|\'ALARM\'|\'INSUFFICIENT_DATA\',
                        \'StateReason\': \'string\',
                        \'StateReasonData\': \'string\',
                        \'StateUpdatedTimestamp\': datetime(2015, 1, 1),
                        \'MetricName\': \'string\',
                        \'Namespace\': \'string\',
                        \'Statistic\': \'SampleCount\'|\'Average\'|\'Sum\'|\'Minimum\'|\'Maximum\',
                        \'ExtendedStatistic\': \'string\',
                        \'Dimensions\': [
                            {
                                \'Name\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'Period\': 123,
                        \'Unit\': \'Seconds\'|\'Microseconds\'|\'Milliseconds\'|\'Bytes\'|\'Kilobytes\'|\'Megabytes\'|\'Gigabytes\'|\'Terabytes\'|\'Bits\'|\'Kilobits\'|\'Megabits\'|\'Gigabits\'|\'Terabits\'|\'Percent\'|\'Count\'|\'Bytes/Second\'|\'Kilobytes/Second\'|\'Megabytes/Second\'|\'Gigabytes/Second\'|\'Terabytes/Second\'|\'Bits/Second\'|\'Kilobits/Second\'|\'Megabits/Second\'|\'Gigabits/Second\'|\'Terabits/Second\'|\'Count/Second\'|\'None\',
                        \'EvaluationPeriods\': 123,
                        \'DatapointsToAlarm\': 123,
                        \'Threshold\': 123.0,
                        \'ComparisonOperator\': \'GreaterThanOrEqualToThreshold\'|\'GreaterThanThreshold\'|\'LessThanThreshold\'|\'LessThanOrEqualToThreshold\',
                        \'TreatMissingData\': \'string\',
                        \'EvaluateLowSampleCountPercentile\': \'string\'
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
        
        """
        pass


class ListDashboards(Paginator):
    def paginate(self, DashboardNamePrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListDashboards>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DashboardNamePrefix=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'DashboardEntries\': [
                    {
                        \'DashboardName\': \'string\',
                        \'DashboardArn\': \'string\',
                        \'LastModified\': datetime(2015, 1, 1),
                        \'Size\': 123
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
        
        """
        pass


class ListMetrics(Paginator):
    def paginate(self, Namespace: str = None, MetricName: str = None, Dimensions: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListMetrics>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Namespace=\'string\',
              MetricName=\'string\',
              Dimensions=[
                  {
                      \'Name\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Metrics\': [
                    {
                        \'Namespace\': \'string\',
                        \'MetricName\': \'string\',
                        \'Dimensions\': [
                            {
                                \'Name\': \'string\',
                                \'Value\': \'string\'
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
        
                  The name of the metric.
        
                - **Dimensions** *(list) --* 
        
                  The dimensions for the metric.
        
                  - *(dict) --* 
        
                    Expands the identity of a metric.
        
                    - **Name** *(string) --* 
        
                      The name of the dimension.
        
                    - **Value** *(string) --* 
        
                      The value representing the dimension measurement.
        
        """
        pass
