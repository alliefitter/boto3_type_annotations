from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None) -> NoReturn:
        """
        
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        
        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """
        pass

    def cancel_update_stack(self, StackName: str, ClientRequestToken: str = None) -> NoReturn:
        """
        
        .. note::
        
          You can cancel only stacks that are in the UPDATE_IN_PROGRESS state.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CancelUpdateStack>`_
        
        **Request Syntax** 
        ::
        
          response = client.cancel_update_stack(
              StackName=\'string\',
              ClientRequestToken=\'string\'
          )
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name or the unique stack ID that is associated with the stack.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          A unique identifier for this ``CancelUpdateStack`` request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you\'re not attempting to cancel an update on a stack with the same name. You might retry ``CancelUpdateStack`` requests to ensure that AWS CloudFormation successfully received them.
        
        :returns: None
        """
        pass

    def continue_update_rollback(self, StackName: str, RoleARN: str = None, ResourcesToSkip: List = None, ClientRequestToken: str = None) -> Dict:
        """
        
        A stack goes into the ``UPDATE_ROLLBACK_FAILED`` state when AWS CloudFormation cannot roll back all changes after a failed stack update. For example, you might have a stack that is rolling back to an old database instance that was deleted outside of AWS CloudFormation. Because AWS CloudFormation doesn\'t know the database was deleted, it assumes that the database instance still exists and attempts to roll back to it, causing the update rollback to fail.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ContinueUpdateRollback>`_
        
        **Request Syntax** 
        ::
        
          response = client.continue_update_rollback(
              StackName=\'string\',
              RoleARN=\'string\',
              ResourcesToSkip=[
                  \'string\',
              ],
              ClientRequestToken=\'string\'
          )
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name or the unique ID of the stack that you want to continue rolling back.
        
          .. note::
        
            Don\'t specify the name of a nested stack (a stack that was created by using the ``AWS::CloudFormation::Stack`` resource). Instead, use this operation on the parent stack (the stack that contains the ``AWS::CloudFormation::Stack`` resource).
        
        :type RoleARN: string
        :param RoleARN: 
        
          The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes to roll back the stack. AWS CloudFormation uses the role\'s credentials to make calls on your behalf. AWS CloudFormation always uses this role for all future operations on the stack. As long as users have permission to operate on the stack, AWS CloudFormation uses this role even if the users don\'t have permission to pass it. Ensure that the role grants least privilege.
        
          If you don\'t specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
        
        :type ResourcesToSkip: list
        :param ResourcesToSkip: 
        
          A list of the logical IDs of the resources that AWS CloudFormation skips during the continue update rollback operation. You can specify only resources that are in the ``UPDATE_FAILED`` state because a rollback failed. You can\'t specify resources that are in the ``UPDATE_FAILED`` state for other reasons, for example, because an update was cancelled. To check why a resource update failed, use the  DescribeStackResources action, and view the resource status reason. 
        
          .. warning::
        
            Specify this property to skip rolling back resources that AWS CloudFormation can\'t successfully roll back. We recommend that you `troubleshoot <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-update-rollback-failed>`__ resources before skipping them. AWS CloudFormation sets the status of the specified resources to ``UPDATE_COMPLETE`` and continues to roll back the stack. After the rollback is complete, the state of the skipped resources will be inconsistent with the state of the resources in the stack template. Before performing another stack update, you must update the stack or resources to be consistent with each other. If you don\'t, subsequent stack updates might fail, and the stack will become unrecoverable. 
        
          Specify the minimum number of resources required to successfully roll back your stack. For example, a failed resource update might cause dependent resources to fail. In this case, it might not be necessary to skip the dependent resources. 
        
          To skip resources that are part of nested stacks, use the following format: ``NestedStackName.ResourceLogicalID`` . If you want to specify the logical ID of a stack resource (``Type: AWS::CloudFormation::Stack`` ) in the ``ResourcesToSkip`` list, then its corresponding embedded stack must be in one of the following states: ``DELETE_IN_PROGRESS`` , ``DELETE_COMPLETE`` , or ``DELETE_FAILED`` . 
        
          .. note::
        
            Don\'t confuse a child stack\'s name with its corresponding logical ID defined in the parent stack. For an example of a continue update rollback operation with nested stacks, see `Using ResourcesToSkip to recover a nested stacks hierarchy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html#nested-stacks>`__ . 
        
          - *(string) --* 
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          A unique identifier for this ``ContinueUpdateRollback`` request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you\'re not attempting to continue the rollback to a stack with the same name. You might retry ``ContinueUpdateRollback`` requests to ensure that AWS CloudFormation successfully received them.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for a  ContinueUpdateRollback action.
        
        """
        pass

    def create_change_set(self, StackName: str, ChangeSetName: str, TemplateBody: str = None, TemplateURL: str = None, UsePreviousTemplate: bool = None, Parameters: List = None, Capabilities: List = None, ResourceTypes: List = None, RoleARN: str = None, RollbackConfiguration: Dict = None, NotificationARNs: List = None, Tags: List = None, ClientToken: str = None, Description: str = None, ChangeSetType: str = None) -> Dict:
        """
        
        Creates a list of changes that will be applied to a stack so that you can review the changes before executing them. You can create a change set for a stack that doesn\'t exist or an existing stack. If you create a change set for a stack that doesn\'t exist, the change set shows all of the resources that AWS CloudFormation will create. If you create a change set for an existing stack, AWS CloudFormation compares the stack\'s information with the information that you submit in the change set and lists the differences. Use change sets to understand which resources AWS CloudFormation will create or change, and how it will change resources in an existing stack, before you create or update a stack.
        
        To create a change set for a stack that doesn\'t exist, for the ``ChangeSetType`` parameter, specify ``CREATE`` . To create a change set for an existing stack, specify ``UPDATE`` for the ``ChangeSetType`` parameter. After the ``CreateChangeSet`` call successfully completes, AWS CloudFormation starts creating the change set. To check the status of the change set or to review it, use the  DescribeChangeSet action.
        
        When you are satisfied with the changes the change set will make, execute the change set by using the  ExecuteChangeSet action. AWS CloudFormation doesn\'t make changes until you execute the change set.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_change_set(
              StackName=\'string\',
              TemplateBody=\'string\',
              TemplateURL=\'string\',
              UsePreviousTemplate=True|False,
              Parameters=[
                  {
                      \'ParameterKey\': \'string\',
                      \'ParameterValue\': \'string\',
                      \'UsePreviousValue\': True|False,
                      \'ResolvedValue\': \'string\'
                  },
              ],
              Capabilities=[
                  \'CAPABILITY_IAM\'|\'CAPABILITY_NAMED_IAM\',
              ],
              ResourceTypes=[
                  \'string\',
              ],
              RoleARN=\'string\',
              RollbackConfiguration={
                  \'RollbackTriggers\': [
                      {
                          \'Arn\': \'string\',
                          \'Type\': \'string\'
                      },
                  ],
                  \'MonitoringTimeInMinutes\': 123
              },
              NotificationARNs=[
                  \'string\',
              ],
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              ChangeSetName=\'string\',
              ClientToken=\'string\',
              Description=\'string\',
              ChangeSetType=\'CREATE\'|\'UPDATE\'
          )
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name or the unique ID of the stack for which you are creating a change set. AWS CloudFormation generates the change set by comparing this stack\'s information with the information that you submit, such as a modified template or different parameter input values.
        
        :type TemplateBody: string
        :param TemplateBody: 
        
          A structure that contains the body of the revised template, with a minimum length of 1 byte and a maximum length of 51,200 bytes. AWS CloudFormation generates the change set by comparing this template with the template of the stack that you specified.
        
          Conditional: You must specify only ``TemplateBody`` or ``TemplateURL`` .
        
        :type TemplateURL: string
        :param TemplateURL: 
        
          The location of the file that contains the revised template. The URL must point to a template (max size: 460,800 bytes) that is located in an S3 bucket. AWS CloudFormation generates the change set by comparing this template with the stack that you specified.
        
          Conditional: You must specify only ``TemplateBody`` or ``TemplateURL`` .
        
        :type UsePreviousTemplate: boolean
        :param UsePreviousTemplate: 
        
          Whether to reuse the template that is associated with the stack to create the change set.
        
        :type Parameters: list
        :param Parameters: 
        
          A list of ``Parameter`` structures that specify input parameters for the change set. For more information, see the  Parameter data type.
        
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
        
        :type Capabilities: list
        :param Capabilities: 
        
          A list of values that you must specify before AWS CloudFormation can update certain stacks. Some stack templates might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge their capabilities by specifying this parameter.
        
          The only valid values are ``CAPABILITY_IAM`` and ``CAPABILITY_NAMED_IAM`` . The following resources require you to specify this parameter: `AWS\:\:IAM\:\:AccessKey <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html>`__ , `AWS\:\:IAM\:\:Group <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html>`__ , `AWS\:\:IAM\:\:InstanceProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html>`__ , `AWS\:\:IAM\:\:Policy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html>`__ , `AWS\:\:IAM\:\:Role <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html>`__ , `AWS\:\:IAM\:\:User <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html>`__ , and `AWS\:\:IAM\:\:UserToGroupAddition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html>`__ . If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.
        
          If you have IAM resources, you can specify either capability. If you have IAM resources with custom names, you must specify ``CAPABILITY_NAMED_IAM`` . If you don\'t specify this parameter, this action returns an ``InsufficientCapabilities`` error.
        
          For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities>`__ .
        
          - *(string) --* 
        
        :type ResourceTypes: list
        :param ResourceTypes: 
        
          The template resource types that you have permissions to work with if you execute this change set, such as ``AWS::EC2::Instance`` , ``AWS::EC2::*`` , or ``Custom::MyCustomInstance`` .
        
          If the list of resource types doesn\'t include a resource type that you\'re updating, the stack update fails. By default, AWS CloudFormation grants permissions to all resource types. AWS Identity and Access Management (IAM) uses this parameter for condition keys in IAM policies for AWS CloudFormation. For more information, see `Controlling Access with AWS Identity and Access Management <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html>`__ in the AWS CloudFormation User Guide.
        
          - *(string) --* 
        
        :type RoleARN: string
        :param RoleARN: 
        
          The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes when executing the change set. AWS CloudFormation uses the role\'s credentials to make calls on your behalf. AWS CloudFormation uses this role for all future operations on the stack. As long as users have permission to operate on the stack, AWS CloudFormation uses this role even if the users don\'t have permission to pass it. Ensure that the role grants least privilege.
        
          If you don\'t specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
        
        :type RollbackConfiguration: dict
        :param RollbackConfiguration: 
        
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
        
              - **Arn** *(string) --* **[REQUIRED]** 
        
                The Amazon Resource Name (ARN) of the rollback trigger.
        
                If a specified trigger is missing, the entire stack operation fails and is rolled back. 
        
              - **Type** *(string) --* **[REQUIRED]** 
        
                The resource type of the rollback trigger. Currently, `AWS\:\:CloudWatch\:\:Alarm <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__ is the only supported resource type.
        
          - **MonitoringTimeInMinutes** *(integer) --* 
        
            The amount of time, in minutes, during which CloudFormation should monitor all the rollback triggers after the stack creation or update operation deploys all necessary resources.
        
            The default is 0 minutes.
        
            If you specify a monitoring period but do not specify any rollback triggers, CloudFormation still waits the specified period of time before cleaning up old resources after update operations. You can use this monitoring period to perform any manual stack validation desired, and manually cancel the stack creation or update (using `CancelUpdateStack <http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__ , for example) as necessary.
        
            If you specify 0 for this parameter, CloudFormation still monitors the specified rollback triggers during stack creation and update operations. Then, for update operations, it begins disposing of old resources immediately once the operation completes.
        
        :type NotificationARNs: list
        :param NotificationARNs: 
        
          The Amazon Resource Names (ARNs) of Amazon Simple Notification Service (Amazon SNS) topics that AWS CloudFormation associates with the stack. To remove all associated notification topics, specify an empty list.
        
          - *(string) --* 
        
        :type Tags: list
        :param Tags: 
        
          Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to resources in the stack. You can specify a maximum of 50 tags.
        
          - *(dict) --* 
        
            The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
               *Required* . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .
        
            - **Value** *(string) --* **[REQUIRED]** 
        
               *Required* . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
        
        :type ChangeSetName: string
        :param ChangeSetName: **[REQUIRED]** 
        
          The name of the change set. The name must be unique among all change sets that are associated with the specified stack.
        
          A change set name can contain only alphanumeric, case sensitive characters and hyphens. It must start with an alphabetic character and cannot exceed 128 characters.
        
        :type ClientToken: string
        :param ClientToken: 
        
          A unique identifier for this ``CreateChangeSet`` request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you\'re not attempting to create another change set with the same name. You might retry ``CreateChangeSet`` requests to ensure that AWS CloudFormation successfully received them.
        
        :type Description: string
        :param Description: 
        
          A description to help you identify this change set.
        
        :type ChangeSetType: string
        :param ChangeSetType: 
        
          The type of change set operation. To create a change set for a new stack, specify ``CREATE`` . To create a change set for an existing stack, specify ``UPDATE`` .
        
          If you create a change set for a new stack, AWS Cloudformation creates a stack with a unique stack ID, but no template or resources. The stack will be in the ` ``REVIEW_IN_PROGRESS`` http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-describing-stacks.html#d0e11995`__ state until you execute the change set.
        
          By default, AWS CloudFormation specifies ``UPDATE`` . You can\'t use the ``UPDATE`` type to create a change set for a new stack or the ``CREATE`` type to create a change set for an existing stack.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Id\': \'string\',
                \'StackId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for the  CreateChangeSet action.
        
            - **Id** *(string) --* 
        
              The Amazon Resource Name (ARN) of the change set.
        
            - **StackId** *(string) --* 
        
              The unique ID of the stack.
        
        """
        pass

    def create_stack(self, StackName: str, TemplateBody: str = None, TemplateURL: str = None, Parameters: List = None, DisableRollback: bool = None, RollbackConfiguration: Dict = None, TimeoutInMinutes: int = None, NotificationARNs: List = None, Capabilities: List = None, ResourceTypes: List = None, RoleARN: str = None, OnFailure: str = None, StackPolicyBody: str = None, StackPolicyURL: str = None, Tags: List = None, ClientRequestToken: str = None, EnableTerminationProtection: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateStack>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_stack(
              StackName=\'string\',
              TemplateBody=\'string\',
              TemplateURL=\'string\',
              Parameters=[
                  {
                      \'ParameterKey\': \'string\',
                      \'ParameterValue\': \'string\',
                      \'UsePreviousValue\': True|False,
                      \'ResolvedValue\': \'string\'
                  },
              ],
              DisableRollback=True|False,
              RollbackConfiguration={
                  \'RollbackTriggers\': [
                      {
                          \'Arn\': \'string\',
                          \'Type\': \'string\'
                      },
                  ],
                  \'MonitoringTimeInMinutes\': 123
              },
              TimeoutInMinutes=123,
              NotificationARNs=[
                  \'string\',
              ],
              Capabilities=[
                  \'CAPABILITY_IAM\'|\'CAPABILITY_NAMED_IAM\',
              ],
              ResourceTypes=[
                  \'string\',
              ],
              RoleARN=\'string\',
              OnFailure=\'DO_NOTHING\'|\'ROLLBACK\'|\'DELETE\',
              StackPolicyBody=\'string\',
              StackPolicyURL=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              ClientRequestToken=\'string\',
              EnableTerminationProtection=True|False
          )
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name that is associated with the stack. The name must be unique in the region in which you are creating the stack.
        
          .. note::
        
            A stack name can contain only alphanumeric characters (case sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.
        
        :type TemplateBody: string
        :param TemplateBody: 
        
          Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, go to `Template Anatomy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`__ in the AWS CloudFormation User Guide.
        
          Conditional: You must specify either the ``TemplateBody`` or the ``TemplateURL`` parameter, but not both.
        
        :type TemplateURL: string
        :param TemplateURL: 
        
          Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket. For more information, go to the `Template Anatomy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`__ in the AWS CloudFormation User Guide.
        
          Conditional: You must specify either the ``TemplateBody`` or the ``TemplateURL`` parameter, but not both.
        
        :type Parameters: list
        :param Parameters: 
        
          A list of ``Parameter`` structures that specify input parameters for the stack. For more information, see the `Parameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html>`__ data type.
        
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
        
        :type DisableRollback: boolean
        :param DisableRollback: 
        
          Set to ``true`` to disable rollback of the stack if stack creation failed. You can specify either ``DisableRollback`` or ``OnFailure`` , but not both.
        
          Default: ``false``  
        
        :type RollbackConfiguration: dict
        :param RollbackConfiguration: 
        
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
        
              - **Arn** *(string) --* **[REQUIRED]** 
        
                The Amazon Resource Name (ARN) of the rollback trigger.
        
                If a specified trigger is missing, the entire stack operation fails and is rolled back. 
        
              - **Type** *(string) --* **[REQUIRED]** 
        
                The resource type of the rollback trigger. Currently, `AWS\:\:CloudWatch\:\:Alarm <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__ is the only supported resource type.
        
          - **MonitoringTimeInMinutes** *(integer) --* 
        
            The amount of time, in minutes, during which CloudFormation should monitor all the rollback triggers after the stack creation or update operation deploys all necessary resources.
        
            The default is 0 minutes.
        
            If you specify a monitoring period but do not specify any rollback triggers, CloudFormation still waits the specified period of time before cleaning up old resources after update operations. You can use this monitoring period to perform any manual stack validation desired, and manually cancel the stack creation or update (using `CancelUpdateStack <http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__ , for example) as necessary.
        
            If you specify 0 for this parameter, CloudFormation still monitors the specified rollback triggers during stack creation and update operations. Then, for update operations, it begins disposing of old resources immediately once the operation completes.
        
        :type TimeoutInMinutes: integer
        :param TimeoutInMinutes: 
        
          The amount of time that can pass before the stack status becomes CREATE_FAILED; if ``DisableRollback`` is not set or is set to ``false`` , the stack will be rolled back.
        
        :type NotificationARNs: list
        :param NotificationARNs: 
        
          The Simple Notification Service (SNS) topic ARNs to publish stack related events. You can find your SNS topic ARNs using the SNS console or your Command Line Interface (CLI).
        
          - *(string) --* 
        
        :type Capabilities: list
        :param Capabilities: 
        
          A list of values that you must specify before AWS CloudFormation can create certain stacks. Some stack templates might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge their capabilities by specifying this parameter.
        
          The only valid values are ``CAPABILITY_IAM`` and ``CAPABILITY_NAMED_IAM`` . The following resources require you to specify this parameter: `AWS\:\:IAM\:\:AccessKey <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html>`__ , `AWS\:\:IAM\:\:Group <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html>`__ , `AWS\:\:IAM\:\:InstanceProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html>`__ , `AWS\:\:IAM\:\:Policy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html>`__ , `AWS\:\:IAM\:\:Role <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html>`__ , `AWS\:\:IAM\:\:User <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html>`__ , and `AWS\:\:IAM\:\:UserToGroupAddition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html>`__ . If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.
        
          If you have IAM resources, you can specify either capability. If you have IAM resources with custom names, you must specify ``CAPABILITY_NAMED_IAM`` . If you don\'t specify this parameter, this action returns an ``InsufficientCapabilities`` error.
        
          For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities>`__ .
        
          - *(string) --* 
        
        :type ResourceTypes: list
        :param ResourceTypes: 
        
          The template resource types that you have permissions to work with for this create stack action, such as ``AWS::EC2::Instance`` , ``AWS::EC2::*`` , or ``Custom::MyCustomInstance`` . Use the following syntax to describe template resource types: ``AWS::*`` (for all AWS resource), ``Custom::*`` (for all custom resources), ``Custom::*logical_ID* `` (for a specific custom resource), ``AWS::*service_name* ::*`` (for all resources of a particular AWS service), and ``AWS::*service_name* ::*resource_logical_ID* `` (for a specific AWS resource).
        
          If the list of resource types doesn\'t include a resource that you\'re creating, the stack creation fails. By default, AWS CloudFormation grants permissions to all resource types. AWS Identity and Access Management (IAM) uses this parameter for AWS CloudFormation-specific condition keys in IAM policies. For more information, see `Controlling Access with AWS Identity and Access Management <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html>`__ .
        
          - *(string) --* 
        
        :type RoleARN: string
        :param RoleARN: 
        
          The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes to create the stack. AWS CloudFormation uses the role\'s credentials to make calls on your behalf. AWS CloudFormation always uses this role for all future operations on the stack. As long as users have permission to operate on the stack, AWS CloudFormation uses this role even if the users don\'t have permission to pass it. Ensure that the role grants least privilege.
        
          If you don\'t specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
        
        :type OnFailure: string
        :param OnFailure: 
        
          Determines what action will be taken if stack creation fails. This must be one of: DO_NOTHING, ROLLBACK, or DELETE. You can specify either ``OnFailure`` or ``DisableRollback`` , but not both.
        
          Default: ``ROLLBACK``  
        
        :type StackPolicyBody: string
        :param StackPolicyBody: 
        
          Structure containing the stack policy body. For more information, go to `Prevent Updates to Stack Resources <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html>`__ in the *AWS CloudFormation User Guide* . You can specify either the ``StackPolicyBody`` or the ``StackPolicyURL`` parameter, but not both.
        
        :type StackPolicyURL: string
        :param StackPolicyURL: 
        
          Location of a file containing the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an S3 bucket in the same region as the stack. You can specify either the ``StackPolicyBody`` or the ``StackPolicyURL`` parameter, but not both.
        
        :type Tags: list
        :param Tags: 
        
          Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to the resources created in the stack. A maximum number of 50 tags can be specified.
        
          - *(dict) --* 
        
            The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
               *Required* . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .
        
            - **Value** *(string) --* **[REQUIRED]** 
        
               *Required* . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          A unique identifier for this ``CreateStack`` request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you\'re not attempting to create a stack with the same name. You might retry ``CreateStack`` requests to ensure that AWS CloudFormation successfully received them.
        
          All events triggered by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a ``CreateStack`` operation with the token ``token1`` , then all the ``StackEvents`` generated by that operation will have ``ClientRequestToken`` set as ``token1`` .
        
          In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format *Console-StackOperation-ID* , which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: ``Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002`` . 
        
        :type EnableTerminationProtection: boolean
        :param EnableTerminationProtection: 
        
          Whether to enable termination protection on the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see `Protecting a Stack From Being Deleted <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html>`__ in the *AWS CloudFormation User Guide* . Termination protection is disabled on stacks by default. 
        
          For `nested stacks <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__ , termination protection is set on the root stack and cannot be changed directly on the nested stack.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StackId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for a  CreateStack action.
        
            - **StackId** *(string) --* 
        
              Unique identifier of the stack.
        
        """
        pass

    def create_stack_instances(self, StackSetName: str, Accounts: List, Regions: List, ParameterOverrides: List = None, OperationPreferences: Dict = None, OperationId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateStackInstances>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_stack_instances(
              StackSetName=\'string\',
              Accounts=[
                  \'string\',
              ],
              Regions=[
                  \'string\',
              ],
              ParameterOverrides=[
                  {
                      \'ParameterKey\': \'string\',
                      \'ParameterValue\': \'string\',
                      \'UsePreviousValue\': True|False,
                      \'ResolvedValue\': \'string\'
                  },
              ],
              OperationPreferences={
                  \'RegionOrder\': [
                      \'string\',
                  ],
                  \'FailureToleranceCount\': 123,
                  \'FailureTolerancePercentage\': 123,
                  \'MaxConcurrentCount\': 123,
                  \'MaxConcurrentPercentage\': 123
              },
              OperationId=\'string\'
          )
        :type StackSetName: string
        :param StackSetName: **[REQUIRED]** 
        
          The name or unique ID of the stack set that you want to create stack instances from.
        
        :type Accounts: list
        :param Accounts: **[REQUIRED]** 
        
          The names of one or more AWS accounts that you want to create stack instances in the specified region(s) for.
        
          - *(string) --* 
        
        :type Regions: list
        :param Regions: **[REQUIRED]** 
        
          The names of one or more regions where you want to create stack instances using the specified AWS account(s). 
        
          - *(string) --* 
        
        :type ParameterOverrides: list
        :param ParameterOverrides: 
        
          A list of stack set parameters whose values you want to override in the selected stack instances.
        
          Any overridden parameter values will be applied to all stack instances in the specified accounts and regions. When specifying parameters and their values, be aware of how AWS CloudFormation sets parameter values during stack instance operations:
        
          * To override the current value for a parameter, include the parameter and specify its value. 
           
          * To leave a parameter set to its present value, you can do one of the following: 
        
            * Do not include the parameter in the list. 
             
            * Include the parameter and specify ``UsePreviousValue`` as ``true`` . (You cannot specify both a value and set ``UsePreviousValue`` to ``true`` .) 
             
          * To set all overridden parameter back to the values specified in the stack set, specify a parameter list but do not include any parameters. 
           
          * To leave all parameters set to their present values, do not specify this property at all. 
           
          During stack set updates, any parameter values overridden for a stack instance are not updated, but retain their overridden value.
        
          You can only override the parameter *values* that are specified in the stack set; to add or delete a parameter itself, use `UpdateStackSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html>`__ to update the stack set template.
        
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
        
        :type OperationPreferences: dict
        :param OperationPreferences: 
        
          Preferences for how AWS CloudFormation performs this stack set operation.
        
          - **RegionOrder** *(list) --* 
        
            The order of the regions in where you want to perform the stack operation.
        
            - *(string) --* 
        
          - **FailureToleranceCount** *(integer) --* 
        
            The number of accounts, per region, for which this operation can fail before AWS CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation doesn\'t attempt the operation in any subsequent regions.
        
            Conditional: You must specify either ``FailureToleranceCount`` or ``FailureTolerancePercentage`` (but not both).
        
          - **FailureTolerancePercentage** *(integer) --* 
        
            The percentage of accounts, per region, for which this stack operation can fail before AWS CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation doesn\'t attempt the operation in any subsequent regions.
        
            When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds *down* to the next whole number.
        
            Conditional: You must specify either ``FailureToleranceCount`` or ``FailureTolerancePercentage`` , but not both.
        
          - **MaxConcurrentCount** *(integer) --* 
        
            The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of ``FailureToleranceCount`` —``MaxConcurrentCount`` is at most one more than the ``FailureToleranceCount`` .
        
            Note that this setting lets you specify the *maximum* for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
        
            Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` , but not both.
        
          - **MaxConcurrentPercentage** *(integer) --* 
        
            The maximum percentage of accounts in which to perform this operation at one time.
        
            When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.
        
            Note that this setting lets you specify the *maximum* for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
        
            Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` , but not both.
        
        :type OperationId: string
        :param OperationId: 
        
          The unique identifier for this stack set operation. 
        
          The operation ID also functions as an idempotency token, to ensure that AWS CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that AWS CloudFormation successfully received them.
        
          If you don\'t specify an operation ID, the SDK generates one automatically. 
        
          Repeating this stack set operation with a new operation ID retries all stack instances whose status is ``OUTDATED`` . 
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **OperationId** *(string) --* 
        
              The unique identifier for this stack set operation.
        
        """
        pass

    def create_stack_set(self, StackSetName: str, Description: str = None, TemplateBody: str = None, TemplateURL: str = None, Parameters: List = None, Capabilities: List = None, Tags: List = None, AdministrationRoleARN: str = None, ExecutionRoleName: str = None, ClientRequestToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateStackSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_stack_set(
              StackSetName=\'string\',
              Description=\'string\',
              TemplateBody=\'string\',
              TemplateURL=\'string\',
              Parameters=[
                  {
                      \'ParameterKey\': \'string\',
                      \'ParameterValue\': \'string\',
                      \'UsePreviousValue\': True|False,
                      \'ResolvedValue\': \'string\'
                  },
              ],
              Capabilities=[
                  \'CAPABILITY_IAM\'|\'CAPABILITY_NAMED_IAM\',
              ],
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              AdministrationRoleARN=\'string\',
              ExecutionRoleName=\'string\',
              ClientRequestToken=\'string\'
          )
        :type StackSetName: string
        :param StackSetName: **[REQUIRED]** 
        
          The name to associate with the stack set. The name must be unique in the region where you create your stack set.
        
          .. note::
        
            A stack name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and can\'t be longer than 128 characters.
        
        :type Description: string
        :param Description: 
        
          A description of the stack set. You can use the description to identify the stack set\'s purpose or other important information.
        
        :type TemplateBody: string
        :param TemplateBody: 
        
          The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, see `Template Anatomy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`__ in the AWS CloudFormation User Guide.
        
          Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.
        
        :type TemplateURL: string
        :param TemplateURL: 
        
          The location of the file that contains the template body. The URL must point to a template (maximum size: 460,800 bytes) that\'s located in an Amazon S3 bucket. For more information, see `Template Anatomy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`__ in the AWS CloudFormation User Guide.
        
          Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.
        
        :type Parameters: list
        :param Parameters: 
        
          The input parameters for the stack set template. 
        
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
        
        :type Capabilities: list
        :param Capabilities: 
        
          A list of values that you must specify before AWS CloudFormation can create certain stack sets. Some stack set templates might include resources that can affect permissions in your AWS account—for example, by creating new AWS Identity and Access Management (IAM) users. For those stack sets, you must explicitly acknowledge their capabilities by specifying this parameter.
        
          The only valid values are CAPABILITY_IAM and CAPABILITY_NAMED_IAM. The following resources require you to specify this parameter: 
        
          * AWS::IAM::AccessKey 
           
          * AWS::IAM::Group 
           
          * AWS::IAM::InstanceProfile 
           
          * AWS::IAM::Policy 
           
          * AWS::IAM::Role 
           
          * AWS::IAM::User 
           
          * AWS::IAM::UserToGroupAddition 
           
          If your stack template contains these resources, we recommend that you review all permissions that are associated with them and edit their permissions if necessary.
        
          If you have IAM resources, you can specify either capability. If you have IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM. If you don\'t specify this parameter, this action returns an ``InsufficientCapabilities`` error.
        
          For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates. <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities>`__  
        
          - *(string) --* 
        
        :type Tags: list
        :param Tags: 
        
          The key-value pairs to associate with this stack set and the stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.
        
          If you specify tags as part of a ``CreateStackSet`` action, AWS CloudFormation checks to see if you have the required IAM permission to tag resources. If you don\'t, the entire ``CreateStackSet`` action fails with an ``access denied`` error, and the stack set is not created.
        
          - *(dict) --* 
        
            The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
               *Required* . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .
        
            - **Value** *(string) --* **[REQUIRED]** 
        
               *Required* . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
        
        :type AdministrationRoleARN: string
        :param AdministrationRoleARN: 
        
          The Amazon Resource Number (ARN) of the IAM role to use to create this stack set. 
        
          Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see `Prerequisites\: Granting Permissions for Stack Set Operations <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html>`__ in the *AWS CloudFormation User Guide* .
        
        :type ExecutionRoleName: string
        :param ExecutionRoleName: 
        
          The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, AWS CloudFormation uses the ``AWSCloudFormationStackSetExecutionRole`` role for the stack set operation.
        
          Specify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their stack sets. 
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          A unique identifier for this ``CreateStackSet`` request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you\'re not attempting to create another stack set with the same name. You might retry ``CreateStackSet`` requests to ensure that AWS CloudFormation successfully received them.
        
          If you don\'t specify an operation ID, the SDK generates one automatically. 
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StackSetId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **StackSetId** *(string) --* 
        
              The ID of the stack set that you\'re creating.
        
        """
        pass

    def delete_change_set(self, ChangeSetName: str, StackName: str = None) -> Dict:
        """
        
        If the call successfully completes, AWS CloudFormation successfully deleted the change set.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DeleteChangeSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_change_set(
              ChangeSetName=\'string\',
              StackName=\'string\'
          )
        :type ChangeSetName: string
        :param ChangeSetName: **[REQUIRED]** 
        
          The name or Amazon Resource Name (ARN) of the change set that you want to delete.
        
        :type StackName: string
        :param StackName: 
        
          If you specified the name of a change set to delete, specify the stack name or ID (ARN) that is associated with it.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for the  DeleteChangeSet action.
        
        """
        pass

    def delete_stack(self, StackName: str, RetainResources: List = None, RoleARN: str = None, ClientRequestToken: str = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DeleteStack>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_stack(
              StackName=\'string\',
              RetainResources=[
                  \'string\',
              ],
              RoleARN=\'string\',
              ClientRequestToken=\'string\'
          )
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name or the unique stack ID that is associated with the stack.
        
        :type RetainResources: list
        :param RetainResources: 
        
          For stacks in the ``DELETE_FAILED`` state, a list of resource logical IDs that are associated with the resources you want to retain. During deletion, AWS CloudFormation deletes the stack but does not delete the retained resources.
        
          Retaining resources is useful when you cannot delete a resource, such as a non-empty S3 bucket, but you want to delete the stack.
        
          - *(string) --* 
        
        :type RoleARN: string
        :param RoleARN: 
        
          The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes to delete the stack. AWS CloudFormation uses the role\'s credentials to make calls on your behalf.
        
          If you don\'t specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          A unique identifier for this ``DeleteStack`` request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you\'re not attempting to delete a stack with the same name. You might retry ``DeleteStack`` requests to ensure that AWS CloudFormation successfully received them.
        
          All events triggered by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a ``CreateStack`` operation with the token ``token1`` , then all the ``StackEvents`` generated by that operation will have ``ClientRequestToken`` set as ``token1`` .
        
          In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format *Console-StackOperation-ID* , which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: ``Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002`` . 
        
        :returns: None
        """
        pass

    def delete_stack_instances(self, StackSetName: str, Accounts: List, Regions: List, RetainStacks: bool, OperationPreferences: Dict = None, OperationId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DeleteStackInstances>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_stack_instances(
              StackSetName=\'string\',
              Accounts=[
                  \'string\',
              ],
              Regions=[
                  \'string\',
              ],
              OperationPreferences={
                  \'RegionOrder\': [
                      \'string\',
                  ],
                  \'FailureToleranceCount\': 123,
                  \'FailureTolerancePercentage\': 123,
                  \'MaxConcurrentCount\': 123,
                  \'MaxConcurrentPercentage\': 123
              },
              RetainStacks=True|False,
              OperationId=\'string\'
          )
        :type StackSetName: string
        :param StackSetName: **[REQUIRED]** 
        
          The name or unique ID of the stack set that you want to delete stack instances for.
        
        :type Accounts: list
        :param Accounts: **[REQUIRED]** 
        
          The names of the AWS accounts that you want to delete stack instances for.
        
          - *(string) --* 
        
        :type Regions: list
        :param Regions: **[REQUIRED]** 
        
          The regions where you want to delete stack set instances. 
        
          - *(string) --* 
        
        :type OperationPreferences: dict
        :param OperationPreferences: 
        
          Preferences for how AWS CloudFormation performs this stack set operation.
        
          - **RegionOrder** *(list) --* 
        
            The order of the regions in where you want to perform the stack operation.
        
            - *(string) --* 
        
          - **FailureToleranceCount** *(integer) --* 
        
            The number of accounts, per region, for which this operation can fail before AWS CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation doesn\'t attempt the operation in any subsequent regions.
        
            Conditional: You must specify either ``FailureToleranceCount`` or ``FailureTolerancePercentage`` (but not both).
        
          - **FailureTolerancePercentage** *(integer) --* 
        
            The percentage of accounts, per region, for which this stack operation can fail before AWS CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation doesn\'t attempt the operation in any subsequent regions.
        
            When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds *down* to the next whole number.
        
            Conditional: You must specify either ``FailureToleranceCount`` or ``FailureTolerancePercentage`` , but not both.
        
          - **MaxConcurrentCount** *(integer) --* 
        
            The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of ``FailureToleranceCount`` —``MaxConcurrentCount`` is at most one more than the ``FailureToleranceCount`` .
        
            Note that this setting lets you specify the *maximum* for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
        
            Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` , but not both.
        
          - **MaxConcurrentPercentage** *(integer) --* 
        
            The maximum percentage of accounts in which to perform this operation at one time.
        
            When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.
        
            Note that this setting lets you specify the *maximum* for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
        
            Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` , but not both.
        
        :type RetainStacks: boolean
        :param RetainStacks: **[REQUIRED]** 
        
          Removes the stack instances from the specified stack set, but doesn\'t delete the stacks. You can\'t reassociate a retained stack or add an existing, saved stack to a new stack set.
        
          For more information, see `Stack set operation options <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options>`__ .
        
        :type OperationId: string
        :param OperationId: 
        
          The unique identifier for this stack set operation. 
        
          If you don\'t specify an operation ID, the SDK generates one automatically. 
        
          The operation ID also functions as an idempotency token, to ensure that AWS CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You can retry stack set operation requests to ensure that AWS CloudFormation successfully received them.
        
          Repeating this stack set operation with a new operation ID retries all stack instances whose status is ``OUTDATED`` . 
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **OperationId** *(string) --* 
        
              The unique identifier for this stack set operation.
        
        """
        pass

    def delete_stack_set(self, StackSetName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DeleteStackSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_stack_set(
              StackSetName=\'string\'
          )
        :type StackSetName: string
        :param StackSetName: **[REQUIRED]** 
        
          The name or unique ID of the stack set that you\'re deleting. You can obtain this value by running  ListStackSets .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def describe_account_limits(self, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeAccountLimits>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_account_limits(
              NextToken=\'string\'
          )
        :type NextToken: string
        :param NextToken: 
        
          A string that identifies the next page of limits that you want to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AccountLimits\': [
                    {
                        \'Name\': \'string\',
                        \'Value\': 123
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for the  DescribeAccountLimits action.
        
            - **AccountLimits** *(list) --* 
        
              An account limit structure that contain a list of AWS CloudFormation account limits and their values.
        
              - *(dict) --* 
        
                The AccountLimit data type.
        
                - **Name** *(string) --* 
        
                  The name of the account limit. Currently, the only account limit is ``StackLimit`` .
        
                - **Value** *(integer) --* 
        
                  The value that is associated with the account limit name.
        
            - **NextToken** *(string) --* 
        
              If the output exceeds 1 MB in size, a string that identifies the next page of limits. If no additional page exists, this value is null.
        
        """
        pass

    def describe_change_set(self, ChangeSetName: str, StackName: str = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeChangeSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_change_set(
              ChangeSetName=\'string\',
              StackName=\'string\',
              NextToken=\'string\'
          )
        :type ChangeSetName: string
        :param ChangeSetName: **[REQUIRED]** 
        
          The name or Amazon Resource Name (ARN) of the change set that you want to describe.
        
        :type StackName: string
        :param StackName: 
        
          If you specified the name of a change set, specify the stack name or ID (ARN) of the change set you want to describe.
        
        :type NextToken: string
        :param NextToken: 
        
          A string (provided by the  DescribeChangeSet response output) that identifies the next page of information that you want to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ChangeSetName\': \'string\',
                \'ChangeSetId\': \'string\',
                \'StackId\': \'string\',
                \'StackName\': \'string\',
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
                \'ExecutionStatus\': \'UNAVAILABLE\'|\'AVAILABLE\'|\'EXECUTE_IN_PROGRESS\'|\'EXECUTE_COMPLETE\'|\'EXECUTE_FAILED\'|\'OBSOLETE\',
                \'Status\': \'CREATE_PENDING\'|\'CREATE_IN_PROGRESS\'|\'CREATE_COMPLETE\'|\'DELETE_COMPLETE\'|\'FAILED\',
                \'StatusReason\': \'string\',
                \'NotificationARNs\': [
                    \'string\',
                ],
                \'RollbackConfiguration\': {
                    \'RollbackTriggers\': [
                        {
                            \'Arn\': \'string\',
                            \'Type\': \'string\'
                        },
                    ],
                    \'MonitoringTimeInMinutes\': 123
                },
                \'Capabilities\': [
                    \'CAPABILITY_IAM\'|\'CAPABILITY_NAMED_IAM\',
                ],
                \'Tags\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ],
                \'Changes\': [
                    {
                        \'Type\': \'Resource\',
                        \'ResourceChange\': {
                            \'Action\': \'Add\'|\'Modify\'|\'Remove\',
                            \'LogicalResourceId\': \'string\',
                            \'PhysicalResourceId\': \'string\',
                            \'ResourceType\': \'string\',
                            \'Replacement\': \'True\'|\'False\'|\'Conditional\',
                            \'Scope\': [
                                \'Properties\'|\'Metadata\'|\'CreationPolicy\'|\'UpdatePolicy\'|\'DeletionPolicy\'|\'Tags\',
                            ],
                            \'Details\': [
                                {
                                    \'Target\': {
                                        \'Attribute\': \'Properties\'|\'Metadata\'|\'CreationPolicy\'|\'UpdatePolicy\'|\'DeletionPolicy\'|\'Tags\',
                                        \'Name\': \'string\',
                                        \'RequiresRecreation\': \'Never\'|\'Conditionally\'|\'Always\'
                                    },
                                    \'Evaluation\': \'Static\'|\'Dynamic\',
                                    \'ChangeSource\': \'ResourceReference\'|\'ParameterReference\'|\'ResourceAttribute\'|\'DirectModification\'|\'Automatic\',
                                    \'CausingEntity\': \'string\'
                                },
                            ]
                        }
                    },
                ],
                \'NextToken\': \'string\'
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
        
              A list of ``Parameter`` structures that describes the input parameters and their values used to create the change set. For more information, see the `Parameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html>`__ data type.
        
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
        
              The start time when the change set was created, in UTC.
        
            - **ExecutionStatus** *(string) --* 
        
              If the change set execution status is ``AVAILABLE`` , you can execute the change set. If you can’t execute the change set, the status indicates why. For example, a change set might be in an ``UNAVAILABLE`` state because AWS CloudFormation is still creating it or in an ``OBSOLETE`` state because the stack was already updated.
        
            - **Status** *(string) --* 
        
              The current status of the change set, such as ``CREATE_IN_PROGRESS`` , ``CREATE_COMPLETE`` , or ``FAILED`` .
        
            - **StatusReason** *(string) --* 
        
              A description of the change set\'s status. For example, if your attempt to create a change set failed, AWS CloudFormation shows the error message.
        
            - **NotificationARNs** *(list) --* 
        
              The ARNs of the Amazon Simple Notification Service (Amazon SNS) topics that will be associated with the stack if you execute the change set.
        
              - *(string) --* 
          
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
        
                    The resource\'s logical ID, which is defined in the stack\'s template.
        
                  - **PhysicalResourceId** *(string) --* 
        
                    The resource\'s physical ID (resource name). Resources that you are adding don\'t have physical IDs because they haven\'t been created.
        
                  - **ResourceType** *(string) --* 
        
                    The type of AWS CloudFormation resource, such as ``AWS::S3::Bucket`` .
        
                  - **Replacement** *(string) --* 
        
                    For the ``Modify`` action, indicates whether AWS CloudFormation will replace the resource by creating a new one and deleting the old one. This value depends on the value of the ``RequiresRecreation`` property in the ``ResourceTargetDefinition`` structure. For example, if the ``RequiresRecreation`` field is ``Always`` and the ``Evaluation`` field is ``Static`` , ``Replacement`` is ``True`` . If the ``RequiresRecreation`` field is ``Always`` and the ``Evaluation`` field is ``Dynamic`` , ``Replacement`` is ``Conditionally`` .
        
                    If you have multiple changes with different ``RequiresRecreation`` values, the ``Replacement`` value depends on the change with the most impact. A ``RequiresRecreation`` value of ``Always`` has the most impact, followed by ``Conditionally`` , and then ``Never`` .
        
                  - **Scope** *(list) --* 
        
                    For the ``Modify`` action, indicates which resource attribute is triggering this update, such as a change in the resource attribute\'s ``Metadata`` , ``Properties`` , or ``Tags`` .
        
                    - *(string) --* 
                
                  - **Details** *(list) --* 
        
                    For the ``Modify`` action, a list of ``ResourceChangeDetail`` structures that describes the changes that AWS CloudFormation will make to the resource. 
        
                    - *(dict) --* 
        
                      For a resource with ``Modify`` as the action, the ``ResourceChange`` structure describes the changes AWS CloudFormation will make to that resource.
        
                      - **Target** *(dict) --* 
        
                        A ``ResourceTargetDefinition`` structure that describes the field that AWS CloudFormation will change and whether the resource will be recreated.
        
                        - **Attribute** *(string) --* 
        
                          Indicates which resource attribute is triggering this update, such as a change in the resource attribute\'s ``Metadata`` , ``Properties`` , or ``Tags`` .
        
                        - **Name** *(string) --* 
        
                          If the ``Attribute`` value is ``Properties`` , the name of the property. For all other attributes, the value is null.
        
                        - **RequiresRecreation** *(string) --* 
        
                          If the ``Attribute`` value is ``Properties`` , indicates whether a change to this property causes the resource to be recreated. The value can be ``Never`` , ``Always`` , or ``Conditionally`` . To determine the conditions for a ``Conditionally`` recreation, see the update behavior for that `property <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ in the AWS CloudFormation User Guide.
        
                      - **Evaluation** *(string) --* 
        
                        Indicates whether AWS CloudFormation can determine the target value, and whether the target value will change before you execute a change set.
        
                        For ``Static`` evaluations, AWS CloudFormation can determine that the target value will change, and its value. For example, if you directly modify the ``InstanceType`` property of an EC2 instance, AWS CloudFormation knows that this property value will change, and its value, so this is a ``Static`` evaluation.
        
                        For ``Dynamic`` evaluations, cannot determine the target value because it depends on the result of an intrinsic function, such as a ``Ref`` or ``Fn::GetAtt`` intrinsic function, when the stack is updated. For example, if your template includes a reference to a resource that is conditionally recreated, the value of the reference (the physical ID of the resource) might change, depending on if the resource is recreated. If the resource is recreated, it will have a new physical ID, so all references to that resource will also be updated.
        
                      - **ChangeSource** *(string) --* 
        
                        The group to which the ``CausingEntity`` value belongs. There are five entity groups:
        
                        * ``ResourceReference`` entities are ``Ref`` intrinsic functions that refer to resources in the template, such as ``{ \"Ref\" : \"MyEC2InstanceResource\" }`` . 
                         
                        * ``ParameterReference`` entities are ``Ref`` intrinsic functions that get template parameter values, such as ``{ \"Ref\" : \"MyPasswordParameter\" }`` . 
                         
                        * ``ResourceAttribute`` entities are ``Fn::GetAtt`` intrinsic functions that get resource attribute values, such as ``{ \"Fn::GetAtt\" : [ \"MyEC2InstanceResource\", \"PublicDnsName\" ] }`` . 
                         
                        * ``DirectModification`` entities are changes that are made directly to the template. 
                         
                        * ``Automatic`` entities are ``AWS::CloudFormation::Stack`` resource types, which are also known as nested stacks. If you made no changes to the ``AWS::CloudFormation::Stack`` resource, AWS CloudFormation sets the ``ChangeSource`` to ``Automatic`` because the nested stack\'s template might have changed. Changes to a nested stack\'s template aren\'t visible to AWS CloudFormation until you run an update on the parent stack. 
                         
                      - **CausingEntity** *(string) --* 
        
                        The identity of the entity that triggered this change. This entity is a member of the group that is specified by the ``ChangeSource`` field. For example, if you modified the value of the ``KeyPairName`` parameter, the ``CausingEntity`` is the name of the parameter (``KeyPairName`` ).
        
                        If the ``ChangeSource`` value is ``DirectModification`` , no value is given for ``CausingEntity`` .
        
            - **NextToken** *(string) --* 
        
              If the output exceeds 1 MB, a string that identifies the next page of changes. If there is no additional page, this value is null.
        
        """
        pass

    def describe_stack_drift_detection_status(self, StackDriftDetectionId: str) -> Dict:
        """
        
        Use  DetectStackDrift to initiate a stack drift detection operation. ``DetectStackDrift`` returns a ``StackDriftDetectionId`` you can use to monitor the progress of the operation using ``DescribeStackDriftDetectionStatus`` . Once the drift detection operation has completed, use  DescribeStackResourceDrifts to return drift information about the stack and its resources.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_stack_drift_detection_status(
              StackDriftDetectionId=\'string\'
          )
        :type StackDriftDetectionId: string
        :param StackDriftDetectionId: **[REQUIRED]** 
        
          The ID of the drift detection results of this operation. 
        
          AWS CloudFormation generates new results, with a new drift detection ID, each time this operation is run. However, the number of drift results AWS CloudFormation retains for any given stack, and for how long, may vary. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StackId\': \'string\',
                \'StackDriftDetectionId\': \'string\',
                \'StackDriftStatus\': \'DRIFTED\'|\'IN_SYNC\'|\'UNKNOWN\'|\'NOT_CHECKED\',
                \'DetectionStatus\': \'DETECTION_IN_PROGRESS\'|\'DETECTION_FAILED\'|\'DETECTION_COMPLETE\',
                \'DetectionStatusReason\': \'string\',
                \'DriftedStackResourceCount\': 123,
                \'Timestamp\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **StackId** *(string) --* 
        
              The ID of the stack.
        
            - **StackDriftDetectionId** *(string) --* 
        
              The ID of the drift detection results of this operation. 
        
              AWS CloudFormation generates new results, with a new drift detection ID, each time this operation is run. However, the number of reports AWS CloudFormation retains for any given stack, and for how long, may vary.
        
            - **StackDriftStatus** *(string) --* 
        
              Status of the stack\'s actual configuration compared to its expected configuration. 
        
              * ``DRIFTED`` : The stack differs from its expected template configuration. A stack is considered to have drifted if one or more of its resources have drifted. 
               
              * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the stack differs from its expected template configuration. 
               
              * ``IN_SYNC`` : The stack\'s actual configuration matches its expected template configuration. 
               
              * ``UNKNOWN`` : This value is reserved for future use. 
               
            - **DetectionStatus** *(string) --* 
        
              The status of the stack drift detection operation.
        
              * ``DETECTION_COMPLETE`` : The stack drift detection operation has successfully completed for all resources in the stack that support drift detection. (Resources that do not currently support stack detection remain unchecked.) If you specified logical resource IDs for AWS CloudFormation to use as a filter for the stack drift detection operation, only the resources with those logical IDs are checked for drift. 
               
              * ``DETECTION_FAILED`` : The stack drift detection operation has failed for at least one resource in the stack. Results will be available for resources on which AWS CloudFormation successfully completed drift detection. 
               
              * ``DETECTION_IN_PROGRESS`` : The stack drift detection operation is currently in progress. 
               
            - **DetectionStatusReason** *(string) --* 
        
              The reason the stack drift detection operation has its current status.
        
            - **DriftedStackResourceCount** *(integer) --* 
        
              Total number of stack resources that have drifted. This is NULL until the drift detection operation reaches a status of ``DETECTION_COMPLETE`` . This value will be 0 for stacks whose drift status is ``IN_SYNC`` .
        
            - **Timestamp** *(datetime) --* 
        
              Time at which the stack drift detection operation was initiated.
        
        """
        pass

    def describe_stack_events(self, StackName: str = None, NextToken: str = None) -> Dict:
        """
        
        .. note::
        
          You can list events for stacks that have failed to create or have been deleted by specifying the unique stack identifier (stack ID).
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStackEvents>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_stack_events(
              StackName=\'string\',
              NextToken=\'string\'
          )
        :type StackName: string
        :param StackName: 
        
          The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
        
          * Running stacks: You can specify either the stack\'s name or its unique stack ID. 
           
          * Deleted stacks: You must specify the unique stack ID. 
           
          Default: There is no default value.
        
        :type NextToken: string
        :param NextToken: 
        
          A string that identifies the next page of events that you want to retrieve.
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              If the output exceeds 1 MB in size, a string that identifies the next page of events. If no additional page exists, this value is null.
        
        """
        pass

    def describe_stack_instance(self, StackSetName: str, StackInstanceAccount: str, StackInstanceRegion: str) -> Dict:
        """
        
        For a list of stack instances that are associated with a specific stack set, use  ListStackInstances .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStackInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_stack_instance(
              StackSetName=\'string\',
              StackInstanceAccount=\'string\',
              StackInstanceRegion=\'string\'
          )
        :type StackSetName: string
        :param StackSetName: **[REQUIRED]** 
        
          The name or the unique stack ID of the stack set that you want to get stack instance information for.
        
        :type StackInstanceAccount: string
        :param StackInstanceAccount: **[REQUIRED]** 
        
          The ID of an AWS account that\'s associated with this stack instance.
        
        :type StackInstanceRegion: string
        :param StackInstanceRegion: **[REQUIRED]** 
        
          The name of a region that\'s associated with this stack instance.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StackInstance\': {
                    \'StackSetId\': \'string\',
                    \'Region\': \'string\',
                    \'Account\': \'string\',
                    \'StackId\': \'string\',
                    \'ParameterOverrides\': [
                        {
                            \'ParameterKey\': \'string\',
                            \'ParameterValue\': \'string\',
                            \'UsePreviousValue\': True|False,
                            \'ResolvedValue\': \'string\'
                        },
                    ],
                    \'Status\': \'CURRENT\'|\'OUTDATED\'|\'INOPERABLE\',
                    \'StatusReason\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **StackInstance** *(dict) --* 
        
              The stack instance that matches the specified request parameters.
        
              - **StackSetId** *(string) --* 
        
                The name or unique ID of the stack set that the stack instance is associated with.
        
              - **Region** *(string) --* 
        
                The name of the AWS region that the stack instance is associated with.
        
              - **Account** *(string) --* 
        
                The name of the AWS account that the stack instance is associated with.
        
              - **StackId** *(string) --* 
        
                The ID of the stack instance.
        
              - **ParameterOverrides** *(list) --* 
        
                A list of parameters from the stack set template whose values have been overridden in this stack instance.
        
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
        
              - **Status** *(string) --* 
        
                The status of the stack instance, in terms of its synchronization with its associated stack set.
        
                * ``INOPERABLE`` : A ``DeleteStackInstances`` operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further ``UpdateStackSet`` operations. You might need to perform a ``DeleteStackInstances`` operation, with ``RetainStacks`` set to ``true`` , to delete the stack instance, and then delete the stack manually. 
                 
                * ``OUTDATED`` : The stack isn\'t currently up to date with the stack set because: 
        
                  * The associated stack failed during a ``CreateStackSet`` or ``UpdateStackSet`` operation.  
                   
                  * The stack was part of a ``CreateStackSet`` or ``UpdateStackSet`` operation that failed or was stopped before the stack was created or updated.  
                   
                * ``CURRENT`` : The stack is currently up to date with the stack set. 
                 
              - **StatusReason** *(string) --* 
        
                The explanation for the specific status code that is assigned to this stack instance.
        
        """
        pass

    def describe_stack_resource(self, StackName: str, LogicalResourceId: str) -> Dict:
        """
        
        For deleted stacks, DescribeStackResource returns resource information for up to 90 days after the stack has been deleted.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStackResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_stack_resource(
              StackName=\'string\',
              LogicalResourceId=\'string\'
          )
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
        
          * Running stacks: You can specify either the stack\'s name or its unique stack ID. 
           
          * Deleted stacks: You must specify the unique stack ID. 
           
          Default: There is no default value.
        
        :type LogicalResourceId: string
        :param LogicalResourceId: **[REQUIRED]** 
        
          The logical name of the resource as specified in the template.
        
          Default: There is no default value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StackResourceDetail\': {
                    \'StackName\': \'string\',
                    \'StackId\': \'string\',
                    \'LogicalResourceId\': \'string\',
                    \'PhysicalResourceId\': \'string\',
                    \'ResourceType\': \'string\',
                    \'LastUpdatedTimestamp\': datetime(2015, 1, 1),
                    \'ResourceStatus\': \'CREATE_IN_PROGRESS\'|\'CREATE_FAILED\'|\'CREATE_COMPLETE\'|\'DELETE_IN_PROGRESS\'|\'DELETE_FAILED\'|\'DELETE_COMPLETE\'|\'DELETE_SKIPPED\'|\'UPDATE_IN_PROGRESS\'|\'UPDATE_FAILED\'|\'UPDATE_COMPLETE\',
                    \'ResourceStatusReason\': \'string\',
                    \'Description\': \'string\',
                    \'Metadata\': \'string\',
                    \'DriftInformation\': {
                        \'StackResourceDriftStatus\': \'IN_SYNC\'|\'MODIFIED\'|\'DELETED\'|\'NOT_CHECKED\',
                        \'LastCheckTimestamp\': datetime(2015, 1, 1)
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for a  DescribeStackResource action.
        
            - **StackResourceDetail** *(dict) --* 
        
              A ``StackResourceDetail`` structure containing the description of the specified resource in the specified stack.
        
              - **StackName** *(string) --* 
        
                The name associated with the stack.
        
              - **StackId** *(string) --* 
        
                Unique identifier of the stack.
        
              - **LogicalResourceId** *(string) --* 
        
                The logical name of the resource specified in the template.
        
              - **PhysicalResourceId** *(string) --* 
        
                The name or unique identifier that corresponds to a physical instance ID of a resource supported by AWS CloudFormation.
        
              - **ResourceType** *(string) --* 
        
                Type of resource. ((For more information, go to `AWS Resource Types Reference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ in the AWS CloudFormation User Guide.)
        
              - **LastUpdatedTimestamp** *(datetime) --* 
        
                Time the status was updated.
        
              - **ResourceStatus** *(string) --* 
        
                Current status of the resource.
        
              - **ResourceStatusReason** *(string) --* 
        
                Success/failure message associated with the resource.
        
              - **Description** *(string) --* 
        
                User defined description associated with the resource.
        
              - **Metadata** *(string) --* 
        
                The content of the ``Metadata`` attribute declared for the resource. For more information, see `Metadata Attribute <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-metadata.html>`__ in the AWS CloudFormation User Guide.
        
              - **DriftInformation** *(dict) --* 
        
                Information about whether the resource\'s actual configuration differs, or has *drifted* , from its expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see `Detecting Unregulated Configuration Changes to Stacks and Resources <http://docs.aws.amazon.com/http:/docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__ .
        
                - **StackResourceDriftStatus** *(string) --* 
        
                  Status of the resource\'s actual configuration compared to its expected configuration
        
                  * ``DELETED`` : The resource differs from its expected configuration in that it has been deleted. 
                   
                  * ``MODIFIED`` : The resource differs from its expected configuration. 
                   
                  * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the resource differs from its expected configuration. Any resources that do not currently support drift detection have a status of ``NOT_CHECKED`` . For more information, see `Resources that Support Drift Detection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__ .  
                   
                  * ``IN_SYNC`` : The resources\'s actual configuration matches its expected configuration. 
                   
                - **LastCheckTimestamp** *(datetime) --* 
        
                  When AWS CloudFormation last checked if the resource had drifted from its expected configuration.
        
        """
        pass

    def describe_stack_resource_drifts(self, StackName: str, StackResourceDriftStatusFilters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        For a given stack, there will be one ``StackResourceDrift`` for each stack resource that has been checked for drift. Resources that have not yet been checked for drift are not included. Resources that do not currently support drift detection are not checked, and so not included. For a list of resources that support drift detection, see `Resources that Support Drift Detection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__ .
        
        Use  DetectStackResourceDrift to detect drift on individual resources, or  DetectStackDrift to detect drift on all supported resources for a given stack.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStackResourceDrifts>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_stack_resource_drifts(
              StackName=\'string\',
              StackResourceDriftStatusFilters=[
                  \'IN_SYNC\'|\'MODIFIED\'|\'DELETED\'|\'NOT_CHECKED\',
              ],
              NextToken=\'string\',
              MaxResults=123
          )
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name of the stack for which you want drift information.
        
        :type StackResourceDriftStatusFilters: list
        :param StackResourceDriftStatusFilters: 
        
          The resource drift status values to use as filters for the resource drift results returned.
        
          * ``DELETED`` : The resource differs from its expected template configuration in that the resource has been deleted. 
           
          * ``MODIFIED`` : One or more resource properties differ from their expected template values. 
           
          * ``IN_SYNC`` : The resources\'s actual configuration matches its expected template configuration. 
           
          * ``NOT_CHECKED`` : AWS CloudFormation does not currently return this value. 
           
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          A string that identifies the next page of stack resource drift results.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a ``NextToken`` value that you can assign to the ``NextToken`` request parameter to get the next set of results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StackResourceDrifts\': [
                    {
                        \'StackId\': \'string\',
                        \'LogicalResourceId\': \'string\',
                        \'PhysicalResourceId\': \'string\',
                        \'PhysicalResourceIdContext\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'ResourceType\': \'string\',
                        \'ExpectedProperties\': \'string\',
                        \'ActualProperties\': \'string\',
                        \'PropertyDifferences\': [
                            {
                                \'PropertyPath\': \'string\',
                                \'ExpectedValue\': \'string\',
                                \'ActualValue\': \'string\',
                                \'DifferenceType\': \'ADD\'|\'REMOVE\'|\'NOT_EQUAL\'
                            },
                        ],
                        \'StackResourceDriftStatus\': \'IN_SYNC\'|\'MODIFIED\'|\'DELETED\'|\'NOT_CHECKED\',
                        \'Timestamp\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **StackResourceDrifts** *(list) --* 
        
              Drift information for the resources that have been checked for drift in the specified stack. This includes actual and expected configuration values for resources where AWS CloudFormation detects drift.
        
              For a given stack, there will be one ``StackResourceDrift`` for each stack resource that has been checked for drift. Resources that have not yet been checked for drift are not included. Resources that do not currently support drift detection are not checked, and so not included. For a list of resources that support drift detection, see `Resources that Support Drift Detection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__ .
        
              - *(dict) --* 
        
                Contains the drift information for a resource that has been checked for drift. This includes actual and expected property values for resources in which AWS CloudFormation has detected drift. Only resource properties explicitly defined in the stack template are checked for drift. For more information, see `Detecting Unregulated Configuration Changes to Stacks and Resources <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__ .
        
                Resources that do not currently support drift detection cannot be checked. For a list of resources that support drift detection, see `Resources that Support Drift Detection <http://docs.aws.amazon.com/http:/docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__ .
        
                Use  DetectStackResourceDrift to detect drift on individual resources, or  DetectStackDrift to detect drift on all resources in a given stack that support drift detection.
        
                - **StackId** *(string) --* 
        
                  The ID of the stack.
        
                - **LogicalResourceId** *(string) --* 
        
                  The logical name of the resource specified in the template.
        
                - **PhysicalResourceId** *(string) --* 
        
                  The name or unique identifier that corresponds to a physical instance ID of a resource supported by AWS CloudFormation. 
        
                - **PhysicalResourceIdContext** *(list) --* 
        
                  Context information that enables AWS CloudFormation to uniquely identify a resource. AWS CloudFormation uses context key-value pairs in cases where a resource\'s logical and physical IDs are not enough to uniquely identify that resource. Each context key-value pair specifies a unique resource that contains the targeted resource.
        
                  - *(dict) --* 
        
                    Context information that enables AWS CloudFormation to uniquely identify a resource. AWS CloudFormation uses context key-value pairs in cases where a resource\'s logical and physical IDs are not enough to uniquely identify that resource. Each context key-value pair specifies a resource that contains the targeted resource.
        
                    - **Key** *(string) --* 
        
                      The resource context key.
        
                    - **Value** *(string) --* 
        
                      The resource context value.
        
                - **ResourceType** *(string) --* 
        
                  The type of the resource.
        
                - **ExpectedProperties** *(string) --* 
        
                  A JSON structure containing the expected property values of the stack resource, as defined in the stack template and any values specified as template parameters. 
        
                  For resources whose ``StackResourceDriftStatus`` is ``DELETED`` , this structure will not be present. 
        
                - **ActualProperties** *(string) --* 
        
                  A JSON structure containing the actual property values of the stack resource.
        
                  For resources whose ``StackResourceDriftStatus`` is ``DELETED`` , this structure will not be present. 
        
                - **PropertyDifferences** *(list) --* 
        
                  A collection of the resource properties whose actual values differ from their expected values. These will be present only for resources whose ``StackResourceDriftStatus`` is ``MODIFIED`` . 
        
                  - *(dict) --* 
        
                    Information about a resource property whose actual value differs from its expected value, as defined in the stack template and any values specified as template parameters. These will be present only for resources whose ``StackResourceDriftStatus`` is ``MODIFIED`` . For more information, see `Detecting Unregulated Configuration Changes to Stacks and Resources <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__ .
        
                    - **PropertyPath** *(string) --* 
        
                      The fully-qualified path to the resource property.
        
                    - **ExpectedValue** *(string) --* 
        
                      The expected property value of the resource property, as defined in the stack template and any values specified as template parameters.
        
                    - **ActualValue** *(string) --* 
        
                      The actual property value of the resource property.
        
                    - **DifferenceType** *(string) --* 
        
                      The type of property difference.
        
                      * ``ADD`` : A value has been added to a resource property that is an array or list data type. 
                       
                      * ``REMOVE`` : The property has been removed from the current resource configuration. 
                       
                      * ``NOT_EQUAL`` : The current property value differs from its expected value (as defined in the stack template and any values specified as template parameters). 
                       
                - **StackResourceDriftStatus** *(string) --* 
        
                  Status of the resource\'s actual configuration compared to its expected configuration
        
                  * ``DELETED`` : The resource differs from its expected template configuration because the resource has been deleted. 
                   
                  * ``MODIFIED`` : One or more resource properties differ from their expected values (as defined in the stack template and any values specified as template parameters). 
                   
                  * ``IN_SYNC`` : The resources\'s actual configuration matches its expected template configuration. 
                   
                  * ``NOT_CHECKED`` : AWS CloudFormation does not currently return this value. 
                   
                - **Timestamp** *(datetime) --* 
        
                  Time at which AWS CloudFormation performed drift detection on the stack resource.
        
            - **NextToken** *(string) --* 
        
              If the request doesn\'t return all of the remaining results, ``NextToken`` is set to a token. To retrieve the next set of results, call ``DescribeStackResourceDrifts`` again and assign that token to the request object\'s ``NextToken`` parameter. If the request returns all results, ``NextToken`` is set to ``null`` .
        
        """
        pass

    def describe_stack_resources(self, StackName: str = None, LogicalResourceId: str = None, PhysicalResourceId: str = None) -> Dict:
        """
        
        .. note::
        
          Only the first 100 resources will be returned. If your stack has more resources than this, you should use ``ListStackResources`` instead.
        
        For deleted stacks, ``DescribeStackResources`` returns resource information for up to 90 days after the stack has been deleted.
        
        You must specify either ``StackName`` or ``PhysicalResourceId`` , but not both. In addition, you can specify ``LogicalResourceId`` to filter the returned result. For more information about resources, the ``LogicalResourceId`` and ``PhysicalResourceId`` , go to the `AWS CloudFormation User Guide <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/>`__ .
        
        .. note::
        
          A ``ValidationError`` is returned if you specify both ``StackName`` and ``PhysicalResourceId`` in the same request.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStackResources>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_stack_resources(
              StackName=\'string\',
              LogicalResourceId=\'string\',
              PhysicalResourceId=\'string\'
          )
        :type StackName: string
        :param StackName: 
        
          The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
        
          * Running stacks: You can specify either the stack\'s name or its unique stack ID. 
           
          * Deleted stacks: You must specify the unique stack ID. 
           
          Default: There is no default value.
        
          Required: Conditional. If you do not specify ``StackName`` , you must specify ``PhysicalResourceId`` .
        
        :type LogicalResourceId: string
        :param LogicalResourceId: 
        
          The logical name of the resource as specified in the template.
        
          Default: There is no default value.
        
        :type PhysicalResourceId: string
        :param PhysicalResourceId: 
        
          The name or unique identifier that corresponds to a physical instance ID of a resource supported by AWS CloudFormation.
        
          For example, for an Amazon Elastic Compute Cloud (EC2) instance, ``PhysicalResourceId`` corresponds to the ``InstanceId`` . You can pass the EC2 ``InstanceId`` to ``DescribeStackResources`` to find which stack the instance belongs to and what other resources are part of the stack.
        
          Required: Conditional. If you do not specify ``PhysicalResourceId`` , you must specify ``StackName`` .
        
          Default: There is no default value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StackResources\': [
                    {
                        \'StackName\': \'string\',
                        \'StackId\': \'string\',
                        \'LogicalResourceId\': \'string\',
                        \'PhysicalResourceId\': \'string\',
                        \'ResourceType\': \'string\',
                        \'Timestamp\': datetime(2015, 1, 1),
                        \'ResourceStatus\': \'CREATE_IN_PROGRESS\'|\'CREATE_FAILED\'|\'CREATE_COMPLETE\'|\'DELETE_IN_PROGRESS\'|\'DELETE_FAILED\'|\'DELETE_COMPLETE\'|\'DELETE_SKIPPED\'|\'UPDATE_IN_PROGRESS\'|\'UPDATE_FAILED\'|\'UPDATE_COMPLETE\',
                        \'ResourceStatusReason\': \'string\',
                        \'Description\': \'string\',
                        \'DriftInformation\': {
                            \'StackResourceDriftStatus\': \'IN_SYNC\'|\'MODIFIED\'|\'DELETED\'|\'NOT_CHECKED\',
                            \'LastCheckTimestamp\': datetime(2015, 1, 1)
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for a  DescribeStackResources action.
        
            - **StackResources** *(list) --* 
        
              A list of ``StackResource`` structures.
        
              - *(dict) --* 
        
                The StackResource data type.
        
                - **StackName** *(string) --* 
        
                  The name associated with the stack.
        
                - **StackId** *(string) --* 
        
                  Unique identifier of the stack.
        
                - **LogicalResourceId** *(string) --* 
        
                  The logical name of the resource specified in the template.
        
                - **PhysicalResourceId** *(string) --* 
        
                  The name or unique identifier that corresponds to a physical instance ID of a resource supported by AWS CloudFormation.
        
                - **ResourceType** *(string) --* 
        
                  Type of resource. (For more information, go to `AWS Resource Types Reference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ in the AWS CloudFormation User Guide.)
        
                - **Timestamp** *(datetime) --* 
        
                  Time the status was updated.
        
                - **ResourceStatus** *(string) --* 
        
                  Current status of the resource.
        
                - **ResourceStatusReason** *(string) --* 
        
                  Success/failure message associated with the resource.
        
                - **Description** *(string) --* 
        
                  User defined description associated with the resource.
        
                - **DriftInformation** *(dict) --* 
        
                  Information about whether the resource\'s actual configuration differs, or has *drifted* , from its expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see `Detecting Unregulated Configuration Changes to Stacks and Resources <http://docs.aws.amazon.com/http:/docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__ .
        
                  - **StackResourceDriftStatus** *(string) --* 
        
                    Status of the resource\'s actual configuration compared to its expected configuration
        
                    * ``DELETED`` : The resource differs from its expected configuration in that it has been deleted. 
                     
                    * ``MODIFIED`` : The resource differs from its expected configuration. 
                     
                    * ``NOT_CHECKED`` : AWS CloudFormation has not checked if the resource differs from its expected configuration. Any resources that do not currently support drift detection have a status of ``NOT_CHECKED`` . For more information, see `Resources that Support Drift Detection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__ .  
                     
                    * ``IN_SYNC`` : The resources\'s actual configuration matches its expected configuration. 
                     
                  - **LastCheckTimestamp** *(datetime) --* 
        
                    When AWS CloudFormation last checked if the resource had drifted from its expected configuration.
        
        """
        pass

    def describe_stack_set(self, StackSetName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStackSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_stack_set(
              StackSetName=\'string\'
          )
        :type StackSetName: string
        :param StackSetName: **[REQUIRED]** 
        
          The name or unique ID of the stack set whose description you want.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StackSet\': {
                    \'StackSetName\': \'string\',
                    \'StackSetId\': \'string\',
                    \'Description\': \'string\',
                    \'Status\': \'ACTIVE\'|\'DELETED\',
                    \'TemplateBody\': \'string\',
                    \'Parameters\': [
                        {
                            \'ParameterKey\': \'string\',
                            \'ParameterValue\': \'string\',
                            \'UsePreviousValue\': True|False,
                            \'ResolvedValue\': \'string\'
                        },
                    ],
                    \'Capabilities\': [
                        \'CAPABILITY_IAM\'|\'CAPABILITY_NAMED_IAM\',
                    ],
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'StackSetARN\': \'string\',
                    \'AdministrationRoleARN\': \'string\',
                    \'ExecutionRoleName\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **StackSet** *(dict) --* 
        
              The specified stack set.
        
              - **StackSetName** *(string) --* 
        
                The name that\'s associated with the stack set.
        
              - **StackSetId** *(string) --* 
        
                The ID of the stack set.
        
              - **Description** *(string) --* 
        
                A description of the stack set that you specify when the stack set is created or updated.
        
              - **Status** *(string) --* 
        
                The status of the stack set.
        
              - **TemplateBody** *(string) --* 
        
                The structure that contains the body of the template that was used to create or update the stack set.
        
              - **Parameters** *(list) --* 
        
                A list of input parameters for a stack set.
        
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
        
              - **Capabilities** *(list) --* 
        
                The capabilities that are allowed in the stack set. Some stack set templates might include resources that can affect permissions in your AWS account—for example, by creating new AWS Identity and Access Management (IAM) users. For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates. <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities>`__  
        
                - *(string) --* 
            
              - **Tags** *(list) --* 
        
                A list of tags that specify information about the stack set. A maximum number of 50 tags can be specified.
        
                - *(dict) --* 
        
                  The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
        
                  - **Key** *(string) --* 
        
                     *Required* . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .
        
                  - **Value** *(string) --* 
        
                     *Required* . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
        
              - **StackSetARN** *(string) --* 
        
                The Amazon Resource Number (ARN) of the stack set.
        
              - **AdministrationRoleARN** *(string) --* 
        
                The Amazon Resource Number (ARN) of the IAM role used to create or update the stack set.
        
                Use customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see `Prerequisites\: Granting Permissions for Stack Set Operations <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html>`__ in the *AWS CloudFormation User Guide* .
        
              - **ExecutionRoleName** *(string) --* 
        
                The name of the IAM execution role used to create or update the stack set. 
        
                Use customized execution roles to control which stack resources users and groups can include in their stack sets. 
        
        """
        pass

    def describe_stack_set_operation(self, StackSetName: str, OperationId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStackSetOperation>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_stack_set_operation(
              StackSetName=\'string\',
              OperationId=\'string\'
          )
        :type StackSetName: string
        :param StackSetName: **[REQUIRED]** 
        
          The name or the unique stack ID of the stack set for the stack operation.
        
        :type OperationId: string
        :param OperationId: **[REQUIRED]** 
        
          The unique ID of the stack set operation. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StackSetOperation\': {
                    \'OperationId\': \'string\',
                    \'StackSetId\': \'string\',
                    \'Action\': \'CREATE\'|\'UPDATE\'|\'DELETE\',
                    \'Status\': \'RUNNING\'|\'SUCCEEDED\'|\'FAILED\'|\'STOPPING\'|\'STOPPED\',
                    \'OperationPreferences\': {
                        \'RegionOrder\': [
                            \'string\',
                        ],
                        \'FailureToleranceCount\': 123,
                        \'FailureTolerancePercentage\': 123,
                        \'MaxConcurrentCount\': 123,
                        \'MaxConcurrentPercentage\': 123
                    },
                    \'RetainStacks\': True|False,
                    \'AdministrationRoleARN\': \'string\',
                    \'ExecutionRoleName\': \'string\',
                    \'CreationTimestamp\': datetime(2015, 1, 1),
                    \'EndTimestamp\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **StackSetOperation** *(dict) --* 
        
              The specified stack set operation.
        
              - **OperationId** *(string) --* 
        
                The unique ID of a stack set operation.
        
              - **StackSetId** *(string) --* 
        
                The ID of the stack set.
        
              - **Action** *(string) --* 
        
                The type of stack set operation: ``CREATE`` , ``UPDATE`` , or ``DELETE`` . Create and delete operations affect only the specified stack set instances that are associated with the specified stack set. Update operations affect both the stack set itself, as well as *all* associated stack set instances.
        
              - **Status** *(string) --* 
        
                The status of the operation. 
        
                * ``FAILED`` : The operation exceeded the specified failure tolerance. The failure tolerance value that you\'ve set for an operation is applied for each region during stack create and update operations. If the number of failed stacks within a region exceeds the failure tolerance, the status of the operation in the region is set to ``FAILED`` . This in turn sets the status of the operation as a whole to ``FAILED`` , and AWS CloudFormation cancels the operation in any remaining regions. 
                 
                * ``RUNNING`` : The operation is currently being performed. 
                 
                * ``STOPPED`` : The user has cancelled the operation. 
                 
                * ``STOPPING`` : The operation is in the process of stopping, at user request.  
                 
                * ``SUCCEEDED`` : The operation completed creating or updating all the specified stacks without exceeding the failure tolerance for the operation. 
                 
              - **OperationPreferences** *(dict) --* 
        
                The preferences for how AWS CloudFormation performs this stack set operation.
        
                - **RegionOrder** *(list) --* 
        
                  The order of the regions in where you want to perform the stack operation.
        
                  - *(string) --* 
              
                - **FailureToleranceCount** *(integer) --* 
        
                  The number of accounts, per region, for which this operation can fail before AWS CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation doesn\'t attempt the operation in any subsequent regions.
        
                  Conditional: You must specify either ``FailureToleranceCount`` or ``FailureTolerancePercentage`` (but not both).
        
                - **FailureTolerancePercentage** *(integer) --* 
        
                  The percentage of accounts, per region, for which this stack operation can fail before AWS CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation doesn\'t attempt the operation in any subsequent regions.
        
                  When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds *down* to the next whole number.
        
                  Conditional: You must specify either ``FailureToleranceCount`` or ``FailureTolerancePercentage`` , but not both.
        
                - **MaxConcurrentCount** *(integer) --* 
        
                  The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of ``FailureToleranceCount`` —``MaxConcurrentCount`` is at most one more than the ``FailureToleranceCount`` .
        
                  Note that this setting lets you specify the *maximum* for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
        
                  Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` , but not both.
        
                - **MaxConcurrentPercentage** *(integer) --* 
        
                  The maximum percentage of accounts in which to perform this operation at one time.
        
                  When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.
        
                  Note that this setting lets you specify the *maximum* for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
        
                  Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` , but not both.
        
              - **RetainStacks** *(boolean) --* 
        
                For stack set operations of action type ``DELETE`` , specifies whether to remove the stack instances from the specified stack set, but doesn\'t delete the stacks. You can\'t reassociate a retained stack, or add an existing, saved stack to a new stack set.
        
              - **AdministrationRoleARN** *(string) --* 
        
                The Amazon Resource Number (ARN) of the IAM role used to perform this stack set operation. 
        
                Use customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see `Define Permissions for Multiple Administrators <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html>`__ in the *AWS CloudFormation User Guide* .
        
              - **ExecutionRoleName** *(string) --* 
        
                The name of the IAM execution role used to create or update the stack set.
        
                Use customized execution roles to control which stack resources users and groups can include in their stack sets. 
        
              - **CreationTimestamp** *(datetime) --* 
        
                The time at which the operation was initiated. Note that the creation times for the stack set operation might differ from the creation time of the individual stacks themselves. This is because AWS CloudFormation needs to perform preparatory work for the operation, such as dispatching the work to the requested regions, before actually creating the first stacks.
        
              - **EndTimestamp** *(datetime) --* 
        
                The time at which the stack set operation ended, across all accounts and regions specified. Note that this doesn\'t necessarily mean that the stack set operation was successful, or even attempted, in each account or region.
        
        """
        pass

    def describe_stacks(self, StackName: str = None, NextToken: str = None) -> Dict:
        """
        
        .. note::
        
          If the stack does not exist, an ``AmazonCloudFormationException`` is returned.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStacks>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_stacks(
              StackName=\'string\',
              NextToken=\'string\'
          )
        :type StackName: string
        :param StackName: 
        
          The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
        
          * Running stacks: You can specify either the stack\'s name or its unique stack ID. 
           
          * Deleted stacks: You must specify the unique stack ID. 
           
          Default: There is no default value.
        
        :type NextToken: string
        :param NextToken: 
        
          A string that identifies the next page of stacks that you want to retrieve.
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              If the output exceeds 1 MB in size, a string that identifies the next page of stacks. If no additional page exists, this value is null.
        
        """
        pass

    def detect_stack_drift(self, StackName: str, LogicalResourceIds: List = None) -> Dict:
        """
        
        Use ``DetectStackDrift`` to detect drift on all supported resources for a given stack, or  DetectStackResourceDrift to detect drift on individual resources.
        
        For a list of stack resources that currently support drift detection, see `Resources that Support Drift Detection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__ .
        
         ``DetectStackDrift`` can take up to several minutes, depending on the number of resources contained within the stack. Use  DescribeStackDriftDetectionStatus to monitor the progress of a detect stack drift operation. Once the drift detection operation has completed, use  DescribeStackResourceDrifts to return drift information about the stack and its resources.
        
        When detecting drift on a stack, AWS CloudFormation does not detect drift on any nested stacks belonging to that stack. Perform ``DetectStackDrift`` directly on the nested stack itself.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DetectStackDrift>`_
        
        **Request Syntax** 
        ::
        
          response = client.detect_stack_drift(
              StackName=\'string\',
              LogicalResourceIds=[
                  \'string\',
              ]
          )
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name of the stack for which you want to detect drift. 
        
        :type LogicalResourceIds: list
        :param LogicalResourceIds: 
        
          The logical names of any resources you want to use as filters.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StackDriftDetectionId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **StackDriftDetectionId** *(string) --* 
        
              The ID of the drift detection results of this operation. 
        
              AWS CloudFormation generates new results, with a new drift detection ID, each time this operation is run. However, the number of drift results AWS CloudFormation retains for any given stack, and for how long, may vary. 
        
        """
        pass

    def detect_stack_resource_drift(self, StackName: str, LogicalResourceId: str) -> Dict:
        """
        
        Use ``DetectStackResourceDrift`` to detect drift on individual resources, or  DetectStackDrift to detect drift on all resources in a given stack that support drift detection.
        
        Resources that do not currently support drift detection cannot be checked. For a list of resources that support drift detection, see `Resources that Support Drift Detection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DetectStackResourceDrift>`_
        
        **Request Syntax** 
        ::
        
          response = client.detect_stack_resource_drift(
              StackName=\'string\',
              LogicalResourceId=\'string\'
          )
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name of the stack to which the resource belongs.
        
        :type LogicalResourceId: string
        :param LogicalResourceId: **[REQUIRED]** 
        
          The logical name of the resource for which to return drift information.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StackResourceDrift\': {
                    \'StackId\': \'string\',
                    \'LogicalResourceId\': \'string\',
                    \'PhysicalResourceId\': \'string\',
                    \'PhysicalResourceIdContext\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'ResourceType\': \'string\',
                    \'ExpectedProperties\': \'string\',
                    \'ActualProperties\': \'string\',
                    \'PropertyDifferences\': [
                        {
                            \'PropertyPath\': \'string\',
                            \'ExpectedValue\': \'string\',
                            \'ActualValue\': \'string\',
                            \'DifferenceType\': \'ADD\'|\'REMOVE\'|\'NOT_EQUAL\'
                        },
                    ],
                    \'StackResourceDriftStatus\': \'IN_SYNC\'|\'MODIFIED\'|\'DELETED\'|\'NOT_CHECKED\',
                    \'Timestamp\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **StackResourceDrift** *(dict) --* 
        
              Information about whether the resource\'s actual configuration has drifted from its expected template configuration, including actual and expected property values and any differences detected.
        
              - **StackId** *(string) --* 
        
                The ID of the stack.
        
              - **LogicalResourceId** *(string) --* 
        
                The logical name of the resource specified in the template.
        
              - **PhysicalResourceId** *(string) --* 
        
                The name or unique identifier that corresponds to a physical instance ID of a resource supported by AWS CloudFormation. 
        
              - **PhysicalResourceIdContext** *(list) --* 
        
                Context information that enables AWS CloudFormation to uniquely identify a resource. AWS CloudFormation uses context key-value pairs in cases where a resource\'s logical and physical IDs are not enough to uniquely identify that resource. Each context key-value pair specifies a unique resource that contains the targeted resource.
        
                - *(dict) --* 
        
                  Context information that enables AWS CloudFormation to uniquely identify a resource. AWS CloudFormation uses context key-value pairs in cases where a resource\'s logical and physical IDs are not enough to uniquely identify that resource. Each context key-value pair specifies a resource that contains the targeted resource.
        
                  - **Key** *(string) --* 
        
                    The resource context key.
        
                  - **Value** *(string) --* 
        
                    The resource context value.
        
              - **ResourceType** *(string) --* 
        
                The type of the resource.
        
              - **ExpectedProperties** *(string) --* 
        
                A JSON structure containing the expected property values of the stack resource, as defined in the stack template and any values specified as template parameters. 
        
                For resources whose ``StackResourceDriftStatus`` is ``DELETED`` , this structure will not be present. 
        
              - **ActualProperties** *(string) --* 
        
                A JSON structure containing the actual property values of the stack resource.
        
                For resources whose ``StackResourceDriftStatus`` is ``DELETED`` , this structure will not be present. 
        
              - **PropertyDifferences** *(list) --* 
        
                A collection of the resource properties whose actual values differ from their expected values. These will be present only for resources whose ``StackResourceDriftStatus`` is ``MODIFIED`` . 
        
                - *(dict) --* 
        
                  Information about a resource property whose actual value differs from its expected value, as defined in the stack template and any values specified as template parameters. These will be present only for resources whose ``StackResourceDriftStatus`` is ``MODIFIED`` . For more information, see `Detecting Unregulated Configuration Changes to Stacks and Resources <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__ .
        
                  - **PropertyPath** *(string) --* 
        
                    The fully-qualified path to the resource property.
        
                  - **ExpectedValue** *(string) --* 
        
                    The expected property value of the resource property, as defined in the stack template and any values specified as template parameters.
        
                  - **ActualValue** *(string) --* 
        
                    The actual property value of the resource property.
        
                  - **DifferenceType** *(string) --* 
        
                    The type of property difference.
        
                    * ``ADD`` : A value has been added to a resource property that is an array or list data type. 
                     
                    * ``REMOVE`` : The property has been removed from the current resource configuration. 
                     
                    * ``NOT_EQUAL`` : The current property value differs from its expected value (as defined in the stack template and any values specified as template parameters). 
                     
              - **StackResourceDriftStatus** *(string) --* 
        
                Status of the resource\'s actual configuration compared to its expected configuration
        
                * ``DELETED`` : The resource differs from its expected template configuration because the resource has been deleted. 
                 
                * ``MODIFIED`` : One or more resource properties differ from their expected values (as defined in the stack template and any values specified as template parameters). 
                 
                * ``IN_SYNC`` : The resources\'s actual configuration matches its expected template configuration. 
                 
                * ``NOT_CHECKED`` : AWS CloudFormation does not currently return this value. 
                 
              - **Timestamp** *(datetime) --* 
        
                Time at which AWS CloudFormation performed drift detection on the stack resource.
        
        """
        pass

    def estimate_template_cost(self, TemplateBody: str = None, TemplateURL: str = None, Parameters: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/EstimateTemplateCost>`_
        
        **Request Syntax** 
        ::
        
          response = client.estimate_template_cost(
              TemplateBody=\'string\',
              TemplateURL=\'string\',
              Parameters=[
                  {
                      \'ParameterKey\': \'string\',
                      \'ParameterValue\': \'string\',
                      \'UsePreviousValue\': True|False,
                      \'ResolvedValue\': \'string\'
                  },
              ]
          )
        :type TemplateBody: string
        :param TemplateBody: 
        
          Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. (For more information, go to `Template Anatomy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`__ in the AWS CloudFormation User Guide.)
        
          Conditional: You must pass ``TemplateBody`` or ``TemplateURL`` . If both are passed, only ``TemplateBody`` is used.
        
        :type TemplateURL: string
        :param TemplateURL: 
        
          Location of file containing the template body. The URL must point to a template that is located in an Amazon S3 bucket. For more information, go to `Template Anatomy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`__ in the AWS CloudFormation User Guide.
        
          Conditional: You must pass ``TemplateURL`` or ``TemplateBody`` . If both are passed, only ``TemplateBody`` is used.
        
        :type Parameters: list
        :param Parameters: 
        
          A list of ``Parameter`` structures that specify input parameters.
        
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
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Url\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for a  EstimateTemplateCost action.
        
            - **Url** *(string) --* 
        
              An AWS Simple Monthly Calculator URL with a query string that describes the resources required to run the template.
        
        """
        pass

    def execute_change_set(self, ChangeSetName: str, StackName: str = None, ClientRequestToken: str = None) -> Dict:
        """
        
        When you execute a change set, AWS CloudFormation deletes all other change sets associated with the stack because they aren\'t valid for the updated stack.
        
        If a stack policy is associated with the stack, AWS CloudFormation enforces the policy during the update. You can\'t specify a temporary stack policy that overrides the current policy.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ExecuteChangeSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.execute_change_set(
              ChangeSetName=\'string\',
              StackName=\'string\',
              ClientRequestToken=\'string\'
          )
        :type ChangeSetName: string
        :param ChangeSetName: **[REQUIRED]** 
        
          The name or ARN of the change set that you want use to update the specified stack.
        
        :type StackName: string
        :param StackName: 
        
          If you specified the name of a change set, specify the stack name or ID (ARN) that is associated with the change set you want to execute.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          A unique identifier for this ``ExecuteChangeSet`` request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you\'re not attempting to execute a change set to update a stack with the same name. You might retry ``ExecuteChangeSet`` requests to ensure that AWS CloudFormation successfully received them.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for the  ExecuteChangeSet action.
        
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        """
        
        :type ClientMethod: string
        :param ClientMethod: The client method to presign for
        
        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.
        
        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
        
        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method\'s model.
        
        :returns: The presigned url
        """
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        """
        
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        
        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.
        
        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """
        pass

    def get_stack_policy(self, StackName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/GetStackPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_stack_policy(
              StackName=\'string\'
          )
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name or unique stack ID that is associated with the stack whose policy you want to get.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StackPolicyBody\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for the  GetStackPolicy action.
        
            - **StackPolicyBody** *(string) --* 
        
              Structure containing the stack policy body. (For more information, go to `Prevent Updates to Stack Resources <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html>`__ in the AWS CloudFormation User Guide.)
        
        """
        pass

    def get_template(self, StackName: str = None, ChangeSetName: str = None, TemplateStage: str = None) -> Dict:
        """
        
        For deleted stacks, GetTemplate returns the template for up to 90 days after the stack has been deleted.
        
        .. note::
        
          If the template does not exist, a ``ValidationError`` is returned. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/GetTemplate>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_template(
              StackName=\'string\',
              ChangeSetName=\'string\',
              TemplateStage=\'Original\'|\'Processed\'
          )
        :type StackName: string
        :param StackName: 
        
          The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
        
          * Running stacks: You can specify either the stack\'s name or its unique stack ID. 
           
          * Deleted stacks: You must specify the unique stack ID. 
           
          Default: There is no default value.
        
        :type ChangeSetName: string
        :param ChangeSetName: 
        
          The name or Amazon Resource Name (ARN) of a change set for which AWS CloudFormation returns the associated template. If you specify a name, you must also specify the ``StackName`` .
        
        :type TemplateStage: string
        :param TemplateStage: 
        
          For templates that include transforms, the stage of the template that AWS CloudFormation returns. To get the user-submitted template, specify ``Original`` . To get the template after AWS CloudFormation has processed all transforms, specify ``Processed`` . 
        
          If the template doesn\'t include transforms, ``Original`` and ``Processed`` return the same template. By default, AWS CloudFormation specifies ``Original`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TemplateBody\': {},
                \'StagesAvailable\': [
                    \'Original\'|\'Processed\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for  GetTemplate action.
        
            - **TemplateBody** (*dict*) --
        
              Structure containing the template body. (For more information, go to `Template Anatomy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`__ in the AWS CloudFormation User Guide.)
        
              AWS CloudFormation returns the same template that was used when the stack was created.
        
            - **StagesAvailable** *(list) --* 
        
              The stage of the template that you can retrieve. For stacks, the ``Original`` and ``Processed`` templates are always available. For change sets, the ``Original`` template is always available. After AWS CloudFormation finishes creating the change set, the ``Processed`` template becomes available.
        
              - *(string) --* 
          
        """
        pass

    def get_template_summary(self, TemplateBody: str = None, TemplateURL: str = None, StackName: str = None, StackSetName: str = None) -> Dict:
        """
        
        You can use the ``GetTemplateSummary`` action when you submit a template, or you can get template information for a stack set, or a running or deleted stack.
        
        For deleted stacks, ``GetTemplateSummary`` returns the template information for up to 90 days after the stack has been deleted. If the template does not exist, a ``ValidationError`` is returned.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/GetTemplateSummary>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_template_summary(
              TemplateBody=\'string\',
              TemplateURL=\'string\',
              StackName=\'string\',
              StackSetName=\'string\'
          )
        :type TemplateBody: string
        :param TemplateBody: 
        
          Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information about templates, see `Template Anatomy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`__ in the AWS CloudFormation User Guide.
        
          Conditional: You must specify only one of the following parameters: ``StackName`` , ``StackSetName`` , ``TemplateBody`` , or ``TemplateURL`` .
        
        :type TemplateURL: string
        :param TemplateURL: 
        
          Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket. For more information about templates, see `Template Anatomy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`__ in the AWS CloudFormation User Guide.
        
          Conditional: You must specify only one of the following parameters: ``StackName`` , ``StackSetName`` , ``TemplateBody`` , or ``TemplateURL`` .
        
        :type StackName: string
        :param StackName: 
        
          The name or the stack ID that is associated with the stack, which are not always interchangeable. For running stacks, you can specify either the stack\'s name or its unique stack ID. For deleted stack, you must specify the unique stack ID.
        
          Conditional: You must specify only one of the following parameters: ``StackName`` , ``StackSetName`` , ``TemplateBody`` , or ``TemplateURL`` .
        
        :type StackSetName: string
        :param StackSetName: 
        
          The name or unique ID of the stack set from which the stack was created.
        
          Conditional: You must specify only one of the following parameters: ``StackName`` , ``StackSetName`` , ``TemplateBody`` , or ``TemplateURL`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Parameters\': [
                    {
                        \'ParameterKey\': \'string\',
                        \'DefaultValue\': \'string\',
                        \'ParameterType\': \'string\',
                        \'NoEcho\': True|False,
                        \'Description\': \'string\',
                        \'ParameterConstraints\': {
                            \'AllowedValues\': [
                                \'string\',
                            ]
                        }
                    },
                ],
                \'Description\': \'string\',
                \'Capabilities\': [
                    \'CAPABILITY_IAM\'|\'CAPABILITY_NAMED_IAM\',
                ],
                \'CapabilitiesReason\': \'string\',
                \'ResourceTypes\': [
                    \'string\',
                ],
                \'Version\': \'string\',
                \'Metadata\': \'string\',
                \'DeclaredTransforms\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for the  GetTemplateSummary action.
        
            - **Parameters** *(list) --* 
        
              A list of parameter declarations that describe various properties for each parameter.
        
              - *(dict) --* 
        
                The ParameterDeclaration data type.
        
                - **ParameterKey** *(string) --* 
        
                  The name that is associated with the parameter.
        
                - **DefaultValue** *(string) --* 
        
                  The default value of the parameter.
        
                - **ParameterType** *(string) --* 
        
                  The type of parameter.
        
                - **NoEcho** *(boolean) --* 
        
                  Flag that indicates whether the parameter value is shown as plain text in logs and in the AWS Management Console.
        
                - **Description** *(string) --* 
        
                  The description that is associate with the parameter.
        
                - **ParameterConstraints** *(dict) --* 
        
                  The criteria that AWS CloudFormation uses to validate parameter values.
        
                  - **AllowedValues** *(list) --* 
        
                    A list of values that are permitted for a parameter.
        
                    - *(string) --* 
                
            - **Description** *(string) --* 
        
              The value that is defined in the ``Description`` property of the template.
        
            - **Capabilities** *(list) --* 
        
              The capabilities found within the template. If your template contains IAM resources, you must specify the CAPABILITY_IAM or CAPABILITY_NAMED_IAM value for this parameter when you use the  CreateStack or  UpdateStack actions with your template; otherwise, those actions return an InsufficientCapabilities error.
        
              For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities>`__ .
        
              - *(string) --* 
          
            - **CapabilitiesReason** *(string) --* 
        
              The list of resources that generated the values in the ``Capabilities`` response element.
        
            - **ResourceTypes** *(list) --* 
        
              A list of all the template resource types that are defined in the template, such as ``AWS::EC2::Instance`` , ``AWS::Dynamo::Table`` , and ``Custom::MyCustomInstance`` .
        
              - *(string) --* 
          
            - **Version** *(string) --* 
        
              The AWS template format version, which identifies the capabilities of the template.
        
            - **Metadata** *(string) --* 
        
              The value that is defined for the ``Metadata`` property of the template.
        
            - **DeclaredTransforms** *(list) --* 
        
              A list of the transforms that are declared in the template.
        
              - *(string) --* 
          
        """
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def list_change_sets(self, StackName: str, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListChangeSets>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_change_sets(
              StackName=\'string\',
              NextToken=\'string\'
          )
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name or the Amazon Resource Name (ARN) of the stack for which you want to list change sets.
        
        :type NextToken: string
        :param NextToken: 
        
          A string (provided by the  ListChangeSets response output) that identifies the next page of change sets that you want to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Summaries\': [
                    {
                        \'StackId\': \'string\',
                        \'StackName\': \'string\',
                        \'ChangeSetId\': \'string\',
                        \'ChangeSetName\': \'string\',
                        \'ExecutionStatus\': \'UNAVAILABLE\'|\'AVAILABLE\'|\'EXECUTE_IN_PROGRESS\'|\'EXECUTE_COMPLETE\'|\'EXECUTE_FAILED\'|\'OBSOLETE\',
                        \'Status\': \'CREATE_PENDING\'|\'CREATE_IN_PROGRESS\'|\'CREATE_COMPLETE\'|\'DELETE_COMPLETE\'|\'FAILED\',
                        \'StatusReason\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'Description\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for the  ListChangeSets action.
        
            - **Summaries** *(list) --* 
        
              A list of ``ChangeSetSummary`` structures that provides the ID and status of each change set for the specified stack.
        
              - *(dict) --* 
        
                The ``ChangeSetSummary`` structure describes a change set, its status, and the stack with which it\'s associated.
        
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
        
                  A description of the change set\'s status. For example, if your change set is in the ``FAILED`` state, AWS CloudFormation shows the error message.
        
                - **CreationTime** *(datetime) --* 
        
                  The start time when the change set was created, in UTC.
        
                - **Description** *(string) --* 
        
                  Descriptive information about the change set.
        
            - **NextToken** *(string) --* 
        
              If the output exceeds 1 MB, a string that identifies the next page of change sets. If there is no additional page, this value is null.
        
        """
        pass

    def list_exports(self, NextToken: str = None) -> Dict:
        """
        
        Lists all exported output values in the account and region in which you call this action. Use this action to see the exported output values that you can import into other stacks. To import values, use the ` ``Fn::ImportValue`` http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html`__ function. 
        
        For more information, see `AWS CloudFormation Export Stack Output Values <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-exports.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListExports>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_exports(
              NextToken=\'string\'
          )
        :type NextToken: string
        :param NextToken: 
        
          A string (provided by the  ListExports response output) that identifies the next page of exported output values that you asked to retrieve.
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              If the output exceeds 100 exported output values, a string that identifies the next page of exports. If there is no additional page, this value is null.
        
        """
        pass

    def list_imports(self, ExportName: str, NextToken: str = None) -> Dict:
        """
        
        Lists all stacks that are importing an exported output value. To modify or remove an exported output value, first use this action to see which stacks are using it. To see the exported output values in your account, see  ListExports . 
        
        For more information about importing an exported output value, see the ` ``Fn::ImportValue`` http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html`__ function. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListImports>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_imports(
              ExportName=\'string\',
              NextToken=\'string\'
          )
        :type ExportName: string
        :param ExportName: **[REQUIRED]** 
        
          The name of the exported output value. AWS CloudFormation returns the stack names that are importing this value. 
        
        :type NextToken: string
        :param NextToken: 
        
          A string (provided by the  ListImports response output) that identifies the next page of stacks that are importing the specified exported output value. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Imports\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Imports** *(list) --* 
        
              A list of stack names that are importing the specified exported output value. 
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A string that identifies the next page of exports. If there is no additional page, this value is null.
        
        """
        pass

    def list_stack_instances(self, StackSetName: str, NextToken: str = None, MaxResults: int = None, StackInstanceAccount: str = None, StackInstanceRegion: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListStackInstances>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_stack_instances(
              StackSetName=\'string\',
              NextToken=\'string\',
              MaxResults=123,
              StackInstanceAccount=\'string\',
              StackInstanceRegion=\'string\'
          )
        :type StackSetName: string
        :param StackSetName: **[REQUIRED]** 
        
          The name or unique ID of the stack set that you want to list stack instances for.
        
        :type NextToken: string
        :param NextToken: 
        
          If the previous request didn\'t return all of the remaining results, the response\'s ``NextToken`` parameter value is set to a token. To retrieve the next set of results, call ``ListStackInstances`` again and assign that token to the request object\'s ``NextToken`` parameter. If there are no remaining results, the previous response object\'s ``NextToken`` parameter is set to ``null`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a ``NextToken`` value that you can assign to the ``NextToken`` request parameter to get the next set of results.
        
        :type StackInstanceAccount: string
        :param StackInstanceAccount: 
        
          The name of the AWS account that you want to list stack instances for.
        
        :type StackInstanceRegion: string
        :param StackInstanceRegion: 
        
          The name of the region where you want to list stack instances. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Summaries\': [
                    {
                        \'StackSetId\': \'string\',
                        \'Region\': \'string\',
                        \'Account\': \'string\',
                        \'StackId\': \'string\',
                        \'Status\': \'CURRENT\'|\'OUTDATED\'|\'INOPERABLE\',
                        \'StatusReason\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
                   
                  * ``OUTDATED`` : The stack isn\'t currently up to date with the stack set because: 
        
                    * The associated stack failed during a ``CreateStackSet`` or ``UpdateStackSet`` operation.  
                     
                    * The stack was part of a ``CreateStackSet`` or ``UpdateStackSet`` operation that failed or was stopped before the stack was created or updated.  
                     
                  * ``CURRENT`` : The stack is currently up to date with the stack set. 
                   
                - **StatusReason** *(string) --* 
        
                  The explanation for the specific status code assigned to this stack instance.
        
            - **NextToken** *(string) --* 
        
              If the request doesn\'t return all of the remaining results, ``NextToken`` is set to a token. To retrieve the next set of results, call ``ListStackInstances`` again and assign that token to the request object\'s ``NextToken`` parameter. If the request returns all results, ``NextToken`` is set to ``null`` .
        
        """
        pass

    def list_stack_resources(self, StackName: str, NextToken: str = None) -> Dict:
        """
        
        For deleted stacks, ListStackResources returns resource information for up to 90 days after the stack has been deleted.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListStackResources>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_stack_resources(
              StackName=\'string\',
              NextToken=\'string\'
          )
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
        
          * Running stacks: You can specify either the stack\'s name or its unique stack ID. 
           
          * Deleted stacks: You must specify the unique stack ID. 
           
          Default: There is no default value.
        
        :type NextToken: string
        :param NextToken: 
        
          A string that identifies the next page of stack resources that you want to retrieve.
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              If the output exceeds 1 MB, a string that identifies the next page of stack resources. If no additional page exists, this value is null.
        
        """
        pass

    def list_stack_set_operation_results(self, StackSetName: str, OperationId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListStackSetOperationResults>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_stack_set_operation_results(
              StackSetName=\'string\',
              OperationId=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type StackSetName: string
        :param StackSetName: **[REQUIRED]** 
        
          The name or unique ID of the stack set that you want to get operation results for.
        
        :type OperationId: string
        :param OperationId: **[REQUIRED]** 
        
          The ID of the stack set operation.
        
        :type NextToken: string
        :param NextToken: 
        
          If the previous request didn\'t return all of the remaining results, the response object\'s ``NextToken`` parameter value is set to a token. To retrieve the next set of results, call ``ListStackSetOperationResults`` again and assign that token to the request object\'s ``NextToken`` parameter. If there are no remaining results, the previous response object\'s ``NextToken`` parameter is set to ``null`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a ``NextToken`` value that you can assign to the ``NextToken`` request parameter to get the next set of results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Summaries\': [
                    {
                        \'Account\': \'string\',
                        \'Region\': \'string\',
                        \'Status\': \'PENDING\'|\'RUNNING\'|\'SUCCEEDED\'|\'FAILED\'|\'CANCELLED\',
                        \'StatusReason\': \'string\',
                        \'AccountGateResult\': {
                            \'Status\': \'SUCCEEDED\'|\'FAILED\'|\'SKIPPED\',
                            \'StatusReason\': \'string\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Summaries** *(list) --* 
        
              A list of ``StackSetOperationResultSummary`` structures that contain information about the specified operation results, for accounts and regions that are included in the operation.
        
              - *(dict) --* 
        
                The structure that contains information about a specified operation\'s results for a given account in a given region.
        
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
        
            - **NextToken** *(string) --* 
        
              If the request doesn\'t return all results, ``NextToken`` is set to a token. To retrieve the next set of results, call ``ListOperationResults`` again and assign that token to the request object\'s ``NextToken`` parameter. If there are no remaining results, ``NextToken`` is set to ``null`` .
        
        """
        pass

    def list_stack_set_operations(self, StackSetName: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListStackSetOperations>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_stack_set_operations(
              StackSetName=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type StackSetName: string
        :param StackSetName: **[REQUIRED]** 
        
          The name or unique ID of the stack set that you want to get operation summaries for.
        
        :type NextToken: string
        :param NextToken: 
        
          If the previous paginated request didn\'t return all of the remaining results, the response object\'s ``NextToken`` parameter value is set to a token. To retrieve the next set of results, call ``ListStackSetOperations`` again and assign that token to the request object\'s ``NextToken`` parameter. If there are no remaining results, the previous response object\'s ``NextToken`` parameter is set to ``null`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a ``NextToken`` value that you can assign to the ``NextToken`` request parameter to get the next set of results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Summaries\': [
                    {
                        \'OperationId\': \'string\',
                        \'Action\': \'CREATE\'|\'UPDATE\'|\'DELETE\',
                        \'Status\': \'RUNNING\'|\'SUCCEEDED\'|\'FAILED\'|\'STOPPING\'|\'STOPPED\',
                        \'CreationTimestamp\': datetime(2015, 1, 1),
                        \'EndTimestamp\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  * ``FAILED`` : The operation exceeded the specified failure tolerance. The failure tolerance value that you\'ve set for an operation is applied for each region during stack create and update operations. If the number of failed stacks within a region exceeds the failure tolerance, the status of the operation in the region is set to ``FAILED`` . This in turn sets the status of the operation as a whole to ``FAILED`` , and AWS CloudFormation cancels the operation in any remaining regions. 
                   
                  * ``RUNNING`` : The operation is currently being performed. 
                   
                  * ``STOPPED`` : The user has cancelled the operation. 
                   
                  * ``STOPPING`` : The operation is in the process of stopping, at user request.  
                   
                  * ``SUCCEEDED`` : The operation completed creating or updating all the specified stacks without exceeding the failure tolerance for the operation. 
                   
                - **CreationTimestamp** *(datetime) --* 
        
                  The time at which the operation was initiated. Note that the creation times for the stack set operation might differ from the creation time of the individual stacks themselves. This is because AWS CloudFormation needs to perform preparatory work for the operation, such as dispatching the work to the requested regions, before actually creating the first stacks.
        
                - **EndTimestamp** *(datetime) --* 
        
                  The time at which the stack set operation ended, across all accounts and regions specified. Note that this doesn\'t necessarily mean that the stack set operation was successful, or even attempted, in each account or region.
        
            - **NextToken** *(string) --* 
        
              If the request doesn\'t return all results, ``NextToken`` is set to a token. To retrieve the next set of results, call ``ListOperationResults`` again and assign that token to the request object\'s ``NextToken`` parameter. If there are no remaining results, ``NextToken`` is set to ``null`` .
        
        """
        pass

    def list_stack_sets(self, NextToken: str = None, MaxResults: int = None, Status: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListStackSets>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_stack_sets(
              NextToken=\'string\',
              MaxResults=123,
              Status=\'ACTIVE\'|\'DELETED\'
          )
        :type NextToken: string
        :param NextToken: 
        
          If the previous paginated request didn\'t return all of the remaining results, the response object\'s ``NextToken`` parameter value is set to a token. To retrieve the next set of results, call ``ListStackSets`` again and assign that token to the request object\'s ``NextToken`` parameter. If there are no remaining results, the previous response object\'s ``NextToken`` parameter is set to ``null`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a ``NextToken`` value that you can assign to the ``NextToken`` request parameter to get the next set of results.
        
        :type Status: string
        :param Status: 
        
          The status of the stack sets that you want to get summary information about.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Summaries\': [
                    {
                        \'StackSetName\': \'string\',
                        \'StackSetId\': \'string\',
                        \'Description\': \'string\',
                        \'Status\': \'ACTIVE\'|\'DELETED\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Summaries** *(list) --* 
        
              A list of ``StackSetSummary`` structures that contain information about the user\'s stack sets.
        
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
        
            - **NextToken** *(string) --* 
        
              If the request doesn\'t return all of the remaining results, ``NextToken`` is set to a token. To retrieve the next set of results, call ``ListStackInstances`` again and assign that token to the request object\'s ``NextToken`` parameter. If the request returns all results, ``NextToken`` is set to ``null`` .
        
        """
        pass

    def list_stacks(self, NextToken: str = None, StackStatusFilter: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListStacks>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_stacks(
              NextToken=\'string\',
              StackStatusFilter=[
                  \'CREATE_IN_PROGRESS\'|\'CREATE_FAILED\'|\'CREATE_COMPLETE\'|\'ROLLBACK_IN_PROGRESS\'|\'ROLLBACK_FAILED\'|\'ROLLBACK_COMPLETE\'|\'DELETE_IN_PROGRESS\'|\'DELETE_FAILED\'|\'DELETE_COMPLETE\'|\'UPDATE_IN_PROGRESS\'|\'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS\'|\'UPDATE_COMPLETE\'|\'UPDATE_ROLLBACK_IN_PROGRESS\'|\'UPDATE_ROLLBACK_FAILED\'|\'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS\'|\'UPDATE_ROLLBACK_COMPLETE\'|\'REVIEW_IN_PROGRESS\',
              ]
          )
        :type NextToken: string
        :param NextToken: 
        
          A string that identifies the next page of stacks that you want to retrieve.
        
        :type StackStatusFilter: list
        :param StackStatusFilter: 
        
          Stack status to use as a filter. Specify one or more stack status codes to list only stacks with the specified status codes. For a complete list of stack status codes, see the ``StackStatus`` parameter of the  Stack data type.
        
          - *(string) --* 
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              If the output exceeds 1 MB in size, a string that identifies the next page of stacks. If no additional page exists, this value is null.
        
        """
        pass

    def set_stack_policy(self, StackName: str, StackPolicyBody: str = None, StackPolicyURL: str = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/SetStackPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.set_stack_policy(
              StackName=\'string\',
              StackPolicyBody=\'string\',
              StackPolicyURL=\'string\'
          )
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name or unique stack ID that you want to associate a policy with.
        
        :type StackPolicyBody: string
        :param StackPolicyBody: 
        
          Structure containing the stack policy body. For more information, go to `Prevent Updates to Stack Resources <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html>`__ in the AWS CloudFormation User Guide. You can specify either the ``StackPolicyBody`` or the ``StackPolicyURL`` parameter, but not both.
        
        :type StackPolicyURL: string
        :param StackPolicyURL: 
        
          Location of a file containing the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an S3 bucket in the same region as the stack. You can specify either the ``StackPolicyBody`` or the ``StackPolicyURL`` parameter, but not both.
        
        :returns: None
        """
        pass

    def signal_resource(self, StackName: str, LogicalResourceId: str, UniqueId: str, Status: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/SignalResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.signal_resource(
              StackName=\'string\',
              LogicalResourceId=\'string\',
              UniqueId=\'string\',
              Status=\'SUCCESS\'|\'FAILURE\'
          )
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The stack name or unique stack ID that includes the resource that you want to signal.
        
        :type LogicalResourceId: string
        :param LogicalResourceId: **[REQUIRED]** 
        
          The logical ID of the resource that you want to signal. The logical ID is the name of the resource that given in the template.
        
        :type UniqueId: string
        :param UniqueId: **[REQUIRED]** 
        
          A unique ID of the signal. When you signal Amazon EC2 instances or Auto Scaling groups, specify the instance ID that you are signaling as the unique ID. If you send multiple signals to a single resource (such as signaling a wait condition), each signal requires a different unique ID.
        
        :type Status: string
        :param Status: **[REQUIRED]** 
        
          The status of the signal, which is either success or failure. A failure signal causes AWS CloudFormation to immediately fail the stack creation or update.
        
        :returns: None
        """
        pass

    def stop_stack_set_operation(self, StackSetName: str, OperationId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/StopStackSetOperation>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_stack_set_operation(
              StackSetName=\'string\',
              OperationId=\'string\'
          )
        :type StackSetName: string
        :param StackSetName: **[REQUIRED]** 
        
          The name or unique ID of the stack set that you want to stop the operation for.
        
        :type OperationId: string
        :param OperationId: **[REQUIRED]** 
        
          The ID of the stack operation. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_stack(self, StackName: str, TemplateBody: str = None, TemplateURL: str = None, UsePreviousTemplate: bool = None, StackPolicyDuringUpdateBody: str = None, StackPolicyDuringUpdateURL: str = None, Parameters: List = None, Capabilities: List = None, ResourceTypes: List = None, RoleARN: str = None, RollbackConfiguration: Dict = None, StackPolicyBody: str = None, StackPolicyURL: str = None, NotificationARNs: List = None, Tags: List = None, ClientRequestToken: str = None) -> Dict:
        """
        
        To get a copy of the template for an existing stack, you can use the  GetTemplate action.
        
        For more information about creating an update template, updating a stack, and monitoring the progress of the update, see `Updating a Stack <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/UpdateStack>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_stack(
              StackName=\'string\',
              TemplateBody=\'string\',
              TemplateURL=\'string\',
              UsePreviousTemplate=True|False,
              StackPolicyDuringUpdateBody=\'string\',
              StackPolicyDuringUpdateURL=\'string\',
              Parameters=[
                  {
                      \'ParameterKey\': \'string\',
                      \'ParameterValue\': \'string\',
                      \'UsePreviousValue\': True|False,
                      \'ResolvedValue\': \'string\'
                  },
              ],
              Capabilities=[
                  \'CAPABILITY_IAM\'|\'CAPABILITY_NAMED_IAM\',
              ],
              ResourceTypes=[
                  \'string\',
              ],
              RoleARN=\'string\',
              RollbackConfiguration={
                  \'RollbackTriggers\': [
                      {
                          \'Arn\': \'string\',
                          \'Type\': \'string\'
                      },
                  ],
                  \'MonitoringTimeInMinutes\': 123
              },
              StackPolicyBody=\'string\',
              StackPolicyURL=\'string\',
              NotificationARNs=[
                  \'string\',
              ],
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              ClientRequestToken=\'string\'
          )
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name or unique stack ID of the stack to update.
        
        :type TemplateBody: string
        :param TemplateBody: 
        
          Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. (For more information, go to `Template Anatomy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`__ in the AWS CloudFormation User Guide.)
        
          Conditional: You must specify only one of the following parameters: ``TemplateBody`` , ``TemplateURL`` , or set the ``UsePreviousTemplate`` to ``true`` .
        
        :type TemplateURL: string
        :param TemplateURL: 
        
          Location of file containing the template body. The URL must point to a template that is located in an Amazon S3 bucket. For more information, go to `Template Anatomy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`__ in the AWS CloudFormation User Guide.
        
          Conditional: You must specify only one of the following parameters: ``TemplateBody`` , ``TemplateURL`` , or set the ``UsePreviousTemplate`` to ``true`` .
        
        :type UsePreviousTemplate: boolean
        :param UsePreviousTemplate: 
        
          Reuse the existing template that is associated with the stack that you are updating.
        
          Conditional: You must specify only one of the following parameters: ``TemplateBody`` , ``TemplateURL`` , or set the ``UsePreviousTemplate`` to ``true`` .
        
        :type StackPolicyDuringUpdateBody: string
        :param StackPolicyDuringUpdateBody: 
        
          Structure containing the temporary overriding stack policy body. You can specify either the ``StackPolicyDuringUpdateBody`` or the ``StackPolicyDuringUpdateURL`` parameter, but not both.
        
          If you want to update protected resources, specify a temporary overriding stack policy during this update. If you do not specify a stack policy, the current policy that is associated with the stack will be used.
        
        :type StackPolicyDuringUpdateURL: string
        :param StackPolicyDuringUpdateURL: 
        
          Location of a file containing the temporary overriding stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same region as the stack. You can specify either the ``StackPolicyDuringUpdateBody`` or the ``StackPolicyDuringUpdateURL`` parameter, but not both.
        
          If you want to update protected resources, specify a temporary overriding stack policy during this update. If you do not specify a stack policy, the current policy that is associated with the stack will be used.
        
        :type Parameters: list
        :param Parameters: 
        
          A list of ``Parameter`` structures that specify input parameters for the stack. For more information, see the `Parameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html>`__ data type.
        
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
        
        :type Capabilities: list
        :param Capabilities: 
        
          A list of values that you must specify before AWS CloudFormation can update certain stacks. Some stack templates might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge their capabilities by specifying this parameter.
        
          The only valid values are ``CAPABILITY_IAM`` and ``CAPABILITY_NAMED_IAM`` . The following resources require you to specify this parameter: `AWS\:\:IAM\:\:AccessKey <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html>`__ , `AWS\:\:IAM\:\:Group <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html>`__ , `AWS\:\:IAM\:\:InstanceProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html>`__ , `AWS\:\:IAM\:\:Policy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html>`__ , `AWS\:\:IAM\:\:Role <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html>`__ , `AWS\:\:IAM\:\:User <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html>`__ , and `AWS\:\:IAM\:\:UserToGroupAddition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html>`__ . If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.
        
          If you have IAM resources, you can specify either capability. If you have IAM resources with custom names, you must specify ``CAPABILITY_NAMED_IAM`` . If you don\'t specify this parameter, this action returns an ``InsufficientCapabilities`` error.
        
          For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities>`__ .
        
          - *(string) --* 
        
        :type ResourceTypes: list
        :param ResourceTypes: 
        
          The template resource types that you have permissions to work with for this update stack action, such as ``AWS::EC2::Instance`` , ``AWS::EC2::*`` , or ``Custom::MyCustomInstance`` .
        
          If the list of resource types doesn\'t include a resource that you\'re updating, the stack update fails. By default, AWS CloudFormation grants permissions to all resource types. AWS Identity and Access Management (IAM) uses this parameter for AWS CloudFormation-specific condition keys in IAM policies. For more information, see `Controlling Access with AWS Identity and Access Management <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html>`__ .
        
          - *(string) --* 
        
        :type RoleARN: string
        :param RoleARN: 
        
          The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes to update the stack. AWS CloudFormation uses the role\'s credentials to make calls on your behalf. AWS CloudFormation always uses this role for all future operations on the stack. As long as users have permission to operate on the stack, AWS CloudFormation uses this role even if the users don\'t have permission to pass it. Ensure that the role grants least privilege.
        
          If you don\'t specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
        
        :type RollbackConfiguration: dict
        :param RollbackConfiguration: 
        
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
        
              - **Arn** *(string) --* **[REQUIRED]** 
        
                The Amazon Resource Name (ARN) of the rollback trigger.
        
                If a specified trigger is missing, the entire stack operation fails and is rolled back. 
        
              - **Type** *(string) --* **[REQUIRED]** 
        
                The resource type of the rollback trigger. Currently, `AWS\:\:CloudWatch\:\:Alarm <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html>`__ is the only supported resource type.
        
          - **MonitoringTimeInMinutes** *(integer) --* 
        
            The amount of time, in minutes, during which CloudFormation should monitor all the rollback triggers after the stack creation or update operation deploys all necessary resources.
        
            The default is 0 minutes.
        
            If you specify a monitoring period but do not specify any rollback triggers, CloudFormation still waits the specified period of time before cleaning up old resources after update operations. You can use this monitoring period to perform any manual stack validation desired, and manually cancel the stack creation or update (using `CancelUpdateStack <http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html>`__ , for example) as necessary.
        
            If you specify 0 for this parameter, CloudFormation still monitors the specified rollback triggers during stack creation and update operations. Then, for update operations, it begins disposing of old resources immediately once the operation completes.
        
        :type StackPolicyBody: string
        :param StackPolicyBody: 
        
          Structure containing a new stack policy body. You can specify either the ``StackPolicyBody`` or the ``StackPolicyURL`` parameter, but not both.
        
          You might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you do not specify a stack policy, the current policy that is associated with the stack is unchanged.
        
        :type StackPolicyURL: string
        :param StackPolicyURL: 
        
          Location of a file containing the updated stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same region as the stack. You can specify either the ``StackPolicyBody`` or the ``StackPolicyURL`` parameter, but not both.
        
          You might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you do not specify a stack policy, the current policy that is associated with the stack is unchanged.
        
        :type NotificationARNs: list
        :param NotificationARNs: 
        
          Amazon Simple Notification Service topic Amazon Resource Names (ARNs) that AWS CloudFormation associates with the stack. Specify an empty list to remove all notification topics.
        
          - *(string) --* 
        
        :type Tags: list
        :param Tags: 
        
          Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to supported resources in the stack. You can specify a maximum number of 50 tags.
        
          If you don\'t specify this parameter, AWS CloudFormation doesn\'t modify the stack\'s tags. If you specify an empty value, AWS CloudFormation removes all associated tags.
        
          - *(dict) --* 
        
            The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
               *Required* . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .
        
            - **Value** *(string) --* **[REQUIRED]** 
        
               *Required* . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          A unique identifier for this ``UpdateStack`` request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you\'re not attempting to update a stack with the same name. You might retry ``UpdateStack`` requests to ensure that AWS CloudFormation successfully received them.
        
          All events triggered by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a ``CreateStack`` operation with the token ``token1`` , then all the ``StackEvents`` generated by that operation will have ``ClientRequestToken`` set as ``token1`` .
        
          In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format *Console-StackOperation-ID* , which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: ``Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StackId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for an  UpdateStack action.
        
            - **StackId** *(string) --* 
        
              Unique identifier of the stack.
        
        """
        pass

    def update_stack_instances(self, StackSetName: str, Accounts: List, Regions: List, ParameterOverrides: List = None, OperationPreferences: Dict = None, OperationId: str = None) -> Dict:
        """
        
        You can only update stack instances in regions and accounts where they already exist; to create additional stack instances, use `CreateStackInstances <http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStackInstances.html>`__ . 
        
        During stack set updates, any parameters overridden for a stack instance are not updated, but retain their overridden value.
        
        You can only update the parameter *values* that are specified in the stack set; to add or delete a parameter itself, use `UpdateStackSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html>`__ to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use `UpdateStackSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html>`__ to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using ``UpdateStackInstances`` .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/UpdateStackInstances>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_stack_instances(
              StackSetName=\'string\',
              Accounts=[
                  \'string\',
              ],
              Regions=[
                  \'string\',
              ],
              ParameterOverrides=[
                  {
                      \'ParameterKey\': \'string\',
                      \'ParameterValue\': \'string\',
                      \'UsePreviousValue\': True|False,
                      \'ResolvedValue\': \'string\'
                  },
              ],
              OperationPreferences={
                  \'RegionOrder\': [
                      \'string\',
                  ],
                  \'FailureToleranceCount\': 123,
                  \'FailureTolerancePercentage\': 123,
                  \'MaxConcurrentCount\': 123,
                  \'MaxConcurrentPercentage\': 123
              },
              OperationId=\'string\'
          )
        :type StackSetName: string
        :param StackSetName: **[REQUIRED]** 
        
          The name or unique ID of the stack set associated with the stack instances.
        
        :type Accounts: list
        :param Accounts: **[REQUIRED]** 
        
          The names of one or more AWS accounts for which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and regions.
        
          - *(string) --* 
        
        :type Regions: list
        :param Regions: **[REQUIRED]** 
        
          The names of one or more regions in which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and regions.
        
          - *(string) --* 
        
        :type ParameterOverrides: list
        :param ParameterOverrides: 
        
          A list of input parameters whose values you want to update for the specified stack instances. 
        
          Any overridden parameter values will be applied to all stack instances in the specified accounts and regions. When specifying parameters and their values, be aware of how AWS CloudFormation sets parameter values during stack instance update operations:
        
          * To override the current value for a parameter, include the parameter and specify its value. 
           
          * To leave a parameter set to its present value, you can do one of the following: 
        
            * Do not include the parameter in the list. 
             
            * Include the parameter and specify ``UsePreviousValue`` as ``true`` . (You cannot specify both a value and set ``UsePreviousValue`` to ``true`` .) 
             
          * To set all overridden parameter back to the values specified in the stack set, specify a parameter list but do not include any parameters. 
           
          * To leave all parameters set to their present values, do not specify this property at all. 
           
          During stack set updates, any parameter values overridden for a stack instance are not updated, but retain their overridden value.
        
          You can only override the parameter *values* that are specified in the stack set; to add or delete a parameter itself, use ``UpdateStackSet`` to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use `UpdateStackSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html>`__ to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using ``UpdateStackInstances`` .
        
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
        
        :type OperationPreferences: dict
        :param OperationPreferences: 
        
          Preferences for how AWS CloudFormation performs this stack set operation.
        
          - **RegionOrder** *(list) --* 
        
            The order of the regions in where you want to perform the stack operation.
        
            - *(string) --* 
        
          - **FailureToleranceCount** *(integer) --* 
        
            The number of accounts, per region, for which this operation can fail before AWS CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation doesn\'t attempt the operation in any subsequent regions.
        
            Conditional: You must specify either ``FailureToleranceCount`` or ``FailureTolerancePercentage`` (but not both).
        
          - **FailureTolerancePercentage** *(integer) --* 
        
            The percentage of accounts, per region, for which this stack operation can fail before AWS CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation doesn\'t attempt the operation in any subsequent regions.
        
            When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds *down* to the next whole number.
        
            Conditional: You must specify either ``FailureToleranceCount`` or ``FailureTolerancePercentage`` , but not both.
        
          - **MaxConcurrentCount** *(integer) --* 
        
            The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of ``FailureToleranceCount`` —``MaxConcurrentCount`` is at most one more than the ``FailureToleranceCount`` .
        
            Note that this setting lets you specify the *maximum* for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
        
            Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` , but not both.
        
          - **MaxConcurrentPercentage** *(integer) --* 
        
            The maximum percentage of accounts in which to perform this operation at one time.
        
            When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.
        
            Note that this setting lets you specify the *maximum* for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
        
            Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` , but not both.
        
        :type OperationId: string
        :param OperationId: 
        
          The unique identifier for this stack set operation. 
        
          The operation ID also functions as an idempotency token, to ensure that AWS CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that AWS CloudFormation successfully received them.
        
          If you don\'t specify an operation ID, the SDK generates one automatically. 
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **OperationId** *(string) --* 
        
              The unique identifier for this stack set operation. 
        
        """
        pass

    def update_stack_set(self, StackSetName: str, Description: str = None, TemplateBody: str = None, TemplateURL: str = None, UsePreviousTemplate: bool = None, Parameters: List = None, Capabilities: List = None, Tags: List = None, OperationPreferences: Dict = None, AdministrationRoleARN: str = None, ExecutionRoleName: str = None, OperationId: str = None, Accounts: List = None, Regions: List = None) -> Dict:
        """
        
        Even if the stack set operation created by updating the stack set fails (completely or partially, below or above a specified failure tolerance), the stack set is updated with your changes. Subsequent  CreateStackInstances calls on the specified stack set use the updated stack set.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/UpdateStackSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_stack_set(
              StackSetName=\'string\',
              Description=\'string\',
              TemplateBody=\'string\',
              TemplateURL=\'string\',
              UsePreviousTemplate=True|False,
              Parameters=[
                  {
                      \'ParameterKey\': \'string\',
                      \'ParameterValue\': \'string\',
                      \'UsePreviousValue\': True|False,
                      \'ResolvedValue\': \'string\'
                  },
              ],
              Capabilities=[
                  \'CAPABILITY_IAM\'|\'CAPABILITY_NAMED_IAM\',
              ],
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              OperationPreferences={
                  \'RegionOrder\': [
                      \'string\',
                  ],
                  \'FailureToleranceCount\': 123,
                  \'FailureTolerancePercentage\': 123,
                  \'MaxConcurrentCount\': 123,
                  \'MaxConcurrentPercentage\': 123
              },
              AdministrationRoleARN=\'string\',
              ExecutionRoleName=\'string\',
              OperationId=\'string\',
              Accounts=[
                  \'string\',
              ],
              Regions=[
                  \'string\',
              ]
          )
        :type StackSetName: string
        :param StackSetName: **[REQUIRED]** 
        
          The name or unique ID of the stack set that you want to update.
        
        :type Description: string
        :param Description: 
        
          A brief description of updates that you are making.
        
        :type TemplateBody: string
        :param TemplateBody: 
        
          The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, see `Template Anatomy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`__ in the AWS CloudFormation User Guide.
        
          Conditional: You must specify only one of the following parameters: ``TemplateBody`` or ``TemplateURL`` —or set ``UsePreviousTemplate`` to true.
        
        :type TemplateURL: string
        :param TemplateURL: 
        
          The location of the file that contains the template body. The URL must point to a template (maximum size: 460,800 bytes) that is located in an Amazon S3 bucket. For more information, see `Template Anatomy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`__ in the AWS CloudFormation User Guide.
        
          Conditional: You must specify only one of the following parameters: ``TemplateBody`` or ``TemplateURL`` —or set ``UsePreviousTemplate`` to true. 
        
        :type UsePreviousTemplate: boolean
        :param UsePreviousTemplate: 
        
          Use the existing template that\'s associated with the stack set that you\'re updating.
        
          Conditional: You must specify only one of the following parameters: ``TemplateBody`` or ``TemplateURL`` —or set ``UsePreviousTemplate`` to true. 
        
        :type Parameters: list
        :param Parameters: 
        
          A list of input parameters for the stack set template. 
        
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
        
        :type Capabilities: list
        :param Capabilities: 
        
          A list of values that you must specify before AWS CloudFormation can create certain stack sets. Some stack set templates might include resources that can affect permissions in your AWS account—for example, by creating new AWS Identity and Access Management (IAM) users. For those stack sets, you must explicitly acknowledge their capabilities by specifying this parameter.
        
          The only valid values are CAPABILITY_IAM and CAPABILITY_NAMED_IAM. The following resources require you to specify this parameter: 
        
          * AWS::IAM::AccessKey 
           
          * AWS::IAM::Group 
           
          * AWS::IAM::InstanceProfile 
           
          * AWS::IAM::Policy 
           
          * AWS::IAM::Role 
           
          * AWS::IAM::User 
           
          * AWS::IAM::UserToGroupAddition 
           
          If your stack template contains these resources, we recommend that you review all permissions that are associated with them and edit their permissions if necessary.
        
          If you have IAM resources, you can specify either capability. If you have IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM. If you don\'t specify this parameter, this action returns an ``InsufficientCapabilities`` error.
        
          For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates. <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities>`__  
        
          - *(string) --* 
        
        :type Tags: list
        :param Tags: 
        
          The key-value pairs to associate with this stack set and the stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the stacks. You can specify a maximum number of 50 tags.
        
          If you specify tags for this parameter, those tags replace any list of tags that are currently associated with this stack set. This means:
        
          * If you don\'t specify this parameter, AWS CloudFormation doesn\'t modify the stack\'s tags.  
           
          * If you specify *any* tags using this parameter, you must specify *all* the tags that you want associated with this stack set, even tags you\'ve specifed before (for example, when creating the stack set or during a previous update of the stack set.). Any tags that you don\'t include in the updated list of tags are removed from the stack set, and therefore from the stacks and resources as well.  
           
          * If you specify an empty value, AWS CloudFormation removes all currently associated tags. 
           
          If you specify new tags as part of an ``UpdateStackSet`` action, AWS CloudFormation checks to see if you have the required IAM permission to tag resources. If you omit tags that are currently associated with the stack set from the list of tags you specify, AWS CloudFormation assumes that you want to remove those tags from the stack set, and checks to see if you have permission to untag resources. If you don\'t have the necessary permission(s), the entire ``UpdateStackSet`` action fails with an ``access denied`` error, and the stack set is not updated.
        
          - *(dict) --* 
        
            The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
               *Required* . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .
        
            - **Value** *(string) --* **[REQUIRED]** 
        
               *Required* . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
        
        :type OperationPreferences: dict
        :param OperationPreferences: 
        
          Preferences for how AWS CloudFormation performs this stack set operation.
        
          - **RegionOrder** *(list) --* 
        
            The order of the regions in where you want to perform the stack operation.
        
            - *(string) --* 
        
          - **FailureToleranceCount** *(integer) --* 
        
            The number of accounts, per region, for which this operation can fail before AWS CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation doesn\'t attempt the operation in any subsequent regions.
        
            Conditional: You must specify either ``FailureToleranceCount`` or ``FailureTolerancePercentage`` (but not both).
        
          - **FailureTolerancePercentage** *(integer) --* 
        
            The percentage of accounts, per region, for which this stack operation can fail before AWS CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation doesn\'t attempt the operation in any subsequent regions.
        
            When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds *down* to the next whole number.
        
            Conditional: You must specify either ``FailureToleranceCount`` or ``FailureTolerancePercentage`` , but not both.
        
          - **MaxConcurrentCount** *(integer) --* 
        
            The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of ``FailureToleranceCount`` —``MaxConcurrentCount`` is at most one more than the ``FailureToleranceCount`` .
        
            Note that this setting lets you specify the *maximum* for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
        
            Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` , but not both.
        
          - **MaxConcurrentPercentage** *(integer) --* 
        
            The maximum percentage of accounts in which to perform this operation at one time.
        
            When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.
        
            Note that this setting lets you specify the *maximum* for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
        
            Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` , but not both.
        
        :type AdministrationRoleARN: string
        :param AdministrationRoleARN: 
        
          The Amazon Resource Number (ARN) of the IAM role to use to update this stack set.
        
          Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see `Define Permissions for Multiple Administrators <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html>`__ in the *AWS CloudFormation User Guide* .
        
          If you specify a customized administrator role, AWS CloudFormation uses that role to update the stack. If you do not specify a customized administrator role, AWS CloudFormation performs the update using the role previously associated with the stack set, so long as you have permissions to perform operations on the stack set.
        
        :type ExecutionRoleName: string
        :param ExecutionRoleName: 
        
          The name of the IAM execution role to use to update the stack set. If you do not specify an execution role, AWS CloudFormation uses the ``AWSCloudFormationStackSetExecutionRole`` role for the stack set operation.
        
          Specify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their stack sets. 
        
          If you specify a customized execution role, AWS CloudFormation uses that role to update the stack. If you do not specify a customized execution role, AWS CloudFormation performs the update using the role previously associated with the stack set, so long as you have permissions to perform operations on the stack set.
        
        :type OperationId: string
        :param OperationId: 
        
          The unique ID for this stack set operation. 
        
          The operation ID also functions as an idempotency token, to ensure that AWS CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that AWS CloudFormation successfully received them.
        
          If you don\'t specify an operation ID, AWS CloudFormation generates one automatically.
        
          Repeating this stack set operation with a new operation ID retries all stack instances whose status is ``OUTDATED`` . 
        
          This field is autopopulated if not provided.
        
        :type Accounts: list
        :param Accounts: 
        
          The accounts in which to update associated stack instances. If you specify accounts, you must also specify the regions in which to update stack set instances.
        
          To update *all* the stack instances associated with this stack set, do not specify the ``Accounts`` or ``Regions`` properties.
        
          If the stack set update includes changes to the template (that is, if the ``TemplateBody`` or ``TemplateURL`` properties are specified), or the ``Parameters`` property, AWS CloudFormation marks all stack instances with a status of ``OUTDATED`` prior to updating the stack instances in the specified accounts and regions. If the stack set update does not include changes to the template or parameters, AWS CloudFormation updates the stack instances in the specified accounts and regions, while leaving all other stack instances with their existing stack instance status. 
        
          - *(string) --* 
        
        :type Regions: list
        :param Regions: 
        
          The regions in which to update associated stack instances. If you specify regions, you must also specify accounts in which to update stack set instances.
        
          To update *all* the stack instances associated with this stack set, do not specify the ``Accounts`` or ``Regions`` properties.
        
          If the stack set update includes changes to the template (that is, if the ``TemplateBody`` or ``TemplateURL`` properties are specified), or the ``Parameters`` property, AWS CloudFormation marks all stack instances with a status of ``OUTDATED`` prior to updating the stack instances in the specified accounts and regions. If the stack set update does not include changes to the template or parameters, AWS CloudFormation updates the stack instances in the specified accounts and regions, while leaving all other stack instances with their existing stack instance status. 
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **OperationId** *(string) --* 
        
              The unique ID for this stack set operation.
        
        """
        pass

    def update_termination_protection(self, EnableTerminationProtection: bool, StackName: str) -> Dict:
        """
        
        For `nested stacks <AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__ , termination protection is set on the root stack and cannot be changed directly on the nested stack.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/UpdateTerminationProtection>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_termination_protection(
              EnableTerminationProtection=True|False,
              StackName=\'string\'
          )
        :type EnableTerminationProtection: boolean
        :param EnableTerminationProtection: **[REQUIRED]** 
        
          Whether to enable termination protection on the specified stack.
        
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name or unique ID of the stack for which you want to set termination protection.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StackId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **StackId** *(string) --* 
        
              The unique ID of the stack.
        
        """
        pass

    def validate_template(self, TemplateBody: str = None, TemplateURL: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ValidateTemplate>`_
        
        **Request Syntax** 
        ::
        
          response = client.validate_template(
              TemplateBody=\'string\',
              TemplateURL=\'string\'
          )
        :type TemplateBody: string
        :param TemplateBody: 
        
          Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, go to `Template Anatomy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`__ in the AWS CloudFormation User Guide.
        
          Conditional: You must pass ``TemplateURL`` or ``TemplateBody`` . If both are passed, only ``TemplateBody`` is used.
        
        :type TemplateURL: string
        :param TemplateURL: 
        
          Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket. For more information, go to `Template Anatomy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`__ in the AWS CloudFormation User Guide.
        
          Conditional: You must pass ``TemplateURL`` or ``TemplateBody`` . If both are passed, only ``TemplateBody`` is used.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Parameters\': [
                    {
                        \'ParameterKey\': \'string\',
                        \'DefaultValue\': \'string\',
                        \'NoEcho\': True|False,
                        \'Description\': \'string\'
                    },
                ],
                \'Description\': \'string\',
                \'Capabilities\': [
                    \'CAPABILITY_IAM\'|\'CAPABILITY_NAMED_IAM\',
                ],
                \'CapabilitiesReason\': \'string\',
                \'DeclaredTransforms\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for  ValidateTemplate action.
        
            - **Parameters** *(list) --* 
        
              A list of ``TemplateParameter`` structures.
        
              - *(dict) --* 
        
                The TemplateParameter data type.
        
                - **ParameterKey** *(string) --* 
        
                  The name associated with the parameter.
        
                - **DefaultValue** *(string) --* 
        
                  The default value associated with the parameter.
        
                - **NoEcho** *(boolean) --* 
        
                  Flag indicating whether the parameter should be displayed as plain text in logs and UIs.
        
                - **Description** *(string) --* 
        
                  User defined description associated with the parameter.
        
            - **Description** *(string) --* 
        
              The description found within the template.
        
            - **Capabilities** *(list) --* 
        
              The capabilities found within the template. If your template contains IAM resources, you must specify the CAPABILITY_IAM or CAPABILITY_NAMED_IAM value for this parameter when you use the  CreateStack or  UpdateStack actions with your template; otherwise, those actions return an InsufficientCapabilities error.
        
              For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities>`__ .
        
              - *(string) --* 
          
            - **CapabilitiesReason** *(string) --* 
        
              The list of resources that generated the values in the ``Capabilities`` response element.
        
            - **DeclaredTransforms** *(list) --* 
        
              A list of the transforms that are declared in the template.
        
              - *(string) --* 
          
        """
        pass
