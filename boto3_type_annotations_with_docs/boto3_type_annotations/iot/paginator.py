from typing import Dict
from datetime import datetime
from botocore.paginate import Paginator


class ListActiveViolations(Paginator):
    def paginate(self, thingName: str = None, securityProfileName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_active_violations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListActiveViolations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              thingName='string',
              securityProfileName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'activeViolations': [
                    {
                        'violationId': 'string',
                        'thingName': 'string',
                        'securityProfileName': 'string',
                        'behavior': {
                            'name': 'string',
                            'metric': 'string',
                            'criteria': {
                                'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                                'value': {
                                    'count': 123,
                                    'cidrs': [
                                        'string',
                                    ],
                                    'ports': [
                                        123,
                                    ]
                                },
                                'durationSeconds': 123,
                                'consecutiveDatapointsToAlarm': 123,
                                'consecutiveDatapointsToClear': 123,
                                'statisticalThreshold': {
                                    'statistic': 'string'
                                }
                            }
                        },
                        'lastViolationValue': {
                            'count': 123,
                            'cidrs': [
                                'string',
                            ],
                            'ports': [
                                123,
                            ]
                        },
                        'lastViolationTime': datetime(2015, 1, 1),
                        'violationStartTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **activeViolations** *(list) --* 
              The list of active violations.
              - *(dict) --* 
                Information about an active Device Defender security profile behavior violation.
                - **violationId** *(string) --* 
                  The ID of the active violation.
                - **thingName** *(string) --* 
                  The name of the thing responsible for the active violation.
                - **securityProfileName** *(string) --* 
                  The security profile whose behavior is in violation.
                - **behavior** *(dict) --* 
                  The behavior which is being violated.
                  - **name** *(string) --* 
                    The name you have given to the behavior.
                  - **metric** *(string) --* 
                    What is measured by the behavior.
                  - **criteria** *(dict) --* 
                    The criteria that determine if a device is behaving normally in regard to the ``metric`` .
                    - **comparisonOperator** *(string) --* 
                      The operator that relates the thing measured (``metric`` ) to the criteria (containing a ``value`` or ``statisticalThreshold`` ).
                    - **value** *(dict) --* 
                      The value to be compared with the ``metric`` .
                      - **count** *(integer) --* 
                        If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric value to be compared with the ``metric`` .
                      - **cidrs** *(list) --* 
                        If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to be compared with the ``metric`` .
                        - *(string) --* 
                      - **ports** *(list) --* 
                        If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to be compared with the ``metric`` .
                        - *(integer) --* 
                    - **durationSeconds** *(integer) --* 
                      Use this to specify the time duration over which the behavior is evaluated, for those criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank.
                    - **consecutiveDatapointsToAlarm** *(integer) --* 
                      If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.
                    - **consecutiveDatapointsToClear** *(integer) --* 
                      If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.
                    - **statisticalThreshold** *(dict) --* 
                      A statistical ranking (percentile) which indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.
                      - **statistic** *(string) --* 
                        The percentile which resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (``durationSeconds`` ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (``comparisonOperator`` ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.
                - **lastViolationValue** *(dict) --* 
                  The value of the metric (the measurement) which caused the most recent violation.
                  - **count** *(integer) --* 
                    If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric value to be compared with the ``metric`` .
                  - **cidrs** *(list) --* 
                    If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to be compared with the ``metric`` .
                    - *(string) --* 
                  - **ports** *(list) --* 
                    If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to be compared with the ``metric`` .
                    - *(integer) --* 
                - **lastViolationTime** *(datetime) --* 
                  The time the most recent violation occurred.
                - **violationStartTime** *(datetime) --* 
                  The time the violation started.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type thingName: string
        :param thingName:
          The name of the thing whose active violations are listed.
        :type securityProfileName: string
        :param securityProfileName:
          The name of the Device Defender security profile for which violations are listed.
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


class ListAttachedPolicies(Paginator):
    def paginate(self, target: str, recursive: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_attached_policies`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListAttachedPolicies>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              target='string',
              recursive=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'policies': [
                    {
                        'policyName': 'string',
                        'policyArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **policies** *(list) --* 
              The policies.
              - *(dict) --* 
                Describes an AWS IoT policy.
                - **policyName** *(string) --* 
                  The policy name.
                - **policyArn** *(string) --* 
                  The policy ARN.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type target: string
        :param target: **[REQUIRED]**
          The group for which the policies will be listed.
        :type recursive: boolean
        :param recursive:
          When true, recursively list attached policies.
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


class ListAuditFindings(Paginator):
    def paginate(self, taskId: str = None, checkName: str = None, resourceIdentifier: Dict = None, startTime: datetime = None, endTime: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_audit_findings`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListAuditFindings>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              taskId='string',
              checkName='string',
              resourceIdentifier={
                  'deviceCertificateId': 'string',
                  'caCertificateId': 'string',
                  'cognitoIdentityPoolId': 'string',
                  'clientId': 'string',
                  'policyVersionIdentifier': {
                      'policyName': 'string',
                      'policyVersionId': 'string'
                  },
                  'account': 'string'
              },
              startTime=datetime(2015, 1, 1),
              endTime=datetime(2015, 1, 1),
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'findings': [
                    {
                        'taskId': 'string',
                        'checkName': 'string',
                        'taskStartTime': datetime(2015, 1, 1),
                        'findingTime': datetime(2015, 1, 1),
                        'severity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW',
                        'nonCompliantResource': {
                            'resourceType': 'DEVICE_CERTIFICATE'|'CA_CERTIFICATE'|'IOT_POLICY'|'COGNITO_IDENTITY_POOL'|'CLIENT_ID'|'ACCOUNT_SETTINGS',
                            'resourceIdentifier': {
                                'deviceCertificateId': 'string',
                                'caCertificateId': 'string',
                                'cognitoIdentityPoolId': 'string',
                                'clientId': 'string',
                                'policyVersionIdentifier': {
                                    'policyName': 'string',
                                    'policyVersionId': 'string'
                                },
                                'account': 'string'
                            },
                            'additionalInfo': {
                                'string': 'string'
                            }
                        },
                        'relatedResources': [
                            {
                                'resourceType': 'DEVICE_CERTIFICATE'|'CA_CERTIFICATE'|'IOT_POLICY'|'COGNITO_IDENTITY_POOL'|'CLIENT_ID'|'ACCOUNT_SETTINGS',
                                'resourceIdentifier': {
                                    'deviceCertificateId': 'string',
                                    'caCertificateId': 'string',
                                    'cognitoIdentityPoolId': 'string',
                                    'clientId': 'string',
                                    'policyVersionIdentifier': {
                                        'policyName': 'string',
                                        'policyVersionId': 'string'
                                    },
                                    'account': 'string'
                                },
                                'additionalInfo': {
                                    'string': 'string'
                                }
                            },
                        ],
                        'reasonForNonCompliance': 'string',
                        'reasonForNonComplianceCode': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **findings** *(list) --* 
              The findings (results) of the audit.
              - *(dict) --* 
                The findings (results) of the audit.
                - **taskId** *(string) --* 
                  The ID of the audit that generated this result (finding)
                - **checkName** *(string) --* 
                  The audit check that generated this result.
                - **taskStartTime** *(datetime) --* 
                  The time the audit started.
                - **findingTime** *(datetime) --* 
                  The time the result (finding) was discovered.
                - **severity** *(string) --* 
                  The severity of the result (finding).
                - **nonCompliantResource** *(dict) --* 
                  The resource that was found to be non-compliant with the audit check.
                  - **resourceType** *(string) --* 
                    The type of the non-compliant resource.
                  - **resourceIdentifier** *(dict) --* 
                    Information identifying the non-compliant resource.
                    - **deviceCertificateId** *(string) --* 
                      The ID of the certificate attached to the resource.
                    - **caCertificateId** *(string) --* 
                      The ID of the CA certificate used to authorize the certificate.
                    - **cognitoIdentityPoolId** *(string) --* 
                      The ID of the Cognito Identity Pool.
                    - **clientId** *(string) --* 
                      The client ID.
                    - **policyVersionIdentifier** *(dict) --* 
                      The version of the policy associated with the resource.
                      - **policyName** *(string) --* 
                        The name of the policy.
                      - **policyVersionId** *(string) --* 
                        The ID of the version of the policy associated with the resource.
                    - **account** *(string) --* 
                      The account with which the resource is associated.
                  - **additionalInfo** *(dict) --* 
                    Additional information about the non-compliant resource.
                    - *(string) --* 
                      - *(string) --* 
                - **relatedResources** *(list) --* 
                  The list of related resources.
                  - *(dict) --* 
                    Information about a related resource.
                    - **resourceType** *(string) --* 
                      The type of resource.
                    - **resourceIdentifier** *(dict) --* 
                      Information identifying the resource.
                      - **deviceCertificateId** *(string) --* 
                        The ID of the certificate attached to the resource.
                      - **caCertificateId** *(string) --* 
                        The ID of the CA certificate used to authorize the certificate.
                      - **cognitoIdentityPoolId** *(string) --* 
                        The ID of the Cognito Identity Pool.
                      - **clientId** *(string) --* 
                        The client ID.
                      - **policyVersionIdentifier** *(dict) --* 
                        The version of the policy associated with the resource.
                        - **policyName** *(string) --* 
                          The name of the policy.
                        - **policyVersionId** *(string) --* 
                          The ID of the version of the policy associated with the resource.
                      - **account** *(string) --* 
                        The account with which the resource is associated.
                    - **additionalInfo** *(dict) --* 
                      Additional information about the resource.
                      - *(string) --* 
                        - *(string) --* 
                - **reasonForNonCompliance** *(string) --* 
                  The reason the resource was non-compliant.
                - **reasonForNonComplianceCode** *(string) --* 
                  A code which indicates the reason that the resource was non-compliant.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type taskId: string
        :param taskId:
          A filter to limit results to the audit with the specified ID. You must specify either the taskId or the startTime and endTime, but not both.
        :type checkName: string
        :param checkName:
          A filter to limit results to the findings for the specified audit check.
        :type resourceIdentifier: dict
        :param resourceIdentifier:
          Information identifying the non-compliant resource.
          - **deviceCertificateId** *(string) --*
            The ID of the certificate attached to the resource.
          - **caCertificateId** *(string) --*
            The ID of the CA certificate used to authorize the certificate.
          - **cognitoIdentityPoolId** *(string) --*
            The ID of the Cognito Identity Pool.
          - **clientId** *(string) --*
            The client ID.
          - **policyVersionIdentifier** *(dict) --*
            The version of the policy associated with the resource.
            - **policyName** *(string) --*
              The name of the policy.
            - **policyVersionId** *(string) --*
              The ID of the version of the policy associated with the resource.
          - **account** *(string) --*
            The account with which the resource is associated.
        :type startTime: datetime
        :param startTime:
          A filter to limit results to those found after the specified time. You must specify either the startTime and endTime or the taskId, but not both.
        :type endTime: datetime
        :param endTime:
          A filter to limit results to those found before the specified time. You must specify either the startTime and endTime or the taskId, but not both.
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


class ListAuditTasks(Paginator):
    def paginate(self, startTime: datetime, endTime: datetime, taskType: str = None, taskStatus: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_audit_tasks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListAuditTasks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              startTime=datetime(2015, 1, 1),
              endTime=datetime(2015, 1, 1),
              taskType='ON_DEMAND_AUDIT_TASK'|'SCHEDULED_AUDIT_TASK',
              taskStatus='IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'tasks': [
                    {
                        'taskId': 'string',
                        'taskStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED',
                        'taskType': 'ON_DEMAND_AUDIT_TASK'|'SCHEDULED_AUDIT_TASK'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **tasks** *(list) --* 
              The audits that were performed during the specified time period.
              - *(dict) --* 
                The audits that were performed.
                - **taskId** *(string) --* 
                  The ID of this audit.
                - **taskStatus** *(string) --* 
                  The status of this audit: one of "IN_PROGRESS", "COMPLETED", "FAILED" or "CANCELED".
                - **taskType** *(string) --* 
                  The type of this audit: one of "ON_DEMAND_AUDIT_TASK" or "SCHEDULED_AUDIT_TASK".
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type startTime: datetime
        :param startTime: **[REQUIRED]**
          The beginning of the time period. Note that audit information is retained for a limited time (180 days). Requesting a start time prior to what is retained results in an \"InvalidRequestException\".
        :type endTime: datetime
        :param endTime: **[REQUIRED]**
          The end of the time period.
        :type taskType: string
        :param taskType:
          A filter to limit the output to the specified type of audit: can be one of \"ON_DEMAND_AUDIT_TASK\" or \"SCHEDULED__AUDIT_TASK\".
        :type taskStatus: string
        :param taskStatus:
          A filter to limit the output to audits with the specified completion status: can be one of \"IN_PROGRESS\", \"COMPLETED\", \"FAILED\" or \"CANCELED\".
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


class ListAuthorizers(Paginator):
    def paginate(self, ascendingOrder: bool = None, status: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_authorizers`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListAuthorizers>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ascendingOrder=True|False,
              status='ACTIVE'|'INACTIVE',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'authorizers': [
                    {
                        'authorizerName': 'string',
                        'authorizerArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **authorizers** *(list) --* 
              The authorizers.
              - *(dict) --* 
                The authorizer summary.
                - **authorizerName** *(string) --* 
                  The authorizer name.
                - **authorizerArn** *(string) --* 
                  The authorizer ARN.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Return the list of authorizers in ascending alphabetical order.
        :type status: string
        :param status:
          The status of the list authorizers request.
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


class ListBillingGroups(Paginator):
    def paginate(self, namePrefixFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_billing_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListBillingGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              namePrefixFilter='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'billingGroups': [
                    {
                        'groupName': 'string',
                        'groupArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **billingGroups** *(list) --* 
              The list of billing groups.
              - *(dict) --* 
                The name and ARN of a group.
                - **groupName** *(string) --* 
                  The group name.
                - **groupArn** *(string) --* 
                  The group ARN.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type namePrefixFilter: string
        :param namePrefixFilter:
          Limit the results to billing groups whose names have the given prefix.
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


class ListCACertificates(Paginator):
    def paginate(self, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_ca_certificates`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListCACertificates>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ascendingOrder=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'certificates': [
                    {
                        'certificateArn': 'string',
                        'certificateId': 'string',
                        'status': 'ACTIVE'|'INACTIVE',
                        'creationDate': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the ListCACertificates operation.
            - **certificates** *(list) --* 
              The CA certificates registered in your AWS account.
              - *(dict) --* 
                A CA certificate.
                - **certificateArn** *(string) --* 
                  The ARN of the CA certificate.
                - **certificateId** *(string) --* 
                  The ID of the CA certificate.
                - **status** *(string) --* 
                  The status of the CA certificate.
                  The status value REGISTER_INACTIVE is deprecated and should not be used.
                - **creationDate** *(datetime) --* 
                  The date the CA certificate was created.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Determines the order of the results.
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


class ListCertificates(Paginator):
    def paginate(self, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_certificates`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListCertificates>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ascendingOrder=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'certificates': [
                    {
                        'certificateArn': 'string',
                        'certificateId': 'string',
                        'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
                        'creationDate': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output of the ListCertificates operation.
            - **certificates** *(list) --* 
              The descriptions of the certificates.
              - *(dict) --* 
                Information about a certificate.
                - **certificateArn** *(string) --* 
                  The ARN of the certificate.
                - **certificateId** *(string) --* 
                  The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
                - **status** *(string) --* 
                  The status of the certificate.
                  The status value REGISTER_INACTIVE is deprecated and should not be used.
                - **creationDate** *(datetime) --* 
                  The date and time the certificate was created.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.
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


class ListCertificatesByCA(Paginator):
    def paginate(self, caCertificateId: str, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_certificates_by_ca`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListCertificatesByCA>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              caCertificateId='string',
              ascendingOrder=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'certificates': [
                    {
                        'certificateArn': 'string',
                        'certificateId': 'string',
                        'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
                        'creationDate': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output of the ListCertificatesByCA operation.
            - **certificates** *(list) --* 
              The device certificates signed by the specified CA certificate.
              - *(dict) --* 
                Information about a certificate.
                - **certificateArn** *(string) --* 
                  The ARN of the certificate.
                - **certificateId** *(string) --* 
                  The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
                - **status** *(string) --* 
                  The status of the certificate.
                  The status value REGISTER_INACTIVE is deprecated and should not be used.
                - **creationDate** *(datetime) --* 
                  The date and time the certificate was created.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type caCertificateId: string
        :param caCertificateId: **[REQUIRED]**
          The ID of the CA certificate. This operation will list all registered device certificate that were signed by this CA certificate.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.
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


class ListIndices(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_indices`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListIndices>`_
        
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
                'indexNames': [
                    'string',
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **indexNames** *(list) --* 
              The index names.
              - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListJobExecutionsForJob(Paginator):
    def paginate(self, jobId: str, status: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_job_executions_for_job`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListJobExecutionsForJob>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              jobId='string',
              status='QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'executionSummaries': [
                    {
                        'thingArn': 'string',
                        'jobExecutionSummary': {
                            'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
                            'queuedAt': datetime(2015, 1, 1),
                            'startedAt': datetime(2015, 1, 1),
                            'lastUpdatedAt': datetime(2015, 1, 1),
                            'executionNumber': 123
                        }
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **executionSummaries** *(list) --* 
              A list of job execution summaries.
              - *(dict) --* 
                Contains a summary of information about job executions for a specific job.
                - **thingArn** *(string) --* 
                  The ARN of the thing on which the job execution is running.
                - **jobExecutionSummary** *(dict) --* 
                  Contains a subset of information about a job execution.
                  - **status** *(string) --* 
                    The status of the job execution.
                  - **queuedAt** *(datetime) --* 
                    The time, in seconds since the epoch, when the job execution was queued.
                  - **startedAt** *(datetime) --* 
                    The time, in seconds since the epoch, when the job execution started.
                  - **lastUpdatedAt** *(datetime) --* 
                    The time, in seconds since the epoch, when the job execution was last updated.
                  - **executionNumber** *(integer) --* 
                    A string (consisting of the digits "0" through "9") which identifies this particular job execution on this particular device. It can be used later in commands which return or update job execution information.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type jobId: string
        :param jobId: **[REQUIRED]**
          The unique identifier you assigned to this job when it was created.
        :type status: string
        :param status:
          The status of the job.
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


class ListJobExecutionsForThing(Paginator):
    def paginate(self, thingName: str, status: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_job_executions_for_thing`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListJobExecutionsForThing>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              thingName='string',
              status='QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'executionSummaries': [
                    {
                        'jobId': 'string',
                        'jobExecutionSummary': {
                            'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
                            'queuedAt': datetime(2015, 1, 1),
                            'startedAt': datetime(2015, 1, 1),
                            'lastUpdatedAt': datetime(2015, 1, 1),
                            'executionNumber': 123
                        }
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **executionSummaries** *(list) --* 
              A list of job execution summaries.
              - *(dict) --* 
                The job execution summary for a thing.
                - **jobId** *(string) --* 
                  The unique identifier you assigned to this job when it was created.
                - **jobExecutionSummary** *(dict) --* 
                  Contains a subset of information about a job execution.
                  - **status** *(string) --* 
                    The status of the job execution.
                  - **queuedAt** *(datetime) --* 
                    The time, in seconds since the epoch, when the job execution was queued.
                  - **startedAt** *(datetime) --* 
                    The time, in seconds since the epoch, when the job execution started.
                  - **lastUpdatedAt** *(datetime) --* 
                    The time, in seconds since the epoch, when the job execution was last updated.
                  - **executionNumber** *(integer) --* 
                    A string (consisting of the digits "0" through "9") which identifies this particular job execution on this particular device. It can be used later in commands which return or update job execution information.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type thingName: string
        :param thingName: **[REQUIRED]**
          The thing name.
        :type status: string
        :param status:
          An optional filter that lets you search for jobs that have the specified status.
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


class ListJobs(Paginator):
    def paginate(self, status: str = None, targetSelection: str = None, thingGroupName: str = None, thingGroupId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_jobs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListJobs>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              status='IN_PROGRESS'|'CANCELED'|'COMPLETED'|'DELETION_IN_PROGRESS',
              targetSelection='CONTINUOUS'|'SNAPSHOT',
              thingGroupName='string',
              thingGroupId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'jobs': [
                    {
                        'jobArn': 'string',
                        'jobId': 'string',
                        'thingGroupId': 'string',
                        'targetSelection': 'CONTINUOUS'|'SNAPSHOT',
                        'status': 'IN_PROGRESS'|'CANCELED'|'COMPLETED'|'DELETION_IN_PROGRESS',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'completedAt': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **jobs** *(list) --* 
              A list of jobs.
              - *(dict) --* 
                The job summary.
                - **jobArn** *(string) --* 
                  The job ARN.
                - **jobId** *(string) --* 
                  The unique identifier you assigned to this job when it was created.
                - **thingGroupId** *(string) --* 
                  The ID of the thing group.
                - **targetSelection** *(string) --* 
                  Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group.
                - **status** *(string) --* 
                  The job summary status.
                - **createdAt** *(datetime) --* 
                  The time, in seconds since the epoch, when the job was created.
                - **lastUpdatedAt** *(datetime) --* 
                  The time, in seconds since the epoch, when the job was last updated.
                - **completedAt** *(datetime) --* 
                  The time, in seconds since the epoch, when the job completed.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type status: string
        :param status:
          An optional filter that lets you search for jobs that have the specified status.
        :type targetSelection: string
        :param targetSelection:
          Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group.
        :type thingGroupName: string
        :param thingGroupName:
          A filter that limits the returned jobs to those for the specified group.
        :type thingGroupId: string
        :param thingGroupId:
          A filter that limits the returned jobs to those for the specified group.
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


class ListOTAUpdates(Paginator):
    def paginate(self, otaUpdateStatus: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_ota_updates`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListOTAUpdates>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              otaUpdateStatus='CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'CREATE_FAILED',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'otaUpdates': [
                    {
                        'otaUpdateId': 'string',
                        'otaUpdateArn': 'string',
                        'creationDate': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **otaUpdates** *(list) --* 
              A list of OTA update jobs.
              - *(dict) --* 
                An OTA update summary.
                - **otaUpdateId** *(string) --* 
                  The OTA update ID.
                - **otaUpdateArn** *(string) --* 
                  The OTA update ARN.
                - **creationDate** *(datetime) --* 
                  The date when the OTA update was created.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type otaUpdateStatus: string
        :param otaUpdateStatus:
          The OTA update job status.
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


class ListOutgoingCertificates(Paginator):
    def paginate(self, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_outgoing_certificates`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListOutgoingCertificates>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ascendingOrder=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'outgoingCertificates': [
                    {
                        'certificateArn': 'string',
                        'certificateId': 'string',
                        'transferredTo': 'string',
                        'transferDate': datetime(2015, 1, 1),
                        'transferMessage': 'string',
                        'creationDate': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the ListOutgoingCertificates operation.
            - **outgoingCertificates** *(list) --* 
              The certificates that are being transferred but not yet accepted.
              - *(dict) --* 
                A certificate that has been transferred but not yet accepted.
                - **certificateArn** *(string) --* 
                  The certificate ARN.
                - **certificateId** *(string) --* 
                  The certificate ID.
                - **transferredTo** *(string) --* 
                  The AWS account to which the transfer was made.
                - **transferDate** *(datetime) --* 
                  The date the transfer was initiated.
                - **transferMessage** *(string) --* 
                  The transfer message.
                - **creationDate** *(datetime) --* 
                  The certificate creation date.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.
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


class ListPolicies(Paginator):
    def paginate(self, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_policies`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPolicies>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ascendingOrder=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'policies': [
                    {
                        'policyName': 'string',
                        'policyArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the ListPolicies operation.
            - **policies** *(list) --* 
              The descriptions of the policies.
              - *(dict) --* 
                Describes an AWS IoT policy.
                - **policyName** *(string) --* 
                  The policy name.
                - **policyArn** *(string) --* 
                  The policy ARN.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Specifies the order for results. If true, the results are returned in ascending creation order.
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


class ListPolicyPrincipals(Paginator):
    def paginate(self, policyName: str, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_policy_principals`.
        .. danger::
            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPolicyPrincipals>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              policyName='string',
              ascendingOrder=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'principals': [
                    'string',
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the ListPolicyPrincipals operation.
            - **principals** *(list) --* 
              The descriptions of the principals.
              - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type policyName: string
        :param policyName: **[REQUIRED]**
          The policy name.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Specifies the order for results. If true, the results are returned in ascending creation order.
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


class ListPrincipalPolicies(Paginator):
    def paginate(self, principal: str, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_principal_policies`.
        .. danger::
            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPrincipalPolicies>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              principal='string',
              ascendingOrder=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'policies': [
                    {
                        'policyName': 'string',
                        'policyArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the ListPrincipalPolicies operation.
            - **policies** *(list) --* 
              The policies.
              - *(dict) --* 
                Describes an AWS IoT policy.
                - **policyName** *(string) --* 
                  The policy name.
                - **policyArn** *(string) --* 
                  The policy ARN.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type principal: string
        :param principal: **[REQUIRED]**
          The principal.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Specifies the order for results. If true, results are returned in ascending creation order.
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


class ListPrincipalThings(Paginator):
    def paginate(self, principal: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_principal_things`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPrincipalThings>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              principal='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'things': [
                    'string',
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the ListPrincipalThings operation.
            - **things** *(list) --* 
              The things.
              - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type principal: string
        :param principal: **[REQUIRED]**
          The principal.
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


class ListRoleAliases(Paginator):
    def paginate(self, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_role_aliases`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListRoleAliases>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ascendingOrder=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'roleAliases': [
                    'string',
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **roleAliases** *(list) --* 
              The role aliases.
              - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Return the list of role aliases in ascending alphabetical order.
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


class ListScheduledAudits(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_scheduled_audits`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListScheduledAudits>`_
        
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
                'scheduledAudits': [
                    {
                        'scheduledAuditName': 'string',
                        'scheduledAuditArn': 'string',
                        'frequency': 'DAILY'|'WEEKLY'|'BIWEEKLY'|'MONTHLY',
                        'dayOfMonth': 'string',
                        'dayOfWeek': 'SUN'|'MON'|'TUE'|'WED'|'THU'|'FRI'|'SAT'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **scheduledAudits** *(list) --* 
              The list of scheduled audits.
              - *(dict) --* 
                Information about the scheduled audit.
                - **scheduledAuditName** *(string) --* 
                  The name of the scheduled audit.
                - **scheduledAuditArn** *(string) --* 
                  The ARN of the scheduled audit.
                - **frequency** *(string) --* 
                  How often the scheduled audit takes place.
                - **dayOfMonth** *(string) --* 
                  The day of the month on which the scheduled audit is run (if the ``frequency`` is "MONTHLY"). If days 29-31 are specified, and the month does not have that many days, the audit takes place on the "LAST" day of the month.
                - **dayOfWeek** *(string) --* 
                  The day of the week on which the scheduled audit is run (if the ``frequency`` is "WEEKLY" or "BIWEEKLY").
            - **NextToken** *(string) --* 
              A token to resume pagination.
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
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_security_profiles`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListSecurityProfiles>`_
        
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
                'securityProfileIdentifiers': [
                    {
                        'name': 'string',
                        'arn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **securityProfileIdentifiers** *(list) --* 
              A list of security profile identifiers (names and ARNs).
              - *(dict) --* 
                Identifying information for a Device Defender security profile.
                - **name** *(string) --* 
                  The name you have given to the security profile.
                - **arn** *(string) --* 
                  The ARN of the security profile.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListSecurityProfilesForTarget(Paginator):
    def paginate(self, securityProfileTargetArn: str, recursive: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_security_profiles_for_target`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListSecurityProfilesForTarget>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              recursive=True|False,
              securityProfileTargetArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'securityProfileTargetMappings': [
                    {
                        'securityProfileIdentifier': {
                            'name': 'string',
                            'arn': 'string'
                        },
                        'target': {
                            'arn': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **securityProfileTargetMappings** *(list) --* 
              A list of security profiles and their associated targets.
              - *(dict) --* 
                Information about a security profile and the target associated with it.
                - **securityProfileIdentifier** *(dict) --* 
                  Information that identifies the security profile.
                  - **name** *(string) --* 
                    The name you have given to the security profile.
                  - **arn** *(string) --* 
                    The ARN of the security profile.
                - **target** *(dict) --* 
                  Information about the target (thing group) associated with the security profile.
                  - **arn** *(string) --* 
                    The ARN of the security profile.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type recursive: boolean
        :param recursive:
          If true, return child groups as well.
        :type securityProfileTargetArn: string
        :param securityProfileTargetArn: **[REQUIRED]**
          The ARN of the target (thing group) whose attached security profiles you want to get.
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


class ListStreams(Paginator):
    def paginate(self, ascendingOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_streams`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListStreams>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ascendingOrder=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'streams': [
                    {
                        'streamId': 'string',
                        'streamArn': 'string',
                        'streamVersion': 123,
                        'description': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **streams** *(list) --* 
              A list of streams.
              - *(dict) --* 
                A summary of a stream.
                - **streamId** *(string) --* 
                  The stream ID.
                - **streamArn** *(string) --* 
                  The stream ARN.
                - **streamVersion** *(integer) --* 
                  The stream version.
                - **description** *(string) --* 
                  A description of the stream.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ascendingOrder: boolean
        :param ascendingOrder:
          Set to true to return the list of streams in ascending order.
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


class ListTagsForResource(Paginator):
    def paginate(self, resourceArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_tags_for_resource`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListTagsForResource>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              resourceArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **tags** *(list) --* 
              The list of tags assigned to the resource.
              - *(dict) --* 
                A set of key/value pairs that are used to manage the resource.
                - **Key** *(string) --* 
                  The tag's key.
                - **Value** *(string) --* 
                  The tag's value.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**
          The ARN of the resource.
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


class ListTargetsForPolicy(Paginator):
    def paginate(self, policyName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_targets_for_policy`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListTargetsForPolicy>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              policyName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'targets': [
                    'string',
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **targets** *(list) --* 
              The policy targets.
              - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type policyName: string
        :param policyName: **[REQUIRED]**
          The policy name.
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


class ListTargetsForSecurityProfile(Paginator):
    def paginate(self, securityProfileName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_targets_for_security_profile`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListTargetsForSecurityProfile>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              securityProfileName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'securityProfileTargets': [
                    {
                        'arn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **securityProfileTargets** *(list) --* 
              The thing groups to which the security profile is attached.
              - *(dict) --* 
                A target to which an alert is sent when a security profile behavior is violated.
                - **arn** *(string) --* 
                  The ARN of the security profile.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type securityProfileName: string
        :param securityProfileName: **[REQUIRED]**
          The security profile.
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


class ListThingGroups(Paginator):
    def paginate(self, parentGroup: str = None, namePrefixFilter: str = None, recursive: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_thing_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              parentGroup='string',
              namePrefixFilter='string',
              recursive=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'thingGroups': [
                    {
                        'groupName': 'string',
                        'groupArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **thingGroups** *(list) --* 
              The thing groups.
              - *(dict) --* 
                The name and ARN of a group.
                - **groupName** *(string) --* 
                  The group name.
                - **groupArn** *(string) --* 
                  The group ARN.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type parentGroup: string
        :param parentGroup:
          A filter that limits the results to those with the specified parent group.
        :type namePrefixFilter: string
        :param namePrefixFilter:
          A filter that limits the results to those with the specified name prefix.
        :type recursive: boolean
        :param recursive:
          If true, return child groups as well.
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


class ListThingGroupsForThing(Paginator):
    def paginate(self, thingName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_thing_groups_for_thing`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingGroupsForThing>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              thingName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'thingGroups': [
                    {
                        'groupName': 'string',
                        'groupArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **thingGroups** *(list) --* 
              The thing groups.
              - *(dict) --* 
                The name and ARN of a group.
                - **groupName** *(string) --* 
                  The group name.
                - **groupArn** *(string) --* 
                  The group ARN.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type thingName: string
        :param thingName: **[REQUIRED]**
          The thing name.
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


class ListThingRegistrationTasks(Paginator):
    def paginate(self, status: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_thing_registration_tasks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingRegistrationTasks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              status='InProgress'|'Completed'|'Failed'|'Cancelled'|'Cancelling',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'taskIds': [
                    'string',
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **taskIds** *(list) --* 
              A list of bulk thing provisioning task IDs.
              - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type status: string
        :param status:
          The status of the bulk thing provisioning task.
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


class ListThingTypes(Paginator):
    def paginate(self, thingTypeName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_thing_types`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingTypes>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              thingTypeName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'thingTypes': [
                    {
                        'thingTypeName': 'string',
                        'thingTypeArn': 'string',
                        'thingTypeProperties': {
                            'thingTypeDescription': 'string',
                            'searchableAttributes': [
                                'string',
                            ]
                        },
                        'thingTypeMetadata': {
                            'deprecated': True|False,
                            'deprecationDate': datetime(2015, 1, 1),
                            'creationDate': datetime(2015, 1, 1)
                        }
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output for the ListThingTypes operation.
            - **thingTypes** *(list) --* 
              The thing types.
              - *(dict) --* 
                The definition of the thing type, including thing type name and description.
                - **thingTypeName** *(string) --* 
                  The name of the thing type.
                - **thingTypeArn** *(string) --* 
                  The thing type ARN.
                - **thingTypeProperties** *(dict) --* 
                  The ThingTypeProperties for the thing type.
                  - **thingTypeDescription** *(string) --* 
                    The description of the thing type.
                  - **searchableAttributes** *(list) --* 
                    A list of searchable thing attribute names.
                    - *(string) --* 
                - **thingTypeMetadata** *(dict) --* 
                  The ThingTypeMetadata contains additional information about the thing type including: creation date and time, a value indicating whether the thing type is deprecated, and a date and time when it was deprecated.
                  - **deprecated** *(boolean) --* 
                    Whether the thing type is deprecated. If **true** , no new things could be associated with this type.
                  - **deprecationDate** *(datetime) --* 
                    The date and time when the thing type was deprecated.
                  - **creationDate** *(datetime) --* 
                    The date and time when the thing type was created.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type thingTypeName: string
        :param thingTypeName:
          The name of the thing type.
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


class ListThings(Paginator):
    def paginate(self, attributeName: str = None, attributeValue: str = None, thingTypeName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_things`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThings>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              attributeName='string',
              attributeValue='string',
              thingTypeName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'things': [
                    {
                        'thingName': 'string',
                        'thingTypeName': 'string',
                        'thingArn': 'string',
                        'attributes': {
                            'string': 'string'
                        },
                        'version': 123
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the ListThings operation.
            - **things** *(list) --* 
              The things.
              - *(dict) --* 
                The properties of the thing, including thing name, thing type name, and a list of thing attributes.
                - **thingName** *(string) --* 
                  The name of the thing.
                - **thingTypeName** *(string) --* 
                  The name of the thing type, if the thing has been associated with a type.
                - **thingArn** *(string) --* 
                  The thing ARN.
                - **attributes** *(dict) --* 
                  A list of thing attributes which are name-value pairs.
                  - *(string) --* 
                    - *(string) --* 
                - **version** *(integer) --* 
                  The version of the thing record in the registry.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type attributeName: string
        :param attributeName:
          The attribute name used to search for things.
        :type attributeValue: string
        :param attributeValue:
          The attribute value used to search for things.
        :type thingTypeName: string
        :param thingTypeName:
          The name of the thing type used to search for things.
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


class ListThingsInBillingGroup(Paginator):
    def paginate(self, billingGroupName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_things_in_billing_group`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingsInBillingGroup>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              billingGroupName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'things': [
                    'string',
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **things** *(list) --* 
              A list of things in the billing group.
              - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type billingGroupName: string
        :param billingGroupName: **[REQUIRED]**
          The name of the billing group.
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


class ListThingsInThingGroup(Paginator):
    def paginate(self, thingGroupName: str, recursive: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_things_in_thing_group`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingsInThingGroup>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              thingGroupName='string',
              recursive=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'things': [
                    'string',
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **things** *(list) --* 
              The things in the specified thing group.
              - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type thingGroupName: string
        :param thingGroupName: **[REQUIRED]**
          The thing group name.
        :type recursive: boolean
        :param recursive:
          When true, list things in this thing group and in all child groups as well.
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


class ListTopicRules(Paginator):
    def paginate(self, topic: str = None, ruleDisabled: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_topic_rules`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListTopicRules>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              topic='string',
              ruleDisabled=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'rules': [
                    {
                        'ruleArn': 'string',
                        'ruleName': 'string',
                        'topicPattern': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'ruleDisabled': True|False
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The output from the ListTopicRules operation.
            - **rules** *(list) --* 
              The rules.
              - *(dict) --* 
                Describes a rule.
                - **ruleArn** *(string) --* 
                  The rule ARN.
                - **ruleName** *(string) --* 
                  The name of the rule.
                - **topicPattern** *(string) --* 
                  The pattern for the topic names that apply.
                - **createdAt** *(datetime) --* 
                  The date and time the rule was created.
                - **ruleDisabled** *(boolean) --* 
                  Specifies whether the rule is disabled.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type topic: string
        :param topic:
          The topic.
        :type ruleDisabled: boolean
        :param ruleDisabled:
          Specifies whether the rule is disabled.
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


class ListV2LoggingLevels(Paginator):
    def paginate(self, targetType: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_v2_logging_levels`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListV2LoggingLevels>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              targetType='DEFAULT'|'THING_GROUP',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'logTargetConfigurations': [
                    {
                        'logTarget': {
                            'targetType': 'DEFAULT'|'THING_GROUP',
                            'targetName': 'string'
                        },
                        'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **logTargetConfigurations** *(list) --* 
              The logging configuration for a target.
              - *(dict) --* 
                The target configuration.
                - **logTarget** *(dict) --* 
                  A log target
                  - **targetType** *(string) --* 
                    The target type.
                  - **targetName** *(string) --* 
                    The target name.
                - **logLevel** *(string) --* 
                  The logging level.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type targetType: string
        :param targetType:
          The type of resource for which you are configuring logging. Must be ``THING_Group`` .
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


class ListViolationEvents(Paginator):
    def paginate(self, startTime: datetime, endTime: datetime, thingName: str = None, securityProfileName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_violation_events`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListViolationEvents>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              startTime=datetime(2015, 1, 1),
              endTime=datetime(2015, 1, 1),
              thingName='string',
              securityProfileName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'violationEvents': [
                    {
                        'violationId': 'string',
                        'thingName': 'string',
                        'securityProfileName': 'string',
                        'behavior': {
                            'name': 'string',
                            'metric': 'string',
                            'criteria': {
                                'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                                'value': {
                                    'count': 123,
                                    'cidrs': [
                                        'string',
                                    ],
                                    'ports': [
                                        123,
                                    ]
                                },
                                'durationSeconds': 123,
                                'consecutiveDatapointsToAlarm': 123,
                                'consecutiveDatapointsToClear': 123,
                                'statisticalThreshold': {
                                    'statistic': 'string'
                                }
                            }
                        },
                        'metricValue': {
                            'count': 123,
                            'cidrs': [
                                'string',
                            ],
                            'ports': [
                                123,
                            ]
                        },
                        'violationEventType': 'in-alarm'|'alarm-cleared'|'alarm-invalidated',
                        'violationEventTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **violationEvents** *(list) --* 
              The security profile violation alerts issued for this account during the given time frame, potentially filtered by security profile, behavior violated, or thing (device) violating.
              - *(dict) --* 
                Information about a Device Defender security profile behavior violation.
                - **violationId** *(string) --* 
                  The ID of the violation event.
                - **thingName** *(string) --* 
                  The name of the thing responsible for the violation event.
                - **securityProfileName** *(string) --* 
                  The name of the security profile whose behavior was violated.
                - **behavior** *(dict) --* 
                  The behavior which was violated.
                  - **name** *(string) --* 
                    The name you have given to the behavior.
                  - **metric** *(string) --* 
                    What is measured by the behavior.
                  - **criteria** *(dict) --* 
                    The criteria that determine if a device is behaving normally in regard to the ``metric`` .
                    - **comparisonOperator** *(string) --* 
                      The operator that relates the thing measured (``metric`` ) to the criteria (containing a ``value`` or ``statisticalThreshold`` ).
                    - **value** *(dict) --* 
                      The value to be compared with the ``metric`` .
                      - **count** *(integer) --* 
                        If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric value to be compared with the ``metric`` .
                      - **cidrs** *(list) --* 
                        If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to be compared with the ``metric`` .
                        - *(string) --* 
                      - **ports** *(list) --* 
                        If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to be compared with the ``metric`` .
                        - *(integer) --* 
                    - **durationSeconds** *(integer) --* 
                      Use this to specify the time duration over which the behavior is evaluated, for those criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank.
                    - **consecutiveDatapointsToAlarm** *(integer) --* 
                      If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.
                    - **consecutiveDatapointsToClear** *(integer) --* 
                      If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.
                    - **statisticalThreshold** *(dict) --* 
                      A statistical ranking (percentile) which indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.
                      - **statistic** *(string) --* 
                        The percentile which resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (``durationSeconds`` ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (``comparisonOperator`` ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.
                - **metricValue** *(dict) --* 
                  The value of the metric (the measurement).
                  - **count** *(integer) --* 
                    If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric value to be compared with the ``metric`` .
                  - **cidrs** *(list) --* 
                    If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to be compared with the ``metric`` .
                    - *(string) --* 
                  - **ports** *(list) --* 
                    If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to be compared with the ``metric`` .
                    - *(integer) --* 
                - **violationEventType** *(string) --* 
                  The type of violation event.
                - **violationEventTime** *(datetime) --* 
                  The time the violation event occurred.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type startTime: datetime
        :param startTime: **[REQUIRED]**
          The start time for the alerts to be listed.
        :type endTime: datetime
        :param endTime: **[REQUIRED]**
          The end time for the alerts to be listed.
        :type thingName: string
        :param thingName:
          A filter to limit results to those alerts caused by the specified thing.
        :type securityProfileName: string
        :param securityProfileName:
          A filter to limit results to those alerts generated by the specified security profile.
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
