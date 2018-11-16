from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class BatchGetTraces(Paginator):
    def paginate(self, TraceIds: List, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/BatchGetTraces>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              TraceIds=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Traces\': [
                    {
                        \'Id\': \'string\',
                        \'Duration\': 123.0,
                        \'Segments\': [
                            {
                                \'Id\': \'string\',
                                \'Document\': \'string\'
                            },
                        ]
                    },
                ],
                \'UnprocessedTraceIds\': [
                    \'string\',
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Traces** *(list) --* 
        
              Full traces for the specified requests.
        
              - *(dict) --* 
        
                A collection of segment documents with matching trace IDs.
        
                - **Id** *(string) --* 
        
                  The unique identifier for the request that generated the trace\'s segments and subsegments.
        
                - **Duration** *(float) --* 
        
                  The length of time in seconds between the start time of the root segment and the end time of the last segment that completed.
        
                - **Segments** *(list) --* 
        
                  Segment documents for the segments and subsegments that comprise the trace.
        
                  - *(dict) --* 
        
                    A segment from a trace that has been ingested by the X-Ray service. The segment can be compiled from documents uploaded with  PutTraceSegments , or an ``inferred`` segment for a downstream service, generated from a subsegment sent by the service that called it.
        
                    For the full segment document schema, see `AWS X-Ray Segment Documents <https://docs.aws.amazon.com/xray/latest/devguide/xray-api-segmentdocuments.html>`__ in the *AWS X-Ray Developer Guide* .
        
                    - **Id** *(string) --* 
        
                      The segment\'s ID.
        
                    - **Document** *(string) --* 
        
                      The segment document.
        
            - **UnprocessedTraceIds** *(list) --* 
        
              Trace IDs of requests that haven\'t been processed.
        
              - *(string) --* 
          
        """
        pass


class GetServiceGraph(Paginator):
    def paginate(self, StartTime: datetime, EndTime: datetime, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetServiceGraph>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type StartTime: datetime
        :param StartTime: **[REQUIRED]** 
        
          The start of the time frame for which to generate a graph.
        
        :type EndTime: datetime
        :param EndTime: **[REQUIRED]** 
        
          The end of the time frame for which to generate a graph.
        
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
                \'StartTime\': datetime(2015, 1, 1),
                \'EndTime\': datetime(2015, 1, 1),
                \'Services\': [
                    {
                        \'ReferenceId\': 123,
                        \'Name\': \'string\',
                        \'Names\': [
                            \'string\',
                        ],
                        \'Root\': True|False,
                        \'AccountId\': \'string\',
                        \'Type\': \'string\',
                        \'State\': \'string\',
                        \'StartTime\': datetime(2015, 1, 1),
                        \'EndTime\': datetime(2015, 1, 1),
                        \'Edges\': [
                            {
                                \'ReferenceId\': 123,
                                \'StartTime\': datetime(2015, 1, 1),
                                \'EndTime\': datetime(2015, 1, 1),
                                \'SummaryStatistics\': {
                                    \'OkCount\': 123,
                                    \'ErrorStatistics\': {
                                        \'ThrottleCount\': 123,
                                        \'OtherCount\': 123,
                                        \'TotalCount\': 123
                                    },
                                    \'FaultStatistics\': {
                                        \'OtherCount\': 123,
                                        \'TotalCount\': 123
                                    },
                                    \'TotalCount\': 123,
                                    \'TotalResponseTime\': 123.0
                                },
                                \'ResponseTimeHistogram\': [
                                    {
                                        \'Value\': 123.0,
                                        \'Count\': 123
                                    },
                                ],
                                \'Aliases\': [
                                    {
                                        \'Name\': \'string\',
                                        \'Names\': [
                                            \'string\',
                                        ],
                                        \'Type\': \'string\'
                                    },
                                ]
                            },
                        ],
                        \'SummaryStatistics\': {
                            \'OkCount\': 123,
                            \'ErrorStatistics\': {
                                \'ThrottleCount\': 123,
                                \'OtherCount\': 123,
                                \'TotalCount\': 123
                            },
                            \'FaultStatistics\': {
                                \'OtherCount\': 123,
                                \'TotalCount\': 123
                            },
                            \'TotalCount\': 123,
                            \'TotalResponseTime\': 123.0
                        },
                        \'DurationHistogram\': [
                            {
                                \'Value\': 123.0,
                                \'Count\': 123
                            },
                        ],
                        \'ResponseTimeHistogram\': [
                            {
                                \'Value\': 123.0,
                                \'Count\': 123
                            },
                        ]
                    },
                ],
                
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
                   
                  * AWS Service - The type of an AWS service. For example, ``AWS::DynamoDB`` for downstream calls to Amazon DynamoDB that didn\'t target a specific table. 
                   
                  * ``client`` - Represents the clients that sent requests to a root service. 
                   
                  * ``remote`` - A downstream service of indeterminate type. 
                   
                - **State** *(string) --* 
        
                  The service\'s state.
        
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
        
        """
        pass


