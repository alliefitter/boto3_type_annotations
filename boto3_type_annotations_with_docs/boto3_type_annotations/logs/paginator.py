from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeDestinations(Paginator):
    def paginate(self, DestinationNamePrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeDestinations>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DestinationNamePrefix=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type DestinationNamePrefix: string
        :param DestinationNamePrefix: 
        
          The prefix to match. If you don\'t specify a value, no prefix filter is applied.
        
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
                \'destinations\': [
                    {
                        \'destinationName\': \'string\',
                        \'targetArn\': \'string\',
                        \'roleArn\': \'string\',
                        \'accessPolicy\': \'string\',
                        \'arn\': \'string\',
                        \'creationTime\': 123
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **destinations** *(list) --* 
        
              The destinations.
        
              - *(dict) --* 
        
                Represents a cross-account destination that receives subscription log events.
        
                - **destinationName** *(string) --* 
        
                  The name of the destination.
        
                - **targetArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the physical target to where the log events are delivered (for example, a Kinesis stream).
        
                - **roleArn** *(string) --* 
        
                  A role for impersonation, used when delivering log events to the target.
        
                - **accessPolicy** *(string) --* 
        
                  An IAM policy document that governs which AWS accounts can create subscription filters against this destination.
        
                - **arn** *(string) --* 
        
                  The ARN of this destination.
        
                - **creationTime** *(integer) --* 
        
                  The creation time of the destination, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeLogGroups(Paginator):
    def paginate(self, logGroupNamePrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeLogGroups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              logGroupNamePrefix=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type logGroupNamePrefix: string
        :param logGroupNamePrefix: 
        
          The prefix to match.
        
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
                \'logGroups\': [
                    {
                        \'logGroupName\': \'string\',
                        \'creationTime\': 123,
                        \'retentionInDays\': 123,
                        \'metricFilterCount\': 123,
                        \'arn\': \'string\',
                        \'storedBytes\': 123,
                        \'kmsKeyId\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **logGroups** *(list) --* 
        
              The log groups.
        
              - *(dict) --* 
        
                Represents a log group.
        
                - **logGroupName** *(string) --* 
        
                  The name of the log group.
        
                - **creationTime** *(integer) --* 
        
                  The creation time of the log group, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
        
                - **retentionInDays** *(integer) --* 
        
                  The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.
        
                - **metricFilterCount** *(integer) --* 
        
                  The number of metric filters.
        
                - **arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the log group.
        
                - **storedBytes** *(integer) --* 
        
                  The number of bytes stored.
        
                - **kmsKeyId** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeLogStreams(Paginator):
    def paginate(self, logGroupName: str, logStreamNamePrefix: str = None, orderBy: str = None, descending: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeLogStreams>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              logGroupName=\'string\',
              logStreamNamePrefix=\'string\',
              orderBy=\'LogStreamName\'|\'LastEventTime\',
              descending=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type logGroupName: string
        :param logGroupName: **[REQUIRED]** 
        
          The name of the log group.
        
        :type logStreamNamePrefix: string
        :param logStreamNamePrefix: 
        
          The prefix to match.
        
          If ``orderBy`` is ``LastEventTime`` ,you cannot specify this parameter.
        
        :type orderBy: string
        :param orderBy: 
        
          If the value is ``LogStreamName`` , the results are ordered by log stream name. If the value is ``LastEventTime`` , the results are ordered by the event time. The default value is ``LogStreamName`` .
        
          If you order the results by event time, you cannot specify the ``logStreamNamePrefix`` parameter.
        
          lastEventTimestamp represents the time of the most recent log event in the log stream in CloudWatch Logs. This number is expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. lastEventTimeStamp updates on an eventual consistency basis. It typically updates in less than an hour from ingestion, but may take longer in some rare situations.
        
        :type descending: boolean
        :param descending: 
        
          If the value is true, results are returned in descending order. If the value is to false, results are returned in ascending order. The default value is false.
        
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
                \'logStreams\': [
                    {
                        \'logStreamName\': \'string\',
                        \'creationTime\': 123,
                        \'firstEventTimestamp\': 123,
                        \'lastEventTimestamp\': 123,
                        \'lastIngestionTime\': 123,
                        \'uploadSequenceToken\': \'string\',
                        \'arn\': \'string\',
                        \'storedBytes\': 123
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **logStreams** *(list) --* 
        
              The log streams.
        
              - *(dict) --* 
        
                Represents a log stream, which is a sequence of log events from a single emitter of logs.
        
                - **logStreamName** *(string) --* 
        
                  The name of the log stream.
        
                - **creationTime** *(integer) --* 
        
                  The creation time of the stream, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
        
                - **firstEventTimestamp** *(integer) --* 
        
                  The time of the first event, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
        
                - **lastEventTimestamp** *(integer) --* 
        
                  the time of the most recent log event in the log stream in CloudWatch Logs. This number is expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. lastEventTime updates on an eventual consistency basis. It typically updates in less than an hour from ingestion, but may take longer in some rare situations.
        
                - **lastIngestionTime** *(integer) --* 
        
                  The ingestion time, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
        
                - **uploadSequenceToken** *(string) --* 
        
                  The sequence token.
        
                - **arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the log stream.
        
                - **storedBytes** *(integer) --* 
        
                  The number of bytes stored.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeMetricFilters(Paginator):
    def paginate(self, logGroupName: str = None, filterNamePrefix: str = None, metricName: str = None, metricNamespace: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeMetricFilters>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              logGroupName=\'string\',
              filterNamePrefix=\'string\',
              metricName=\'string\',
              metricNamespace=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type logGroupName: string
        :param logGroupName: 
        
          The name of the log group.
        
        :type filterNamePrefix: string
        :param filterNamePrefix: 
        
          The prefix to match.
        
        :type metricName: string
        :param metricName: 
        
          Filters results to include only those with the specified metric name. If you include this parameter in your request, you must also include the ``metricNamespace`` parameter.
        
        :type metricNamespace: string
        :param metricNamespace: 
        
          Filters results to include only those in the specified namespace. If you include this parameter in your request, you must also include the ``metricName`` parameter.
        
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
                \'metricFilters\': [
                    {
                        \'filterName\': \'string\',
                        \'filterPattern\': \'string\',
                        \'metricTransformations\': [
                            {
                                \'metricName\': \'string\',
                                \'metricNamespace\': \'string\',
                                \'metricValue\': \'string\',
                                \'defaultValue\': 123.0
                            },
                        ],
                        \'creationTime\': 123,
                        \'logGroupName\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **metricFilters** *(list) --* 
        
              The metric filters.
        
              - *(dict) --* 
        
                Metric filters express how CloudWatch Logs would extract metric observations from ingested log events and transform them into metric data in a CloudWatch metric.
        
                - **filterName** *(string) --* 
        
                  The name of the metric filter.
        
                - **filterPattern** *(string) --* 
        
                  A symbolic description of how CloudWatch Logs should interpret the data in each log event. For example, a log event may contain time stamps, IP addresses, strings, and so on. You use the filter pattern to specify what to look for in the log event message.
        
                - **metricTransformations** *(list) --* 
        
                  The metric transformations.
        
                  - *(dict) --* 
        
                    Indicates how to transform ingested log events in to metric data in a CloudWatch metric.
        
                    - **metricName** *(string) --* 
        
                      The name of the CloudWatch metric.
        
                    - **metricNamespace** *(string) --* 
        
                      The namespace of the CloudWatch metric.
        
                    - **metricValue** *(string) --* 
        
                      The value to publish to the CloudWatch metric when a filter pattern matches a log event.
        
                    - **defaultValue** *(float) --* 
        
                      (Optional) The value to emit when a filter pattern does not match a log event. This value can be null.
        
                - **creationTime** *(integer) --* 
        
                  The creation time of the metric filter, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
        
                - **logGroupName** *(string) --* 
        
                  The name of the log group.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeSubscriptionFilters(Paginator):
    def paginate(self, logGroupName: str, filterNamePrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeSubscriptionFilters>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              logGroupName=\'string\',
              filterNamePrefix=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type logGroupName: string
        :param logGroupName: **[REQUIRED]** 
        
          The name of the log group.
        
        :type filterNamePrefix: string
        :param filterNamePrefix: 
        
          The prefix to match. If you don\'t specify a value, no prefix filter is applied.
        
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
                \'subscriptionFilters\': [
                    {
                        \'filterName\': \'string\',
                        \'logGroupName\': \'string\',
                        \'filterPattern\': \'string\',
                        \'destinationArn\': \'string\',
                        \'roleArn\': \'string\',
                        \'distribution\': \'Random\'|\'ByLogStream\',
                        \'creationTime\': 123
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **subscriptionFilters** *(list) --* 
        
              The subscription filters.
        
              - *(dict) --* 
        
                Represents a subscription filter.
        
                - **filterName** *(string) --* 
        
                  The name of the subscription filter.
        
                - **logGroupName** *(string) --* 
        
                  The name of the log group.
        
                - **filterPattern** *(string) --* 
        
                  A symbolic description of how CloudWatch Logs should interpret the data in each log event. For example, a log event may contain time stamps, IP addresses, strings, and so on. You use the filter pattern to specify what to look for in the log event message.
        
                - **destinationArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the destination.
        
                - **roleArn** *(string) --* 
        
                - **distribution** *(string) --* 
        
                  The method used to distribute log data to the destination, which can be either random or grouped by log stream.
        
                - **creationTime** *(integer) --* 
        
                  The creation time of the subscription filter, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class FilterLogEvents(Paginator):
    def paginate(self, logGroupName: str, logStreamNames: List = None, logStreamNamePrefix: str = None, startTime: int = None, endTime: int = None, filterPattern: str = None, interleaved: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/FilterLogEvents>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              logGroupName=\'string\',
              logStreamNames=[
                  \'string\',
              ],
              logStreamNamePrefix=\'string\',
              startTime=123,
              endTime=123,
              filterPattern=\'string\',
              interleaved=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type logGroupName: string
        :param logGroupName: **[REQUIRED]** 
        
          The name of the log group to search.
        
        :type logStreamNames: list
        :param logStreamNames: 
        
          Filters the results to only logs from the log streams in this list.
        
          If you specify a value for both ``logStreamNamePrefix`` and ``logStreamNames`` , but the value for ``logStreamNamePrefix`` does not match any log stream names specified in ``logStreamNames`` , the action returns an ``InvalidParameterException`` error.
        
          - *(string) --* 
        
        :type logStreamNamePrefix: string
        :param logStreamNamePrefix: 
        
          Filters the results to include only events from log streams that have names starting with this prefix.
        
          If you specify a value for both ``logStreamNamePrefix`` and ``logStreamNames`` , but the value for ``logStreamNamePrefix`` does not match any log stream names specified in ``logStreamNames`` , the action returns an ``InvalidParameterException`` error.
        
        :type startTime: integer
        :param startTime: 
        
          The start of the time range, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp before this time are not returned.
        
        :type endTime: integer
        :param endTime: 
        
          The end of the time range, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp later than this time are not returned.
        
        :type filterPattern: string
        :param filterPattern: 
        
          The filter pattern to use. For more information, see `Filter and Pattern Syntax <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html>`__ .
        
          If not provided, all the events are matched.
        
        :type interleaved: boolean
        :param interleaved: 
        
          If the value is true, the operation makes a best effort to provide responses that contain events from multiple log streams within the log group, interleaved in a single response. If the value is false, all the matched log events in the first log stream are searched first, then those in the next log stream, and so on. The default is false.
        
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
                \'events\': [
                    {
                        \'logStreamName\': \'string\',
                        \'timestamp\': 123,
                        \'message\': \'string\',
                        \'ingestionTime\': 123,
                        \'eventId\': \'string\'
                    },
                ],
                \'searchedLogStreams\': [
                    {
                        \'logStreamName\': \'string\',
                        \'searchedCompletely\': True|False
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **events** *(list) --* 
        
              The matched events.
        
              - *(dict) --* 
        
                Represents a matched event.
        
                - **logStreamName** *(string) --* 
        
                  The name of the log stream this event belongs to.
        
                - **timestamp** *(integer) --* 
        
                  The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
        
                - **message** *(string) --* 
        
                  The data contained in the log event.
        
                - **ingestionTime** *(integer) --* 
        
                  The time the event was ingested, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
        
                - **eventId** *(string) --* 
        
                  The ID of the event.
        
            - **searchedLogStreams** *(list) --* 
        
              Indicates which log streams have been searched and whether each has been searched completely.
        
              - *(dict) --* 
        
                Represents the search status of a log stream.
        
                - **logStreamName** *(string) --* 
        
                  The name of the log stream.
        
                - **searchedCompletely** *(boolean) --* 
        
                  Indicates whether all the events in this log stream were searched.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
