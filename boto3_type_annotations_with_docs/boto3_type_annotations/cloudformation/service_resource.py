from typing import Optional
from typing import Union
from typing import List
from boto3.resources.collection import ResourceCollection
from datetime import datetime
from typing import Dict
from boto3.resources import base


class ServiceResource(base.ServiceResource):
    stacks: 'stacks'

    def Event(self, id: str = None) -> 'Event':
        """
        Creates a Event resource.::
        
          event = cloudformation.Event(\'id\')
        
        :type id: string
        :param id: The Event\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`CloudFormation.Event`
        :returns: A Event resource
        """
        pass

    def Stack(self, name: str = None) -> 'Stack':
        """
        Creates a Stack resource.::
        
          stack = cloudformation.Stack(\'name\')
        
        :type name: string
        :param name: The Stack\'s name identifier. This **must** be set.
        
        :rtype: :py:class:`CloudFormation.Stack`
        :returns: A Stack resource
        """
        pass

    def StackResource(self, stack_name: str = None, logical_id: str = None) -> 'StackResource':
        """
        Creates a StackResource resource.::
        
          stack_resource = cloudformation.StackResource(\'stack_name\',\'logical_id\')
        
        :type stack_name: string
        :param stack_name: The StackResource\'s stack_name identifier. This **must** be set.
        :type logical_id: string
        :param logical_id: The StackResource\'s logical_id identifier. This **must** be set.
        
        :rtype: :py:class:`CloudFormation.StackResource`
        :returns: A StackResource resource
        """
        pass

    def StackResourceSummary(self, stack_name: str = None, logical_id: str = None) -> 'StackResourceSummary':
        """
        Creates a StackResourceSummary resource.::
        
          stack_resource_summary = cloudformation.StackResourceSummary(\'stack_name\',\'logical_id\')
        
        :type stack_name: string
        :param stack_name: The StackResourceSummary\'s stack_name identifier. This **must** be set.
        :type logical_id: string
        :param logical_id: The StackResourceSummary\'s logical_id identifier. This **must** be set.
        
        :rtype: :py:class:`CloudFormation.StackResourceSummary`
        :returns: A StackResourceSummary resource
        """
        pass

    def create_stack(self, StackName: str, TemplateBody: str = None, TemplateURL: str = None, Parameters: List = None, DisableRollback: bool = None, RollbackConfiguration: Dict = None, TimeoutInMinutes: int = None, NotificationARNs: List = None, Capabilities: List = None, ResourceTypes: List = None, RoleARN: str = None, OnFailure: str = None, StackPolicyBody: str = None, StackPolicyURL: str = None, Tags: List = None, ClientRequestToken: str = None, EnableTerminationProtection: bool = None) -> 'Stack':
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateStack>`_
        
        **Request Syntax** 
        ::
        
          stack = cloudformation.create_stack(
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
        
        :rtype: :py:class:`cloudformation.Stack`
        :returns: Stack resource
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass


class Event(base.ServiceResource):
    stack_id: str
    event_id: str
    stack_name: str
    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    timestamp: datetime
    resource_status: str
    resource_status_reason: str
    resource_properties: str
    client_request_token: str
    id: str

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass


class Stack(base.ServiceResource):
    stack_id: str
    stack_name: str
    change_set_id: str
    description: str
    parameters: List
    creation_time: datetime
    deletion_time: datetime
    last_updated_time: datetime
    rollback_configuration: Dict
    stack_status: str
    stack_status_reason: str
    disable_rollback: bool
    notification_arns: List
    timeout_in_minutes: int
    capabilities: List
    outputs: List
    role_arn: str
    tags: List
    enable_termination_protection: bool
    parent_id: str
    root_id: str
    drift_information: Dict
    name: str
    events: 'events'
    resource_summaries: 'resource_summaries'

    def cancel_update(self, ClientRequestToken: str = None):
        """
        
        .. note::
        
          You can cancel only stacks that are in the UPDATE_IN_PROGRESS state.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CancelUpdateStack>`_
        
        **Request Syntax** 
        ::
        
          response = stack.cancel_update(
              ClientRequestToken=\'string\'
          )
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          A unique identifier for this ``CancelUpdateStack`` request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you\'re not attempting to cancel an update on a stack with the same name. You might retry ``CancelUpdateStack`` requests to ensure that AWS CloudFormation successfully received them.
        
        :returns: None
        """
        pass

    def delete(self, RetainResources: List = None, RoleARN: str = None, ClientRequestToken: str = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DeleteStack>`_
        
        **Request Syntax** 
        ::
        
          response = stack.delete(
              RetainResources=[
                  \'string\',
              ],
              RoleARN=\'string\',
              ClientRequestToken=\'string\'
          )
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

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          stack.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          stack.load()
        :returns: None
        """
        pass

    def update(self, TemplateBody: str = None, TemplateURL: str = None, UsePreviousTemplate: bool = None, StackPolicyDuringUpdateBody: str = None, StackPolicyDuringUpdateURL: str = None, Parameters: List = None, Capabilities: List = None, ResourceTypes: List = None, RoleARN: str = None, RollbackConfiguration: Dict = None, StackPolicyBody: str = None, StackPolicyURL: str = None, NotificationARNs: List = None, Tags: List = None, ClientRequestToken: str = None) -> Dict:
        """
        
        To get a copy of the template for an existing stack, you can use the  GetTemplate action.
        
        For more information about creating an update template, updating a stack, and monitoring the progress of the update, see `Updating a Stack <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/UpdateStack>`_
        
        **Request Syntax** 
        ::
        
          response = stack.update(
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


class StackResource(base.ServiceResource):
    stack_id: str
    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    last_updated_timestamp: datetime
    resource_status: str
    resource_status_reason: str
    description: str
    metadata: str
    drift_information: Dict
    stack_name: str
    logical_id: str

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          stack_resource.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          stack_resource.load()
        :returns: None
        """
        pass


class StackResourceSummary(base.ServiceResource):
    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    last_updated_timestamp: datetime
    resource_status: str
    resource_status_reason: str
    drift_information: Dict
    stack_name: str
    logical_id: str

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass


class stacks(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Stack']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStacks>`_
        
        **Request Syntax** 
        ::
        
          stack_iterator = cloudformation.stacks.all()
          
        :rtype: list(:py:class:`cloudformation.Stack`)
        :returns: A list of Stack resources
        """
        pass

    
    @classmethod
    def filter(cls, StackName: str = None, NextToken: str = None) -> List['Stack']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStacks>`_
        
        **Request Syntax** 
        ::
        
          stack_iterator = cloudformation.stacks.filter(
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
        
        :rtype: list(:py:class:`cloudformation.Stack`)
        :returns: A list of Stack resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Stack']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStacks>`_
        
        **Request Syntax** 
        ::
        
          stack_iterator = cloudformation.stacks.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`cloudformation.Stack`)
        :returns: A list of Stack resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Stack']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStacks>`_
        
        **Request Syntax** 
        ::
        
          stack_iterator = cloudformation.stacks.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`cloudformation.Stack`)
        :returns: A list of Stack resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass
