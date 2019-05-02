from typing import Dict
from typing import List
from datetime import datetime
from botocore.paginate import Paginator


class BatchGetTraces(Paginator):
    def paginate(self, TraceIds: List, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`XRay.Client.batch_get_traces`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/BatchGetTraces>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              TraceIds=[
                  'string',
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
                'Traces': [
                    {
                        'Id': 'string',
                        'Duration': 123.0,
                        'Segments': [
                            {
                                'Id': 'string',
                                'Document': 'string'
                            },
                        ]
                    },
                ],
                'UnprocessedTraceIds': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Traces** *(list) --* 
              Full traces for the specified requests.
              - *(dict) --* 
                A collection of segment documents with matching trace IDs.
                - **Id** *(string) --* 
                  The unique identifier for the request that generated the trace's segments and subsegments.
                - **Duration** *(float) --* 
                  The length of time in seconds between the start time of the root segment and the end time of the last segment that completed.
                - **Segments** *(list) --* 
                  Segment documents for the segments and subsegments that comprise the trace.
                  - *(dict) --* 
                    A segment from a trace that has been ingested by the X-Ray service. The segment can be compiled from documents uploaded with  PutTraceSegments , or an ``inferred`` segment for a downstream service, generated from a subsegment sent by the service that called it.
                    For the full segment document schema, see `AWS X-Ray Segment Documents <https://docs.aws.amazon.com/xray/latest/devguide/xray-api-segmentdocuments.html>`__ in the *AWS X-Ray Developer Guide* .
                    - **Id** *(string) --* 
                      The segment's ID.
                    - **Document** *(string) --* 
                      The segment document.
            - **UnprocessedTraceIds** *(list) --* 
              Trace IDs of requests that haven't been processed.
              - *(string) --* 
        :type TraceIds: list
        :param TraceIds: **[REQUIRED]**
          Specify the trace IDs of requests for which to retrieve segments.
          - *(string) --*
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


class GetGroups(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`XRay.Client.get_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Groups': [
                    {
                        'GroupName': 'string',
                        'GroupARN': 'string',
                        'FilterExpression': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Groups** *(list) --* 
              The collection of all active groups.
              - *(dict) --* 
                Details for a group without metadata.
                - **GroupName** *(string) --* 
                  The unique case-sensitive name of the group.
                - **GroupARN** *(string) --* 
                  The ARN of the group generated based on the GroupName.
                - **FilterExpression** *(string) --* 
                  The filter expression defining the parameters to include traces.
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


class GetSamplingRules(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`XRay.Client.get_sampling_rules`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetSamplingRules>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'SamplingRuleRecords': [
                    {
                        'SamplingRule': {
                            'RuleName': 'string',
                            'RuleARN': 'string',
                            'ResourceARN': 'string',
                            'Priority': 123,
                            'FixedRate': 123.0,
                            'ReservoirSize': 123,
                            'ServiceName': 'string',
                            'ServiceType': 'string',
                            'Host': 'string',
                            'HTTPMethod': 'string',
                            'URLPath': 'string',
                            'Version': 123,
                            'Attributes': {
                                'string': 'string'
                            }
                        },
                        'CreatedAt': datetime(2015, 1, 1),
                        'ModifiedAt': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **SamplingRuleRecords** *(list) --* 
              Rule definitions and metadata.
              - *(dict) --* 
                A  SamplingRule and its metadata.
                - **SamplingRule** *(dict) --* 
                  The sampling rule.
                  - **RuleName** *(string) --* 
                    The name of the sampling rule. Specify a rule by either name or ARN, but not both.
                  - **RuleARN** *(string) --* 
                    The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.
                  - **ResourceARN** *(string) --* 
                    Matches the ARN of the AWS resource on which the service runs.
                  - **Priority** *(integer) --* 
                    The priority of the sampling rule.
                  - **FixedRate** *(float) --* 
                    The percentage of matching requests to instrument, after the reservoir is exhausted.
                  - **ReservoirSize** *(integer) --* 
                    A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.
                  - **ServiceName** *(string) --* 
                    Matches the ``name`` that the service uses to identify itself in segments.
                  - **ServiceType** *(string) --* 
                    Matches the ``origin`` that the service uses to identify its type in segments.
                  - **Host** *(string) --* 
                    Matches the hostname from a request URL.
                  - **HTTPMethod** *(string) --* 
                    Matches the HTTP method of a request.
                  - **URLPath** *(string) --* 
                    Matches the path from a request URL.
                  - **Version** *(integer) --* 
                    The version of the sampling rule format (``1`` ).
                  - **Attributes** *(dict) --* 
                    Matches attributes derived from the request.
                    - *(string) --* 
                      - *(string) --* 
                - **CreatedAt** *(datetime) --* 
                  When the rule was created.
                - **ModifiedAt** *(datetime) --* 
                  When the rule was last modified.
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


class GetSamplingStatisticSummaries(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`XRay.Client.get_sampling_statistic_summaries`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetSamplingStatisticSummaries>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'SamplingStatisticSummaries': [
                    {
                        'RuleName': 'string',
                        'Timestamp': datetime(2015, 1, 1),
                        'RequestCount': 123,
                        'BorrowCount': 123,
                        'SampledCount': 123
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **SamplingStatisticSummaries** *(list) --* 
              Information about the number of requests instrumented for each sampling rule.
              - *(dict) --* 
                Aggregated request sampling data for a sampling rule across all services for a 10 second window.
                - **RuleName** *(string) --* 
                  The name of the sampling rule.
                - **Timestamp** *(datetime) --* 
                  The start time of the reporting window.
                - **RequestCount** *(integer) --* 
                  The number of requests that matched the rule.
                - **BorrowCount** *(integer) --* 
                  The number of requests recorded with borrowed reservoir quota.
                - **SampledCount** *(integer) --* 
                  The number of requests recorded.
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


class GetServiceGraph(Paginator):
    def paginate(self, StartTime: datetime, EndTime: datetime, GroupName: str = None, GroupARN: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`XRay.Client.get_service_graph`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetServiceGraph>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              GroupName='string',
              GroupARN='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'Services': [
                    {
                        'ReferenceId': 123,
                        'Name': 'string',
                        'Names': [
                            'string',
                        ],
                        'Root': True|False,
                        'AccountId': 'string',
                        'Type': 'string',
                        'State': 'string',
                        'StartTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'Edges': [
                            {
                                'ReferenceId': 123,
                                'StartTime': datetime(2015, 1, 1),
                                'EndTime': datetime(2015, 1, 1),
                                'SummaryStatistics': {
                                    'OkCount': 123,
                                    'ErrorStatistics': {
                                        'ThrottleCount': 123,
                                        'OtherCount': 123,
                                        'TotalCount': 123
                                    },
                                    'FaultStatistics': {
                                        'OtherCount': 123,
                                        'TotalCount': 123
                                    },
                                    'TotalCount': 123,
                                    'TotalResponseTime': 123.0
                                },
                                'ResponseTimeHistogram': [
                                    {
                                        'Value': 123.0,
                                        'Count': 123
                                    },
                                ],
                                'Aliases': [
                                    {
                                        'Name': 'string',
                                        'Names': [
                                            'string',
                                        ],
                                        'Type': 'string'
                                    },
                                ]
                            },
                        ],
                        'SummaryStatistics': {
                            'OkCount': 123,
                            'ErrorStatistics': {
                                'ThrottleCount': 123,
                                'OtherCount': 123,
                                'TotalCount': 123
                            },
                            'FaultStatistics': {
                                'OtherCount': 123,
                                'TotalCount': 123
                            },
                            'TotalCount': 123,
                            'TotalResponseTime': 123.0
                        },
                        'DurationHistogram': [
                            {
                                'Value': 123.0,
                                'Count': 123
                            },
                        ],
                        'ResponseTimeHistogram': [
                            {
                                'Value': 123.0,
                                'Count': 123
                            },
                        ]
                    },
                ],
                'ContainsOldGroupVersions': True|False,
            }
        
        **Response Structure**
          - *(dict) --* 
            - **StartTime** *(datetime) --* 
              The start of the time frame for which the graph was generated.
            - **EndTime** *(datetime) --* 
              The end of the time frame for which the graph was generated.
            - **Services** *(list) --* 
              The services that have processed a traced request during the specified time frame.
              - *(dict) --* 
                Information about an application that processed requests, users that made requests, or downstream services, resources and applications that an application used.
                - **ReferenceId** *(integer) --* 
                  Identifier for the service. Unique within the service map.
                - **Name** *(string) --* 
                  The canonical name of the service.
                - **Names** *(list) --* 
                  A list of names for the service, including the canonical name.
                  - *(string) --* 
                - **Root** *(boolean) --* 
                  Indicates that the service was the first service to process a request.
                - **AccountId** *(string) --* 
                  Identifier of the AWS account in which the service runs.
                - **Type** *(string) --* 
                  The type of service.
                  * AWS Resource - The type of an AWS resource. For example, ``AWS::EC2::Instance`` for a application running on Amazon EC2 or ``AWS::DynamoDB::Table`` for an Amazon DynamoDB table that the application used. 
                  * AWS Service - The type of an AWS service. For example, ``AWS::DynamoDB`` for downstream calls to Amazon DynamoDB that didn't target a specific table. 
                  * ``client`` - Represents the clients that sent requests to a root service. 
                  * ``remote`` - A downstream service of indeterminate type. 
                - **State** *(string) --* 
                  The service's state.
                - **StartTime** *(datetime) --* 
                  The start time of the first segment that the service generated.
                - **EndTime** *(datetime) --* 
                  The end time of the last segment that the service generated.
                - **Edges** *(list) --* 
                  Connections to downstream services.
                  - *(dict) --* 
                    Information about a connection between two services.
                    - **ReferenceId** *(integer) --* 
                      Identifier of the edge. Unique within a service map.
                    - **StartTime** *(datetime) --* 
                      The start time of the first segment on the edge.
                    - **EndTime** *(datetime) --* 
                      The end time of the last segment on the edge.
                    - **SummaryStatistics** *(dict) --* 
                      Response statistics for segments on the edge.
                      - **OkCount** *(integer) --* 
                        The number of requests that completed with a 2xx Success status code.
                      - **ErrorStatistics** *(dict) --* 
                        Information about requests that failed with a 4xx Client Error status code.
                        - **ThrottleCount** *(integer) --* 
                          The number of requests that failed with a 419 throttling status code.
                        - **OtherCount** *(integer) --* 
                          The number of requests that failed with untracked 4xx Client Error status codes.
                        - **TotalCount** *(integer) --* 
                          The total number of requests that failed with a 4xx Client Error status code.
                      - **FaultStatistics** *(dict) --* 
                        Information about requests that failed with a 5xx Server Error status code.
                        - **OtherCount** *(integer) --* 
                          The number of requests that failed with untracked 5xx Server Error status codes.
                        - **TotalCount** *(integer) --* 
                          The total number of requests that failed with a 5xx Server Error status code.
                      - **TotalCount** *(integer) --* 
                        The total number of completed requests.
                      - **TotalResponseTime** *(float) --* 
                        The aggregate response time of completed requests.
                    - **ResponseTimeHistogram** *(list) --* 
                      A histogram that maps the spread of client response times on an edge.
                      - *(dict) --* 
                        An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.
                        - **Value** *(float) --* 
                          The value of the entry.
                        - **Count** *(integer) --* 
                          The prevalence of the entry.
                    - **Aliases** *(list) --* 
                      Aliases for the edge.
                      - *(dict) --* 
                        An alias for an edge.
                        - **Name** *(string) --* 
                          The canonical name of the alias.
                        - **Names** *(list) --* 
                          A list of names for the alias, including the canonical name.
                          - *(string) --* 
                        - **Type** *(string) --* 
                          The type of the alias.
                - **SummaryStatistics** *(dict) --* 
                  Aggregated statistics for the service.
                  - **OkCount** *(integer) --* 
                    The number of requests that completed with a 2xx Success status code.
                  - **ErrorStatistics** *(dict) --* 
                    Information about requests that failed with a 4xx Client Error status code.
                    - **ThrottleCount** *(integer) --* 
                      The number of requests that failed with a 419 throttling status code.
                    - **OtherCount** *(integer) --* 
                      The number of requests that failed with untracked 4xx Client Error status codes.
                    - **TotalCount** *(integer) --* 
                      The total number of requests that failed with a 4xx Client Error status code.
                  - **FaultStatistics** *(dict) --* 
                    Information about requests that failed with a 5xx Server Error status code.
                    - **OtherCount** *(integer) --* 
                      The number of requests that failed with untracked 5xx Server Error status codes.
                    - **TotalCount** *(integer) --* 
                      The total number of requests that failed with a 5xx Server Error status code.
                  - **TotalCount** *(integer) --* 
                    The total number of completed requests.
                  - **TotalResponseTime** *(float) --* 
                    The aggregate response time of completed requests.
                - **DurationHistogram** *(list) --* 
                  A histogram that maps the spread of service durations.
                  - *(dict) --* 
                    An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.
                    - **Value** *(float) --* 
                      The value of the entry.
                    - **Count** *(integer) --* 
                      The prevalence of the entry.
                - **ResponseTimeHistogram** *(list) --* 
                  A histogram that maps the spread of service response times.
                  - *(dict) --* 
                    An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.
                    - **Value** *(float) --* 
                      The value of the entry.
                    - **Count** *(integer) --* 
                      The prevalence of the entry.
            - **ContainsOldGroupVersions** *(boolean) --* 
              A flag indicating whether the group's filter expression has been consistent, or if the returned service graph may show traces from an older version of the group's filter expression.
        :type StartTime: datetime
        :param StartTime: **[REQUIRED]**
          The start of the time frame for which to generate a graph.
        :type EndTime: datetime
        :param EndTime: **[REQUIRED]**
          The end of the timeframe for which to generate a graph.
        :type GroupName: string
        :param GroupName:
          The name of a group to generate a graph based on.
        :type GroupARN: string
        :param GroupARN:
          The ARN of a group to generate a graph based on.
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


class GetTimeSeriesServiceStatistics(Paginator):
    def paginate(self, StartTime: datetime, EndTime: datetime, GroupName: str = None, GroupARN: str = None, EntitySelectorExpression: str = None, Period: int = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`XRay.Client.get_time_series_service_statistics`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetTimeSeriesServiceStatistics>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              GroupName='string',
              GroupARN='string',
              EntitySelectorExpression='string',
              Period=123,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'TimeSeriesServiceStatistics': [
                    {
                        'Timestamp': datetime(2015, 1, 1),
                        'EdgeSummaryStatistics': {
                            'OkCount': 123,
                            'ErrorStatistics': {
                                'ThrottleCount': 123,
                                'OtherCount': 123,
                                'TotalCount': 123
                            },
                            'FaultStatistics': {
                                'OtherCount': 123,
                                'TotalCount': 123
                            },
                            'TotalCount': 123,
                            'TotalResponseTime': 123.0
                        },
                        'ServiceSummaryStatistics': {
                            'OkCount': 123,
                            'ErrorStatistics': {
                                'ThrottleCount': 123,
                                'OtherCount': 123,
                                'TotalCount': 123
                            },
                            'FaultStatistics': {
                                'OtherCount': 123,
                                'TotalCount': 123
                            },
                            'TotalCount': 123,
                            'TotalResponseTime': 123.0
                        },
                        'ResponseTimeHistogram': [
                            {
                                'Value': 123.0,
                                'Count': 123
                            },
                        ]
                    },
                ],
                'ContainsOldGroupVersions': True|False,
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TimeSeriesServiceStatistics** *(list) --* 
              The collection of statistics.
              - *(dict) --* 
                A list of TimeSeriesStatistic structures.
                - **Timestamp** *(datetime) --* 
                  Timestamp of the window for which statistics are aggregated.
                - **EdgeSummaryStatistics** *(dict) --* 
                  Response statistics for an edge.
                  - **OkCount** *(integer) --* 
                    The number of requests that completed with a 2xx Success status code.
                  - **ErrorStatistics** *(dict) --* 
                    Information about requests that failed with a 4xx Client Error status code.
                    - **ThrottleCount** *(integer) --* 
                      The number of requests that failed with a 419 throttling status code.
                    - **OtherCount** *(integer) --* 
                      The number of requests that failed with untracked 4xx Client Error status codes.
                    - **TotalCount** *(integer) --* 
                      The total number of requests that failed with a 4xx Client Error status code.
                  - **FaultStatistics** *(dict) --* 
                    Information about requests that failed with a 5xx Server Error status code.
                    - **OtherCount** *(integer) --* 
                      The number of requests that failed with untracked 5xx Server Error status codes.
                    - **TotalCount** *(integer) --* 
                      The total number of requests that failed with a 5xx Server Error status code.
                  - **TotalCount** *(integer) --* 
                    The total number of completed requests.
                  - **TotalResponseTime** *(float) --* 
                    The aggregate response time of completed requests.
                - **ServiceSummaryStatistics** *(dict) --* 
                  Response statistics for a service.
                  - **OkCount** *(integer) --* 
                    The number of requests that completed with a 2xx Success status code.
                  - **ErrorStatistics** *(dict) --* 
                    Information about requests that failed with a 4xx Client Error status code.
                    - **ThrottleCount** *(integer) --* 
                      The number of requests that failed with a 419 throttling status code.
                    - **OtherCount** *(integer) --* 
                      The number of requests that failed with untracked 4xx Client Error status codes.
                    - **TotalCount** *(integer) --* 
                      The total number of requests that failed with a 4xx Client Error status code.
                  - **FaultStatistics** *(dict) --* 
                    Information about requests that failed with a 5xx Server Error status code.
                    - **OtherCount** *(integer) --* 
                      The number of requests that failed with untracked 5xx Server Error status codes.
                    - **TotalCount** *(integer) --* 
                      The total number of requests that failed with a 5xx Server Error status code.
                  - **TotalCount** *(integer) --* 
                    The total number of completed requests.
                  - **TotalResponseTime** *(float) --* 
                    The aggregate response time of completed requests.
                - **ResponseTimeHistogram** *(list) --* 
                  The response time histogram for the selected entities.
                  - *(dict) --* 
                    An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.
                    - **Value** *(float) --* 
                      The value of the entry.
                    - **Count** *(integer) --* 
                      The prevalence of the entry.
            - **ContainsOldGroupVersions** *(boolean) --* 
              A flag indicating whether or not a group's filter expression has been consistent, or if a returned aggregation may show statistics from an older version of the group's filter expression.
        :type StartTime: datetime
        :param StartTime: **[REQUIRED]**
          The start of the time frame for which to aggregate statistics.
        :type EndTime: datetime
        :param EndTime: **[REQUIRED]**
          The end of the time frame for which to aggregate statistics.
        :type GroupName: string
        :param GroupName:
          The case-sensitive name of the group for which to pull statistics from.
        :type GroupARN: string
        :param GroupARN:
          The ARN of the group for which to pull statistics from.
        :type EntitySelectorExpression: string
        :param EntitySelectorExpression:
          A filter expression defining entities that will be aggregated for statistics. Supports ID, service, and edge functions. If no selector expression is specified, edge statistics are returned.
        :type Period: integer
        :param Period:
          Aggregation period in seconds.
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


class GetTraceGraph(Paginator):
    def paginate(self, TraceIds: List, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`XRay.Client.get_trace_graph`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetTraceGraph>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              TraceIds=[
                  'string',
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
                'Services': [
                    {
                        'ReferenceId': 123,
                        'Name': 'string',
                        'Names': [
                            'string',
                        ],
                        'Root': True|False,
                        'AccountId': 'string',
                        'Type': 'string',
                        'State': 'string',
                        'StartTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'Edges': [
                            {
                                'ReferenceId': 123,
                                'StartTime': datetime(2015, 1, 1),
                                'EndTime': datetime(2015, 1, 1),
                                'SummaryStatistics': {
                                    'OkCount': 123,
                                    'ErrorStatistics': {
                                        'ThrottleCount': 123,
                                        'OtherCount': 123,
                                        'TotalCount': 123
                                    },
                                    'FaultStatistics': {
                                        'OtherCount': 123,
                                        'TotalCount': 123
                                    },
                                    'TotalCount': 123,
                                    'TotalResponseTime': 123.0
                                },
                                'ResponseTimeHistogram': [
                                    {
                                        'Value': 123.0,
                                        'Count': 123
                                    },
                                ],
                                'Aliases': [
                                    {
                                        'Name': 'string',
                                        'Names': [
                                            'string',
                                        ],
                                        'Type': 'string'
                                    },
                                ]
                            },
                        ],
                        'SummaryStatistics': {
                            'OkCount': 123,
                            'ErrorStatistics': {
                                'ThrottleCount': 123,
                                'OtherCount': 123,
                                'TotalCount': 123
                            },
                            'FaultStatistics': {
                                'OtherCount': 123,
                                'TotalCount': 123
                            },
                            'TotalCount': 123,
                            'TotalResponseTime': 123.0
                        },
                        'DurationHistogram': [
                            {
                                'Value': 123.0,
                                'Count': 123
                            },
                        ],
                        'ResponseTimeHistogram': [
                            {
                                'Value': 123.0,
                                'Count': 123
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Services** *(list) --* 
              The services that have processed one of the specified requests.
              - *(dict) --* 
                Information about an application that processed requests, users that made requests, or downstream services, resources and applications that an application used.
                - **ReferenceId** *(integer) --* 
                  Identifier for the service. Unique within the service map.
                - **Name** *(string) --* 
                  The canonical name of the service.
                - **Names** *(list) --* 
                  A list of names for the service, including the canonical name.
                  - *(string) --* 
                - **Root** *(boolean) --* 
                  Indicates that the service was the first service to process a request.
                - **AccountId** *(string) --* 
                  Identifier of the AWS account in which the service runs.
                - **Type** *(string) --* 
                  The type of service.
                  * AWS Resource - The type of an AWS resource. For example, ``AWS::EC2::Instance`` for a application running on Amazon EC2 or ``AWS::DynamoDB::Table`` for an Amazon DynamoDB table that the application used. 
                  * AWS Service - The type of an AWS service. For example, ``AWS::DynamoDB`` for downstream calls to Amazon DynamoDB that didn't target a specific table. 
                  * ``client`` - Represents the clients that sent requests to a root service. 
                  * ``remote`` - A downstream service of indeterminate type. 
                - **State** *(string) --* 
                  The service's state.
                - **StartTime** *(datetime) --* 
                  The start time of the first segment that the service generated.
                - **EndTime** *(datetime) --* 
                  The end time of the last segment that the service generated.
                - **Edges** *(list) --* 
                  Connections to downstream services.
                  - *(dict) --* 
                    Information about a connection between two services.
                    - **ReferenceId** *(integer) --* 
                      Identifier of the edge. Unique within a service map.
                    - **StartTime** *(datetime) --* 
                      The start time of the first segment on the edge.
                    - **EndTime** *(datetime) --* 
                      The end time of the last segment on the edge.
                    - **SummaryStatistics** *(dict) --* 
                      Response statistics for segments on the edge.
                      - **OkCount** *(integer) --* 
                        The number of requests that completed with a 2xx Success status code.
                      - **ErrorStatistics** *(dict) --* 
                        Information about requests that failed with a 4xx Client Error status code.
                        - **ThrottleCount** *(integer) --* 
                          The number of requests that failed with a 419 throttling status code.
                        - **OtherCount** *(integer) --* 
                          The number of requests that failed with untracked 4xx Client Error status codes.
                        - **TotalCount** *(integer) --* 
                          The total number of requests that failed with a 4xx Client Error status code.
                      - **FaultStatistics** *(dict) --* 
                        Information about requests that failed with a 5xx Server Error status code.
                        - **OtherCount** *(integer) --* 
                          The number of requests that failed with untracked 5xx Server Error status codes.
                        - **TotalCount** *(integer) --* 
                          The total number of requests that failed with a 5xx Server Error status code.
                      - **TotalCount** *(integer) --* 
                        The total number of completed requests.
                      - **TotalResponseTime** *(float) --* 
                        The aggregate response time of completed requests.
                    - **ResponseTimeHistogram** *(list) --* 
                      A histogram that maps the spread of client response times on an edge.
                      - *(dict) --* 
                        An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.
                        - **Value** *(float) --* 
                          The value of the entry.
                        - **Count** *(integer) --* 
                          The prevalence of the entry.
                    - **Aliases** *(list) --* 
                      Aliases for the edge.
                      - *(dict) --* 
                        An alias for an edge.
                        - **Name** *(string) --* 
                          The canonical name of the alias.
                        - **Names** *(list) --* 
                          A list of names for the alias, including the canonical name.
                          - *(string) --* 
                        - **Type** *(string) --* 
                          The type of the alias.
                - **SummaryStatistics** *(dict) --* 
                  Aggregated statistics for the service.
                  - **OkCount** *(integer) --* 
                    The number of requests that completed with a 2xx Success status code.
                  - **ErrorStatistics** *(dict) --* 
                    Information about requests that failed with a 4xx Client Error status code.
                    - **ThrottleCount** *(integer) --* 
                      The number of requests that failed with a 419 throttling status code.
                    - **OtherCount** *(integer) --* 
                      The number of requests that failed with untracked 4xx Client Error status codes.
                    - **TotalCount** *(integer) --* 
                      The total number of requests that failed with a 4xx Client Error status code.
                  - **FaultStatistics** *(dict) --* 
                    Information about requests that failed with a 5xx Server Error status code.
                    - **OtherCount** *(integer) --* 
                      The number of requests that failed with untracked 5xx Server Error status codes.
                    - **TotalCount** *(integer) --* 
                      The total number of requests that failed with a 5xx Server Error status code.
                  - **TotalCount** *(integer) --* 
                    The total number of completed requests.
                  - **TotalResponseTime** *(float) --* 
                    The aggregate response time of completed requests.
                - **DurationHistogram** *(list) --* 
                  A histogram that maps the spread of service durations.
                  - *(dict) --* 
                    An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.
                    - **Value** *(float) --* 
                      The value of the entry.
                    - **Count** *(integer) --* 
                      The prevalence of the entry.
                - **ResponseTimeHistogram** *(list) --* 
                  A histogram that maps the spread of service response times.
                  - *(dict) --* 
                    An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.
                    - **Value** *(float) --* 
                      The value of the entry.
                    - **Count** *(integer) --* 
                      The prevalence of the entry.
        :type TraceIds: list
        :param TraceIds: **[REQUIRED]**
          Trace IDs of requests for which to generate a service graph.
          - *(string) --*
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


class GetTraceSummaries(Paginator):
    def paginate(self, StartTime: datetime, EndTime: datetime, TimeRangeType: str = None, Sampling: bool = None, SamplingStrategy: Dict = None, FilterExpression: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`XRay.Client.get_trace_summaries`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetTraceSummaries>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              TimeRangeType='TraceId'|'Event',
              Sampling=True|False,
              SamplingStrategy={
                  'Name': 'PartialScan'|'FixedRate',
                  'Value': 123.0
              },
              FilterExpression='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'TraceSummaries': [
                    {
                        'Id': 'string',
                        'Duration': 123.0,
                        'ResponseTime': 123.0,
                        'HasFault': True|False,
                        'HasError': True|False,
                        'HasThrottle': True|False,
                        'IsPartial': True|False,
                        'Http': {
                            'HttpURL': 'string',
                            'HttpStatus': 123,
                            'HttpMethod': 'string',
                            'UserAgent': 'string',
                            'ClientIp': 'string'
                        },
                        'Annotations': {
                            'string': [
                                {
                                    'AnnotationValue': {
                                        'NumberValue': 123.0,
                                        'BooleanValue': True|False,
                                        'StringValue': 'string'
                                    },
                                    'ServiceIds': [
                                        {
                                            'Name': 'string',
                                            'Names': [
                                                'string',
                                            ],
                                            'AccountId': 'string',
                                            'Type': 'string'
                                        },
                                    ]
                                },
                            ]
                        },
                        'Users': [
                            {
                                'UserName': 'string',
                                'ServiceIds': [
                                    {
                                        'Name': 'string',
                                        'Names': [
                                            'string',
                                        ],
                                        'AccountId': 'string',
                                        'Type': 'string'
                                    },
                                ]
                            },
                        ],
                        'ServiceIds': [
                            {
                                'Name': 'string',
                                'Names': [
                                    'string',
                                ],
                                'AccountId': 'string',
                                'Type': 'string'
                            },
                        ],
                        'ResourceARNs': [
                            {
                                'ARN': 'string'
                            },
                        ],
                        'InstanceIds': [
                            {
                                'Id': 'string'
                            },
                        ],
                        'AvailabilityZones': [
                            {
                                'Name': 'string'
                            },
                        ],
                        'EntryPoint': {
                            'Name': 'string',
                            'Names': [
                                'string',
                            ],
                            'AccountId': 'string',
                            'Type': 'string'
                        },
                        'FaultRootCauses': [
                            {
                                'Services': [
                                    {
                                        'Name': 'string',
                                        'Names': [
                                            'string',
                                        ],
                                        'Type': 'string',
                                        'AccountId': 'string',
                                        'EntityPath': [
                                            {
                                                'Name': 'string',
                                                'Exceptions': [
                                                    {
                                                        'Name': 'string',
                                                        'Message': 'string'
                                                    },
                                                ],
                                                'Remote': True|False
                                            },
                                        ],
                                        'Inferred': True|False
                                    },
                                ]
                            },
                        ],
                        'ErrorRootCauses': [
                            {
                                'Services': [
                                    {
                                        'Name': 'string',
                                        'Names': [
                                            'string',
                                        ],
                                        'Type': 'string',
                                        'AccountId': 'string',
                                        'EntityPath': [
                                            {
                                                'Name': 'string',
                                                'Exceptions': [
                                                    {
                                                        'Name': 'string',
                                                        'Message': 'string'
                                                    },
                                                ],
                                                'Remote': True|False
                                            },
                                        ],
                                        'Inferred': True|False
                                    },
                                ]
                            },
                        ],
                        'ResponseTimeRootCauses': [
                            {
                                'Services': [
                                    {
                                        'Name': 'string',
                                        'Names': [
                                            'string',
                                        ],
                                        'Type': 'string',
                                        'AccountId': 'string',
                                        'EntityPath': [
                                            {
                                                'Name': 'string',
                                                'Coverage': 123.0,
                                                'Remote': True|False
                                            },
                                        ],
                                        'Inferred': True|False
                                    },
                                ]
                            },
                        ],
                        'Revision': 123,
                        'MatchedEventTime': datetime(2015, 1, 1)
                    },
                ],
                'ApproximateTime': datetime(2015, 1, 1),
                'TracesProcessedCount': 123,
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TraceSummaries** *(list) --* 
              Trace IDs and metadata for traces that were found in the specified time frame.
              - *(dict) --* 
                Metadata generated from the segment documents in a trace.
                - **Id** *(string) --* 
                  The unique identifier for the request that generated the trace's segments and subsegments.
                - **Duration** *(float) --* 
                  The length of time in seconds between the start time of the root segment and the end time of the last segment that completed.
                - **ResponseTime** *(float) --* 
                  The length of time in seconds between the start and end times of the root segment. If the service performs work asynchronously, the response time measures the time before the response is sent to the user, while the duration measures the amount of time before the last traced activity completes.
                - **HasFault** *(boolean) --* 
                  One or more of the segment documents has a 500 series error.
                - **HasError** *(boolean) --* 
                  One or more of the segment documents has a 400 series error.
                - **HasThrottle** *(boolean) --* 
                  One or more of the segment documents has a 429 throttling error.
                - **IsPartial** *(boolean) --* 
                  One or more of the segment documents is in progress.
                - **Http** *(dict) --* 
                  Information about the HTTP request served by the trace.
                  - **HttpURL** *(string) --* 
                    The request URL.
                  - **HttpStatus** *(integer) --* 
                    The response status.
                  - **HttpMethod** *(string) --* 
                    The request method.
                  - **UserAgent** *(string) --* 
                    The request's user agent string.
                  - **ClientIp** *(string) --* 
                    The IP address of the requestor.
                - **Annotations** *(dict) --* 
                  Annotations from the trace's segment documents.
                  - *(string) --* 
                    - *(list) --* 
                      - *(dict) --* 
                        Information about a segment annotation.
                        - **AnnotationValue** *(dict) --* 
                          Values of the annotation.
                          - **NumberValue** *(float) --* 
                            Value for a Number annotation.
                          - **BooleanValue** *(boolean) --* 
                            Value for a Boolean annotation.
                          - **StringValue** *(string) --* 
                            Value for a String annotation.
                        - **ServiceIds** *(list) --* 
                          Services to which the annotation applies.
                          - *(dict) --* 
                            - **Name** *(string) --* 
                            - **Names** *(list) --* 
                              - *(string) --* 
                            - **AccountId** *(string) --* 
                            - **Type** *(string) --* 
                - **Users** *(list) --* 
                  Users from the trace's segment documents.
                  - *(dict) --* 
                    Information about a user recorded in segment documents.
                    - **UserName** *(string) --* 
                      The user's name.
                    - **ServiceIds** *(list) --* 
                      Services that the user's request hit.
                      - *(dict) --* 
                        - **Name** *(string) --* 
                        - **Names** *(list) --* 
                          - *(string) --* 
                        - **AccountId** *(string) --* 
                        - **Type** *(string) --* 
                - **ServiceIds** *(list) --* 
                  Service IDs from the trace's segment documents.
                  - *(dict) --* 
                    - **Name** *(string) --* 
                    - **Names** *(list) --* 
                      - *(string) --* 
                    - **AccountId** *(string) --* 
                    - **Type** *(string) --* 
                - **ResourceARNs** *(list) --* 
                  A list of resource ARNs for any resource corresponding to the trace segments.
                  - *(dict) --* 
                    A list of resources ARNs corresponding to the segments in a trace.
                    - **ARN** *(string) --* 
                      The ARN of a corresponding resource.
                - **InstanceIds** *(list) --* 
                  A list of EC2 instance IDs for any instance corresponding to the trace segments.
                  - *(dict) --* 
                    A list of EC2 instance IDs corresponding to the segments in a trace. 
                    - **Id** *(string) --* 
                      The ID of a corresponding EC2 instance.
                - **AvailabilityZones** *(list) --* 
                  A list of availability zones for any zone corresponding to the trace segments.
                  - *(dict) --* 
                    A list of availability zones corresponding to the segments in a trace.
                    - **Name** *(string) --* 
                      The name of a corresponding availability zone.
                - **EntryPoint** *(dict) --* 
                  The root of a trace.
                  - **Name** *(string) --* 
                  - **Names** *(list) --* 
                    - *(string) --* 
                  - **AccountId** *(string) --* 
                  - **Type** *(string) --* 
                - **FaultRootCauses** *(list) --* 
                  A collection of FaultRootCause structures corresponding to the the trace segments.
                  - *(dict) --* 
                    The root cause information for a trace summary fault.
                    - **Services** *(list) --* 
                      A list of corresponding services. A service identifies a segment and it contains a name, account ID, type, and inferred flag.
                      - *(dict) --* 
                        A collection of fields identifying the services in a trace summary fault.
                        - **Name** *(string) --* 
                          The service name.
                        - **Names** *(list) --* 
                          A collection of associated service names.
                          - *(string) --* 
                        - **Type** *(string) --* 
                          The type associated to the service.
                        - **AccountId** *(string) --* 
                          The account ID associated to the service.
                        - **EntityPath** *(list) --* 
                          The path of root cause entities found on the service. 
                          - *(dict) --* 
                            A collection of segments and corresponding subsegments associated to a trace summary fault error.
                            - **Name** *(string) --* 
                              The name of the entity.
                            - **Exceptions** *(list) --* 
                              The types and messages of the exceptions.
                              - *(dict) --* 
                                The exception associated with a root cause.
                                - **Name** *(string) --* 
                                  The name of the exception.
                                - **Message** *(string) --* 
                                  The message of the exception.
                            - **Remote** *(boolean) --* 
                              A flag that denotes a remote subsegment.
                        - **Inferred** *(boolean) --* 
                          A Boolean value indicating if the service is inferred from the trace.
                - **ErrorRootCauses** *(list) --* 
                  A collection of ErrorRootCause structures corresponding to the trace segments.
                  - *(dict) --* 
                    The root cause of a trace summary error.
                    - **Services** *(list) --* 
                      A list of services corresponding to an error. A service identifies a segment and it contains a name, account ID, type, and inferred flag.
                      - *(dict) --* 
                        A collection of fields identifying the services in a trace summary error.
                        - **Name** *(string) --* 
                          The service name.
                        - **Names** *(list) --* 
                          A collection of associated service names.
                          - *(string) --* 
                        - **Type** *(string) --* 
                          The type associated to the service.
                        - **AccountId** *(string) --* 
                          The account ID associated to the service.
                        - **EntityPath** *(list) --* 
                          The path of root cause entities found on the service. 
                          - *(dict) --* 
                            A collection of segments and corresponding subsegments associated to a trace summary error.
                            - **Name** *(string) --* 
                              The name of the entity.
                            - **Exceptions** *(list) --* 
                              The types and messages of the exceptions.
                              - *(dict) --* 
                                The exception associated with a root cause.
                                - **Name** *(string) --* 
                                  The name of the exception.
                                - **Message** *(string) --* 
                                  The message of the exception.
                            - **Remote** *(boolean) --* 
                              A flag that denotes a remote subsegment.
                        - **Inferred** *(boolean) --* 
                          A Boolean value indicating if the service is inferred from the trace.
                - **ResponseTimeRootCauses** *(list) --* 
                  A collection of ResponseTimeRootCause structures corresponding to the trace segments.
                  - *(dict) --* 
                    The root cause information for a response time warning.
                    - **Services** *(list) --* 
                      A list of corresponding services. A service identifies a segment and contains a name, account ID, type, and inferred flag.
                      - *(dict) --* 
                        A collection of fields identifying the service in a response time warning.
                        - **Name** *(string) --* 
                          The service name.
                        - **Names** *(list) --* 
                          A collection of associated service names.
                          - *(string) --* 
                        - **Type** *(string) --* 
                          The type associated to the service.
                        - **AccountId** *(string) --* 
                          The account ID associated to the service.
                        - **EntityPath** *(list) --* 
                          The path of root cause entities found on the service. 
                          - *(dict) --* 
                            A collection of segments and corresponding subsegments associated to a response time warning.
                            - **Name** *(string) --* 
                              The name of the entity.
                            - **Coverage** *(float) --* 
                              The types and messages of the exceptions.
                            - **Remote** *(boolean) --* 
                              A flag that denotes a remote subsegment.
                        - **Inferred** *(boolean) --* 
                          A Boolean value indicating if the service is inferred from the trace.
                - **Revision** *(integer) --* 
                  The revision number of a trace.
                - **MatchedEventTime** *(datetime) --* 
                  The matched time stamp of a defined event.
            - **ApproximateTime** *(datetime) --* 
              The start time of this page of results.
            - **TracesProcessedCount** *(integer) --* 
              The total number of traces processed, including traces that did not match the specified filter expression.
        :type StartTime: datetime
        :param StartTime: **[REQUIRED]**
          The start of the time frame for which to retrieve traces.
        :type EndTime: datetime
        :param EndTime: **[REQUIRED]**
          The end of the time frame for which to retrieve traces.
        :type TimeRangeType: string
        :param TimeRangeType:
          A parameter to indicate whether to query trace summaries by TraceId or Event time.
        :type Sampling: boolean
        :param Sampling:
          Set to ``true`` to get summaries for only a subset of available traces.
        :type SamplingStrategy: dict
        :param SamplingStrategy:
          A paramater to indicate whether to enable sampling on trace summaries. Input parameters are Name and Value.
          - **Name** *(string) --*
            The name of a sampling rule.
          - **Value** *(float) --*
            The value of a sampling rule.
        :type FilterExpression: string
        :param FilterExpression:
          Specify a filter expression to retrieve trace summaries for services or requests that meet certain requirements.
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
