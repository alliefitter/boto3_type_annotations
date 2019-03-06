from typing import List
from datetime import datetime
from typing import Dict
from botocore.paginate import Paginator


class GetMetricData(Paginator):
    def paginate(self, InstanceId: str, StartTime: datetime, EndTime: datetime, Filters: Dict, HistoricalMetrics: List, Groupings: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Connect.Client.get_metric_data`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/GetMetricData>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              InstanceId='string',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Filters={
                  'Queues': [
                      'string',
                  ],
                  'Channels': [
                      'VOICE',
                  ]
              },
              Groupings=[
                  'QUEUE'|'CHANNEL',
              ],
              HistoricalMetrics=[
                  {
                      'Name': 'CONTACTS_QUEUED'|'CONTACTS_HANDLED'|'CONTACTS_ABANDONED'|'CONTACTS_CONSULTED'|'CONTACTS_AGENT_HUNG_UP_FIRST'|'CONTACTS_HANDLED_INCOMING'|'CONTACTS_HANDLED_OUTBOUND'|'CONTACTS_HOLD_ABANDONS'|'CONTACTS_TRANSFERRED_IN'|'CONTACTS_TRANSFERRED_OUT'|'CONTACTS_TRANSFERRED_IN_FROM_QUEUE'|'CONTACTS_TRANSFERRED_OUT_FROM_QUEUE'|'CONTACTS_MISSED'|'CALLBACK_CONTACTS_HANDLED'|'API_CONTACTS_HANDLED'|'OCCUPANCY'|'HANDLE_TIME'|'AFTER_CONTACT_WORK_TIME'|'QUEUED_TIME'|'ABANDON_TIME'|'QUEUE_ANSWER_TIME'|'HOLD_TIME'|'INTERACTION_TIME'|'INTERACTION_AND_HOLD_TIME'|'SERVICE_LEVEL',
                      'Threshold': {
                          'Comparison': 'LT',
                          'ThresholdValue': 123.0
                      },
                      'Statistic': 'SUM'|'MAX'|'AVG',
                      'Unit': 'SECONDS'|'COUNT'|'PERCENT'
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
                'MetricResults': [
                    {
                        'Dimensions': {
                            'Queue': {
                                'Id': 'string',
                                'Arn': 'string'
                            },
                            'Channel': 'VOICE'
                        },
                        'Collections': [
                            {
                                'Metric': {
                                    'Name': 'CONTACTS_QUEUED'|'CONTACTS_HANDLED'|'CONTACTS_ABANDONED'|'CONTACTS_CONSULTED'|'CONTACTS_AGENT_HUNG_UP_FIRST'|'CONTACTS_HANDLED_INCOMING'|'CONTACTS_HANDLED_OUTBOUND'|'CONTACTS_HOLD_ABANDONS'|'CONTACTS_TRANSFERRED_IN'|'CONTACTS_TRANSFERRED_OUT'|'CONTACTS_TRANSFERRED_IN_FROM_QUEUE'|'CONTACTS_TRANSFERRED_OUT_FROM_QUEUE'|'CONTACTS_MISSED'|'CALLBACK_CONTACTS_HANDLED'|'API_CONTACTS_HANDLED'|'OCCUPANCY'|'HANDLE_TIME'|'AFTER_CONTACT_WORK_TIME'|'QUEUED_TIME'|'ABANDON_TIME'|'QUEUE_ANSWER_TIME'|'HOLD_TIME'|'INTERACTION_TIME'|'INTERACTION_AND_HOLD_TIME'|'SERVICE_LEVEL',
                                    'Threshold': {
                                        'Comparison': 'LT',
                                        'ThresholdValue': 123.0
                                    },
                                    'Statistic': 'SUM'|'MAX'|'AVG',
                                    'Unit': 'SECONDS'|'COUNT'|'PERCENT'
                                },
                                'Value': 123.0
                            },
                        ]
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **MetricResults** *(list) --* 
              A list of ``HistoricalMetricResult`` objects, organized by ``Dimensions`` , which is the ID of the resource specified in the ``Filters`` used for the request. The metrics are combined with the metrics included in ``Collections`` , which is a list of ``HisotricalMetricData`` objects.
              If no ``Grouping`` is specified in the request, ``Collections`` includes summary data for the ``HistoricalMetrics`` .
              - *(dict) --* 
                The metrics data returned from a ``GetMetricData`` operation.
                - **Dimensions** *(dict) --* 
                  The ``Dimensions`` for the metrics.
                  - **Queue** *(dict) --* 
                    A ``QueueReference`` object used as one part of dimension for the metrics results.
                    - **Id** *(string) --* 
                      The ID of the queue associated with the metrics returned.
                    - **Arn** *(string) --* 
                      The Amazon Resource Name (ARN) of queue.
                  - **Channel** *(string) --* 
                    The channel used for grouping and filters. Only VOICE is supported.
                - **Collections** *(list) --* 
                  A list of ``HistoricalMetricData`` objects.
                  - *(dict) --* 
                    A ``HistoricalMetricData`` object than contains a ``Metric`` and a ``Value`` .
                    - **Metric** *(dict) --* 
                      A ``HistoricalMetric`` object.
                      - **Name** *(string) --* 
                        The name of the historical metric.
                      - **Threshold** *(dict) --* 
                        The threshold for the metric, used with service level metrics.
                        - **Comparison** *(string) --* 
                          The Threshold to use to compare service level metrics to. Only "Less than" (LT) comparisons are supported.
                        - **ThresholdValue** *(float) --* 
                          The value of the threshold to compare the metric to. Only "Less than" (LT) comparisons are supported.
                      - **Statistic** *(string) --* 
                        The statistic for the metric.
                      - **Unit** *(string) --* 
                        The unit for the metric.
                    - **Value** *(float) --* 
                      The ``Value`` of the metric.
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
        :type StartTime: datetime
        :param StartTime: **[REQUIRED]**
          The timestamp, in UNIX Epoch time format, at which to start the reporting interval for the retrieval of historical metrics data. The time must be specified using a multiple of 5 minutes, such as 10:05, 10:10, 10:15.
           ``StartTime`` cannot be earlier than 24 hours before the time of the request. Historical metrics are available in Amazon Connect only for 24 hours.
        :type EndTime: datetime
        :param EndTime: **[REQUIRED]**
          The timestamp, in UNIX Epoch time format, at which to end the reporting interval for the retrieval of historical metrics data. The time must be specified using an interval of 5 minutes, such as 11:00, 11:05, 11:10, and must be later than the ``StartTime`` timestamp.
          The time range between ``StartTime`` and ``EndTime`` must be less than 24 hours.
        :type Filters: dict
        :param Filters: **[REQUIRED]**
          A ``Filters`` object that contains a list of queue IDs or queue ARNs, up to 100, or a list of Channels to use to filter the metrics returned in the response. Metric data is retrieved only for the resources associated with the IDs, ARNs, or Channels included in the filter. You can use both IDs and ARNs together in a request. Only VOICE is supported for Channel.
          To find the ARN for a queue, open the queue you want to use in the Amazon Connect Queue editor. The ARN for the queue is displayed in the address bar as part of the URL. For example, the queue ARN is the set of characters at the end of the URL, after \'id=\' such as ``arn:aws:connect:us-east-1:270923740243:instance/78fb859d-1b7d-44b1-8aa3-12f0835c5855/queue/1d1a4575-9618-40ab-bbeb-81e45795fe61`` . The queue ID is also included in the URL, and is the string after \'queue/\'.
          - **Queues** *(list) --*
            A list of up to 100 queue IDs or queue ARNs to use to filter the metrics retrieved. You can include both IDs and ARNs in a request.
            - *(string) --*
          - **Channels** *(list) --*
            The Channel to use as a filter for the metrics returned. Only VOICE is supported.
            - *(string) --*
        :type Groupings: list
        :param Groupings:
          The grouping applied to the metrics returned. For example, when results are grouped by queueId, the metrics returned are grouped by queue. The values returned apply to the metrics for each queue rather than aggregated for all queues.
          The current version supports grouping by Queue
          If no ``Grouping`` is included in the request, a summary of ``HistoricalMetrics`` for all queues is returned.
          - *(string) --*
        :type HistoricalMetrics: list
        :param HistoricalMetrics: **[REQUIRED]**
          A list of ``HistoricalMetric`` objects that contain the metrics to retrieve with the request.
          A ``HistoricalMetric`` object contains: ``HistoricalMetricName`` , ``Statistic`` , ``Threshold`` , and ``Unit`` .
          You must list each metric to retrieve data for in the request. For each historical metric you include in the request, you must include a ``Unit`` and a ``Statistic`` .
          The following historical metrics are available:
            CONTACTS_QUEUED
          Unit: COUNT
          Statistic: SUM
            CONTACTS_HANDLED
          Unit: COUNT
          Statistics: SUM
            CONTACTS_ABANDONED
          Unit: COUNT
          Statistics: SUM
            CONTACTS_CONSULTED
          Unit: COUNT
          Statistics: SUM
            CONTACTS_AGENT_HUNG_UP_FIRST
          Unit: COUNT
          Statistics: SUM
            CONTACTS_HANDLED_INCOMING
          Unit: COUNT
          Statistics: SUM
            CONTACTS_HANDLED_OUTBOUND
          Unit: COUNT
          Statistics: SUM
            CONTACTS_HOLD_ABANDONS
          Unit: COUNT
          Statistics: SUM
            CONTACTS_TRANSFERRED_IN
          Unit: COUNT
          Statistics: SUM
            CONTACTS_TRANSFERRED_OUT
          Unit: COUNT
          Statistics: SUM
            CONTACTS_TRANSFERRED_IN_FROM_QUEUE
          Unit: COUNT
          Statistics: SUM
            CONTACTS_TRANSFERRED_OUT_FROM_QUEUE
          Unit: COUNT
          Statistics: SUM
            CALLBACK_CONTACTS_HANDLED
          Unit: COUNT
          Statistics: SUM
            CALLBACK_CONTACTS_HANDLED
          Unit: COUNT
          Statistics: SUM
            API_CONTACTS_HANDLED
          Unit: COUNT
          Statistics: SUM
            CONTACTS_MISSED
          Unit: COUNT
          Statistics: SUM
            OCCUPANCY
          Unit: PERCENT
          Statistics: AVG
            HANDLE_TIME
          Unit: SECONDS
          Statistics: AVG
            AFTER_CONTACT_WORK_TIME
          Unit: SECONDS
          Statistics: AVG
            QUEUED_TIME
          Unit: SECONDS
          Statistics: MAX
            ABANDON_TIME
          Unit: COUNT
          Statistics: SUM
            QUEUE_ANSWER_TIME
          Unit: SECONDS
          Statistics: AVG
            HOLD_TIME
          Unit: SECONDS
          Statistics: AVG
            INTERACTION_TIME
          Unit: SECONDS
          Statistics: AVG
            INTERACTION_AND_HOLD_TIME
          Unit: SECONDS
          Statistics: AVG
            SERVICE_LEVEL
          Unit: PERCENT
          Statistics: AVG
          Threshold: Only \"Less than\" comparisons are supported, with the following service level thresholds: 15, 20, 25, 30, 45, 60, 90, 120, 180, 240, 300, 600
          - *(dict) --*
            A ``HistoricalMetric`` object that contains the Name, Unit, Statistic, and Threshold for the metric.
            - **Name** *(string) --*
              The name of the historical metric.
            - **Threshold** *(dict) --*
              The threshold for the metric, used with service level metrics.
              - **Comparison** *(string) --*
                The Threshold to use to compare service level metrics to. Only \"Less than\" (LT) comparisons are supported.
              - **ThresholdValue** *(float) --*
                The value of the threshold to compare the metric to. Only \"Less than\" (LT) comparisons are supported.
            - **Statistic** *(string) --*
              The statistic for the metric.
            - **Unit** *(string) --*
              The unit for the metric.
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


class ListRoutingProfiles(Paginator):
    def paginate(self, InstanceId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Connect.Client.list_routing_profiles`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListRoutingProfiles>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              InstanceId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'RoutingProfileSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RoutingProfileSummaryList** *(list) --* 
              An array of ``RoutingProfileSummary`` objects that include the ARN, Id, and Name of the routing profile.
              - *(dict) --* 
                A ``RoutingProfileSummary`` object that contains information about a routing profile, including ARN, Id, and Name.
                - **Id** *(string) --* 
                  The identifier of the routing profile.
                - **Arn** *(string) --* 
                  The ARN of the routing profile.
                - **Name** *(string) --* 
                  The name of the routing profile.
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
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


class ListSecurityProfiles(Paginator):
    def paginate(self, InstanceId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Connect.Client.list_security_profiles`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListSecurityProfiles>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              InstanceId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'SecurityProfileSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **SecurityProfileSummaryList** *(list) --* 
              An array of ``SecurityProfileSummary`` objects.
              - *(dict) --* 
                A ``SecurityProfileSummary`` object that contains information about a security profile, including ARN, Id, Name.
                - **Id** *(string) --* 
                  The identifier of the security profile.
                - **Arn** *(string) --* 
                  The ARN of the security profile.
                - **Name** *(string) --* 
                  The name of the security profile.
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
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


class ListUserHierarchyGroups(Paginator):
    def paginate(self, InstanceId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Connect.Client.list_user_hierarchy_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListUserHierarchyGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              InstanceId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'UserHierarchyGroupSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **UserHierarchyGroupSummaryList** *(list) --* 
              An array of ``HierarchyGroupSummary`` objects.
              - *(dict) --* 
                A ``HierarchyGroupSummary`` object that contains information about the hierarchy group, including ARN, Id, and Name.
                - **Id** *(string) --* 
                  The identifier of the hierarchy group.
                - **Arn** *(string) --* 
                  The ARN for the hierarchy group.
                - **Name** *(string) --* 
                  The name of the hierarchy group.
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
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


class ListUsers(Paginator):
    def paginate(self, InstanceId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Connect.Client.list_users`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListUsers>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              InstanceId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'UserSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Username': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **UserSummaryList** *(list) --* 
              An array of ``UserSummary`` objects that contain information about the users in your instance.
              - *(dict) --* 
                A ``UserSummary`` object that contains Information about a user, including ARN, Id, and user name.
                - **Id** *(string) --* 
                  The identifier for the user account.
                - **Arn** *(string) --* 
                  The ARN for the user account.
                - **Username** *(string) --* 
                  The Amazon Connect user name for the user account.
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**
          The identifier for your Amazon Connect instance. To find the ID of your instance, open the AWS console and select Amazon Connect. Select the alias of the instance in the Instance alias column. The instance ID is displayed in the Overview section of your instance settings. For example, the instance ID is the set of characters at the end of the instance ARN, after instance/, such as 10a4c4eb-f57e-4d4c-b602-bf39176ced07.
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
