from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeAccountLimits(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudFormation.Client.describe_account_limits`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeAccountLimits>`_
        
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
                'AccountLimits': [
                    {
                        'Name': 'string',
                        'Value': 123
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            The output for the  DescribeAccountLimits action.
            - **AccountLimits** *(list) --* 
              An account limit structure that contain a list of AWS CloudFormation account limits and their values.
              - *(dict) --* 
                The AccountLimit data type. For more information about account limits, see `AWS CloudFormation Limits <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html>`__ in the *AWS CloudFormation User Guide* .
                - **Name** *(string) --* 
                  The name of the account limit.
                - **Value** *(integer) --* 
                  The value that is associated with the account limit name.
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


class DescribeChangeSet(Paginator):
    def paginate(self, ChangeSetName: str, StackName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudFormation.Client.describe_change_set`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeChangeSet>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ChangeSetName='string',
              StackName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ChangeSetName': 'string',
                'ChangeSetId': 'string',
                'StackId': 'string',
                'StackName': 'string',
                'Description': 'string',
                'Parameters': [
                    {
                        'ParameterKey': 'string',
                        'ParameterValue': 'string',
                        'UsePreviousValue': True|False,
                        'ResolvedValue': 'string'
                    },
                ],
                'CreationTime': datetime(2015, 1, 1),
                'ExecutionStatus': 'UNAVAILABLE'|'AVAILABLE'|'EXECUTE_IN_PROGRESS'|'EXECUTE_COMPLETE'|'EXECUTE_FAILED'|'OBSOLETE',
                'Status': 'CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'DELETE_COMPLETE'|'FAILED',
                'StatusReason': 'string',
                'NotificationARNs': [
                    'string',
                ],
                'RollbackConfiguration': {
                    'RollbackTriggers': [
                        {
                            'Arn': 'string',
                            'Type': 'string'
                        },
                    ],
                    'MonitoringTimeInMinutes': 123
                },
                'Capabilities': [
                    'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
                ],
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'Changes': [
                    {
                        'Type': 'Resource',
                        'ResourceChange': {
                            'Action': 'Add'|'Modify'|'Remove',
                            'LogicalResourceId': 'string',
                            'PhysicalResourceId': 'string',
                            'ResourceType': 'string',
                            'Replacement': 'True'|'False'|'Conditional',
                            'Scope': [
                                'Properties'|'Metadata'|'CreationPolicy'|'UpdatePolicy'|'DeletionPolicy'|'Tags',
                            ],
                            'Details': [
                                {
                                    'Target': {
                                        'Attribute': 'Properties'|'Metadata'|'CreationPolicy'|'UpdatePolicy'|'DeletionPolicy'|'Tags',
                                        'Name': 'string',
                                        'RequiresRecreation': 'Never'|'Conditionally'|'Always'
                                    },
                                    'Evaluation': 'Static'|'Dynamic',
                                    'ChangeSource': 'ResourceReference'|'ParameterReference'|'ResourceAttribute'|'DirectModification'|'Automatic',
                                    'CausingEntity': 'string'
                                },
                            ]
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            The output for the  DescribeChangeSet action.
            - **ChangeSetName** *(string) --* 
              The name of the change set.
            - **ChangeSetId** *(string) --* 
              The ARN of the change set.
            - **StackId** *(string) --* 
              The ARN of the stack that is associated with the change set.
            - **StackName** *(string) --* 
              The name of the stack that is associated with the change set.
            - **Description** *(string) --* 
              Information about the change set.
            - **Parameters** *(list) --* 
              A list of ``Parameter`` structures that describes the input parameters and their values used to create the change set. For more information, see the `Parameter <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html>`__ data type.
              - *(dict) --* 
                The Parameter data type.
                - **ParameterKey** *(string) --* 
                  The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
                - **ParameterValue** *(string) --* 
                  The input value associated with the parameter.
                - **UsePreviousValue** *(boolean) --* 
                  During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify ``true`` , do not specify a parameter value.
                - **ResolvedValue** *(string) --* 
                  Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` ``SSM`` parameter types <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.
            - **CreationTime** *(datetime) --* 
              The start time when the change set was created, in UTC.
            - **ExecutionStatus** *(string) --* 
              If the change set execution status is ``AVAILABLE`` , you can execute the change set. If you can’t execute the change set, the status indicates why. For example, a change set might be in an ``UNAVAILABLE`` state because AWS CloudFormation is still creating it or in an ``OBSOLETE`` state because the stack was already updated.
            - **Status** *(string) --* 
              The current status of the change set, such as ``CREATE_IN_PROGRESS`` , ``CREATE_COMPLETE`` , or ``FAILED`` .
            - **StatusReason** *(string) --* 
              A description of the change set's status. For example, if your attempt to create a change set failed, AWS CloudFormation shows the error message.
            - **NotificationARNs** *(list) --* 
              The ARNs of the Amazon Simple Notification Service (Amazon SNS) topics that will be associated with the stack if you execute the change set.
              - *(string) --* 
            - **RollbackConfiguration** *(dict) --* 
              The rollback triggers for AWS CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.
              - **RollbackTriggers** *(list) --* 
                The triggers to monitor during stack creation or update actions. 
                By default, AWS CloudFormation saves the rollback triggers specified for a stack and applies them to any subsequent update operations for the stack, unless you specify otherwise. If you do specify rollback triggers for this parameter, those triggers replace any list of triggers previously specified for the stack. This means:
                * To use the rollback triggers previously specified for this stack, if any, don't specify this parameter. 
                * To specify new or updated rollback triggers, you must specify *all* the triggers that you want used for this stack, even triggers you've specifed before (for example, when creating the stack or during a previous stack update). Any triggers that you don't include in the updated list of triggers are no longer applied to the stack. 
                * To remove all currently specified triggers, specify an empty list for this parameter. 
                If a specified trigger is missing, the entire stack operation fails and is rolled back. 
                - *(dict) --* 
                  A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any of the alarms you specify goes to ALARM state during the stack operation or within the specified monitoring period afterwards, CloudFormation rolls back the entire stack operation. 
                  - **Arn** *(string) --* 
                    The Amazon Resource Name (ARN) of the rollback trigger.
                    If a specified trigger is missing, the entire stack operation fails and is rolled back. 
                  - **Type** *(string) --* 
                    The resource type of the rollback trigger. Currently, `AWS\:\:CloudWatch\:\:Alarm <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__ is the only supported resource type.
              - **MonitoringTimeInMinutes** *(integer) --* 
                The amount of time, in minutes, during which CloudFormation should monitor all the rollback triggers after the stack creation or update operation deploys all necessary resources.
                The default is 0 minutes.
                If you specify a monitoring period but do not specify any rollback triggers, CloudFormation still waits the specified period of time before cleaning up old resources after update operations. You can use this monitoring period to perform any manual stack validation desired, and manually cancel the stack creation or update (using `CancelUpdateStack <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__ , for example) as necessary.
                If you specify 0 for this parameter, CloudFormation still monitors the specified rollback triggers during stack creation and update operations. Then, for update operations, it begins disposing of old resources immediately once the operation completes.
            - **Capabilities** *(list) --* 
              If you execute the change set, the list of capabilities that were explicitly acknowledged when the change set was created.
              - *(string) --* 
            - **Tags** *(list) --* 
              If you execute the change set, the tags that will be associated with the stack.
              - *(dict) --* 
                The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
                - **Key** *(string) --* 
                   *Required* . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .
                - **Value** *(string) --* 
                   *Required* . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
            - **Changes** *(list) --* 
              A list of ``Change`` structures that describes the resources AWS CloudFormation changes if you execute the change set.
              - *(dict) --* 
                The ``Change`` structure describes the changes AWS CloudFormation will perform if you execute the change set.
                - **Type** *(string) --* 
                  The type of entity that AWS CloudFormation changes. Currently, the only entity type is ``Resource`` .
                - **ResourceChange** *(dict) --* 
                  A ``ResourceChange`` structure that describes the resource and action that AWS CloudFormation will perform.
                  - **Action** *(string) --* 
                    The action that AWS CloudFormation takes on the resource, such as ``Add`` (adds a new resource), ``Modify`` (changes a resource), or ``Remove`` (deletes a resource).
                  - **LogicalResourceId** *(string) --* 
                    The resource's logical ID, which is defined in the stack's template.
                  - **PhysicalResourceId** *(string) --* 
                    The resource's physical ID (resource name). Resources that you are adding don't have physical IDs because they haven't been created.
                  - **ResourceType** *(string) --* 
                    The type of AWS CloudFormation resource, such as ``AWS::S3::Bucket`` .
                  - **Replacement** *(string) --* 
                    For the ``Modify`` action, indicates whether AWS CloudFormation will replace the resource by creating a new one and deleting the old one. This value depends on the value of the ``RequiresRecreation`` property in the ``ResourceTargetDefinition`` structure. For example, if the ``RequiresRecreation`` field is ``Always`` and the ``Evaluation`` field is ``Static`` , ``Replacement`` is ``True`` . If the ``RequiresRecreation`` field is ``Always`` and the ``Evaluation`` field is ``Dynamic`` , ``Replacement`` is ``Conditionally`` .
                    If you have multiple changes with different ``RequiresRecreation`` values, the ``Replacement`` value depends on the change with the most impact. A ``RequiresRecreation`` value of ``Always`` has the most impact, followed by ``Conditionally`` , and then ``Never`` .
                  - **Scope** *(list) --* 
                    For the ``Modify`` action, indicates which resource attribute is triggering this update, such as a change in the resource attribute's ``Metadata`` , ``Properties`` , or ``Tags`` .
                    - *(string) --* 
                  - **Details** *(list) --* 
                    For the ``Modify`` action, a list of ``ResourceChangeDetail`` structures that describes the changes that AWS CloudFormation will make to the resource. 
                    - *(dict) --* 
                      For a resource with ``Modify`` as the action, the ``ResourceChange`` structure describes the changes AWS CloudFormation will make to that resource.
                      - **Target** *(dict) --* 
                        A ``ResourceTargetDefinition`` structure that describes the field that AWS CloudFormation will change and whether the resource will be recreated.
                        - **Attribute** *(string) --* 
                          Indicates which resource attribute is triggering this update, such as a change in the resource attribute's ``Metadata`` , ``Properties`` , or ``Tags`` .
                        - **Name** *(string) --* 
                          If the ``Attribute`` value is ``Properties`` , the name of the property. For all other attributes, the value is null.
                        - **RequiresRecreation** *(string) --* 
                          If the ``Attribute`` value is ``Properties`` , indicates whether a change to this property causes the resource to be recreated. The value can be ``Never`` , ``Always`` , or ``Conditionally`` . To determine the conditions for a ``Conditionally`` recreation, see the update behavior for that `property <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ in the AWS CloudFormation User Guide.
                      - **Evaluation** *(string) --* 
                        Indicates whether AWS CloudFormation can determine the target value, and whether the target value will change before you execute a change set.
                        For ``Static`` evaluations, AWS CloudFormation can determine that the target value will change, and its value. For example, if you directly modify the ``InstanceType`` property of an EC2 instance, AWS CloudFormation knows that this property value will change, and its value, so this is a ``Static`` evaluation.
                        For ``Dynamic`` evaluations, cannot determine the target value because it depends on the result of an intrinsic function, such as a ``Ref`` or ``Fn::GetAtt`` intrinsic function, when the stack is updated. For example, if your template includes a reference to a resource that is conditionally recreated, the value of the reference (the physical ID of the resource) might change, depending on if the resource is recreated. If the resource is recreated, it will have a new physical ID, so all references to that resource will also be updated.
                      - **ChangeSource** *(string) --* 
                        The group to which the ``CausingEntity`` value belongs. There are five entity groups:
                        * ``ResourceReference`` entities are ``Ref`` intrinsic functions that refer to resources in the template, such as ``{ "Ref" : "MyEC2InstanceResource" }`` . 
                        * ``ParameterReference`` entities are ``Ref`` intrinsic functions that get template parameter values, such as ``{ "Ref" : "MyPasswordParameter" }`` . 
                        * ``ResourceAttribute`` entities are ``Fn::GetAtt`` intrinsic functions that get resource attribute values, such as ``{ "Fn::GetAtt" : [ "MyEC2InstanceResource", "PublicDnsName" ] }`` . 
                        * ``DirectModification`` entities are changes that are made directly to the template. 
                        * ``Automatic`` entities are ``AWS::CloudFormation::Stack`` resource types, which are also known as nested stacks. If you made no changes to the ``AWS::CloudFormation::Stack`` resource, AWS CloudFormation sets the ``ChangeSource`` to ``Automatic`` because the nested stack's template might have changed. Changes to a nested stack's template aren't visible to AWS CloudFormation until you run an update on the parent stack. 
                      - **CausingEntity** *(string) --* 
                        The identity of the entity that triggered this change. This entity is a member of the group that is specified by the ``ChangeSource`` field. For example, if you modified the value of the ``KeyPairName`` parameter, the ``CausingEntity`` is the name of the parameter (``KeyPairName`` ).
                        If the ``ChangeSource`` value is ``DirectModification`` , no value is given for ``CausingEntity`` .
        :type ChangeSetName: string
        :param ChangeSetName: **[REQUIRED]**
          The name or Amazon Resource Name (ARN) of the change set that you want to describe.
        :type StackName: string
        :param StackName:
          If you specified the name of a change set, specify the stack name or ID (ARN) of the change set you want to describe.
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


class DescribeStackEvents(Paginator):
    def paginate(self, StackName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudFormation.Client.describe_stack_events`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStackEvents>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              StackName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'StackEvents': [
                    {
                        'StackId': 'string',
                        'EventId': 'string',
                        'StackName': 'string',
                        'LogicalResourceId': 'string',
                        'PhysicalResourceId': 'string',
                        'ResourceType': 'string',
                        'Timestamp': datetime(2015, 1, 1),
                        'ResourceStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'DELETE_SKIPPED'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED'|'UPDATE_COMPLETE',
                        'ResourceStatusReason': 'string',
                        'ResourceProperties': 'string',
                        'ClientRequestToken': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            The output for a  DescribeStackEvents action.
            - **StackEvents** *(list) --* 
              A list of ``StackEvents`` structures.
              - *(dict) --* 
                The StackEvent data type.
                - **StackId** *(string) --* 
                  The unique ID name of the instance of the stack.
                - **EventId** *(string) --* 
                  The unique ID of this event.
                - **StackName** *(string) --* 
                  The name associated with a stack.
                - **LogicalResourceId** *(string) --* 
                  The logical name of the resource specified in the template.
                - **PhysicalResourceId** *(string) --* 
                  The name or unique identifier associated with the physical instance of the resource.
                - **ResourceType** *(string) --* 
                  Type of resource. (For more information, go to `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ in the AWS CloudFormation User Guide.)
                - **Timestamp** *(datetime) --* 
                  Time the status was updated.
                - **ResourceStatus** *(string) --* 
                  Current status of the resource.
                - **ResourceStatusReason** *(string) --* 
                  Success/failure message associated with the resource.
                - **ResourceProperties** *(string) --* 
                  BLOB of the properties used to create the resource.
                - **ClientRequestToken** *(string) --* 
                  The token passed to the operation that generated this event.
                  All events triggered by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a ``CreateStack`` operation with the token ``token1`` , then all the ``StackEvents`` generated by that operation will have ``ClientRequestToken`` set as ``token1`` .
                  In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format *Console-StackOperation-ID* , which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: ``Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002`` . 
        :type StackName: string
        :param StackName:
          The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
          * Running stacks: You can specify either the stack\'s name or its unique stack ID.
          * Deleted stacks: You must specify the unique stack ID.
          Default: There is no default value.
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


class DescribeStacks(Paginator):
    def paginate(self, StackName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudFormation.Client.describe_stacks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStacks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              StackName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Stacks': [
                    {
                        'StackId': 'string',
                        'StackName': 'string',
                        'ChangeSetId': 'string',
                        'Description': 'string',
                        'Parameters': [
                            {
                                'ParameterKey': 'string',
                                'ParameterValue': 'string',
                                'UsePreviousValue': True|False,
                                'ResolvedValue': 'string'
                            },
                        ],
                        'CreationTime': datetime(2015, 1, 1),
                        'DeletionTime': datetime(2015, 1, 1),
                        'LastUpdatedTime': datetime(2015, 1, 1),
                        'RollbackConfiguration': {
                            'RollbackTriggers': [
                                {
                                    'Arn': 'string',
                                    'Type': 'string'
                                },
                            ],
                            'MonitoringTimeInMinutes': 123
                        },
                        'StackStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'ROLLBACK_IN_PROGRESS'|'ROLLBACK_FAILED'|'ROLLBACK_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'UPDATE_IN_PROGRESS'|'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_COMPLETE'|'UPDATE_ROLLBACK_IN_PROGRESS'|'UPDATE_ROLLBACK_FAILED'|'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_ROLLBACK_COMPLETE'|'REVIEW_IN_PROGRESS',
                        'StackStatusReason': 'string',
                        'DisableRollback': True|False,
                        'NotificationARNs': [
                            'string',
                        ],
                        'TimeoutInMinutes': 123,
                        'Capabilities': [
                            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
                        ],
                        'Outputs': [
                            {
                                'OutputKey': 'string',
                                'OutputValue': 'string',
                                'Description': 'string',
                                'ExportName': 'string'
                            },
                        ],
                        'RoleARN': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'EnableTerminationProtection': True|False,
                        'ParentId': 'string',
                        'RootId': 'string',
                        'DriftInformation': {
                            'StackDriftStatus': 'DRIFTED'|'IN_SYNC'|'UNKNOWN'|'NOT_CHECKED',
                            'LastCheckTimestamp': datetime(2015, 1, 1)
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            The output for a  DescribeStacks action.
            - **Stacks** *(list) --* 
              A list of stack structures.
              - *(dict) --* 
                The Stack data type.
                - **StackId** *(string) --* 
                  Unique identifier of the stack.
                - **StackName** *(string) --* 
                  The name associated with the stack.
                - **ChangeSetId** *(string) --* 
                  The unique ID of the change set.
                - **Description** *(string) --* 
                  A user-defined description associated with the stack.
                - **Parameters** *(list) --* 
                  A list of ``Parameter`` structures.
                  - *(dict) --* 
                    The Parameter data type.
                    - **ParameterKey** *(string) --* 
                      The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
                    - **ParameterValue** *(string) --* 
                      The input value associated with the parameter.
                    - **UsePreviousValue** *(boolean) --* 
                      During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify ``true`` , do not specify a parameter value.
                    - **ResolvedValue** *(string) --* 
                      Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` ``SSM`` parameter types <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.
                - **CreationTime** *(datetime) --* 
                  The time at which the stack was created.
                - **DeletionTime** *(datetime) --* 
                  The time the stack was deleted.
                - **LastUpdatedTime** *(datetime) --* 
                  The time the stack was last updated. This field will only be returned if the stack has been updated at least once.
                - **RollbackConfiguration** *(dict) --* 
                  The rollback triggers for AWS CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.
                  - **RollbackTriggers** *(list) --* 
                    The triggers to monitor during stack creation or update actions. 
                    By default, AWS CloudFormation saves the rollback triggers specified for a stack and applies them to any subsequent update operations for the stack, unless you specify otherwise. If you do specify rollback triggers for this parameter, those triggers replace any list of triggers previously specified for the stack. This means:
                    * To use the rollback triggers previously specified for this stack, if any, don't specify this parameter. 
                    * To specify new or updated rollback triggers, you must specify *all* the triggers that you want used for this stack, even triggers you've specifed before (for example, when creating the stack or during a previous stack update). Any triggers that you don't include in the updated list of triggers are no longer applied to the stack. 
                    * To remove all currently specified triggers, specify an empty list for this parameter. 
                    If a specified trigger is missing, the entire stack operation fails and is rolled back. 
                    - *(dict) --* 
                      A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any of the alarms you specify goes to ALARM state during the stack operation or within the specified monitoring period afterwards, CloudFormation rolls back the entire stack operation. 
                      - **Arn** *(string) --* 
                        The Amazon Resource Name (ARN) of the rollback trigger.
                        If a specified trigger is missing, the entire stack operation fails and is rolled back. 
                      - **Type** *(string) --* 
                        The resource type of the rollback trigger. Currently, `AWS\:\:CloudWatch\:\:Alarm <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__ is the only supported resource type.
                  - **MonitoringTimeInMinutes** *(integer) --* 
                    The amount of time, in minutes, during which CloudFormation should monitor all the rollback triggers after the stack creation or update operation deploys all necessary resources.
                    The default is 0 minutes.
                    If you specify a monitoring period but do not specify any rollback triggers, CloudFormation still waits the specified period of time before cleaning up old resources after update operations. You can use this monitoring period to perform any manual stack validation desired, and manually cancel the stack creation or update (using `CancelUpdateStack <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__ , for example) as necessary.
                    If you specify 0 for this parameter, CloudFormation still monitors the specified rollback triggers during stack creation and update operations. Then, for update operations, it begins disposing of old resources immediately once the operation completes.
                - **StackStatus** *(string) --* 
                  Current status of the stack.
                - **StackStatusReason** *(string) --* 
                  Success/failure message associated with the stack status.
                - **DisableRollback** *(boolean) --* 
                  Boolean to enable or disable rollback on stack creation failures:
                  * ``true`` : disable rollback 
                  * ``false`` : enable rollback 
                - **NotificationARNs** *(list) --* 
                  SNS topic ARNs to which stack related events are published.
                  - *(string) --* 
                - **TimeoutInMinutes** *(integer) --* 
                  The amount of time within which stack creation should complete.
                - **Capabilities** *(list) --* 
                  The capabilities allowed in the stack.
                  - *(string) --* 
                - **Outputs** *(list) --* 
                  A list of output structures.
                  - *(dict) --* 
                    The Output data type.
                    - **OutputKey** *(string) --* 
                      The key associated with the output.
                    - **OutputValue** *(string) --* 
                      The value associated with the output.
                    - **Description** *(string) --* 
                      User defined description associated with the output.
                    - **ExportName** *(string) --* 
                      The name of the export associated with the output.
                - **RoleARN** *(string) --* 
                  The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that is associated with the stack. During a stack operation, AWS CloudFormation uses this role's credentials to make calls on your behalf.
                - **Tags** *(list) --* 
                  A list of ``Tag`` s that specify information about the stack.
                  - *(dict) --* 
                    The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
                    - **Key** *(string) --* 
                       *Required* . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .
                    - **Value** *(string) --* 
                       *Required* . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
                - **EnableTerminationProtection** *(boolean) --* 
                  Whether termination protection is enabled for the stack.
                  For `nested stacks <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__ , termination protection is set on the root stack and cannot be changed directly on the nested stack. For more information, see `Protecting a Stack From Being Deleted <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html>`__ in the *AWS CloudFormation User Guide* .
                - **ParentId** *(string) --* 
                  For nested stacks--stacks created as resources for another stack--the stack ID of the direct parent of this stack. For the first level of nested stacks, the root stack is also the parent stack.
                  For more information, see `Working with Nested Stacks <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__ in the *AWS CloudFormation User Guide* .
                - **RootId** *(string) --* 
                  For nested stacks--stacks created as resources for another stack--the stack ID of the the top-level stack to which the nested stack ultimately belongs.
                  For more information, see `Working with Nested Stacks <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__ in the *AWS CloudFormation User Guide* .
                - **DriftInformation** *(dict) --* 
                  Information on whether a stack's actual configuration differs, or has *drifted* , from it's expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see `Detecting Unregulated Configuration Changes to Stacks and Resources <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__ .
                  - **StackDriftStatus** *(string) --* 
                    Status of the stack's actual configuration compared to its expected template configuration. 
                    * ``DRIFTED`` : The stack differs from its expected template configuration. A stack is considered to have drifted if one or more of its resources have drifted. 
                    * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack differs from its expected template configuration. 
                    * ``IN_SYNC`` : The stack's actual configuration matches its expected template configuration. 
                    * ``UNKNOWN`` : This value is reserved for future use. 
                  - **LastCheckTimestamp** *(datetime) --* 
                    Most recent time when a drift detection operation was initiated on the stack, or any of its individual resources that support drift detection.
        :type StackName: string
        :param StackName:
          The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
          * Running stacks: You can specify either the stack\'s name or its unique stack ID.
          * Deleted stacks: You must specify the unique stack ID.
          Default: There is no default value.
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


class ListChangeSets(Paginator):
    def paginate(self, StackName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudFormation.Client.list_change_sets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListChangeSets>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              StackName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Summaries': [
                    {
                        'StackId': 'string',
                        'StackName': 'string',
                        'ChangeSetId': 'string',
                        'ChangeSetName': 'string',
                        'ExecutionStatus': 'UNAVAILABLE'|'AVAILABLE'|'EXECUTE_IN_PROGRESS'|'EXECUTE_COMPLETE'|'EXECUTE_FAILED'|'OBSOLETE',
                        'Status': 'CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'DELETE_COMPLETE'|'FAILED',
                        'StatusReason': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'Description': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            The output for the  ListChangeSets action.
            - **Summaries** *(list) --* 
              A list of ``ChangeSetSummary`` structures that provides the ID and status of each change set for the specified stack.
              - *(dict) --* 
                The ``ChangeSetSummary`` structure describes a change set, its status, and the stack with which it's associated.
                - **StackId** *(string) --* 
                  The ID of the stack with which the change set is associated.
                - **StackName** *(string) --* 
                  The name of the stack with which the change set is associated.
                - **ChangeSetId** *(string) --* 
                  The ID of the change set.
                - **ChangeSetName** *(string) --* 
                  The name of the change set.
                - **ExecutionStatus** *(string) --* 
                  If the change set execution status is ``AVAILABLE`` , you can execute the change set. If you can’t execute the change set, the status indicates why. For example, a change set might be in an ``UNAVAILABLE`` state because AWS CloudFormation is still creating it or in an ``OBSOLETE`` state because the stack was already updated.
                - **Status** *(string) --* 
                  The state of the change set, such as ``CREATE_IN_PROGRESS`` , ``CREATE_COMPLETE`` , or ``FAILED`` .
                - **StatusReason** *(string) --* 
                  A description of the change set's status. For example, if your change set is in the ``FAILED`` state, AWS CloudFormation shows the error message.
                - **CreationTime** *(datetime) --* 
                  The start time when the change set was created, in UTC.
                - **Description** *(string) --* 
                  Descriptive information about the change set.
        :type StackName: string
        :param StackName: **[REQUIRED]**
          The name or the Amazon Resource Name (ARN) of the stack for which you want to list change sets.
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


class ListExports(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudFormation.Client.list_exports`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListExports>`_
        
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
                'Exports': [
                    {
                        'ExportingStackId': 'string',
                        'Name': 'string',
                        'Value': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Exports** *(list) --* 
              The output for the  ListExports action.
              - *(dict) --* 
                The ``Export`` structure describes the exported output values for a stack.
                - **ExportingStackId** *(string) --* 
                  The stack that contains the exported output name and value.
                - **Name** *(string) --* 
                  The name of exported output value. Use this name and the ``Fn::ImportValue`` function to import the associated value into other stacks. The name is defined in the ``Export`` field in the associated stack's ``Outputs`` section.
                - **Value** *(string) --* 
                  The value of the exported output, such as a resource physical ID. This value is defined in the ``Export`` field in the associated stack's ``Outputs`` section.
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


class ListImports(Paginator):
    def paginate(self, ExportName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudFormation.Client.list_imports`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListImports>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ExportName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Imports': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Imports** *(list) --* 
              A list of stack names that are importing the specified exported output value. 
              - *(string) --* 
        :type ExportName: string
        :param ExportName: **[REQUIRED]**
          The name of the exported output value. AWS CloudFormation returns the stack names that are importing this value.
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


class ListStackInstances(Paginator):
    def paginate(self, StackSetName: str, StackInstanceAccount: str = None, StackInstanceRegion: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudFormation.Client.list_stack_instances`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListStackInstances>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              StackSetName='string',
              StackInstanceAccount='string',
              StackInstanceRegion='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Summaries': [
                    {
                        'StackSetId': 'string',
                        'Region': 'string',
                        'Account': 'string',
                        'StackId': 'string',
                        'Status': 'CURRENT'|'OUTDATED'|'INOPERABLE',
                        'StatusReason': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Summaries** *(list) --* 
              A list of ``StackInstanceSummary`` structures that contain information about the specified stack instances.
              - *(dict) --* 
                The structure that contains summary information about a stack instance.
                - **StackSetId** *(string) --* 
                  The name or unique ID of the stack set that the stack instance is associated with.
                - **Region** *(string) --* 
                  The name of the AWS region that the stack instance is associated with.
                - **Account** *(string) --* 
                  The name of the AWS account that the stack instance is associated with.
                - **StackId** *(string) --* 
                  The ID of the stack instance.
                - **Status** *(string) --* 
                  The status of the stack instance, in terms of its synchronization with its associated stack set.
                  * ``INOPERABLE`` : A ``DeleteStackInstances`` operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further ``UpdateStackSet`` operations. You might need to perform a ``DeleteStackInstances`` operation, with ``RetainStacks`` set to ``true`` , to delete the stack instance, and then delete the stack manually. 
                  * ``OUTDATED`` : The stack isn't currently up to date with the stack set because: 
                    * The associated stack failed during a ``CreateStackSet`` or ``UpdateStackSet`` operation.  
                    * The stack was part of a ``CreateStackSet`` or ``UpdateStackSet`` operation that failed or was stopped before the stack was created or updated.  
                  * ``CURRENT`` : The stack is currently up to date with the stack set. 
                - **StatusReason** *(string) --* 
                  The explanation for the specific status code assigned to this stack instance.
        :type StackSetName: string
        :param StackSetName: **[REQUIRED]**
          The name or unique ID of the stack set that you want to list stack instances for.
        :type StackInstanceAccount: string
        :param StackInstanceAccount:
          The name of the AWS account that you want to list stack instances for.
        :type StackInstanceRegion: string
        :param StackInstanceRegion:
          The name of the region where you want to list stack instances.
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


class ListStackResources(Paginator):
    def paginate(self, StackName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudFormation.Client.list_stack_resources`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListStackResources>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              StackName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'StackResourceSummaries': [
                    {
                        'LogicalResourceId': 'string',
                        'PhysicalResourceId': 'string',
                        'ResourceType': 'string',
                        'LastUpdatedTimestamp': datetime(2015, 1, 1),
                        'ResourceStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'DELETE_SKIPPED'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED'|'UPDATE_COMPLETE',
                        'ResourceStatusReason': 'string',
                        'DriftInformation': {
                            'StackResourceDriftStatus': 'IN_SYNC'|'MODIFIED'|'DELETED'|'NOT_CHECKED',
                            'LastCheckTimestamp': datetime(2015, 1, 1)
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            The output for a  ListStackResources action.
            - **StackResourceSummaries** *(list) --* 
              A list of ``StackResourceSummary`` structures.
              - *(dict) --* 
                Contains high-level information about the specified stack resource.
                - **LogicalResourceId** *(string) --* 
                  The logical name of the resource specified in the template.
                - **PhysicalResourceId** *(string) --* 
                  The name or unique identifier that corresponds to a physical instance ID of the resource.
                - **ResourceType** *(string) --* 
                  Type of resource. (For more information, go to `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ in the AWS CloudFormation User Guide.)
                - **LastUpdatedTimestamp** *(datetime) --* 
                  Time the status was updated.
                - **ResourceStatus** *(string) --* 
                  Current status of the resource.
                - **ResourceStatusReason** *(string) --* 
                  Success/failure message associated with the resource.
                - **DriftInformation** *(dict) --* 
                  Information about whether the resource's actual configuration differs, or has *drifted* , from its expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see `Detecting Unregulated Configuration Changes to Stacks and Resources <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__ .
                  - **StackResourceDriftStatus** *(string) --* 
                    Status of the resource's actual configuration compared to its expected configuration
                    * ``DELETED`` : The resource differs from its expected configuration in that it has been deleted. 
                    * ``MODIFIED`` : The resource differs from its expected configuration. 
                    * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the resource differs from its expected configuration. Any resources that do not currently support drift detection have a status of ``NOT_CHECKED`` . For more information, see `Resources that Support Drift Detection <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__ . If you performed an  ContinueUpdateRollback operation on a stack, any resources included in ``ResourcesToSkip`` will also have a status of ``NOT_CHECKED`` . For more information on skipping resources during rollback operations, see `Continue Rolling Back an Update <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html>`__ in the AWS CloudFormation User Guide. 
                    * ``IN_SYNC`` : The resources's actual configuration matches its expected configuration. 
                  - **LastCheckTimestamp** *(datetime) --* 
                    When AWS CloudFormation last checked if the resource had drifted from its expected configuration.
        :type StackName: string
        :param StackName: **[REQUIRED]**
          The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
          * Running stacks: You can specify either the stack\'s name or its unique stack ID.
          * Deleted stacks: You must specify the unique stack ID.
          Default: There is no default value.
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


class ListStackSetOperationResults(Paginator):
    def paginate(self, StackSetName: str, OperationId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudFormation.Client.list_stack_set_operation_results`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListStackSetOperationResults>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              StackSetName='string',
              OperationId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Summaries': [
                    {
                        'Account': 'string',
                        'Region': 'string',
                        'Status': 'PENDING'|'RUNNING'|'SUCCEEDED'|'FAILED'|'CANCELLED',
                        'StatusReason': 'string',
                        'AccountGateResult': {
                            'Status': 'SUCCEEDED'|'FAILED'|'SKIPPED',
                            'StatusReason': 'string'
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Summaries** *(list) --* 
              A list of ``StackSetOperationResultSummary`` structures that contain information about the specified operation results, for accounts and regions that are included in the operation.
              - *(dict) --* 
                The structure that contains information about a specified operation's results for a given account in a given region.
                - **Account** *(string) --* 
                  The name of the AWS account for this operation result.
                - **Region** *(string) --* 
                  The name of the AWS region for this operation result.
                - **Status** *(string) --* 
                  The result status of the stack set operation for the given account in the given region.
                  * ``CANCELLED`` : The operation in the specified account and region has been cancelled. This is either because a user has stopped the stack set operation, or because the failure tolerance of the stack set operation has been exceeded. 
                  * ``FAILED`` : The operation in the specified account and region failed.  If the stack set operation fails in enough accounts within a region, the failure tolerance for the stack set operation as a whole might be exceeded.  
                  * ``RUNNING`` : The operation in the specified account and region is currently in progress. 
                  * ``PENDING`` : The operation in the specified account and region has yet to start.  
                  * ``SUCCEEDED`` : The operation in the specified account and region completed successfully. 
                - **StatusReason** *(string) --* 
                  The reason for the assigned result status.
                - **AccountGateResult** *(dict) --* 
                  The results of the account gate function AWS CloudFormation invokes, if present, before proceeding with stack set operations in an account
                  - **Status** *(string) --* 
                    The status of the account gate function.
                    * ``SUCCEEDED`` : The account gate function has determined that the account and region passes any requirements for a stack set operation to occur. AWS CloudFormation proceeds with the stack operation in that account and region.  
                    * ``FAILED`` : The account gate function has determined that the account and region does not meet the requirements for a stack set operation to occur. AWS CloudFormation cancels the stack set operation in that account and region, and sets the stack set operation result status for that account and region to ``FAILED`` .  
                    * ``SKIPPED`` : AWS CloudFormation has skipped calling the account gate function for this account and region, for one of the following reasons: 
                      * An account gate function has not been specified for the account and region. AWS CloudFormation proceeds with the stack set operation in this account and region. 
                      * The ``AWSCloudFormationStackSetExecutionRole`` of the stack set adminstration account lacks permissions to invoke the function. AWS CloudFormation proceeds with the stack set operation in this account and region. 
                      * Either no action is necessary, or no action is possible, on the stack. AWS CloudFormation skips the stack set operation in this account and region. 
                  - **StatusReason** *(string) --* 
                    The reason for the account gate status assigned to this account and region for the stack set operation.
        :type StackSetName: string
        :param StackSetName: **[REQUIRED]**
          The name or unique ID of the stack set that you want to get operation results for.
        :type OperationId: string
        :param OperationId: **[REQUIRED]**
          The ID of the stack set operation.
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


class ListStackSetOperations(Paginator):
    def paginate(self, StackSetName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudFormation.Client.list_stack_set_operations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListStackSetOperations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              StackSetName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Summaries': [
                    {
                        'OperationId': 'string',
                        'Action': 'CREATE'|'UPDATE'|'DELETE',
                        'Status': 'RUNNING'|'SUCCEEDED'|'FAILED'|'STOPPING'|'STOPPED',
                        'CreationTimestamp': datetime(2015, 1, 1),
                        'EndTimestamp': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Summaries** *(list) --* 
              A list of ``StackSetOperationSummary`` structures that contain summary information about operations for the specified stack set.
              - *(dict) --* 
                The structures that contain summary information about the specified operation.
                - **OperationId** *(string) --* 
                  The unique ID of the stack set operation.
                - **Action** *(string) --* 
                  The type of operation: ``CREATE`` , ``UPDATE`` , or ``DELETE`` . Create and delete operations affect only the specified stack instances that are associated with the specified stack set. Update operations affect both the stack set itself as well as *all* associated stack set instances.
                - **Status** *(string) --* 
                  The overall status of the operation.
                  * ``FAILED`` : The operation exceeded the specified failure tolerance. The failure tolerance value that you've set for an operation is applied for each region during stack create and update operations. If the number of failed stacks within a region exceeds the failure tolerance, the status of the operation in the region is set to ``FAILED`` . This in turn sets the status of the operation as a whole to ``FAILED`` , and AWS CloudFormation cancels the operation in any remaining regions. 
                  * ``RUNNING`` : The operation is currently being performed. 
                  * ``STOPPED`` : The user has cancelled the operation. 
                  * ``STOPPING`` : The operation is in the process of stopping, at user request.  
                  * ``SUCCEEDED`` : The operation completed creating or updating all the specified stacks without exceeding the failure tolerance for the operation. 
                - **CreationTimestamp** *(datetime) --* 
                  The time at which the operation was initiated. Note that the creation times for the stack set operation might differ from the creation time of the individual stacks themselves. This is because AWS CloudFormation needs to perform preparatory work for the operation, such as dispatching the work to the requested regions, before actually creating the first stacks.
                - **EndTimestamp** *(datetime) --* 
                  The time at which the stack set operation ended, across all accounts and regions specified. Note that this doesn't necessarily mean that the stack set operation was successful, or even attempted, in each account or region.
        :type StackSetName: string
        :param StackSetName: **[REQUIRED]**
          The name or unique ID of the stack set that you want to get operation summaries for.
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


class ListStackSets(Paginator):
    def paginate(self, Status: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudFormation.Client.list_stack_sets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListStackSets>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Status='ACTIVE'|'DELETED',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Summaries': [
                    {
                        'StackSetName': 'string',
                        'StackSetId': 'string',
                        'Description': 'string',
                        'Status': 'ACTIVE'|'DELETED'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Summaries** *(list) --* 
              A list of ``StackSetSummary`` structures that contain information about the user's stack sets.
              - *(dict) --* 
                The structures that contain summary information about the specified stack set.
                - **StackSetName** *(string) --* 
                  The name of the stack set.
                - **StackSetId** *(string) --* 
                  The ID of the stack set.
                - **Description** *(string) --* 
                  A description of the stack set that you specify when the stack set is created or updated.
                - **Status** *(string) --* 
                  The status of the stack set.
        :type Status: string
        :param Status:
          The status of the stack sets that you want to get summary information about.
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


class ListStacks(Paginator):
    def paginate(self, StackStatusFilter: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CloudFormation.Client.list_stacks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListStacks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              StackStatusFilter=[
                  'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'ROLLBACK_IN_PROGRESS'|'ROLLBACK_FAILED'|'ROLLBACK_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'UPDATE_IN_PROGRESS'|'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_COMPLETE'|'UPDATE_ROLLBACK_IN_PROGRESS'|'UPDATE_ROLLBACK_FAILED'|'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_ROLLBACK_COMPLETE'|'REVIEW_IN_PROGRESS',
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
                'StackSummaries': [
                    {
                        'StackId': 'string',
                        'StackName': 'string',
                        'TemplateDescription': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastUpdatedTime': datetime(2015, 1, 1),
                        'DeletionTime': datetime(2015, 1, 1),
                        'StackStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'ROLLBACK_IN_PROGRESS'|'ROLLBACK_FAILED'|'ROLLBACK_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'UPDATE_IN_PROGRESS'|'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_COMPLETE'|'UPDATE_ROLLBACK_IN_PROGRESS'|'UPDATE_ROLLBACK_FAILED'|'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_ROLLBACK_COMPLETE'|'REVIEW_IN_PROGRESS',
                        'StackStatusReason': 'string',
                        'ParentId': 'string',
                        'RootId': 'string',
                        'DriftInformation': {
                            'StackDriftStatus': 'DRIFTED'|'IN_SYNC'|'UNKNOWN'|'NOT_CHECKED',
                            'LastCheckTimestamp': datetime(2015, 1, 1)
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            The output for  ListStacks action.
            - **StackSummaries** *(list) --* 
              A list of ``StackSummary`` structures containing information about the specified stacks.
              - *(dict) --* 
                The StackSummary Data Type
                - **StackId** *(string) --* 
                  Unique stack identifier.
                - **StackName** *(string) --* 
                  The name associated with the stack.
                - **TemplateDescription** *(string) --* 
                  The template description of the template used to create the stack.
                - **CreationTime** *(datetime) --* 
                  The time the stack was created.
                - **LastUpdatedTime** *(datetime) --* 
                  The time the stack was last updated. This field will only be returned if the stack has been updated at least once.
                - **DeletionTime** *(datetime) --* 
                  The time the stack was deleted.
                - **StackStatus** *(string) --* 
                  The current status of the stack.
                - **StackStatusReason** *(string) --* 
                  Success/Failure message associated with the stack status.
                - **ParentId** *(string) --* 
                  For nested stacks--stacks created as resources for another stack--the stack ID of the direct parent of this stack. For the first level of nested stacks, the root stack is also the parent stack.
                  For more information, see `Working with Nested Stacks <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__ in the *AWS CloudFormation User Guide* .
                - **RootId** *(string) --* 
                  For nested stacks--stacks created as resources for another stack--the stack ID of the the top-level stack to which the nested stack ultimately belongs.
                  For more information, see `Working with Nested Stacks <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__ in the *AWS CloudFormation User Guide* .
                - **DriftInformation** *(dict) --* 
                  Summarizes information on whether a stack's actual configuration differs, or has *drifted* , from it's expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see `Detecting Unregulated Configuration Changes to Stacks and Resources <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__ .
                  - **StackDriftStatus** *(string) --* 
                    Status of the stack's actual configuration compared to its expected template configuration. 
                    * ``DRIFTED`` : The stack differs from its expected template configuration. A stack is considered to have drifted if one or more of its resources have drifted. 
                    * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack differs from its expected template configuration. 
                    * ``IN_SYNC`` : The stack's actual configuration matches its expected template configuration. 
                    * ``UNKNOWN`` : This value is reserved for future use. 
                  - **LastCheckTimestamp** *(datetime) --* 
                    Most recent time when a drift detection operation was initiated on the stack, or any of its individual resources that support drift detection.
        :type StackStatusFilter: list
        :param StackStatusFilter:
          Stack status to use as a filter. Specify one or more stack status codes to list only stacks with the specified status codes. For a complete list of stack status codes, see the ``StackStatus`` parameter of the  Stack data type.
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
