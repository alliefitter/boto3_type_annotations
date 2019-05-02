from typing import Dict
from typing import List
from botocore.paginate import Paginator


class DescribeActivations(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_activations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeActivations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'FilterKey': 'ActivationIds'|'DefaultInstanceName'|'IamRole',
                      'FilterValues': [
                          'string',
                      ]
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
                'ActivationList': [
                    {
                        'ActivationId': 'string',
                        'Description': 'string',
                        'DefaultInstanceName': 'string',
                        'IamRole': 'string',
                        'RegistrationLimit': 123,
                        'RegistrationsCount': 123,
                        'ExpirationDate': datetime(2015, 1, 1),
                        'Expired': True|False,
                        'CreatedDate': datetime(2015, 1, 1),
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ActivationList** *(list) --* 
              A list of activations for your AWS account.
              - *(dict) --* 
                An activation registers one or more on-premises servers or virtual machines (VMs) with AWS so that you can configure those servers or VMs using Run Command. A server or VM that has been registered with AWS is called a managed instance.
                - **ActivationId** *(string) --* 
                  The ID created by Systems Manager when you submitted the activation.
                - **Description** *(string) --* 
                  A user defined description of the activation.
                - **DefaultInstanceName** *(string) --* 
                  A name for the managed instance when it is created.
                - **IamRole** *(string) --* 
                  The Amazon Identity and Access Management (IAM) role to assign to the managed instance.
                - **RegistrationLimit** *(integer) --* 
                  The maximum number of managed instances that can be registered using this activation.
                - **RegistrationsCount** *(integer) --* 
                  The number of managed instances already registered with this activation.
                - **ExpirationDate** *(datetime) --* 
                  The date when this activation can no longer be used to register managed instances.
                - **Expired** *(boolean) --* 
                  Whether or not the activation is expired.
                - **CreatedDate** *(datetime) --* 
                  The date the activation was created.
                - **Tags** *(list) --* 
                  Tags assigned to the activation.
                  - *(dict) --* 
                    Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, Maintenance Windows, Parameter Store parameters, and patch baselines.
                    - **Key** *(string) --* 
                      The name of the tag.
                    - **Value** *(string) --* 
                      The value of the tag.
        :type Filters: list
        :param Filters:
          A filter to view information about your activations.
          - *(dict) --*
            Filter for the DescribeActivation API.
            - **FilterKey** *(string) --*
              The name of the filter.
            - **FilterValues** *(list) --*
              The filter values.
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


class DescribeAssociationExecutionTargets(Paginator):
    def paginate(self, AssociationId: str, ExecutionId: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_association_execution_targets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeAssociationExecutionTargets>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AssociationId='string',
              ExecutionId='string',
              Filters=[
                  {
                      'Key': 'Status'|'ResourceId'|'ResourceType',
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
                'AssociationExecutionTargets': [
                    {
                        'AssociationId': 'string',
                        'AssociationVersion': 'string',
                        'ExecutionId': 'string',
                        'ResourceId': 'string',
                        'ResourceType': 'string',
                        'Status': 'string',
                        'DetailedStatus': 'string',
                        'LastExecutionDate': datetime(2015, 1, 1),
                        'OutputSource': {
                            'OutputSourceId': 'string',
                            'OutputSourceType': 'string'
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AssociationExecutionTargets** *(list) --* 
              Information about the execution.
              - *(dict) --* 
                Includes information about the specified association execution.
                - **AssociationId** *(string) --* 
                  The association ID.
                - **AssociationVersion** *(string) --* 
                  The association version.
                - **ExecutionId** *(string) --* 
                  The execution ID.
                - **ResourceId** *(string) --* 
                  The resource ID, for example, the instance ID where the association ran.
                - **ResourceType** *(string) --* 
                  The resource type, for example, instance.
                - **Status** *(string) --* 
                  The association execution status.
                - **DetailedStatus** *(string) --* 
                  Detailed information about the execution status.
                - **LastExecutionDate** *(datetime) --* 
                  The date of the last execution.
                - **OutputSource** *(dict) --* 
                  The location where the association details are saved.
                  - **OutputSourceId** *(string) --* 
                    The ID of the output source, for example the URL of an Amazon S3 bucket.
                  - **OutputSourceType** *(string) --* 
                    The type of source where the association execution details are stored, for example, Amazon S3.
        :type AssociationId: string
        :param AssociationId: **[REQUIRED]**
          The association ID that includes the execution for which you want to view details.
        :type ExecutionId: string
        :param ExecutionId: **[REQUIRED]**
          The execution ID for which you want to view details.
        :type Filters: list
        :param Filters:
          Filters for the request. You can specify the following filters and values.
          Status (EQUAL)
          ResourceId (EQUAL)
          ResourceType (EQUAL)
          - *(dict) --*
            Filters for the association execution.
            - **Key** *(string) --* **[REQUIRED]**
              The key value used in the request.
            - **Value** *(string) --* **[REQUIRED]**
              The value specified for the key.
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


class DescribeAssociationExecutions(Paginator):
    def paginate(self, AssociationId: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_association_executions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeAssociationExecutions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AssociationId='string',
              Filters=[
                  {
                      'Key': 'ExecutionId'|'Status'|'CreatedTime',
                      'Value': 'string',
                      'Type': 'EQUAL'|'LESS_THAN'|'GREATER_THAN'
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
                'AssociationExecutions': [
                    {
                        'AssociationId': 'string',
                        'AssociationVersion': 'string',
                        'ExecutionId': 'string',
                        'Status': 'string',
                        'DetailedStatus': 'string',
                        'CreatedTime': datetime(2015, 1, 1),
                        'LastExecutionDate': datetime(2015, 1, 1),
                        'ResourceCountByStatus': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AssociationExecutions** *(list) --* 
              A list of the executions for the specified association ID.
              - *(dict) --* 
                Includes information about the specified association.
                - **AssociationId** *(string) --* 
                  The association ID.
                - **AssociationVersion** *(string) --* 
                  The association version.
                - **ExecutionId** *(string) --* 
                  The execution ID for the association.
                - **Status** *(string) --* 
                  The status of the association execution.
                - **DetailedStatus** *(string) --* 
                  Detailed status information about the execution.
                - **CreatedTime** *(datetime) --* 
                  The time the execution started.
                - **LastExecutionDate** *(datetime) --* 
                  The date of the last execution.
                - **ResourceCountByStatus** *(string) --* 
                  An aggregate status of the resources in the execution based on the status type.
        :type AssociationId: string
        :param AssociationId: **[REQUIRED]**
          The association ID for which you want to view execution history details.
        :type Filters: list
        :param Filters:
          Filters for the request. You can specify the following filters and values.
          ExecutionId (EQUAL)
          Status (EQUAL)
          CreatedTime (EQUAL, GREATER_THAN, LESS_THAN)
          - *(dict) --*
            Filters used in the request.
            - **Key** *(string) --* **[REQUIRED]**
              The key value used in the request.
            - **Value** *(string) --* **[REQUIRED]**
              The value specified for the key.
            - **Type** *(string) --* **[REQUIRED]**
              The filter type specified in the request.
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


class DescribeAutomationExecutions(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_automation_executions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeAutomationExecutions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Key': 'DocumentNamePrefix'|'ExecutionStatus'|'ExecutionId'|'ParentExecutionId'|'CurrentAction'|'StartTimeBefore'|'StartTimeAfter'|'AutomationType',
                      'Values': [
                          'string',
                      ]
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
                'AutomationExecutionMetadataList': [
                    {
                        'AutomationExecutionId': 'string',
                        'DocumentName': 'string',
                        'DocumentVersion': 'string',
                        'AutomationExecutionStatus': 'Pending'|'InProgress'|'Waiting'|'Success'|'TimedOut'|'Cancelling'|'Cancelled'|'Failed',
                        'ExecutionStartTime': datetime(2015, 1, 1),
                        'ExecutionEndTime': datetime(2015, 1, 1),
                        'ExecutedBy': 'string',
                        'LogFile': 'string',
                        'Outputs': {
                            'string': [
                                'string',
                            ]
                        },
                        'Mode': 'Auto'|'Interactive',
                        'ParentAutomationExecutionId': 'string',
                        'CurrentStepName': 'string',
                        'CurrentAction': 'string',
                        'FailureMessage': 'string',
                        'TargetParameterName': 'string',
                        'Targets': [
                            {
                                'Key': 'string',
                                'Values': [
                                    'string',
                                ]
                            },
                        ],
                        'TargetMaps': [
                            {
                                'string': [
                                    'string',
                                ]
                            },
                        ],
                        'ResolvedTargets': {
                            'ParameterValues': [
                                'string',
                            ],
                            'Truncated': True|False
                        },
                        'MaxConcurrency': 'string',
                        'MaxErrors': 'string',
                        'Target': 'string',
                        'AutomationType': 'CrossAccount'|'Local'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AutomationExecutionMetadataList** *(list) --* 
              The list of details about each automation execution which has occurred which matches the filter specification, if any.
              - *(dict) --* 
                Details about a specific Automation execution.
                - **AutomationExecutionId** *(string) --* 
                  The execution ID.
                - **DocumentName** *(string) --* 
                  The name of the Automation document used during execution.
                - **DocumentVersion** *(string) --* 
                  The document version used during the execution.
                - **AutomationExecutionStatus** *(string) --* 
                  The status of the execution. Valid values include: Running, Succeeded, Failed, Timed out, or Cancelled.
                - **ExecutionStartTime** *(datetime) --* 
                  The time the execution started.>
                - **ExecutionEndTime** *(datetime) --* 
                  The time the execution finished. This is not populated if the execution is still in progress.
                - **ExecutedBy** *(string) --* 
                  The IAM role ARN of the user who ran the Automation.
                - **LogFile** *(string) --* 
                  An Amazon S3 bucket where execution information is stored.
                - **Outputs** *(dict) --* 
                  The list of execution outputs as defined in the Automation document.
                  - *(string) --* 
                    - *(list) --* 
                      - *(string) --* 
                - **Mode** *(string) --* 
                  The Automation execution mode.
                - **ParentAutomationExecutionId** *(string) --* 
                  The ExecutionId of the parent Automation.
                - **CurrentStepName** *(string) --* 
                  The name of the step that is currently running.
                - **CurrentAction** *(string) --* 
                  The action of the step that is currently running.
                - **FailureMessage** *(string) --* 
                  The list of execution outputs as defined in the Automation document.
                - **TargetParameterName** *(string) --* 
                  The list of execution outputs as defined in the Automation document.
                - **Targets** *(list) --* 
                  The targets defined by the user when starting the Automation.
                  - *(dict) --* 
                    An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.
                    - **Key** *(string) --* 
                      User-defined criteria for sending commands that target instances that meet the criteria. ``Key`` can be ``tag:<Amazon EC2 tag>`` or ``InstanceIds`` . For more information about how to send commands that target instances using ``Key,Value`` parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
                    - **Values** *(list) --* 
                      User-defined criteria that maps to ``Key`` . For example, if you specified ``tag:ServerRole`` , you could specify ``value:WebServer`` to run a command on instances that include Amazon EC2 tags of ``ServerRole,WebServer`` . For more information about how to send commands that target instances using ``Key,Value`` parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
                      - *(string) --* 
                - **TargetMaps** *(list) --* 
                  The specified key-value mapping of document parameters to target resources.
                  - *(dict) --* 
                    - *(string) --* 
                      - *(list) --* 
                        - *(string) --* 
                - **ResolvedTargets** *(dict) --* 
                  A list of targets that resolved during the execution.
                  - **ParameterValues** *(list) --* 
                    A list of parameter values sent to targets that resolved during the Automation execution.
                    - *(string) --* 
                  - **Truncated** *(boolean) --* 
                    A boolean value indicating whether the resolved target list is truncated.
                - **MaxConcurrency** *(string) --* 
                  The MaxConcurrency value specified by the user when starting the Automation.
                - **MaxErrors** *(string) --* 
                  The MaxErrors value specified by the user when starting the Automation.
                - **Target** *(string) --* 
                  The list of execution outputs as defined in the Automation document.
                - **AutomationType** *(string) --* 
                  Use this filter with  DescribeAutomationExecutions . Specify either Local or CrossAccount. CrossAccount is an Automation that runs in multiple AWS Regions and accounts. For more information, see `Executing Automations in Multiple AWS Regions and Accounts <http://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation-multiple-accounts-and-regions.html>`__ in the *AWS Systems Manager User Guide* . 
        :type Filters: list
        :param Filters:
          Filters used to limit the scope of executions that are requested.
          - *(dict) --*
            A filter used to match specific automation executions. This is used to limit the scope of Automation execution information returned.
            - **Key** *(string) --* **[REQUIRED]**
              One or more keys to limit the results. Valid filter keys include the following: DocumentNamePrefix, ExecutionStatus, ExecutionId, ParentExecutionId, CurrentAction, StartTimeBefore, StartTimeAfter.
            - **Values** *(list) --* **[REQUIRED]**
              The values used to limit the execution information associated with the filter\'s key.
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


class DescribeAutomationStepExecutions(Paginator):
    def paginate(self, AutomationExecutionId: str, Filters: List = None, ReverseOrder: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_automation_step_executions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeAutomationStepExecutions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AutomationExecutionId='string',
              Filters=[
                  {
                      'Key': 'StartTimeBefore'|'StartTimeAfter'|'StepExecutionStatus'|'StepExecutionId'|'StepName'|'Action',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              ReverseOrder=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'StepExecutions': [
                    {
                        'StepName': 'string',
                        'Action': 'string',
                        'TimeoutSeconds': 123,
                        'OnFailure': 'string',
                        'MaxAttempts': 123,
                        'ExecutionStartTime': datetime(2015, 1, 1),
                        'ExecutionEndTime': datetime(2015, 1, 1),
                        'StepStatus': 'Pending'|'InProgress'|'Waiting'|'Success'|'TimedOut'|'Cancelling'|'Cancelled'|'Failed',
                        'ResponseCode': 'string',
                        'Inputs': {
                            'string': 'string'
                        },
                        'Outputs': {
                            'string': [
                                'string',
                            ]
                        },
                        'Response': 'string',
                        'FailureMessage': 'string',
                        'FailureDetails': {
                            'FailureStage': 'string',
                            'FailureType': 'string',
                            'Details': {
                                'string': [
                                    'string',
                                ]
                            }
                        },
                        'StepExecutionId': 'string',
                        'OverriddenParameters': {
                            'string': [
                                'string',
                            ]
                        },
                        'IsEnd': True|False,
                        'NextStep': 'string',
                        'IsCritical': True|False,
                        'ValidNextSteps': [
                            'string',
                        ],
                        'Targets': [
                            {
                                'Key': 'string',
                                'Values': [
                                    'string',
                                ]
                            },
                        ],
                        'TargetLocation': {
                            'Accounts': [
                                'string',
                            ],
                            'Regions': [
                                'string',
                            ],
                            'TargetLocationMaxConcurrency': 'string',
                            'TargetLocationMaxErrors': 'string',
                            'ExecutionRoleName': 'string'
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **StepExecutions** *(list) --* 
              A list of details about the current state of all steps that make up an execution.
              - *(dict) --* 
                Detailed information about an the execution state of an Automation step.
                - **StepName** *(string) --* 
                  The name of this execution step.
                - **Action** *(string) --* 
                  The action this step performs. The action determines the behavior of the step.
                - **TimeoutSeconds** *(integer) --* 
                  The timeout seconds of the step.
                - **OnFailure** *(string) --* 
                  The action to take if the step fails. The default value is Abort.
                - **MaxAttempts** *(integer) --* 
                  The maximum number of tries to run the action of the step. The default value is 1.
                - **ExecutionStartTime** *(datetime) --* 
                  If a step has begun execution, this contains the time the step started. If the step is in Pending status, this field is not populated.
                - **ExecutionEndTime** *(datetime) --* 
                  If a step has finished execution, this contains the time the execution ended. If the step has not yet concluded, this field is not populated.
                - **StepStatus** *(string) --* 
                  The execution status for this step. Valid values include: Pending, InProgress, Success, Cancelled, Failed, and TimedOut.
                - **ResponseCode** *(string) --* 
                  The response code returned by the execution of the step.
                - **Inputs** *(dict) --* 
                  Fully-resolved values passed into the step before execution.
                  - *(string) --* 
                    - *(string) --* 
                - **Outputs** *(dict) --* 
                  Returned values from the execution of the step.
                  - *(string) --* 
                    - *(list) --* 
                      - *(string) --* 
                - **Response** *(string) --* 
                  A message associated with the response code for an execution.
                - **FailureMessage** *(string) --* 
                  If a step failed, this message explains why the execution failed.
                - **FailureDetails** *(dict) --* 
                  Information about the Automation failure.
                  - **FailureStage** *(string) --* 
                    The stage of the Automation execution when the failure occurred. The stages include the following: InputValidation, PreVerification, Invocation, PostVerification.
                  - **FailureType** *(string) --* 
                    The type of Automation failure. Failure types include the following: Action, Permission, Throttling, Verification, Internal.
                  - **Details** *(dict) --* 
                    Detailed information about the Automation step failure.
                    - *(string) --* 
                      - *(list) --* 
                        - *(string) --* 
                - **StepExecutionId** *(string) --* 
                  The unique ID of a step execution.
                - **OverriddenParameters** *(dict) --* 
                  A user-specified list of parameters to override when running a step.
                  - *(string) --* 
                    - *(list) --* 
                      - *(string) --* 
                - **IsEnd** *(boolean) --* 
                  The flag which can be used to end automation no matter whether the step succeeds or fails.
                - **NextStep** *(string) --* 
                  The next step after the step succeeds.
                - **IsCritical** *(boolean) --* 
                  The flag which can be used to help decide whether the failure of current step leads to the Automation failure.
                - **ValidNextSteps** *(list) --* 
                  Strategies used when step fails, we support Continue and Abort. Abort will fail the automation when the step fails. Continue will ignore the failure of current step and allow automation to run the next step. With conditional branching, we add step:stepName to support the automation to go to another specific step.
                  - *(string) --* 
                - **Targets** *(list) --* 
                  The targets for the step execution.
                  - *(dict) --* 
                    An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.
                    - **Key** *(string) --* 
                      User-defined criteria for sending commands that target instances that meet the criteria. ``Key`` can be ``tag:<Amazon EC2 tag>`` or ``InstanceIds`` . For more information about how to send commands that target instances using ``Key,Value`` parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
                    - **Values** *(list) --* 
                      User-defined criteria that maps to ``Key`` . For example, if you specified ``tag:ServerRole`` , you could specify ``value:WebServer`` to run a command on instances that include Amazon EC2 tags of ``ServerRole,WebServer`` . For more information about how to send commands that target instances using ``Key,Value`` parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
                      - *(string) --* 
                - **TargetLocation** *(dict) --* 
                  The combination of AWS Regions and accounts targeted by the current Automation execution.
                  - **Accounts** *(list) --* 
                    The AWS accounts targeted by the current Automation execution.
                    - *(string) --* 
                  - **Regions** *(list) --* 
                    The AWS Regions targeted by the current Automation execution.
                    - *(string) --* 
                  - **TargetLocationMaxConcurrency** *(string) --* 
                    The maxium number of AWS accounts and AWS regions allowed to run the Automation concurrently 
                  - **TargetLocationMaxErrors** *(string) --* 
                    The maxium number of errors allowed before the system stops queueing additional Automation executions for the currently running Automation. 
                  - **ExecutionRoleName** *(string) --* 
                    The Automation execution role used by the currently running Automation.
        :type AutomationExecutionId: string
        :param AutomationExecutionId: **[REQUIRED]**
          The Automation execution ID for which you want step execution descriptions.
        :type Filters: list
        :param Filters:
          One or more filters to limit the number of step executions returned by the request.
          - *(dict) --*
            A filter to limit the amount of step execution information returned by the call.
            - **Key** *(string) --* **[REQUIRED]**
              One or more keys to limit the results. Valid filter keys include the following: StepName, Action, StepExecutionId, StepExecutionStatus, StartTimeBefore, StartTimeAfter.
            - **Values** *(list) --* **[REQUIRED]**
              The values of the filter key.
              - *(string) --*
        :type ReverseOrder: boolean
        :param ReverseOrder:
          A boolean that indicates whether to list step executions in reverse order by start time. The default value is false.
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


class DescribeAvailablePatches(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_available_patches`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeAvailablePatches>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
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
                'Patches': [
                    {
                        'Id': 'string',
                        'ReleaseDate': datetime(2015, 1, 1),
                        'Title': 'string',
                        'Description': 'string',
                        'ContentUrl': 'string',
                        'Vendor': 'string',
                        'ProductFamily': 'string',
                        'Product': 'string',
                        'Classification': 'string',
                        'MsrcSeverity': 'string',
                        'KbNumber': 'string',
                        'MsrcNumber': 'string',
                        'Language': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Patches** *(list) --* 
              An array of patches. Each entry in the array is a patch structure.
              - *(dict) --* 
                Represents metadata about a patch.
                - **Id** *(string) --* 
                  The ID of the patch (this is different than the Microsoft Knowledge Base ID).
                - **ReleaseDate** *(datetime) --* 
                  The date the patch was released.
                - **Title** *(string) --* 
                  The title of the patch.
                - **Description** *(string) --* 
                  The description of the patch.
                - **ContentUrl** *(string) --* 
                  The URL where more information can be obtained about the patch.
                - **Vendor** *(string) --* 
                  The name of the vendor providing the patch.
                - **ProductFamily** *(string) --* 
                  The product family the patch is applicable for (for example, Windows).
                - **Product** *(string) --* 
                  The specific product the patch is applicable for (for example, WindowsServer2016).
                - **Classification** *(string) --* 
                  The classification of the patch (for example, SecurityUpdates, Updates, CriticalUpdates).
                - **MsrcSeverity** *(string) --* 
                  The severity of the patch (for example Critical, Important, Moderate).
                - **KbNumber** *(string) --* 
                  The Microsoft Knowledge Base ID of the patch.
                - **MsrcNumber** *(string) --* 
                  The ID of the MSRC bulletin the patch is related to.
                - **Language** *(string) --* 
                  The language of the patch if it's language-specific.
        :type Filters: list
        :param Filters:
          Filters used to scope down the returned patches.
          - *(dict) --*
            Defines a filter used in Patch Manager APIs.
            - **Key** *(string) --*
              The key for the filter.
            - **Values** *(list) --*
              The value for the filter.
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


class DescribeEffectiveInstanceAssociations(Paginator):
    def paginate(self, InstanceId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_effective_instance_associations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeEffectiveInstanceAssociations>`_
        
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
                'Associations': [
                    {
                        'AssociationId': 'string',
                        'InstanceId': 'string',
                        'Content': 'string',
                        'AssociationVersion': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Associations** *(list) --* 
              The associations for the requested instance.
              - *(dict) --* 
                One or more association documents on the instance. 
                - **AssociationId** *(string) --* 
                  The association ID.
                - **InstanceId** *(string) --* 
                  The instance ID.
                - **Content** *(string) --* 
                  The content of the association document for the instance(s).
                - **AssociationVersion** *(string) --* 
                  Version information for the association on the instance.
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**
          The instance ID for which you want to view all associations.
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


class DescribeEffectivePatchesForPatchBaseline(Paginator):
    def paginate(self, BaselineId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_effective_patches_for_patch_baseline`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeEffectivePatchesForPatchBaseline>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              BaselineId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'EffectivePatches': [
                    {
                        'Patch': {
                            'Id': 'string',
                            'ReleaseDate': datetime(2015, 1, 1),
                            'Title': 'string',
                            'Description': 'string',
                            'ContentUrl': 'string',
                            'Vendor': 'string',
                            'ProductFamily': 'string',
                            'Product': 'string',
                            'Classification': 'string',
                            'MsrcSeverity': 'string',
                            'KbNumber': 'string',
                            'MsrcNumber': 'string',
                            'Language': 'string'
                        },
                        'PatchStatus': {
                            'DeploymentStatus': 'APPROVED'|'PENDING_APPROVAL'|'EXPLICIT_APPROVED'|'EXPLICIT_REJECTED',
                            'ComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                            'ApprovalDate': datetime(2015, 1, 1)
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EffectivePatches** *(list) --* 
              An array of patches and patch status.
              - *(dict) --* 
                The EffectivePatch structure defines metadata about a patch along with the approval state of the patch in a particular patch baseline. The approval state includes information about whether the patch is currently approved, due to be approved by a rule, explicitly approved, or explicitly rejected and the date the patch was or will be approved.
                - **Patch** *(dict) --* 
                  Provides metadata for a patch, including information such as the KB ID, severity, classification and a URL for where more information can be obtained about the patch.
                  - **Id** *(string) --* 
                    The ID of the patch (this is different than the Microsoft Knowledge Base ID).
                  - **ReleaseDate** *(datetime) --* 
                    The date the patch was released.
                  - **Title** *(string) --* 
                    The title of the patch.
                  - **Description** *(string) --* 
                    The description of the patch.
                  - **ContentUrl** *(string) --* 
                    The URL where more information can be obtained about the patch.
                  - **Vendor** *(string) --* 
                    The name of the vendor providing the patch.
                  - **ProductFamily** *(string) --* 
                    The product family the patch is applicable for (for example, Windows).
                  - **Product** *(string) --* 
                    The specific product the patch is applicable for (for example, WindowsServer2016).
                  - **Classification** *(string) --* 
                    The classification of the patch (for example, SecurityUpdates, Updates, CriticalUpdates).
                  - **MsrcSeverity** *(string) --* 
                    The severity of the patch (for example Critical, Important, Moderate).
                  - **KbNumber** *(string) --* 
                    The Microsoft Knowledge Base ID of the patch.
                  - **MsrcNumber** *(string) --* 
                    The ID of the MSRC bulletin the patch is related to.
                  - **Language** *(string) --* 
                    The language of the patch if it's language-specific.
                - **PatchStatus** *(dict) --* 
                  The status of the patch in a patch baseline. This includes information about whether the patch is currently approved, due to be approved by a rule, explicitly approved, or explicitly rejected and the date the patch was or will be approved.
                  - **DeploymentStatus** *(string) --* 
                    The approval status of a patch (APPROVED, PENDING_APPROVAL, EXPLICIT_APPROVED, EXPLICIT_REJECTED).
                  - **ComplianceLevel** *(string) --* 
                    The compliance severity level for a patch.
                  - **ApprovalDate** *(datetime) --* 
                    The date the patch was approved (or will be approved if the status is PENDING_APPROVAL).
        :type BaselineId: string
        :param BaselineId: **[REQUIRED]**
          The ID of the patch baseline to retrieve the effective patches for.
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


class DescribeInstanceAssociationsStatus(Paginator):
    def paginate(self, InstanceId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_instance_associations_status`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstanceAssociationsStatus>`_
        
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
                'InstanceAssociationStatusInfos': [
                    {
                        'AssociationId': 'string',
                        'Name': 'string',
                        'DocumentVersion': 'string',
                        'AssociationVersion': 'string',
                        'InstanceId': 'string',
                        'ExecutionDate': datetime(2015, 1, 1),
                        'Status': 'string',
                        'DetailedStatus': 'string',
                        'ExecutionSummary': 'string',
                        'ErrorCode': 'string',
                        'OutputUrl': {
                            'S3OutputUrl': {
                                'OutputUrl': 'string'
                            }
                        },
                        'AssociationName': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **InstanceAssociationStatusInfos** *(list) --* 
              Status information about the association.
              - *(dict) --* 
                Status information about the instance association.
                - **AssociationId** *(string) --* 
                  The association ID.
                - **Name** *(string) --* 
                  The name of the association.
                - **DocumentVersion** *(string) --* 
                  The association document verions.
                - **AssociationVersion** *(string) --* 
                  The version of the association applied to the instance.
                - **InstanceId** *(string) --* 
                  The instance ID where the association was created.
                - **ExecutionDate** *(datetime) --* 
                  The date the instance association ran. 
                - **Status** *(string) --* 
                  Status information about the instance association.
                - **DetailedStatus** *(string) --* 
                  Detailed status information about the instance association.
                - **ExecutionSummary** *(string) --* 
                  Summary information about association execution.
                - **ErrorCode** *(string) --* 
                  An error code returned by the request to create the association.
                - **OutputUrl** *(dict) --* 
                  A URL for an Amazon S3 bucket where you want to store the results of this request.
                  - **S3OutputUrl** *(dict) --* 
                    The URL of Amazon S3 bucket where you want to store the results of this request.
                    - **OutputUrl** *(string) --* 
                      A URL for an Amazon S3 bucket where you want to store the results of this request.
                - **AssociationName** *(string) --* 
                  The name of the association applied to the instance.
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**
          The instance IDs for which you want association status information.
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


class DescribeInstanceInformation(Paginator):
    def paginate(self, InstanceInformationFilterList: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_instance_information`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstanceInformation>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              InstanceInformationFilterList=[
                  {
                      'key': 'InstanceIds'|'AgentVersion'|'PingStatus'|'PlatformTypes'|'ActivationIds'|'IamRole'|'ResourceType'|'AssociationStatus',
                      'valueSet': [
                          'string',
                      ]
                  },
              ],
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
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
                'InstanceInformationList': [
                    {
                        'InstanceId': 'string',
                        'PingStatus': 'Online'|'ConnectionLost'|'Inactive',
                        'LastPingDateTime': datetime(2015, 1, 1),
                        'AgentVersion': 'string',
                        'IsLatestVersion': True|False,
                        'PlatformType': 'Windows'|'Linux',
                        'PlatformName': 'string',
                        'PlatformVersion': 'string',
                        'ActivationId': 'string',
                        'IamRole': 'string',
                        'RegistrationDate': datetime(2015, 1, 1),
                        'ResourceType': 'ManagedInstance'|'Document'|'EC2Instance',
                        'Name': 'string',
                        'IPAddress': 'string',
                        'ComputerName': 'string',
                        'AssociationStatus': 'string',
                        'LastAssociationExecutionDate': datetime(2015, 1, 1),
                        'LastSuccessfulAssociationExecutionDate': datetime(2015, 1, 1),
                        'AssociationOverview': {
                            'DetailedStatus': 'string',
                            'InstanceAssociationStatusAggregatedCount': {
                                'string': 123
                            }
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **InstanceInformationList** *(list) --* 
              The instance information list.
              - *(dict) --* 
                Describes a filter for a specific list of instances. 
                - **InstanceId** *(string) --* 
                  The instance ID. 
                - **PingStatus** *(string) --* 
                  Connection status of SSM Agent. 
                - **LastPingDateTime** *(datetime) --* 
                  The date and time when agent last pinged Systems Manager service. 
                - **AgentVersion** *(string) --* 
                  The version of SSM Agent running on your Linux instance. 
                - **IsLatestVersion** *(boolean) --* 
                  Indicates whether latest version of SSM Agent is running on your instance. Some older versions of Windows Server use the EC2Config service to process SSM requests. For this reason, this field does not indicate whether or not the latest version is installed on Windows managed instances.
                - **PlatformType** *(string) --* 
                  The operating system platform type. 
                - **PlatformName** *(string) --* 
                  The name of the operating system platform running on your instance. 
                - **PlatformVersion** *(string) --* 
                  The version of the OS platform running on your instance. 
                - **ActivationId** *(string) --* 
                  The activation ID created by Systems Manager when the server or VM was registered.
                - **IamRole** *(string) --* 
                  The Amazon Identity and Access Management (IAM) role assigned to the on-premises Systems Manager managed instances. This call does not return the IAM role for Amazon EC2 instances. 
                - **RegistrationDate** *(datetime) --* 
                  The date the server or VM was registered with AWS as a managed instance.
                - **ResourceType** *(string) --* 
                  The type of instance. Instances are either EC2 instances or managed instances. 
                - **Name** *(string) --* 
                  The name of the managed instance.
                - **IPAddress** *(string) --* 
                  The IP address of the managed instance.
                - **ComputerName** *(string) --* 
                  The fully qualified host name of the managed instance.
                - **AssociationStatus** *(string) --* 
                  The status of the association.
                - **LastAssociationExecutionDate** *(datetime) --* 
                  The date the association was last run.
                - **LastSuccessfulAssociationExecutionDate** *(datetime) --* 
                  The last date the association was successfully run.
                - **AssociationOverview** *(dict) --* 
                  Information about the association.
                  - **DetailedStatus** *(string) --* 
                    Detailed status information about the aggregated associations.
                  - **InstanceAssociationStatusAggregatedCount** *(dict) --* 
                    The number of associations for the instance(s).
                    - *(string) --* 
                      - *(integer) --* 
        :type InstanceInformationFilterList: list
        :param InstanceInformationFilterList:
          This is a legacy method. We recommend that you don\'t use this method. Instead, use the  InstanceInformationFilter action. The ``InstanceInformationFilter`` action enables you to return instance information by using tags that are specified as a key-value mapping.
          If you do use this method, then you can\'t use the ``InstanceInformationFilter`` action. Using this method and the ``InstanceInformationFilter`` action causes an exception error.
          - *(dict) --*
            Describes a filter for a specific list of instances. You can filter instances information by using tags. You specify tags by using a key-value mapping.
            Use this action instead of the  DescribeInstanceInformationRequest$InstanceInformationFilterList method. The ``InstanceInformationFilterList`` method is a legacy method and does not support tags.
            - **key** *(string) --* **[REQUIRED]**
              The name of the filter.
            - **valueSet** *(list) --* **[REQUIRED]**
              The filter values.
              - *(string) --*
        :type Filters: list
        :param Filters:
          One or more filters. Use a filter to return a more specific list of instances. You can filter on Amazon EC2 tag. Specify tags by using a key-value mapping.
          - *(dict) --*
            The filters to describe or get information about your managed instances.
            - **Key** *(string) --* **[REQUIRED]**
              The filter key name to describe your instances. For example:
              \"InstanceIds\"|\"AgentVersion\"|\"PingStatus\"|\"PlatformTypes\"|\"ActivationIds\"|\"IamRole\"|\"ResourceType\"|\"AssociationStatus\"|\"Tag Key\"
            - **Values** *(list) --* **[REQUIRED]**
              The filter values.
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


class DescribeInstancePatchStates(Paginator):
    def paginate(self, InstanceIds: List, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_instance_patch_states`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstancePatchStates>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              InstanceIds=[
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
                'InstancePatchStates': [
                    {
                        'InstanceId': 'string',
                        'PatchGroup': 'string',
                        'BaselineId': 'string',
                        'SnapshotId': 'string',
                        'InstallOverrideList': 'string',
                        'OwnerInformation': 'string',
                        'InstalledCount': 123,
                        'InstalledOtherCount': 123,
                        'InstalledRejectedCount': 123,
                        'MissingCount': 123,
                        'FailedCount': 123,
                        'NotApplicableCount': 123,
                        'OperationStartTime': datetime(2015, 1, 1),
                        'OperationEndTime': datetime(2015, 1, 1),
                        'Operation': 'Scan'|'Install'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **InstancePatchStates** *(list) --* 
              The high-level patch state for the requested instances.
              - *(dict) --* 
                Defines the high-level patch compliance state for a managed instance, providing information about the number of installed, missing, not applicable, and failed patches along with metadata about the operation when this information was gathered for the instance.
                - **InstanceId** *(string) --* 
                  The ID of the managed instance the high-level patch compliance information was collected for.
                - **PatchGroup** *(string) --* 
                  The name of the patch group the managed instance belongs to.
                - **BaselineId** *(string) --* 
                  The ID of the patch baseline used to patch the instance.
                - **SnapshotId** *(string) --* 
                  The ID of the patch baseline snapshot used during the patching operation when this compliance data was collected.
                - **InstallOverrideList** *(string) --* 
                  An https URL or an Amazon S3 path-style URL to a list of patches to be installed. This patch installation list, which you maintain in an Amazon S3 bucket in YAML format and specify in the SSM document ``AWS-RunPatchBaseline`` , overrides the patches specified by the default patch baseline.
                  For more information about the ``InstallOverrideList`` parameter, see `About the SSM Document AWS-RunPatchBaseline <http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-about-aws-runpatchbaseline.html>`__ in the *AWS Systems Manager User Guide* .
                - **OwnerInformation** *(string) --* 
                  Placeholder information. This field will always be empty in the current release of the service.
                - **InstalledCount** *(integer) --* 
                  The number of patches from the patch baseline that are installed on the instance.
                - **InstalledOtherCount** *(integer) --* 
                  The number of patches not specified in the patch baseline that are installed on the instance.
                - **InstalledRejectedCount** *(integer) --* 
                  The number of instances with patches installed that are specified in a RejectedPatches list. Patches with a status of *InstalledRejected* were typically installed before they were added to a RejectedPatches list.
                  .. note::
                    If ALLOW_AS_DEPENDENCY is the specified option for RejectedPatchesAction, the value of InstalledRejectedCount will always be 0 (zero).
                - **MissingCount** *(integer) --* 
                  The number of patches from the patch baseline that are applicable for the instance but aren't currently installed.
                - **FailedCount** *(integer) --* 
                  The number of patches from the patch baseline that were attempted to be installed during the last patching operation, but failed to install.
                - **NotApplicableCount** *(integer) --* 
                  The number of patches from the patch baseline that aren't applicable for the instance and hence aren't installed on the instance.
                - **OperationStartTime** *(datetime) --* 
                  The time the most recent patching operation was started on the instance.
                - **OperationEndTime** *(datetime) --* 
                  The time the most recent patching operation completed on the instance.
                - **Operation** *(string) --* 
                  The type of patching operation that was performed: SCAN (assess patch compliance state) or INSTALL (install missing patches).
        :type InstanceIds: list
        :param InstanceIds: **[REQUIRED]**
          The ID of the instance whose patch state information should be retrieved.
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


class DescribeInstancePatchStatesForPatchGroup(Paginator):
    def paginate(self, PatchGroup: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_instance_patch_states_for_patch_group`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstancePatchStatesForPatchGroup>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PatchGroup='string',
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ],
                      'Type': 'Equal'|'NotEqual'|'LessThan'|'GreaterThan'
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
                'InstancePatchStates': [
                    {
                        'InstanceId': 'string',
                        'PatchGroup': 'string',
                        'BaselineId': 'string',
                        'SnapshotId': 'string',
                        'InstallOverrideList': 'string',
                        'OwnerInformation': 'string',
                        'InstalledCount': 123,
                        'InstalledOtherCount': 123,
                        'InstalledRejectedCount': 123,
                        'MissingCount': 123,
                        'FailedCount': 123,
                        'NotApplicableCount': 123,
                        'OperationStartTime': datetime(2015, 1, 1),
                        'OperationEndTime': datetime(2015, 1, 1),
                        'Operation': 'Scan'|'Install'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **InstancePatchStates** *(list) --* 
              The high-level patch state for the requested instances. 
              - *(dict) --* 
                Defines the high-level patch compliance state for a managed instance, providing information about the number of installed, missing, not applicable, and failed patches along with metadata about the operation when this information was gathered for the instance.
                - **InstanceId** *(string) --* 
                  The ID of the managed instance the high-level patch compliance information was collected for.
                - **PatchGroup** *(string) --* 
                  The name of the patch group the managed instance belongs to.
                - **BaselineId** *(string) --* 
                  The ID of the patch baseline used to patch the instance.
                - **SnapshotId** *(string) --* 
                  The ID of the patch baseline snapshot used during the patching operation when this compliance data was collected.
                - **InstallOverrideList** *(string) --* 
                  An https URL or an Amazon S3 path-style URL to a list of patches to be installed. This patch installation list, which you maintain in an Amazon S3 bucket in YAML format and specify in the SSM document ``AWS-RunPatchBaseline`` , overrides the patches specified by the default patch baseline.
                  For more information about the ``InstallOverrideList`` parameter, see `About the SSM Document AWS-RunPatchBaseline <http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-about-aws-runpatchbaseline.html>`__ in the *AWS Systems Manager User Guide* .
                - **OwnerInformation** *(string) --* 
                  Placeholder information. This field will always be empty in the current release of the service.
                - **InstalledCount** *(integer) --* 
                  The number of patches from the patch baseline that are installed on the instance.
                - **InstalledOtherCount** *(integer) --* 
                  The number of patches not specified in the patch baseline that are installed on the instance.
                - **InstalledRejectedCount** *(integer) --* 
                  The number of instances with patches installed that are specified in a RejectedPatches list. Patches with a status of *InstalledRejected* were typically installed before they were added to a RejectedPatches list.
                  .. note::
                    If ALLOW_AS_DEPENDENCY is the specified option for RejectedPatchesAction, the value of InstalledRejectedCount will always be 0 (zero).
                - **MissingCount** *(integer) --* 
                  The number of patches from the patch baseline that are applicable for the instance but aren't currently installed.
                - **FailedCount** *(integer) --* 
                  The number of patches from the patch baseline that were attempted to be installed during the last patching operation, but failed to install.
                - **NotApplicableCount** *(integer) --* 
                  The number of patches from the patch baseline that aren't applicable for the instance and hence aren't installed on the instance.
                - **OperationStartTime** *(datetime) --* 
                  The time the most recent patching operation was started on the instance.
                - **OperationEndTime** *(datetime) --* 
                  The time the most recent patching operation completed on the instance.
                - **Operation** *(string) --* 
                  The type of patching operation that was performed: SCAN (assess patch compliance state) or INSTALL (install missing patches).
        :type PatchGroup: string
        :param PatchGroup: **[REQUIRED]**
          The name of the patch group for which the patch state information should be retrieved.
        :type Filters: list
        :param Filters:
          Each entry in the array is a structure containing:
          Key (string between 1 and 200 characters)
          Values (array containing a single string)
          Type (string \"Equal\", \"NotEqual\", \"LessThan\", \"GreaterThan\")
          - *(dict) --*
            Defines a filter used in DescribeInstancePatchStatesForPatchGroup used to scope down the information returned by the API.
            - **Key** *(string) --* **[REQUIRED]**
              The key for the filter. Supported values are FailedCount, InstalledCount, InstalledOtherCount, MissingCount and NotApplicableCount.
            - **Values** *(list) --* **[REQUIRED]**
              The value for the filter, must be an integer greater than or equal to 0.
              - *(string) --*
            - **Type** *(string) --* **[REQUIRED]**
              The type of comparison that should be performed for the value: Equal, NotEqual, LessThan or GreaterThan.
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


class DescribeInstancePatches(Paginator):
    def paginate(self, InstanceId: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_instance_patches`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstancePatches>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              InstanceId='string',
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
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
                'Patches': [
                    {
                        'Title': 'string',
                        'KBId': 'string',
                        'Classification': 'string',
                        'Severity': 'string',
                        'State': 'INSTALLED'|'INSTALLED_OTHER'|'INSTALLED_REJECTED'|'MISSING'|'NOT_APPLICABLE'|'FAILED',
                        'InstalledTime': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Patches** *(list) --* 
              Each entry in the array is a structure containing:
              Title (string)
              KBId (string)
              Classification (string)
              Severity (string)
              State (string, such as "INSTALLED" or "FAILED")
              InstalledTime (DateTime)
              InstalledBy (string)
              - *(dict) --* 
                Information about the state of a patch on a particular instance as it relates to the patch baseline used to patch the instance.
                - **Title** *(string) --* 
                  The title of the patch.
                - **KBId** *(string) --* 
                  The operating system-specific ID of the patch.
                - **Classification** *(string) --* 
                  The classification of the patch (for example, SecurityUpdates, Updates, CriticalUpdates).
                - **Severity** *(string) --* 
                  The severity of the patch (for example, Critical, Important, Moderate).
                - **State** *(string) --* 
                  The state of the patch on the instance, such as INSTALLED or FAILED.
                  For descriptions of each patch state, see `About Patch Compliance <http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-compliance-about.html#sysman-compliance-monitor-patch>`__ in the *AWS Systems Manager User Guide* .
                - **InstalledTime** *(datetime) --* 
                  The date/time the patch was installed on the instance. Note that not all operating systems provide this level of information.
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**
          The ID of the instance whose patch state information should be retrieved.
        :type Filters: list
        :param Filters:
          Each entry in the array is a structure containing:
          Key (string, between 1 and 128 characters)
          Values (array of strings, each string between 1 and 256 characters)
          - *(dict) --*
            Defines a filter used in Patch Manager APIs.
            - **Key** *(string) --*
              The key for the filter.
            - **Values** *(list) --*
              The value for the filter.
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


class DescribeInventoryDeletions(Paginator):
    def paginate(self, DeletionId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_inventory_deletions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInventoryDeletions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DeletionId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'InventoryDeletions': [
                    {
                        'DeletionId': 'string',
                        'TypeName': 'string',
                        'DeletionStartTime': datetime(2015, 1, 1),
                        'LastStatus': 'InProgress'|'Complete',
                        'LastStatusMessage': 'string',
                        'DeletionSummary': {
                            'TotalCount': 123,
                            'RemainingCount': 123,
                            'SummaryItems': [
                                {
                                    'Version': 'string',
                                    'Count': 123,
                                    'RemainingCount': 123
                                },
                            ]
                        },
                        'LastStatusUpdateTime': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **InventoryDeletions** *(list) --* 
              A list of status items for deleted inventory.
              - *(dict) --* 
                Status information returned by the ``DeleteInventory`` action.
                - **DeletionId** *(string) --* 
                  The deletion ID returned by the ``DeleteInventory`` action.
                - **TypeName** *(string) --* 
                  The name of the inventory data type.
                - **DeletionStartTime** *(datetime) --* 
                  The UTC timestamp when the delete operation started.
                - **LastStatus** *(string) --* 
                  The status of the operation. Possible values are InProgress and Complete.
                - **LastStatusMessage** *(string) --* 
                  Information about the status.
                - **DeletionSummary** *(dict) --* 
                  Information about the delete operation. For more information about this summary, see `Understanding the Delete Inventory Summary <http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-delete.html#sysman-inventory-delete-summary>`__ in the *AWS Systems Manager User Guide* .
                  - **TotalCount** *(integer) --* 
                    The total number of items to delete. This count does not change during the delete operation.
                  - **RemainingCount** *(integer) --* 
                    Remaining number of items to delete.
                  - **SummaryItems** *(list) --* 
                    A list of counts and versions for deleted items.
                    - *(dict) --* 
                      Either a count, remaining count, or a version number in a delete inventory summary.
                      - **Version** *(string) --* 
                        The inventory type version.
                      - **Count** *(integer) --* 
                        A count of the number of deleted items.
                      - **RemainingCount** *(integer) --* 
                        The remaining number of items to delete.
                - **LastStatusUpdateTime** *(datetime) --* 
                  The UTC timestamp of when the last status report.
        :type DeletionId: string
        :param DeletionId:
          Specify the delete inventory ID for which you want information. This ID was returned by the ``DeleteInventory`` action.
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


class DescribeMaintenanceWindowExecutionTaskInvocations(Paginator):
    def paginate(self, WindowExecutionId: str, TaskId: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_maintenance_window_execution_task_invocations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTaskInvocations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              WindowExecutionId='string',
              TaskId='string',
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
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
                'WindowExecutionTaskInvocationIdentities': [
                    {
                        'WindowExecutionId': 'string',
                        'TaskExecutionId': 'string',
                        'InvocationId': 'string',
                        'ExecutionId': 'string',
                        'TaskType': 'RUN_COMMAND'|'AUTOMATION'|'STEP_FUNCTIONS'|'LAMBDA',
                        'Parameters': 'string',
                        'Status': 'PENDING'|'IN_PROGRESS'|'SUCCESS'|'FAILED'|'TIMED_OUT'|'CANCELLING'|'CANCELLED'|'SKIPPED_OVERLAPPING',
                        'StatusDetails': 'string',
                        'StartTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'OwnerInformation': 'string',
                        'WindowTargetId': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **WindowExecutionTaskInvocationIdentities** *(list) --* 
              Information about the task invocation results per invocation.
              - *(dict) --* 
                Describes the information about a task invocation for a particular target as part of a task execution performed as part of a Maintenance Window execution.
                - **WindowExecutionId** *(string) --* 
                  The ID of the Maintenance Window execution that ran the task.
                - **TaskExecutionId** *(string) --* 
                  The ID of the specific task execution in the Maintenance Window execution.
                - **InvocationId** *(string) --* 
                  The ID of the task invocation.
                - **ExecutionId** *(string) --* 
                  The ID of the action performed in the service that actually handled the task invocation. If the task type is RUN_COMMAND, this value is the command ID.
                - **TaskType** *(string) --* 
                  The task type.
                - **Parameters** *(string) --* 
                  The parameters that were provided for the invocation when it was run.
                - **Status** *(string) --* 
                  The status of the task invocation.
                - **StatusDetails** *(string) --* 
                  The details explaining the status of the task invocation. Only available for certain Status values. 
                - **StartTime** *(datetime) --* 
                  The time the invocation started.
                - **EndTime** *(datetime) --* 
                  The time the invocation finished.
                - **OwnerInformation** *(string) --* 
                  User-provided value that was specified when the target was registered with the Maintenance Window. This was also included in any CloudWatch events raised during the task invocation.
                - **WindowTargetId** *(string) --* 
                  The ID of the target definition in this Maintenance Window the invocation was performed for.
        :type WindowExecutionId: string
        :param WindowExecutionId: **[REQUIRED]**
          The ID of the Maintenance Window execution the task is part of.
        :type TaskId: string
        :param TaskId: **[REQUIRED]**
          The ID of the specific task in the Maintenance Window task that should be retrieved.
        :type Filters: list
        :param Filters:
          Optional filters used to scope down the returned task invocations. The supported filter key is STATUS with the corresponding values PENDING, IN_PROGRESS, SUCCESS, FAILED, TIMED_OUT, CANCELLING, and CANCELLED.
          - *(dict) --*
            Filter used in the request. Supported filter keys are Name and Enabled.
            - **Key** *(string) --*
              The name of the filter.
            - **Values** *(list) --*
              The filter values.
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


class DescribeMaintenanceWindowExecutionTasks(Paginator):
    def paginate(self, WindowExecutionId: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_maintenance_window_execution_tasks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTasks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              WindowExecutionId='string',
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
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
                'WindowExecutionTaskIdentities': [
                    {
                        'WindowExecutionId': 'string',
                        'TaskExecutionId': 'string',
                        'Status': 'PENDING'|'IN_PROGRESS'|'SUCCESS'|'FAILED'|'TIMED_OUT'|'CANCELLING'|'CANCELLED'|'SKIPPED_OVERLAPPING',
                        'StatusDetails': 'string',
                        'StartTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'TaskArn': 'string',
                        'TaskType': 'RUN_COMMAND'|'AUTOMATION'|'STEP_FUNCTIONS'|'LAMBDA'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **WindowExecutionTaskIdentities** *(list) --* 
              Information about the task executions.
              - *(dict) --* 
                Information about a task execution performed as part of a Maintenance Window execution.
                - **WindowExecutionId** *(string) --* 
                  The ID of the Maintenance Window execution that ran the task.
                - **TaskExecutionId** *(string) --* 
                  The ID of the specific task execution in the Maintenance Window execution.
                - **Status** *(string) --* 
                  The status of the task execution.
                - **StatusDetails** *(string) --* 
                  The details explaining the status of the task execution. Only available for certain status values.
                - **StartTime** *(datetime) --* 
                  The time the task execution started.
                - **EndTime** *(datetime) --* 
                  The time the task execution finished.
                - **TaskArn** *(string) --* 
                  The ARN of the task that ran.
                - **TaskType** *(string) --* 
                  The type of task that ran.
        :type WindowExecutionId: string
        :param WindowExecutionId: **[REQUIRED]**
          The ID of the Maintenance Window execution whose task executions should be retrieved.
        :type Filters: list
        :param Filters:
          Optional filters used to scope down the returned tasks. The supported filter key is STATUS with the corresponding values PENDING, IN_PROGRESS, SUCCESS, FAILED, TIMED_OUT, CANCELLING, and CANCELLED.
          - *(dict) --*
            Filter used in the request. Supported filter keys are Name and Enabled.
            - **Key** *(string) --*
              The name of the filter.
            - **Values** *(list) --*
              The filter values.
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


class DescribeMaintenanceWindowExecutions(Paginator):
    def paginate(self, WindowId: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_maintenance_window_executions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowExecutions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              WindowId='string',
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
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
                'WindowExecutions': [
                    {
                        'WindowId': 'string',
                        'WindowExecutionId': 'string',
                        'Status': 'PENDING'|'IN_PROGRESS'|'SUCCESS'|'FAILED'|'TIMED_OUT'|'CANCELLING'|'CANCELLED'|'SKIPPED_OVERLAPPING',
                        'StatusDetails': 'string',
                        'StartTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **WindowExecutions** *(list) --* 
              Information about the Maintenance Windows execution.
              - *(dict) --* 
                Describes the information about an execution of a Maintenance Window. 
                - **WindowId** *(string) --* 
                  The ID of the Maintenance Window.
                - **WindowExecutionId** *(string) --* 
                  The ID of the Maintenance Window execution.
                - **Status** *(string) --* 
                  The status of the execution.
                - **StatusDetails** *(string) --* 
                  The details explaining the Status. Only available for certain status values.
                - **StartTime** *(datetime) --* 
                  The time the execution started.
                - **EndTime** *(datetime) --* 
                  The time the execution finished.
        :type WindowId: string
        :param WindowId: **[REQUIRED]**
          The ID of the Maintenance Window whose executions should be retrieved.
        :type Filters: list
        :param Filters:
          Each entry in the array is a structure containing:
          Key (string, between 1 and 128 characters)
          Values (array of strings, each string is between 1 and 256 characters)
          The supported Keys are ExecutedBefore and ExecutedAfter with the value being a date/time string such as 2016-11-04T05:00:00Z.
          - *(dict) --*
            Filter used in the request. Supported filter keys are Name and Enabled.
            - **Key** *(string) --*
              The name of the filter.
            - **Values** *(list) --*
              The filter values.
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


class DescribeMaintenanceWindowSchedule(Paginator):
    def paginate(self, WindowId: str = None, Targets: List = None, ResourceType: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_maintenance_window_schedule`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowSchedule>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              WindowId='string',
              Targets=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              ResourceType='INSTANCE',
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
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
                'ScheduledWindowExecutions': [
                    {
                        'WindowId': 'string',
                        'Name': 'string',
                        'ExecutionTime': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ScheduledWindowExecutions** *(list) --* 
              Information about Maintenance Window executions scheduled for the specified time range.
              - *(dict) --* 
                Information about a scheduled execution for a Maintenance Window.
                - **WindowId** *(string) --* 
                  The ID of the Maintenance Window to be run.
                - **Name** *(string) --* 
                  The name of the Maintenance Window to be run.
                - **ExecutionTime** *(string) --* 
                  The time, in ISO-8601 Extended format, that the Maintenance Window is scheduled to be run.
        :type WindowId: string
        :param WindowId:
          The ID of the Maintenance Window to retrieve information about.
        :type Targets: list
        :param Targets:
          The instance ID or key/value pair to retrieve information about.
          - *(dict) --*
            An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
            - **Key** *(string) --*
              User-defined criteria for sending commands that target instances that meet the criteria. ``Key`` can be ``tag:<Amazon EC2 tag>`` or ``InstanceIds`` . For more information about how to send commands that target instances using ``Key,Value`` parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
            - **Values** *(list) --*
              User-defined criteria that maps to ``Key`` . For example, if you specified ``tag:ServerRole`` , you could specify ``value:WebServer`` to run a command on instances that include Amazon EC2 tags of ``ServerRole,WebServer`` . For more information about how to send commands that target instances using ``Key,Value`` parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
              - *(string) --*
        :type ResourceType: string
        :param ResourceType:
          The type of resource you want to retrieve information about. For example, \"INSTANCE\".
        :type Filters: list
        :param Filters:
          Filters used to limit the range of results. For example, you can limit Maintenance Window executions to only those scheduled before or after a certain date and time.
          - *(dict) --*
            Defines a filter used in Patch Manager APIs.
            - **Key** *(string) --*
              The key for the filter.
            - **Values** *(list) --*
              The value for the filter.
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


class DescribeMaintenanceWindowTargets(Paginator):
    def paginate(self, WindowId: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_maintenance_window_targets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowTargets>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              WindowId='string',
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
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
                'Targets': [
                    {
                        'WindowId': 'string',
                        'WindowTargetId': 'string',
                        'ResourceType': 'INSTANCE',
                        'Targets': [
                            {
                                'Key': 'string',
                                'Values': [
                                    'string',
                                ]
                            },
                        ],
                        'OwnerInformation': 'string',
                        'Name': 'string',
                        'Description': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Targets** *(list) --* 
              Information about the targets in the Maintenance Window.
              - *(dict) --* 
                The target registered with the Maintenance Window.
                - **WindowId** *(string) --* 
                  The ID of the Maintenance Window to register the target with.
                - **WindowTargetId** *(string) --* 
                  The ID of the target.
                - **ResourceType** *(string) --* 
                  The type of target that is being registered with the Maintenance Window.
                - **Targets** *(list) --* 
                  The targets, either instances or tags.
                  Specify instances using the following format:
                   ``Key=instanceids,Values=<instanceid1>,<instanceid2>``  
                  Tags are specified using the following format:
                   ``Key=<tag name>,Values=<tag value>`` .
                  - *(dict) --* 
                    An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.
                    - **Key** *(string) --* 
                      User-defined criteria for sending commands that target instances that meet the criteria. ``Key`` can be ``tag:<Amazon EC2 tag>`` or ``InstanceIds`` . For more information about how to send commands that target instances using ``Key,Value`` parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
                    - **Values** *(list) --* 
                      User-defined criteria that maps to ``Key`` . For example, if you specified ``tag:ServerRole`` , you could specify ``value:WebServer`` to run a command on instances that include Amazon EC2 tags of ``ServerRole,WebServer`` . For more information about how to send commands that target instances using ``Key,Value`` parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
                      - *(string) --* 
                - **OwnerInformation** *(string) --* 
                  A user-provided value that will be included in any CloudWatch events that are raised while running tasks for these targets in this Maintenance Window.
                - **Name** *(string) --* 
                  The target name.
                - **Description** *(string) --* 
                  A description for the target.
        :type WindowId: string
        :param WindowId: **[REQUIRED]**
          The ID of the Maintenance Window whose targets should be retrieved.
        :type Filters: list
        :param Filters:
          Optional filters that can be used to narrow down the scope of the returned window targets. The supported filter keys are Type, WindowTargetId and OwnerInformation.
          - *(dict) --*
            Filter used in the request. Supported filter keys are Name and Enabled.
            - **Key** *(string) --*
              The name of the filter.
            - **Values** *(list) --*
              The filter values.
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


class DescribeMaintenanceWindowTasks(Paginator):
    def paginate(self, WindowId: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_maintenance_window_tasks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowTasks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              WindowId='string',
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
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
                'Tasks': [
                    {
                        'WindowId': 'string',
                        'WindowTaskId': 'string',
                        'TaskArn': 'string',
                        'Type': 'RUN_COMMAND'|'AUTOMATION'|'STEP_FUNCTIONS'|'LAMBDA',
                        'Targets': [
                            {
                                'Key': 'string',
                                'Values': [
                                    'string',
                                ]
                            },
                        ],
                        'TaskParameters': {
                            'string': {
                                'Values': [
                                    'string',
                                ]
                            }
                        },
                        'Priority': 123,
                        'LoggingInfo': {
                            'S3BucketName': 'string',
                            'S3KeyPrefix': 'string',
                            'S3Region': 'string'
                        },
                        'ServiceRoleArn': 'string',
                        'MaxConcurrency': 'string',
                        'MaxErrors': 'string',
                        'Name': 'string',
                        'Description': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Tasks** *(list) --* 
              Information about the tasks in the Maintenance Window.
              - *(dict) --* 
                Information about a task defined for a Maintenance Window.
                - **WindowId** *(string) --* 
                  The ID of the Maintenance Window where the task is registered.
                - **WindowTaskId** *(string) --* 
                  The task ID.
                - **TaskArn** *(string) --* 
                  The resource that the task uses during execution. For RUN_COMMAND and AUTOMATION task types, ``TaskArn`` is the Systems Manager document name or ARN. For LAMBDA tasks, it's the function name or ARN. For STEP_FUNCTION tasks, it's the state machine ARN.
                - **Type** *(string) --* 
                  The type of task. The type can be one of the following: RUN_COMMAND, AUTOMATION, LAMBDA, or STEP_FUNCTION.
                - **Targets** *(list) --* 
                  The targets (either instances or tags). Instances are specified using Key=instanceids,Values=<instanceid1>,<instanceid2>. Tags are specified using Key=<tag name>,Values=<tag value>.
                  - *(dict) --* 
                    An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.
                    - **Key** *(string) --* 
                      User-defined criteria for sending commands that target instances that meet the criteria. ``Key`` can be ``tag:<Amazon EC2 tag>`` or ``InstanceIds`` . For more information about how to send commands that target instances using ``Key,Value`` parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
                    - **Values** *(list) --* 
                      User-defined criteria that maps to ``Key`` . For example, if you specified ``tag:ServerRole`` , you could specify ``value:WebServer`` to run a command on instances that include Amazon EC2 tags of ``ServerRole,WebServer`` . For more information about how to send commands that target instances using ``Key,Value`` parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
                      - *(string) --* 
                - **TaskParameters** *(dict) --* 
                  The parameters that should be passed to the task when it is run.
                  .. note::
                     ``TaskParameters`` has been deprecated. To specify parameters to pass to a task when it runs, instead use the ``Parameters`` option in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
                  - *(string) --* 
                    - *(dict) --* 
                      Defines the values for a task parameter.
                      - **Values** *(list) --* 
                        This field contains an array of 0 or more strings, each 1 to 255 characters in length.
                        - *(string) --* 
                - **Priority** *(integer) --* 
                  The priority of the task in the Maintenance Window. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.
                - **LoggingInfo** *(dict) --* 
                  Information about an Amazon S3 bucket to write task-level logs to.
                  .. note::
                     ``LoggingInfo`` has been deprecated. To specify an S3 bucket to contain logs, instead use the ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
                  - **S3BucketName** *(string) --* 
                    The name of an Amazon S3 bucket where execution logs are stored .
                  - **S3KeyPrefix** *(string) --* 
                    (Optional) The Amazon S3 bucket subfolder. 
                  - **S3Region** *(string) --* 
                    The region where the Amazon S3 bucket is located.
                - **ServiceRoleArn** *(string) --* 
                  The role that should be assumed when running the task.
                - **MaxConcurrency** *(string) --* 
                  The maximum number of targets this task can be run for, in parallel.
                - **MaxErrors** *(string) --* 
                  The maximum number of errors allowed before this task stops being scheduled.
                - **Name** *(string) --* 
                  The task name.
                - **Description** *(string) --* 
                  A description of the task.
        :type WindowId: string
        :param WindowId: **[REQUIRED]**
          The ID of the Maintenance Window whose tasks should be retrieved.
        :type Filters: list
        :param Filters:
          Optional filters used to narrow down the scope of the returned tasks. The supported filter keys are WindowTaskId, TaskArn, Priority, and TaskType.
          - *(dict) --*
            Filter used in the request. Supported filter keys are Name and Enabled.
            - **Key** *(string) --*
              The name of the filter.
            - **Values** *(list) --*
              The filter values.
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


class DescribeMaintenanceWindows(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_maintenance_windows`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindows>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
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
                'WindowIdentities': [
                    {
                        'WindowId': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'Enabled': True|False,
                        'Duration': 123,
                        'Cutoff': 123,
                        'Schedule': 'string',
                        'ScheduleTimezone': 'string',
                        'EndDate': 'string',
                        'StartDate': 'string',
                        'NextExecutionTime': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **WindowIdentities** *(list) --* 
              Information about the Maintenance Windows.
              - *(dict) --* 
                Information about the Maintenance Window.
                - **WindowId** *(string) --* 
                  The ID of the Maintenance Window.
                - **Name** *(string) --* 
                  The name of the Maintenance Window.
                - **Description** *(string) --* 
                  A description of the Maintenance Window.
                - **Enabled** *(boolean) --* 
                  Whether the Maintenance Window is enabled.
                - **Duration** *(integer) --* 
                  The duration of the Maintenance Window in hours.
                - **Cutoff** *(integer) --* 
                  The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.
                - **Schedule** *(string) --* 
                  The schedule of the Maintenance Window in the form of a cron or rate expression.
                - **ScheduleTimezone** *(string) --* 
                  The time zone that the scheduled Maintenance Window executions are based on, in Internet Assigned Numbers Authority (IANA) format.
                - **EndDate** *(string) --* 
                  The date and time, in ISO-8601 Extended format, for when the Maintenance Window is scheduled to become inactive.
                - **StartDate** *(string) --* 
                  The date and time, in ISO-8601 Extended format, for when the Maintenance Window is scheduled to become active.
                - **NextExecutionTime** *(string) --* 
                  The next time the Maintenance Window will actually run, taking into account any specified times for the Maintenance Window to become active or inactive.
        :type Filters: list
        :param Filters:
          Optional filters used to narrow down the scope of the returned Maintenance Windows. Supported filter keys are **Name** and **Enabled** .
          - *(dict) --*
            Filter used in the request. Supported filter keys are Name and Enabled.
            - **Key** *(string) --*
              The name of the filter.
            - **Values** *(list) --*
              The filter values.
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


class DescribeMaintenanceWindowsForTarget(Paginator):
    def paginate(self, Targets: List, ResourceType: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_maintenance_windows_for_target`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowsForTarget>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Targets=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              ResourceType='INSTANCE',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'WindowIdentities': [
                    {
                        'WindowId': 'string',
                        'Name': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **WindowIdentities** *(list) --* 
              Information about the Maintenance Window targets and tasks an instance is associated with.
              - *(dict) --* 
                The Maintenance Window to which the specified target belongs.
                - **WindowId** *(string) --* 
                  The ID of the Maintenance Window.
                - **Name** *(string) --* 
                  The name of the Maintenance Window.
        :type Targets: list
        :param Targets: **[REQUIRED]**
          The instance ID or key/value pair to retrieve information about.
          - *(dict) --*
            An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
            - **Key** *(string) --*
              User-defined criteria for sending commands that target instances that meet the criteria. ``Key`` can be ``tag:<Amazon EC2 tag>`` or ``InstanceIds`` . For more information about how to send commands that target instances using ``Key,Value`` parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
            - **Values** *(list) --*
              User-defined criteria that maps to ``Key`` . For example, if you specified ``tag:ServerRole`` , you could specify ``value:WebServer`` to run a command on instances that include Amazon EC2 tags of ``ServerRole,WebServer`` . For more information about how to send commands that target instances using ``Key,Value`` parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
              - *(string) --*
        :type ResourceType: string
        :param ResourceType: **[REQUIRED]**
          The type of resource you want to retrieve information about. For example, \"INSTANCE\".
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


class DescribeParameters(Paginator):
    def paginate(self, Filters: List = None, ParameterFilters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_parameters`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeParameters>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Key': 'Name'|'Type'|'KeyId',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              ParameterFilters=[
                  {
                      'Key': 'string',
                      'Option': 'string',
                      'Values': [
                          'string',
                      ]
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
                'Parameters': [
                    {
                        'Name': 'string',
                        'Type': 'String'|'StringList'|'SecureString',
                        'KeyId': 'string',
                        'LastModifiedDate': datetime(2015, 1, 1),
                        'LastModifiedUser': 'string',
                        'Description': 'string',
                        'AllowedPattern': 'string',
                        'Version': 123,
                        'Tier': 'Standard'|'Advanced',
                        'Policies': [
                            {
                                'PolicyText': 'string',
                                'PolicyType': 'string',
                                'PolicyStatus': 'string'
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Parameters** *(list) --* 
              Parameters returned by the request.
              - *(dict) --* 
                Metada includes information like the ARN of the last user and the date/time the parameter was last used.
                - **Name** *(string) --* 
                  The parameter name.
                - **Type** *(string) --* 
                  The type of parameter. Valid parameter types include the following: String, String list, Secure string.
                - **KeyId** *(string) --* 
                  The ID of the query key used for this parameter.
                - **LastModifiedDate** *(datetime) --* 
                  Date the parameter was last changed or updated.
                - **LastModifiedUser** *(string) --* 
                  Amazon Resource Name (ARN) of the AWS user who last changed the parameter.
                - **Description** *(string) --* 
                  Description of the parameter actions.
                - **AllowedPattern** *(string) --* 
                  A parameter name can include only the following letters and symbols.
                  a-zA-Z0-9_.-
                - **Version** *(integer) --* 
                  The parameter version.
                - **Tier** *(string) --* 
                  The parameter tier.
                - **Policies** *(list) --* 
                  A list of policies associated with a parameter.
                  - *(dict) --* 
                    One or more policies assigned to a parameter.
                    - **PolicyText** *(string) --* 
                      The JSON text of the policy.
                    - **PolicyType** *(string) --* 
                      The type of policy. Parameter Store supports the following policy types: Expiration, ExpirationNotification, and NoChangeNotification. 
                    - **PolicyStatus** *(string) --* 
                      The status of the policy. Policies report the following statuses: Pending (the policy has not been enforced or applied yet), Finished (the policy was applied), Failed (the policy was not applied), or InProgress (the policy is being applied now). 
        :type Filters: list
        :param Filters:
          One or more filters. Use a filter to return a more specific list of results.
          - *(dict) --*
            This data type is deprecated. Instead, use  ParameterStringFilter .
            - **Key** *(string) --* **[REQUIRED]**
              The name of the filter.
            - **Values** *(list) --* **[REQUIRED]**
              The filter values.
              - *(string) --*
        :type ParameterFilters: list
        :param ParameterFilters:
          Filters to limit the request results.
          - *(dict) --*
            One or more filters. Use a filter to return a more specific list of results.
            .. note::
              The ``Name`` and ``Tier`` filter keys can\'t be used with the  GetParametersByPath API action. Also, the ``Label`` filter key can\'t be used with the  DescribeParameters API action.
            - **Key** *(string) --* **[REQUIRED]**
              The name of the filter.
            - **Option** *(string) --*
              Valid options are Equals and BeginsWith. For Path filter, valid options are Recursive and OneLevel.
            - **Values** *(list) --*
              The value you want to search for.
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


class DescribePatchBaselines(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_patch_baselines`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribePatchBaselines>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
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
                'BaselineIdentities': [
                    {
                        'BaselineId': 'string',
                        'BaselineName': 'string',
                        'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'AMAZON_LINUX_2'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS',
                        'BaselineDescription': 'string',
                        'DefaultBaseline': True|False
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BaselineIdentities** *(list) --* 
              An array of PatchBaselineIdentity elements.
              - *(dict) --* 
                Defines the basic information about a patch baseline.
                - **BaselineId** *(string) --* 
                  The ID of the patch baseline.
                - **BaselineName** *(string) --* 
                  The name of the patch baseline.
                - **OperatingSystem** *(string) --* 
                  Defines the operating system the patch baseline applies to. The Default value is WINDOWS. 
                - **BaselineDescription** *(string) --* 
                  The description of the patch baseline.
                - **DefaultBaseline** *(boolean) --* 
                  Whether this is the default baseline. Note that Systems Manager supports creating multiple default patch baselines. For example, you can create a default patch baseline for each operating system.
        :type Filters: list
        :param Filters:
          Each element in the array is a structure containing:
          Key: (string, \"NAME_PREFIX\" or \"OWNER\")
          Value: (array of strings, exactly 1 entry, between 1 and 255 characters)
          - *(dict) --*
            Defines a filter used in Patch Manager APIs.
            - **Key** *(string) --*
              The key for the filter.
            - **Values** *(list) --*
              The value for the filter.
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


class DescribePatchGroups(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_patch_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribePatchGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
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
                'Mappings': [
                    {
                        'PatchGroup': 'string',
                        'BaselineIdentity': {
                            'BaselineId': 'string',
                            'BaselineName': 'string',
                            'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'AMAZON_LINUX_2'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS',
                            'BaselineDescription': 'string',
                            'DefaultBaseline': True|False
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Mappings** *(list) --* 
              Each entry in the array contains:
              PatchGroup: string (between 1 and 256 characters, Regex: ^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$)
              PatchBaselineIdentity: A PatchBaselineIdentity element. 
              - *(dict) --* 
                The mapping between a patch group and the patch baseline the patch group is registered with.
                - **PatchGroup** *(string) --* 
                  The name of the patch group registered with the patch baseline.
                - **BaselineIdentity** *(dict) --* 
                  The patch baseline the patch group is registered with.
                  - **BaselineId** *(string) --* 
                    The ID of the patch baseline.
                  - **BaselineName** *(string) --* 
                    The name of the patch baseline.
                  - **OperatingSystem** *(string) --* 
                    Defines the operating system the patch baseline applies to. The Default value is WINDOWS. 
                  - **BaselineDescription** *(string) --* 
                    The description of the patch baseline.
                  - **DefaultBaseline** *(boolean) --* 
                    Whether this is the default baseline. Note that Systems Manager supports creating multiple default patch baselines. For example, you can create a default patch baseline for each operating system.
        :type Filters: list
        :param Filters:
          One or more filters. Use a filter to return a more specific list of results.
          - *(dict) --*
            Defines a filter used in Patch Manager APIs.
            - **Key** *(string) --*
              The key for the filter.
            - **Values** *(list) --*
              The value for the filter.
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


class DescribeSessions(Paginator):
    def paginate(self, State: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.describe_sessions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeSessions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              State='Active'|'History',
              Filters=[
                  {
                      'key': 'InvokedAfter'|'InvokedBefore'|'Target'|'Owner'|'Status',
                      'value': 'string'
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
                'Sessions': [
                    {
                        'SessionId': 'string',
                        'Target': 'string',
                        'Status': 'Connected'|'Connecting'|'Disconnected'|'Terminated'|'Terminating'|'Failed',
                        'StartDate': datetime(2015, 1, 1),
                        'EndDate': datetime(2015, 1, 1),
                        'DocumentName': 'string',
                        'Owner': 'string',
                        'Details': 'string',
                        'OutputUrl': {
                            'S3OutputUrl': 'string',
                            'CloudWatchOutputUrl': 'string'
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Sessions** *(list) --* 
              A list of sessions meeting the request parameters.
              - *(dict) --* 
                Information about a Session Manager connection to an instance.
                - **SessionId** *(string) --* 
                  The ID of the session.
                - **Target** *(string) --* 
                  The instance that the Session Manager session connected to.
                - **Status** *(string) --* 
                  The status of the session. For example, "Connected" or "Terminated".
                - **StartDate** *(datetime) --* 
                  The date and time, in ISO-8601 Extended format, when the session began.
                - **EndDate** *(datetime) --* 
                  The date and time, in ISO-8601 Extended format, when the session was terminated.
                - **DocumentName** *(string) --* 
                  The name of the Session Manager SSM document used to define the parameters and plugin settings for the session. For example, ``SSM-SessionManagerRunShell`` .
                - **Owner** *(string) --* 
                  The ID of the AWS user account that started the session.
                - **Details** *(string) --* 
                  Reserved for future use.
                - **OutputUrl** *(dict) --* 
                  Reserved for future use.
                  - **S3OutputUrl** *(string) --* 
                    Reserved for future use.
                  - **CloudWatchOutputUrl** *(string) --* 
                    Reserved for future use.
        :type State: string
        :param State: **[REQUIRED]**
          The session status to retrieve a list of sessions for. For example, \"Active\".
        :type Filters: list
        :param Filters:
          One or more filters to limit the type of sessions returned by the request.
          - *(dict) --*
            Describes a filter for Session Manager information.
            - **key** *(string) --* **[REQUIRED]**
              The name of the filter.
            - **value** *(string) --* **[REQUIRED]**
              The filter value. Valid values for each filter key are as follows:
              * InvokedAfter: Specify a timestamp to limit your results. For example, specify 2018-08-29T00:00:00Z to see sessions that started August 29, 2018, and later.
              * InvokedBefore: Specify a timestamp to limit your results. For example, specify 2018-08-29T00:00:00Z to see sessions that started before August 29, 2018.
              * Target: Specify an instance to which session connections have been made.
              * Owner: Specify an AWS user account to see a list of sessions started by that user.
              * Status: Specify a valid session status to see a list of all sessions with that status. Status values you can specify include:
                * Connected
                * Connecting
                * Disconnected
                * Terminated
                * Terminating
                * Failed
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


class GetInventory(Paginator):
    def paginate(self, Filters: List = None, Aggregators: List = None, ResultAttributes: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.get_inventory`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetInventory>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ],
                      'Type': 'Equal'|'NotEqual'|'BeginWith'|'LessThan'|'GreaterThan'|'Exists'
                  },
              ],
              Aggregators=[
                  {
                      'Expression': 'string',
                      'Aggregators': {'... recursive ...'},
                      'Groups': [
                          {
                              'Name': 'string',
                              'Filters': [
                                  {
                                      'Key': 'string',
                                      'Values': [
                                          'string',
                                      ],
                                      'Type': 'Equal'|'NotEqual'|'BeginWith'|'LessThan'|'GreaterThan'|'Exists'
                                  },
                              ]
                          },
                      ]
                  },
              ],
              ResultAttributes=[
                  {
                      'TypeName': 'string'
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
                'Entities': [
                    {
                        'Id': 'string',
                        'Data': {
                            'string': {
                                'TypeName': 'string',
                                'SchemaVersion': 'string',
                                'CaptureTime': 'string',
                                'ContentHash': 'string',
                                'Content': [
                                    {
                                        'string': 'string'
                                    },
                                ]
                            }
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Entities** *(list) --* 
              Collection of inventory entities such as a collection of instance inventory. 
              - *(dict) --* 
                Inventory query results.
                - **Id** *(string) --* 
                  ID of the inventory result entity. For example, for managed instance inventory the result will be the managed instance ID. For EC2 instance inventory, the result will be the instance ID. 
                - **Data** *(dict) --* 
                  The data section in the inventory result entity JSON.
                  - *(string) --* 
                    - *(dict) --* 
                      The inventory result item.
                      - **TypeName** *(string) --* 
                        The name of the inventory result item type.
                      - **SchemaVersion** *(string) --* 
                        The schema version for the inventory result item/
                      - **CaptureTime** *(string) --* 
                        The time inventory item data was captured.
                      - **ContentHash** *(string) --* 
                        MD5 hash of the inventory item type contents. The content hash is used to determine whether to update inventory information. The PutInventory API does not update the inventory item type contents if the MD5 hash has not changed since last update. 
                      - **Content** *(list) --* 
                        Contains all the inventory data of the item type. Results include attribute names and values. 
                        - *(dict) --* 
                          - *(string) --* 
                            - *(string) --* 
        :type Filters: list
        :param Filters:
          One or more filters. Use a filter to return a more specific list of results.
          - *(dict) --*
            One or more filters. Use a filter to return a more specific list of results.
            - **Key** *(string) --* **[REQUIRED]**
              The name of the filter key.
            - **Values** *(list) --* **[REQUIRED]**
              Inventory filter values. Example: inventory filter where instance IDs are specified as values Key=AWS:InstanceInformation.InstanceId,Values= i-a12b3c4d5e6g, i-1a2b3c4d5e6,Type=Equal
              - *(string) --*
            - **Type** *(string) --*
              The type of filter. Valid values include the following: \"Equal\"|\"NotEqual\"|\"BeginWith\"|\"LessThan\"|\"GreaterThan\"
        :type Aggregators: list
        :param Aggregators:
          Returns counts of inventory types based on one or more expressions. For example, if you aggregate by using an expression that uses the ``AWS:InstanceInformation.PlatformType`` type, you can see a count of how many Windows and Linux instances exist in your inventoried fleet.
          - *(dict) --*
            Specifies the inventory type and attribute for the aggregation execution.
            - **Expression** *(string) --*
              The inventory type and attribute name for aggregation.
            - **Aggregators** *(list) --*
              Nested aggregators to further refine aggregation for an inventory type.
            - **Groups** *(list) --*
              A user-defined set of one or more filters on which to aggregate inventory data. Groups return a count of resources that match and don\'t match the specified criteria.
              - *(dict) --*
                A user-defined set of one or more filters on which to aggregate inventory data. Groups return a count of resources that match and don\'t match the specified criteria.
                - **Name** *(string) --* **[REQUIRED]**
                  The name of the group.
                - **Filters** *(list) --* **[REQUIRED]**
                  Filters define the criteria for the group. The ``matchingCount`` field displays the number of resources that match the criteria. The ``notMatchingCount`` field displays the number of resources that don\'t match the criteria.
                  - *(dict) --*
                    One or more filters. Use a filter to return a more specific list of results.
                    - **Key** *(string) --* **[REQUIRED]**
                      The name of the filter key.
                    - **Values** *(list) --* **[REQUIRED]**
                      Inventory filter values. Example: inventory filter where instance IDs are specified as values Key=AWS:InstanceInformation.InstanceId,Values= i-a12b3c4d5e6g, i-1a2b3c4d5e6,Type=Equal
                      - *(string) --*
                    - **Type** *(string) --*
                      The type of filter. Valid values include the following: \"Equal\"|\"NotEqual\"|\"BeginWith\"|\"LessThan\"|\"GreaterThan\"
        :type ResultAttributes: list
        :param ResultAttributes:
          The list of inventory item types to return.
          - *(dict) --*
            The inventory item result attribute.
            - **TypeName** *(string) --* **[REQUIRED]**
              Name of the inventory item type. Valid value: AWS:InstanceInformation. Default Value: AWS:InstanceInformation.
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


class GetInventorySchema(Paginator):
    def paginate(self, TypeName: str = None, Aggregator: bool = None, SubType: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.get_inventory_schema`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetInventorySchema>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              TypeName='string',
              Aggregator=True|False,
              SubType=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Schemas': [
                    {
                        'TypeName': 'string',
                        'Version': 'string',
                        'Attributes': [
                            {
                                'Name': 'string',
                                'DataType': 'string'|'number'
                            },
                        ],
                        'DisplayName': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Schemas** *(list) --* 
              Inventory schemas returned by the request.
              - *(dict) --* 
                The inventory item schema definition. Users can use this to compose inventory query filters.
                - **TypeName** *(string) --* 
                  The name of the inventory type. Default inventory item type names start with AWS. Custom inventory type names will start with Custom. Default inventory item types include the following: AWS:AWSComponent, AWS:Application, AWS:InstanceInformation, AWS:Network, and AWS:WindowsUpdate.
                - **Version** *(string) --* 
                  The schema version for the inventory item.
                - **Attributes** *(list) --* 
                  The schema attributes for inventory. This contains data type and attribute name.
                  - *(dict) --* 
                    Attributes are the entries within the inventory item content. It contains name and value.
                    - **Name** *(string) --* 
                      Name of the inventory item attribute.
                    - **DataType** *(string) --* 
                      The data type of the inventory item attribute. 
                - **DisplayName** *(string) --* 
                  The alias name of the inventory type. The alias name is used for display purposes.
        :type TypeName: string
        :param TypeName:
          The type of inventory item to return.
        :type Aggregator: boolean
        :param Aggregator:
          Returns inventory schemas that support aggregation. For example, this call returns the ``AWS:InstanceInformation`` type, because it supports aggregation based on the ``PlatformName`` , ``PlatformType`` , and ``PlatformVersion`` attributes.
        :type SubType: boolean
        :param SubType:
          Returns the sub-type schema for a specified inventory type.
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


class GetParameterHistory(Paginator):
    def paginate(self, Name: str, WithDecryption: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.get_parameter_history`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetParameterHistory>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Name='string',
              WithDecryption=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Parameters': [
                    {
                        'Name': 'string',
                        'Type': 'String'|'StringList'|'SecureString',
                        'KeyId': 'string',
                        'LastModifiedDate': datetime(2015, 1, 1),
                        'LastModifiedUser': 'string',
                        'Description': 'string',
                        'Value': 'string',
                        'AllowedPattern': 'string',
                        'Version': 123,
                        'Labels': [
                            'string',
                        ],
                        'Tier': 'Standard'|'Advanced',
                        'Policies': [
                            {
                                'PolicyText': 'string',
                                'PolicyType': 'string',
                                'PolicyStatus': 'string'
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Parameters** *(list) --* 
              A list of parameters returned by the request.
              - *(dict) --* 
                Information about parameter usage.
                - **Name** *(string) --* 
                  The name of the parameter.
                - **Type** *(string) --* 
                  The type of parameter used.
                - **KeyId** *(string) --* 
                  The ID of the query key used for this parameter.
                - **LastModifiedDate** *(datetime) --* 
                  Date the parameter was last changed or updated.
                - **LastModifiedUser** *(string) --* 
                  Amazon Resource Name (ARN) of the AWS user who last changed the parameter.
                - **Description** *(string) --* 
                  Information about the parameter.
                - **Value** *(string) --* 
                  The parameter value.
                - **AllowedPattern** *(string) --* 
                  Parameter names can include the following letters and symbols.
                  a-zA-Z0-9_.-
                - **Version** *(integer) --* 
                  The parameter version.
                - **Labels** *(list) --* 
                  Labels assigned to the parameter version.
                  - *(string) --* 
                - **Tier** *(string) --* 
                  The parameter tier.
                - **Policies** *(list) --* 
                  Information about the policies assigned to a parameter.
                  - *(dict) --* 
                    One or more policies assigned to a parameter.
                    - **PolicyText** *(string) --* 
                      The JSON text of the policy.
                    - **PolicyType** *(string) --* 
                      The type of policy. Parameter Store supports the following policy types: Expiration, ExpirationNotification, and NoChangeNotification. 
                    - **PolicyStatus** *(string) --* 
                      The status of the policy. Policies report the following statuses: Pending (the policy has not been enforced or applied yet), Finished (the policy was applied), Failed (the policy was not applied), or InProgress (the policy is being applied now). 
        :type Name: string
        :param Name: **[REQUIRED]**
          The name of a parameter you want to query.
        :type WithDecryption: boolean
        :param WithDecryption:
          Return decrypted values for secure string parameters. This flag is ignored for String and StringList parameter types.
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


class GetParametersByPath(Paginator):
    def paginate(self, Path: str, Recursive: bool = None, ParameterFilters: List = None, WithDecryption: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.get_parameters_by_path`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetParametersByPath>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Path='string',
              Recursive=True|False,
              ParameterFilters=[
                  {
                      'Key': 'string',
                      'Option': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              WithDecryption=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Parameters': [
                    {
                        'Name': 'string',
                        'Type': 'String'|'StringList'|'SecureString',
                        'Value': 'string',
                        'Version': 123,
                        'Selector': 'string',
                        'SourceResult': 'string',
                        'LastModifiedDate': datetime(2015, 1, 1),
                        'ARN': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Parameters** *(list) --* 
              A list of parameters found in the specified hierarchy.
              - *(dict) --* 
                An Amazon EC2 Systems Manager parameter in Parameter Store.
                - **Name** *(string) --* 
                  The name of the parameter.
                - **Type** *(string) --* 
                  The type of parameter. Valid values include the following: String, String list, Secure string.
                - **Value** *(string) --* 
                  The parameter value.
                - **Version** *(integer) --* 
                  The parameter version.
                - **Selector** *(string) --* 
                  Either the version number or the label used to retrieve the parameter value. Specify selectors by using one of the following formats:
                  parameter_name:version
                  parameter_name:label
                - **SourceResult** *(string) --* 
                  Applies to parameters that reference information in other AWS services. SourceResult is the raw result or response from the source.
                - **LastModifiedDate** *(datetime) --* 
                  Date the parameter was last changed or updated and the parameter version was created.
                - **ARN** *(string) --* 
                  The Amazon Resource Name (ARN) of the parameter.
        :type Path: string
        :param Path: **[REQUIRED]**
          The hierarchy for the parameter. Hierarchies start with a forward slash (/) and end with the parameter name. A parameter name hierarchy can have a maximum of 15 levels. Here is an example of a hierarchy: ``/Finance/Prod/IAD/WinServ2016/license33``
        :type Recursive: boolean
        :param Recursive:
          Retrieve all parameters within a hierarchy.
          .. warning::
            If a user has access to a path, then the user can access all levels of that path. For example, if a user has permission to access path ``/a`` , then the user can also access ``/a/b`` . Even if a user has explicitly been denied access in IAM for parameter ``/a/b`` , they can still call the GetParametersByPath API action recursively for ``/a`` and view ``/a/b`` .
        :type ParameterFilters: list
        :param ParameterFilters:
          Filters to limit the request results.
          .. note::
            You can\'t filter using the parameter name.
          - *(dict) --*
            One or more filters. Use a filter to return a more specific list of results.
            .. note::
              The ``Name`` and ``Tier`` filter keys can\'t be used with the  GetParametersByPath API action. Also, the ``Label`` filter key can\'t be used with the  DescribeParameters API action.
            - **Key** *(string) --* **[REQUIRED]**
              The name of the filter.
            - **Option** *(string) --*
              Valid options are Equals and BeginsWith. For Path filter, valid options are Recursive and OneLevel.
            - **Values** *(list) --*
              The value you want to search for.
              - *(string) --*
        :type WithDecryption: boolean
        :param WithDecryption:
          Retrieve all parameters in a hierarchy with their value decrypted.
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


class ListAssociationVersions(Paginator):
    def paginate(self, AssociationId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.list_association_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListAssociationVersions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AssociationId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'AssociationVersions': [
                    {
                        'AssociationId': 'string',
                        'AssociationVersion': 'string',
                        'CreatedDate': datetime(2015, 1, 1),
                        'Name': 'string',
                        'DocumentVersion': 'string',
                        'Parameters': {
                            'string': [
                                'string',
                            ]
                        },
                        'Targets': [
                            {
                                'Key': 'string',
                                'Values': [
                                    'string',
                                ]
                            },
                        ],
                        'ScheduleExpression': 'string',
                        'OutputLocation': {
                            'S3Location': {
                                'OutputS3Region': 'string',
                                'OutputS3BucketName': 'string',
                                'OutputS3KeyPrefix': 'string'
                            }
                        },
                        'AssociationName': 'string',
                        'MaxErrors': 'string',
                        'MaxConcurrency': 'string',
                        'ComplianceSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'UNSPECIFIED'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AssociationVersions** *(list) --* 
              Information about all versions of the association for the specified association ID.
              - *(dict) --* 
                Information about the association version.
                - **AssociationId** *(string) --* 
                  The ID created by the system when the association was created.
                - **AssociationVersion** *(string) --* 
                  The association version.
                - **CreatedDate** *(datetime) --* 
                  The date the association version was created.
                - **Name** *(string) --* 
                  The name specified when the association was created.
                - **DocumentVersion** *(string) --* 
                  The version of a Systems Manager document used when the association version was created.
                - **Parameters** *(dict) --* 
                  Parameters specified when the association version was created.
                  - *(string) --* 
                    - *(list) --* 
                      - *(string) --* 
                - **Targets** *(list) --* 
                  The targets specified for the association when the association version was created. 
                  - *(dict) --* 
                    An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.
                    - **Key** *(string) --* 
                      User-defined criteria for sending commands that target instances that meet the criteria. ``Key`` can be ``tag:<Amazon EC2 tag>`` or ``InstanceIds`` . For more information about how to send commands that target instances using ``Key,Value`` parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
                    - **Values** *(list) --* 
                      User-defined criteria that maps to ``Key`` . For example, if you specified ``tag:ServerRole`` , you could specify ``value:WebServer`` to run a command on instances that include Amazon EC2 tags of ``ServerRole,WebServer`` . For more information about how to send commands that target instances using ``Key,Value`` parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
                      - *(string) --* 
                - **ScheduleExpression** *(string) --* 
                  The cron or rate schedule specified for the association when the association version was created.
                - **OutputLocation** *(dict) --* 
                  The location in Amazon S3 specified for the association when the association version was created.
                  - **S3Location** *(dict) --* 
                    An Amazon S3 bucket where you want to store the results of this request.
                    - **OutputS3Region** *(string) --* 
                      (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
                    - **OutputS3BucketName** *(string) --* 
                      The name of the Amazon S3 bucket.
                    - **OutputS3KeyPrefix** *(string) --* 
                      The Amazon S3 bucket subfolder.
                - **AssociationName** *(string) --* 
                  The name specified for the association version when the association version was created.
                - **MaxErrors** *(string) --* 
                  The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.
                  Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.
                - **MaxConcurrency** *(string) --* 
                  The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
                  If a new instance starts and attempts to run an association while Systems Manager is running MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.
                - **ComplianceSeverity** *(string) --* 
                  The severity level that is assigned to the association.
        :type AssociationId: string
        :param AssociationId: **[REQUIRED]**
          The association ID for which you want to view all versions.
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


class ListAssociations(Paginator):
    def paginate(self, AssociationFilterList: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.list_associations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListAssociations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AssociationFilterList=[
                  {
                      'key': 'InstanceId'|'Name'|'AssociationId'|'AssociationStatusName'|'LastExecutedBefore'|'LastExecutedAfter'|'AssociationName',
                      'value': 'string'
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
                'Associations': [
                    {
                        'Name': 'string',
                        'InstanceId': 'string',
                        'AssociationId': 'string',
                        'AssociationVersion': 'string',
                        'DocumentVersion': 'string',
                        'Targets': [
                            {
                                'Key': 'string',
                                'Values': [
                                    'string',
                                ]
                            },
                        ],
                        'LastExecutionDate': datetime(2015, 1, 1),
                        'Overview': {
                            'Status': 'string',
                            'DetailedStatus': 'string',
                            'AssociationStatusAggregatedCount': {
                                'string': 123
                            }
                        },
                        'ScheduleExpression': 'string',
                        'AssociationName': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Associations** *(list) --* 
              The associations.
              - *(dict) --* 
                Describes an association of a Systems Manager document and an instance.
                - **Name** *(string) --* 
                  The name of the Systems Manager document.
                - **InstanceId** *(string) --* 
                  The ID of the instance.
                - **AssociationId** *(string) --* 
                  The ID created by the system when you create an association. An association is a binding between a document and a set of targets with a schedule.
                - **AssociationVersion** *(string) --* 
                  The association version.
                - **DocumentVersion** *(string) --* 
                  The version of the document used in the association.
                - **Targets** *(list) --* 
                  The instances targeted by the request to create an association. 
                  - *(dict) --* 
                    An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.
                    - **Key** *(string) --* 
                      User-defined criteria for sending commands that target instances that meet the criteria. ``Key`` can be ``tag:<Amazon EC2 tag>`` or ``InstanceIds`` . For more information about how to send commands that target instances using ``Key,Value`` parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
                    - **Values** *(list) --* 
                      User-defined criteria that maps to ``Key`` . For example, if you specified ``tag:ServerRole`` , you could specify ``value:WebServer`` to run a command on instances that include Amazon EC2 tags of ``ServerRole,WebServer`` . For more information about how to send commands that target instances using ``Key,Value`` parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
                      - *(string) --* 
                - **LastExecutionDate** *(datetime) --* 
                  The date on which the association was last run.
                - **Overview** *(dict) --* 
                  Information about the association.
                  - **Status** *(string) --* 
                    The status of the association. Status can be: Pending, Success, or Failed.
                  - **DetailedStatus** *(string) --* 
                    A detailed status of the association.
                  - **AssociationStatusAggregatedCount** *(dict) --* 
                    Returns the number of targets for the association status. For example, if you created an association with two instances, and one of them was successful, this would return the count of instances by status.
                    - *(string) --* 
                      - *(integer) --* 
                - **ScheduleExpression** *(string) --* 
                  A cron expression that specifies a schedule when the association runs.
                - **AssociationName** *(string) --* 
                  The association name.
        :type AssociationFilterList: list
        :param AssociationFilterList:
          One or more filters. Use a filter to return a more specific list of results.
          - *(dict) --*
            Describes a filter.
            - **key** *(string) --* **[REQUIRED]**
              The name of the filter.
            - **value** *(string) --* **[REQUIRED]**
              The filter value.
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


class ListCommandInvocations(Paginator):
    def paginate(self, CommandId: str = None, InstanceId: str = None, Filters: List = None, Details: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.list_command_invocations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListCommandInvocations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              CommandId='string',
              InstanceId='string',
              Filters=[
                  {
                      'key': 'InvokedAfter'|'InvokedBefore'|'Status'|'ExecutionStage'|'DocumentName',
                      'value': 'string'
                  },
              ],
              Details=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'CommandInvocations': [
                    {
                        'CommandId': 'string',
                        'InstanceId': 'string',
                        'InstanceName': 'string',
                        'Comment': 'string',
                        'DocumentName': 'string',
                        'DocumentVersion': 'string',
                        'RequestedDateTime': datetime(2015, 1, 1),
                        'Status': 'Pending'|'InProgress'|'Delayed'|'Success'|'Cancelled'|'TimedOut'|'Failed'|'Cancelling',
                        'StatusDetails': 'string',
                        'TraceOutput': 'string',
                        'StandardOutputUrl': 'string',
                        'StandardErrorUrl': 'string',
                        'CommandPlugins': [
                            {
                                'Name': 'string',
                                'Status': 'Pending'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                                'StatusDetails': 'string',
                                'ResponseCode': 123,
                                'ResponseStartDateTime': datetime(2015, 1, 1),
                                'ResponseFinishDateTime': datetime(2015, 1, 1),
                                'Output': 'string',
                                'StandardOutputUrl': 'string',
                                'StandardErrorUrl': 'string',
                                'OutputS3Region': 'string',
                                'OutputS3BucketName': 'string',
                                'OutputS3KeyPrefix': 'string'
                            },
                        ],
                        'ServiceRole': 'string',
                        'NotificationConfig': {
                            'NotificationArn': 'string',
                            'NotificationEvents': [
                                'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                            ],
                            'NotificationType': 'Command'|'Invocation'
                        },
                        'CloudWatchOutputConfig': {
                            'CloudWatchLogGroupName': 'string',
                            'CloudWatchOutputEnabled': True|False
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CommandInvocations** *(list) --* 
              (Optional) A list of all invocations. 
              - *(dict) --* 
                An invocation is copy of a command sent to a specific instance. A command can apply to one or more instances. A command invocation applies to one instance. For example, if a user runs SendCommand against three instances, then a command invocation is created for each requested instance ID. A command invocation returns status and detail information about a command you ran. 
                - **CommandId** *(string) --* 
                  The command against which this invocation was requested.
                - **InstanceId** *(string) --* 
                  The instance ID in which this invocation was requested.
                - **InstanceName** *(string) --* 
                  The name of the invocation target. For Amazon EC2 instances this is the value for the aws:Name tag. For on-premises instances, this is the name of the instance.
                - **Comment** *(string) --* 
                  User-specified information about the command, such as a brief description of what the command should do.
                - **DocumentName** *(string) --* 
                  The document name that was requested for execution.
                - **DocumentVersion** *(string) --* 
                  The SSM document version.
                - **RequestedDateTime** *(datetime) --* 
                  The time and date the request was sent to this instance.
                - **Status** *(string) --* 
                  Whether or not the invocation succeeded, failed, or is pending.
                - **StatusDetails** *(string) --* 
                  A detailed status of the command execution for each invocation (each instance targeted by the command). StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see `Understanding Command Statuses <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* . StatusDetails can be one of the following values:
                  * Pending: The command has not been sent to the instance. 
                  * In Progress: The command has been sent to the instance but has not reached a terminal state. 
                  * Success: The execution of the command or plugin was successfully completed. This is a terminal state. 
                  * Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command's MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
                  * Execution Timed Out: Command execution started on the instance, but the execution was not complete before the execution timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state. 
                  * Failed: The command was not successful on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state. 
                  * Canceled: The command was terminated before it was completed. This is a terminal state. 
                  * Undeliverable: The command can't be delivered to the instance. The instance might not exist or might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit and don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
                  * Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state. 
                - **TraceOutput** *(string) --* 
                  Gets the trace output sent by the agent. 
                - **StandardOutputUrl** *(string) --* 
                  The URL to the plugin's StdOut file in Amazon S3, if the Amazon S3 bucket was defined for the parent command. For an invocation, StandardOutputUrl is populated if there is just one plugin defined for the command, and the Amazon S3 bucket was defined for the command.
                - **StandardErrorUrl** *(string) --* 
                  The URL to the plugin's StdErr file in Amazon S3, if the Amazon S3 bucket was defined for the parent command. For an invocation, StandardErrorUrl is populated if there is just one plugin defined for the command, and the Amazon S3 bucket was defined for the command.
                - **CommandPlugins** *(list) --* 
                  - *(dict) --* 
                    Describes plugin details.
                    - **Name** *(string) --* 
                      The name of the plugin. Must be one of the following: aws:updateAgent, aws:domainjoin, aws:applications, aws:runPowerShellScript, aws:psmodule, aws:cloudWatch, aws:runShellScript, or aws:updateSSMAgent. 
                    - **Status** *(string) --* 
                      The status of this plugin. You can run a document with multiple plugins.
                    - **StatusDetails** *(string) --* 
                      A detailed status of the plugin execution. StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see `Understanding Command Statuses <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* . StatusDetails can be one of the following values:
                      * Pending: The command has not been sent to the instance. 
                      * In Progress: The command has been sent to the instance but has not reached a terminal state. 
                      * Success: The execution of the command or plugin was successfully completed. This is a terminal state. 
                      * Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command's MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
                      * Execution Timed Out: Command execution started on the instance, but the execution was not complete before the execution timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state. 
                      * Failed: The command was not successful on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state. 
                      * Canceled: The command was terminated before it was completed. This is a terminal state. 
                      * Undeliverable: The command can't be delivered to the instance. The instance might not exist, or it might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit, and they don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
                      * Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state. 
                    - **ResponseCode** *(integer) --* 
                      A numeric response code generated after running the plugin. 
                    - **ResponseStartDateTime** *(datetime) --* 
                      The time the plugin started running. 
                    - **ResponseFinishDateTime** *(datetime) --* 
                      The time the plugin stopped running. Could stop prematurely if, for example, a cancel command was sent. 
                    - **Output** *(string) --* 
                      Output of the plugin execution.
                    - **StandardOutputUrl** *(string) --* 
                      The URL for the complete text written by the plugin to stdout in Amazon S3. If the Amazon S3 bucket for the command was not specified, then this string is empty.
                    - **StandardErrorUrl** *(string) --* 
                      The URL for the complete text written by the plugin to stderr. If execution is not yet complete, then this string is empty.
                    - **OutputS3Region** *(string) --* 
                      (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
                    - **OutputS3BucketName** *(string) --* 
                      The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command. For example, in the following response:
                      test_folder/ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix/i-1234567876543/awsrunShellScript 
                      test_folder is the name of the Amazon S3 bucket;
                      ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix is the name of the S3 prefix;
                      i-1234567876543 is the instance ID;
                      awsrunShellScript is the name of the plugin.
                    - **OutputS3KeyPrefix** *(string) --* 
                      The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command. For example, in the following response:
                      test_folder/ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix/i-1234567876543/awsrunShellScript 
                      test_folder is the name of the Amazon S3 bucket;
                      ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix is the name of the S3 prefix;
                      i-1234567876543 is the instance ID;
                      awsrunShellScript is the name of the plugin.
                - **ServiceRole** *(string) --* 
                  The IAM service role that Run Command uses to act on your behalf when sending notifications about command status changes on a per instance basis.
                - **NotificationConfig** *(dict) --* 
                  Configurations for sending notifications about command status changes on a per instance basis.
                  - **NotificationArn** *(string) --* 
                    An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.
                  - **NotificationEvents** *(list) --* 
                    The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Configuring Amazon SNS Notifications for Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/rc-sns-notifications.html>`__ in the *AWS Systems Manager User Guide* .
                    - *(string) --* 
                  - **NotificationType** *(string) --* 
                    Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 
                - **CloudWatchOutputConfig** *(dict) --* 
                  CloudWatch Logs information where you want Systems Manager to send the command output.
                  - **CloudWatchLogGroupName** *(string) --* 
                    The name of the CloudWatch log group where you want to send command output. If you don't specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/*SystemsManagerDocumentName* .
                  - **CloudWatchOutputEnabled** *(boolean) --* 
                    Enables Systems Manager to send command output to CloudWatch Logs.
        :type CommandId: string
        :param CommandId:
          (Optional) The invocations for a specific command ID.
        :type InstanceId: string
        :param InstanceId:
          (Optional) The command execution details for a specific instance ID.
        :type Filters: list
        :param Filters:
          (Optional) One or more filters. Use a filter to return a more specific list of results.
          - *(dict) --*
            Describes a command filter.
            - **key** *(string) --* **[REQUIRED]**
              The name of the filter.
            - **value** *(string) --* **[REQUIRED]**
              The filter value. Valid values for each filter key are as follows:
              * **InvokedAfter** : Specify a timestamp to limit your results. For example, specify ``2018-07-07T00:00:00Z`` to see a list of command executions occurring July 7, 2018, and later.
              * **InvokedBefore** : Specify a timestamp to limit your results. For example, specify ``2018-07-07T00:00:00Z`` to see a list of command executions from before July 7, 2018.
              * **Status** : Specify a valid command status to see a list of all command executions with that status. Status values you can specify include:
                * ``Pending``
                * ``InProgress``
                * ``Success``
                * ``Cancelled``
                * ``Failed``
                * ``TimedOut``
                * ``Cancelling``
              * **DocumentName** : Specify name of the SSM document for which you want to see command execution results. For example, specify ``AWS-RunPatchBaseline`` to see command executions that used this SSM document to perform security patching operations on instances.
              * **ExecutionStage** : Specify one of the following values:
                * ``Executing`` : Returns a list of command executions that are currently still running.
                * ``Complete`` : Returns a list of command executions that have already completed.
        :type Details: boolean
        :param Details:
          (Optional) If set this returns the response of the command executions and any command output. By default this is set to False.
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


class ListCommands(Paginator):
    def paginate(self, CommandId: str = None, InstanceId: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.list_commands`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListCommands>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              CommandId='string',
              InstanceId='string',
              Filters=[
                  {
                      'key': 'InvokedAfter'|'InvokedBefore'|'Status'|'ExecutionStage'|'DocumentName',
                      'value': 'string'
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
                'Commands': [
                    {
                        'CommandId': 'string',
                        'DocumentName': 'string',
                        'DocumentVersion': 'string',
                        'Comment': 'string',
                        'ExpiresAfter': datetime(2015, 1, 1),
                        'Parameters': {
                            'string': [
                                'string',
                            ]
                        },
                        'InstanceIds': [
                            'string',
                        ],
                        'Targets': [
                            {
                                'Key': 'string',
                                'Values': [
                                    'string',
                                ]
                            },
                        ],
                        'RequestedDateTime': datetime(2015, 1, 1),
                        'Status': 'Pending'|'InProgress'|'Success'|'Cancelled'|'Failed'|'TimedOut'|'Cancelling',
                        'StatusDetails': 'string',
                        'OutputS3Region': 'string',
                        'OutputS3BucketName': 'string',
                        'OutputS3KeyPrefix': 'string',
                        'MaxConcurrency': 'string',
                        'MaxErrors': 'string',
                        'TargetCount': 123,
                        'CompletedCount': 123,
                        'ErrorCount': 123,
                        'DeliveryTimedOutCount': 123,
                        'ServiceRole': 'string',
                        'NotificationConfig': {
                            'NotificationArn': 'string',
                            'NotificationEvents': [
                                'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                            ],
                            'NotificationType': 'Command'|'Invocation'
                        },
                        'CloudWatchOutputConfig': {
                            'CloudWatchLogGroupName': 'string',
                            'CloudWatchOutputEnabled': True|False
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Commands** *(list) --* 
              (Optional) The list of commands requested by the user. 
              - *(dict) --* 
                Describes a command request.
                - **CommandId** *(string) --* 
                  A unique identifier for this command.
                - **DocumentName** *(string) --* 
                  The name of the document requested for execution.
                - **DocumentVersion** *(string) --* 
                  The SSM document version.
                - **Comment** *(string) --* 
                  User-specified information about the command, such as a brief description of what the command should do.
                - **ExpiresAfter** *(datetime) --* 
                  If this time is reached and the command has not already started running, it will not run. Calculated based on the ExpiresAfter user input provided as part of the SendCommand API.
                - **Parameters** *(dict) --* 
                  The parameter values to be inserted in the document when running the command.
                  - *(string) --* 
                    - *(list) --* 
                      - *(string) --* 
                - **InstanceIds** *(list) --* 
                  The instance IDs against which this command was requested.
                  - *(string) --* 
                - **Targets** *(list) --* 
                  An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don't provide one or more instance IDs in the call.
                  - *(dict) --* 
                    An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don't provide one or more instance IDs in the call.
                    - **Key** *(string) --* 
                      User-defined criteria for sending commands that target instances that meet the criteria. ``Key`` can be ``tag:<Amazon EC2 tag>`` or ``InstanceIds`` . For more information about how to send commands that target instances using ``Key,Value`` parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
                    - **Values** *(list) --* 
                      User-defined criteria that maps to ``Key`` . For example, if you specified ``tag:ServerRole`` , you could specify ``value:WebServer`` to run a command on instances that include Amazon EC2 tags of ``ServerRole,WebServer`` . For more information about how to send commands that target instances using ``Key,Value`` parameters, see `Using Targets and Rate Controls to Send Commands to a Fleet <https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
                      - *(string) --* 
                - **RequestedDateTime** *(datetime) --* 
                  The date and time the command was requested.
                - **Status** *(string) --* 
                  The status of the command.
                - **StatusDetails** *(string) --* 
                  A detailed status of the command execution. StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see `Understanding Command Statuses <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* . StatusDetails can be one of the following values:
                  * Pending: The command has not been sent to any instances. 
                  * In Progress: The command has been sent to at least one instance but has not reached a final state on all instances. 
                  * Success: The command successfully ran on all invocations. This is a terminal state. 
                  * Delivery Timed Out: The value of MaxErrors or more command invocations shows a status of Delivery Timed Out. This is a terminal state. 
                  * Execution Timed Out: The value of MaxErrors or more command invocations shows a status of Execution Timed Out. This is a terminal state. 
                  * Failed: The value of MaxErrors or more command invocations shows a status of Failed. This is a terminal state. 
                  * Incomplete: The command was attempted on all instances and one or more invocations does not have a value of Success but not enough invocations failed for the status to be Failed. This is a terminal state. 
                  * Canceled: The command was terminated before it was completed. This is a terminal state. 
                  * Rate Exceeded: The number of instances targeted by the command exceeded the account limit for pending invocations. The system has canceled the command before running it on any instance. This is a terminal state. 
                - **OutputS3Region** *(string) --* 
                  (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
                - **OutputS3BucketName** *(string) --* 
                  The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command.
                - **OutputS3KeyPrefix** *(string) --* 
                  The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command.
                - **MaxConcurrency** *(string) --* 
                  The maximum number of instances that are allowed to run the command at the same time. You can specify a number of instances, such as 10, or a percentage of instances, such as 10%. The default value is 50. For more information about how to use MaxConcurrency, see `Running Commands Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html>`__ in the *AWS Systems Manager User Guide* .
                - **MaxErrors** *(string) --* 
                  The maximum number of errors allowed before the system stops sending the command to additional targets. You can specify a number of errors, such as 10, or a percentage or errors, such as 10%. The default value is 0. For more information about how to use MaxErrors, see `Running Commands Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html>`__ in the *AWS Systems Manager User Guide* .
                - **TargetCount** *(integer) --* 
                  The number of targets for the command.
                - **CompletedCount** *(integer) --* 
                  The number of targets for which the command invocation reached a terminal state. Terminal states include the following: Success, Failed, Execution Timed Out, Delivery Timed Out, Canceled, Terminated, or Undeliverable.
                - **ErrorCount** *(integer) --* 
                  The number of targets for which the status is Failed or Execution Timed Out.
                - **DeliveryTimedOutCount** *(integer) --* 
                  The number of targets for which the status is Delivery Timed Out.
                - **ServiceRole** *(string) --* 
                  The IAM service role that Run Command uses to act on your behalf when sending notifications about command status changes. 
                - **NotificationConfig** *(dict) --* 
                  Configurations for sending notifications about command status changes. 
                  - **NotificationArn** *(string) --* 
                    An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.
                  - **NotificationEvents** *(list) --* 
                    The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Configuring Amazon SNS Notifications for Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/rc-sns-notifications.html>`__ in the *AWS Systems Manager User Guide* .
                    - *(string) --* 
                  - **NotificationType** *(string) --* 
                    Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 
                - **CloudWatchOutputConfig** *(dict) --* 
                  CloudWatch Logs information where you want Systems Manager to send the command output.
                  - **CloudWatchLogGroupName** *(string) --* 
                    The name of the CloudWatch log group where you want to send command output. If you don't specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/*SystemsManagerDocumentName* .
                  - **CloudWatchOutputEnabled** *(boolean) --* 
                    Enables Systems Manager to send command output to CloudWatch Logs.
        :type CommandId: string
        :param CommandId:
          (Optional) If provided, lists only the specified command.
        :type InstanceId: string
        :param InstanceId:
          (Optional) Lists commands issued against this instance ID.
        :type Filters: list
        :param Filters:
          (Optional) One or more filters. Use a filter to return a more specific list of results.
          - *(dict) --*
            Describes a command filter.
            - **key** *(string) --* **[REQUIRED]**
              The name of the filter.
            - **value** *(string) --* **[REQUIRED]**
              The filter value. Valid values for each filter key are as follows:
              * **InvokedAfter** : Specify a timestamp to limit your results. For example, specify ``2018-07-07T00:00:00Z`` to see a list of command executions occurring July 7, 2018, and later.
              * **InvokedBefore** : Specify a timestamp to limit your results. For example, specify ``2018-07-07T00:00:00Z`` to see a list of command executions from before July 7, 2018.
              * **Status** : Specify a valid command status to see a list of all command executions with that status. Status values you can specify include:
                * ``Pending``
                * ``InProgress``
                * ``Success``
                * ``Cancelled``
                * ``Failed``
                * ``TimedOut``
                * ``Cancelling``
              * **DocumentName** : Specify name of the SSM document for which you want to see command execution results. For example, specify ``AWS-RunPatchBaseline`` to see command executions that used this SSM document to perform security patching operations on instances.
              * **ExecutionStage** : Specify one of the following values:
                * ``Executing`` : Returns a list of command executions that are currently still running.
                * ``Complete`` : Returns a list of command executions that have already completed.
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


class ListComplianceItems(Paginator):
    def paginate(self, Filters: List = None, ResourceIds: List = None, ResourceTypes: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.list_compliance_items`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListComplianceItems>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ],
                      'Type': 'EQUAL'|'NOT_EQUAL'|'BEGIN_WITH'|'LESS_THAN'|'GREATER_THAN'
                  },
              ],
              ResourceIds=[
                  'string',
              ],
              ResourceTypes=[
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
                'ComplianceItems': [
                    {
                        'ComplianceType': 'string',
                        'ResourceType': 'string',
                        'ResourceId': 'string',
                        'Id': 'string',
                        'Title': 'string',
                        'Status': 'COMPLIANT'|'NON_COMPLIANT',
                        'Severity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                        'ExecutionSummary': {
                            'ExecutionTime': datetime(2015, 1, 1),
                            'ExecutionId': 'string',
                            'ExecutionType': 'string'
                        },
                        'Details': {
                            'string': 'string'
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ComplianceItems** *(list) --* 
              A list of compliance information for the specified resource ID. 
              - *(dict) --* 
                Information about the compliance as defined by the resource type. For example, for a patch resource type, ``Items`` includes information about the PatchSeverity, Classification, etc.
                - **ComplianceType** *(string) --* 
                  The compliance type. For example, Association (for a State Manager association), Patch, or Custom:``string`` are all valid compliance types.
                - **ResourceType** *(string) --* 
                  The type of resource. ``ManagedInstance`` is currently the only supported resource type.
                - **ResourceId** *(string) --* 
                  An ID for the resource. For a managed instance, this is the instance ID.
                - **Id** *(string) --* 
                  An ID for the compliance item. For example, if the compliance item is a Windows patch, the ID could be the number of the KB article; for example: KB4010320.
                - **Title** *(string) --* 
                  A title for the compliance item. For example, if the compliance item is a Windows patch, the title could be the title of the KB article for the patch; for example: Security Update for Active Directory Federation Services.
                - **Status** *(string) --* 
                  The status of the compliance item. An item is either COMPLIANT or NON_COMPLIANT.
                - **Severity** *(string) --* 
                  The severity of the compliance status. Severity can be one of the following: Critical, High, Medium, Low, Informational, Unspecified.
                - **ExecutionSummary** *(dict) --* 
                  A summary for the compliance item. The summary includes an execution ID, the execution type (for example, command), and the execution time.
                  - **ExecutionTime** *(datetime) --* 
                    The time the execution ran as a datetime object that is saved in the following format: yyyy-MM-dd'T'HH:mm:ss'Z'.
                  - **ExecutionId** *(string) --* 
                    An ID created by the system when ``PutComplianceItems`` was called. For example, ``CommandID`` is a valid execution ID. You can use this ID in subsequent calls.
                  - **ExecutionType** *(string) --* 
                    The type of execution. For example, ``Command`` is a valid execution type.
                - **Details** *(dict) --* 
                  A "Key": "Value" tag combination for the compliance item.
                  - *(string) --* 
                    - *(string) --* 
        :type Filters: list
        :param Filters:
          One or more compliance filters. Use a filter to return a more specific list of results.
          - *(dict) --*
            One or more filters. Use a filter to return a more specific list of results.
            - **Key** *(string) --*
              The name of the filter.
            - **Values** *(list) --*
              The value for which to search.
              - *(string) --*
            - **Type** *(string) --*
              The type of comparison that should be performed for the value: Equal, NotEqual, BeginWith, LessThan, or GreaterThan.
        :type ResourceIds: list
        :param ResourceIds:
          The ID for the resources from which to get compliance information. Currently, you can only specify one resource ID.
          - *(string) --*
        :type ResourceTypes: list
        :param ResourceTypes:
          The type of resource from which to get compliance information. Currently, the only supported resource type is ``ManagedInstance`` .
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


class ListComplianceSummaries(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.list_compliance_summaries`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListComplianceSummaries>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ],
                      'Type': 'EQUAL'|'NOT_EQUAL'|'BEGIN_WITH'|'LESS_THAN'|'GREATER_THAN'
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
                'ComplianceSummaryItems': [
                    {
                        'ComplianceType': 'string',
                        'CompliantSummary': {
                            'CompliantCount': 123,
                            'SeveritySummary': {
                                'CriticalCount': 123,
                                'HighCount': 123,
                                'MediumCount': 123,
                                'LowCount': 123,
                                'InformationalCount': 123,
                                'UnspecifiedCount': 123
                            }
                        },
                        'NonCompliantSummary': {
                            'NonCompliantCount': 123,
                            'SeveritySummary': {
                                'CriticalCount': 123,
                                'HighCount': 123,
                                'MediumCount': 123,
                                'LowCount': 123,
                                'InformationalCount': 123,
                                'UnspecifiedCount': 123
                            }
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ComplianceSummaryItems** *(list) --* 
              A list of compliant and non-compliant summary counts based on compliance types. For example, this call returns State Manager associations, patches, or custom compliance types according to the filter criteria that you specified.
              - *(dict) --* 
                A summary of compliance information by compliance type.
                - **ComplianceType** *(string) --* 
                  The type of compliance item. For example, the compliance type can be Association, Patch, or Custom:string.
                - **CompliantSummary** *(dict) --* 
                  A list of COMPLIANT items for the specified compliance type.
                  - **CompliantCount** *(integer) --* 
                    The total number of resources that are compliant.
                  - **SeveritySummary** *(dict) --* 
                    A summary of the compliance severity by compliance type.
                    - **CriticalCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of critical. Critical severity is determined by the organization that published the compliance items.
                    - **HighCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of high. High severity is determined by the organization that published the compliance items.
                    - **MediumCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of medium. Medium severity is determined by the organization that published the compliance items.
                    - **LowCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of low. Low severity is determined by the organization that published the compliance items.
                    - **InformationalCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of informational. Informational severity is determined by the organization that published the compliance items.
                    - **UnspecifiedCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of unspecified. Unspecified severity is determined by the organization that published the compliance items.
                - **NonCompliantSummary** *(dict) --* 
                  A list of NON_COMPLIANT items for the specified compliance type.
                  - **NonCompliantCount** *(integer) --* 
                    The total number of compliance items that are not compliant.
                  - **SeveritySummary** *(dict) --* 
                    A summary of the non-compliance severity by compliance type
                    - **CriticalCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of critical. Critical severity is determined by the organization that published the compliance items.
                    - **HighCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of high. High severity is determined by the organization that published the compliance items.
                    - **MediumCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of medium. Medium severity is determined by the organization that published the compliance items.
                    - **LowCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of low. Low severity is determined by the organization that published the compliance items.
                    - **InformationalCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of informational. Informational severity is determined by the organization that published the compliance items.
                    - **UnspecifiedCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of unspecified. Unspecified severity is determined by the organization that published the compliance items.
        :type Filters: list
        :param Filters:
          One or more compliance or inventory filters. Use a filter to return a more specific list of results.
          - *(dict) --*
            One or more filters. Use a filter to return a more specific list of results.
            - **Key** *(string) --*
              The name of the filter.
            - **Values** *(list) --*
              The value for which to search.
              - *(string) --*
            - **Type** *(string) --*
              The type of comparison that should be performed for the value: Equal, NotEqual, BeginWith, LessThan, or GreaterThan.
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


class ListDocumentVersions(Paginator):
    def paginate(self, Name: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.list_document_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListDocumentVersions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Name='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'DocumentVersions': [
                    {
                        'Name': 'string',
                        'DocumentVersion': 'string',
                        'VersionName': 'string',
                        'CreatedDate': datetime(2015, 1, 1),
                        'IsDefaultVersion': True|False,
                        'DocumentFormat': 'YAML'|'JSON',
                        'Status': 'Creating'|'Active'|'Updating'|'Deleting'|'Failed',
                        'StatusInformation': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DocumentVersions** *(list) --* 
              The document versions.
              - *(dict) --* 
                Version information about the document.
                - **Name** *(string) --* 
                  The document name.
                - **DocumentVersion** *(string) --* 
                  The document version.
                - **VersionName** *(string) --* 
                  The version of the artifact associated with the document. For example, "Release 12, Update 6". This value is unique across all versions of a document, and cannot be changed.
                - **CreatedDate** *(datetime) --* 
                  The date the document was created.
                - **IsDefaultVersion** *(boolean) --* 
                  An identifier for the default version of the document.
                - **DocumentFormat** *(string) --* 
                  The document format, either JSON or YAML.
                - **Status** *(string) --* 
                  The status of the Systems Manager document, such as ``Creating`` , ``Active`` , ``Failed`` , and ``Deleting`` .
                - **StatusInformation** *(string) --* 
                  A message returned by AWS Systems Manager that explains the ``Status`` value. For example, a ``Failed`` status might be explained by the ``StatusInformation`` message, "The specified S3 bucket does not exist. Verify that the URL of the S3 bucket is correct."
        :type Name: string
        :param Name: **[REQUIRED]**
          The name of the document about which you want version information.
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


class ListDocuments(Paginator):
    def paginate(self, DocumentFilterList: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.list_documents`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListDocuments>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DocumentFilterList=[
                  {
                      'key': 'Name'|'Owner'|'PlatformTypes'|'DocumentType',
                      'value': 'string'
                  },
              ],
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
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
                'DocumentIdentifiers': [
                    {
                        'Name': 'string',
                        'Owner': 'string',
                        'VersionName': 'string',
                        'PlatformTypes': [
                            'Windows'|'Linux',
                        ],
                        'DocumentVersion': 'string',
                        'DocumentType': 'Command'|'Policy'|'Automation'|'Session'|'Package',
                        'SchemaVersion': 'string',
                        'DocumentFormat': 'YAML'|'JSON',
                        'TargetType': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DocumentIdentifiers** *(list) --* 
              The names of the Systems Manager documents.
              - *(dict) --* 
                Describes the name of a Systems Manager document.
                - **Name** *(string) --* 
                  The name of the Systems Manager document.
                - **Owner** *(string) --* 
                  The AWS user account that created the document.
                - **VersionName** *(string) --* 
                  An optional field specifying the version of the artifact associated with the document. For example, "Release 12, Update 6". This value is unique across all versions of a document, and cannot be changed.
                - **PlatformTypes** *(list) --* 
                  The operating system platform. 
                  - *(string) --* 
                - **DocumentVersion** *(string) --* 
                  The document version.
                - **DocumentType** *(string) --* 
                  The document type.
                - **SchemaVersion** *(string) --* 
                  The schema version.
                - **DocumentFormat** *(string) --* 
                  The document format, either JSON or YAML.
                - **TargetType** *(string) --* 
                  The target type which defines the kinds of resources the document can run on. For example, /AWS::EC2::Instance. For a list of valid resource types, see `AWS Resource Types Reference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ in the *AWS CloudFormation User Guide* . 
                - **Tags** *(list) --* 
                  The tags, or metadata, that have been applied to the document.
                  - *(dict) --* 
                    Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, Maintenance Windows, Parameter Store parameters, and patch baselines.
                    - **Key** *(string) --* 
                      The name of the tag.
                    - **Value** *(string) --* 
                      The value of the tag.
        :type DocumentFilterList: list
        :param DocumentFilterList:
          One or more filters. Use a filter to return a more specific list of results.
          - *(dict) --*
            Describes a filter.
            - **key** *(string) --* **[REQUIRED]**
              The name of the filter.
            - **value** *(string) --* **[REQUIRED]**
              The value of the filter.
        :type Filters: list
        :param Filters:
          One or more filters. Use a filter to return a more specific list of results.
          - *(dict) --*
            One or more filters. Use a filter to return a more specific list of documents.
            For keys, you can specify one or more tags that have been applied to a document.
            Other valid values include Owner, Name, PlatformTypes, and DocumentType.
            Note that only one Owner can be specified in a request. For example: ``Key=Owner,Values=Self`` .
            If you use Name as a key, you can use a name prefix to return a list of documents. For example, in the AWS CLI, to return a list of all documents that begin with ``Te`` , run the following command:
             ``aws ssm list-documents --filters Key=Name,Values=Te``
            If you specify more than two keys, only documents that are identified by all the tags are returned in the results. If you specify more than two values for a key, documents that are identified by any of the values are returned in the results.
            To specify a custom key and value pair, use the format ``Key=tag:[tagName],Values=[valueName]`` .
            For example, if you created a Key called region and are using the AWS CLI to call the ``list-documents`` command:
             ``aws ssm list-documents --filters Key=tag:region,Values=east,west Key=Owner,Values=Self``
            - **Key** *(string) --*
              The name of the filter key.
            - **Values** *(list) --*
              The value for the filter key.
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


class ListResourceComplianceSummaries(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.list_resource_compliance_summaries`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListResourceComplianceSummaries>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ],
                      'Type': 'EQUAL'|'NOT_EQUAL'|'BEGIN_WITH'|'LESS_THAN'|'GREATER_THAN'
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
                'ResourceComplianceSummaryItems': [
                    {
                        'ComplianceType': 'string',
                        'ResourceType': 'string',
                        'ResourceId': 'string',
                        'Status': 'COMPLIANT'|'NON_COMPLIANT',
                        'OverallSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                        'ExecutionSummary': {
                            'ExecutionTime': datetime(2015, 1, 1),
                            'ExecutionId': 'string',
                            'ExecutionType': 'string'
                        },
                        'CompliantSummary': {
                            'CompliantCount': 123,
                            'SeveritySummary': {
                                'CriticalCount': 123,
                                'HighCount': 123,
                                'MediumCount': 123,
                                'LowCount': 123,
                                'InformationalCount': 123,
                                'UnspecifiedCount': 123
                            }
                        },
                        'NonCompliantSummary': {
                            'NonCompliantCount': 123,
                            'SeveritySummary': {
                                'CriticalCount': 123,
                                'HighCount': 123,
                                'MediumCount': 123,
                                'LowCount': 123,
                                'InformationalCount': 123,
                                'UnspecifiedCount': 123
                            }
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ResourceComplianceSummaryItems** *(list) --* 
              A summary count for specified or targeted managed instances. Summary count includes information about compliant and non-compliant State Manager associations, patch status, or custom items according to the filter criteria that you specify. 
              - *(dict) --* 
                Compliance summary information for a specific resource. 
                - **ComplianceType** *(string) --* 
                  The compliance type.
                - **ResourceType** *(string) --* 
                  The resource type.
                - **ResourceId** *(string) --* 
                  The resource ID.
                - **Status** *(string) --* 
                  The compliance status for the resource.
                - **OverallSeverity** *(string) --* 
                  The highest severity item found for the resource. The resource is compliant for this item.
                - **ExecutionSummary** *(dict) --* 
                  Information about the execution.
                  - **ExecutionTime** *(datetime) --* 
                    The time the execution ran as a datetime object that is saved in the following format: yyyy-MM-dd'T'HH:mm:ss'Z'.
                  - **ExecutionId** *(string) --* 
                    An ID created by the system when ``PutComplianceItems`` was called. For example, ``CommandID`` is a valid execution ID. You can use this ID in subsequent calls.
                  - **ExecutionType** *(string) --* 
                    The type of execution. For example, ``Command`` is a valid execution type.
                - **CompliantSummary** *(dict) --* 
                  A list of items that are compliant for the resource.
                  - **CompliantCount** *(integer) --* 
                    The total number of resources that are compliant.
                  - **SeveritySummary** *(dict) --* 
                    A summary of the compliance severity by compliance type.
                    - **CriticalCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of critical. Critical severity is determined by the organization that published the compliance items.
                    - **HighCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of high. High severity is determined by the organization that published the compliance items.
                    - **MediumCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of medium. Medium severity is determined by the organization that published the compliance items.
                    - **LowCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of low. Low severity is determined by the organization that published the compliance items.
                    - **InformationalCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of informational. Informational severity is determined by the organization that published the compliance items.
                    - **UnspecifiedCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of unspecified. Unspecified severity is determined by the organization that published the compliance items.
                - **NonCompliantSummary** *(dict) --* 
                  A list of items that aren't compliant for the resource.
                  - **NonCompliantCount** *(integer) --* 
                    The total number of compliance items that are not compliant.
                  - **SeveritySummary** *(dict) --* 
                    A summary of the non-compliance severity by compliance type
                    - **CriticalCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of critical. Critical severity is determined by the organization that published the compliance items.
                    - **HighCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of high. High severity is determined by the organization that published the compliance items.
                    - **MediumCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of medium. Medium severity is determined by the organization that published the compliance items.
                    - **LowCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of low. Low severity is determined by the organization that published the compliance items.
                    - **InformationalCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of informational. Informational severity is determined by the organization that published the compliance items.
                    - **UnspecifiedCount** *(integer) --* 
                      The total number of resources or compliance items that have a severity level of unspecified. Unspecified severity is determined by the organization that published the compliance items.
        :type Filters: list
        :param Filters:
          One or more filters. Use a filter to return a more specific list of results.
          - *(dict) --*
            One or more filters. Use a filter to return a more specific list of results.
            - **Key** *(string) --*
              The name of the filter.
            - **Values** *(list) --*
              The value for which to search.
              - *(string) --*
            - **Type** *(string) --*
              The type of comparison that should be performed for the value: Equal, NotEqual, BeginWith, LessThan, or GreaterThan.
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


class ListResourceDataSync(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SSM.Client.list_resource_data_sync`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListResourceDataSync>`_
        
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
                'ResourceDataSyncItems': [
                    {
                        'SyncName': 'string',
                        'S3Destination': {
                            'BucketName': 'string',
                            'Prefix': 'string',
                            'SyncFormat': 'JsonSerDe',
                            'Region': 'string',
                            'AWSKMSKeyARN': 'string'
                        },
                        'LastSyncTime': datetime(2015, 1, 1),
                        'LastSuccessfulSyncTime': datetime(2015, 1, 1),
                        'LastStatus': 'Successful'|'Failed'|'InProgress',
                        'SyncCreatedTime': datetime(2015, 1, 1),
                        'LastSyncStatusMessage': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ResourceDataSyncItems** *(list) --* 
              A list of your current Resource Data Sync configurations and their statuses.
              - *(dict) --* 
                Information about a Resource Data Sync configuration, including its current status and last successful sync.
                - **SyncName** *(string) --* 
                  The name of the Resource Data Sync.
                - **S3Destination** *(dict) --* 
                  Configuration information for the target Amazon S3 bucket.
                  - **BucketName** *(string) --* 
                    The name of the Amazon S3 bucket where the aggregated data is stored.
                  - **Prefix** *(string) --* 
                    An Amazon S3 prefix for the bucket.
                  - **SyncFormat** *(string) --* 
                    A supported sync format. The following format is currently supported: JsonSerDe
                  - **Region** *(string) --* 
                    The AWS Region with the Amazon S3 bucket targeted by the Resource Data Sync.
                  - **AWSKMSKeyARN** *(string) --* 
                    The ARN of an encryption key for a destination in Amazon S3. Must belong to the same region as the destination Amazon S3 bucket.
                - **LastSyncTime** *(datetime) --* 
                  The last time the configuration attempted to sync (UTC).
                - **LastSuccessfulSyncTime** *(datetime) --* 
                  The last time the sync operations returned a status of ``SUCCESSFUL`` (UTC).
                - **LastStatus** *(string) --* 
                  The status reported by the last sync.
                - **SyncCreatedTime** *(datetime) --* 
                  The date and time the configuration was created (UTC).
                - **LastSyncStatusMessage** *(string) --* 
                  The status message details reported by the last sync.
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
