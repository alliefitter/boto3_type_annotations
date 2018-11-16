from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeStackEvents(Paginator):
    def paginate(self, StackName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStackEvents>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              StackName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'StackEvents\': [
                    {
                        \'StackId\': \'string\',
                        \'EventId\': \'string\',
                        \'StackName\': \'string\',
                        \'LogicalResourceId\': \'string\',
                        \'PhysicalResourceId\': \'string\',
                        \'ResourceType\': \'string\',
                        \'Timestamp\': datetime(2015, 1, 1),
                        \'ResourceStatus\': \'CREATE_IN_PROGRESS\'|\'CREATE_FAILED\'|\'CREATE_COMPLETE\'|\'DELETE_IN_PROGRESS\'|\'DELETE_FAILED\'|\'DELETE_COMPLETE\'|\'DELETE_SKIPPED\'|\'UPDATE_IN_PROGRESS\'|\'UPDATE_FAILED\'|\'UPDATE_COMPLETE\',
                        \'ResourceStatusReason\': \'string\',
                        \'ResourceProperties\': \'string\',
                        \'ClientRequestToken\': \'string\'
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
        
                  Type of resource. (For more information, go to `AWS Resource Types Reference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ in the AWS CloudFormation User Guide.)
        
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
        
        """
        pass


class DescribeStacks(Paginator):
    def paginate(self, StackName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStacks>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              StackName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Stacks\': [
                    {
                        \'StackId\': \'string\',
                        \'StackName\': \'string\',
                        \'ChangeSetId\': \'string\',
                        \'Description\': \'string\',
                        \'Parameters\': [
                            {
                                \'ParameterKey\': \'string\',
                                \'ParameterValue\': \'string\',
                                \'UsePreviousValue\': True|False,
                                \'ResolvedValue\': \'string\'
                            },
                        ],
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'DeletionTime\': datetime(2015, 1, 1),
                        \'LastUpdatedTime\': datetime(2015, 1, 1),
                        \'RollbackConfiguration\': {
                            \'RollbackTriggers\': [
                                {
                                    \'Arn\': \'string\',
                                    \'Type\': \'string\'
                                },
                            ],
                            \'MonitoringTimeInMinutes\': 123
                        },
                        \'StackStatus\': \'CREATE_IN_PROGRESS\'|\'CREATE_FAILED\'|\'CREATE_COMPLETE\'|\'ROLLBACK_IN_PROGRESS\'|\'ROLLBACK_FAILED\'|\'ROLLBACK_COMPLETE\'|\'DELETE_IN_PROGRESS\'|\'DELETE_FAILED\'|\'DELETE_COMPLETE\'|\'UPDATE_IN_PROGRESS\'|\'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS\'|\'UPDATE_COMPLETE\'|\'UPDATE_ROLLBACK_IN_PROGRESS\'|\'UPDATE_ROLLBACK_FAILED\'|\'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS\'|\'UPDATE_ROLLBACK_COMPLETE\'|\'REVIEW_IN_PROGRESS\',
                        \'StackStatusReason\': \'string\',
                        \'DisableRollback\': True|False,
                        \'NotificationARNs\': [
                            \'string\',
                        ],
                        \'TimeoutInMinutes\': 123,
                        \'Capabilities\': [
                            \'CAPABILITY_IAM\'|\'CAPABILITY_NAMED_IAM\',
                        ],
                        \'Outputs\': [
                            {
                                \'OutputKey\': \'string\',
                                \'OutputValue\': \'string\',
                                \'Description\': \'string\',
                                \'ExportName\': \'string\'
                            },
                        ],
                        \'RoleARN\': \'string\',
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'EnableTerminationProtection\': True|False,
                        \'ParentId\': \'string\',
                        \'RootId\': \'string\',
                        \'DriftInformation\': {
                            \'StackDriftStatus\': \'DRIFTED\'|\'IN_SYNC\'|\'UNKNOWN\'|\'NOT_CHECKED\',
                            \'LastCheckTimestamp\': datetime(2015, 1, 1)
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
        
                      The key associated with the parameter. If you don\'t specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
        
                    - **ParameterValue** *(string) --* 
        
                      The input value associated with the parameter.
        
                    - **UsePreviousValue** *(boolean) --* 
        
                      During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify ``true`` , do not specify a parameter value.
        
                    - **ResolvedValue** *(string) --* 
        
                      Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` ``SSM`` parameter types <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.
        
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
        
                    * To use the rollback triggers previously specified for this stack, if any, don\'t specify this parameter. 
                     
                    * To specify new or updated rollback triggers, you must specify *all* the triggers that you want used for this stack, even triggers you\'ve specifed before (for example, when creating the stack or during a previous stack update). Any triggers that you don\'t include in the updated list of triggers are no longer applied to the stack. 
                     
                    * To remove all currently specified triggers, specify an empty list for this parameter. 
                     
                    If a specified trigger is missing, the entire stack operation fails and is rolled back. 
        
                    - *(dict) --* 
        
                      A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any of the alarms you specify goes to ALARM state during the stack operation or within the specified monitoring period afterwards, CloudFormation rolls back the entire stack operation. 
        
                      - **Arn** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the rollback trigger.
        
                        If a specified trigger is missing, the entire stack operation fails and is rolled back. 
        
                      - **Type** *(string) --* 
        
                        The resource type of the rollback trigger. Currently, `AWS\:\:CloudWatch\:\:Alarm <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__ is the only supported resource type.
        
                  - **MonitoringTimeInMinutes** *(integer) --* 
        
                    The amount of time, in minutes, during which CloudFormation should monitor all the rollback triggers after the stack creation or update operation deploys all necessary resources.
        
                    The default is 0 minutes.
        
                    If you specify a monitoring period but do not specify any rollback triggers, CloudFormation still waits the specified period of time before cleaning up old resources after update operations. You can use this monitoring period to perform any manual stack validation desired, and manually cancel the stack creation or update (using `CancelUpdateStack <http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__ , for example) as necessary.
        
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
        
                  The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that is associated with the stack. During a stack operation, AWS CloudFormation uses this role\'s credentials to make calls on your behalf.
        
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
        
                  Information on whether a stack\'s actual configuration differs, or has *drifted* , from it\'s expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see `Detecting Unregulated Configuration Changes to Stacks and Resources <http://docs.aws.amazon.com/http:/docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__ .
        
                  - **StackDriftStatus** *(string) --* 
        
                    Status of the stack\'s actual configuration compared to its expected template configuration. 
        
                    * ``DRIFTED`` : The stack differs from its expected template configuration. A stack is considered to have drifted if one or more of its resources have drifted. 
                     
                    * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack differs from its expected template configuration. 
                     
                    * ``IN_SYNC`` : The stack\'s actual configuration matches its expected template configuration. 
                     
                    * ``UNKNOWN`` : This value is reserved for future use. 
                     
                  - **LastCheckTimestamp** *(datetime) --* 
        
                    Most recent time when a drift detection operation was initiated on the stack, or any of its individual resources that support drift detection.
        
        """
        pass


class ListExports(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListExports>`_
        
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
                \'Exports\': [
                    {
                        \'ExportingStackId\': \'string\',
                        \'Name\': \'string\',
                        \'Value\': \'string\'
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
        
                  The name of exported output value. Use this name and the ``Fn::ImportValue`` function to import the associated value into other stacks. The name is defined in the ``Export`` field in the associated stack\'s ``Outputs`` section.
        
                - **Value** *(string) --* 
        
                  The value of the exported output, such as a resource physical ID. This value is defined in the ``Export`` field in the associated stack\'s ``Outputs`` section.
        
        """
        pass


class ListImports(Paginator):
    def paginate(self, ExportName: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListImports>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ExportName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Imports\': [
                    \'string\',
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Imports** *(list) --* 
        
              A list of stack names that are importing the specified exported output value. 
        
              - *(string) --* 
          
        """
        pass


class ListStackResources(Paginator):
    def paginate(self, StackName: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListStackResources>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              StackName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'StackResourceSummaries\': [
                    {
                        \'LogicalResourceId\': \'string\',
                        \'PhysicalResourceId\': \'string\',
                        \'ResourceType\': \'string\',
                        \'LastUpdatedTimestamp\': datetime(2015, 1, 1),
                        \'ResourceStatus\': \'CREATE_IN_PROGRESS\'|\'CREATE_FAILED\'|\'CREATE_COMPLETE\'|\'DELETE_IN_PROGRESS\'|\'DELETE_FAILED\'|\'DELETE_COMPLETE\'|\'DELETE_SKIPPED\'|\'UPDATE_IN_PROGRESS\'|\'UPDATE_FAILED\'|\'UPDATE_COMPLETE\',
                        \'ResourceStatusReason\': \'string\',
                        \'DriftInformation\': {
                            \'StackResourceDriftStatus\': \'IN_SYNC\'|\'MODIFIED\'|\'DELETED\'|\'NOT_CHECKED\',
                            \'LastCheckTimestamp\': datetime(2015, 1, 1)
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
        
                  Type of resource. (For more information, go to `AWS Resource Types Reference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ in the AWS CloudFormation User Guide.)
        
                - **LastUpdatedTimestamp** *(datetime) --* 
        
                  Time the status was updated.
        
                - **ResourceStatus** *(string) --* 
        
                  Current status of the resource.
        
                - **ResourceStatusReason** *(string) --* 
        
                  Success/failure message associated with the resource.
        
                - **DriftInformation** *(dict) --* 
        
                  Information about whether the resource\'s actual configuration differs, or has *drifted* , from its expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see `Detecting Unregulated Configuration Changes to Stacks and Resources <http://docs.aws.amazon.com/http:/docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__ .
        
                  - **StackResourceDriftStatus** *(string) --* 
        
                    Status of the resource\'s actual configuration compared to its expected configuration
        
                    * ``DELETED`` : The resource differs from its expected configuration in that it has been deleted. 
                     
                    * ``MODIFIED`` : The resource differs from its expected configuration. 
                     
                    * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the resource differs from its expected configuration. Any resources that do not currently support drift detection have a status of ``NOT_CHECKED`` . For more information, see `Resources that Support Drift Detection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__ . If you performed an  ContinueUpdateRollback operation on a stack, any resources included in ``ResourcesToSkip`` will also have a status of ``NOT_CHECKED`` . For more information on skipping resources during rollback operations, see `Continue Rolling Back an Update <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html>`__ in the AWS CloudFormation User Guide. 
                     
                    * ``IN_SYNC`` : The resources\'s actual configuration matches its expected configuration. 
                     
                  - **LastCheckTimestamp** *(datetime) --* 
        
                    When AWS CloudFormation last checked if the resource had drifted from its expected configuration.
        
        """
        pass


class ListStacks(Paginator):
    def paginate(self, StackStatusFilter: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListStacks>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              StackStatusFilter=[
                  \'CREATE_IN_PROGRESS\'|\'CREATE_FAILED\'|\'CREATE_COMPLETE\'|\'ROLLBACK_IN_PROGRESS\'|\'ROLLBACK_FAILED\'|\'ROLLBACK_COMPLETE\'|\'DELETE_IN_PROGRESS\'|\'DELETE_FAILED\'|\'DELETE_COMPLETE\'|\'UPDATE_IN_PROGRESS\'|\'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS\'|\'UPDATE_COMPLETE\'|\'UPDATE_ROLLBACK_IN_PROGRESS\'|\'UPDATE_ROLLBACK_FAILED\'|\'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS\'|\'UPDATE_ROLLBACK_COMPLETE\'|\'REVIEW_IN_PROGRESS\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'StackSummaries\': [
                    {
                        \'StackId\': \'string\',
                        \'StackName\': \'string\',
                        \'TemplateDescription\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'LastUpdatedTime\': datetime(2015, 1, 1),
                        \'DeletionTime\': datetime(2015, 1, 1),
                        \'StackStatus\': \'CREATE_IN_PROGRESS\'|\'CREATE_FAILED\'|\'CREATE_COMPLETE\'|\'ROLLBACK_IN_PROGRESS\'|\'ROLLBACK_FAILED\'|\'ROLLBACK_COMPLETE\'|\'DELETE_IN_PROGRESS\'|\'DELETE_FAILED\'|\'DELETE_COMPLETE\'|\'UPDATE_IN_PROGRESS\'|\'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS\'|\'UPDATE_COMPLETE\'|\'UPDATE_ROLLBACK_IN_PROGRESS\'|\'UPDATE_ROLLBACK_FAILED\'|\'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS\'|\'UPDATE_ROLLBACK_COMPLETE\'|\'REVIEW_IN_PROGRESS\',
                        \'StackStatusReason\': \'string\',
                        \'ParentId\': \'string\',
                        \'RootId\': \'string\',
                        \'DriftInformation\': {
                            \'StackDriftStatus\': \'DRIFTED\'|\'IN_SYNC\'|\'UNKNOWN\'|\'NOT_CHECKED\',
                            \'LastCheckTimestamp\': datetime(2015, 1, 1)
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
        
                  Summarizes information on whether a stack\'s actual configuration differs, or has *drifted* , from it\'s expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see `Detecting Unregulated Configuration Changes to Stacks and Resources <http://docs.aws.amazon.com/http:/docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__ .
        
                  - **StackDriftStatus** *(string) --* 
        
                    Status of the stack\'s actual configuration compared to its expected template configuration. 
        
                    * ``DRIFTED`` : The stack differs from its expected template configuration. A stack is considered to have drifted if one or more of its resources have drifted. 
                     
                    * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack differs from its expected template configuration. 
                     
                    * ``IN_SYNC`` : The stack\'s actual configuration matches its expected template configuration. 
                     
                    * ``UNKNOWN`` : This value is reserved for future use. 
                     
                  - **LastCheckTimestamp** *(datetime) --* 
        
                    Most recent time when a drift detection operation was initiated on the stack, or any of its individual resources that support drift detection.
        
        """
        pass