class GetTraceGraph(Paginator):
    def paginate(self, TraceIds: List, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetTraceGraph>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              TraceIds=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Services\': [
                    {
                        \'ReferenceId\': 123,
                        \'Name\': \'string\',
                        \'Names\': [
                            \'string\',
                        ],
                        \'Root\': True|False,
                        \'AccountId\': \'string\',
                        \'Type\': \'string\',
                        \'State\': \'string\',
                        \'StartTime\': datetime(2015, 1, 1),
                        \'EndTime\': datetime(2015, 1, 1),
                        \'Edges\': [
                            {
                                \'ReferenceId\': 123,
                                \'StartTime\': datetime(2015, 1, 1),
                                \'EndTime\': datetime(2015, 1, 1),
                                \'SummaryStatistics\': {
                                    \'OkCount\': 123,
                                    \'ErrorStatistics\': {
                                        \'ThrottleCount\': 123,
                                        \'OtherCount\': 123,
                                        \'TotalCount\': 123
                                    },
                                    \'FaultStatistics\': {
                                        \'OtherCount\': 123,
                                        \'TotalCount\': 123
                                    },
                                    \'TotalCount\': 123,
                                    \'TotalResponseTime\': 123.0
                                },
                                \'ResponseTimeHistogram\': [
                                    {
                                        \'Value\': 123.0,
                                        \'Count\': 123
                                    },
                                ],
                                \'Aliases\': [
                                    {
                                        \'Name\': \'string\',
                                        \'Names\': [
                                            \'string\',
                                        ],
                                        \'Type\': \'string\'
                                    },
                                ]
                            },
                        ],
                        \'SummaryStatistics\': {
                            \'OkCount\': 123,
                            \'ErrorStatistics\': {
                                \'ThrottleCount\': 123,
                                \'OtherCount\': 123,
                                \'TotalCount\': 123
                            },
                            \'FaultStatistics\': {
                                \'OtherCount\': 123,
                                \'TotalCount\': 123
                            },
                            \'TotalCount\': 123,
                            \'TotalResponseTime\': 123.0
                        },
                        \'DurationHistogram\': [
                            {
                                \'Value\': 123.0,
                                \'Count\': 123
                            },
                        ],
                        \'ResponseTimeHistogram\': [
                            {
                                \'Value\': 123.0,
                                \'Count\': 123
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
                   
                  * AWS Service - The type of an AWS service. For example, ``AWS::DynamoDB`` for downstream calls to Amazon DynamoDB that didn\'t target a specific table. 
                   
                  * ``client`` - Represents the clients that sent requests to a root service. 
                   
                  * ``remote`` - A downstream service of indeterminate type. 
                   
                - **State** *(string) --* 
        
                  The service\'s state.
        
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
        
        """
        pass


class GetTraceSummaries(Paginator):
    def paginate(self, StartTime: datetime, EndTime: datetime, Sampling: bool = None, FilterExpression: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetTraceSummaries>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Sampling=True|False,
              FilterExpression=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type StartTime: datetime
        :param StartTime: **[REQUIRED]** 
        
          The start of the time frame for which to retrieve traces.
        
        :type EndTime: datetime
        :param EndTime: **[REQUIRED]** 
        
          The end of the time frame for which to retrieve traces.
        
        :type Sampling: boolean
        :param Sampling: 
        
          Set to ``true`` to get summaries for only a subset of available traces.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'TraceSummaries\': [
                    {
                        \'Id\': \'string\',
                        \'Duration\': 123.0,
                        \'ResponseTime\': 123.0,
                        \'HasFault\': True|False,
                        \'HasError\': True|False,
                        \'HasThrottle\': True|False,
                        \'IsPartial\': True|False,
                        \'Http\': {
                            \'HttpURL\': \'string\',
                            \'HttpStatus\': 123,
                            \'HttpMethod\': \'string\',
                            \'UserAgent\': \'string\',
                            \'ClientIp\': \'string\'
                        },
                        \'Annotations\': {
                            \'string\': [
                                {
                                    \'AnnotationValue\': {
                                        \'NumberValue\': 123.0,
                                        \'BooleanValue\': True|False,
                                        \'StringValue\': \'string\'
                                    },
                                    \'ServiceIds\': [
                                        {
                                            \'Name\': \'string\',
                                            \'Names\': [
                                                \'string\',
                                            ],
                                            \'AccountId\': \'string\',
                                            \'Type\': \'string\'
                                        },
                                    ]
                                },
                            ]
                        },
                        \'Users\': [
                            {
                                \'UserName\': \'string\',
                                \'ServiceIds\': [
                                    {
                                        \'Name\': \'string\',
                                        \'Names\': [
                                            \'string\',
                                        ],
                                        \'AccountId\': \'string\',
                                        \'Type\': \'string\'
                                    },
                                ]
                            },
                        ],
                        \'ServiceIds\': [
                            {
                                \'Name\': \'string\',
                                \'Names\': [
                                    \'string\',
                                ],
                                \'AccountId\': \'string\',
                                \'Type\': \'string\'
                            },
                        ]
                    },
                ],
                \'ApproximateTime\': datetime(2015, 1, 1),
                \'TracesProcessedCount\': 123,
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TraceSummaries** *(list) --* 
        
              Trace IDs and metadata for traces that were found in the specified time frame.
        
              - *(dict) --* 
        
                Metadata generated from the segment documents in a trace.
        
                - **Id** *(string) --* 
        
                  The unique identifier for the request that generated the trace\'s segments and subsegments.
        
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
        
                    The request\'s user agent string.
        
                  - **ClientIp** *(string) --* 
        
                    The IP address of the requestor.
        
                - **Annotations** *(dict) --* 
        
                  Annotations from the trace\'s segment documents.
        
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
        
                  Users from the trace\'s segment documents.
        
                  - *(dict) --* 
        
                    Information about a user recorded in segment documents.
        
                    - **UserName** *(string) --* 
        
                      The user\'s name.
        
                    - **ServiceIds** *(list) --* 
        
                      Services that the user\'s request hit.
        
                      - *(dict) --* 
        
                        - **Name** *(string) --* 
        
                        - **Names** *(list) --* 
        
                          - *(string) --* 
                      
                        - **AccountId** *(string) --* 
        
                        - **Type** *(string) --* 
        
                - **ServiceIds** *(list) --* 
        
                  Service IDs from the trace\'s segment documents.
        
                  - *(dict) --* 
        
                    - **Name** *(string) --* 
        
                    - **Names** *(list) --* 
        
                      - *(string) --* 
                  
                    - **AccountId** *(string) --* 
        
                    - **Type** *(string) --* 
        
            - **ApproximateTime** *(datetime) --* 
        
              The start time of this page of results.
        
            - **TracesProcessedCount** *(integer) --* 
        
              The total number of traces processed, including traces that did not match the specified filter expression.
        
        """
        pass
