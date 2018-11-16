from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListAssessmentRunAgents(Paginator):
    def paginate(self, assessmentRunArn: str, filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListAssessmentRunAgents>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              assessmentRunArn=\'string\',
              filter={
                  \'agentHealths\': [
                      \'HEALTHY\'|\'UNHEALTHY\'|\'UNKNOWN\',
                  ],
                  \'agentHealthCodes\': [
                      \'IDLE\'|\'RUNNING\'|\'SHUTDOWN\'|\'UNHEALTHY\'|\'THROTTLED\'|\'UNKNOWN\',
                  ]
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type assessmentRunArn: string
        :param assessmentRunArn: **[REQUIRED]** 
        
          The ARN that specifies the assessment run whose agents you want to list.
        
        :type filter: dict
        :param filter: 
        
          You can use this parameter to specify a subset of data to be included in the action\'s response.
        
          For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.
        
          - **agentHealths** *(list) --* **[REQUIRED]** 
        
            The current health state of the agent. Values can be set to **HEALTHY** or **UNHEALTHY** .
        
            - *(string) --* 
        
          - **agentHealthCodes** *(list) --* **[REQUIRED]** 
        
            The detailed health state of the agent. Values can be set to **IDLE** , **RUNNING** , **SHUTDOWN** , **UNHEALTHY** , **THROTTLED** , and **UNKNOWN** . 
        
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
                \'assessmentRunAgents\': [
                    {
                        \'agentId\': \'string\',
                        \'assessmentRunArn\': \'string\',
                        \'agentHealth\': \'HEALTHY\'|\'UNHEALTHY\'|\'UNKNOWN\',
                        \'agentHealthCode\': \'IDLE\'|\'RUNNING\'|\'SHUTDOWN\'|\'UNHEALTHY\'|\'THROTTLED\'|\'UNKNOWN\',
                        \'agentHealthDetails\': \'string\',
                        \'autoScalingGroup\': \'string\',
                        \'telemetryMetadata\': [
                            {
                                \'messageType\': \'string\',
                                \'count\': 123,
                                \'dataSize\': 123
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **assessmentRunAgents** *(list) --* 
        
              A list of ARNs that specifies the agents returned by the action.
        
              - *(dict) --* 
        
                Contains information about an Amazon Inspector agent. This data type is used as a response element in the  ListAssessmentRunAgents action.
        
                - **agentId** *(string) --* 
        
                  The AWS account of the EC2 instance where the agent is installed.
        
                - **assessmentRunArn** *(string) --* 
        
                  The ARN of the assessment run that is associated with the agent.
        
                - **agentHealth** *(string) --* 
        
                  The current health state of the agent.
        
                - **agentHealthCode** *(string) --* 
        
                  The detailed health state of the agent.
        
                - **agentHealthDetails** *(string) --* 
        
                  The description for the agent health code.
        
                - **autoScalingGroup** *(string) --* 
        
                  The Auto Scaling group of the EC2 instance that is specified by the agent ID.
        
                - **telemetryMetadata** *(list) --* 
        
                  The Amazon Inspector application data metrics that are collected by the agent.
        
                  - *(dict) --* 
        
                    The metadata about the Amazon Inspector application data metrics collected by the agent. This data type is used as the response element in the  GetTelemetryMetadata action.
        
                    - **messageType** *(string) --* 
        
                      A specific type of behavioral data that is collected by the agent.
        
                    - **count** *(integer) --* 
        
                      The count of messages that the agent sends to the Amazon Inspector service.
        
                    - **dataSize** *(integer) --* 
        
                      The data size of messages that the agent sends to the Amazon Inspector service.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListAssessmentRuns(Paginator):
    def paginate(self, assessmentTemplateArns: List = None, filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListAssessmentRuns>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              assessmentTemplateArns=[
                  \'string\',
              ],
              filter={
                  \'namePattern\': \'string\',
                  \'states\': [
                      \'CREATED\'|\'START_DATA_COLLECTION_PENDING\'|\'START_DATA_COLLECTION_IN_PROGRESS\'|\'COLLECTING_DATA\'|\'STOP_DATA_COLLECTION_PENDING\'|\'DATA_COLLECTED\'|\'START_EVALUATING_RULES_PENDING\'|\'EVALUATING_RULES\'|\'FAILED\'|\'ERROR\'|\'COMPLETED\'|\'COMPLETED_WITH_ERRORS\'|\'CANCELED\',
                  ],
                  \'durationRange\': {
                      \'minSeconds\': 123,
                      \'maxSeconds\': 123
                  },
                  \'rulesPackageArns\': [
                      \'string\',
                  ],
                  \'startTimeRange\': {
                      \'beginDate\': datetime(2015, 1, 1),
                      \'endDate\': datetime(2015, 1, 1)
                  },
                  \'completionTimeRange\': {
                      \'beginDate\': datetime(2015, 1, 1),
                      \'endDate\': datetime(2015, 1, 1)
                  },
                  \'stateChangeTimeRange\': {
                      \'beginDate\': datetime(2015, 1, 1),
                      \'endDate\': datetime(2015, 1, 1)
                  }
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type assessmentTemplateArns: list
        :param assessmentTemplateArns: 
        
          The ARNs that specify the assessment templates whose assessment runs you want to list.
        
          - *(string) --* 
        
        :type filter: dict
        :param filter: 
        
          You can use this parameter to specify a subset of data to be included in the action\'s response.
        
          For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.
        
          - **namePattern** *(string) --* 
        
            For a record to match a filter, an explicit value or a string containing a wildcard that is specified for this data type property must match the value of the **assessmentRunName** property of the  AssessmentRun data type.
        
          - **states** *(list) --* 
        
            For a record to match a filter, one of the values specified for this data type property must be the exact match of the value of the **assessmentRunState** property of the  AssessmentRun data type.
        
            - *(string) --* 
        
          - **durationRange** *(dict) --* 
        
            For a record to match a filter, the value that is specified for this data type property must inclusively match any value between the specified minimum and maximum values of the **durationInSeconds** property of the  AssessmentRun data type.
        
            - **minSeconds** *(integer) --* 
        
              The minimum value of the duration range. Must be greater than zero.
        
            - **maxSeconds** *(integer) --* 
        
              The maximum value of the duration range. Must be less than or equal to 604800 seconds (1 week).
        
          - **rulesPackageArns** *(list) --* 
        
            For a record to match a filter, the value that is specified for this data type property must be contained in the list of values of the **rulesPackages** property of the  AssessmentRun data type.
        
            - *(string) --* 
        
          - **startTimeRange** *(dict) --* 
        
            For a record to match a filter, the value that is specified for this data type property must inclusively match any value between the specified minimum and maximum values of the **startTime** property of the  AssessmentRun data type.
        
            - **beginDate** *(datetime) --* 
        
              The minimum value of the timestamp range.
        
            - **endDate** *(datetime) --* 
        
              The maximum value of the timestamp range.
        
          - **completionTimeRange** *(dict) --* 
        
            For a record to match a filter, the value that is specified for this data type property must inclusively match any value between the specified minimum and maximum values of the **completedAt** property of the  AssessmentRun data type.
        
            - **beginDate** *(datetime) --* 
        
              The minimum value of the timestamp range.
        
            - **endDate** *(datetime) --* 
        
              The maximum value of the timestamp range.
        
          - **stateChangeTimeRange** *(dict) --* 
        
            For a record to match a filter, the value that is specified for this data type property must match the **stateChangedAt** property of the  AssessmentRun data type.
        
            - **beginDate** *(datetime) --* 
        
              The minimum value of the timestamp range.
        
            - **endDate** *(datetime) --* 
        
              The maximum value of the timestamp range.
        
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
                \'assessmentRunArns\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **assessmentRunArns** *(list) --* 
        
              A list of ARNs that specifies the assessment runs that are returned by the action.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListAssessmentTargets(Paginator):
    def paginate(self, filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListAssessmentTargets>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              filter={
                  \'assessmentTargetNamePattern\': \'string\'
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type filter: dict
        :param filter: 
        
          You can use this parameter to specify a subset of data to be included in the action\'s response.
        
          For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.
        
          - **assessmentTargetNamePattern** *(string) --* 
        
            For a record to match a filter, an explicit value or a string that contains a wildcard that is specified for this data type property must match the value of the **assessmentTargetName** property of the  AssessmentTarget data type.
        
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
                \'assessmentTargetArns\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **assessmentTargetArns** *(list) --* 
        
              A list of ARNs that specifies the assessment targets that are returned by the action.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListAssessmentTemplates(Paginator):
    def paginate(self, assessmentTargetArns: List = None, filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListAssessmentTemplates>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              assessmentTargetArns=[
                  \'string\',
              ],
              filter={
                  \'namePattern\': \'string\',
                  \'durationRange\': {
                      \'minSeconds\': 123,
                      \'maxSeconds\': 123
                  },
                  \'rulesPackageArns\': [
                      \'string\',
                  ]
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type assessmentTargetArns: list
        :param assessmentTargetArns: 
        
          A list of ARNs that specifies the assessment targets whose assessment templates you want to list.
        
          - *(string) --* 
        
        :type filter: dict
        :param filter: 
        
          You can use this parameter to specify a subset of data to be included in the action\'s response.
        
          For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.
        
          - **namePattern** *(string) --* 
        
            For a record to match a filter, an explicit value or a string that contains a wildcard that is specified for this data type property must match the value of the **assessmentTemplateName** property of the  AssessmentTemplate data type.
        
          - **durationRange** *(dict) --* 
        
            For a record to match a filter, the value specified for this data type property must inclusively match any value between the specified minimum and maximum values of the **durationInSeconds** property of the  AssessmentTemplate data type.
        
            - **minSeconds** *(integer) --* 
        
              The minimum value of the duration range. Must be greater than zero.
        
            - **maxSeconds** *(integer) --* 
        
              The maximum value of the duration range. Must be less than or equal to 604800 seconds (1 week).
        
          - **rulesPackageArns** *(list) --* 
        
            For a record to match a filter, the values that are specified for this data type property must be contained in the list of values of the **rulesPackageArns** property of the  AssessmentTemplate data type.
        
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
                \'assessmentTemplateArns\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **assessmentTemplateArns** *(list) --* 
        
              A list of ARNs that specifies the assessment templates returned by the action.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListEventSubscriptions(Paginator):
    def paginate(self, resourceArn: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListEventSubscriptions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              resourceArn=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type resourceArn: string
        :param resourceArn: 
        
          The ARN of the assessment template for which you want to list the existing event subscriptions.
        
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
                \'subscriptions\': [
                    {
                        \'resourceArn\': \'string\',
                        \'topicArn\': \'string\',
                        \'eventSubscriptions\': [
                            {
                                \'event\': \'ASSESSMENT_RUN_STARTED\'|\'ASSESSMENT_RUN_COMPLETED\'|\'ASSESSMENT_RUN_STATE_CHANGED\'|\'FINDING_REPORTED\'|\'OTHER\',
                                \'subscribedAt\': datetime(2015, 1, 1)
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **subscriptions** *(list) --* 
        
              Details of the returned event subscriptions.
        
              - *(dict) --* 
        
                This data type is used as a response element in the  ListEventSubscriptions action.
        
                - **resourceArn** *(string) --* 
        
                  The ARN of the assessment template that is used during the event for which the SNS notification is sent.
        
                - **topicArn** *(string) --* 
        
                  The ARN of the Amazon Simple Notification Service (SNS) topic to which the SNS notifications are sent.
        
                - **eventSubscriptions** *(list) --* 
        
                  The list of existing event subscriptions.
        
                  - *(dict) --* 
        
                    This data type is used in the  Subscription data type.
        
                    - **event** *(string) --* 
        
                      The event for which Amazon Simple Notification Service (SNS) notifications are sent.
        
                    - **subscribedAt** *(datetime) --* 
        
                      The time at which  SubscribeToEvent is called.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListFindings(Paginator):
    def paginate(self, assessmentRunArns: List = None, filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListFindings>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              assessmentRunArns=[
                  \'string\',
              ],
              filter={
                  \'agentIds\': [
                      \'string\',
                  ],
                  \'autoScalingGroups\': [
                      \'string\',
                  ],
                  \'ruleNames\': [
                      \'string\',
                  ],
                  \'severities\': [
                      \'Low\'|\'Medium\'|\'High\'|\'Informational\'|\'Undefined\',
                  ],
                  \'rulesPackageArns\': [
                      \'string\',
                  ],
                  \'attributes\': [
                      {
                          \'key\': \'string\',
                          \'value\': \'string\'
                      },
                  ],
                  \'userAttributes\': [
                      {
                          \'key\': \'string\',
                          \'value\': \'string\'
                      },
                  ],
                  \'creationTimeRange\': {
                      \'beginDate\': datetime(2015, 1, 1),
                      \'endDate\': datetime(2015, 1, 1)
                  }
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type assessmentRunArns: list
        :param assessmentRunArns: 
        
          The ARNs of the assessment runs that generate the findings that you want to list.
        
          - *(string) --* 
        
        :type filter: dict
        :param filter: 
        
          You can use this parameter to specify a subset of data to be included in the action\'s response.
        
          For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.
        
          - **agentIds** *(list) --* 
        
            For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **agentId** property of the  Finding data type.
        
            - *(string) --* 
        
          - **autoScalingGroups** *(list) --* 
        
            For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **autoScalingGroup** property of the  Finding data type.
        
            - *(string) --* 
        
          - **ruleNames** *(list) --* 
        
            For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **ruleName** property of the  Finding data type.
        
            - *(string) --* 
        
          - **severities** *(list) --* 
        
            For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **severity** property of the  Finding data type.
        
            - *(string) --* 
        
          - **rulesPackageArns** *(list) --* 
        
            For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the **rulesPackageArn** property of the  Finding data type.
        
            - *(string) --* 
        
          - **attributes** *(list) --* 
        
            For a record to match a filter, the list of values that are specified for this data type property must be contained in the list of values of the **attributes** property of the  Finding data type.
        
            - *(dict) --* 
        
              This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.
        
              - **key** *(string) --* **[REQUIRED]** 
        
                The attribute key.
        
              - **value** *(string) --* 
        
                The value assigned to the attribute key.
        
          - **userAttributes** *(list) --* 
        
            For a record to match a filter, the value that is specified for this data type property must be contained in the list of values of the **userAttributes** property of the  Finding data type.
        
            - *(dict) --* 
        
              This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.
        
              - **key** *(string) --* **[REQUIRED]** 
        
                The attribute key.
        
              - **value** *(string) --* 
        
                The value assigned to the attribute key.
        
          - **creationTimeRange** *(dict) --* 
        
            The time range during which the finding is generated.
        
            - **beginDate** *(datetime) --* 
        
              The minimum value of the timestamp range.
        
            - **endDate** *(datetime) --* 
        
              The maximum value of the timestamp range.
        
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
                \'findingArns\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **findingArns** *(list) --* 
        
              A list of ARNs that specifies the findings returned by the action.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListRulesPackages(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/ListRulesPackages>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'rulesPackageArns\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **rulesPackageArns** *(list) --* 
        
              The list of ARNs that specifies the rules packages returned by the action.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class PreviewAgents(Paginator):
    def paginate(self, previewAgentsArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/PreviewAgents>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              previewAgentsArn=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type previewAgentsArn: string
        :param previewAgentsArn: **[REQUIRED]** 
        
          The ARN of the assessment target whose agents you want to preview.
        
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
                \'agentPreviews\': [
                    {
                        \'hostname\': \'string\',
                        \'agentId\': \'string\',
                        \'autoScalingGroup\': \'string\',
                        \'agentHealth\': \'HEALTHY\'|\'UNHEALTHY\'|\'UNKNOWN\',
                        \'agentVersion\': \'string\',
                        \'operatingSystem\': \'string\',
                        \'kernelVersion\': \'string\',
                        \'ipv4Address\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **agentPreviews** *(list) --* 
        
              The resulting list of agents.
        
              - *(dict) --* 
        
                Used as a response element in the  PreviewAgents action.
        
                - **hostname** *(string) --* 
        
                  The hostname of the EC2 instance on which the Amazon Inspector Agent is installed.
        
                - **agentId** *(string) --* 
        
                  The ID of the EC2 instance where the agent is installed.
        
                - **autoScalingGroup** *(string) --* 
        
                  The Auto Scaling group for the EC2 instance where the agent is installed.
        
                - **agentHealth** *(string) --* 
        
                  The health status of the Amazon Inspector Agent.
        
                - **agentVersion** *(string) --* 
        
                  The version of the Amazon Inspector Agent.
        
                - **operatingSystem** *(string) --* 
        
                  The operating system running on the EC2 instance on which the Amazon Inspector Agent is installed.
        
                - **kernelVersion** *(string) --* 
        
                  The kernel version of the operating system running on the EC2 instance on which the Amazon Inspector Agent is installed.
        
                - **ipv4Address** *(string) --* 
        
                  The IP address of the EC2 instance on which the Amazon Inspector Agent is installed.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
