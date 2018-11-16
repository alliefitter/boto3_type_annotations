from datetime import datetime
from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def add_tags_to_resource(self, ResourceType: str, ResourceId: str, Tags: List) -> Dict:
        """
        
        Each resource can have a maximum of 50 tags. 
        
        We recommend that you devise a set of tag keys that meets your needs for each resource type. Using a consistent set of tag keys makes it easier for you to manage your resources. You can search and filter the resources based on the tags you add. Tags don\'t have any semantic meaning to Amazon EC2 and are interpreted strictly as a string of characters. 
        
        For more information about tags, see `Tagging Your Amazon EC2 Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon EC2 User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/AddTagsToResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.add_tags_to_resource(
              ResourceType=\'Document\'|\'ManagedInstance\'|\'MaintenanceWindow\'|\'Parameter\'|\'PatchBaseline\',
              ResourceId=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type ResourceType: string
        :param ResourceType: **[REQUIRED]** 
        
          Specifies the type of resource you are tagging.
        
          .. note::
        
            The ManagedInstance type for this API action is for on-premises managed instances. You must specify the the name of the managed instance in the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.
        
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          The resource ID you want to tag.
        
          Use the ID of the resource. Here are some examples:
        
          ManagedInstance: mi-012345abcde
        
          MaintenanceWindow: mw-012345abcde
        
          PatchBaseline: pb-012345abcde
        
          For the Document and Parameter values, use the name of the resource.
        
          .. note::
        
            The ManagedInstance type for this API action is only for on-premises managed instances. You must specify the the name of the managed instance in the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          One or more tags. The value parameter is required, but if you don\'t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. 
        
          .. warning::
        
            Do not enter personally identifiable information in this field.
        
          - *(dict) --* 
        
            Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, Maintenance Windows, Parameter Store parameters, and patch baselines.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The name of the tag.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The value of the tag.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

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

    def cancel_command(self, CommandId: str, InstanceIds: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CancelCommand>`_
        
        **Request Syntax** 
        ::
        
          response = client.cancel_command(
              CommandId=\'string\',
              InstanceIds=[
                  \'string\',
              ]
          )
        :type CommandId: string
        :param CommandId: **[REQUIRED]** 
        
          The ID of the command you want to cancel.
        
        :type InstanceIds: list
        :param InstanceIds: 
        
          (Optional) A list of instance IDs on which you want to cancel the command. If not provided, the command is canceled on every instance on which it was requested.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Whether or not the command was successfully canceled. There is no guarantee that a request can be canceled.
        
        """
        pass

    def cancel_maintenance_window_execution(self, WindowExecutionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CancelMaintenanceWindowExecution>`_
        
        **Request Syntax** 
        ::
        
          response = client.cancel_maintenance_window_execution(
              WindowExecutionId=\'string\'
          )
        :type WindowExecutionId: string
        :param WindowExecutionId: **[REQUIRED]** 
        
          The ID of the Maintenance Window execution to stop.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowExecutionId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **WindowExecutionId** *(string) --* 
        
              The ID of the Maintenance Window execution that has been stopped.
        
        """
        pass

    def create_activation(self, IamRole: str, Description: str = None, DefaultInstanceName: str = None, RegistrationLimit: int = None, ExpirationDate: datetime = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CreateActivation>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_activation(
              Description=\'string\',
              DefaultInstanceName=\'string\',
              IamRole=\'string\',
              RegistrationLimit=123,
              ExpirationDate=datetime(2015, 1, 1)
          )
        :type Description: string
        :param Description: 
        
          A user-defined description of the resource that you want to register with Amazon EC2. 
        
          .. warning::
        
            Do not enter personally identifiable information in this field.
        
        :type DefaultInstanceName: string
        :param DefaultInstanceName: 
        
          The name of the registered, managed instance as it will appear in the Amazon EC2 console or when you use the AWS command line tools to list EC2 resources.
        
          .. warning::
        
            Do not enter personally identifiable information in this field.
        
        :type IamRole: string
        :param IamRole: **[REQUIRED]** 
        
          The Amazon Identity and Access Management (IAM) role that you want to assign to the managed instance. 
        
        :type RegistrationLimit: integer
        :param RegistrationLimit: 
        
          Specify the maximum number of managed instances you want to register. The default value is 1 instance.
        
        :type ExpirationDate: datetime
        :param ExpirationDate: 
        
          The date by which this activation request should expire. The default value is 24 hours.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ActivationId\': \'string\',
                \'ActivationCode\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ActivationId** *(string) --* 
        
              The ID number generated by the system when it processed the activation. The activation ID functions like a user name.
        
            - **ActivationCode** *(string) --* 
        
              The code the system generates when it processes the activation. The activation code functions like a password to validate the activation ID. 
        
        """
        pass

    def create_association(self, Name: str, DocumentVersion: str = None, InstanceId: str = None, Parameters: Dict = None, Targets: List = None, ScheduleExpression: str = None, OutputLocation: Dict = None, AssociationName: str = None, MaxErrors: str = None, MaxConcurrency: str = None, ComplianceSeverity: str = None) -> Dict:
        """
        
        When you associate a document with one or more instances using instance IDs or tags, SSM Agent running on the instance processes the document and configures the instance as specified.
        
        If you associate a document with an instance that already has an associated document, the system throws the AssociationAlreadyExists exception.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CreateAssociation>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_association(
              Name=\'string\',
              DocumentVersion=\'string\',
              InstanceId=\'string\',
              Parameters={
                  \'string\': [
                      \'string\',
                  ]
              },
              Targets=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              ScheduleExpression=\'string\',
              OutputLocation={
                  \'S3Location\': {
                      \'OutputS3Region\': \'string\',
                      \'OutputS3BucketName\': \'string\',
                      \'OutputS3KeyPrefix\': \'string\'
                  }
              },
              AssociationName=\'string\',
              MaxErrors=\'string\',
              MaxConcurrency=\'string\',
              ComplianceSeverity=\'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'UNSPECIFIED\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the Systems Manager document.
        
        :type DocumentVersion: string
        :param DocumentVersion: 
        
          The document version you want to associate with the target(s). Can be a specific version or the default version.
        
        :type InstanceId: string
        :param InstanceId: 
        
          The instance ID.
        
        :type Parameters: dict
        :param Parameters: 
        
          The parameters for the documents runtime configuration. 
        
          - *(string) --* 
        
            - *(list) --* 
        
              - *(string) --* 
        
        :type Targets: list
        :param Targets: 
        
          The targets (either instances or tags) for the association.
        
          - *(dict) --* 
        
            An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
            - **Key** *(string) --* 
        
              User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
            - **Values** *(list) --* 
        
              User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
              - *(string) --* 
        
        :type ScheduleExpression: string
        :param ScheduleExpression: 
        
          A cron expression when the association will be applied to the target(s).
        
        :type OutputLocation: dict
        :param OutputLocation: 
        
          An Amazon S3 bucket where you want to store the output details of the request.
        
          - **S3Location** *(dict) --* 
        
            An Amazon S3 bucket where you want to store the results of this request.
        
            - **OutputS3Region** *(string) --* 
        
              (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
        
            - **OutputS3BucketName** *(string) --* 
        
              The name of the Amazon S3 bucket.
        
            - **OutputS3KeyPrefix** *(string) --* 
        
              The Amazon S3 bucket subfolder.
        
        :type AssociationName: string
        :param AssociationName: 
        
          Specify a descriptive name for the association.
        
        :type MaxErrors: string
        :param MaxErrors: 
        
          The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.
        
          Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.
        
        :type MaxConcurrency: string
        :param MaxConcurrency: 
        
          The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
        
          If a new instance starts and attempts to execute an association while Systems Manager is executing MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.
        
        :type ComplianceSeverity: string
        :param ComplianceSeverity: 
        
          The severity level to assign to the association.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AssociationDescription\': {
                    \'Name\': \'string\',
                    \'InstanceId\': \'string\',
                    \'AssociationVersion\': \'string\',
                    \'Date\': datetime(2015, 1, 1),
                    \'LastUpdateAssociationDate\': datetime(2015, 1, 1),
                    \'Status\': {
                        \'Date\': datetime(2015, 1, 1),
                        \'Name\': \'Pending\'|\'Success\'|\'Failed\',
                        \'Message\': \'string\',
                        \'AdditionalInfo\': \'string\'
                    },
                    \'Overview\': {
                        \'Status\': \'string\',
                        \'DetailedStatus\': \'string\',
                        \'AssociationStatusAggregatedCount\': {
                            \'string\': 123
                        }
                    },
                    \'DocumentVersion\': \'string\',
                    \'Parameters\': {
                        \'string\': [
                            \'string\',
                        ]
                    },
                    \'AssociationId\': \'string\',
                    \'Targets\': [
                        {
                            \'Key\': \'string\',
                            \'Values\': [
                                \'string\',
                            ]
                        },
                    ],
                    \'ScheduleExpression\': \'string\',
                    \'OutputLocation\': {
                        \'S3Location\': {
                            \'OutputS3Region\': \'string\',
                            \'OutputS3BucketName\': \'string\',
                            \'OutputS3KeyPrefix\': \'string\'
                        }
                    },
                    \'LastExecutionDate\': datetime(2015, 1, 1),
                    \'LastSuccessfulExecutionDate\': datetime(2015, 1, 1),
                    \'AssociationName\': \'string\',
                    \'MaxErrors\': \'string\',
                    \'MaxConcurrency\': \'string\',
                    \'ComplianceSeverity\': \'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'UNSPECIFIED\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AssociationDescription** *(dict) --* 
        
              Information about the association.
        
              - **Name** *(string) --* 
        
                The name of the Systems Manager document.
        
              - **InstanceId** *(string) --* 
        
                The ID of the instance.
        
              - **AssociationVersion** *(string) --* 
        
                The association version.
        
              - **Date** *(datetime) --* 
        
                The date when the association was made.
        
              - **LastUpdateAssociationDate** *(datetime) --* 
        
                The date when the association was last updated.
        
              - **Status** *(dict) --* 
        
                The association status.
        
                - **Date** *(datetime) --* 
        
                  The date when the status changed.
        
                - **Name** *(string) --* 
        
                  The status.
        
                - **Message** *(string) --* 
        
                  The reason for the status.
        
                - **AdditionalInfo** *(string) --* 
        
                  A user-defined string.
        
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
              
              - **DocumentVersion** *(string) --* 
        
                The document version.
        
              - **Parameters** *(dict) --* 
        
                A description of the parameters for a document. 
        
                - *(string) --* 
                  
                  - *(list) --* 
                    
                    - *(string) --* 
                
              - **AssociationId** *(string) --* 
        
                The association ID.
        
              - **Targets** *(list) --* 
        
                The instances targeted by the request. 
        
                - *(dict) --* 
        
                  An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                  - **Key** *(string) --* 
        
                    User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                  - **Values** *(list) --* 
        
                    User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
                    - *(string) --* 
                
              - **ScheduleExpression** *(string) --* 
        
                A cron expression that specifies a schedule when the association runs.
        
              - **OutputLocation** *(dict) --* 
        
                An Amazon S3 bucket where you want to store the output details of the request.
        
                - **S3Location** *(dict) --* 
        
                  An Amazon S3 bucket where you want to store the results of this request.
        
                  - **OutputS3Region** *(string) --* 
        
                    (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
        
                  - **OutputS3BucketName** *(string) --* 
        
                    The name of the Amazon S3 bucket.
        
                  - **OutputS3KeyPrefix** *(string) --* 
        
                    The Amazon S3 bucket subfolder.
        
              - **LastExecutionDate** *(datetime) --* 
        
                The date on which the association was last run.
        
              - **LastSuccessfulExecutionDate** *(datetime) --* 
        
                The last date on which the association was successfully run.
        
              - **AssociationName** *(string) --* 
        
                The association name.
        
              - **MaxErrors** *(string) --* 
        
                The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.
        
                Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.
        
              - **MaxConcurrency** *(string) --* 
        
                The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
        
                If a new instance starts and attempts to execute an association while Systems Manager is executing MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.
        
              - **ComplianceSeverity** *(string) --* 
        
                The severity level that is assigned to the association.
        
        """
        pass

    def create_association_batch(self, Entries: List) -> Dict:
        """
        
        When you associate a document with one or more instances using instance IDs or tags, SSM Agent running on the instance processes the document and configures the instance as specified.
        
        If you associate a document with an instance that already has an associated document, the system throws the AssociationAlreadyExists exception.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CreateAssociationBatch>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_association_batch(
              Entries=[
                  {
                      \'Name\': \'string\',
                      \'InstanceId\': \'string\',
                      \'Parameters\': {
                          \'string\': [
                              \'string\',
                          ]
                      },
                      \'DocumentVersion\': \'string\',
                      \'Targets\': [
                          {
                              \'Key\': \'string\',
                              \'Values\': [
                                  \'string\',
                              ]
                          },
                      ],
                      \'ScheduleExpression\': \'string\',
                      \'OutputLocation\': {
                          \'S3Location\': {
                              \'OutputS3Region\': \'string\',
                              \'OutputS3BucketName\': \'string\',
                              \'OutputS3KeyPrefix\': \'string\'
                          }
                      },
                      \'AssociationName\': \'string\',
                      \'MaxErrors\': \'string\',
                      \'MaxConcurrency\': \'string\',
                      \'ComplianceSeverity\': \'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'UNSPECIFIED\'
                  },
              ]
          )
        :type Entries: list
        :param Entries: **[REQUIRED]** 
        
          One or more associations.
        
          - *(dict) --* 
        
            Describes the association of a Systems Manager document and an instance.
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the configuration document. 
        
            - **InstanceId** *(string) --* 
        
              The ID of the instance. 
        
            - **Parameters** *(dict) --* 
        
              A description of the parameters for a document. 
        
              - *(string) --* 
        
                - *(list) --* 
        
                  - *(string) --* 
        
            - **DocumentVersion** *(string) --* 
        
              The document version.
        
            - **Targets** *(list) --* 
        
              The instances targeted by the request.
        
              - *(dict) --* 
        
                An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                - **Key** *(string) --* 
        
                  User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                - **Values** *(list) --* 
        
                  User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
                  - *(string) --* 
        
            - **ScheduleExpression** *(string) --* 
        
              A cron expression that specifies a schedule when the association runs.
        
            - **OutputLocation** *(dict) --* 
        
              An Amazon S3 bucket where you want to store the results of this request.
        
              - **S3Location** *(dict) --* 
        
                An Amazon S3 bucket where you want to store the results of this request.
        
                - **OutputS3Region** *(string) --* 
        
                  (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
        
                - **OutputS3BucketName** *(string) --* 
        
                  The name of the Amazon S3 bucket.
        
                - **OutputS3KeyPrefix** *(string) --* 
        
                  The Amazon S3 bucket subfolder.
        
            - **AssociationName** *(string) --* 
        
              Specify a descriptive name for the association.
        
            - **MaxErrors** *(string) --* 
        
              The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.
        
              Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.
        
            - **MaxConcurrency** *(string) --* 
        
              The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
        
              If a new instance starts and attempts to execute an association while Systems Manager is executing MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.
        
            - **ComplianceSeverity** *(string) --* 
        
              The severity level to assign to the association.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Successful\': [
                    {
                        \'Name\': \'string\',
                        \'InstanceId\': \'string\',
                        \'AssociationVersion\': \'string\',
                        \'Date\': datetime(2015, 1, 1),
                        \'LastUpdateAssociationDate\': datetime(2015, 1, 1),
                        \'Status\': {
                            \'Date\': datetime(2015, 1, 1),
                            \'Name\': \'Pending\'|\'Success\'|\'Failed\',
                            \'Message\': \'string\',
                            \'AdditionalInfo\': \'string\'
                        },
                        \'Overview\': {
                            \'Status\': \'string\',
                            \'DetailedStatus\': \'string\',
                            \'AssociationStatusAggregatedCount\': {
                                \'string\': 123
                            }
                        },
                        \'DocumentVersion\': \'string\',
                        \'Parameters\': {
                            \'string\': [
                                \'string\',
                            ]
                        },
                        \'AssociationId\': \'string\',
                        \'Targets\': [
                            {
                                \'Key\': \'string\',
                                \'Values\': [
                                    \'string\',
                                ]
                            },
                        ],
                        \'ScheduleExpression\': \'string\',
                        \'OutputLocation\': {
                            \'S3Location\': {
                                \'OutputS3Region\': \'string\',
                                \'OutputS3BucketName\': \'string\',
                                \'OutputS3KeyPrefix\': \'string\'
                            }
                        },
                        \'LastExecutionDate\': datetime(2015, 1, 1),
                        \'LastSuccessfulExecutionDate\': datetime(2015, 1, 1),
                        \'AssociationName\': \'string\',
                        \'MaxErrors\': \'string\',
                        \'MaxConcurrency\': \'string\',
                        \'ComplianceSeverity\': \'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'UNSPECIFIED\'
                    },
                ],
                \'Failed\': [
                    {
                        \'Entry\': {
                            \'Name\': \'string\',
                            \'InstanceId\': \'string\',
                            \'Parameters\': {
                                \'string\': [
                                    \'string\',
                                ]
                            },
                            \'DocumentVersion\': \'string\',
                            \'Targets\': [
                                {
                                    \'Key\': \'string\',
                                    \'Values\': [
                                        \'string\',
                                    ]
                                },
                            ],
                            \'ScheduleExpression\': \'string\',
                            \'OutputLocation\': {
                                \'S3Location\': {
                                    \'OutputS3Region\': \'string\',
                                    \'OutputS3BucketName\': \'string\',
                                    \'OutputS3KeyPrefix\': \'string\'
                                }
                            },
                            \'AssociationName\': \'string\',
                            \'MaxErrors\': \'string\',
                            \'MaxConcurrency\': \'string\',
                            \'ComplianceSeverity\': \'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'UNSPECIFIED\'
                        },
                        \'Message\': \'string\',
                        \'Fault\': \'Client\'|\'Server\'|\'Unknown\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Successful** *(list) --* 
        
              Information about the associations that succeeded.
        
              - *(dict) --* 
        
                Describes the parameters for a document.
        
                - **Name** *(string) --* 
        
                  The name of the Systems Manager document.
        
                - **InstanceId** *(string) --* 
        
                  The ID of the instance.
        
                - **AssociationVersion** *(string) --* 
        
                  The association version.
        
                - **Date** *(datetime) --* 
        
                  The date when the association was made.
        
                - **LastUpdateAssociationDate** *(datetime) --* 
        
                  The date when the association was last updated.
        
                - **Status** *(dict) --* 
        
                  The association status.
        
                  - **Date** *(datetime) --* 
        
                    The date when the status changed.
        
                  - **Name** *(string) --* 
        
                    The status.
        
                  - **Message** *(string) --* 
        
                    The reason for the status.
        
                  - **AdditionalInfo** *(string) --* 
        
                    A user-defined string.
        
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
                
                - **DocumentVersion** *(string) --* 
        
                  The document version.
        
                - **Parameters** *(dict) --* 
        
                  A description of the parameters for a document. 
        
                  - *(string) --* 
                    
                    - *(list) --* 
                      
                      - *(string) --* 
                  
                - **AssociationId** *(string) --* 
        
                  The association ID.
        
                - **Targets** *(list) --* 
        
                  The instances targeted by the request. 
        
                  - *(dict) --* 
        
                    An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                    - **Key** *(string) --* 
        
                      User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                    - **Values** *(list) --* 
        
                      User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
                      - *(string) --* 
                  
                - **ScheduleExpression** *(string) --* 
        
                  A cron expression that specifies a schedule when the association runs.
        
                - **OutputLocation** *(dict) --* 
        
                  An Amazon S3 bucket where you want to store the output details of the request.
        
                  - **S3Location** *(dict) --* 
        
                    An Amazon S3 bucket where you want to store the results of this request.
        
                    - **OutputS3Region** *(string) --* 
        
                      (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
        
                    - **OutputS3BucketName** *(string) --* 
        
                      The name of the Amazon S3 bucket.
        
                    - **OutputS3KeyPrefix** *(string) --* 
        
                      The Amazon S3 bucket subfolder.
        
                - **LastExecutionDate** *(datetime) --* 
        
                  The date on which the association was last run.
        
                - **LastSuccessfulExecutionDate** *(datetime) --* 
        
                  The last date on which the association was successfully run.
        
                - **AssociationName** *(string) --* 
        
                  The association name.
        
                - **MaxErrors** *(string) --* 
        
                  The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.
        
                  Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.
        
                - **MaxConcurrency** *(string) --* 
        
                  The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
        
                  If a new instance starts and attempts to execute an association while Systems Manager is executing MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.
        
                - **ComplianceSeverity** *(string) --* 
        
                  The severity level that is assigned to the association.
        
            - **Failed** *(list) --* 
        
              Information about the associations that failed.
        
              - *(dict) --* 
        
                Describes a failed association.
        
                - **Entry** *(dict) --* 
        
                  The association.
        
                  - **Name** *(string) --* 
        
                    The name of the configuration document. 
        
                  - **InstanceId** *(string) --* 
        
                    The ID of the instance. 
        
                  - **Parameters** *(dict) --* 
        
                    A description of the parameters for a document. 
        
                    - *(string) --* 
                      
                      - *(list) --* 
                        
                        - *(string) --* 
                    
                  - **DocumentVersion** *(string) --* 
        
                    The document version.
        
                  - **Targets** *(list) --* 
        
                    The instances targeted by the request.
        
                    - *(dict) --* 
        
                      An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                      - **Key** *(string) --* 
        
                        User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                      - **Values** *(list) --* 
        
                        User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
                        - *(string) --* 
                    
                  - **ScheduleExpression** *(string) --* 
        
                    A cron expression that specifies a schedule when the association runs.
        
                  - **OutputLocation** *(dict) --* 
        
                    An Amazon S3 bucket where you want to store the results of this request.
        
                    - **S3Location** *(dict) --* 
        
                      An Amazon S3 bucket where you want to store the results of this request.
        
                      - **OutputS3Region** *(string) --* 
        
                        (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
        
                      - **OutputS3BucketName** *(string) --* 
        
                        The name of the Amazon S3 bucket.
        
                      - **OutputS3KeyPrefix** *(string) --* 
        
                        The Amazon S3 bucket subfolder.
        
                  - **AssociationName** *(string) --* 
        
                    Specify a descriptive name for the association.
        
                  - **MaxErrors** *(string) --* 
        
                    The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.
        
                    Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.
        
                  - **MaxConcurrency** *(string) --* 
        
                    The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
        
                    If a new instance starts and attempts to execute an association while Systems Manager is executing MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.
        
                  - **ComplianceSeverity** *(string) --* 
        
                    The severity level to assign to the association.
        
                - **Message** *(string) --* 
        
                  A description of the failure.
        
                - **Fault** *(string) --* 
        
                  The source of the failure.
        
        """
        pass

    def create_document(self, Content: str, Name: str, DocumentType: str = None, DocumentFormat: str = None, TargetType: str = None) -> Dict:
        """
        
        After you create a document, you can use CreateAssociation to associate it with one or more running instances.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CreateDocument>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_document(
              Content=\'string\',
              Name=\'string\',
              DocumentType=\'Command\'|\'Policy\'|\'Automation\'|\'Session\',
              DocumentFormat=\'YAML\'|\'JSON\',
              TargetType=\'string\'
          )
        :type Content: string
        :param Content: **[REQUIRED]** 
        
          A valid JSON or YAML string.
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          A name for the Systems Manager document.
        
          .. warning::
        
            Do not use the following to begin the names of documents you create. They are reserved by AWS for use as document prefixes:
        
            * ``aws``   
             
            * ``amazon``   
             
            * ``amzn``   
             
        :type DocumentType: string
        :param DocumentType: 
        
          The type of document to create. Valid document types include: Policy, Automation, and Command.
        
        :type DocumentFormat: string
        :param DocumentFormat: 
        
          Specify the document format for the request. The document format can be either JSON or YAML. JSON is the default format.
        
        :type TargetType: string
        :param TargetType: 
        
          Specify a target type to define the kinds of resources the document can run on. For example, to run a document on EC2 instances, specify the following value: /AWS::EC2::Instance. If you specify a value of \'/\' the document can run on all types of resources. If you don\'t specify a value, the document can\'t run on any resources. For a list of valid resource types, see `AWS Resource Types Reference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`__ in the *AWS CloudFormation User Guide* . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DocumentDescription\': {
                    \'Sha1\': \'string\',
                    \'Hash\': \'string\',
                    \'HashType\': \'Sha256\'|\'Sha1\',
                    \'Name\': \'string\',
                    \'Owner\': \'string\',
                    \'CreatedDate\': datetime(2015, 1, 1),
                    \'Status\': \'Creating\'|\'Active\'|\'Updating\'|\'Deleting\',
                    \'DocumentVersion\': \'string\',
                    \'Description\': \'string\',
                    \'Parameters\': [
                        {
                            \'Name\': \'string\',
                            \'Type\': \'String\'|\'StringList\',
                            \'Description\': \'string\',
                            \'DefaultValue\': \'string\'
                        },
                    ],
                    \'PlatformTypes\': [
                        \'Windows\'|\'Linux\',
                    ],
                    \'DocumentType\': \'Command\'|\'Policy\'|\'Automation\'|\'Session\',
                    \'SchemaVersion\': \'string\',
                    \'LatestVersion\': \'string\',
                    \'DefaultVersion\': \'string\',
                    \'DocumentFormat\': \'YAML\'|\'JSON\',
                    \'TargetType\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DocumentDescription** *(dict) --* 
        
              Information about the Systems Manager document.
        
              - **Sha1** *(string) --* 
        
                The SHA1 hash of the document, which you can use for verification.
        
              - **Hash** *(string) --* 
        
                The Sha256 or Sha1 hash created by the system when the document was created. 
        
                .. note::
        
                  Sha1 hashes have been deprecated.
        
              - **HashType** *(string) --* 
        
                Sha256 or Sha1.
        
                .. note::
        
                  Sha1 hashes have been deprecated.
        
              - **Name** *(string) --* 
        
                The name of the Systems Manager document.
        
              - **Owner** *(string) --* 
        
                The AWS user account that created the document.
        
              - **CreatedDate** *(datetime) --* 
        
                The date when the document was created.
        
              - **Status** *(string) --* 
        
                The status of the Systems Manager document.
        
              - **DocumentVersion** *(string) --* 
        
                The document version.
        
              - **Description** *(string) --* 
        
                A description of the document. 
        
              - **Parameters** *(list) --* 
        
                A description of the parameters for a document.
        
                - *(dict) --* 
        
                  Parameters specified in a System Manager document that execute on the server when the command is run. 
        
                  - **Name** *(string) --* 
        
                    The name of the parameter.
        
                  - **Type** *(string) --* 
        
                    The type of parameter. The type can be either String or StringList.
        
                  - **Description** *(string) --* 
        
                    A description of what the parameter does, how to use it, the default value, and whether or not the parameter is optional.
        
                  - **DefaultValue** *(string) --* 
        
                    If specified, the default values for the parameters. Parameters without a default value are required. Parameters with a default value are optional.
        
              - **PlatformTypes** *(list) --* 
        
                The list of OS platforms compatible with this Systems Manager document. 
        
                - *(string) --* 
            
              - **DocumentType** *(string) --* 
        
                The type of document. 
        
              - **SchemaVersion** *(string) --* 
        
                The schema version.
        
              - **LatestVersion** *(string) --* 
        
                The latest version of the document.
        
              - **DefaultVersion** *(string) --* 
        
                The default version.
        
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
        
        """
        pass

    def create_maintenance_window(self, Name: str, Schedule: str, Duration: int, Cutoff: int, AllowUnassociatedTargets: bool, Description: str = None, StartDate: str = None, EndDate: str = None, ScheduleTimezone: str = None, ClientToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CreateMaintenanceWindow>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_maintenance_window(
              Name=\'string\',
              Description=\'string\',
              StartDate=\'string\',
              EndDate=\'string\',
              Schedule=\'string\',
              ScheduleTimezone=\'string\',
              Duration=123,
              Cutoff=123,
              AllowUnassociatedTargets=True|False,
              ClientToken=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the Maintenance Window.
        
        :type Description: string
        :param Description: 
        
          An optional description for the Maintenance Window. We recommend specifying a description to help you organize your Maintenance Windows. 
        
        :type StartDate: string
        :param StartDate: 
        
          The date and time, in ISO-8601 Extended format, for when you want the Maintenance Window to become active. StartDate allows you to delay activation of the Maintenance Window until the specified future date.
        
        :type EndDate: string
        :param EndDate: 
        
          The date and time, in ISO-8601 Extended format, for when you want the Maintenance Window to become inactive. EndDate allows you to set a date and time in the future when the Maintenance Window will no longer run.
        
        :type Schedule: string
        :param Schedule: **[REQUIRED]** 
        
          The schedule of the Maintenance Window in the form of a cron or rate expression.
        
        :type ScheduleTimezone: string
        :param ScheduleTimezone: 
        
          The time zone that the scheduled Maintenance Window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: \"America/Los_Angeles\", \"etc/UTC\", or \"Asia/Seoul\". For more information, see the `Time Zone Database <https://www.iana.org/time-zones>`__ on the IANA website.
        
        :type Duration: integer
        :param Duration: **[REQUIRED]** 
        
          The duration of the Maintenance Window in hours.
        
        :type Cutoff: integer
        :param Cutoff: **[REQUIRED]** 
        
          The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.
        
        :type AllowUnassociatedTargets: boolean
        :param AllowUnassociatedTargets: **[REQUIRED]** 
        
          Enables a Maintenance Window task to execute on managed instances, even if you have not registered those instances as targets. If enabled, then you must specify the unregistered instances (by instance ID) when you register a task with the Maintenance Window 
        
          If you don\'t enable this option, then you must specify previously-registered targets when you register a task with the Maintenance Window. 
        
        :type ClientToken: string
        :param ClientToken: 
        
          User-provided idempotency token.
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **WindowId** *(string) --* 
        
              The ID of the created Maintenance Window.
        
        """
        pass

    def create_patch_baseline(self, Name: str, OperatingSystem: str = None, GlobalFilters: Dict = None, ApprovalRules: Dict = None, ApprovedPatches: List = None, ApprovedPatchesComplianceLevel: str = None, ApprovedPatchesEnableNonSecurity: bool = None, RejectedPatches: List = None, RejectedPatchesAction: str = None, Description: str = None, Sources: List = None, ClientToken: str = None) -> Dict:
        """
        
        .. note::
        
          For information about valid key and value pairs in ``PatchFilters`` for each supported operating system type, see `PatchFilter <http://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CreatePatchBaseline>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_patch_baseline(
              OperatingSystem=\'WINDOWS\'|\'AMAZON_LINUX\'|\'AMAZON_LINUX_2\'|\'UBUNTU\'|\'REDHAT_ENTERPRISE_LINUX\'|\'SUSE\'|\'CENTOS\',
              Name=\'string\',
              GlobalFilters={
                  \'PatchFilters\': [
                      {
                          \'Key\': \'PRODUCT\'|\'CLASSIFICATION\'|\'MSRC_SEVERITY\'|\'PATCH_ID\'|\'SECTION\'|\'PRIORITY\'|\'SEVERITY\',
                          \'Values\': [
                              \'string\',
                          ]
                      },
                  ]
              },
              ApprovalRules={
                  \'PatchRules\': [
                      {
                          \'PatchFilterGroup\': {
                              \'PatchFilters\': [
                                  {
                                      \'Key\': \'PRODUCT\'|\'CLASSIFICATION\'|\'MSRC_SEVERITY\'|\'PATCH_ID\'|\'SECTION\'|\'PRIORITY\'|\'SEVERITY\',
                                      \'Values\': [
                                          \'string\',
                                      ]
                                  },
                              ]
                          },
                          \'ComplianceLevel\': \'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'INFORMATIONAL\'|\'UNSPECIFIED\',
                          \'ApproveAfterDays\': 123,
                          \'EnableNonSecurity\': True|False
                      },
                  ]
              },
              ApprovedPatches=[
                  \'string\',
              ],
              ApprovedPatchesComplianceLevel=\'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'INFORMATIONAL\'|\'UNSPECIFIED\',
              ApprovedPatchesEnableNonSecurity=True|False,
              RejectedPatches=[
                  \'string\',
              ],
              RejectedPatchesAction=\'ALLOW_AS_DEPENDENCY\'|\'BLOCK\',
              Description=\'string\',
              Sources=[
                  {
                      \'Name\': \'string\',
                      \'Products\': [
                          \'string\',
                      ],
                      \'Configuration\': \'string\'
                  },
              ],
              ClientToken=\'string\'
          )
        :type OperatingSystem: string
        :param OperatingSystem: 
        
          Defines the operating system the patch baseline applies to. The Default value is WINDOWS.
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the patch baseline.
        
        :type GlobalFilters: dict
        :param GlobalFilters: 
        
          A set of global filters used to exclude patches from the baseline.
        
          - **PatchFilters** *(list) --* **[REQUIRED]** 
        
            The set of patch filters that make up the group.
        
            - *(dict) --* 
        
              Defines a patch filter.
        
              A patch filter consists of key/value pairs, but not all keys are valid for all operating system types. For example, the key ``PRODUCT`` is valid for all supported operating system types. The key ``MSRC_SEVERITY`` , however, is valid only for Windows operating systems, and the key ``SECTION`` is valid only for Ubuntu operating systems.
        
              Refer to the following sections for information about which keys may be used with each major operating system, and which values are valid for each key.
        
               **Windows Operating Systems**  
        
              The supported keys for Windows operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``MSRC_SEVERITY`` . See the following lists for valid values for each of these keys.
        
               *Supported key:*  ``PRODUCT``  
        
               *Supported values:*  
        
              * ``Windows7``   
               
              * ``Windows8``   
               
              * ``Windows8.1``   
               
              * ``Windows8Embedded``   
               
              * ``Windows10``   
               
              * ``Windows10LTSB``   
               
              * ``WindowsServer2008``   
               
              * ``WindowsServer2008R2``   
               
              * ``WindowsServer2012``   
               
              * ``WindowsServer2012R2``   
               
              * ``WindowsServer2016``   
               
              * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
               
               *Supported key:*  ``CLASSIFICATION``  
        
               *Supported values:*  
        
              * ``CriticalUpdates``   
               
              * ``DefinitionUpdates``   
               
              * ``Drivers``   
               
              * ``FeaturePacks``   
               
              * ``SecurityUpdates``   
               
              * ``ServicePacks``   
               
              * ``Tools``   
               
              * ``UpdateRollups``   
               
              * ``Updates``   
               
              * ``Upgrades``   
               
               *Supported key:*  ``MSRC_SEVERITY``  
        
               *Supported values:*  
        
              * ``Critical``   
               
              * ``Important``   
               
              * ``Moderate``   
               
              * ``Low``   
               
              * ``Unspecified``   
               
               **Ubuntu Operating Systems**  
        
              The supported keys for Ubuntu operating systems are ``PRODUCT`` , ``PRIORITY`` , and ``SECTION`` . See the following lists for valid values for each of these keys.
        
               *Supported key:*  ``PRODUCT``  
        
               *Supported values:*  
        
              * ``Ubuntu14.04``   
               
              * ``Ubuntu16.04``   
               
              * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
               
               *Supported key:*  ``PRIORITY``  
        
               *Supported values:*  
        
              * ``Required``   
               
              * ``Important``   
               
              * ``Standard``   
               
              * ``Optional``   
               
              * ``Extra``   
               
               *Supported key:*  ``SECTION``  
        
              Only the length of the key value is validated. Minimum length is 1. Maximum length is 64.
        
               **Amazon Linux Operating Systems**  
        
              The supported keys for Amazon Linux operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
               *Supported key:*  ``PRODUCT``  
        
               *Supported values:*  
        
              * ``AmazonLinux2012.03``   
               
              * ``AmazonLinux2012.09``   
               
              * ``AmazonLinux2013.03``   
               
              * ``AmazonLinux2013.09``   
               
              * ``AmazonLinux2014.03``   
               
              * ``AmazonLinux2014.09``   
               
              * ``AmazonLinux2015.03``   
               
              * ``AmazonLinux2015.09``   
               
              * ``AmazonLinux2016.03``   
               
              * ``AmazonLinux2016.09``   
               
              * ``AmazonLinux2017.03``   
               
              * ``AmazonLinux2017.09``   
               
              * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
               
               *Supported key:*  ``CLASSIFICATION``  
        
               *Supported values:*  
        
              * ``Security``   
               
              * ``Bugfix``   
               
              * ``Enhancement``   
               
              * ``Recommended``   
               
              * ``Newpackage``   
               
               *Supported key:*  ``SEVERITY``  
        
               *Supported values:*  
        
              * ``Critical``   
               
              * ``Important``   
               
              * ``Medium``   
               
              * ``Low``   
               
               **Amazon Linux 2 Operating Systems**  
        
              The supported keys for Amazon Linux 2 operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
               *Supported key:*  ``PRODUCT``  
        
               *Supported values:*  
        
              * ``AmazonLinux2``   
               
              * ``AmazonLinux2.0``   
               
              * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
               
               *Supported key:*  ``CLASSIFICATION``  
        
               *Supported values:*  
        
              * ``Security``   
               
              * ``Bugfix``   
               
              * ``Enhancement``   
               
              * ``Recommended``   
               
              * ``Newpackage``   
               
               *Supported key:*  ``SEVERITY``  
        
               *Supported values:*  
        
              * ``Critical``   
               
              * ``Important``   
               
              * ``Medium``   
               
              * ``Low``   
               
               **RedHat Enterprise Linux (RHEL) Operating Systems**  
        
              The supported keys for RedHat Enterprise Linux operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
               *Supported key:*  ``PRODUCT``  
        
               *Supported values:*  
        
              * ``RedhatEnterpriseLinux6.5``   
               
              * ``RedhatEnterpriseLinux6.6``   
               
              * ``RedhatEnterpriseLinux6.7``   
               
              * ``RedhatEnterpriseLinux6.8``   
               
              * ``RedhatEnterpriseLinux6.9``   
               
              * ``RedhatEnterpriseLinux7.0``   
               
              * ``RedhatEnterpriseLinux7.1``   
               
              * ``RedhatEnterpriseLinux7.2``   
               
              * ``RedhatEnterpriseLinux7.3``   
               
              * ``RedhatEnterpriseLinux7.4``   
               
              * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
               
               *Supported key:*  ``CLASSIFICATION``  
        
               *Supported values:*  
        
              * ``Security``   
               
              * ``Bugfix``   
               
              * ``Enhancement``   
               
              * ``Recommended``   
               
              * ``Newpackage``   
               
               *Supported key:*  ``SEVERITY``  
        
               *Supported values:*  
        
              * ``Critical``   
               
              * ``Important``   
               
              * ``Medium``   
               
              * ``Low``   
               
               **SUSE Linux Enterprise Server (SLES) Operating Systems**  
        
              The supported keys for SLES operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
               *Supported key:*  ``PRODUCT``  
        
               *Supported values:*  
        
              * ``Suse12.0``   
               
              * ``Suse12.1``   
               
              * ``Suse12.2``   
               
              * ``Suse12.3``   
               
              * ``Suse12.4``   
               
              * ``Suse12.5``   
               
              * ``Suse12.6``   
               
              * ``Suse12.7``   
               
              * ``Suse12.8``   
               
              * ``Suse12.9``   
               
              * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
               
               *Supported key:*  ``CLASSIFICATION``  
        
               *Supported values:*  
        
              * ``Security``   
               
              * ``Recommended``   
               
              * ``Optional``   
               
              * ``Feature``   
               
              * ``Document``   
               
              * ``Yast``   
               
               *Supported key:*  ``SEVERITY``  
        
               *Supported values:*  
        
              * ``Critical``   
               
              * ``Important``   
               
              * ``Moderate``   
               
              * ``Low``   
               
               **CentOS Operating Systems**  
        
              The supported keys for CentOS operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
               *Supported key:*  ``PRODUCT``  
        
               *Supported values:*  
        
              * ``CentOS6.5``   
               
              * ``CentOS6.6``   
               
              * ``CentOS6.7``   
               
              * ``CentOS6.8``   
               
              * ``CentOS6.9``   
               
              * ``CentOS7.0``   
               
              * ``CentOS7.1``   
               
              * ``CentOS7.2``   
               
              * ``CentOS7.3``   
               
              * ``CentOS7.4``   
               
              * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
               
               *Supported key:*  ``CLASSIFICATION``  
        
               *Supported values:*  
        
              * ``Security``   
               
              * ``Bugfix``   
               
              * ``Enhancement``   
               
              * ``Recommended``   
               
              * ``Newpackage``   
               
               *Supported key:*  ``SEVERITY``  
        
               *Supported values:*  
        
              * ``Critical``   
               
              * ``Important``   
               
              * ``Medium``   
               
              * ``Low``   
               
              - **Key** *(string) --* **[REQUIRED]** 
        
                The key for the filter.
        
                See  PatchFilter for lists of valid keys for each operating system type.
        
              - **Values** *(list) --* **[REQUIRED]** 
        
                The value for the filter key.
        
                See  PatchFilter for lists of valid values for each key based on operating system type.
        
                - *(string) --* 
        
        :type ApprovalRules: dict
        :param ApprovalRules: 
        
          A set of rules used to include patches in the baseline.
        
          - **PatchRules** *(list) --* **[REQUIRED]** 
        
            The rules that make up the rule group.
        
            - *(dict) --* 
        
              Defines an approval rule for a patch baseline.
        
              - **PatchFilterGroup** *(dict) --* **[REQUIRED]** 
        
                The patch filter group that defines the criteria for the rule.
        
                - **PatchFilters** *(list) --* **[REQUIRED]** 
        
                  The set of patch filters that make up the group.
        
                  - *(dict) --* 
        
                    Defines a patch filter.
        
                    A patch filter consists of key/value pairs, but not all keys are valid for all operating system types. For example, the key ``PRODUCT`` is valid for all supported operating system types. The key ``MSRC_SEVERITY`` , however, is valid only for Windows operating systems, and the key ``SECTION`` is valid only for Ubuntu operating systems.
        
                    Refer to the following sections for information about which keys may be used with each major operating system, and which values are valid for each key.
        
                     **Windows Operating Systems**  
        
                    The supported keys for Windows operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``MSRC_SEVERITY`` . See the following lists for valid values for each of these keys.
        
                     *Supported key:*  ``PRODUCT``  
        
                     *Supported values:*  
        
                    * ``Windows7``   
                     
                    * ``Windows8``   
                     
                    * ``Windows8.1``   
                     
                    * ``Windows8Embedded``   
                     
                    * ``Windows10``   
                     
                    * ``Windows10LTSB``   
                     
                    * ``WindowsServer2008``   
                     
                    * ``WindowsServer2008R2``   
                     
                    * ``WindowsServer2012``   
                     
                    * ``WindowsServer2012R2``   
                     
                    * ``WindowsServer2016``   
                     
                    * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                     
                     *Supported key:*  ``CLASSIFICATION``  
        
                     *Supported values:*  
        
                    * ``CriticalUpdates``   
                     
                    * ``DefinitionUpdates``   
                     
                    * ``Drivers``   
                     
                    * ``FeaturePacks``   
                     
                    * ``SecurityUpdates``   
                     
                    * ``ServicePacks``   
                     
                    * ``Tools``   
                     
                    * ``UpdateRollups``   
                     
                    * ``Updates``   
                     
                    * ``Upgrades``   
                     
                     *Supported key:*  ``MSRC_SEVERITY``  
        
                     *Supported values:*  
        
                    * ``Critical``   
                     
                    * ``Important``   
                     
                    * ``Moderate``   
                     
                    * ``Low``   
                     
                    * ``Unspecified``   
                     
                     **Ubuntu Operating Systems**  
        
                    The supported keys for Ubuntu operating systems are ``PRODUCT`` , ``PRIORITY`` , and ``SECTION`` . See the following lists for valid values for each of these keys.
        
                     *Supported key:*  ``PRODUCT``  
        
                     *Supported values:*  
        
                    * ``Ubuntu14.04``   
                     
                    * ``Ubuntu16.04``   
                     
                    * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                     
                     *Supported key:*  ``PRIORITY``  
        
                     *Supported values:*  
        
                    * ``Required``   
                     
                    * ``Important``   
                     
                    * ``Standard``   
                     
                    * ``Optional``   
                     
                    * ``Extra``   
                     
                     *Supported key:*  ``SECTION``  
        
                    Only the length of the key value is validated. Minimum length is 1. Maximum length is 64.
        
                     **Amazon Linux Operating Systems**  
        
                    The supported keys for Amazon Linux operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                     *Supported key:*  ``PRODUCT``  
        
                     *Supported values:*  
        
                    * ``AmazonLinux2012.03``   
                     
                    * ``AmazonLinux2012.09``   
                     
                    * ``AmazonLinux2013.03``   
                     
                    * ``AmazonLinux2013.09``   
                     
                    * ``AmazonLinux2014.03``   
                     
                    * ``AmazonLinux2014.09``   
                     
                    * ``AmazonLinux2015.03``   
                     
                    * ``AmazonLinux2015.09``   
                     
                    * ``AmazonLinux2016.03``   
                     
                    * ``AmazonLinux2016.09``   
                     
                    * ``AmazonLinux2017.03``   
                     
                    * ``AmazonLinux2017.09``   
                     
                    * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                     
                     *Supported key:*  ``CLASSIFICATION``  
        
                     *Supported values:*  
        
                    * ``Security``   
                     
                    * ``Bugfix``   
                     
                    * ``Enhancement``   
                     
                    * ``Recommended``   
                     
                    * ``Newpackage``   
                     
                     *Supported key:*  ``SEVERITY``  
        
                     *Supported values:*  
        
                    * ``Critical``   
                     
                    * ``Important``   
                     
                    * ``Medium``   
                     
                    * ``Low``   
                     
                     **Amazon Linux 2 Operating Systems**  
        
                    The supported keys for Amazon Linux 2 operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                     *Supported key:*  ``PRODUCT``  
        
                     *Supported values:*  
        
                    * ``AmazonLinux2``   
                     
                    * ``AmazonLinux2.0``   
                     
                    * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                     
                     *Supported key:*  ``CLASSIFICATION``  
        
                     *Supported values:*  
        
                    * ``Security``   
                     
                    * ``Bugfix``   
                     
                    * ``Enhancement``   
                     
                    * ``Recommended``   
                     
                    * ``Newpackage``   
                     
                     *Supported key:*  ``SEVERITY``  
        
                     *Supported values:*  
        
                    * ``Critical``   
                     
                    * ``Important``   
                     
                    * ``Medium``   
                     
                    * ``Low``   
                     
                     **RedHat Enterprise Linux (RHEL) Operating Systems**  
        
                    The supported keys for RedHat Enterprise Linux operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                     *Supported key:*  ``PRODUCT``  
        
                     *Supported values:*  
        
                    * ``RedhatEnterpriseLinux6.5``   
                     
                    * ``RedhatEnterpriseLinux6.6``   
                     
                    * ``RedhatEnterpriseLinux6.7``   
                     
                    * ``RedhatEnterpriseLinux6.8``   
                     
                    * ``RedhatEnterpriseLinux6.9``   
                     
                    * ``RedhatEnterpriseLinux7.0``   
                     
                    * ``RedhatEnterpriseLinux7.1``   
                     
                    * ``RedhatEnterpriseLinux7.2``   
                     
                    * ``RedhatEnterpriseLinux7.3``   
                     
                    * ``RedhatEnterpriseLinux7.4``   
                     
                    * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                     
                     *Supported key:*  ``CLASSIFICATION``  
        
                     *Supported values:*  
        
                    * ``Security``   
                     
                    * ``Bugfix``   
                     
                    * ``Enhancement``   
                     
                    * ``Recommended``   
                     
                    * ``Newpackage``   
                     
                     *Supported key:*  ``SEVERITY``  
        
                     *Supported values:*  
        
                    * ``Critical``   
                     
                    * ``Important``   
                     
                    * ``Medium``   
                     
                    * ``Low``   
                     
                     **SUSE Linux Enterprise Server (SLES) Operating Systems**  
        
                    The supported keys for SLES operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                     *Supported key:*  ``PRODUCT``  
        
                     *Supported values:*  
        
                    * ``Suse12.0``   
                     
                    * ``Suse12.1``   
                     
                    * ``Suse12.2``   
                     
                    * ``Suse12.3``   
                     
                    * ``Suse12.4``   
                     
                    * ``Suse12.5``   
                     
                    * ``Suse12.6``   
                     
                    * ``Suse12.7``   
                     
                    * ``Suse12.8``   
                     
                    * ``Suse12.9``   
                     
                    * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                     
                     *Supported key:*  ``CLASSIFICATION``  
        
                     *Supported values:*  
        
                    * ``Security``   
                     
                    * ``Recommended``   
                     
                    * ``Optional``   
                     
                    * ``Feature``   
                     
                    * ``Document``   
                     
                    * ``Yast``   
                     
                     *Supported key:*  ``SEVERITY``  
        
                     *Supported values:*  
        
                    * ``Critical``   
                     
                    * ``Important``   
                     
                    * ``Moderate``   
                     
                    * ``Low``   
                     
                     **CentOS Operating Systems**  
        
                    The supported keys for CentOS operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                     *Supported key:*  ``PRODUCT``  
        
                     *Supported values:*  
        
                    * ``CentOS6.5``   
                     
                    * ``CentOS6.6``   
                     
                    * ``CentOS6.7``   
                     
                    * ``CentOS6.8``   
                     
                    * ``CentOS6.9``   
                     
                    * ``CentOS7.0``   
                     
                    * ``CentOS7.1``   
                     
                    * ``CentOS7.2``   
                     
                    * ``CentOS7.3``   
                     
                    * ``CentOS7.4``   
                     
                    * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                     
                     *Supported key:*  ``CLASSIFICATION``  
        
                     *Supported values:*  
        
                    * ``Security``   
                     
                    * ``Bugfix``   
                     
                    * ``Enhancement``   
                     
                    * ``Recommended``   
                     
                    * ``Newpackage``   
                     
                     *Supported key:*  ``SEVERITY``  
        
                     *Supported values:*  
        
                    * ``Critical``   
                     
                    * ``Important``   
                     
                    * ``Medium``   
                     
                    * ``Low``   
                     
                    - **Key** *(string) --* **[REQUIRED]** 
        
                      The key for the filter.
        
                      See  PatchFilter for lists of valid keys for each operating system type.
        
                    - **Values** *(list) --* **[REQUIRED]** 
        
                      The value for the filter key.
        
                      See  PatchFilter for lists of valid values for each key based on operating system type.
        
                      - *(string) --* 
        
              - **ComplianceLevel** *(string) --* 
        
                A compliance severity level for all approved patches in a patch baseline. Valid compliance severity levels include the following: Unspecified, Critical, High, Medium, Low, and Informational.
        
              - **ApproveAfterDays** *(integer) --* **[REQUIRED]** 
        
                The number of days after the release date of each patch matched by the rule that the patch is marked as approved in the patch baseline. For example, a value of ``7`` means that patches are approved seven days after they are released. 
        
              - **EnableNonSecurity** *(boolean) --* 
        
                For instances identified by the approval rule filters, enables a patch baseline to apply non-security updates available in the specified repository. The default value is \'false\'. Applies to Linux instances only.
        
        :type ApprovedPatches: list
        :param ApprovedPatches: 
        
          A list of explicitly approved patches for the baseline.
        
          For information about accepted formats for lists of approved patches and rejected patches, see `Package Name Formats for Approved and Rejected Patch Lists <http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html>`__ in the *AWS Systems Manager User Guide* .
        
          - *(string) --* 
        
        :type ApprovedPatchesComplianceLevel: string
        :param ApprovedPatchesComplianceLevel: 
        
          Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. The default value is UNSPECIFIED.
        
        :type ApprovedPatchesEnableNonSecurity: boolean
        :param ApprovedPatchesEnableNonSecurity: 
        
          Indicates whether the list of approved patches includes non-security updates that should be applied to the instances. The default value is \'false\'. Applies to Linux instances only.
        
        :type RejectedPatches: list
        :param RejectedPatches: 
        
          A list of explicitly rejected patches for the baseline.
        
          For information about accepted formats for lists of approved patches and rejected patches, see `Package Name Formats for Approved and Rejected Patch Lists <http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html>`__ in the *AWS Systems Manager User Guide* .
        
          - *(string) --* 
        
        :type RejectedPatchesAction: string
        :param RejectedPatchesAction: 
        
          The action for Patch Manager to take on patches included in the RejectedPackages list.
        
          * **ALLOW_AS_DEPENDENCY** : A package in the Rejected patches list is installed only if it is a dependency of another package. It is considered compliant with the patch baseline, and its status is reported as *InstalledOther* . This is the default action if no option is specified. 
           
          * **BLOCK** : Packages in the RejectedPatches list, and packages that include them as dependencies, are not installed under any circumstances. If a package was installed before it was added to the Rejected patches list, it is considered non-compliant with the patch baseline, and its status is reported as *InstalledRejected* . 
           
        :type Description: string
        :param Description: 
        
          A description of the patch baseline.
        
        :type Sources: list
        :param Sources: 
        
          Information about the patches to use to update the instances, including target operating systems and source repositories. Applies to Linux instances only.
        
          - *(dict) --* 
        
            Information about the patches to use to update the instances, including target operating systems and source repository. Applies to Linux instances only.
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name specified to identify the patch source.
        
            - **Products** *(list) --* **[REQUIRED]** 
        
              The specific operating system versions a patch repository applies to, such as \"Ubuntu16.04\", \"AmazonLinux2016.09\", \"RedhatEnterpriseLinux7.2\" or \"Suse12.7\". For lists of supported product values, see  PatchFilter .
        
              - *(string) --* 
        
            - **Configuration** *(string) --* **[REQUIRED]** 
        
              The value of the yum repo configuration. For example:
        
               ``cachedir=/var/cache/yum/$basesearch``  
        
               ``$releasever``  
        
               ``keepcache=0``  
        
               ``debuglevel=2``  
        
        :type ClientToken: string
        :param ClientToken: 
        
          User-provided idempotency token.
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'BaselineId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **BaselineId** *(string) --* 
        
              The ID of the created patch baseline.
        
        """
        pass

    def create_resource_data_sync(self, SyncName: str, S3Destination: Dict) -> Dict:
        """
        
        By default, data is not encrypted in Amazon S3. We strongly recommend that you enable encryption in Amazon S3 to ensure secure data storage. We also recommend that you secure access to the Amazon S3 bucket by creating a restrictive bucket policy. To view an example of a restrictive Amazon S3 bucket policy for Resource Data Sync, see `Create a Resource Data Sync for Inventory <http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-datasync-create.html>`__ in the *AWS Systems Manager User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CreateResourceDataSync>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_resource_data_sync(
              SyncName=\'string\',
              S3Destination={
                  \'BucketName\': \'string\',
                  \'Prefix\': \'string\',
                  \'SyncFormat\': \'JsonSerDe\',
                  \'Region\': \'string\',
                  \'AWSKMSKeyARN\': \'string\'
              }
          )
        :type SyncName: string
        :param SyncName: **[REQUIRED]** 
        
          A name for the configuration.
        
        :type S3Destination: dict
        :param S3Destination: **[REQUIRED]** 
        
          Amazon S3 configuration details for the sync.
        
          - **BucketName** *(string) --* **[REQUIRED]** 
        
            The name of the Amazon S3 bucket where the aggregated data is stored.
        
          - **Prefix** *(string) --* 
        
            An Amazon S3 prefix for the bucket.
        
          - **SyncFormat** *(string) --* **[REQUIRED]** 
        
            A supported sync format. The following format is currently supported: JsonSerDe
        
          - **Region** *(string) --* **[REQUIRED]** 
        
            The AWS Region with the Amazon S3 bucket targeted by the Resource Data Sync.
        
          - **AWSKMSKeyARN** *(string) --* 
        
            The ARN of an encryption key for a destination in Amazon S3. Must belong to the same region as the destination Amazon S3 bucket.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_activation(self, ActivationId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeleteActivation>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_activation(
              ActivationId=\'string\'
          )
        :type ActivationId: string
        :param ActivationId: **[REQUIRED]** 
        
          The ID of the activation that you want to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_association(self, Name: str = None, InstanceId: str = None, AssociationId: str = None) -> Dict:
        """
        
        When you disassociate a document from an instance, it does not change the configuration of the instance. To change the configuration state of an instance after you disassociate a document, you must create a new document with the desired configuration and associate it with the instance.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeleteAssociation>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_association(
              Name=\'string\',
              InstanceId=\'string\',
              AssociationId=\'string\'
          )
        :type Name: string
        :param Name: 
        
          The name of the Systems Manager document.
        
        :type InstanceId: string
        :param InstanceId: 
        
          The ID of the instance.
        
        :type AssociationId: string
        :param AssociationId: 
        
          The association ID that you want to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_document(self, Name: str) -> Dict:
        """
        
        Before you delete the document, we recommend that you use  DeleteAssociation to disassociate all instances that are associated with the document.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeleteDocument>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_document(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the document.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_inventory(self, TypeName: str, SchemaDeleteOption: str = None, DryRun: bool = None, ClientToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeleteInventory>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_inventory(
              TypeName=\'string\',
              SchemaDeleteOption=\'DisableSchema\'|\'DeleteSchema\',
              DryRun=True|False,
              ClientToken=\'string\'
          )
        :type TypeName: string
        :param TypeName: **[REQUIRED]** 
        
          The name of the custom inventory type for which you want to delete either all previously collected data, or the inventory type itself. 
        
        :type SchemaDeleteOption: string
        :param SchemaDeleteOption: 
        
          Use the ``SchemaDeleteOption`` to delete a custom inventory type (schema). If you don\'t choose this option, the system only deletes existing inventory data associated with the custom inventory type. Choose one of the following options:
        
          DisableSchema: If you choose this option, the system ignores all inventory data for the specified version, and any earlier versions. To enable this schema again, you must call the ``PutInventory`` action for a version greater than the disbled version.
        
          DeleteSchema: This option deletes the specified custom type from the Inventory service. You can recreate the schema later, if you want.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Use this option to view a summary of the deletion request without deleting any data or the data type. This option is useful when you only want to understand what will be deleted. Once you validate that the data to be deleted is what you intend to delete, you can run the same command without specifying the ``DryRun`` option.
        
        :type ClientToken: string
        :param ClientToken: 
        
          User-provided idempotency token.
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeletionId\': \'string\',
                \'TypeName\': \'string\',
                \'DeletionSummary\': {
                    \'TotalCount\': 123,
                    \'RemainingCount\': 123,
                    \'SummaryItems\': [
                        {
                            \'Version\': \'string\',
                            \'Count\': 123,
                            \'RemainingCount\': 123
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DeletionId** *(string) --* 
        
              Every ``DeleteInventory`` action is assigned a unique ID. This option returns a unique ID. You can use this ID to query the status of a delete operation. This option is useful for ensuring that a delete operation has completed before you begin other actions. 
        
            - **TypeName** *(string) --* 
        
              The name of the inventory data type specified in the request.
        
            - **DeletionSummary** *(dict) --* 
        
              A summary of the delete operation. For more information about this summary, see `Understanding the Delete Inventory Summary <http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-delete.html#sysman-inventory-delete-summary>`__ in the *AWS Systems Manager User Guide* .
        
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
        
        """
        pass

    def delete_maintenance_window(self, WindowId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeleteMaintenanceWindow>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_maintenance_window(
              WindowId=\'string\'
          )
        :type WindowId: string
        :param WindowId: **[REQUIRED]** 
        
          The ID of the Maintenance Window to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **WindowId** *(string) --* 
        
              The ID of the deleted Maintenance Window.
        
        """
        pass

    def delete_parameter(self, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeleteParameter>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_parameter(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the parameter to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_parameters(self, Names: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeleteParameters>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_parameters(
              Names=[
                  \'string\',
              ]
          )
        :type Names: list
        :param Names: **[REQUIRED]** 
        
          The names of the parameters to delete.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeletedParameters\': [
                    \'string\',
                ],
                \'InvalidParameters\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DeletedParameters** *(list) --* 
        
              The names of the deleted parameters.
        
              - *(string) --* 
          
            - **InvalidParameters** *(list) --* 
        
              The names of parameters that weren\'t deleted because the parameters are not valid.
        
              - *(string) --* 
          
        """
        pass

    def delete_patch_baseline(self, BaselineId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeletePatchBaseline>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_patch_baseline(
              BaselineId=\'string\'
          )
        :type BaselineId: string
        :param BaselineId: **[REQUIRED]** 
        
          The ID of the patch baseline to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'BaselineId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **BaselineId** *(string) --* 
        
              The ID of the deleted patch baseline.
        
        """
        pass

    def delete_resource_data_sync(self, SyncName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeleteResourceDataSync>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_resource_data_sync(
              SyncName=\'string\'
          )
        :type SyncName: string
        :param SyncName: **[REQUIRED]** 
        
          The name of the configuration to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def deregister_managed_instance(self, InstanceId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeregisterManagedInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.deregister_managed_instance(
              InstanceId=\'string\'
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The ID assigned to the managed instance when you registered it using the activation process. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def deregister_patch_baseline_for_patch_group(self, BaselineId: str, PatchGroup: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeregisterPatchBaselineForPatchGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.deregister_patch_baseline_for_patch_group(
              BaselineId=\'string\',
              PatchGroup=\'string\'
          )
        :type BaselineId: string
        :param BaselineId: **[REQUIRED]** 
        
          The ID of the patch baseline to deregister the patch group from.
        
        :type PatchGroup: string
        :param PatchGroup: **[REQUIRED]** 
        
          The name of the patch group that should be deregistered from the patch baseline.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'BaselineId\': \'string\',
                \'PatchGroup\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **BaselineId** *(string) --* 
        
              The ID of the patch baseline the patch group was deregistered from.
        
            - **PatchGroup** *(string) --* 
        
              The name of the patch group deregistered from the patch baseline.
        
        """
        pass

    def deregister_target_from_maintenance_window(self, WindowId: str, WindowTargetId: str, Safe: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeregisterTargetFromMaintenanceWindow>`_
        
        **Request Syntax** 
        ::
        
          response = client.deregister_target_from_maintenance_window(
              WindowId=\'string\',
              WindowTargetId=\'string\',
              Safe=True|False
          )
        :type WindowId: string
        :param WindowId: **[REQUIRED]** 
        
          The ID of the Maintenance Window the target should be removed from.
        
        :type WindowTargetId: string
        :param WindowTargetId: **[REQUIRED]** 
        
          The ID of the target definition to remove.
        
        :type Safe: boolean
        :param Safe: 
        
          The system checks if the target is being referenced by a task. If the target is being referenced, the system returns an error and does not deregister the target from the Maintenance Window.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowId\': \'string\',
                \'WindowTargetId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **WindowId** *(string) --* 
        
              The ID of the Maintenance Window the target was removed from.
        
            - **WindowTargetId** *(string) --* 
        
              The ID of the removed target definition.
        
        """
        pass

    def deregister_task_from_maintenance_window(self, WindowId: str, WindowTaskId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DeregisterTaskFromMaintenanceWindow>`_
        
        **Request Syntax** 
        ::
        
          response = client.deregister_task_from_maintenance_window(
              WindowId=\'string\',
              WindowTaskId=\'string\'
          )
        :type WindowId: string
        :param WindowId: **[REQUIRED]** 
        
          The ID of the Maintenance Window the task should be removed from.
        
        :type WindowTaskId: string
        :param WindowTaskId: **[REQUIRED]** 
        
          The ID of the task to remove from the Maintenance Window.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowId\': \'string\',
                \'WindowTaskId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **WindowId** *(string) --* 
        
              The ID of the Maintenance Window the task was removed from.
        
            - **WindowTaskId** *(string) --* 
        
              The ID of the task removed from the Maintenance Window.
        
        """
        pass

    def describe_activations(self, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeActivations>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_activations(
              Filters=[
                  {
                      \'FilterKey\': \'ActivationIds\'|\'DefaultInstanceName\'|\'IamRole\',
                      \'FilterValues\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
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
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          A token to start the list. Use this token to get the next set of results. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ActivationList\': [
                    {
                        \'ActivationId\': \'string\',
                        \'Description\': \'string\',
                        \'DefaultInstanceName\': \'string\',
                        \'IamRole\': \'string\',
                        \'RegistrationLimit\': 123,
                        \'RegistrationsCount\': 123,
                        \'ExpirationDate\': datetime(2015, 1, 1),
                        \'Expired\': True|False,
                        \'CreatedDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token for the next set of items to return. Use this token to get the next set of results. 
        
        """
        pass

    def describe_association(self, Name: str = None, InstanceId: str = None, AssociationId: str = None, AssociationVersion: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeAssociation>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_association(
              Name=\'string\',
              InstanceId=\'string\',
              AssociationId=\'string\',
              AssociationVersion=\'string\'
          )
        :type Name: string
        :param Name: 
        
          The name of the Systems Manager document.
        
        :type InstanceId: string
        :param InstanceId: 
        
          The instance ID.
        
        :type AssociationId: string
        :param AssociationId: 
        
          The association ID for which you want information.
        
        :type AssociationVersion: string
        :param AssociationVersion: 
        
          Specify the association version to retrieve. To view the latest version, either specify ``$LATEST`` for this parameter, or omit this parameter. To view a list of all associations for an instance, use ListInstanceAssociations. To get a list of versions for a specific association, use ListAssociationVersions. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AssociationDescription\': {
                    \'Name\': \'string\',
                    \'InstanceId\': \'string\',
                    \'AssociationVersion\': \'string\',
                    \'Date\': datetime(2015, 1, 1),
                    \'LastUpdateAssociationDate\': datetime(2015, 1, 1),
                    \'Status\': {
                        \'Date\': datetime(2015, 1, 1),
                        \'Name\': \'Pending\'|\'Success\'|\'Failed\',
                        \'Message\': \'string\',
                        \'AdditionalInfo\': \'string\'
                    },
                    \'Overview\': {
                        \'Status\': \'string\',
                        \'DetailedStatus\': \'string\',
                        \'AssociationStatusAggregatedCount\': {
                            \'string\': 123
                        }
                    },
                    \'DocumentVersion\': \'string\',
                    \'Parameters\': {
                        \'string\': [
                            \'string\',
                        ]
                    },
                    \'AssociationId\': \'string\',
                    \'Targets\': [
                        {
                            \'Key\': \'string\',
                            \'Values\': [
                                \'string\',
                            ]
                        },
                    ],
                    \'ScheduleExpression\': \'string\',
                    \'OutputLocation\': {
                        \'S3Location\': {
                            \'OutputS3Region\': \'string\',
                            \'OutputS3BucketName\': \'string\',
                            \'OutputS3KeyPrefix\': \'string\'
                        }
                    },
                    \'LastExecutionDate\': datetime(2015, 1, 1),
                    \'LastSuccessfulExecutionDate\': datetime(2015, 1, 1),
                    \'AssociationName\': \'string\',
                    \'MaxErrors\': \'string\',
                    \'MaxConcurrency\': \'string\',
                    \'ComplianceSeverity\': \'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'UNSPECIFIED\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AssociationDescription** *(dict) --* 
        
              Information about the association.
        
              - **Name** *(string) --* 
        
                The name of the Systems Manager document.
        
              - **InstanceId** *(string) --* 
        
                The ID of the instance.
        
              - **AssociationVersion** *(string) --* 
        
                The association version.
        
              - **Date** *(datetime) --* 
        
                The date when the association was made.
        
              - **LastUpdateAssociationDate** *(datetime) --* 
        
                The date when the association was last updated.
        
              - **Status** *(dict) --* 
        
                The association status.
        
                - **Date** *(datetime) --* 
        
                  The date when the status changed.
        
                - **Name** *(string) --* 
        
                  The status.
        
                - **Message** *(string) --* 
        
                  The reason for the status.
        
                - **AdditionalInfo** *(string) --* 
        
                  A user-defined string.
        
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
              
              - **DocumentVersion** *(string) --* 
        
                The document version.
        
              - **Parameters** *(dict) --* 
        
                A description of the parameters for a document. 
        
                - *(string) --* 
                  
                  - *(list) --* 
                    
                    - *(string) --* 
                
              - **AssociationId** *(string) --* 
        
                The association ID.
        
              - **Targets** *(list) --* 
        
                The instances targeted by the request. 
        
                - *(dict) --* 
        
                  An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                  - **Key** *(string) --* 
        
                    User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                  - **Values** *(list) --* 
        
                    User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
                    - *(string) --* 
                
              - **ScheduleExpression** *(string) --* 
        
                A cron expression that specifies a schedule when the association runs.
        
              - **OutputLocation** *(dict) --* 
        
                An Amazon S3 bucket where you want to store the output details of the request.
        
                - **S3Location** *(dict) --* 
        
                  An Amazon S3 bucket where you want to store the results of this request.
        
                  - **OutputS3Region** *(string) --* 
        
                    (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
        
                  - **OutputS3BucketName** *(string) --* 
        
                    The name of the Amazon S3 bucket.
        
                  - **OutputS3KeyPrefix** *(string) --* 
        
                    The Amazon S3 bucket subfolder.
        
              - **LastExecutionDate** *(datetime) --* 
        
                The date on which the association was last run.
        
              - **LastSuccessfulExecutionDate** *(datetime) --* 
        
                The last date on which the association was successfully run.
        
              - **AssociationName** *(string) --* 
        
                The association name.
        
              - **MaxErrors** *(string) --* 
        
                The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.
        
                Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.
        
              - **MaxConcurrency** *(string) --* 
        
                The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
        
                If a new instance starts and attempts to execute an association while Systems Manager is executing MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.
        
              - **ComplianceSeverity** *(string) --* 
        
                The severity level that is assigned to the association.
        
        """
        pass

    def describe_association_execution_targets(self, AssociationId: str, ExecutionId: str, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeAssociationExecutionTargets>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_association_execution_targets(
              AssociationId=\'string\',
              ExecutionId=\'string\',
              Filters=[
                  {
                      \'Key\': \'Status\'|\'ResourceId\'|\'ResourceType\',
                      \'Value\': \'string\'
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
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
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          A token to start the list. Use this token to get the next set of results. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AssociationExecutionTargets\': [
                    {
                        \'AssociationId\': \'string\',
                        \'AssociationVersion\': \'string\',
                        \'ExecutionId\': \'string\',
                        \'ResourceId\': \'string\',
                        \'ResourceType\': \'string\',
                        \'Status\': \'string\',
                        \'DetailedStatus\': \'string\',
                        \'LastExecutionDate\': datetime(2015, 1, 1),
                        \'OutputSource\': {
                            \'OutputSourceId\': \'string\',
                            \'OutputSourceType\': \'string\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  The execution ID. If the association does not run at intervals or according to a schedule, then the ExecutionID is the same as the AssociationID.
        
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
        
            - **NextToken** *(string) --* 
        
              The token for the next set of items to return. Use this token to get the next set of results.
        
        """
        pass

    def describe_association_executions(self, AssociationId: str, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeAssociationExecutions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_association_executions(
              AssociationId=\'string\',
              Filters=[
                  {
                      \'Key\': \'ExecutionId\'|\'Status\'|\'CreatedTime\',
                      \'Value\': \'string\',
                      \'Type\': \'EQUAL\'|\'LESS_THAN\'|\'GREATER_THAN\'
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
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
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          A token to start the list. Use this token to get the next set of results. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AssociationExecutions\': [
                    {
                        \'AssociationId\': \'string\',
                        \'AssociationVersion\': \'string\',
                        \'ExecutionId\': \'string\',
                        \'Status\': \'string\',
                        \'DetailedStatus\': \'string\',
                        \'CreatedTime\': datetime(2015, 1, 1),
                        \'LastExecutionDate\': datetime(2015, 1, 1),
                        \'ResourceCountByStatus\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  The execution ID for the association. If the association does not run at intervals or according to a schedule, then the ExecutionID is the same as the AssociationID.
        
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
        
            - **NextToken** *(string) --* 
        
              The token for the next set of items to return. Use this token to get the next set of results.
        
        """
        pass

    def describe_automation_executions(self, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeAutomationExecutions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_automation_executions(
              Filters=[
                  {
                      \'Key\': \'DocumentNamePrefix\'|\'ExecutionStatus\'|\'ExecutionId\'|\'ParentExecutionId\'|\'CurrentAction\'|\'StartTimeBefore\'|\'StartTimeAfter\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
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
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AutomationExecutionMetadataList\': [
                    {
                        \'AutomationExecutionId\': \'string\',
                        \'DocumentName\': \'string\',
                        \'DocumentVersion\': \'string\',
                        \'AutomationExecutionStatus\': \'Pending\'|\'InProgress\'|\'Waiting\'|\'Success\'|\'TimedOut\'|\'Cancelling\'|\'Cancelled\'|\'Failed\',
                        \'ExecutionStartTime\': datetime(2015, 1, 1),
                        \'ExecutionEndTime\': datetime(2015, 1, 1),
                        \'ExecutedBy\': \'string\',
                        \'LogFile\': \'string\',
                        \'Outputs\': {
                            \'string\': [
                                \'string\',
                            ]
                        },
                        \'Mode\': \'Auto\'|\'Interactive\',
                        \'ParentAutomationExecutionId\': \'string\',
                        \'CurrentStepName\': \'string\',
                        \'CurrentAction\': \'string\',
                        \'FailureMessage\': \'string\',
                        \'TargetParameterName\': \'string\',
                        \'Targets\': [
                            {
                                \'Key\': \'string\',
                                \'Values\': [
                                    \'string\',
                                ]
                            },
                        ],
                        \'TargetMaps\': [
                            {
                                \'string\': [
                                    \'string\',
                                ]
                            },
                        ],
                        \'ResolvedTargets\': {
                            \'ParameterValues\': [
                                \'string\',
                            ],
                            \'Truncated\': True|False
                        },
                        \'MaxConcurrency\': \'string\',
                        \'MaxErrors\': \'string\',
                        \'Target\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  The IAM role ARN of the user who executed the Automation.
        
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
        
                  The name of the currently executing step.
        
                - **CurrentAction** *(string) --* 
        
                  The action of the currently executing step.
        
                - **FailureMessage** *(string) --* 
        
                  The list of execution outputs as defined in the Automation document.
        
                - **TargetParameterName** *(string) --* 
        
                  The list of execution outputs as defined in the Automation document.
        
                - **Targets** *(list) --* 
        
                  The targets defined by the user when starting the Automation.
        
                  - *(dict) --* 
        
                    An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                    - **Key** *(string) --* 
        
                      User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                    - **Values** *(list) --* 
        
                      User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
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
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def describe_automation_step_executions(self, AutomationExecutionId: str, Filters: List = None, NextToken: str = None, MaxResults: int = None, ReverseOrder: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeAutomationStepExecutions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_automation_step_executions(
              AutomationExecutionId=\'string\',
              Filters=[
                  {
                      \'Key\': \'StartTimeBefore\'|\'StartTimeAfter\'|\'StepExecutionStatus\'|\'StepExecutionId\'|\'StepName\'|\'Action\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              NextToken=\'string\',
              MaxResults=123,
              ReverseOrder=True|False
          )
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
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type ReverseOrder: boolean
        :param ReverseOrder: 
        
          A boolean that indicates whether to list step executions in reverse order by start time. The default value is false.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StepExecutions\': [
                    {
                        \'StepName\': \'string\',
                        \'Action\': \'string\',
                        \'TimeoutSeconds\': 123,
                        \'OnFailure\': \'string\',
                        \'MaxAttempts\': 123,
                        \'ExecutionStartTime\': datetime(2015, 1, 1),
                        \'ExecutionEndTime\': datetime(2015, 1, 1),
                        \'StepStatus\': \'Pending\'|\'InProgress\'|\'Waiting\'|\'Success\'|\'TimedOut\'|\'Cancelling\'|\'Cancelled\'|\'Failed\',
                        \'ResponseCode\': \'string\',
                        \'Inputs\': {
                            \'string\': \'string\'
                        },
                        \'Outputs\': {
                            \'string\': [
                                \'string\',
                            ]
                        },
                        \'Response\': \'string\',
                        \'FailureMessage\': \'string\',
                        \'FailureDetails\': {
                            \'FailureStage\': \'string\',
                            \'FailureType\': \'string\',
                            \'Details\': {
                                \'string\': [
                                    \'string\',
                                ]
                            }
                        },
                        \'StepExecutionId\': \'string\',
                        \'OverriddenParameters\': {
                            \'string\': [
                                \'string\',
                            ]
                        },
                        \'IsEnd\': True|False,
                        \'NextStep\': \'string\',
                        \'IsCritical\': True|False,
                        \'ValidNextSteps\': [
                            \'string\',
                        ]
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  A user-specified list of parameters to override when executing a step.
        
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
        
                  Strategies used when step fails, we support Continue and Abort. Abort will fail the automation when the step fails. Continue will ignore the failure of current step and allow automation to execute the next step. With conditional branching, we add step:stepName to support the automation to go to another specific step.
        
                  - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def describe_available_patches(self, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeAvailablePatches>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_available_patches(
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
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
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of patches to return (per page).
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Patches\': [
                    {
                        \'Id\': \'string\',
                        \'ReleaseDate\': datetime(2015, 1, 1),
                        \'Title\': \'string\',
                        \'Description\': \'string\',
                        \'ContentUrl\': \'string\',
                        \'Vendor\': \'string\',
                        \'ProductFamily\': \'string\',
                        \'Product\': \'string\',
                        \'Classification\': \'string\',
                        \'MsrcSeverity\': \'string\',
                        \'KbNumber\': \'string\',
                        \'MsrcNumber\': \'string\',
                        \'Language\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  The language of the patch if it\'s language-specific.
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def describe_document(self, Name: str, DocumentVersion: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeDocument>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_document(
              Name=\'string\',
              DocumentVersion=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the Systems Manager document.
        
        :type DocumentVersion: string
        :param DocumentVersion: 
        
          The document version for which you want information. Can be a specific version or the default version.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Document\': {
                    \'Sha1\': \'string\',
                    \'Hash\': \'string\',
                    \'HashType\': \'Sha256\'|\'Sha1\',
                    \'Name\': \'string\',
                    \'Owner\': \'string\',
                    \'CreatedDate\': datetime(2015, 1, 1),
                    \'Status\': \'Creating\'|\'Active\'|\'Updating\'|\'Deleting\',
                    \'DocumentVersion\': \'string\',
                    \'Description\': \'string\',
                    \'Parameters\': [
                        {
                            \'Name\': \'string\',
                            \'Type\': \'String\'|\'StringList\',
                            \'Description\': \'string\',
                            \'DefaultValue\': \'string\'
                        },
                    ],
                    \'PlatformTypes\': [
                        \'Windows\'|\'Linux\',
                    ],
                    \'DocumentType\': \'Command\'|\'Policy\'|\'Automation\'|\'Session\',
                    \'SchemaVersion\': \'string\',
                    \'LatestVersion\': \'string\',
                    \'DefaultVersion\': \'string\',
                    \'DocumentFormat\': \'YAML\'|\'JSON\',
                    \'TargetType\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Document** *(dict) --* 
        
              Information about the Systems Manager document.
        
              - **Sha1** *(string) --* 
        
                The SHA1 hash of the document, which you can use for verification.
        
              - **Hash** *(string) --* 
        
                The Sha256 or Sha1 hash created by the system when the document was created. 
        
                .. note::
        
                  Sha1 hashes have been deprecated.
        
              - **HashType** *(string) --* 
        
                Sha256 or Sha1.
        
                .. note::
        
                  Sha1 hashes have been deprecated.
        
              - **Name** *(string) --* 
        
                The name of the Systems Manager document.
        
              - **Owner** *(string) --* 
        
                The AWS user account that created the document.
        
              - **CreatedDate** *(datetime) --* 
        
                The date when the document was created.
        
              - **Status** *(string) --* 
        
                The status of the Systems Manager document.
        
              - **DocumentVersion** *(string) --* 
        
                The document version.
        
              - **Description** *(string) --* 
        
                A description of the document. 
        
              - **Parameters** *(list) --* 
        
                A description of the parameters for a document.
        
                - *(dict) --* 
        
                  Parameters specified in a System Manager document that execute on the server when the command is run. 
        
                  - **Name** *(string) --* 
        
                    The name of the parameter.
        
                  - **Type** *(string) --* 
        
                    The type of parameter. The type can be either String or StringList.
        
                  - **Description** *(string) --* 
        
                    A description of what the parameter does, how to use it, the default value, and whether or not the parameter is optional.
        
                  - **DefaultValue** *(string) --* 
        
                    If specified, the default values for the parameters. Parameters without a default value are required. Parameters with a default value are optional.
        
              - **PlatformTypes** *(list) --* 
        
                The list of OS platforms compatible with this Systems Manager document. 
        
                - *(string) --* 
            
              - **DocumentType** *(string) --* 
        
                The type of document. 
        
              - **SchemaVersion** *(string) --* 
        
                The schema version.
        
              - **LatestVersion** *(string) --* 
        
                The latest version of the document.
        
              - **DefaultVersion** *(string) --* 
        
                The default version.
        
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
        
        """
        pass

    def describe_document_permission(self, Name: str, PermissionType: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeDocumentPermission>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_document_permission(
              Name=\'string\',
              PermissionType=\'Share\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the document for which you are the owner.
        
        :type PermissionType: string
        :param PermissionType: **[REQUIRED]** 
        
          The permission type for the document. The permission type can be *Share* .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AccountIds\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AccountIds** *(list) --* 
        
              The account IDs that have permission to use this document. The ID can be either an AWS account or *All* .
        
              - *(string) --* 
          
        """
        pass

    def describe_effective_instance_associations(self, InstanceId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeEffectiveInstanceAssociations>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_effective_instance_associations(
              InstanceId=\'string\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The instance ID for which you want to view all associations.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Associations\': [
                    {
                        \'AssociationId\': \'string\',
                        \'InstanceId\': \'string\',
                        \'Content\': \'string\',
                        \'AssociationVersion\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def describe_effective_patches_for_patch_baseline(self, BaselineId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeEffectivePatchesForPatchBaseline>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_effective_patches_for_patch_baseline(
              BaselineId=\'string\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type BaselineId: string
        :param BaselineId: **[REQUIRED]** 
        
          The ID of the patch baseline to retrieve the effective patches for.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of patches to return (per page).
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EffectivePatches\': [
                    {
                        \'Patch\': {
                            \'Id\': \'string\',
                            \'ReleaseDate\': datetime(2015, 1, 1),
                            \'Title\': \'string\',
                            \'Description\': \'string\',
                            \'ContentUrl\': \'string\',
                            \'Vendor\': \'string\',
                            \'ProductFamily\': \'string\',
                            \'Product\': \'string\',
                            \'Classification\': \'string\',
                            \'MsrcSeverity\': \'string\',
                            \'KbNumber\': \'string\',
                            \'MsrcNumber\': \'string\',
                            \'Language\': \'string\'
                        },
                        \'PatchStatus\': {
                            \'DeploymentStatus\': \'APPROVED\'|\'PENDING_APPROVAL\'|\'EXPLICIT_APPROVED\'|\'EXPLICIT_REJECTED\',
                            \'ComplianceLevel\': \'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'INFORMATIONAL\'|\'UNSPECIFIED\',
                            \'ApprovalDate\': datetime(2015, 1, 1)
                        }
                    },
                ],
                \'NextToken\': \'string\'
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
        
                    The language of the patch if it\'s language-specific.
        
                - **PatchStatus** *(dict) --* 
        
                  The status of the patch in a patch baseline. This includes information about whether the patch is currently approved, due to be approved by a rule, explicitly approved, or explicitly rejected and the date the patch was or will be approved.
        
                  - **DeploymentStatus** *(string) --* 
        
                    The approval status of a patch (APPROVED, PENDING_APPROVAL, EXPLICIT_APPROVED, EXPLICIT_REJECTED).
        
                  - **ComplianceLevel** *(string) --* 
        
                    The compliance severity level for a patch.
        
                  - **ApprovalDate** *(datetime) --* 
        
                    The date the patch was approved (or will be approved if the status is PENDING_APPROVAL).
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def describe_instance_associations_status(self, InstanceId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstanceAssociationsStatus>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_instance_associations_status(
              InstanceId=\'string\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The instance IDs for which you want association status information.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'InstanceAssociationStatusInfos\': [
                    {
                        \'AssociationId\': \'string\',
                        \'Name\': \'string\',
                        \'DocumentVersion\': \'string\',
                        \'AssociationVersion\': \'string\',
                        \'InstanceId\': \'string\',
                        \'ExecutionDate\': datetime(2015, 1, 1),
                        \'Status\': \'string\',
                        \'DetailedStatus\': \'string\',
                        \'ExecutionSummary\': \'string\',
                        \'ErrorCode\': \'string\',
                        \'OutputUrl\': {
                            \'S3OutputUrl\': {
                                \'OutputUrl\': \'string\'
                            }
                        },
                        \'AssociationName\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  The date the instance association executed. 
        
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
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def describe_instance_information(self, InstanceInformationFilterList: List = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        .. note::
        
          The IamRole field for this API action is the Amazon Identity and Access Management (IAM) role assigned to on-premises instances. This call does not return the IAM role for Amazon EC2 instances.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstanceInformation>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_instance_information(
              InstanceInformationFilterList=[
                  {
                      \'key\': \'InstanceIds\'|\'AgentVersion\'|\'PingStatus\'|\'PlatformTypes\'|\'ActivationIds\'|\'IamRole\'|\'ResourceType\'|\'AssociationStatus\',
                      \'valueSet\': [
                          \'string\',
                      ]
                  },
              ],
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
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
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results. 
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'InstanceInformationList\': [
                    {
                        \'InstanceId\': \'string\',
                        \'PingStatus\': \'Online\'|\'ConnectionLost\'|\'Inactive\',
                        \'LastPingDateTime\': datetime(2015, 1, 1),
                        \'AgentVersion\': \'string\',
                        \'IsLatestVersion\': True|False,
                        \'PlatformType\': \'Windows\'|\'Linux\',
                        \'PlatformName\': \'string\',
                        \'PlatformVersion\': \'string\',
                        \'ActivationId\': \'string\',
                        \'IamRole\': \'string\',
                        \'RegistrationDate\': datetime(2015, 1, 1),
                        \'ResourceType\': \'ManagedInstance\'|\'Document\'|\'EC2Instance\',
                        \'Name\': \'string\',
                        \'IPAddress\': \'string\',
                        \'ComputerName\': \'string\',
                        \'AssociationStatus\': \'string\',
                        \'LastAssociationExecutionDate\': datetime(2015, 1, 1),
                        \'LastSuccessfulAssociationExecutionDate\': datetime(2015, 1, 1),
                        \'AssociationOverview\': {
                            \'DetailedStatus\': \'string\',
                            \'InstanceAssociationStatusAggregatedCount\': {
                                \'string\': 123
                            }
                        }
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  The date the association was last executed.
        
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
                
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty. 
        
        """
        pass

    def describe_instance_patch_states(self, InstanceIds: List, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstancePatchStates>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_instance_patch_states(
              InstanceIds=[
                  \'string\',
              ],
              NextToken=\'string\',
              MaxResults=123
          )
        :type InstanceIds: list
        :param InstanceIds: **[REQUIRED]** 
        
          The ID of the instance whose patch state information should be retrieved.
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of instances to return (per page).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'InstancePatchStates\': [
                    {
                        \'InstanceId\': \'string\',
                        \'PatchGroup\': \'string\',
                        \'BaselineId\': \'string\',
                        \'SnapshotId\': \'string\',
                        \'InstallOverrideList\': \'string\',
                        \'OwnerInformation\': \'string\',
                        \'InstalledCount\': 123,
                        \'InstalledOtherCount\': 123,
                        \'InstalledRejectedCount\': 123,
                        \'MissingCount\': 123,
                        \'FailedCount\': 123,
                        \'NotApplicableCount\': 123,
                        \'OperationStartTime\': datetime(2015, 1, 1),
                        \'OperationEndTime\': datetime(2015, 1, 1),
                        \'Operation\': \'Scan\'|\'Install\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  The number of patches from the patch baseline that are applicable for the instance but aren\'t currently installed.
        
                - **FailedCount** *(integer) --* 
        
                  The number of patches from the patch baseline that were attempted to be installed during the last patching operation, but failed to install.
        
                - **NotApplicableCount** *(integer) --* 
        
                  The number of patches from the patch baseline that aren\'t applicable for the instance and hence aren\'t installed on the instance.
        
                - **OperationStartTime** *(datetime) --* 
        
                  The time the most recent patching operation was started on the instance.
        
                - **OperationEndTime** *(datetime) --* 
        
                  The time the most recent patching operation completed on the instance.
        
                - **Operation** *(string) --* 
        
                  The type of patching operation that was performed: SCAN (assess patch compliance state) or INSTALL (install missing patches).
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def describe_instance_patch_states_for_patch_group(self, PatchGroup: str, Filters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstancePatchStatesForPatchGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_instance_patch_states_for_patch_group(
              PatchGroup=\'string\',
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ],
                      \'Type\': \'Equal\'|\'NotEqual\'|\'LessThan\'|\'GreaterThan\'
                  },
              ],
              NextToken=\'string\',
              MaxResults=123
          )
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
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of patches to return (per page).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'InstancePatchStates\': [
                    {
                        \'InstanceId\': \'string\',
                        \'PatchGroup\': \'string\',
                        \'BaselineId\': \'string\',
                        \'SnapshotId\': \'string\',
                        \'InstallOverrideList\': \'string\',
                        \'OwnerInformation\': \'string\',
                        \'InstalledCount\': 123,
                        \'InstalledOtherCount\': 123,
                        \'InstalledRejectedCount\': 123,
                        \'MissingCount\': 123,
                        \'FailedCount\': 123,
                        \'NotApplicableCount\': 123,
                        \'OperationStartTime\': datetime(2015, 1, 1),
                        \'OperationEndTime\': datetime(2015, 1, 1),
                        \'Operation\': \'Scan\'|\'Install\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  The number of patches from the patch baseline that are applicable for the instance but aren\'t currently installed.
        
                - **FailedCount** *(integer) --* 
        
                  The number of patches from the patch baseline that were attempted to be installed during the last patching operation, but failed to install.
        
                - **NotApplicableCount** *(integer) --* 
        
                  The number of patches from the patch baseline that aren\'t applicable for the instance and hence aren\'t installed on the instance.
        
                - **OperationStartTime** *(datetime) --* 
        
                  The time the most recent patching operation was started on the instance.
        
                - **OperationEndTime** *(datetime) --* 
        
                  The time the most recent patching operation completed on the instance.
        
                - **Operation** *(string) --* 
        
                  The type of patching operation that was performed: SCAN (assess patch compliance state) or INSTALL (install missing patches).
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def describe_instance_patches(self, InstanceId: str, Filters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstancePatches>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_instance_patches(
              InstanceId=\'string\',
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              NextToken=\'string\',
              MaxResults=123
          )
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
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of patches to return (per page).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Patches\': [
                    {
                        \'Title\': \'string\',
                        \'KBId\': \'string\',
                        \'Classification\': \'string\',
                        \'Severity\': \'string\',
                        \'State\': \'INSTALLED\'|\'INSTALLED_OTHER\'|\'INSTALLED_REJECTED\'|\'MISSING\'|\'NOT_APPLICABLE\'|\'FAILED\',
                        \'InstalledTime\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Patches** *(list) --* 
        
              Each entry in the array is a structure containing:
        
              Title (string)
        
              KBId (string)
        
              Classification (string)
        
              Severity (string)
        
              State (string, such as \"INSTALLED\" or \"FAILED\")
        
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
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def describe_inventory_deletions(self, DeletionId: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInventoryDeletions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_inventory_deletions(
              DeletionId=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type DeletionId: string
        :param DeletionId: 
        
          Specify the delete inventory ID for which you want information. This ID was returned by the ``DeleteInventory`` action.
        
        :type NextToken: string
        :param NextToken: 
        
          A token to start the list. Use this token to get the next set of results. 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'InventoryDeletions\': [
                    {
                        \'DeletionId\': \'string\',
                        \'TypeName\': \'string\',
                        \'DeletionStartTime\': datetime(2015, 1, 1),
                        \'LastStatus\': \'InProgress\'|\'Complete\',
                        \'LastStatusMessage\': \'string\',
                        \'DeletionSummary\': {
                            \'TotalCount\': 123,
                            \'RemainingCount\': 123,
                            \'SummaryItems\': [
                                {
                                    \'Version\': \'string\',
                                    \'Count\': 123,
                                    \'RemainingCount\': 123
                                },
                            ]
                        },
                        \'LastStatusUpdateTime\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token for the next set of items to return. Use this token to get the next set of results.
        
        """
        pass

    def describe_maintenance_window_execution_task_invocations(self, WindowExecutionId: str, TaskId: str, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTaskInvocations>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_maintenance_window_execution_task_invocations(
              WindowExecutionId=\'string\',
              TaskId=\'string\',
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
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
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowExecutionTaskInvocationIdentities\': [
                    {
                        \'WindowExecutionId\': \'string\',
                        \'TaskExecutionId\': \'string\',
                        \'InvocationId\': \'string\',
                        \'ExecutionId\': \'string\',
                        \'TaskType\': \'RUN_COMMAND\'|\'AUTOMATION\'|\'STEP_FUNCTIONS\'|\'LAMBDA\',
                        \'Parameters\': \'string\',
                        \'Status\': \'PENDING\'|\'IN_PROGRESS\'|\'SUCCESS\'|\'FAILED\'|\'TIMED_OUT\'|\'CANCELLING\'|\'CANCELLED\'|\'SKIPPED_OVERLAPPING\',
                        \'StatusDetails\': \'string\',
                        \'StartTime\': datetime(2015, 1, 1),
                        \'EndTime\': datetime(2015, 1, 1),
                        \'OwnerInformation\': \'string\',
                        \'WindowTargetId\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  The parameters that were provided for the invocation when it was executed.
        
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
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def describe_maintenance_window_execution_tasks(self, WindowExecutionId: str, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTasks>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_maintenance_window_execution_tasks(
              WindowExecutionId=\'string\',
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
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
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowExecutionTaskIdentities\': [
                    {
                        \'WindowExecutionId\': \'string\',
                        \'TaskExecutionId\': \'string\',
                        \'Status\': \'PENDING\'|\'IN_PROGRESS\'|\'SUCCESS\'|\'FAILED\'|\'TIMED_OUT\'|\'CANCELLING\'|\'CANCELLED\'|\'SKIPPED_OVERLAPPING\',
                        \'StatusDetails\': \'string\',
                        \'StartTime\': datetime(2015, 1, 1),
                        \'EndTime\': datetime(2015, 1, 1),
                        \'TaskArn\': \'string\',
                        \'TaskType\': \'RUN_COMMAND\'|\'AUTOMATION\'|\'STEP_FUNCTIONS\'|\'LAMBDA\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  The ARN of the executed task.
        
                - **TaskType** *(string) --* 
        
                  The type of executed task.
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def describe_maintenance_window_executions(self, WindowId: str, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowExecutions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_maintenance_window_executions(
              WindowId=\'string\',
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
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
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowExecutions\': [
                    {
                        \'WindowId\': \'string\',
                        \'WindowExecutionId\': \'string\',
                        \'Status\': \'PENDING\'|\'IN_PROGRESS\'|\'SUCCESS\'|\'FAILED\'|\'TIMED_OUT\'|\'CANCELLING\'|\'CANCELLED\'|\'SKIPPED_OVERLAPPING\',
                        \'StatusDetails\': \'string\',
                        \'StartTime\': datetime(2015, 1, 1),
                        \'EndTime\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def describe_maintenance_window_schedule(self, WindowId: str = None, Targets: List = None, ResourceType: str = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowSchedule>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_maintenance_window_schedule(
              WindowId=\'string\',
              Targets=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              ResourceType=\'INSTANCE\',
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
        :type WindowId: string
        :param WindowId: 
        
          The ID of the Maintenance Window to retrieve information about.
        
        :type Targets: list
        :param Targets: 
        
          The instance ID or key/value pair to retrieve information about.
        
          - *(dict) --* 
        
            An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
            - **Key** *(string) --* 
        
              User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
            - **Values** *(list) --* 
        
              User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
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
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ScheduledWindowExecutions\': [
                    {
                        \'WindowId\': \'string\',
                        \'Name\': \'string\',
                        \'ExecutionTime\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token for the next set of items to return. (You use this token in the next call.)
        
        """
        pass

    def describe_maintenance_window_targets(self, WindowId: str, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowTargets>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_maintenance_window_targets(
              WindowId=\'string\',
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
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
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Targets\': [
                    {
                        \'WindowId\': \'string\',
                        \'WindowTargetId\': \'string\',
                        \'ResourceType\': \'INSTANCE\',
                        \'Targets\': [
                            {
                                \'Key\': \'string\',
                                \'Values\': [
                                    \'string\',
                                ]
                            },
                        ],
                        \'OwnerInformation\': \'string\',
                        \'Name\': \'string\',
                        \'Description\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Targets** *(list) --* 
        
              Information about the targets in the Maintenance Window.
        
              - *(dict) --* 
        
                The target registered with the Maintenance Window.
        
                - **WindowId** *(string) --* 
        
                  The Maintenance Window ID where the target is registered.
        
                - **WindowTargetId** *(string) --* 
        
                  The ID of the target.
        
                - **ResourceType** *(string) --* 
        
                  The type of target.
        
                - **Targets** *(list) --* 
        
                  The targets (either instances or tags). Instances are specified using Key=instanceids,Values=<instanceid1>,<instanceid2>. Tags are specified using Key=<tag name>,Values=<tag value>.
        
                  - *(dict) --* 
        
                    An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                    - **Key** *(string) --* 
        
                      User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                    - **Values** *(list) --* 
        
                      User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
                      - *(string) --* 
                  
                - **OwnerInformation** *(string) --* 
        
                  User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
        
                - **Name** *(string) --* 
        
                  The target name.
        
                - **Description** *(string) --* 
        
                  A description of the target.
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def describe_maintenance_window_tasks(self, WindowId: str, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowTasks>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_maintenance_window_tasks(
              WindowId=\'string\',
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
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
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Tasks\': [
                    {
                        \'WindowId\': \'string\',
                        \'WindowTaskId\': \'string\',
                        \'TaskArn\': \'string\',
                        \'Type\': \'RUN_COMMAND\'|\'AUTOMATION\'|\'STEP_FUNCTIONS\'|\'LAMBDA\',
                        \'Targets\': [
                            {
                                \'Key\': \'string\',
                                \'Values\': [
                                    \'string\',
                                ]
                            },
                        ],
                        \'TaskParameters\': {
                            \'string\': {
                                \'Values\': [
                                    \'string\',
                                ]
                            }
                        },
                        \'Priority\': 123,
                        \'LoggingInfo\': {
                            \'S3BucketName\': \'string\',
                            \'S3KeyPrefix\': \'string\',
                            \'S3Region\': \'string\'
                        },
                        \'ServiceRoleArn\': \'string\',
                        \'MaxConcurrency\': \'string\',
                        \'MaxErrors\': \'string\',
                        \'Name\': \'string\',
                        \'Description\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Tasks** *(list) --* 
        
              Information about the tasks in the Maintenance Window.
        
              - *(dict) --* 
        
                Information about a task defined for a Maintenance Window.
        
                - **WindowId** *(string) --* 
        
                  The Maintenance Window ID where the task is registered.
        
                - **WindowTaskId** *(string) --* 
        
                  The task ID.
        
                - **TaskArn** *(string) --* 
        
                  The resource that the task uses during execution. For RUN_COMMAND and AUTOMATION task types, ``TaskArn`` is the Systems Manager document name or ARN. For LAMBDA tasks, it\'s the function name or ARN. For STEP_FUNCTION tasks, it\'s the state machine ARN.
        
                - **Type** *(string) --* 
        
                  The type of task. The type can be one of the following: RUN_COMMAND, AUTOMATION, LAMBDA, or STEP_FUNCTION.
        
                - **Targets** *(list) --* 
        
                  The targets (either instances or tags). Instances are specified using Key=instanceids,Values=<instanceid1>,<instanceid2>. Tags are specified using Key=<tag name>,Values=<tag value>.
        
                  - *(dict) --* 
        
                    An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                    - **Key** *(string) --* 
        
                      User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                    - **Values** *(list) --* 
        
                      User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
                      - *(string) --* 
                  
                - **TaskParameters** *(dict) --* 
        
                  The parameters that should be passed to the task when it is executed.
        
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
        
                  The role that should be assumed when executing the task
        
                - **MaxConcurrency** *(string) --* 
        
                  The maximum number of targets this task can be run for in parallel.
        
                - **MaxErrors** *(string) --* 
        
                  The maximum number of errors allowed before this task stops being scheduled.
        
                - **Name** *(string) --* 
        
                  The task name.
        
                - **Description** *(string) --* 
        
                  A description of the task.
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def describe_maintenance_windows(self, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindows>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_maintenance_windows(
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
        :type Filters: list
        :param Filters: 
        
          Optional filters used to narrow down the scope of the returned Maintenance Windows. Supported filter keys are Name and Enabled.
        
          - *(dict) --* 
        
            Filter used in the request. Supported filter keys are Name and Enabled.
        
            - **Key** *(string) --* 
        
              The name of the filter.
        
            - **Values** *(list) --* 
        
              The filter values.
        
              - *(string) --* 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowIdentities\': [
                    {
                        \'WindowId\': \'string\',
                        \'Name\': \'string\',
                        \'Description\': \'string\',
                        \'Enabled\': True|False,
                        \'Duration\': 123,
                        \'Cutoff\': 123,
                        \'Schedule\': \'string\',
                        \'ScheduleTimezone\': \'string\',
                        \'EndDate\': \'string\',
                        \'StartDate\': \'string\',
                        \'NextExecutionTime\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def describe_maintenance_windows_for_target(self, Targets: List, ResourceType: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeMaintenanceWindowsForTarget>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_maintenance_windows_for_target(
              Targets=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              ResourceType=\'INSTANCE\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type Targets: list
        :param Targets: **[REQUIRED]** 
        
          The instance ID or key/value pair to retrieve information about.
        
          - *(dict) --* 
        
            An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
            - **Key** *(string) --* 
        
              User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
            - **Values** *(list) --* 
        
              User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
              - *(string) --* 
        
        :type ResourceType: string
        :param ResourceType: **[REQUIRED]** 
        
          The type of resource you want to retrieve information about. For example, \"INSTANCE\".
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowIdentities\': [
                    {
                        \'WindowId\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token for the next set of items to return. (You use this token in the next call.)
        
        """
        pass

    def describe_parameters(self, Filters: List = None, ParameterFilters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        Request results are returned on a best-effort basis. If you specify ``MaxResults`` in the request, the response includes information up to the limit specified. The number of items returned, however, can be between zero and the value of ``MaxResults`` . If the service reaches an internal limit while processing the results, it stops the operation and returns the matching values up to that point and a ``NextToken`` . You can specify the ``NextToken`` in a subsequent call to get the next set of results.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeParameters>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_parameters(
              Filters=[
                  {
                      \'Key\': \'Name\'|\'Type\'|\'KeyId\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              ParameterFilters=[
                  {
                      \'Key\': \'string\',
                      \'Option\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
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
        
              The ``Name`` field can\'t be used with the  GetParametersByPath API action.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **Option** *(string) --* 
        
              Valid options are Equals and BeginsWith. For Path filter, valid options are Recursive and OneLevel.
        
            - **Values** *(list) --* 
        
              The value you want to search for.
        
              - *(string) --* 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Parameters\': [
                    {
                        \'Name\': \'string\',
                        \'Type\': \'String\'|\'StringList\'|\'SecureString\',
                        \'KeyId\': \'string\',
                        \'LastModifiedDate\': datetime(2015, 1, 1),
                        \'LastModifiedUser\': \'string\',
                        \'Description\': \'string\',
                        \'AllowedPattern\': \'string\',
                        \'Version\': 123
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def describe_patch_baselines(self, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribePatchBaselines>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_patch_baselines(
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
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
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of patch baselines to return (per page).
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'BaselineIdentities\': [
                    {
                        \'BaselineId\': \'string\',
                        \'BaselineName\': \'string\',
                        \'OperatingSystem\': \'WINDOWS\'|\'AMAZON_LINUX\'|\'AMAZON_LINUX_2\'|\'UBUNTU\'|\'REDHAT_ENTERPRISE_LINUX\'|\'SUSE\'|\'CENTOS\',
                        \'BaselineDescription\': \'string\',
                        \'DefaultBaseline\': True|False
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def describe_patch_group_state(self, PatchGroup: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribePatchGroupState>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_patch_group_state(
              PatchGroup=\'string\'
          )
        :type PatchGroup: string
        :param PatchGroup: **[REQUIRED]** 
        
          The name of the patch group whose patch snapshot should be retrieved.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Instances\': 123,
                \'InstancesWithInstalledPatches\': 123,
                \'InstancesWithInstalledOtherPatches\': 123,
                \'InstancesWithInstalledRejectedPatches\': 123,
                \'InstancesWithMissingPatches\': 123,
                \'InstancesWithFailedPatches\': 123,
                \'InstancesWithNotApplicablePatches\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Instances** *(integer) --* 
        
              The number of instances in the patch group.
        
            - **InstancesWithInstalledPatches** *(integer) --* 
        
              The number of instances with installed patches.
        
            - **InstancesWithInstalledOtherPatches** *(integer) --* 
        
              The number of instances with patches installed that aren\'t defined in the patch baseline.
        
            - **InstancesWithInstalledRejectedPatches** *(integer) --* 
        
              The number of instances with patches installed that are specified in a RejectedPatches list. Patches with a status of *INSTALLED_REJECTED* were typically installed before they were added to a RejectedPatches list.
        
              .. note::
        
                If ALLOW_AS_DEPENDENCY is the specified option for RejectedPatchesAction, the value of InstancesWithInstalledRejectedPatches will always be 0 (zero).
        
            - **InstancesWithMissingPatches** *(integer) --* 
        
              The number of instances with missing patches from the patch baseline.
        
            - **InstancesWithFailedPatches** *(integer) --* 
        
              The number of instances with patches from the patch baseline that failed to install.
        
            - **InstancesWithNotApplicablePatches** *(integer) --* 
        
              The number of instances with patches that aren\'t applicable.
        
        """
        pass

    def describe_patch_groups(self, MaxResults: int = None, Filters: List = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribePatchGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_patch_groups(
              MaxResults=123,
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              NextToken=\'string\'
          )
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of patch groups to return (per page).
        
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
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Mappings\': [
                    {
                        \'PatchGroup\': \'string\',
                        \'BaselineIdentity\': {
                            \'BaselineId\': \'string\',
                            \'BaselineName\': \'string\',
                            \'OperatingSystem\': \'WINDOWS\'|\'AMAZON_LINUX\'|\'AMAZON_LINUX_2\'|\'UBUNTU\'|\'REDHAT_ENTERPRISE_LINUX\'|\'SUSE\'|\'CENTOS\',
                            \'BaselineDescription\': \'string\',
                            \'DefaultBaseline\': True|False
                        }
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def describe_sessions(self, State: str, MaxResults: int = None, NextToken: str = None, Filters: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeSessions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_sessions(
              State=\'Active\'|\'History\',
              MaxResults=123,
              NextToken=\'string\',
              Filters=[
                  {
                      \'key\': \'InvokedAfter\'|\'InvokedBefore\'|\'Target\'|\'Owner\'|\'Status\',
                      \'value\': \'string\'
                  },
              ]
          )
        :type State: string
        :param State: **[REQUIRED]** 
        
          The session status to retrieve a list of sessions for. For example, \"Active\".
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
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
                 
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Sessions\': [
                    {
                        \'SessionId\': \'string\',
                        \'Target\': \'string\',
                        \'Status\': \'Connected\'|\'Connecting\'|\'Disconnected\'|\'Terminated\'|\'Terminating\'|\'Failed\',
                        \'StartDate\': datetime(2015, 1, 1),
                        \'EndDate\': datetime(2015, 1, 1),
                        \'DocumentName\': \'string\',
                        \'Owner\': \'string\',
                        \'Details\': \'string\',
                        \'OutputUrl\': {
                            \'S3OutputUrl\': \'string\',
                            \'CloudWatchOutputUrl\': \'string\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  The status of the session. For example, \"Connected\" or \"Terminated\".
        
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
        
            - **NextToken** *(string) --* 
        
              The token for the next set of items to return. (You received this token from a previous call.)
        
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

    def get_automation_execution(self, AutomationExecutionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetAutomationExecution>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_automation_execution(
              AutomationExecutionId=\'string\'
          )
        :type AutomationExecutionId: string
        :param AutomationExecutionId: **[REQUIRED]** 
        
          The unique identifier for an existing automation execution to examine. The execution ID is returned by StartAutomationExecution when the execution of an Automation document is initiated.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AutomationExecution\': {
                    \'AutomationExecutionId\': \'string\',
                    \'DocumentName\': \'string\',
                    \'DocumentVersion\': \'string\',
                    \'ExecutionStartTime\': datetime(2015, 1, 1),
                    \'ExecutionEndTime\': datetime(2015, 1, 1),
                    \'AutomationExecutionStatus\': \'Pending\'|\'InProgress\'|\'Waiting\'|\'Success\'|\'TimedOut\'|\'Cancelling\'|\'Cancelled\'|\'Failed\',
                    \'StepExecutions\': [
                        {
                            \'StepName\': \'string\',
                            \'Action\': \'string\',
                            \'TimeoutSeconds\': 123,
                            \'OnFailure\': \'string\',
                            \'MaxAttempts\': 123,
                            \'ExecutionStartTime\': datetime(2015, 1, 1),
                            \'ExecutionEndTime\': datetime(2015, 1, 1),
                            \'StepStatus\': \'Pending\'|\'InProgress\'|\'Waiting\'|\'Success\'|\'TimedOut\'|\'Cancelling\'|\'Cancelled\'|\'Failed\',
                            \'ResponseCode\': \'string\',
                            \'Inputs\': {
                                \'string\': \'string\'
                            },
                            \'Outputs\': {
                                \'string\': [
                                    \'string\',
                                ]
                            },
                            \'Response\': \'string\',
                            \'FailureMessage\': \'string\',
                            \'FailureDetails\': {
                                \'FailureStage\': \'string\',
                                \'FailureType\': \'string\',
                                \'Details\': {
                                    \'string\': [
                                        \'string\',
                                    ]
                                }
                            },
                            \'StepExecutionId\': \'string\',
                            \'OverriddenParameters\': {
                                \'string\': [
                                    \'string\',
                                ]
                            },
                            \'IsEnd\': True|False,
                            \'NextStep\': \'string\',
                            \'IsCritical\': True|False,
                            \'ValidNextSteps\': [
                                \'string\',
                            ]
                        },
                    ],
                    \'StepExecutionsTruncated\': True|False,
                    \'Parameters\': {
                        \'string\': [
                            \'string\',
                        ]
                    },
                    \'Outputs\': {
                        \'string\': [
                            \'string\',
                        ]
                    },
                    \'FailureMessage\': \'string\',
                    \'Mode\': \'Auto\'|\'Interactive\',
                    \'ParentAutomationExecutionId\': \'string\',
                    \'ExecutedBy\': \'string\',
                    \'CurrentStepName\': \'string\',
                    \'CurrentAction\': \'string\',
                    \'TargetParameterName\': \'string\',
                    \'Targets\': [
                        {
                            \'Key\': \'string\',
                            \'Values\': [
                                \'string\',
                            ]
                        },
                    ],
                    \'TargetMaps\': [
                        {
                            \'string\': [
                                \'string\',
                            ]
                        },
                    ],
                    \'ResolvedTargets\': {
                        \'ParameterValues\': [
                            \'string\',
                        ],
                        \'Truncated\': True|False
                    },
                    \'MaxConcurrency\': \'string\',
                    \'MaxErrors\': \'string\',
                    \'Target\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AutomationExecution** *(dict) --* 
        
              Detailed information about the current state of an automation execution.
        
              - **AutomationExecutionId** *(string) --* 
        
                The execution ID.
        
              - **DocumentName** *(string) --* 
        
                The name of the Automation document used during the execution.
        
              - **DocumentVersion** *(string) --* 
        
                The version of the document to use during execution.
        
              - **ExecutionStartTime** *(datetime) --* 
        
                The time the execution started.
        
              - **ExecutionEndTime** *(datetime) --* 
        
                The time the execution finished.
        
              - **AutomationExecutionStatus** *(string) --* 
        
                The execution status of the Automation.
        
              - **StepExecutions** *(list) --* 
        
                A list of details about the current state of all steps that comprise an execution. An Automation document contains a list of steps that are executed in order.
        
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
        
                    A user-specified list of parameters to override when executing a step.
        
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
        
                    Strategies used when step fails, we support Continue and Abort. Abort will fail the automation when the step fails. Continue will ignore the failure of current step and allow automation to execute the next step. With conditional branching, we add step:stepName to support the automation to go to another specific step.
        
                    - *(string) --* 
                
              - **StepExecutionsTruncated** *(boolean) --* 
        
                A boolean value that indicates if the response contains the full list of the Automation step executions. If true, use the DescribeAutomationStepExecutions API action to get the full list of step executions.
        
              - **Parameters** *(dict) --* 
        
                The key-value map of execution parameters, which were supplied when calling StartAutomationExecution.
        
                - *(string) --* 
                  
                  - *(list) --* 
                    
                    - *(string) --* 
                
              - **Outputs** *(dict) --* 
        
                The list of execution outputs as defined in the automation document.
        
                - *(string) --* 
                  
                  - *(list) --* 
                    
                    - *(string) --* 
                
              - **FailureMessage** *(string) --* 
        
                A message describing why an execution has failed, if the status is set to Failed.
        
              - **Mode** *(string) --* 
        
                The automation execution mode.
        
              - **ParentAutomationExecutionId** *(string) --* 
        
                The AutomationExecutionId of the parent automation.
        
              - **ExecutedBy** *(string) --* 
        
                The Amazon Resource Name (ARN) of the user who executed the automation.
        
              - **CurrentStepName** *(string) --* 
        
                The name of the currently executing step.
        
              - **CurrentAction** *(string) --* 
        
                The action of the currently executing step.
        
              - **TargetParameterName** *(string) --* 
        
                The parameter name.
        
              - **Targets** *(list) --* 
        
                The specified targets.
        
                - *(dict) --* 
        
                  An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                  - **Key** *(string) --* 
        
                    User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                  - **Values** *(list) --* 
        
                    User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
                    - *(string) --* 
                
              - **TargetMaps** *(list) --* 
        
                The specified key-value mapping of document parameters to target resources.
        
                - *(dict) --* 
                  
                  - *(string) --* 
                    
                    - *(list) --* 
                      
                      - *(string) --* 
                  
              - **ResolvedTargets** *(dict) --* 
        
                A list of resolved targets in the rate control execution.
        
                - **ParameterValues** *(list) --* 
        
                  A list of parameter values sent to targets that resolved during the Automation execution.
        
                  - *(string) --* 
              
                - **Truncated** *(boolean) --* 
        
                  A boolean value indicating whether the resolved target list is truncated.
        
              - **MaxConcurrency** *(string) --* 
        
                The MaxConcurrency value specified by the user when the execution started.
        
              - **MaxErrors** *(string) --* 
        
                The MaxErrors value specified by the user when the execution started.
        
              - **Target** *(string) --* 
        
                The target of the execution.
        
        """
        pass

    def get_command_invocation(self, CommandId: str, InstanceId: str, PluginName: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetCommandInvocation>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_command_invocation(
              CommandId=\'string\',
              InstanceId=\'string\',
              PluginName=\'string\'
          )
        :type CommandId: string
        :param CommandId: **[REQUIRED]** 
        
          (Required) The parent command ID of the invocation plugin.
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          (Required) The ID of the managed instance targeted by the command. A managed instance can be an Amazon EC2 instance or an instance in your hybrid environment that is configured for Systems Manager.
        
        :type PluginName: string
        :param PluginName: 
        
          (Optional) The name of the plugin for which you want detailed results. If the document contains only one plugin, the name can be omitted and the details will be returned.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CommandId\': \'string\',
                \'InstanceId\': \'string\',
                \'Comment\': \'string\',
                \'DocumentName\': \'string\',
                \'DocumentVersion\': \'string\',
                \'PluginName\': \'string\',
                \'ResponseCode\': 123,
                \'ExecutionStartDateTime\': \'string\',
                \'ExecutionElapsedTime\': \'string\',
                \'ExecutionEndDateTime\': \'string\',
                \'Status\': \'Pending\'|\'InProgress\'|\'Delayed\'|\'Success\'|\'Cancelled\'|\'TimedOut\'|\'Failed\'|\'Cancelling\',
                \'StatusDetails\': \'string\',
                \'StandardOutputContent\': \'string\',
                \'StandardOutputUrl\': \'string\',
                \'StandardErrorContent\': \'string\',
                \'StandardErrorUrl\': \'string\',
                \'CloudWatchOutputConfig\': {
                    \'CloudWatchLogGroupName\': \'string\',
                    \'CloudWatchOutputEnabled\': True|False
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CommandId** *(string) --* 
        
              The parent command ID of the invocation plugin.
        
            - **InstanceId** *(string) --* 
        
              The ID of the managed instance targeted by the command. A managed instance can be an Amazon EC2 instance or an instance in your hybrid environment that is configured for Systems Manager.
        
            - **Comment** *(string) --* 
        
              The comment text for the command.
        
            - **DocumentName** *(string) --* 
        
              The name of the document that was executed. For example, AWS-RunShellScript.
        
            - **DocumentVersion** *(string) --* 
        
              The SSM document version used in the request.
        
            - **PluginName** *(string) --* 
        
              The name of the plugin for which you want detailed results. For example, aws:RunShellScript is a plugin.
        
            - **ResponseCode** *(integer) --* 
        
              The error level response code for the plugin script. If the response code is -1, then the command has not started executing on the instance, or it was not received by the instance.
        
            - **ExecutionStartDateTime** *(string) --* 
        
              The date and time the plugin started executing. Date and time are written in ISO 8601 format. For example, June 7, 2017 is represented as 2017-06-7. The following sample AWS CLI command uses the ``InvokedBefore`` filter.
        
               ``aws ssm list-commands --filters key=InvokedBefore,value=2017-06-07T00:00:00Z``  
        
              If the plugin has not started to execute, the string is empty.
        
            - **ExecutionElapsedTime** *(string) --* 
        
              Duration since ExecutionStartDateTime.
        
            - **ExecutionEndDateTime** *(string) --* 
        
              The date and time the plugin was finished executing. Date and time are written in ISO 8601 format. For example, June 7, 2017 is represented as 2017-06-7. The following sample AWS CLI command uses the ``InvokedAfter`` filter.
        
               ``aws ssm list-commands --filters key=InvokedAfter,value=2017-06-07T00:00:00Z``  
        
              If the plugin has not started to execute, the string is empty.
        
            - **Status** *(string) --* 
        
              The status of this invocation plugin. This status can be different than StatusDetails.
        
            - **StatusDetails** *(string) --* 
        
              A detailed status of the command execution for an invocation. StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see `Understanding Command Statuses <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* . StatusDetails can be one of the following values:
        
              * Pending: The command has not been sent to the instance. 
               
              * In Progress: The command has been sent to the instance but has not reached a terminal state. 
               
              * Delayed: The system attempted to send the command to the target, but the target was not available. The instance might not be available because of network issues, the instance was stopped, etc. The system will try to deliver the command again. 
               
              * Success: The command or plugin was executed successfully. This is a terminal state. 
               
              * Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command\'s MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
               
              * Execution Timed Out: The command started to execute on the instance, but the execution was not complete before the timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state. 
               
              * Failed: The command wasn\'t executed successfully on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state. 
               
              * Canceled: The command was terminated before it was completed. This is a terminal state. 
               
              * Undeliverable: The command can\'t be delivered to the instance. The instance might not exist or might not be responding. Undeliverable invocations don\'t count against the parent command\'s MaxErrors limit and don\'t contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
               
              * Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state. 
               
            - **StandardOutputContent** *(string) --* 
        
              The first 24,000 characters written by the plugin to stdout. If the command has not finished executing, if ExecutionStatus is neither Succeeded nor Failed, then this string is empty.
        
            - **StandardOutputUrl** *(string) --* 
        
              The URL for the complete text written by the plugin to stdout in Amazon S3. If an Amazon S3 bucket was not specified, then this string is empty.
        
            - **StandardErrorContent** *(string) --* 
        
              The first 8,000 characters written by the plugin to stderr. If the command has not finished executing, then this string is empty.
        
            - **StandardErrorUrl** *(string) --* 
        
              The URL for the complete text written by the plugin to stderr. If the command has not finished executing, then this string is empty.
        
            - **CloudWatchOutputConfig** *(dict) --* 
        
              CloudWatch Logs information where Systems Manager sent the command output.
        
              - **CloudWatchLogGroupName** *(string) --* 
        
                The name of the CloudWatch log group where you want to send command output. If you don\'t specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/*SystemsManagerDocumentName* .
        
              - **CloudWatchOutputEnabled** *(boolean) --* 
        
                Enables Systems Manager to send command output to CloudWatch Logs.
        
        """
        pass

    def get_connection_status(self, Target: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetConnectionStatus>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_connection_status(
              Target=\'string\'
          )
        :type Target: string
        :param Target: **[REQUIRED]** 
        
          The ID of the instance.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Target\': \'string\',
                \'Status\': \'Connected\'|\'NotConnected\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Target** *(string) --* 
        
              The ID of the instance to check connection status. 
        
            - **Status** *(string) --* 
        
              The status of the connection to the instance. For example, \'Connected\' or \'Not Connected\'.
        
        """
        pass

    def get_default_patch_baseline(self, OperatingSystem: str = None) -> Dict:
        """
        
        If you do not specify an operating system value, the default patch baseline for Windows is returned.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetDefaultPatchBaseline>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_default_patch_baseline(
              OperatingSystem=\'WINDOWS\'|\'AMAZON_LINUX\'|\'AMAZON_LINUX_2\'|\'UBUNTU\'|\'REDHAT_ENTERPRISE_LINUX\'|\'SUSE\'|\'CENTOS\'
          )
        :type OperatingSystem: string
        :param OperatingSystem: 
        
          Returns the default patch baseline for the specified operating system.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'BaselineId\': \'string\',
                \'OperatingSystem\': \'WINDOWS\'|\'AMAZON_LINUX\'|\'AMAZON_LINUX_2\'|\'UBUNTU\'|\'REDHAT_ENTERPRISE_LINUX\'|\'SUSE\'|\'CENTOS\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **BaselineId** *(string) --* 
        
              The ID of the default patch baseline.
        
            - **OperatingSystem** *(string) --* 
        
              The operating system for the returned patch baseline. 
        
        """
        pass

    def get_deployable_patch_snapshot_for_instance(self, InstanceId: str, SnapshotId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetDeployablePatchSnapshotForInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_deployable_patch_snapshot_for_instance(
              InstanceId=\'string\',
              SnapshotId=\'string\'
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The ID of the instance for which the appropriate patch snapshot should be retrieved.
        
        :type SnapshotId: string
        :param SnapshotId: **[REQUIRED]** 
        
          The user-defined snapshot ID.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'InstanceId\': \'string\',
                \'SnapshotId\': \'string\',
                \'SnapshotDownloadUrl\': \'string\',
                \'Product\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **InstanceId** *(string) --* 
        
              The ID of the instance.
        
            - **SnapshotId** *(string) --* 
        
              The user-defined snapshot ID.
        
            - **SnapshotDownloadUrl** *(string) --* 
        
              A pre-signed Amazon S3 URL that can be used to download the patch snapshot.
        
            - **Product** *(string) --* 
        
              Returns the specific operating system (for example Windows Server 2012 or Amazon Linux 2015.09) on the instance for the specified patch snapshot.
        
        """
        pass

    def get_document(self, Name: str, DocumentVersion: str = None, DocumentFormat: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetDocument>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_document(
              Name=\'string\',
              DocumentVersion=\'string\',
              DocumentFormat=\'YAML\'|\'JSON\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the Systems Manager document.
        
        :type DocumentVersion: string
        :param DocumentVersion: 
        
          The document version for which you want information.
        
        :type DocumentFormat: string
        :param DocumentFormat: 
        
          Returns the document in the specified format. The document format can be either JSON or YAML. JSON is the default format.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Name\': \'string\',
                \'DocumentVersion\': \'string\',
                \'Content\': \'string\',
                \'DocumentType\': \'Command\'|\'Policy\'|\'Automation\'|\'Session\',
                \'DocumentFormat\': \'YAML\'|\'JSON\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Name** *(string) --* 
        
              The name of the Systems Manager document.
        
            - **DocumentVersion** *(string) --* 
        
              The document version.
        
            - **Content** *(string) --* 
        
              The contents of the Systems Manager document.
        
            - **DocumentType** *(string) --* 
        
              The document type.
        
            - **DocumentFormat** *(string) --* 
        
              The document format, either JSON or YAML.
        
        """
        pass

    def get_inventory(self, Filters: List = None, Aggregators: List = None, ResultAttributes: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetInventory>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_inventory(
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ],
                      \'Type\': \'Equal\'|\'NotEqual\'|\'BeginWith\'|\'LessThan\'|\'GreaterThan\'|\'Exists\'
                  },
              ],
              Aggregators=[
                  {
                      \'Expression\': \'string\',
                      \'Aggregators\': {\'... recursive ...\'},
                      \'Groups\': [
                          {
                              \'Name\': \'string\',
                              \'Filters\': [
                                  {
                                      \'Key\': \'string\',
                                      \'Values\': [
                                          \'string\',
                                      ],
                                      \'Type\': \'Equal\'|\'NotEqual\'|\'BeginWith\'|\'LessThan\'|\'GreaterThan\'|\'Exists\'
                                  },
                              ]
                          },
                      ]
                  },
              ],
              ResultAttributes=[
                  {
                      \'TypeName\': \'string\'
                  },
              ],
              NextToken=\'string\',
              MaxResults=123
          )
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
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Entities\': [
                    {
                        \'Id\': \'string\',
                        \'Data\': {
                            \'string\': {
                                \'TypeName\': \'string\',
                                \'SchemaVersion\': \'string\',
                                \'CaptureTime\': \'string\',
                                \'ContentHash\': \'string\',
                                \'Content\': [
                                    {
                                        \'string\': \'string\'
                                    },
                                ]
                            }
                        }
                    },
                ],
                \'NextToken\': \'string\'
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
                      
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def get_inventory_schema(self, TypeName: str = None, NextToken: str = None, MaxResults: int = None, Aggregator: bool = None, SubType: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetInventorySchema>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_inventory_schema(
              TypeName=\'string\',
              NextToken=\'string\',
              MaxResults=123,
              Aggregator=True|False,
              SubType=True|False
          )
        :type TypeName: string
        :param TypeName: 
        
          The type of inventory item to return.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type Aggregator: boolean
        :param Aggregator: 
        
          Returns inventory schemas that support aggregation. For example, this call returns the ``AWS:InstanceInformation`` type, because it supports aggregation based on the ``PlatformName`` , ``PlatformType`` , and ``PlatformVersion`` attributes.
        
        :type SubType: boolean
        :param SubType: 
        
          Returns the sub-type schema for a specified inventory type.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Schemas\': [
                    {
                        \'TypeName\': \'string\',
                        \'Version\': \'string\',
                        \'Attributes\': [
                            {
                                \'Name\': \'string\',
                                \'DataType\': \'string\'|\'number\'
                            },
                        ],
                        \'DisplayName\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def get_maintenance_window(self, WindowId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetMaintenanceWindow>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_maintenance_window(
              WindowId=\'string\'
          )
        :type WindowId: string
        :param WindowId: **[REQUIRED]** 
        
          The ID of the desired Maintenance Window.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowId\': \'string\',
                \'Name\': \'string\',
                \'Description\': \'string\',
                \'StartDate\': \'string\',
                \'EndDate\': \'string\',
                \'Schedule\': \'string\',
                \'ScheduleTimezone\': \'string\',
                \'NextExecutionTime\': \'string\',
                \'Duration\': 123,
                \'Cutoff\': 123,
                \'AllowUnassociatedTargets\': True|False,
                \'Enabled\': True|False,
                \'CreatedDate\': datetime(2015, 1, 1),
                \'ModifiedDate\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **WindowId** *(string) --* 
        
              The ID of the created Maintenance Window.
        
            - **Name** *(string) --* 
        
              The name of the Maintenance Window.
        
            - **Description** *(string) --* 
        
              The description of the Maintenance Window.
        
            - **StartDate** *(string) --* 
        
              The date and time, in ISO-8601 Extended format, for when the Maintenance Window is scheduled to become active. The Maintenance Window will not run before this specified time.
        
            - **EndDate** *(string) --* 
        
              The date and time, in ISO-8601 Extended format, for when the Maintenance Window is scheduled to become inactive. The Maintenance Window will not run after this specified time.
        
            - **Schedule** *(string) --* 
        
              The schedule of the Maintenance Window in the form of a cron or rate expression.
        
            - **ScheduleTimezone** *(string) --* 
        
              The time zone that the scheduled Maintenance Window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: \"America/Los_Angeles\", \"etc/UTC\", or \"Asia/Seoul\". For more information, see the `Time Zone Database <https://www.iana.org/time-zones>`__ on the IANA website.
        
            - **NextExecutionTime** *(string) --* 
        
              The next time the Maintenance Window will actually run, taking into account any specified times for the Maintenance Window to become active or inactive.
        
            - **Duration** *(integer) --* 
        
              The duration of the Maintenance Window in hours.
        
            - **Cutoff** *(integer) --* 
        
              The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.
        
            - **AllowUnassociatedTargets** *(boolean) --* 
        
              Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.
        
            - **Enabled** *(boolean) --* 
        
              Whether the Maintenance Windows is enabled.
        
            - **CreatedDate** *(datetime) --* 
        
              The date the Maintenance Window was created.
        
            - **ModifiedDate** *(datetime) --* 
        
              The date the Maintenance Window was last modified.
        
        """
        pass

    def get_maintenance_window_execution(self, WindowExecutionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetMaintenanceWindowExecution>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_maintenance_window_execution(
              WindowExecutionId=\'string\'
          )
        :type WindowExecutionId: string
        :param WindowExecutionId: **[REQUIRED]** 
        
          The ID of the Maintenance Window execution that includes the task.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowExecutionId\': \'string\',
                \'TaskIds\': [
                    \'string\',
                ],
                \'Status\': \'PENDING\'|\'IN_PROGRESS\'|\'SUCCESS\'|\'FAILED\'|\'TIMED_OUT\'|\'CANCELLING\'|\'CANCELLED\'|\'SKIPPED_OVERLAPPING\',
                \'StatusDetails\': \'string\',
                \'StartTime\': datetime(2015, 1, 1),
                \'EndTime\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **WindowExecutionId** *(string) --* 
        
              The ID of the Maintenance Window execution.
        
            - **TaskIds** *(list) --* 
        
              The ID of the task executions from the Maintenance Window execution.
        
              - *(string) --* 
          
            - **Status** *(string) --* 
        
              The status of the Maintenance Window execution.
        
            - **StatusDetails** *(string) --* 
        
              The details explaining the Status. Only available for certain status values.
        
            - **StartTime** *(datetime) --* 
        
              The time the Maintenance Window started executing.
        
            - **EndTime** *(datetime) --* 
        
              The time the Maintenance Window finished executing.
        
        """
        pass

    def get_maintenance_window_execution_task(self, WindowExecutionId: str, TaskId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetMaintenanceWindowExecutionTask>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_maintenance_window_execution_task(
              WindowExecutionId=\'string\',
              TaskId=\'string\'
          )
        :type WindowExecutionId: string
        :param WindowExecutionId: **[REQUIRED]** 
        
          The ID of the Maintenance Window execution that includes the task.
        
        :type TaskId: string
        :param TaskId: **[REQUIRED]** 
        
          The ID of the specific task execution in the Maintenance Window task that should be retrieved.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowExecutionId\': \'string\',
                \'TaskExecutionId\': \'string\',
                \'TaskArn\': \'string\',
                \'ServiceRole\': \'string\',
                \'Type\': \'RUN_COMMAND\'|\'AUTOMATION\'|\'STEP_FUNCTIONS\'|\'LAMBDA\',
                \'TaskParameters\': [
                    {
                        \'string\': {
                            \'Values\': [
                                \'string\',
                            ]
                        }
                    },
                ],
                \'Priority\': 123,
                \'MaxConcurrency\': \'string\',
                \'MaxErrors\': \'string\',
                \'Status\': \'PENDING\'|\'IN_PROGRESS\'|\'SUCCESS\'|\'FAILED\'|\'TIMED_OUT\'|\'CANCELLING\'|\'CANCELLED\'|\'SKIPPED_OVERLAPPING\',
                \'StatusDetails\': \'string\',
                \'StartTime\': datetime(2015, 1, 1),
                \'EndTime\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **WindowExecutionId** *(string) --* 
        
              The ID of the Maintenance Window execution that includes the task.
        
            - **TaskExecutionId** *(string) --* 
        
              The ID of the specific task execution in the Maintenance Window task that was retrieved.
        
            - **TaskArn** *(string) --* 
        
              The ARN of the executed task.
        
            - **ServiceRole** *(string) --* 
        
              The role that was assumed when executing the task.
        
            - **Type** *(string) --* 
        
              The type of task executed.
        
            - **TaskParameters** *(list) --* 
        
              The parameters passed to the task when it was executed.
        
              .. note::
        
                 ``TaskParameters`` has been deprecated. To specify parameters to pass to a task when it runs, instead use the ``Parameters`` option in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
        
              The map has the following format:
        
              Key: string, between 1 and 255 characters
        
              Value: an array of strings, each string is between 1 and 255 characters
        
              - *(dict) --* 
                
                - *(string) --* 
                  
                  - *(dict) --* 
        
                    Defines the values for a task parameter.
        
                    - **Values** *(list) --* 
        
                      This field contains an array of 0 or more strings, each 1 to 255 characters in length.
        
                      - *(string) --* 
                  
            - **Priority** *(integer) --* 
        
              The priority of the task.
        
            - **MaxConcurrency** *(string) --* 
        
              The defined maximum number of task executions that could be run in parallel.
        
            - **MaxErrors** *(string) --* 
        
              The defined maximum number of task execution errors allowed before scheduling of the task execution would have been stopped.
        
            - **Status** *(string) --* 
        
              The status of the task.
        
            - **StatusDetails** *(string) --* 
        
              The details explaining the Status. Only available for certain status values.
        
            - **StartTime** *(datetime) --* 
        
              The time the task execution started.
        
            - **EndTime** *(datetime) --* 
        
              The time the task execution completed.
        
        """
        pass

    def get_maintenance_window_execution_task_invocation(self, WindowExecutionId: str, TaskId: str, InvocationId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetMaintenanceWindowExecutionTaskInvocation>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_maintenance_window_execution_task_invocation(
              WindowExecutionId=\'string\',
              TaskId=\'string\',
              InvocationId=\'string\'
          )
        :type WindowExecutionId: string
        :param WindowExecutionId: **[REQUIRED]** 
        
          The ID of the Maintenance Window execution for which the task is a part.
        
        :type TaskId: string
        :param TaskId: **[REQUIRED]** 
        
          The ID of the specific task in the Maintenance Window task that should be retrieved. 
        
        :type InvocationId: string
        :param InvocationId: **[REQUIRED]** 
        
          The invocation ID to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowExecutionId\': \'string\',
                \'TaskExecutionId\': \'string\',
                \'InvocationId\': \'string\',
                \'ExecutionId\': \'string\',
                \'TaskType\': \'RUN_COMMAND\'|\'AUTOMATION\'|\'STEP_FUNCTIONS\'|\'LAMBDA\',
                \'Parameters\': \'string\',
                \'Status\': \'PENDING\'|\'IN_PROGRESS\'|\'SUCCESS\'|\'FAILED\'|\'TIMED_OUT\'|\'CANCELLING\'|\'CANCELLED\'|\'SKIPPED_OVERLAPPING\',
                \'StatusDetails\': \'string\',
                \'StartTime\': datetime(2015, 1, 1),
                \'EndTime\': datetime(2015, 1, 1),
                \'OwnerInformation\': \'string\',
                \'WindowTargetId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **WindowExecutionId** *(string) --* 
        
              The Maintenance Window execution ID.
        
            - **TaskExecutionId** *(string) --* 
        
              The task execution ID.
        
            - **InvocationId** *(string) --* 
        
              The invocation ID.
        
            - **ExecutionId** *(string) --* 
        
              The execution ID.
        
            - **TaskType** *(string) --* 
        
              Retrieves the task type for a Maintenance Window. Task types include the following: LAMBDA, STEP_FUNCTION, AUTOMATION, RUN_COMMAND.
        
            - **Parameters** *(string) --* 
        
              The parameters used at the time that the task executed.
        
            - **Status** *(string) --* 
        
              The task status for an invocation.
        
            - **StatusDetails** *(string) --* 
        
              The details explaining the status. Details are only available for certain status values.
        
            - **StartTime** *(datetime) --* 
        
              The time that the task started executing on the target.
        
            - **EndTime** *(datetime) --* 
        
              The time that the task finished executing on the target.
        
            - **OwnerInformation** *(string) --* 
        
              User-provided value to be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window. 
        
            - **WindowTargetId** *(string) --* 
        
              The Maintenance Window target ID.
        
        """
        pass

    def get_maintenance_window_task(self, WindowId: str, WindowTaskId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetMaintenanceWindowTask>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_maintenance_window_task(
              WindowId=\'string\',
              WindowTaskId=\'string\'
          )
        :type WindowId: string
        :param WindowId: **[REQUIRED]** 
        
          The Maintenance Window ID that includes the task to retrieve.
        
        :type WindowTaskId: string
        :param WindowTaskId: **[REQUIRED]** 
        
          The Maintenance Window task ID to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowId\': \'string\',
                \'WindowTaskId\': \'string\',
                \'Targets\': [
                    {
                        \'Key\': \'string\',
                        \'Values\': [
                            \'string\',
                        ]
                    },
                ],
                \'TaskArn\': \'string\',
                \'ServiceRoleArn\': \'string\',
                \'TaskType\': \'RUN_COMMAND\'|\'AUTOMATION\'|\'STEP_FUNCTIONS\'|\'LAMBDA\',
                \'TaskParameters\': {
                    \'string\': {
                        \'Values\': [
                            \'string\',
                        ]
                    }
                },
                \'TaskInvocationParameters\': {
                    \'RunCommand\': {
                        \'Comment\': \'string\',
                        \'DocumentHash\': \'string\',
                        \'DocumentHashType\': \'Sha256\'|\'Sha1\',
                        \'NotificationConfig\': {
                            \'NotificationArn\': \'string\',
                            \'NotificationEvents\': [
                                \'All\'|\'InProgress\'|\'Success\'|\'TimedOut\'|\'Cancelled\'|\'Failed\',
                            ],
                            \'NotificationType\': \'Command\'|\'Invocation\'
                        },
                        \'OutputS3BucketName\': \'string\',
                        \'OutputS3KeyPrefix\': \'string\',
                        \'Parameters\': {
                            \'string\': [
                                \'string\',
                            ]
                        },
                        \'ServiceRoleArn\': \'string\',
                        \'TimeoutSeconds\': 123
                    },
                    \'Automation\': {
                        \'DocumentVersion\': \'string\',
                        \'Parameters\': {
                            \'string\': [
                                \'string\',
                            ]
                        }
                    },
                    \'StepFunctions\': {
                        \'Input\': \'string\',
                        \'Name\': \'string\'
                    },
                    \'Lambda\': {
                        \'ClientContext\': \'string\',
                        \'Qualifier\': \'string\',
                        \'Payload\': b\'bytes\'
                    }
                },
                \'Priority\': 123,
                \'MaxConcurrency\': \'string\',
                \'MaxErrors\': \'string\',
                \'LoggingInfo\': {
                    \'S3BucketName\': \'string\',
                    \'S3KeyPrefix\': \'string\',
                    \'S3Region\': \'string\'
                },
                \'Name\': \'string\',
                \'Description\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **WindowId** *(string) --* 
        
              The retrieved Maintenance Window ID.
        
            - **WindowTaskId** *(string) --* 
        
              The retrieved Maintenance Window task ID.
        
            - **Targets** *(list) --* 
        
              The targets where the task should execute.
        
              - *(dict) --* 
        
                An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                - **Key** *(string) --* 
        
                  User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                - **Values** *(list) --* 
        
                  User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
                  - *(string) --* 
              
            - **TaskArn** *(string) --* 
        
              The resource that the task used during execution. For RUN_COMMAND and AUTOMATION task types, the TaskArn is the Systems Manager Document name/ARN. For LAMBDA tasks, the value is the function name/ARN. For STEP_FUNCTION tasks, the value is the state machine ARN.
        
            - **ServiceRoleArn** *(string) --* 
        
              The IAM service role to assume during task execution.
        
            - **TaskType** *(string) --* 
        
              The type of task to execute.
        
            - **TaskParameters** *(dict) --* 
        
              The parameters to pass to the task when it executes.
        
              .. note::
        
                 ``TaskParameters`` has been deprecated. To specify parameters to pass to a task when it runs, instead use the ``Parameters`` option in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
        
              - *(string) --* 
                
                - *(dict) --* 
        
                  Defines the values for a task parameter.
        
                  - **Values** *(list) --* 
        
                    This field contains an array of 0 or more strings, each 1 to 255 characters in length.
        
                    - *(string) --* 
                
            - **TaskInvocationParameters** *(dict) --* 
        
              The parameters to pass to the task when it executes.
        
              - **RunCommand** *(dict) --* 
        
                The parameters for a RUN_COMMAND task type.
        
                - **Comment** *(string) --* 
        
                  Information about the command(s) to execute.
        
                - **DocumentHash** *(string) --* 
        
                  The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.
        
                - **DocumentHashType** *(string) --* 
        
                  SHA-256 or SHA-1. SHA-1 hashes have been deprecated.
        
                - **NotificationConfig** *(dict) --* 
        
                  Configurations for sending notifications about command status changes on a per-instance basis.
        
                  - **NotificationArn** *(string) --* 
        
                    An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.
        
                  - **NotificationEvents** *(list) --* 
        
                    The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Configuring Amazon SNS Notifications for Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/rc-sns-notifications.html>`__ in the *AWS Systems Manager User Guide* .
        
                    - *(string) --* 
                
                  - **NotificationType** *(string) --* 
        
                    Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 
        
                - **OutputS3BucketName** *(string) --* 
        
                  The name of the Amazon S3 bucket.
        
                - **OutputS3KeyPrefix** *(string) --* 
        
                  The Amazon S3 bucket subfolder.
        
                - **Parameters** *(dict) --* 
        
                  The parameters for the RUN_COMMAND task execution.
        
                  - *(string) --* 
                    
                    - *(list) --* 
                      
                      - *(string) --* 
                  
                - **ServiceRoleArn** *(string) --* 
        
                  The IAM service role to assume during task execution.
        
                - **TimeoutSeconds** *(integer) --* 
        
                  If this time is reached and the command has not already started executing, it doesn not execute.
        
              - **Automation** *(dict) --* 
        
                The parameters for an AUTOMATION task type.
        
                - **DocumentVersion** *(string) --* 
        
                  The version of an Automation document to use during task execution.
        
                - **Parameters** *(dict) --* 
        
                  The parameters for the AUTOMATION task.
        
                  For information about specifying and updating task parameters, see  RegisterTaskWithMaintenanceWindow and  UpdateMaintenanceWindowTask .
        
                  .. note::
        
                     ``LoggingInfo`` has been deprecated. To specify an S3 bucket to contain logs, instead use the ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
        
                     ``TaskParameters`` has been deprecated. To specify parameters to pass to a task when it runs, instead use the ``Parameters`` option in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
        
                    For AUTOMATION task types, Systems Manager ignores any values specified for these parameters.
        
                  - *(string) --* 
                    
                    - *(list) --* 
                      
                      - *(string) --* 
                  
              - **StepFunctions** *(dict) --* 
        
                The parameters for a STEP_FUNCTION task type.
        
                - **Input** *(string) --* 
        
                  The inputs for the STEP_FUNCTION task.
        
                - **Name** *(string) --* 
        
                  The name of the STEP_FUNCTION task.
        
              - **Lambda** *(dict) --* 
        
                The parameters for a LAMBDA task type.
        
                - **ClientContext** *(string) --* 
        
                  Pass client-specific information to the Lambda function that you are invoking. You can then process the client information in your Lambda function as you choose through the context variable.
        
                - **Qualifier** *(string) --* 
        
                  (Optional) Specify a Lambda function version or alias name. If you specify a function version, the action uses the qualified function ARN to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version to which the alias points.
        
                - **Payload** *(bytes) --* 
        
                  JSON to provide to your Lambda function as input.
        
            - **Priority** *(integer) --* 
        
              The priority of the task when it executes. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.
        
            - **MaxConcurrency** *(string) --* 
        
              The maximum number of targets allowed to run this task in parallel.
        
            - **MaxErrors** *(string) --* 
        
              The maximum number of errors allowed before the task stops being scheduled.
        
            - **LoggingInfo** *(dict) --* 
        
              The location in Amazon S3 where the task results are logged.
        
              .. note::
        
                 ``LoggingInfo`` has been deprecated. To specify an S3 bucket to contain logs, instead use the ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
        
              - **S3BucketName** *(string) --* 
        
                The name of an Amazon S3 bucket where execution logs are stored .
        
              - **S3KeyPrefix** *(string) --* 
        
                (Optional) The Amazon S3 bucket subfolder. 
        
              - **S3Region** *(string) --* 
        
                The region where the Amazon S3 bucket is located.
        
            - **Name** *(string) --* 
        
              The retrieved task name.
        
            - **Description** *(string) --* 
        
              The retrieved task description.
        
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

    def get_parameter(self, Name: str, WithDecryption: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetParameter>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_parameter(
              Name=\'string\',
              WithDecryption=True|False
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the parameter you want to query.
        
        :type WithDecryption: boolean
        :param WithDecryption: 
        
          Return decrypted values for secure string parameters. This flag is ignored for String and StringList parameter types.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Parameter\': {
                    \'Name\': \'string\',
                    \'Type\': \'String\'|\'StringList\'|\'SecureString\',
                    \'Value\': \'string\',
                    \'Version\': 123,
                    \'Selector\': \'string\',
                    \'SourceResult\': \'string\',
                    \'LastModifiedDate\': datetime(2015, 1, 1),
                    \'ARN\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Parameter** *(dict) --* 
        
              Information about a parameter.
        
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
        
        """
        pass

    def get_parameter_history(self, Name: str, WithDecryption: bool = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetParameterHistory>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_parameter_history(
              Name=\'string\',
              WithDecryption=True|False,
              MaxResults=123,
              NextToken=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of a parameter you want to query.
        
        :type WithDecryption: boolean
        :param WithDecryption: 
        
          Return decrypted values for secure string parameters. This flag is ignored for String and StringList parameter types.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Parameters\': [
                    {
                        \'Name\': \'string\',
                        \'Type\': \'String\'|\'StringList\'|\'SecureString\',
                        \'KeyId\': \'string\',
                        \'LastModifiedDate\': datetime(2015, 1, 1),
                        \'LastModifiedUser\': \'string\',
                        \'Description\': \'string\',
                        \'Value\': \'string\',
                        \'AllowedPattern\': \'string\',
                        \'Version\': 123,
                        \'Labels\': [
                            \'string\',
                        ]
                    },
                ],
                \'NextToken\': \'string\'
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
              
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def get_parameters(self, Names: List, WithDecryption: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetParameters>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_parameters(
              Names=[
                  \'string\',
              ],
              WithDecryption=True|False
          )
        :type Names: list
        :param Names: **[REQUIRED]** 
        
          Names of the parameters for which you want to query information.
        
          - *(string) --* 
        
        :type WithDecryption: boolean
        :param WithDecryption: 
        
          Return decrypted secure string value. Return decrypted values for secure string parameters. This flag is ignored for String and StringList parameter types.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Parameters\': [
                    {
                        \'Name\': \'string\',
                        \'Type\': \'String\'|\'StringList\'|\'SecureString\',
                        \'Value\': \'string\',
                        \'Version\': 123,
                        \'Selector\': \'string\',
                        \'SourceResult\': \'string\',
                        \'LastModifiedDate\': datetime(2015, 1, 1),
                        \'ARN\': \'string\'
                    },
                ],
                \'InvalidParameters\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Parameters** *(list) --* 
        
              A list of details for a parameter.
        
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
        
            - **InvalidParameters** *(list) --* 
        
              A list of parameters that are not formatted correctly or do not run when executed.
        
              - *(string) --* 
          
        """
        pass

    def get_parameters_by_path(self, Path: str, Recursive: bool = None, ParameterFilters: List = None, WithDecryption: bool = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        Request results are returned on a best-effort basis. If you specify ``MaxResults`` in the request, the response includes information up to the limit specified. The number of items returned, however, can be between zero and the value of ``MaxResults`` . If the service reaches an internal limit while processing the results, it stops the operation and returns the matching values up to that point and a ``NextToken`` . You can specify the ``NextToken`` in a subsequent call to get the next set of results.
        
        .. note::
        
          This API action doesn\'t support filtering by tags. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetParametersByPath>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_parameters_by_path(
              Path=\'string\',
              Recursive=True|False,
              ParameterFilters=[
                  {
                      \'Key\': \'string\',
                      \'Option\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              WithDecryption=True|False,
              MaxResults=123,
              NextToken=\'string\'
          )
        :type Path: string
        :param Path: **[REQUIRED]** 
        
          The hierarchy for the parameter. Hierarchies start with a forward slash (/) and end with the parameter name. A parameter name hierarchy can have a maximum of 15 levels. Here is an example of a hierarchy: ``/Finance/Prod/IAD/WinServ2016/license33``  
        
        :type Recursive: boolean
        :param Recursive: 
        
          Retrieve all parameters within a hierarchy.
        
          .. warning::
        
            If a user has access to a path, then the user can access all levels of that path. For example, if a user has permission to access path /a, then the user can also access /a/b. Even if a user has explicitly been denied access in IAM for parameter /a, they can still call the GetParametersByPath API action recursively and view /a/b.
        
        :type ParameterFilters: list
        :param ParameterFilters: 
        
          Filters to limit the request results.
        
          .. note::
        
            You can\'t filter using the parameter name.
        
          - *(dict) --* 
        
            One or more filters. Use a filter to return a more specific list of results.
        
            .. note::
        
              The ``Name`` field can\'t be used with the  GetParametersByPath API action.
        
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
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          A token to start the list. Use this token to get the next set of results. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Parameters\': [
                    {
                        \'Name\': \'string\',
                        \'Type\': \'String\'|\'StringList\'|\'SecureString\',
                        \'Value\': \'string\',
                        \'Version\': 123,
                        \'Selector\': \'string\',
                        \'SourceResult\': \'string\',
                        \'LastModifiedDate\': datetime(2015, 1, 1),
                        \'ARN\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token for the next set of items to return. Use this token to get the next set of results.
        
        """
        pass

    def get_patch_baseline(self, BaselineId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetPatchBaseline>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_patch_baseline(
              BaselineId=\'string\'
          )
        :type BaselineId: string
        :param BaselineId: **[REQUIRED]** 
        
          The ID of the patch baseline to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'BaselineId\': \'string\',
                \'Name\': \'string\',
                \'OperatingSystem\': \'WINDOWS\'|\'AMAZON_LINUX\'|\'AMAZON_LINUX_2\'|\'UBUNTU\'|\'REDHAT_ENTERPRISE_LINUX\'|\'SUSE\'|\'CENTOS\',
                \'GlobalFilters\': {
                    \'PatchFilters\': [
                        {
                            \'Key\': \'PRODUCT\'|\'CLASSIFICATION\'|\'MSRC_SEVERITY\'|\'PATCH_ID\'|\'SECTION\'|\'PRIORITY\'|\'SEVERITY\',
                            \'Values\': [
                                \'string\',
                            ]
                        },
                    ]
                },
                \'ApprovalRules\': {
                    \'PatchRules\': [
                        {
                            \'PatchFilterGroup\': {
                                \'PatchFilters\': [
                                    {
                                        \'Key\': \'PRODUCT\'|\'CLASSIFICATION\'|\'MSRC_SEVERITY\'|\'PATCH_ID\'|\'SECTION\'|\'PRIORITY\'|\'SEVERITY\',
                                        \'Values\': [
                                            \'string\',
                                        ]
                                    },
                                ]
                            },
                            \'ComplianceLevel\': \'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'INFORMATIONAL\'|\'UNSPECIFIED\',
                            \'ApproveAfterDays\': 123,
                            \'EnableNonSecurity\': True|False
                        },
                    ]
                },
                \'ApprovedPatches\': [
                    \'string\',
                ],
                \'ApprovedPatchesComplianceLevel\': \'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'INFORMATIONAL\'|\'UNSPECIFIED\',
                \'ApprovedPatchesEnableNonSecurity\': True|False,
                \'RejectedPatches\': [
                    \'string\',
                ],
                \'RejectedPatchesAction\': \'ALLOW_AS_DEPENDENCY\'|\'BLOCK\',
                \'PatchGroups\': [
                    \'string\',
                ],
                \'CreatedDate\': datetime(2015, 1, 1),
                \'ModifiedDate\': datetime(2015, 1, 1),
                \'Description\': \'string\',
                \'Sources\': [
                    {
                        \'Name\': \'string\',
                        \'Products\': [
                            \'string\',
                        ],
                        \'Configuration\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **BaselineId** *(string) --* 
        
              The ID of the retrieved patch baseline.
        
            - **Name** *(string) --* 
        
              The name of the patch baseline.
        
            - **OperatingSystem** *(string) --* 
        
              Returns the operating system specified for the patch baseline.
        
            - **GlobalFilters** *(dict) --* 
        
              A set of global filters used to exclude patches from the baseline.
        
              - **PatchFilters** *(list) --* 
        
                The set of patch filters that make up the group.
        
                - *(dict) --* 
        
                  Defines a patch filter.
        
                  A patch filter consists of key/value pairs, but not all keys are valid for all operating system types. For example, the key ``PRODUCT`` is valid for all supported operating system types. The key ``MSRC_SEVERITY`` , however, is valid only for Windows operating systems, and the key ``SECTION`` is valid only for Ubuntu operating systems.
        
                  Refer to the following sections for information about which keys may be used with each major operating system, and which values are valid for each key.
        
                   **Windows Operating Systems**  
        
                  The supported keys for Windows operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``MSRC_SEVERITY`` . See the following lists for valid values for each of these keys.
        
                   *Supported key:*  ``PRODUCT``  
        
                   *Supported values:*  
        
                  * ``Windows7``   
                   
                  * ``Windows8``   
                   
                  * ``Windows8.1``   
                   
                  * ``Windows8Embedded``   
                   
                  * ``Windows10``   
                   
                  * ``Windows10LTSB``   
                   
                  * ``WindowsServer2008``   
                   
                  * ``WindowsServer2008R2``   
                   
                  * ``WindowsServer2012``   
                   
                  * ``WindowsServer2012R2``   
                   
                  * ``WindowsServer2016``   
                   
                  * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                   
                   *Supported key:*  ``CLASSIFICATION``  
        
                   *Supported values:*  
        
                  * ``CriticalUpdates``   
                   
                  * ``DefinitionUpdates``   
                   
                  * ``Drivers``   
                   
                  * ``FeaturePacks``   
                   
                  * ``SecurityUpdates``   
                   
                  * ``ServicePacks``   
                   
                  * ``Tools``   
                   
                  * ``UpdateRollups``   
                   
                  * ``Updates``   
                   
                  * ``Upgrades``   
                   
                   *Supported key:*  ``MSRC_SEVERITY``  
        
                   *Supported values:*  
        
                  * ``Critical``   
                   
                  * ``Important``   
                   
                  * ``Moderate``   
                   
                  * ``Low``   
                   
                  * ``Unspecified``   
                   
                   **Ubuntu Operating Systems**  
        
                  The supported keys for Ubuntu operating systems are ``PRODUCT`` , ``PRIORITY`` , and ``SECTION`` . See the following lists for valid values for each of these keys.
        
                   *Supported key:*  ``PRODUCT``  
        
                   *Supported values:*  
        
                  * ``Ubuntu14.04``   
                   
                  * ``Ubuntu16.04``   
                   
                  * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                   
                   *Supported key:*  ``PRIORITY``  
        
                   *Supported values:*  
        
                  * ``Required``   
                   
                  * ``Important``   
                   
                  * ``Standard``   
                   
                  * ``Optional``   
                   
                  * ``Extra``   
                   
                   *Supported key:*  ``SECTION``  
        
                  Only the length of the key value is validated. Minimum length is 1. Maximum length is 64.
        
                   **Amazon Linux Operating Systems**  
        
                  The supported keys for Amazon Linux operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                   *Supported key:*  ``PRODUCT``  
        
                   *Supported values:*  
        
                  * ``AmazonLinux2012.03``   
                   
                  * ``AmazonLinux2012.09``   
                   
                  * ``AmazonLinux2013.03``   
                   
                  * ``AmazonLinux2013.09``   
                   
                  * ``AmazonLinux2014.03``   
                   
                  * ``AmazonLinux2014.09``   
                   
                  * ``AmazonLinux2015.03``   
                   
                  * ``AmazonLinux2015.09``   
                   
                  * ``AmazonLinux2016.03``   
                   
                  * ``AmazonLinux2016.09``   
                   
                  * ``AmazonLinux2017.03``   
                   
                  * ``AmazonLinux2017.09``   
                   
                  * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                   
                   *Supported key:*  ``CLASSIFICATION``  
        
                   *Supported values:*  
        
                  * ``Security``   
                   
                  * ``Bugfix``   
                   
                  * ``Enhancement``   
                   
                  * ``Recommended``   
                   
                  * ``Newpackage``   
                   
                   *Supported key:*  ``SEVERITY``  
        
                   *Supported values:*  
        
                  * ``Critical``   
                   
                  * ``Important``   
                   
                  * ``Medium``   
                   
                  * ``Low``   
                   
                   **Amazon Linux 2 Operating Systems**  
        
                  The supported keys for Amazon Linux 2 operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                   *Supported key:*  ``PRODUCT``  
        
                   *Supported values:*  
        
                  * ``AmazonLinux2``   
                   
                  * ``AmazonLinux2.0``   
                   
                  * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                   
                   *Supported key:*  ``CLASSIFICATION``  
        
                   *Supported values:*  
        
                  * ``Security``   
                   
                  * ``Bugfix``   
                   
                  * ``Enhancement``   
                   
                  * ``Recommended``   
                   
                  * ``Newpackage``   
                   
                   *Supported key:*  ``SEVERITY``  
        
                   *Supported values:*  
        
                  * ``Critical``   
                   
                  * ``Important``   
                   
                  * ``Medium``   
                   
                  * ``Low``   
                   
                   **RedHat Enterprise Linux (RHEL) Operating Systems**  
        
                  The supported keys for RedHat Enterprise Linux operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                   *Supported key:*  ``PRODUCT``  
        
                   *Supported values:*  
        
                  * ``RedhatEnterpriseLinux6.5``   
                   
                  * ``RedhatEnterpriseLinux6.6``   
                   
                  * ``RedhatEnterpriseLinux6.7``   
                   
                  * ``RedhatEnterpriseLinux6.8``   
                   
                  * ``RedhatEnterpriseLinux6.9``   
                   
                  * ``RedhatEnterpriseLinux7.0``   
                   
                  * ``RedhatEnterpriseLinux7.1``   
                   
                  * ``RedhatEnterpriseLinux7.2``   
                   
                  * ``RedhatEnterpriseLinux7.3``   
                   
                  * ``RedhatEnterpriseLinux7.4``   
                   
                  * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                   
                   *Supported key:*  ``CLASSIFICATION``  
        
                   *Supported values:*  
        
                  * ``Security``   
                   
                  * ``Bugfix``   
                   
                  * ``Enhancement``   
                   
                  * ``Recommended``   
                   
                  * ``Newpackage``   
                   
                   *Supported key:*  ``SEVERITY``  
        
                   *Supported values:*  
        
                  * ``Critical``   
                   
                  * ``Important``   
                   
                  * ``Medium``   
                   
                  * ``Low``   
                   
                   **SUSE Linux Enterprise Server (SLES) Operating Systems**  
        
                  The supported keys for SLES operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                   *Supported key:*  ``PRODUCT``  
        
                   *Supported values:*  
        
                  * ``Suse12.0``   
                   
                  * ``Suse12.1``   
                   
                  * ``Suse12.2``   
                   
                  * ``Suse12.3``   
                   
                  * ``Suse12.4``   
                   
                  * ``Suse12.5``   
                   
                  * ``Suse12.6``   
                   
                  * ``Suse12.7``   
                   
                  * ``Suse12.8``   
                   
                  * ``Suse12.9``   
                   
                  * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                   
                   *Supported key:*  ``CLASSIFICATION``  
        
                   *Supported values:*  
        
                  * ``Security``   
                   
                  * ``Recommended``   
                   
                  * ``Optional``   
                   
                  * ``Feature``   
                   
                  * ``Document``   
                   
                  * ``Yast``   
                   
                   *Supported key:*  ``SEVERITY``  
        
                   *Supported values:*  
        
                  * ``Critical``   
                   
                  * ``Important``   
                   
                  * ``Moderate``   
                   
                  * ``Low``   
                   
                   **CentOS Operating Systems**  
        
                  The supported keys for CentOS operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                   *Supported key:*  ``PRODUCT``  
        
                   *Supported values:*  
        
                  * ``CentOS6.5``   
                   
                  * ``CentOS6.6``   
                   
                  * ``CentOS6.7``   
                   
                  * ``CentOS6.8``   
                   
                  * ``CentOS6.9``   
                   
                  * ``CentOS7.0``   
                   
                  * ``CentOS7.1``   
                   
                  * ``CentOS7.2``   
                   
                  * ``CentOS7.3``   
                   
                  * ``CentOS7.4``   
                   
                  * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                   
                   *Supported key:*  ``CLASSIFICATION``  
        
                   *Supported values:*  
        
                  * ``Security``   
                   
                  * ``Bugfix``   
                   
                  * ``Enhancement``   
                   
                  * ``Recommended``   
                   
                  * ``Newpackage``   
                   
                   *Supported key:*  ``SEVERITY``  
        
                   *Supported values:*  
        
                  * ``Critical``   
                   
                  * ``Important``   
                   
                  * ``Medium``   
                   
                  * ``Low``   
                   
                  - **Key** *(string) --* 
        
                    The key for the filter.
        
                    See  PatchFilter for lists of valid keys for each operating system type.
        
                  - **Values** *(list) --* 
        
                    The value for the filter key.
        
                    See  PatchFilter for lists of valid values for each key based on operating system type.
        
                    - *(string) --* 
                
            - **ApprovalRules** *(dict) --* 
        
              A set of rules used to include patches in the baseline.
        
              - **PatchRules** *(list) --* 
        
                The rules that make up the rule group.
        
                - *(dict) --* 
        
                  Defines an approval rule for a patch baseline.
        
                  - **PatchFilterGroup** *(dict) --* 
        
                    The patch filter group that defines the criteria for the rule.
        
                    - **PatchFilters** *(list) --* 
        
                      The set of patch filters that make up the group.
        
                      - *(dict) --* 
        
                        Defines a patch filter.
        
                        A patch filter consists of key/value pairs, but not all keys are valid for all operating system types. For example, the key ``PRODUCT`` is valid for all supported operating system types. The key ``MSRC_SEVERITY`` , however, is valid only for Windows operating systems, and the key ``SECTION`` is valid only for Ubuntu operating systems.
        
                        Refer to the following sections for information about which keys may be used with each major operating system, and which values are valid for each key.
        
                         **Windows Operating Systems**  
        
                        The supported keys for Windows operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``MSRC_SEVERITY`` . See the following lists for valid values for each of these keys.
        
                         *Supported key:*  ``PRODUCT``  
        
                         *Supported values:*  
        
                        * ``Windows7``   
                         
                        * ``Windows8``   
                         
                        * ``Windows8.1``   
                         
                        * ``Windows8Embedded``   
                         
                        * ``Windows10``   
                         
                        * ``Windows10LTSB``   
                         
                        * ``WindowsServer2008``   
                         
                        * ``WindowsServer2008R2``   
                         
                        * ``WindowsServer2012``   
                         
                        * ``WindowsServer2012R2``   
                         
                        * ``WindowsServer2016``   
                         
                        * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                         
                         *Supported key:*  ``CLASSIFICATION``  
        
                         *Supported values:*  
        
                        * ``CriticalUpdates``   
                         
                        * ``DefinitionUpdates``   
                         
                        * ``Drivers``   
                         
                        * ``FeaturePacks``   
                         
                        * ``SecurityUpdates``   
                         
                        * ``ServicePacks``   
                         
                        * ``Tools``   
                         
                        * ``UpdateRollups``   
                         
                        * ``Updates``   
                         
                        * ``Upgrades``   
                         
                         *Supported key:*  ``MSRC_SEVERITY``  
        
                         *Supported values:*  
        
                        * ``Critical``   
                         
                        * ``Important``   
                         
                        * ``Moderate``   
                         
                        * ``Low``   
                         
                        * ``Unspecified``   
                         
                         **Ubuntu Operating Systems**  
        
                        The supported keys for Ubuntu operating systems are ``PRODUCT`` , ``PRIORITY`` , and ``SECTION`` . See the following lists for valid values for each of these keys.
        
                         *Supported key:*  ``PRODUCT``  
        
                         *Supported values:*  
        
                        * ``Ubuntu14.04``   
                         
                        * ``Ubuntu16.04``   
                         
                        * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                         
                         *Supported key:*  ``PRIORITY``  
        
                         *Supported values:*  
        
                        * ``Required``   
                         
                        * ``Important``   
                         
                        * ``Standard``   
                         
                        * ``Optional``   
                         
                        * ``Extra``   
                         
                         *Supported key:*  ``SECTION``  
        
                        Only the length of the key value is validated. Minimum length is 1. Maximum length is 64.
        
                         **Amazon Linux Operating Systems**  
        
                        The supported keys for Amazon Linux operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                         *Supported key:*  ``PRODUCT``  
        
                         *Supported values:*  
        
                        * ``AmazonLinux2012.03``   
                         
                        * ``AmazonLinux2012.09``   
                         
                        * ``AmazonLinux2013.03``   
                         
                        * ``AmazonLinux2013.09``   
                         
                        * ``AmazonLinux2014.03``   
                         
                        * ``AmazonLinux2014.09``   
                         
                        * ``AmazonLinux2015.03``   
                         
                        * ``AmazonLinux2015.09``   
                         
                        * ``AmazonLinux2016.03``   
                         
                        * ``AmazonLinux2016.09``   
                         
                        * ``AmazonLinux2017.03``   
                         
                        * ``AmazonLinux2017.09``   
                         
                        * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                         
                         *Supported key:*  ``CLASSIFICATION``  
        
                         *Supported values:*  
        
                        * ``Security``   
                         
                        * ``Bugfix``   
                         
                        * ``Enhancement``   
                         
                        * ``Recommended``   
                         
                        * ``Newpackage``   
                         
                         *Supported key:*  ``SEVERITY``  
        
                         *Supported values:*  
        
                        * ``Critical``   
                         
                        * ``Important``   
                         
                        * ``Medium``   
                         
                        * ``Low``   
                         
                         **Amazon Linux 2 Operating Systems**  
        
                        The supported keys for Amazon Linux 2 operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                         *Supported key:*  ``PRODUCT``  
        
                         *Supported values:*  
        
                        * ``AmazonLinux2``   
                         
                        * ``AmazonLinux2.0``   
                         
                        * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                         
                         *Supported key:*  ``CLASSIFICATION``  
        
                         *Supported values:*  
        
                        * ``Security``   
                         
                        * ``Bugfix``   
                         
                        * ``Enhancement``   
                         
                        * ``Recommended``   
                         
                        * ``Newpackage``   
                         
                         *Supported key:*  ``SEVERITY``  
        
                         *Supported values:*  
        
                        * ``Critical``   
                         
                        * ``Important``   
                         
                        * ``Medium``   
                         
                        * ``Low``   
                         
                         **RedHat Enterprise Linux (RHEL) Operating Systems**  
        
                        The supported keys for RedHat Enterprise Linux operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                         *Supported key:*  ``PRODUCT``  
        
                         *Supported values:*  
        
                        * ``RedhatEnterpriseLinux6.5``   
                         
                        * ``RedhatEnterpriseLinux6.6``   
                         
                        * ``RedhatEnterpriseLinux6.7``   
                         
                        * ``RedhatEnterpriseLinux6.8``   
                         
                        * ``RedhatEnterpriseLinux6.9``   
                         
                        * ``RedhatEnterpriseLinux7.0``   
                         
                        * ``RedhatEnterpriseLinux7.1``   
                         
                        * ``RedhatEnterpriseLinux7.2``   
                         
                        * ``RedhatEnterpriseLinux7.3``   
                         
                        * ``RedhatEnterpriseLinux7.4``   
                         
                        * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                         
                         *Supported key:*  ``CLASSIFICATION``  
        
                         *Supported values:*  
        
                        * ``Security``   
                         
                        * ``Bugfix``   
                         
                        * ``Enhancement``   
                         
                        * ``Recommended``   
                         
                        * ``Newpackage``   
                         
                         *Supported key:*  ``SEVERITY``  
        
                         *Supported values:*  
        
                        * ``Critical``   
                         
                        * ``Important``   
                         
                        * ``Medium``   
                         
                        * ``Low``   
                         
                         **SUSE Linux Enterprise Server (SLES) Operating Systems**  
        
                        The supported keys for SLES operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                         *Supported key:*  ``PRODUCT``  
        
                         *Supported values:*  
        
                        * ``Suse12.0``   
                         
                        * ``Suse12.1``   
                         
                        * ``Suse12.2``   
                         
                        * ``Suse12.3``   
                         
                        * ``Suse12.4``   
                         
                        * ``Suse12.5``   
                         
                        * ``Suse12.6``   
                         
                        * ``Suse12.7``   
                         
                        * ``Suse12.8``   
                         
                        * ``Suse12.9``   
                         
                        * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                         
                         *Supported key:*  ``CLASSIFICATION``  
        
                         *Supported values:*  
        
                        * ``Security``   
                         
                        * ``Recommended``   
                         
                        * ``Optional``   
                         
                        * ``Feature``   
                         
                        * ``Document``   
                         
                        * ``Yast``   
                         
                         *Supported key:*  ``SEVERITY``  
        
                         *Supported values:*  
        
                        * ``Critical``   
                         
                        * ``Important``   
                         
                        * ``Moderate``   
                         
                        * ``Low``   
                         
                         **CentOS Operating Systems**  
        
                        The supported keys for CentOS operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                         *Supported key:*  ``PRODUCT``  
        
                         *Supported values:*  
        
                        * ``CentOS6.5``   
                         
                        * ``CentOS6.6``   
                         
                        * ``CentOS6.7``   
                         
                        * ``CentOS6.8``   
                         
                        * ``CentOS6.9``   
                         
                        * ``CentOS7.0``   
                         
                        * ``CentOS7.1``   
                         
                        * ``CentOS7.2``   
                         
                        * ``CentOS7.3``   
                         
                        * ``CentOS7.4``   
                         
                        * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                         
                         *Supported key:*  ``CLASSIFICATION``  
        
                         *Supported values:*  
        
                        * ``Security``   
                         
                        * ``Bugfix``   
                         
                        * ``Enhancement``   
                         
                        * ``Recommended``   
                         
                        * ``Newpackage``   
                         
                         *Supported key:*  ``SEVERITY``  
        
                         *Supported values:*  
        
                        * ``Critical``   
                         
                        * ``Important``   
                         
                        * ``Medium``   
                         
                        * ``Low``   
                         
                        - **Key** *(string) --* 
        
                          The key for the filter.
        
                          See  PatchFilter for lists of valid keys for each operating system type.
        
                        - **Values** *(list) --* 
        
                          The value for the filter key.
        
                          See  PatchFilter for lists of valid values for each key based on operating system type.
        
                          - *(string) --* 
                      
                  - **ComplianceLevel** *(string) --* 
        
                    A compliance severity level for all approved patches in a patch baseline. Valid compliance severity levels include the following: Unspecified, Critical, High, Medium, Low, and Informational.
        
                  - **ApproveAfterDays** *(integer) --* 
        
                    The number of days after the release date of each patch matched by the rule that the patch is marked as approved in the patch baseline. For example, a value of ``7`` means that patches are approved seven days after they are released. 
        
                  - **EnableNonSecurity** *(boolean) --* 
        
                    For instances identified by the approval rule filters, enables a patch baseline to apply non-security updates available in the specified repository. The default value is \'false\'. Applies to Linux instances only.
        
            - **ApprovedPatches** *(list) --* 
        
              A list of explicitly approved patches for the baseline.
        
              - *(string) --* 
          
            - **ApprovedPatchesComplianceLevel** *(string) --* 
        
              Returns the specified compliance severity level for approved patches in the patch baseline.
        
            - **ApprovedPatchesEnableNonSecurity** *(boolean) --* 
        
              Indicates whether the list of approved patches includes non-security updates that should be applied to the instances. The default value is \'false\'. Applies to Linux instances only.
        
            - **RejectedPatches** *(list) --* 
        
              A list of explicitly rejected patches for the baseline.
        
              - *(string) --* 
          
            - **RejectedPatchesAction** *(string) --* 
        
              The action specified to take on patches included in the RejectedPatches list. A patch can be allowed only if it is a dependency of another package, or blocked entirely along with packages that include it as a dependency.
        
            - **PatchGroups** *(list) --* 
        
              Patch groups included in the patch baseline.
        
              - *(string) --* 
          
            - **CreatedDate** *(datetime) --* 
        
              The date the patch baseline was created.
        
            - **ModifiedDate** *(datetime) --* 
        
              The date the patch baseline was last modified.
        
            - **Description** *(string) --* 
        
              A description of the patch baseline.
        
            - **Sources** *(list) --* 
        
              Information about the patches to use to update the instances, including target operating systems and source repositories. Applies to Linux instances only.
        
              - *(dict) --* 
        
                Information about the patches to use to update the instances, including target operating systems and source repository. Applies to Linux instances only.
        
                - **Name** *(string) --* 
        
                  The name specified to identify the patch source.
        
                - **Products** *(list) --* 
        
                  The specific operating system versions a patch repository applies to, such as \"Ubuntu16.04\", \"AmazonLinux2016.09\", \"RedhatEnterpriseLinux7.2\" or \"Suse12.7\". For lists of supported product values, see  PatchFilter .
        
                  - *(string) --* 
              
                - **Configuration** *(string) --* 
        
                  The value of the yum repo configuration. For example:
        
                   ``cachedir=/var/cache/yum/$basesearch``  
        
                   ``$releasever``  
        
                   ``keepcache=0``  
        
                   ``debuglevel=2``  
        
        """
        pass

    def get_patch_baseline_for_patch_group(self, PatchGroup: str, OperatingSystem: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetPatchBaselineForPatchGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_patch_baseline_for_patch_group(
              PatchGroup=\'string\',
              OperatingSystem=\'WINDOWS\'|\'AMAZON_LINUX\'|\'AMAZON_LINUX_2\'|\'UBUNTU\'|\'REDHAT_ENTERPRISE_LINUX\'|\'SUSE\'|\'CENTOS\'
          )
        :type PatchGroup: string
        :param PatchGroup: **[REQUIRED]** 
        
          The name of the patch group whose patch baseline should be retrieved.
        
        :type OperatingSystem: string
        :param OperatingSystem: 
        
          Returns he operating system rule specified for patch groups using the patch baseline.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'BaselineId\': \'string\',
                \'PatchGroup\': \'string\',
                \'OperatingSystem\': \'WINDOWS\'|\'AMAZON_LINUX\'|\'AMAZON_LINUX_2\'|\'UBUNTU\'|\'REDHAT_ENTERPRISE_LINUX\'|\'SUSE\'|\'CENTOS\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **BaselineId** *(string) --* 
        
              The ID of the patch baseline that should be used for the patch group.
        
            - **PatchGroup** *(string) --* 
        
              The name of the patch group.
        
            - **OperatingSystem** *(string) --* 
        
              The operating system rule specified for patch groups using the patch baseline.
        
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

    def label_parameter_version(self, Name: str, Labels: List, ParameterVersion: int = None) -> Dict:
        """
        
        Parameter labels have the following requirements and restrictions.
        
        * A version of a parameter can have a maximum of 10 labels. 
         
        * You can\'t attach the same label to different versions of the same parameter. For example, if version 1 has the label Production, then you can\'t attach Production to version 2. 
         
        * You can move a label from one version of a parameter to another. 
         
        * You can\'t create a label when you create a new parameter. You must attach a label to a specific version of a parameter. 
         
        * You can\'t delete a parameter label. If you no longer want to use a parameter label, then you must move it to a different version of a parameter. 
         
        * A label can have a maximum of 100 characters. 
         
        * Labels can contain letters (case sensitive), numbers, periods (.), hyphens (-), or underscores (_). 
         
        * Labels can\'t begin with a number, \"aws,\" or \"ssm\" (not case sensitive). If a label fails to meet these requirements, then the label is not associated with a parameter and the system displays it in the list of InvalidLabels. 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/LabelParameterVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.label_parameter_version(
              Name=\'string\',
              ParameterVersion=123,
              Labels=[
                  \'string\',
              ]
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The parameter name on which you want to attach one or more labels.
        
        :type ParameterVersion: integer
        :param ParameterVersion: 
        
          The specific version of the parameter on which you want to attach one or more labels. If no version is specified, the system attaches the label to the latest version.)
        
        :type Labels: list
        :param Labels: **[REQUIRED]** 
        
          One or more labels to attach to the specified parameter version.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'InvalidLabels\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **InvalidLabels** *(list) --* 
        
              The label does not meet the requirements. For information about parameter label requirements, see `Labeling Parameters <http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-labels.html>`__ in the *AWS Systems Manager User Guide* .
        
              - *(string) --* 
          
        """
        pass

    def list_association_versions(self, AssociationId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListAssociationVersions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_association_versions(
              AssociationId=\'string\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type AssociationId: string
        :param AssociationId: **[REQUIRED]** 
        
          The association ID for which you want to view all versions.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          A token to start the list. Use this token to get the next set of results. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AssociationVersions\': [
                    {
                        \'AssociationId\': \'string\',
                        \'AssociationVersion\': \'string\',
                        \'CreatedDate\': datetime(2015, 1, 1),
                        \'Name\': \'string\',
                        \'DocumentVersion\': \'string\',
                        \'Parameters\': {
                            \'string\': [
                                \'string\',
                            ]
                        },
                        \'Targets\': [
                            {
                                \'Key\': \'string\',
                                \'Values\': [
                                    \'string\',
                                ]
                            },
                        ],
                        \'ScheduleExpression\': \'string\',
                        \'OutputLocation\': {
                            \'S3Location\': {
                                \'OutputS3Region\': \'string\',
                                \'OutputS3BucketName\': \'string\',
                                \'OutputS3KeyPrefix\': \'string\'
                            }
                        },
                        \'AssociationName\': \'string\',
                        \'MaxErrors\': \'string\',
                        \'MaxConcurrency\': \'string\',
                        \'ComplianceSeverity\': \'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'UNSPECIFIED\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                    An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                    - **Key** *(string) --* 
        
                      User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                    - **Values** *(list) --* 
        
                      User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
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
        
                  Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.
        
                - **MaxConcurrency** *(string) --* 
        
                  The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
        
                  If a new instance starts and attempts to execute an association while Systems Manager is executing MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.
        
                - **ComplianceSeverity** *(string) --* 
        
                  The severity level that is assigned to the association.
        
            - **NextToken** *(string) --* 
        
              The token for the next set of items to return. Use this token to get the next set of results.
        
        """
        pass

    def list_associations(self, AssociationFilterList: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListAssociations>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_associations(
              AssociationFilterList=[
                  {
                      \'key\': \'InstanceId\'|\'Name\'|\'AssociationId\'|\'AssociationStatusName\'|\'LastExecutedBefore\'|\'LastExecutedAfter\'|\'AssociationName\',
                      \'value\': \'string\'
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
        :type AssociationFilterList: list
        :param AssociationFilterList: 
        
          One or more filters. Use a filter to return a more specific list of results.
        
          - *(dict) --* 
        
            Describes a filter.
        
            - **key** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **value** *(string) --* **[REQUIRED]** 
        
              The filter value.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Associations\': [
                    {
                        \'Name\': \'string\',
                        \'InstanceId\': \'string\',
                        \'AssociationId\': \'string\',
                        \'AssociationVersion\': \'string\',
                        \'DocumentVersion\': \'string\',
                        \'Targets\': [
                            {
                                \'Key\': \'string\',
                                \'Values\': [
                                    \'string\',
                                ]
                            },
                        ],
                        \'LastExecutionDate\': datetime(2015, 1, 1),
                        \'Overview\': {
                            \'Status\': \'string\',
                            \'DetailedStatus\': \'string\',
                            \'AssociationStatusAggregatedCount\': {
                                \'string\': 123
                            }
                        },
                        \'ScheduleExpression\': \'string\',
                        \'AssociationName\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                    An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                    - **Key** *(string) --* 
        
                      User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                    - **Values** *(list) --* 
        
                      User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
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
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def list_command_invocations(self, CommandId: str = None, InstanceId: str = None, MaxResults: int = None, NextToken: str = None, Filters: List = None, Details: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListCommandInvocations>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_command_invocations(
              CommandId=\'string\',
              InstanceId=\'string\',
              MaxResults=123,
              NextToken=\'string\',
              Filters=[
                  {
                      \'key\': \'InvokedAfter\'|\'InvokedBefore\'|\'Status\'|\'ExecutionStage\'|\'DocumentName\',
                      \'value\': \'string\'
                  },
              ],
              Details=True|False
          )
        :type CommandId: string
        :param CommandId: 
        
          (Optional) The invocations for a specific command ID.
        
        :type InstanceId: string
        :param InstanceId: 
        
          (Optional) The command execution details for a specific instance ID.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          (Optional) The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          (Optional) The token for the next set of items to return. (You received this token from a previous call.)
        
        :type Filters: list
        :param Filters: 
        
          (Optional) One or more filters. Use a filter to return a more specific list of results.
        
          - *(dict) --* 
        
            Describes a command filter.
        
            - **key** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **value** *(string) --* **[REQUIRED]** 
        
              The filter value. Valid values for each filter key are as follows:
        
              * InvokedAfter: A timestamp to limit your results. For example, specify ``2018-07-07T00:00:00Z`` to see results occurring July 7, 2018, and later. 
               
              * InvokedBefore: A timestamp to limit your results. For example, specify ``2018-07-07T00:00:00Z`` to see results before July 7, 2018. 
               
              * Status: Specify a valid command status to see a list of all command executions with that status. Status values you can specify include: 
        
                * Pending 
                 
                * InProgress 
                 
                * Success 
                 
                * Cancelled 
                 
                * Failed 
                 
                * TimedOut 
                 
                * Cancelling  
                 
              * DocumentName: The name of the SSM document for which you want to see command results. For example, specify ``AWS-RunPatchBaseline`` to see command executions that used this SSM document to perform security patching operations on instances.  
               
              * ExecutionStage: An enum whose value can be either ``Executing`` or ``Complete`` . 
        
                * Specify ``Executing`` to see a list of command executions that are currently still running. 
                 
                * Specify ``Complete`` to see a list of command exeuctions that have already completed. 
                 
        :type Details: boolean
        :param Details: 
        
          (Optional) If set this returns the response of the command executions and any command output. By default this is set to False. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CommandInvocations\': [
                    {
                        \'CommandId\': \'string\',
                        \'InstanceId\': \'string\',
                        \'InstanceName\': \'string\',
                        \'Comment\': \'string\',
                        \'DocumentName\': \'string\',
                        \'DocumentVersion\': \'string\',
                        \'RequestedDateTime\': datetime(2015, 1, 1),
                        \'Status\': \'Pending\'|\'InProgress\'|\'Delayed\'|\'Success\'|\'Cancelled\'|\'TimedOut\'|\'Failed\'|\'Cancelling\',
                        \'StatusDetails\': \'string\',
                        \'TraceOutput\': \'string\',
                        \'StandardOutputUrl\': \'string\',
                        \'StandardErrorUrl\': \'string\',
                        \'CommandPlugins\': [
                            {
                                \'Name\': \'string\',
                                \'Status\': \'Pending\'|\'InProgress\'|\'Success\'|\'TimedOut\'|\'Cancelled\'|\'Failed\',
                                \'StatusDetails\': \'string\',
                                \'ResponseCode\': 123,
                                \'ResponseStartDateTime\': datetime(2015, 1, 1),
                                \'ResponseFinishDateTime\': datetime(2015, 1, 1),
                                \'Output\': \'string\',
                                \'StandardOutputUrl\': \'string\',
                                \'StandardErrorUrl\': \'string\',
                                \'OutputS3Region\': \'string\',
                                \'OutputS3BucketName\': \'string\',
                                \'OutputS3KeyPrefix\': \'string\'
                            },
                        ],
                        \'ServiceRole\': \'string\',
                        \'NotificationConfig\': {
                            \'NotificationArn\': \'string\',
                            \'NotificationEvents\': [
                                \'All\'|\'InProgress\'|\'Success\'|\'TimedOut\'|\'Cancelled\'|\'Failed\',
                            ],
                            \'NotificationType\': \'Command\'|\'Invocation\'
                        },
                        \'CloudWatchOutputConfig\': {
                            \'CloudWatchLogGroupName\': \'string\',
                            \'CloudWatchOutputEnabled\': True|False
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CommandInvocations** *(list) --* 
        
              (Optional) A list of all invocations. 
        
              - *(dict) --* 
        
                An invocation is copy of a command sent to a specific instance. A command can apply to one or more instances. A command invocation applies to one instance. For example, if a user executes SendCommand against three instances, then a command invocation is created for each requested instance ID. A command invocation returns status and detail information about a command you executed. 
        
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
                   
                  * Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command\'s MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
                   
                  * Execution Timed Out: Command execution started on the instance, but the execution was not complete before the execution timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state. 
                   
                  * Failed: The command was not successful on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state. 
                   
                  * Canceled: The command was terminated before it was completed. This is a terminal state. 
                   
                  * Undeliverable: The command can\'t be delivered to the instance. The instance might not exist or might not be responding. Undeliverable invocations don\'t count against the parent command\'s MaxErrors limit and don\'t contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
                   
                  * Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state. 
                   
                - **TraceOutput** *(string) --* 
        
                  Gets the trace output sent by the agent. 
        
                - **StandardOutputUrl** *(string) --* 
        
                  The URL to the plugin\'s StdOut file in Amazon S3, if the Amazon S3 bucket was defined for the parent command. For an invocation, StandardOutputUrl is populated if there is just one plugin defined for the command, and the Amazon S3 bucket was defined for the command.
        
                - **StandardErrorUrl** *(string) --* 
        
                  The URL to the plugin\'s StdErr file in Amazon S3, if the Amazon S3 bucket was defined for the parent command. For an invocation, StandardErrorUrl is populated if there is just one plugin defined for the command, and the Amazon S3 bucket was defined for the command.
        
                - **CommandPlugins** *(list) --* 
                  
                  - *(dict) --* 
        
                    Describes plugin details.
        
                    - **Name** *(string) --* 
        
                      The name of the plugin. Must be one of the following: aws:updateAgent, aws:domainjoin, aws:applications, aws:runPowerShellScript, aws:psmodule, aws:cloudWatch, aws:runShellScript, or aws:updateSSMAgent. 
        
                    - **Status** *(string) --* 
        
                      The status of this plugin. You can execute a document with multiple plugins.
        
                    - **StatusDetails** *(string) --* 
        
                      A detailed status of the plugin execution. StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see `Understanding Command Statuses <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* . StatusDetails can be one of the following values:
        
                      * Pending: The command has not been sent to the instance. 
                       
                      * In Progress: The command has been sent to the instance but has not reached a terminal state. 
                       
                      * Success: The execution of the command or plugin was successfully completed. This is a terminal state. 
                       
                      * Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command\'s MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
                       
                      * Execution Timed Out: Command execution started on the instance, but the execution was not complete before the execution timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state. 
                       
                      * Failed: The command was not successful on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state. 
                       
                      * Canceled: The command was terminated before it was completed. This is a terminal state. 
                       
                      * Undeliverable: The command can\'t be delivered to the instance. The instance might not exist, or it might not be responding. Undeliverable invocations don\'t count against the parent command\'s MaxErrors limit, and they don\'t contribute to whether the parent command status is Success or Incomplete. This is a terminal state. 
                       
                      * Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state. 
                       
                    - **ResponseCode** *(integer) --* 
        
                      A numeric response code generated after executing the plugin. 
        
                    - **ResponseStartDateTime** *(datetime) --* 
        
                      The time the plugin started executing. 
        
                    - **ResponseFinishDateTime** *(datetime) --* 
        
                      The time the plugin stopped executing. Could stop prematurely if, for example, a cancel command was sent. 
        
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
        
                    The name of the CloudWatch log group where you want to send command output. If you don\'t specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/*SystemsManagerDocumentName* .
        
                  - **CloudWatchOutputEnabled** *(boolean) --* 
        
                    Enables Systems Manager to send command output to CloudWatch Logs.
        
            - **NextToken** *(string) --* 
        
              (Optional) The token for the next set of items to return. (You received this token from a previous call.)
        
        """
        pass

    def list_commands(self, CommandId: str = None, InstanceId: str = None, MaxResults: int = None, NextToken: str = None, Filters: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListCommands>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_commands(
              CommandId=\'string\',
              InstanceId=\'string\',
              MaxResults=123,
              NextToken=\'string\',
              Filters=[
                  {
                      \'key\': \'InvokedAfter\'|\'InvokedBefore\'|\'Status\'|\'ExecutionStage\'|\'DocumentName\',
                      \'value\': \'string\'
                  },
              ]
          )
        :type CommandId: string
        :param CommandId: 
        
          (Optional) If provided, lists only the specified command.
        
        :type InstanceId: string
        :param InstanceId: 
        
          (Optional) Lists commands issued against this instance ID.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          (Optional) The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          (Optional) The token for the next set of items to return. (You received this token from a previous call.)
        
        :type Filters: list
        :param Filters: 
        
          (Optional) One or more filters. Use a filter to return a more specific list of results. 
        
          - *(dict) --* 
        
            Describes a command filter.
        
            - **key** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **value** *(string) --* **[REQUIRED]** 
        
              The filter value. Valid values for each filter key are as follows:
        
              * InvokedAfter: A timestamp to limit your results. For example, specify ``2018-07-07T00:00:00Z`` to see results occurring July 7, 2018, and later. 
               
              * InvokedBefore: A timestamp to limit your results. For example, specify ``2018-07-07T00:00:00Z`` to see results before July 7, 2018. 
               
              * Status: Specify a valid command status to see a list of all command executions with that status. Status values you can specify include: 
        
                * Pending 
                 
                * InProgress 
                 
                * Success 
                 
                * Cancelled 
                 
                * Failed 
                 
                * TimedOut 
                 
                * Cancelling  
                 
              * DocumentName: The name of the SSM document for which you want to see command results. For example, specify ``AWS-RunPatchBaseline`` to see command executions that used this SSM document to perform security patching operations on instances.  
               
              * ExecutionStage: An enum whose value can be either ``Executing`` or ``Complete`` . 
        
                * Specify ``Executing`` to see a list of command executions that are currently still running. 
                 
                * Specify ``Complete`` to see a list of command exeuctions that have already completed. 
                 
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Commands\': [
                    {
                        \'CommandId\': \'string\',
                        \'DocumentName\': \'string\',
                        \'DocumentVersion\': \'string\',
                        \'Comment\': \'string\',
                        \'ExpiresAfter\': datetime(2015, 1, 1),
                        \'Parameters\': {
                            \'string\': [
                                \'string\',
                            ]
                        },
                        \'InstanceIds\': [
                            \'string\',
                        ],
                        \'Targets\': [
                            {
                                \'Key\': \'string\',
                                \'Values\': [
                                    \'string\',
                                ]
                            },
                        ],
                        \'RequestedDateTime\': datetime(2015, 1, 1),
                        \'Status\': \'Pending\'|\'InProgress\'|\'Success\'|\'Cancelled\'|\'Failed\'|\'TimedOut\'|\'Cancelling\',
                        \'StatusDetails\': \'string\',
                        \'OutputS3Region\': \'string\',
                        \'OutputS3BucketName\': \'string\',
                        \'OutputS3KeyPrefix\': \'string\',
                        \'MaxConcurrency\': \'string\',
                        \'MaxErrors\': \'string\',
                        \'TargetCount\': 123,
                        \'CompletedCount\': 123,
                        \'ErrorCount\': 123,
                        \'DeliveryTimedOutCount\': 123,
                        \'ServiceRole\': \'string\',
                        \'NotificationConfig\': {
                            \'NotificationArn\': \'string\',
                            \'NotificationEvents\': [
                                \'All\'|\'InProgress\'|\'Success\'|\'TimedOut\'|\'Cancelled\'|\'Failed\',
                            ],
                            \'NotificationType\': \'Command\'|\'Invocation\'
                        },
                        \'CloudWatchOutputConfig\': {
                            \'CloudWatchLogGroupName\': \'string\',
                            \'CloudWatchOutputEnabled\': True|False
                        }
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  If this time is reached and the command has not already started executing, it will not run. Calculated based on the ExpiresAfter user input provided as part of the SendCommand API.
        
                - **Parameters** *(dict) --* 
        
                  The parameter values to be inserted in the document when executing the command.
        
                  - *(string) --* 
                    
                    - *(list) --* 
                      
                      - *(string) --* 
                  
                - **InstanceIds** *(list) --* 
        
                  The instance IDs against which this command was requested.
        
                  - *(string) --* 
              
                - **Targets** *(list) --* 
        
                  An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don\'t provide one or more instance IDs in the call.
        
                  - *(dict) --* 
        
                    An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                    - **Key** *(string) --* 
        
                      User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                    - **Values** *(list) --* 
        
                      User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
                      - *(string) --* 
                  
                - **RequestedDateTime** *(datetime) --* 
        
                  The date and time the command was requested.
        
                - **Status** *(string) --* 
        
                  The status of the command.
        
                - **StatusDetails** *(string) --* 
        
                  A detailed status of the command execution. StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see `Understanding Command Statuses <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* . StatusDetails can be one of the following values:
        
                  * Pending: The command has not been sent to any instances. 
                   
                  * In Progress: The command has been sent to at least one instance but has not reached a final state on all instances. 
                   
                  * Success: The command successfully executed on all invocations. This is a terminal state. 
                   
                  * Delivery Timed Out: The value of MaxErrors or more command invocations shows a status of Delivery Timed Out. This is a terminal state. 
                   
                  * Execution Timed Out: The value of MaxErrors or more command invocations shows a status of Execution Timed Out. This is a terminal state. 
                   
                  * Failed: The value of MaxErrors or more command invocations shows a status of Failed. This is a terminal state. 
                   
                  * Incomplete: The command was attempted on all instances and one or more invocations does not have a value of Success but not enough invocations failed for the status to be Failed. This is a terminal state. 
                   
                  * Canceled: The command was terminated before it was completed. This is a terminal state. 
                   
                  * Rate Exceeded: The number of instances targeted by the command exceeded the account limit for pending invocations. The system has canceled the command before executing it on any instance. This is a terminal state. 
                   
                - **OutputS3Region** *(string) --* 
        
                  (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
        
                - **OutputS3BucketName** *(string) --* 
        
                  The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command.
        
                - **OutputS3KeyPrefix** *(string) --* 
        
                  The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command.
        
                - **MaxConcurrency** *(string) --* 
        
                  The maximum number of instances that are allowed to execute the command at the same time. You can specify a number of instances, such as 10, or a percentage of instances, such as 10%. The default value is 50. For more information about how to use MaxConcurrency, see `Executing Commands Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html>`__ in the *AWS Systems Manager User Guide* .
        
                - **MaxErrors** *(string) --* 
        
                  The maximum number of errors allowed before the system stops sending the command to additional targets. You can specify a number of errors, such as 10, or a percentage or errors, such as 10%. The default value is 0. For more information about how to use MaxErrors, see `Executing Commands Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html>`__ in the *AWS Systems Manager User Guide* .
        
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
        
                    The name of the CloudWatch log group where you want to send command output. If you don\'t specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/*SystemsManagerDocumentName* .
        
                  - **CloudWatchOutputEnabled** *(boolean) --* 
        
                    Enables Systems Manager to send command output to CloudWatch Logs.
        
            - **NextToken** *(string) --* 
        
              (Optional) The token for the next set of items to return. (You received this token from a previous call.)
        
        """
        pass

    def list_compliance_items(self, Filters: List = None, ResourceIds: List = None, ResourceTypes: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListComplianceItems>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_compliance_items(
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ],
                      \'Type\': \'EQUAL\'|\'NOT_EQUAL\'|\'BEGIN_WITH\'|\'LESS_THAN\'|\'GREATER_THAN\'
                  },
              ],
              ResourceIds=[
                  \'string\',
              ],
              ResourceTypes=[
                  \'string\',
              ],
              NextToken=\'string\',
              MaxResults=123
          )
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
        
        :type NextToken: string
        :param NextToken: 
        
          A token to start the list. Use this token to get the next set of results. 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ComplianceItems\': [
                    {
                        \'ComplianceType\': \'string\',
                        \'ResourceType\': \'string\',
                        \'ResourceId\': \'string\',
                        \'Id\': \'string\',
                        \'Title\': \'string\',
                        \'Status\': \'COMPLIANT\'|\'NON_COMPLIANT\',
                        \'Severity\': \'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'INFORMATIONAL\'|\'UNSPECIFIED\',
                        \'ExecutionSummary\': {
                            \'ExecutionTime\': datetime(2015, 1, 1),
                            \'ExecutionId\': \'string\',
                            \'ExecutionType\': \'string\'
                        },
                        \'Details\': {
                            \'string\': \'string\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
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
        
                    The time the execution ran as a datetime object that is saved in the following format: yyyy-MM-dd\'T\'HH:mm:ss\'Z\'.
        
                  - **ExecutionId** *(string) --* 
        
                    An ID created by the system when ``PutComplianceItems`` was called. For example, ``CommandID`` is a valid execution ID. You can use this ID in subsequent calls.
        
                  - **ExecutionType** *(string) --* 
        
                    The type of execution. For example, ``Command`` is a valid execution type.
        
                - **Details** *(dict) --* 
        
                  A \"Key\": \"Value\" tag combination for the compliance item.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              The token for the next set of items to return. Use this token to get the next set of results.
        
        """
        pass

    def list_compliance_summaries(self, Filters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListComplianceSummaries>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_compliance_summaries(
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ],
                      \'Type\': \'EQUAL\'|\'NOT_EQUAL\'|\'BEGIN_WITH\'|\'LESS_THAN\'|\'GREATER_THAN\'
                  },
              ],
              NextToken=\'string\',
              MaxResults=123
          )
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
        
        :type NextToken: string
        :param NextToken: 
        
          A token to start the list. Use this token to get the next set of results. 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. Currently, you can specify null or 50. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ComplianceSummaryItems\': [
                    {
                        \'ComplianceType\': \'string\',
                        \'CompliantSummary\': {
                            \'CompliantCount\': 123,
                            \'SeveritySummary\': {
                                \'CriticalCount\': 123,
                                \'HighCount\': 123,
                                \'MediumCount\': 123,
                                \'LowCount\': 123,
                                \'InformationalCount\': 123,
                                \'UnspecifiedCount\': 123
                            }
                        },
                        \'NonCompliantSummary\': {
                            \'NonCompliantCount\': 123,
                            \'SeveritySummary\': {
                                \'CriticalCount\': 123,
                                \'HighCount\': 123,
                                \'MediumCount\': 123,
                                \'LowCount\': 123,
                                \'InformationalCount\': 123,
                                \'UnspecifiedCount\': 123
                            }
                        }
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token for the next set of items to return. Use this token to get the next set of results.
        
        """
        pass

    def list_document_versions(self, Name: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListDocumentVersions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_document_versions(
              Name=\'string\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the document about which you want version information.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DocumentVersions\': [
                    {
                        \'Name\': \'string\',
                        \'DocumentVersion\': \'string\',
                        \'CreatedDate\': datetime(2015, 1, 1),
                        \'IsDefaultVersion\': True|False,
                        \'DocumentFormat\': \'YAML\'|\'JSON\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                - **CreatedDate** *(datetime) --* 
        
                  The date the document was created.
        
                - **IsDefaultVersion** *(boolean) --* 
        
                  An identifier for the default version of the document.
        
                - **DocumentFormat** *(string) --* 
        
                  The document format, either JSON or YAML.
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def list_documents(self, DocumentFilterList: List = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListDocuments>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_documents(
              DocumentFilterList=[
                  {
                      \'key\': \'Name\'|\'Owner\'|\'PlatformTypes\'|\'DocumentType\',
                      \'value\': \'string\'
                  },
              ],
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
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
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DocumentIdentifiers\': [
                    {
                        \'Name\': \'string\',
                        \'Owner\': \'string\',
                        \'PlatformTypes\': [
                            \'Windows\'|\'Linux\',
                        ],
                        \'DocumentVersion\': \'string\',
                        \'DocumentType\': \'Command\'|\'Policy\'|\'Automation\'|\'Session\',
                        \'SchemaVersion\': \'string\',
                        \'DocumentFormat\': \'YAML\'|\'JSON\',
                        \'TargetType\': \'string\',
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def list_inventory_entries(self, InstanceId: str, TypeName: str, Filters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListInventoryEntries>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_inventory_entries(
              InstanceId=\'string\',
              TypeName=\'string\',
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ],
                      \'Type\': \'Equal\'|\'NotEqual\'|\'BeginWith\'|\'LessThan\'|\'GreaterThan\'|\'Exists\'
                  },
              ],
              NextToken=\'string\',
              MaxResults=123
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The instance ID for which you want inventory information.
        
        :type TypeName: string
        :param TypeName: **[REQUIRED]** 
        
          The type of inventory item for which you want information.
        
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
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of items to return. (You received this token from a previous call.)
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TypeName\': \'string\',
                \'InstanceId\': \'string\',
                \'SchemaVersion\': \'string\',
                \'CaptureTime\': \'string\',
                \'Entries\': [
                    {
                        \'string\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TypeName** *(string) --* 
        
              The type of inventory item returned by the request.
        
            - **InstanceId** *(string) --* 
        
              The instance ID targeted by the request to query inventory information.
        
            - **SchemaVersion** *(string) --* 
        
              The inventory schema version used by the instance(s).
        
            - **CaptureTime** *(string) --* 
        
              The time that inventory information was collected for the instance(s).
        
            - **Entries** *(list) --* 
        
              A list of inventory items on the instance(s).
        
              - *(dict) --* 
                
                - *(string) --* 
                  
                  - *(string) --* 
            
            - **NextToken** *(string) --* 
        
              The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
        
        """
        pass

    def list_resource_compliance_summaries(self, Filters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListResourceComplianceSummaries>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_resource_compliance_summaries(
              Filters=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ],
                      \'Type\': \'EQUAL\'|\'NOT_EQUAL\'|\'BEGIN_WITH\'|\'LESS_THAN\'|\'GREATER_THAN\'
                  },
              ],
              NextToken=\'string\',
              MaxResults=123
          )
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
        
        :type NextToken: string
        :param NextToken: 
        
          A token to start the list. Use this token to get the next set of results. 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ResourceComplianceSummaryItems\': [
                    {
                        \'ComplianceType\': \'string\',
                        \'ResourceType\': \'string\',
                        \'ResourceId\': \'string\',
                        \'Status\': \'COMPLIANT\'|\'NON_COMPLIANT\',
                        \'OverallSeverity\': \'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'INFORMATIONAL\'|\'UNSPECIFIED\',
                        \'ExecutionSummary\': {
                            \'ExecutionTime\': datetime(2015, 1, 1),
                            \'ExecutionId\': \'string\',
                            \'ExecutionType\': \'string\'
                        },
                        \'CompliantSummary\': {
                            \'CompliantCount\': 123,
                            \'SeveritySummary\': {
                                \'CriticalCount\': 123,
                                \'HighCount\': 123,
                                \'MediumCount\': 123,
                                \'LowCount\': 123,
                                \'InformationalCount\': 123,
                                \'UnspecifiedCount\': 123
                            }
                        },
                        \'NonCompliantSummary\': {
                            \'NonCompliantCount\': 123,
                            \'SeveritySummary\': {
                                \'CriticalCount\': 123,
                                \'HighCount\': 123,
                                \'MediumCount\': 123,
                                \'LowCount\': 123,
                                \'InformationalCount\': 123,
                                \'UnspecifiedCount\': 123
                            }
                        }
                    },
                ],
                \'NextToken\': \'string\'
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
        
                    The time the execution ran as a datetime object that is saved in the following format: yyyy-MM-dd\'T\'HH:mm:ss\'Z\'.
        
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
        
                  A list of items that aren\'t compliant for the resource.
        
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
        
            - **NextToken** *(string) --* 
        
              The token for the next set of items to return. Use this token to get the next set of results.
        
        """
        pass

    def list_resource_data_sync(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        The number of sync configurations might be too large to return using a single call to ``ListResourceDataSync`` . You can limit the number of sync configurations returned by using the ``MaxResults`` parameter. To determine whether there are more sync configurations to list, check the value of ``NextToken`` in the output. If there are more sync configurations to list, you can request them by specifying the ``NextToken`` returned in the call to the parameter of a subsequent call. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListResourceDataSync>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_resource_data_sync(
              NextToken=\'string\',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken: 
        
          A token to start the list. Use this token to get the next set of results. 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ResourceDataSyncItems\': [
                    {
                        \'SyncName\': \'string\',
                        \'S3Destination\': {
                            \'BucketName\': \'string\',
                            \'Prefix\': \'string\',
                            \'SyncFormat\': \'JsonSerDe\',
                            \'Region\': \'string\',
                            \'AWSKMSKeyARN\': \'string\'
                        },
                        \'LastSyncTime\': datetime(2015, 1, 1),
                        \'LastSuccessfulSyncTime\': datetime(2015, 1, 1),
                        \'LastStatus\': \'Successful\'|\'Failed\'|\'InProgress\',
                        \'SyncCreatedTime\': datetime(2015, 1, 1),
                        \'LastSyncStatusMessage\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token for the next set of items to return. Use this token to get the next set of results.
        
        """
        pass

    def list_tags_for_resource(self, ResourceType: str, ResourceId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListTagsForResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags_for_resource(
              ResourceType=\'Document\'|\'ManagedInstance\'|\'MaintenanceWindow\'|\'Parameter\'|\'PatchBaseline\',
              ResourceId=\'string\'
          )
        :type ResourceType: string
        :param ResourceType: **[REQUIRED]** 
        
          Returns a list of tags for a specific resource type.
        
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          The resource ID for which you want to see a list of tags.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TagList\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TagList** *(list) --* 
        
              A list of tags.
        
              - *(dict) --* 
        
                Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, Maintenance Windows, Parameter Store parameters, and patch baselines.
        
                - **Key** *(string) --* 
        
                  The name of the tag.
        
                - **Value** *(string) --* 
        
                  The value of the tag.
        
        """
        pass

    def modify_document_permission(self, Name: str, PermissionType: str, AccountIdsToAdd: List = None, AccountIdsToRemove: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ModifyDocumentPermission>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_document_permission(
              Name=\'string\',
              PermissionType=\'Share\',
              AccountIdsToAdd=[
                  \'string\',
              ],
              AccountIdsToRemove=[
                  \'string\',
              ]
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the document that you want to share.
        
        :type PermissionType: string
        :param PermissionType: **[REQUIRED]** 
        
          The permission type for the document. The permission type can be *Share* .
        
        :type AccountIdsToAdd: list
        :param AccountIdsToAdd: 
        
          The AWS user accounts that should have access to the document. The account IDs can either be a group of account IDs or *All* .
        
          - *(string) --* 
        
        :type AccountIdsToRemove: list
        :param AccountIdsToRemove: 
        
          The AWS user accounts that should no longer have access to the document. The AWS user account can either be a group of account IDs or *All* . This action has a higher priority than *AccountIdsToAdd* . If you specify an account ID to add and the same ID to remove, the system removes access to the document.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def put_compliance_items(self, ResourceId: str, ResourceType: str, ComplianceType: str, ExecutionSummary: Dict, Items: List, ItemContentHash: str = None) -> Dict:
        """
        
        ComplianceType can be one of the following:
        
        * ExecutionId: The execution ID when the patch, association, or custom compliance item was applied. 
         
        * ExecutionType: Specify patch, association, or Custom:``string`` . 
         
        * ExecutionTime. The time the patch, association, or custom compliance item was applied to the instance. 
         
        * Id: The patch, association, or custom compliance ID. 
         
        * Title: A title. 
         
        * Status: The status of the compliance item. For example, ``approved`` for patches, or ``Failed`` for associations. 
         
        * Severity: A patch severity. For example, ``critical`` . 
         
        * DocumentName: A SSM document name. For example, AWS-RunPatchBaseline. 
         
        * DocumentVersion: An SSM document version number. For example, 4. 
         
        * Classification: A patch classification. For example, ``security updates`` . 
         
        * PatchBaselineId: A patch baseline ID. 
         
        * PatchSeverity: A patch severity. For example, ``Critical`` . 
         
        * PatchState: A patch state. For example, ``InstancesWithFailedPatches`` . 
         
        * PatchGroup: The name of a patch group. 
         
        * InstalledTime: The time the association, patch, or custom compliance item was applied to the resource. Specify the time by using the following format: yyyy-MM-dd\'T\'HH:mm:ss\'Z\' 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/PutComplianceItems>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_compliance_items(
              ResourceId=\'string\',
              ResourceType=\'string\',
              ComplianceType=\'string\',
              ExecutionSummary={
                  \'ExecutionTime\': datetime(2015, 1, 1),
                  \'ExecutionId\': \'string\',
                  \'ExecutionType\': \'string\'
              },
              Items=[
                  {
                      \'Id\': \'string\',
                      \'Title\': \'string\',
                      \'Severity\': \'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'INFORMATIONAL\'|\'UNSPECIFIED\',
                      \'Status\': \'COMPLIANT\'|\'NON_COMPLIANT\',
                      \'Details\': {
                          \'string\': \'string\'
                      }
                  },
              ],
              ItemContentHash=\'string\'
          )
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          Specify an ID for this resource. For a managed instance, this is the instance ID.
        
        :type ResourceType: string
        :param ResourceType: **[REQUIRED]** 
        
          Specify the type of resource. ``ManagedInstance`` is currently the only supported resource type.
        
        :type ComplianceType: string
        :param ComplianceType: **[REQUIRED]** 
        
          Specify the compliance type. For example, specify Association (for a State Manager association), Patch, or Custom:``string`` .
        
        :type ExecutionSummary: dict
        :param ExecutionSummary: **[REQUIRED]** 
        
          A summary of the call execution that includes an execution ID, the type of execution (for example, ``Command`` ), and the date/time of the execution using a datetime object that is saved in the following format: yyyy-MM-dd\'T\'HH:mm:ss\'Z\'.
        
          - **ExecutionTime** *(datetime) --* **[REQUIRED]** 
        
            The time the execution ran as a datetime object that is saved in the following format: yyyy-MM-dd\'T\'HH:mm:ss\'Z\'.
        
          - **ExecutionId** *(string) --* 
        
            An ID created by the system when ``PutComplianceItems`` was called. For example, ``CommandID`` is a valid execution ID. You can use this ID in subsequent calls.
        
          - **ExecutionType** *(string) --* 
        
            The type of execution. For example, ``Command`` is a valid execution type.
        
        :type Items: list
        :param Items: **[REQUIRED]** 
        
          Information about the compliance as defined by the resource type. For example, for a patch compliance type, ``Items`` includes information about the PatchSeverity, Classification, etc.
        
          - *(dict) --* 
        
            Information about a compliance item.
        
            - **Id** *(string) --* 
        
              The compliance item ID. For example, if the compliance item is a Windows patch, the ID could be the number of the KB article.
        
            - **Title** *(string) --* 
        
              The title of the compliance item. For example, if the compliance item is a Windows patch, the title could be the title of the KB article for the patch; for example: Security Update for Active Directory Federation Services. 
        
            - **Severity** *(string) --* **[REQUIRED]** 
        
              The severity of the compliance status. Severity can be one of the following: Critical, High, Medium, Low, Informational, Unspecified.
        
            - **Status** *(string) --* **[REQUIRED]** 
        
              The status of the compliance item. An item is either COMPLIANT or NON_COMPLIANT.
        
            - **Details** *(dict) --* 
        
              A \"Key\": \"Value\" tag combination for the compliance item.
        
              - *(string) --* 
        
                - *(string) --* 
        
        :type ItemContentHash: string
        :param ItemContentHash: 
        
          MD5 or SHA-256 content hash. The content hash is used to determine if existing information should be overwritten or ignored. If the content hashes match, the request to put compliance information is ignored.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def put_inventory(self, InstanceId: str, Items: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/PutInventory>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_inventory(
              InstanceId=\'string\',
              Items=[
                  {
                      \'TypeName\': \'string\',
                      \'SchemaVersion\': \'string\',
                      \'CaptureTime\': \'string\',
                      \'ContentHash\': \'string\',
                      \'Content\': [
                          {
                              \'string\': \'string\'
                          },
                      ],
                      \'Context\': {
                          \'string\': \'string\'
                      }
                  },
              ]
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          One or more instance IDs where you want to add or update inventory items.
        
        :type Items: list
        :param Items: **[REQUIRED]** 
        
          The inventory items that you want to add or update on instances.
        
          - *(dict) --* 
        
            Information collected from managed instances based on your inventory policy document
        
            - **TypeName** *(string) --* **[REQUIRED]** 
        
              The name of the inventory type. Default inventory item type names start with AWS. Custom inventory type names will start with Custom. Default inventory item types include the following: AWS:AWSComponent, AWS:Application, AWS:InstanceInformation, AWS:Network, and AWS:WindowsUpdate.
        
            - **SchemaVersion** *(string) --* **[REQUIRED]** 
        
              The schema version for the inventory item.
        
            - **CaptureTime** *(string) --* **[REQUIRED]** 
        
              The time the inventory information was collected.
        
            - **ContentHash** *(string) --* 
        
              MD5 hash of the inventory item type contents. The content hash is used to determine whether to update inventory information. The PutInventory API does not update the inventory item type contents if the MD5 hash has not changed since last update. 
        
            - **Content** *(list) --* 
        
              The inventory data of the inventory type.
        
              - *(dict) --* 
        
                - *(string) --* 
        
                  - *(string) --* 
        
            - **Context** *(dict) --* 
        
              A map of associated properties for a specified inventory type. For example, with this attribute, you can specify the ``ExecutionId`` , ``ExecutionType`` , ``ComplianceType`` properties of the ``AWS:ComplianceItem`` type.
        
              - *(string) --* 
        
                - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Message\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Message** *(string) --* 
        
              Information about the request.
        
        """
        pass

    def put_parameter(self, Name: str, Value: str, Type: str, Description: str = None, KeyId: str = None, Overwrite: bool = None, AllowedPattern: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/PutParameter>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_parameter(
              Name=\'string\',
              Description=\'string\',
              Value=\'string\',
              Type=\'String\'|\'StringList\'|\'SecureString\',
              KeyId=\'string\',
              Overwrite=True|False,
              AllowedPattern=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The fully qualified name of the parameter that you want to add to the system. The fully qualified name includes the complete hierarchy of the parameter path and name. For example: ``/Dev/DBServer/MySQL/db-string13``  
        
          Naming Constraints:
        
          * Parameter names are case sensitive. 
           
          * A parameter name must be unique within an AWS Region 
           
          * A parameter name can\'t be prefixed with \"aws\" or \"ssm\" (case-insensitive). 
           
          * Parameter names can include only the following symbols and letters: ``a-zA-Z0-9_.-/``   
           
          * A parameter name can\'t include spaces. 
           
          * Parameter hierarchies are limited to a maximum depth of fifteen levels. 
           
          For additional information about valid values for parameter names, see `Requirements and Constraints for Parameter Names <http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-parameter-name-constraints.html>`__ in the *AWS Systems Manager User Guide* .
        
          .. note::
        
            The maximum length constraint listed below includes capacity for additional system attributes that are not part of the name. The maximum length for the fully qualified parameter name is 1011 characters. 
        
        :type Description: string
        :param Description: 
        
          Information about the parameter that you want to add to the system. Optional but recommended.
        
          .. warning::
        
            Do not enter personally identifiable information in this field.
        
        :type Value: string
        :param Value: **[REQUIRED]** 
        
          The parameter value that you want to add to the system.
        
        :type Type: string
        :param Type: **[REQUIRED]** 
        
          The type of parameter that you want to add to the system.
        
          Items in a ``StringList`` must be separated by a comma (,). You can\'t use other punctuation or special character to escape items in the list. If you have a parameter value that requires a comma, then use the ``String`` data type.
        
          .. note::
        
             ``SecureString`` is not currently supported for AWS CloudFormation templates or in the China Regions.
        
        :type KeyId: string
        :param KeyId: 
        
          The KMS Key ID that you want to use to encrypt a parameter. Either the default AWS Key Management Service (AWS KMS) key automatically assigned to your AWS account or a custom key. Required for parameters that use the ``SecureString`` data type.
        
          If you don\'t specify a key ID, the system uses the default key associated with your AWS account.
        
          * To use your default AWS KMS key, choose the ``SecureString`` data type, and do *not* specify the ``Key ID`` when you create the parameter. The system automatically populates ``Key ID`` with your default KMS key. 
           
          * To use a custom KMS key, choose the ``SecureString`` data type with the ``Key ID`` parameter. 
           
        :type Overwrite: boolean
        :param Overwrite: 
        
          Overwrite an existing parameter. If not specified, will default to \"false\".
        
        :type AllowedPattern: string
        :param AllowedPattern: 
        
          A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: AllowedPattern=^\d+$ 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Version\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Version** *(integer) --* 
        
              The new version number of a parameter. If you edit a parameter value, Parameter Store automatically creates a new version and assigns this new version a unique ID. You can reference a parameter version ID in API actions or in Systems Manager documents (SSM documents). By default, if you don\'t specify a specific version, the system returns the latest parameter value when a parameter is called.
        
        """
        pass

    def register_default_patch_baseline(self, BaselineId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/RegisterDefaultPatchBaseline>`_
        
        **Request Syntax** 
        ::
        
          response = client.register_default_patch_baseline(
              BaselineId=\'string\'
          )
        :type BaselineId: string
        :param BaselineId: **[REQUIRED]** 
        
          The ID of the patch baseline that should be the default patch baseline.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'BaselineId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **BaselineId** *(string) --* 
        
              The ID of the default patch baseline.
        
        """
        pass

    def register_patch_baseline_for_patch_group(self, BaselineId: str, PatchGroup: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/RegisterPatchBaselineForPatchGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.register_patch_baseline_for_patch_group(
              BaselineId=\'string\',
              PatchGroup=\'string\'
          )
        :type BaselineId: string
        :param BaselineId: **[REQUIRED]** 
        
          The ID of the patch baseline to register the patch group with.
        
        :type PatchGroup: string
        :param PatchGroup: **[REQUIRED]** 
        
          The name of the patch group that should be registered with the patch baseline.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'BaselineId\': \'string\',
                \'PatchGroup\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **BaselineId** *(string) --* 
        
              The ID of the patch baseline the patch group was registered with.
        
            - **PatchGroup** *(string) --* 
        
              The name of the patch group registered with the patch baseline.
        
        """
        pass

    def register_target_with_maintenance_window(self, WindowId: str, ResourceType: str, Targets: List, OwnerInformation: str = None, Name: str = None, Description: str = None, ClientToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/RegisterTargetWithMaintenanceWindow>`_
        
        **Request Syntax** 
        ::
        
          response = client.register_target_with_maintenance_window(
              WindowId=\'string\',
              ResourceType=\'INSTANCE\',
              Targets=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              OwnerInformation=\'string\',
              Name=\'string\',
              Description=\'string\',
              ClientToken=\'string\'
          )
        :type WindowId: string
        :param WindowId: **[REQUIRED]** 
        
          The ID of the Maintenance Window the target should be registered with.
        
        :type ResourceType: string
        :param ResourceType: **[REQUIRED]** 
        
          The type of target being registered with the Maintenance Window.
        
        :type Targets: list
        :param Targets: **[REQUIRED]** 
        
          The targets (either instances or tags). 
        
          Specify instances using the following format:
        
           ``Key=InstanceIds,Values=<instance-id-1>,<instance-id-2>``  
        
          Specify tags using either of the following formats:
        
           ``Key=tag:<tag-key>,Values=<tag-value-1>,<tag-value-2>``  
        
           ``Key=tag-key,Values=<tag-key-1>,<tag-key-2>``  
        
          - *(dict) --* 
        
            An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
            - **Key** *(string) --* 
        
              User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
            - **Values** *(list) --* 
        
              User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
              - *(string) --* 
        
        :type OwnerInformation: string
        :param OwnerInformation: 
        
          User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
        
        :type Name: string
        :param Name: 
        
          An optional name for the target.
        
        :type Description: string
        :param Description: 
        
          An optional description for the target.
        
        :type ClientToken: string
        :param ClientToken: 
        
          User-provided idempotency token.
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowTargetId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **WindowTargetId** *(string) --* 
        
              The ID of the target definition in this Maintenance Window.
        
        """
        pass

    def register_task_with_maintenance_window(self, WindowId: str, Targets: List, TaskArn: str, TaskType: str, MaxConcurrency: str, MaxErrors: str, ServiceRoleArn: str = None, TaskParameters: Dict = None, TaskInvocationParameters: Dict = None, Priority: int = None, LoggingInfo: Dict = None, Name: str = None, Description: str = None, ClientToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/RegisterTaskWithMaintenanceWindow>`_
        
        **Request Syntax** 
        ::
        
          response = client.register_task_with_maintenance_window(
              WindowId=\'string\',
              Targets=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              TaskArn=\'string\',
              ServiceRoleArn=\'string\',
              TaskType=\'RUN_COMMAND\'|\'AUTOMATION\'|\'STEP_FUNCTIONS\'|\'LAMBDA\',
              TaskParameters={
                  \'string\': {
                      \'Values\': [
                          \'string\',
                      ]
                  }
              },
              TaskInvocationParameters={
                  \'RunCommand\': {
                      \'Comment\': \'string\',
                      \'DocumentHash\': \'string\',
                      \'DocumentHashType\': \'Sha256\'|\'Sha1\',
                      \'NotificationConfig\': {
                          \'NotificationArn\': \'string\',
                          \'NotificationEvents\': [
                              \'All\'|\'InProgress\'|\'Success\'|\'TimedOut\'|\'Cancelled\'|\'Failed\',
                          ],
                          \'NotificationType\': \'Command\'|\'Invocation\'
                      },
                      \'OutputS3BucketName\': \'string\',
                      \'OutputS3KeyPrefix\': \'string\',
                      \'Parameters\': {
                          \'string\': [
                              \'string\',
                          ]
                      },
                      \'ServiceRoleArn\': \'string\',
                      \'TimeoutSeconds\': 123
                  },
                  \'Automation\': {
                      \'DocumentVersion\': \'string\',
                      \'Parameters\': {
                          \'string\': [
                              \'string\',
                          ]
                      }
                  },
                  \'StepFunctions\': {
                      \'Input\': \'string\',
                      \'Name\': \'string\'
                  },
                  \'Lambda\': {
                      \'ClientContext\': \'string\',
                      \'Qualifier\': \'string\',
                      \'Payload\': b\'bytes\'
                  }
              },
              Priority=123,
              MaxConcurrency=\'string\',
              MaxErrors=\'string\',
              LoggingInfo={
                  \'S3BucketName\': \'string\',
                  \'S3KeyPrefix\': \'string\',
                  \'S3Region\': \'string\'
              },
              Name=\'string\',
              Description=\'string\',
              ClientToken=\'string\'
          )
        :type WindowId: string
        :param WindowId: **[REQUIRED]** 
        
          The ID of the Maintenance Window the task should be added to.
        
        :type Targets: list
        :param Targets: **[REQUIRED]** 
        
          The targets (either instances or Maintenance Window targets).
        
          Specify instances using the following format: 
        
           ``Key=InstanceIds,Values=<instance-id-1>,<instance-id-2>``  
        
          Specify Maintenance Window targets using the following format:
        
           ``Key=<WindowTargetIds>,Values=<window-target-id-1>,<window-target-id-2>``  
        
          - *(dict) --* 
        
            An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
            - **Key** *(string) --* 
        
              User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
            - **Values** *(list) --* 
        
              User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
              - *(string) --* 
        
        :type TaskArn: string
        :param TaskArn: **[REQUIRED]** 
        
          The ARN of the task to execute 
        
        :type ServiceRoleArn: string
        :param ServiceRoleArn: 
        
          The role to assume when running the Maintenance Window task.
        
          If you do not specify a service role ARN, Systems Manager will use your account\'s service-linked role for Systems Manager by default. If no service-linked role for Systems Manager exists in your account, it will be created when you run ``RegisterTaskWithMaintenanceWindow`` without specifying a service role ARN.
        
          For more information, see `Service-Linked Role Permissions for Systems Manager <http://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles.html#slr-permissions>`__ and `Should I Use a Service-Linked Role or a Custom Service Role to Run Maintenance Window Tasks? <http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html#maintenance-window-tasks-service-role>`__ in the *AWS Systems Manager User Guide* .
        
        :type TaskType: string
        :param TaskType: **[REQUIRED]** 
        
          The type of task being registered.
        
        :type TaskParameters: dict
        :param TaskParameters: 
        
          The parameters that should be passed to the task when it is executed.
        
          .. note::
        
             ``TaskParameters`` has been deprecated. To specify parameters to pass to a task when it runs, instead use the ``Parameters`` option in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
        
          - *(string) --* 
        
            - *(dict) --* 
        
              Defines the values for a task parameter.
        
              - **Values** *(list) --* 
        
                This field contains an array of 0 or more strings, each 1 to 255 characters in length.
        
                - *(string) --* 
        
        :type TaskInvocationParameters: dict
        :param TaskInvocationParameters: 
        
          The parameters that the task should use during execution. Populate only the fields that match the task type. All other fields should be empty. 
        
          - **RunCommand** *(dict) --* 
        
            The parameters for a RUN_COMMAND task type.
        
            - **Comment** *(string) --* 
        
              Information about the command(s) to execute.
        
            - **DocumentHash** *(string) --* 
        
              The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.
        
            - **DocumentHashType** *(string) --* 
        
              SHA-256 or SHA-1. SHA-1 hashes have been deprecated.
        
            - **NotificationConfig** *(dict) --* 
        
              Configurations for sending notifications about command status changes on a per-instance basis.
        
              - **NotificationArn** *(string) --* 
        
                An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.
        
              - **NotificationEvents** *(list) --* 
        
                The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Configuring Amazon SNS Notifications for Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/rc-sns-notifications.html>`__ in the *AWS Systems Manager User Guide* .
        
                - *(string) --* 
        
              - **NotificationType** *(string) --* 
        
                Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 
        
            - **OutputS3BucketName** *(string) --* 
        
              The name of the Amazon S3 bucket.
        
            - **OutputS3KeyPrefix** *(string) --* 
        
              The Amazon S3 bucket subfolder.
        
            - **Parameters** *(dict) --* 
        
              The parameters for the RUN_COMMAND task execution.
        
              - *(string) --* 
        
                - *(list) --* 
        
                  - *(string) --* 
        
            - **ServiceRoleArn** *(string) --* 
        
              The IAM service role to assume during task execution.
        
            - **TimeoutSeconds** *(integer) --* 
        
              If this time is reached and the command has not already started executing, it doesn not execute.
        
          - **Automation** *(dict) --* 
        
            The parameters for an AUTOMATION task type.
        
            - **DocumentVersion** *(string) --* 
        
              The version of an Automation document to use during task execution.
        
            - **Parameters** *(dict) --* 
        
              The parameters for the AUTOMATION task.
        
              For information about specifying and updating task parameters, see  RegisterTaskWithMaintenanceWindow and  UpdateMaintenanceWindowTask .
        
              .. note::
        
                 ``LoggingInfo`` has been deprecated. To specify an S3 bucket to contain logs, instead use the ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
        
                 ``TaskParameters`` has been deprecated. To specify parameters to pass to a task when it runs, instead use the ``Parameters`` option in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
        
                For AUTOMATION task types, Systems Manager ignores any values specified for these parameters.
        
              - *(string) --* 
        
                - *(list) --* 
        
                  - *(string) --* 
        
          - **StepFunctions** *(dict) --* 
        
            The parameters for a STEP_FUNCTION task type.
        
            - **Input** *(string) --* 
        
              The inputs for the STEP_FUNCTION task.
        
            - **Name** *(string) --* 
        
              The name of the STEP_FUNCTION task.
        
          - **Lambda** *(dict) --* 
        
            The parameters for a LAMBDA task type.
        
            - **ClientContext** *(string) --* 
        
              Pass client-specific information to the Lambda function that you are invoking. You can then process the client information in your Lambda function as you choose through the context variable.
        
            - **Qualifier** *(string) --* 
        
              (Optional) Specify a Lambda function version or alias name. If you specify a function version, the action uses the qualified function ARN to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version to which the alias points.
        
            - **Payload** *(bytes) --* 
        
              JSON to provide to your Lambda function as input.
        
        :type Priority: integer
        :param Priority: 
        
          The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.
        
        :type MaxConcurrency: string
        :param MaxConcurrency: **[REQUIRED]** 
        
          The maximum number of targets this task can be run for in parallel.
        
        :type MaxErrors: string
        :param MaxErrors: **[REQUIRED]** 
        
          The maximum number of errors allowed before this task stops being scheduled.
        
        :type LoggingInfo: dict
        :param LoggingInfo: 
        
          A structure containing information about an Amazon S3 bucket to write instance-level logs to. 
        
          .. note::
        
             ``LoggingInfo`` has been deprecated. To specify an S3 bucket to contain logs, instead use the ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
        
          - **S3BucketName** *(string) --* **[REQUIRED]** 
        
            The name of an Amazon S3 bucket where execution logs are stored .
        
          - **S3KeyPrefix** *(string) --* 
        
            (Optional) The Amazon S3 bucket subfolder. 
        
          - **S3Region** *(string) --* **[REQUIRED]** 
        
            The region where the Amazon S3 bucket is located.
        
        :type Name: string
        :param Name: 
        
          An optional name for the task.
        
        :type Description: string
        :param Description: 
        
          An optional description for the task.
        
        :type ClientToken: string
        :param ClientToken: 
        
          User-provided idempotency token.
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowTaskId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **WindowTaskId** *(string) --* 
        
              The ID of the task in the Maintenance Window.
        
        """
        pass

    def remove_tags_from_resource(self, ResourceType: str, ResourceId: str, TagKeys: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/RemoveTagsFromResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.remove_tags_from_resource(
              ResourceType=\'Document\'|\'ManagedInstance\'|\'MaintenanceWindow\'|\'Parameter\'|\'PatchBaseline\',
              ResourceId=\'string\',
              TagKeys=[
                  \'string\',
              ]
          )
        :type ResourceType: string
        :param ResourceType: **[REQUIRED]** 
        
          The type of resource of which you want to remove a tag.
        
          .. note::
        
            The ManagedInstance type for this API action is only for on-premises managed instances. You must specify the the name of the managed instance in the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.
        
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          The resource ID for which you want to remove tags. Use the ID of the resource. Here are some examples:
        
          ManagedInstance: mi-012345abcde
        
          MaintenanceWindow: mw-012345abcde
        
          PatchBaseline: pb-012345abcde
        
          For the Document and Parameter values, use the name of the resource.
        
          .. note::
        
            The ManagedInstance type for this API action is only for on-premises managed instances. You must specify the the name of the managed instance in the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.
        
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** 
        
          Tag keys that you want to remove from the specified resource.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def resume_session(self, SessionId: str) -> Dict:
        """
        
        .. note::
        
          This command is primarily for use by client machines to automatically reconnect during intermittent network issues. It is not intended for any other use.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ResumeSession>`_
        
        **Request Syntax** 
        ::
        
          response = client.resume_session(
              SessionId=\'string\'
          )
        :type SessionId: string
        :param SessionId: **[REQUIRED]** 
        
          The ID of the disconnected session to resume.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SessionId\': \'string\',
                \'TokenValue\': \'string\',
                \'StreamUrl\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SessionId** *(string) --* 
        
              The ID of the session.
        
            - **TokenValue** *(string) --* 
        
              An encrypted token value containing session and caller information. Used to authenticate the connection to the instance.
        
            - **StreamUrl** *(string) --* 
        
              A URL back to SSM Agent on the instance that the Session Manager client uses to send commands and receive output from the instance. Format: ``wss://ssm-messages.**region** .amazonaws.com/v1/data-channel/**session-id** ?stream=(input|output)`` .
        
               **region** represents the Region identifier for an AWS Region supported by AWS Systems Manager, such as ``us-east-2`` for the US East (Ohio) Region. For a list of supported **region** values, see the **Region** column in the `AWS Systems Manager table of regions and endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html#ssm_region>`__ in the *AWS General Reference* .
        
               **session-id** represents the ID of a Session Manager session, such as ``1a2b3c4dEXAMPLE`` .
        
        """
        pass

    def send_automation_signal(self, AutomationExecutionId: str, SignalType: str, Payload: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/SendAutomationSignal>`_
        
        **Request Syntax** 
        ::
        
          response = client.send_automation_signal(
              AutomationExecutionId=\'string\',
              SignalType=\'Approve\'|\'Reject\'|\'StartStep\'|\'StopStep\'|\'Resume\',
              Payload={
                  \'string\': [
                      \'string\',
                  ]
              }
          )
        :type AutomationExecutionId: string
        :param AutomationExecutionId: **[REQUIRED]** 
        
          The unique identifier for an existing Automation execution that you want to send the signal to.
        
        :type SignalType: string
        :param SignalType: **[REQUIRED]** 
        
          The type of signal. Valid signal types include the following: Approve and Reject 
        
        :type Payload: dict
        :param Payload: 
        
          The data sent with the signal. The data schema depends on the type of signal used in the request. 
        
          - *(string) --* 
        
            - *(list) --* 
        
              - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def send_command(self, DocumentName: str, InstanceIds: List = None, Targets: List = None, DocumentVersion: str = None, DocumentHash: str = None, DocumentHashType: str = None, TimeoutSeconds: int = None, Comment: str = None, Parameters: Dict = None, OutputS3Region: str = None, OutputS3BucketName: str = None, OutputS3KeyPrefix: str = None, MaxConcurrency: str = None, MaxErrors: str = None, ServiceRoleArn: str = None, NotificationConfig: Dict = None, CloudWatchOutputConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/SendCommand>`_
        
        **Request Syntax** 
        ::
        
          response = client.send_command(
              InstanceIds=[
                  \'string\',
              ],
              Targets=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DocumentName=\'string\',
              DocumentVersion=\'string\',
              DocumentHash=\'string\',
              DocumentHashType=\'Sha256\'|\'Sha1\',
              TimeoutSeconds=123,
              Comment=\'string\',
              Parameters={
                  \'string\': [
                      \'string\',
                  ]
              },
              OutputS3Region=\'string\',
              OutputS3BucketName=\'string\',
              OutputS3KeyPrefix=\'string\',
              MaxConcurrency=\'string\',
              MaxErrors=\'string\',
              ServiceRoleArn=\'string\',
              NotificationConfig={
                  \'NotificationArn\': \'string\',
                  \'NotificationEvents\': [
                      \'All\'|\'InProgress\'|\'Success\'|\'TimedOut\'|\'Cancelled\'|\'Failed\',
                  ],
                  \'NotificationType\': \'Command\'|\'Invocation\'
              },
              CloudWatchOutputConfig={
                  \'CloudWatchLogGroupName\': \'string\',
                  \'CloudWatchOutputEnabled\': True|False
              }
          )
        :type InstanceIds: list
        :param InstanceIds: 
        
          The instance IDs where the command should execute. You can specify a maximum of 50 IDs. If you prefer not to list individual instance IDs, you can instead send commands to a fleet of instances using the Targets parameter, which accepts EC2 tags. For more information about how to use targets, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
          - *(string) --* 
        
        :type Targets: list
        :param Targets: 
        
          (Optional) An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don\'t provide one or more instance IDs in the call. For more information about how to use targets, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
          - *(dict) --* 
        
            An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
            - **Key** *(string) --* 
        
              User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
            - **Values** *(list) --* 
        
              User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
              - *(string) --* 
        
        :type DocumentName: string
        :param DocumentName: **[REQUIRED]** 
        
          Required. The name of the Systems Manager document to execute. This can be a public document or a custom document.
        
        :type DocumentVersion: string
        :param DocumentVersion: 
        
          The SSM document version to use in the request. You can specify $DEFAULT, $LATEST, or a specific version number. If you execute commands by using the AWS CLI, then you must escape the first two options by using a backslash. If you specify a version number, then you don\'t need to use the backslash. For example:
        
          --document-version \"\$DEFAULT\"
        
          --document-version \"\$LATEST\"
        
          --document-version \"3\"
        
        :type DocumentHash: string
        :param DocumentHash: 
        
          The Sha256 or Sha1 hash created by the system when the document was created. 
        
          .. note::
        
            Sha1 hashes have been deprecated.
        
        :type DocumentHashType: string
        :param DocumentHashType: 
        
          Sha256 or Sha1.
        
          .. note::
        
            Sha1 hashes have been deprecated.
        
        :type TimeoutSeconds: integer
        :param TimeoutSeconds: 
        
          If this time is reached and the command has not already started executing, it will not run.
        
        :type Comment: string
        :param Comment: 
        
          User-specified information about the command, such as a brief description of what the command should do.
        
        :type Parameters: dict
        :param Parameters: 
        
          The required and optional parameters specified in the document being executed.
        
          - *(string) --* 
        
            - *(list) --* 
        
              - *(string) --* 
        
        :type OutputS3Region: string
        :param OutputS3Region: 
        
          (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
        
        :type OutputS3BucketName: string
        :param OutputS3BucketName: 
        
          The name of the S3 bucket where command execution responses should be stored.
        
        :type OutputS3KeyPrefix: string
        :param OutputS3KeyPrefix: 
        
          The directory structure within the S3 bucket where the responses should be stored.
        
        :type MaxConcurrency: string
        :param MaxConcurrency: 
        
          (Optional) The maximum number of instances that are allowed to execute the command at the same time. You can specify a number such as 10 or a percentage such as 10%. The default value is 50. For more information about how to use MaxConcurrency, see `Using Concurrency Controls <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-velocity>`__ in the *AWS Systems Manager User Guide* .
        
        :type MaxErrors: string
        :param MaxErrors: 
        
          The maximum number of errors allowed without the command failing. When the command fails one more time beyond the value of MaxErrors, the systems stops sending the command to additional targets. You can specify a number like 10 or a percentage like 10%. The default value is 0. For more information about how to use MaxErrors, see `Using Error Controls <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-maxerrors>`__ in the *AWS Systems Manager User Guide* .
        
        :type ServiceRoleArn: string
        :param ServiceRoleArn: 
        
          The IAM role that Systems Manager uses to send notifications. 
        
        :type NotificationConfig: dict
        :param NotificationConfig: 
        
          Configurations for sending notifications.
        
          - **NotificationArn** *(string) --* 
        
            An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.
        
          - **NotificationEvents** *(list) --* 
        
            The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Configuring Amazon SNS Notifications for Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/rc-sns-notifications.html>`__ in the *AWS Systems Manager User Guide* .
        
            - *(string) --* 
        
          - **NotificationType** *(string) --* 
        
            Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 
        
        :type CloudWatchOutputConfig: dict
        :param CloudWatchOutputConfig: 
        
          Enables Systems Manager to send Run Command output to Amazon CloudWatch Logs. 
        
          - **CloudWatchLogGroupName** *(string) --* 
        
            The name of the CloudWatch log group where you want to send command output. If you don\'t specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/*SystemsManagerDocumentName* .
        
          - **CloudWatchOutputEnabled** *(boolean) --* 
        
            Enables Systems Manager to send command output to CloudWatch Logs.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Command\': {
                    \'CommandId\': \'string\',
                    \'DocumentName\': \'string\',
                    \'DocumentVersion\': \'string\',
                    \'Comment\': \'string\',
                    \'ExpiresAfter\': datetime(2015, 1, 1),
                    \'Parameters\': {
                        \'string\': [
                            \'string\',
                        ]
                    },
                    \'InstanceIds\': [
                        \'string\',
                    ],
                    \'Targets\': [
                        {
                            \'Key\': \'string\',
                            \'Values\': [
                                \'string\',
                            ]
                        },
                    ],
                    \'RequestedDateTime\': datetime(2015, 1, 1),
                    \'Status\': \'Pending\'|\'InProgress\'|\'Success\'|\'Cancelled\'|\'Failed\'|\'TimedOut\'|\'Cancelling\',
                    \'StatusDetails\': \'string\',
                    \'OutputS3Region\': \'string\',
                    \'OutputS3BucketName\': \'string\',
                    \'OutputS3KeyPrefix\': \'string\',
                    \'MaxConcurrency\': \'string\',
                    \'MaxErrors\': \'string\',
                    \'TargetCount\': 123,
                    \'CompletedCount\': 123,
                    \'ErrorCount\': 123,
                    \'DeliveryTimedOutCount\': 123,
                    \'ServiceRole\': \'string\',
                    \'NotificationConfig\': {
                        \'NotificationArn\': \'string\',
                        \'NotificationEvents\': [
                            \'All\'|\'InProgress\'|\'Success\'|\'TimedOut\'|\'Cancelled\'|\'Failed\',
                        ],
                        \'NotificationType\': \'Command\'|\'Invocation\'
                    },
                    \'CloudWatchOutputConfig\': {
                        \'CloudWatchLogGroupName\': \'string\',
                        \'CloudWatchOutputEnabled\': True|False
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Command** *(dict) --* 
        
              The request as it was received by Systems Manager. Also provides the command ID which can be used future references to this request.
        
              - **CommandId** *(string) --* 
        
                A unique identifier for this command.
        
              - **DocumentName** *(string) --* 
        
                The name of the document requested for execution.
        
              - **DocumentVersion** *(string) --* 
        
                The SSM document version.
        
              - **Comment** *(string) --* 
        
                User-specified information about the command, such as a brief description of what the command should do.
        
              - **ExpiresAfter** *(datetime) --* 
        
                If this time is reached and the command has not already started executing, it will not run. Calculated based on the ExpiresAfter user input provided as part of the SendCommand API.
        
              - **Parameters** *(dict) --* 
        
                The parameter values to be inserted in the document when executing the command.
        
                - *(string) --* 
                  
                  - *(list) --* 
                    
                    - *(string) --* 
                
              - **InstanceIds** *(list) --* 
        
                The instance IDs against which this command was requested.
        
                - *(string) --* 
            
              - **Targets** *(list) --* 
        
                An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don\'t provide one or more instance IDs in the call.
        
                - *(dict) --* 
        
                  An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                  - **Key** *(string) --* 
        
                    User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                  - **Values** *(list) --* 
        
                    User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
                    - *(string) --* 
                
              - **RequestedDateTime** *(datetime) --* 
        
                The date and time the command was requested.
        
              - **Status** *(string) --* 
        
                The status of the command.
        
              - **StatusDetails** *(string) --* 
        
                A detailed status of the command execution. StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see `Understanding Command Statuses <http://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html>`__ in the *AWS Systems Manager User Guide* . StatusDetails can be one of the following values:
        
                * Pending: The command has not been sent to any instances. 
                 
                * In Progress: The command has been sent to at least one instance but has not reached a final state on all instances. 
                 
                * Success: The command successfully executed on all invocations. This is a terminal state. 
                 
                * Delivery Timed Out: The value of MaxErrors or more command invocations shows a status of Delivery Timed Out. This is a terminal state. 
                 
                * Execution Timed Out: The value of MaxErrors or more command invocations shows a status of Execution Timed Out. This is a terminal state. 
                 
                * Failed: The value of MaxErrors or more command invocations shows a status of Failed. This is a terminal state. 
                 
                * Incomplete: The command was attempted on all instances and one or more invocations does not have a value of Success but not enough invocations failed for the status to be Failed. This is a terminal state. 
                 
                * Canceled: The command was terminated before it was completed. This is a terminal state. 
                 
                * Rate Exceeded: The number of instances targeted by the command exceeded the account limit for pending invocations. The system has canceled the command before executing it on any instance. This is a terminal state. 
                 
              - **OutputS3Region** *(string) --* 
        
                (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
        
              - **OutputS3BucketName** *(string) --* 
        
                The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command.
        
              - **OutputS3KeyPrefix** *(string) --* 
        
                The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command.
        
              - **MaxConcurrency** *(string) --* 
        
                The maximum number of instances that are allowed to execute the command at the same time. You can specify a number of instances, such as 10, or a percentage of instances, such as 10%. The default value is 50. For more information about how to use MaxConcurrency, see `Executing Commands Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html>`__ in the *AWS Systems Manager User Guide* .
        
              - **MaxErrors** *(string) --* 
        
                The maximum number of errors allowed before the system stops sending the command to additional targets. You can specify a number of errors, such as 10, or a percentage or errors, such as 10%. The default value is 0. For more information about how to use MaxErrors, see `Executing Commands Using Systems Manager Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html>`__ in the *AWS Systems Manager User Guide* .
        
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
        
                  The name of the CloudWatch log group where you want to send command output. If you don\'t specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/*SystemsManagerDocumentName* .
        
                - **CloudWatchOutputEnabled** *(boolean) --* 
        
                  Enables Systems Manager to send command output to CloudWatch Logs.
        
        """
        pass

    def start_associations_once(self, AssociationIds: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/StartAssociationsOnce>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_associations_once(
              AssociationIds=[
                  \'string\',
              ]
          )
        :type AssociationIds: list
        :param AssociationIds: **[REQUIRED]** 
        
          The association IDs that you want to execute immediately and only one time.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def start_automation_execution(self, DocumentName: str, DocumentVersion: str = None, Parameters: Dict = None, ClientToken: str = None, Mode: str = None, TargetParameterName: str = None, Targets: List = None, TargetMaps: List = None, MaxConcurrency: str = None, MaxErrors: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/StartAutomationExecution>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_automation_execution(
              DocumentName=\'string\',
              DocumentVersion=\'string\',
              Parameters={
                  \'string\': [
                      \'string\',
                  ]
              },
              ClientToken=\'string\',
              Mode=\'Auto\'|\'Interactive\',
              TargetParameterName=\'string\',
              Targets=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              TargetMaps=[
                  {
                      \'string\': [
                          \'string\',
                      ]
                  },
              ],
              MaxConcurrency=\'string\',
              MaxErrors=\'string\'
          )
        :type DocumentName: string
        :param DocumentName: **[REQUIRED]** 
        
          The name of the Automation document to use for this execution.
        
        :type DocumentVersion: string
        :param DocumentVersion: 
        
          The version of the Automation document to use for this execution.
        
        :type Parameters: dict
        :param Parameters: 
        
          A key-value map of execution parameters, which match the declared parameters in the Automation document.
        
          - *(string) --* 
        
            - *(list) --* 
        
              - *(string) --* 
        
        :type ClientToken: string
        :param ClientToken: 
        
          User-provided idempotency token. The token must be unique, is case insensitive, enforces the UUID format, and can\'t be reused.
        
        :type Mode: string
        :param Mode: 
        
          The execution mode of the automation. Valid modes include the following: Auto and Interactive. The default mode is Auto.
        
        :type TargetParameterName: string
        :param TargetParameterName: 
        
          The name of the parameter used as the target resource for the rate-controlled execution. Required if you specify targets.
        
        :type Targets: list
        :param Targets: 
        
          A key-value mapping to target resources. Required if you specify TargetParameterName.
        
          - *(dict) --* 
        
            An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
            - **Key** *(string) --* 
        
              User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
            - **Values** *(list) --* 
        
              User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
              - *(string) --* 
        
        :type TargetMaps: list
        :param TargetMaps: 
        
          A key-value mapping of document parameters to target resources. Both Targets and TargetMaps cannot be specified together.
        
          - *(dict) --* 
        
            - *(string) --* 
        
              - *(list) --* 
        
                - *(string) --* 
        
        :type MaxConcurrency: string
        :param MaxConcurrency: 
        
          The maximum number of targets allowed to run this task in parallel. You can specify a number, such as 10, or a percentage, such as 10%. The default value is 10.
        
        :type MaxErrors: string
        :param MaxErrors: 
        
          The number of errors that are allowed before the system stops running the automation on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops running the automation when the fourth error is received. If you specify 0, then the system stops running the automation on additional targets after the first error result is returned. If you run an automation on 50 resources and set max-errors to 10%, then the system stops running the automation on additional targets when the sixth error is received.
        
          Executions that are already running an automation when max-errors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set max-concurrency to 1 so the executions proceed one at a time.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AutomationExecutionId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AutomationExecutionId** *(string) --* 
        
              The unique ID of a newly scheduled automation execution.
        
        """
        pass

    def start_session(self, Target: str, DocumentName: str = None, Parameters: Dict = None) -> Dict:
        """
        
        .. note::
        
          AWS CLI usage: ``start-session`` is an interactive command that requires the Session Manager plugin to be installed on the client machine making the call. For information, see `Install the Session Manager Plugin for the AWS CLI <http://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html>`__ in the *AWS Systems Manager User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/StartSession>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_session(
              Target=\'string\',
              DocumentName=\'string\',
              Parameters={
                  \'string\': [
                      \'string\',
                  ]
              }
          )
        :type Target: string
        :param Target: **[REQUIRED]** 
        
          The instance to connect to for the session.
        
        :type DocumentName: string
        :param DocumentName: 
        
          The name of the SSM document to define the parameters and plugin settings for the session. For example, ``SSM-SessionManagerRunShell`` . If no document name is provided, a shell to the instance is launched by default.
        
        :type Parameters: dict
        :param Parameters: 
        
          Reserved for future use.
        
          - *(string) --* 
        
            - *(list) --* 
        
              - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SessionId\': \'string\',
                \'TokenValue\': \'string\',
                \'StreamUrl\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SessionId** *(string) --* 
        
              The ID of the session.
        
            - **TokenValue** *(string) --* 
        
              An encrypted token value containing session and caller information. Used to authenticate the connection to the instance.
        
            - **StreamUrl** *(string) --* 
        
              A URL back to SSM Agent on the instance that the Session Manager client uses to send commands and receive output from the instance. Format: ``wss://ssm-messages.**region** .amazonaws.com/v1/data-channel/**session-id** ?stream=(input|output)``  
        
               **region** represents the Region identifier for an AWS Region supported by AWS Systems Manager, such as ``us-east-2`` for the US East (Ohio) Region. For a list of supported **region** values, see the **Region** column in the `AWS Systems Manager table of regions and endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html#ssm_region>`__ in the *AWS General Reference* .
        
               **session-id** represents the ID of a Session Manager session, such as ``1a2b3c4dEXAMPLE`` .
        
        """
        pass

    def stop_automation_execution(self, AutomationExecutionId: str, Type: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/StopAutomationExecution>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_automation_execution(
              AutomationExecutionId=\'string\',
              Type=\'Complete\'|\'Cancel\'
          )
        :type AutomationExecutionId: string
        :param AutomationExecutionId: **[REQUIRED]** 
        
          The execution ID of the Automation to stop.
        
        :type Type: string
        :param Type: 
        
          The stop request type. Valid types include the following: Cancel and Complete. The default type is Cancel.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def terminate_session(self, SessionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/TerminateSession>`_
        
        **Request Syntax** 
        ::
        
          response = client.terminate_session(
              SessionId=\'string\'
          )
        :type SessionId: string
        :param SessionId: **[REQUIRED]** 
        
          The ID of the session to terminate.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SessionId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SessionId** *(string) --* 
        
              The ID of the session that has been terminated.
        
        """
        pass

    def update_association(self, AssociationId: str, Parameters: Dict = None, DocumentVersion: str = None, ScheduleExpression: str = None, OutputLocation: Dict = None, Name: str = None, Targets: List = None, AssociationName: str = None, AssociationVersion: str = None, MaxErrors: str = None, MaxConcurrency: str = None, ComplianceSeverity: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateAssociation>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_association(
              AssociationId=\'string\',
              Parameters={
                  \'string\': [
                      \'string\',
                  ]
              },
              DocumentVersion=\'string\',
              ScheduleExpression=\'string\',
              OutputLocation={
                  \'S3Location\': {
                      \'OutputS3Region\': \'string\',
                      \'OutputS3BucketName\': \'string\',
                      \'OutputS3KeyPrefix\': \'string\'
                  }
              },
              Name=\'string\',
              Targets=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              AssociationName=\'string\',
              AssociationVersion=\'string\',
              MaxErrors=\'string\',
              MaxConcurrency=\'string\',
              ComplianceSeverity=\'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'UNSPECIFIED\'
          )
        :type AssociationId: string
        :param AssociationId: **[REQUIRED]** 
        
          The ID of the association you want to update. 
        
        :type Parameters: dict
        :param Parameters: 
        
          The parameters you want to update for the association. If you create a parameter using Parameter Store, you can reference the parameter using {{ssm:parameter-name}}
        
          - *(string) --* 
        
            - *(list) --* 
        
              - *(string) --* 
        
        :type DocumentVersion: string
        :param DocumentVersion: 
        
          The document version you want update for the association. 
        
        :type ScheduleExpression: string
        :param ScheduleExpression: 
        
          The cron expression used to schedule the association that you want to update.
        
        :type OutputLocation: dict
        :param OutputLocation: 
        
          An Amazon S3 bucket where you want to store the results of this request.
        
          - **S3Location** *(dict) --* 
        
            An Amazon S3 bucket where you want to store the results of this request.
        
            - **OutputS3Region** *(string) --* 
        
              (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
        
            - **OutputS3BucketName** *(string) --* 
        
              The name of the Amazon S3 bucket.
        
            - **OutputS3KeyPrefix** *(string) --* 
        
              The Amazon S3 bucket subfolder.
        
        :type Name: string
        :param Name: 
        
          The name of the association document.
        
        :type Targets: list
        :param Targets: 
        
          The targets of the association.
        
          - *(dict) --* 
        
            An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
            - **Key** *(string) --* 
        
              User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
            - **Values** *(list) --* 
        
              User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
              - *(string) --* 
        
        :type AssociationName: string
        :param AssociationName: 
        
          The name of the association that you want to update.
        
        :type AssociationVersion: string
        :param AssociationVersion: 
        
          This parameter is provided for concurrency control purposes. You must specify the latest association version in the service. If you want to ensure that this request succeeds, either specify ``$LATEST`` , or omit this parameter.
        
        :type MaxErrors: string
        :param MaxErrors: 
        
          The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.
        
          Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.
        
        :type MaxConcurrency: string
        :param MaxConcurrency: 
        
          The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
        
          If a new instance starts and attempts to execute an association while Systems Manager is executing MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.
        
        :type ComplianceSeverity: string
        :param ComplianceSeverity: 
        
          The severity level to assign to the association.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AssociationDescription\': {
                    \'Name\': \'string\',
                    \'InstanceId\': \'string\',
                    \'AssociationVersion\': \'string\',
                    \'Date\': datetime(2015, 1, 1),
                    \'LastUpdateAssociationDate\': datetime(2015, 1, 1),
                    \'Status\': {
                        \'Date\': datetime(2015, 1, 1),
                        \'Name\': \'Pending\'|\'Success\'|\'Failed\',
                        \'Message\': \'string\',
                        \'AdditionalInfo\': \'string\'
                    },
                    \'Overview\': {
                        \'Status\': \'string\',
                        \'DetailedStatus\': \'string\',
                        \'AssociationStatusAggregatedCount\': {
                            \'string\': 123
                        }
                    },
                    \'DocumentVersion\': \'string\',
                    \'Parameters\': {
                        \'string\': [
                            \'string\',
                        ]
                    },
                    \'AssociationId\': \'string\',
                    \'Targets\': [
                        {
                            \'Key\': \'string\',
                            \'Values\': [
                                \'string\',
                            ]
                        },
                    ],
                    \'ScheduleExpression\': \'string\',
                    \'OutputLocation\': {
                        \'S3Location\': {
                            \'OutputS3Region\': \'string\',
                            \'OutputS3BucketName\': \'string\',
                            \'OutputS3KeyPrefix\': \'string\'
                        }
                    },
                    \'LastExecutionDate\': datetime(2015, 1, 1),
                    \'LastSuccessfulExecutionDate\': datetime(2015, 1, 1),
                    \'AssociationName\': \'string\',
                    \'MaxErrors\': \'string\',
                    \'MaxConcurrency\': \'string\',
                    \'ComplianceSeverity\': \'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'UNSPECIFIED\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AssociationDescription** *(dict) --* 
        
              The description of the association that was updated.
        
              - **Name** *(string) --* 
        
                The name of the Systems Manager document.
        
              - **InstanceId** *(string) --* 
        
                The ID of the instance.
        
              - **AssociationVersion** *(string) --* 
        
                The association version.
        
              - **Date** *(datetime) --* 
        
                The date when the association was made.
        
              - **LastUpdateAssociationDate** *(datetime) --* 
        
                The date when the association was last updated.
        
              - **Status** *(dict) --* 
        
                The association status.
        
                - **Date** *(datetime) --* 
        
                  The date when the status changed.
        
                - **Name** *(string) --* 
        
                  The status.
        
                - **Message** *(string) --* 
        
                  The reason for the status.
        
                - **AdditionalInfo** *(string) --* 
        
                  A user-defined string.
        
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
              
              - **DocumentVersion** *(string) --* 
        
                The document version.
        
              - **Parameters** *(dict) --* 
        
                A description of the parameters for a document. 
        
                - *(string) --* 
                  
                  - *(list) --* 
                    
                    - *(string) --* 
                
              - **AssociationId** *(string) --* 
        
                The association ID.
        
              - **Targets** *(list) --* 
        
                The instances targeted by the request. 
        
                - *(dict) --* 
        
                  An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                  - **Key** *(string) --* 
        
                    User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                  - **Values** *(list) --* 
        
                    User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
                    - *(string) --* 
                
              - **ScheduleExpression** *(string) --* 
        
                A cron expression that specifies a schedule when the association runs.
        
              - **OutputLocation** *(dict) --* 
        
                An Amazon S3 bucket where you want to store the output details of the request.
        
                - **S3Location** *(dict) --* 
        
                  An Amazon S3 bucket where you want to store the results of this request.
        
                  - **OutputS3Region** *(string) --* 
        
                    (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
        
                  - **OutputS3BucketName** *(string) --* 
        
                    The name of the Amazon S3 bucket.
        
                  - **OutputS3KeyPrefix** *(string) --* 
        
                    The Amazon S3 bucket subfolder.
        
              - **LastExecutionDate** *(datetime) --* 
        
                The date on which the association was last run.
        
              - **LastSuccessfulExecutionDate** *(datetime) --* 
        
                The last date on which the association was successfully run.
        
              - **AssociationName** *(string) --* 
        
                The association name.
        
              - **MaxErrors** *(string) --* 
        
                The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.
        
                Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.
        
              - **MaxConcurrency** *(string) --* 
        
                The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
        
                If a new instance starts and attempts to execute an association while Systems Manager is executing MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.
        
              - **ComplianceSeverity** *(string) --* 
        
                The severity level that is assigned to the association.
        
        """
        pass

    def update_association_status(self, Name: str, InstanceId: str, AssociationStatus: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateAssociationStatus>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_association_status(
              Name=\'string\',
              InstanceId=\'string\',
              AssociationStatus={
                  \'Date\': datetime(2015, 1, 1),
                  \'Name\': \'Pending\'|\'Success\'|\'Failed\',
                  \'Message\': \'string\',
                  \'AdditionalInfo\': \'string\'
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the Systems Manager document.
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The ID of the instance.
        
        :type AssociationStatus: dict
        :param AssociationStatus: **[REQUIRED]** 
        
          The association status.
        
          - **Date** *(datetime) --* **[REQUIRED]** 
        
            The date when the status changed.
        
          - **Name** *(string) --* **[REQUIRED]** 
        
            The status.
        
          - **Message** *(string) --* **[REQUIRED]** 
        
            The reason for the status.
        
          - **AdditionalInfo** *(string) --* 
        
            A user-defined string.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AssociationDescription\': {
                    \'Name\': \'string\',
                    \'InstanceId\': \'string\',
                    \'AssociationVersion\': \'string\',
                    \'Date\': datetime(2015, 1, 1),
                    \'LastUpdateAssociationDate\': datetime(2015, 1, 1),
                    \'Status\': {
                        \'Date\': datetime(2015, 1, 1),
                        \'Name\': \'Pending\'|\'Success\'|\'Failed\',
                        \'Message\': \'string\',
                        \'AdditionalInfo\': \'string\'
                    },
                    \'Overview\': {
                        \'Status\': \'string\',
                        \'DetailedStatus\': \'string\',
                        \'AssociationStatusAggregatedCount\': {
                            \'string\': 123
                        }
                    },
                    \'DocumentVersion\': \'string\',
                    \'Parameters\': {
                        \'string\': [
                            \'string\',
                        ]
                    },
                    \'AssociationId\': \'string\',
                    \'Targets\': [
                        {
                            \'Key\': \'string\',
                            \'Values\': [
                                \'string\',
                            ]
                        },
                    ],
                    \'ScheduleExpression\': \'string\',
                    \'OutputLocation\': {
                        \'S3Location\': {
                            \'OutputS3Region\': \'string\',
                            \'OutputS3BucketName\': \'string\',
                            \'OutputS3KeyPrefix\': \'string\'
                        }
                    },
                    \'LastExecutionDate\': datetime(2015, 1, 1),
                    \'LastSuccessfulExecutionDate\': datetime(2015, 1, 1),
                    \'AssociationName\': \'string\',
                    \'MaxErrors\': \'string\',
                    \'MaxConcurrency\': \'string\',
                    \'ComplianceSeverity\': \'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'UNSPECIFIED\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AssociationDescription** *(dict) --* 
        
              Information about the association.
        
              - **Name** *(string) --* 
        
                The name of the Systems Manager document.
        
              - **InstanceId** *(string) --* 
        
                The ID of the instance.
        
              - **AssociationVersion** *(string) --* 
        
                The association version.
        
              - **Date** *(datetime) --* 
        
                The date when the association was made.
        
              - **LastUpdateAssociationDate** *(datetime) --* 
        
                The date when the association was last updated.
        
              - **Status** *(dict) --* 
        
                The association status.
        
                - **Date** *(datetime) --* 
        
                  The date when the status changed.
        
                - **Name** *(string) --* 
        
                  The status.
        
                - **Message** *(string) --* 
        
                  The reason for the status.
        
                - **AdditionalInfo** *(string) --* 
        
                  A user-defined string.
        
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
              
              - **DocumentVersion** *(string) --* 
        
                The document version.
        
              - **Parameters** *(dict) --* 
        
                A description of the parameters for a document. 
        
                - *(string) --* 
                  
                  - *(list) --* 
                    
                    - *(string) --* 
                
              - **AssociationId** *(string) --* 
        
                The association ID.
        
              - **Targets** *(list) --* 
        
                The instances targeted by the request. 
        
                - *(dict) --* 
        
                  An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                  - **Key** *(string) --* 
        
                    User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                  - **Values** *(list) --* 
        
                    User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
                    - *(string) --* 
                
              - **ScheduleExpression** *(string) --* 
        
                A cron expression that specifies a schedule when the association runs.
        
              - **OutputLocation** *(dict) --* 
        
                An Amazon S3 bucket where you want to store the output details of the request.
        
                - **S3Location** *(dict) --* 
        
                  An Amazon S3 bucket where you want to store the results of this request.
        
                  - **OutputS3Region** *(string) --* 
        
                    (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
        
                  - **OutputS3BucketName** *(string) --* 
        
                    The name of the Amazon S3 bucket.
        
                  - **OutputS3KeyPrefix** *(string) --* 
        
                    The Amazon S3 bucket subfolder.
        
              - **LastExecutionDate** *(datetime) --* 
        
                The date on which the association was last run.
        
              - **LastSuccessfulExecutionDate** *(datetime) --* 
        
                The last date on which the association was successfully run.
        
              - **AssociationName** *(string) --* 
        
                The association name.
        
              - **MaxErrors** *(string) --* 
        
                The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.
        
                Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.
        
              - **MaxConcurrency** *(string) --* 
        
                The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
        
                If a new instance starts and attempts to execute an association while Systems Manager is executing MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.
        
              - **ComplianceSeverity** *(string) --* 
        
                The severity level that is assigned to the association.
        
        """
        pass

    def update_document(self, Content: str, Name: str, DocumentVersion: str = None, DocumentFormat: str = None, TargetType: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateDocument>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_document(
              Content=\'string\',
              Name=\'string\',
              DocumentVersion=\'string\',
              DocumentFormat=\'YAML\'|\'JSON\',
              TargetType=\'string\'
          )
        :type Content: string
        :param Content: **[REQUIRED]** 
        
          The content in a document that you want to update.
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the document that you want to update.
        
        :type DocumentVersion: string
        :param DocumentVersion: 
        
          The version of the document that you want to update.
        
        :type DocumentFormat: string
        :param DocumentFormat: 
        
          Specify the document format for the new document version. Systems Manager supports JSON and YAML documents. JSON is the default format.
        
        :type TargetType: string
        :param TargetType: 
        
          Specify a new target type for the document.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DocumentDescription\': {
                    \'Sha1\': \'string\',
                    \'Hash\': \'string\',
                    \'HashType\': \'Sha256\'|\'Sha1\',
                    \'Name\': \'string\',
                    \'Owner\': \'string\',
                    \'CreatedDate\': datetime(2015, 1, 1),
                    \'Status\': \'Creating\'|\'Active\'|\'Updating\'|\'Deleting\',
                    \'DocumentVersion\': \'string\',
                    \'Description\': \'string\',
                    \'Parameters\': [
                        {
                            \'Name\': \'string\',
                            \'Type\': \'String\'|\'StringList\',
                            \'Description\': \'string\',
                            \'DefaultValue\': \'string\'
                        },
                    ],
                    \'PlatformTypes\': [
                        \'Windows\'|\'Linux\',
                    ],
                    \'DocumentType\': \'Command\'|\'Policy\'|\'Automation\'|\'Session\',
                    \'SchemaVersion\': \'string\',
                    \'LatestVersion\': \'string\',
                    \'DefaultVersion\': \'string\',
                    \'DocumentFormat\': \'YAML\'|\'JSON\',
                    \'TargetType\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DocumentDescription** *(dict) --* 
        
              A description of the document that was updated.
        
              - **Sha1** *(string) --* 
        
                The SHA1 hash of the document, which you can use for verification.
        
              - **Hash** *(string) --* 
        
                The Sha256 or Sha1 hash created by the system when the document was created. 
        
                .. note::
        
                  Sha1 hashes have been deprecated.
        
              - **HashType** *(string) --* 
        
                Sha256 or Sha1.
        
                .. note::
        
                  Sha1 hashes have been deprecated.
        
              - **Name** *(string) --* 
        
                The name of the Systems Manager document.
        
              - **Owner** *(string) --* 
        
                The AWS user account that created the document.
        
              - **CreatedDate** *(datetime) --* 
        
                The date when the document was created.
        
              - **Status** *(string) --* 
        
                The status of the Systems Manager document.
        
              - **DocumentVersion** *(string) --* 
        
                The document version.
        
              - **Description** *(string) --* 
        
                A description of the document. 
        
              - **Parameters** *(list) --* 
        
                A description of the parameters for a document.
        
                - *(dict) --* 
        
                  Parameters specified in a System Manager document that execute on the server when the command is run. 
        
                  - **Name** *(string) --* 
        
                    The name of the parameter.
        
                  - **Type** *(string) --* 
        
                    The type of parameter. The type can be either String or StringList.
        
                  - **Description** *(string) --* 
        
                    A description of what the parameter does, how to use it, the default value, and whether or not the parameter is optional.
        
                  - **DefaultValue** *(string) --* 
        
                    If specified, the default values for the parameters. Parameters without a default value are required. Parameters with a default value are optional.
        
              - **PlatformTypes** *(list) --* 
        
                The list of OS platforms compatible with this Systems Manager document. 
        
                - *(string) --* 
            
              - **DocumentType** *(string) --* 
        
                The type of document. 
        
              - **SchemaVersion** *(string) --* 
        
                The schema version.
        
              - **LatestVersion** *(string) --* 
        
                The latest version of the document.
        
              - **DefaultVersion** *(string) --* 
        
                The default version.
        
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
        
        """
        pass

    def update_document_default_version(self, Name: str, DocumentVersion: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateDocumentDefaultVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_document_default_version(
              Name=\'string\',
              DocumentVersion=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of a custom document that you want to set as the default version.
        
        :type DocumentVersion: string
        :param DocumentVersion: **[REQUIRED]** 
        
          The version of a custom document that you want to set as the default version.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Description\': {
                    \'Name\': \'string\',
                    \'DefaultVersion\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Description** *(dict) --* 
        
              The description of a custom document that you want to set as the default version.
        
              - **Name** *(string) --* 
        
                The name of the document.
        
              - **DefaultVersion** *(string) --* 
        
                The default version of the document.
        
        """
        pass

    def update_maintenance_window(self, WindowId: str, Name: str = None, Description: str = None, StartDate: str = None, EndDate: str = None, Schedule: str = None, ScheduleTimezone: str = None, Duration: int = None, Cutoff: int = None, AllowUnassociatedTargets: bool = None, Enabled: bool = None, Replace: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateMaintenanceWindow>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_maintenance_window(
              WindowId=\'string\',
              Name=\'string\',
              Description=\'string\',
              StartDate=\'string\',
              EndDate=\'string\',
              Schedule=\'string\',
              ScheduleTimezone=\'string\',
              Duration=123,
              Cutoff=123,
              AllowUnassociatedTargets=True|False,
              Enabled=True|False,
              Replace=True|False
          )
        :type WindowId: string
        :param WindowId: **[REQUIRED]** 
        
          The ID of the Maintenance Window to update.
        
        :type Name: string
        :param Name: 
        
          The name of the Maintenance Window.
        
        :type Description: string
        :param Description: 
        
          An optional description for the update request.
        
        :type StartDate: string
        :param StartDate: 
        
          The time zone that the scheduled Maintenance Window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: \"America/Los_Angeles\", \"etc/UTC\", or \"Asia/Seoul\". For more information, see the `Time Zone Database <https://www.iana.org/time-zones>`__ on the IANA website.
        
        :type EndDate: string
        :param EndDate: 
        
          The date and time, in ISO-8601 Extended format, for when you want the Maintenance Window to become inactive. EndDate allows you to set a date and time in the future when the Maintenance Window will no longer run.
        
        :type Schedule: string
        :param Schedule: 
        
          The schedule of the Maintenance Window in the form of a cron or rate expression.
        
        :type ScheduleTimezone: string
        :param ScheduleTimezone: 
        
          The time zone that the scheduled Maintenance Window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: \"America/Los_Angeles\", \"etc/UTC\", or \"Asia/Seoul\". For more information, see the `Time Zone Database <https://www.iana.org/time-zones>`__ on the IANA website.
        
        :type Duration: integer
        :param Duration: 
        
          The duration of the Maintenance Window in hours.
        
        :type Cutoff: integer
        :param Cutoff: 
        
          The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.
        
        :type AllowUnassociatedTargets: boolean
        :param AllowUnassociatedTargets: 
        
          Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.
        
        :type Enabled: boolean
        :param Enabled: 
        
          Whether the Maintenance Window is enabled.
        
        :type Replace: boolean
        :param Replace: 
        
          If True, then all fields that are required by the CreateMaintenanceWindow action are also required for this API request. Optional fields that are not specified are set to null. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowId\': \'string\',
                \'Name\': \'string\',
                \'Description\': \'string\',
                \'StartDate\': \'string\',
                \'EndDate\': \'string\',
                \'Schedule\': \'string\',
                \'ScheduleTimezone\': \'string\',
                \'Duration\': 123,
                \'Cutoff\': 123,
                \'AllowUnassociatedTargets\': True|False,
                \'Enabled\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **WindowId** *(string) --* 
        
              The ID of the created Maintenance Window.
        
            - **Name** *(string) --* 
        
              The name of the Maintenance Window.
        
            - **Description** *(string) --* 
        
              An optional description of the update.
        
            - **StartDate** *(string) --* 
        
              The date and time, in ISO-8601 Extended format, for when the Maintenance Window is scheduled to become active. The Maintenance Window will not run before this specified time.
        
            - **EndDate** *(string) --* 
        
              The date and time, in ISO-8601 Extended format, for when the Maintenance Window is scheduled to become inactive. The Maintenance Window will not run after this specified time.
        
            - **Schedule** *(string) --* 
        
              The schedule of the Maintenance Window in the form of a cron or rate expression.
        
            - **ScheduleTimezone** *(string) --* 
        
              The time zone that the scheduled Maintenance Window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: \"America/Los_Angeles\", \"etc/UTC\", or \"Asia/Seoul\". For more information, see the `Time Zone Database <https://www.iana.org/time-zones>`__ on the IANA website.
        
            - **Duration** *(integer) --* 
        
              The duration of the Maintenance Window in hours.
        
            - **Cutoff** *(integer) --* 
        
              The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.
        
            - **AllowUnassociatedTargets** *(boolean) --* 
        
              Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.
        
            - **Enabled** *(boolean) --* 
        
              Whether the Maintenance Window is enabled.
        
        """
        pass

    def update_maintenance_window_target(self, WindowId: str, WindowTargetId: str, Targets: List = None, OwnerInformation: str = None, Name: str = None, Description: str = None, Replace: bool = None) -> Dict:
        """
        Modifies the target of an existing Maintenance Window. You can\'t change the target type, but you can change the following:
        
        The target from being an ID target to a Tag target, or a Tag target to an ID target.
        
        IDs for an ID target.
        
        Tags for a Tag target.
        
        Owner.
        
        Name.
        
        Description.
        
        If a parameter is null, then the corresponding field is not modified.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateMaintenanceWindowTarget>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_maintenance_window_target(
              WindowId=\'string\',
              WindowTargetId=\'string\',
              Targets=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              OwnerInformation=\'string\',
              Name=\'string\',
              Description=\'string\',
              Replace=True|False
          )
        :type WindowId: string
        :param WindowId: **[REQUIRED]** 
        
          The Maintenance Window ID with which to modify the target.
        
        :type WindowTargetId: string
        :param WindowTargetId: **[REQUIRED]** 
        
          The target ID to modify.
        
        :type Targets: list
        :param Targets: 
        
          The targets to add or replace.
        
          - *(dict) --* 
        
            An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
            - **Key** *(string) --* 
        
              User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
            - **Values** *(list) --* 
        
              User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
              - *(string) --* 
        
        :type OwnerInformation: string
        :param OwnerInformation: 
        
          User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
        
        :type Name: string
        :param Name: 
        
          A name for the update.
        
        :type Description: string
        :param Description: 
        
          An optional description for the update.
        
        :type Replace: boolean
        :param Replace: 
        
          If True, then all fields that are required by the RegisterTargetWithMaintenanceWindow action are also required for this API request. Optional fields that are not specified are set to null.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowId\': \'string\',
                \'WindowTargetId\': \'string\',
                \'Targets\': [
                    {
                        \'Key\': \'string\',
                        \'Values\': [
                            \'string\',
                        ]
                    },
                ],
                \'OwnerInformation\': \'string\',
                \'Name\': \'string\',
                \'Description\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **WindowId** *(string) --* 
        
              The Maintenance Window ID specified in the update request.
        
            - **WindowTargetId** *(string) --* 
        
              The target ID specified in the update request.
        
            - **Targets** *(list) --* 
        
              The updated targets.
        
              - *(dict) --* 
        
                An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                - **Key** *(string) --* 
        
                  User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                - **Values** *(list) --* 
        
                  User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
                  - *(string) --* 
              
            - **OwnerInformation** *(string) --* 
        
              The updated owner.
        
            - **Name** *(string) --* 
        
              The updated name.
        
            - **Description** *(string) --* 
        
              The updated description.
        
        """
        pass

    def update_maintenance_window_task(self, WindowId: str, WindowTaskId: str, Targets: List = None, TaskArn: str = None, ServiceRoleArn: str = None, TaskParameters: Dict = None, TaskInvocationParameters: Dict = None, Priority: int = None, MaxConcurrency: str = None, MaxErrors: str = None, LoggingInfo: Dict = None, Name: str = None, Description: str = None, Replace: bool = None) -> Dict:
        """
        Modifies a task assigned to a Maintenance Window. You can\'t change the task type, but you can change the following values:
        
        * TaskARN. For example, you can change a RUN_COMMAND task from AWS-RunPowerShellScript to AWS-RunShellScript. 
         
        * ServiceRoleArn 
         
        * TaskInvocationParameters 
         
        * Priority 
         
        * MaxConcurrency 
         
        * MaxErrors 
         
        If a parameter is null, then the corresponding field is not modified. Also, if you set Replace to true, then all fields required by the  RegisterTaskWithMaintenanceWindow action are required for this request. Optional fields that aren\'t specified are set to null.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateMaintenanceWindowTask>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_maintenance_window_task(
              WindowId=\'string\',
              WindowTaskId=\'string\',
              Targets=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              TaskArn=\'string\',
              ServiceRoleArn=\'string\',
              TaskParameters={
                  \'string\': {
                      \'Values\': [
                          \'string\',
                      ]
                  }
              },
              TaskInvocationParameters={
                  \'RunCommand\': {
                      \'Comment\': \'string\',
                      \'DocumentHash\': \'string\',
                      \'DocumentHashType\': \'Sha256\'|\'Sha1\',
                      \'NotificationConfig\': {
                          \'NotificationArn\': \'string\',
                          \'NotificationEvents\': [
                              \'All\'|\'InProgress\'|\'Success\'|\'TimedOut\'|\'Cancelled\'|\'Failed\',
                          ],
                          \'NotificationType\': \'Command\'|\'Invocation\'
                      },
                      \'OutputS3BucketName\': \'string\',
                      \'OutputS3KeyPrefix\': \'string\',
                      \'Parameters\': {
                          \'string\': [
                              \'string\',
                          ]
                      },
                      \'ServiceRoleArn\': \'string\',
                      \'TimeoutSeconds\': 123
                  },
                  \'Automation\': {
                      \'DocumentVersion\': \'string\',
                      \'Parameters\': {
                          \'string\': [
                              \'string\',
                          ]
                      }
                  },
                  \'StepFunctions\': {
                      \'Input\': \'string\',
                      \'Name\': \'string\'
                  },
                  \'Lambda\': {
                      \'ClientContext\': \'string\',
                      \'Qualifier\': \'string\',
                      \'Payload\': b\'bytes\'
                  }
              },
              Priority=123,
              MaxConcurrency=\'string\',
              MaxErrors=\'string\',
              LoggingInfo={
                  \'S3BucketName\': \'string\',
                  \'S3KeyPrefix\': \'string\',
                  \'S3Region\': \'string\'
              },
              Name=\'string\',
              Description=\'string\',
              Replace=True|False
          )
        :type WindowId: string
        :param WindowId: **[REQUIRED]** 
        
          The Maintenance Window ID that contains the task to modify.
        
        :type WindowTaskId: string
        :param WindowTaskId: **[REQUIRED]** 
        
          The task ID to modify.
        
        :type Targets: list
        :param Targets: 
        
          The targets (either instances or tags) to modify. Instances are specified using Key=instanceids,Values=instanceID_1,instanceID_2. Tags are specified using Key=tag_name,Values=tag_value. 
        
          - *(dict) --* 
        
            An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
            - **Key** *(string) --* 
        
              User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
            - **Values** *(list) --* 
        
              User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
              - *(string) --* 
        
        :type TaskArn: string
        :param TaskArn: 
        
          The task ARN to modify.
        
        :type ServiceRoleArn: string
        :param ServiceRoleArn: 
        
          The IAM service role ARN to modify. The system assumes this role during task execution.
        
          If you do not specify a service role ARN, Systems Manager will use your account\'s service-linked role for Systems Manager by default. If no service-linked role for Systems Manager exists in your account, it will be created when you run ``RegisterTaskWithMaintenanceWindow`` without specifying a service role ARN.
        
          For more information, see `Service-Linked Role Permissions for Systems Manager <http://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles.html#slr-permissions>`__ and `Should I Use a Service-Linked Role or a Custom Service Role to Run Maintenance Window Tasks? <http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html#maintenance-window-tasks-service-role>`__ in the *AWS Systems Manager User Guide* .
        
        :type TaskParameters: dict
        :param TaskParameters: 
        
          The parameters to modify.
        
          .. note::
        
             ``TaskParameters`` has been deprecated. To specify parameters to pass to a task when it runs, instead use the ``Parameters`` option in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
        
          The map has the following format:
        
          Key: string, between 1 and 255 characters
        
          Value: an array of strings, each string is between 1 and 255 characters
        
          - *(string) --* 
        
            - *(dict) --* 
        
              Defines the values for a task parameter.
        
              - **Values** *(list) --* 
        
                This field contains an array of 0 or more strings, each 1 to 255 characters in length.
        
                - *(string) --* 
        
        :type TaskInvocationParameters: dict
        :param TaskInvocationParameters: 
        
          The parameters that the task should use during execution. Populate only the fields that match the task type. All other fields should be empty.
        
          - **RunCommand** *(dict) --* 
        
            The parameters for a RUN_COMMAND task type.
        
            - **Comment** *(string) --* 
        
              Information about the command(s) to execute.
        
            - **DocumentHash** *(string) --* 
        
              The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.
        
            - **DocumentHashType** *(string) --* 
        
              SHA-256 or SHA-1. SHA-1 hashes have been deprecated.
        
            - **NotificationConfig** *(dict) --* 
        
              Configurations for sending notifications about command status changes on a per-instance basis.
        
              - **NotificationArn** *(string) --* 
        
                An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.
        
              - **NotificationEvents** *(list) --* 
        
                The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Configuring Amazon SNS Notifications for Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/rc-sns-notifications.html>`__ in the *AWS Systems Manager User Guide* .
        
                - *(string) --* 
        
              - **NotificationType** *(string) --* 
        
                Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 
        
            - **OutputS3BucketName** *(string) --* 
        
              The name of the Amazon S3 bucket.
        
            - **OutputS3KeyPrefix** *(string) --* 
        
              The Amazon S3 bucket subfolder.
        
            - **Parameters** *(dict) --* 
        
              The parameters for the RUN_COMMAND task execution.
        
              - *(string) --* 
        
                - *(list) --* 
        
                  - *(string) --* 
        
            - **ServiceRoleArn** *(string) --* 
        
              The IAM service role to assume during task execution.
        
            - **TimeoutSeconds** *(integer) --* 
        
              If this time is reached and the command has not already started executing, it doesn not execute.
        
          - **Automation** *(dict) --* 
        
            The parameters for an AUTOMATION task type.
        
            - **DocumentVersion** *(string) --* 
        
              The version of an Automation document to use during task execution.
        
            - **Parameters** *(dict) --* 
        
              The parameters for the AUTOMATION task.
        
              For information about specifying and updating task parameters, see  RegisterTaskWithMaintenanceWindow and  UpdateMaintenanceWindowTask .
        
              .. note::
        
                 ``LoggingInfo`` has been deprecated. To specify an S3 bucket to contain logs, instead use the ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
        
                 ``TaskParameters`` has been deprecated. To specify parameters to pass to a task when it runs, instead use the ``Parameters`` option in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
        
                For AUTOMATION task types, Systems Manager ignores any values specified for these parameters.
        
              - *(string) --* 
        
                - *(list) --* 
        
                  - *(string) --* 
        
          - **StepFunctions** *(dict) --* 
        
            The parameters for a STEP_FUNCTION task type.
        
            - **Input** *(string) --* 
        
              The inputs for the STEP_FUNCTION task.
        
            - **Name** *(string) --* 
        
              The name of the STEP_FUNCTION task.
        
          - **Lambda** *(dict) --* 
        
            The parameters for a LAMBDA task type.
        
            - **ClientContext** *(string) --* 
        
              Pass client-specific information to the Lambda function that you are invoking. You can then process the client information in your Lambda function as you choose through the context variable.
        
            - **Qualifier** *(string) --* 
        
              (Optional) Specify a Lambda function version or alias name. If you specify a function version, the action uses the qualified function ARN to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version to which the alias points.
        
            - **Payload** *(bytes) --* 
        
              JSON to provide to your Lambda function as input.
        
        :type Priority: integer
        :param Priority: 
        
          The new task priority to specify. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.
        
        :type MaxConcurrency: string
        :param MaxConcurrency: 
        
          The new ``MaxConcurrency`` value you want to specify. ``MaxConcurrency`` is the number of targets that are allowed to run this task in parallel.
        
        :type MaxErrors: string
        :param MaxErrors: 
        
          The new ``MaxErrors`` value to specify. ``MaxErrors`` is the maximum number of errors that are allowed before the task stops being scheduled.
        
        :type LoggingInfo: dict
        :param LoggingInfo: 
        
          The new logging location in Amazon S3 to specify.
        
          .. note::
        
             ``LoggingInfo`` has been deprecated. To specify an S3 bucket to contain logs, instead use the ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
        
          - **S3BucketName** *(string) --* **[REQUIRED]** 
        
            The name of an Amazon S3 bucket where execution logs are stored .
        
          - **S3KeyPrefix** *(string) --* 
        
            (Optional) The Amazon S3 bucket subfolder. 
        
          - **S3Region** *(string) --* **[REQUIRED]** 
        
            The region where the Amazon S3 bucket is located.
        
        :type Name: string
        :param Name: 
        
          The new task name to specify.
        
        :type Description: string
        :param Description: 
        
          The new task description to specify.
        
        :type Replace: boolean
        :param Replace: 
        
          If True, then all fields that are required by the RegisterTaskWithMaintenanceWndow action are also required for this API request. Optional fields that are not specified are set to null.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WindowId\': \'string\',
                \'WindowTaskId\': \'string\',
                \'Targets\': [
                    {
                        \'Key\': \'string\',
                        \'Values\': [
                            \'string\',
                        ]
                    },
                ],
                \'TaskArn\': \'string\',
                \'ServiceRoleArn\': \'string\',
                \'TaskParameters\': {
                    \'string\': {
                        \'Values\': [
                            \'string\',
                        ]
                    }
                },
                \'TaskInvocationParameters\': {
                    \'RunCommand\': {
                        \'Comment\': \'string\',
                        \'DocumentHash\': \'string\',
                        \'DocumentHashType\': \'Sha256\'|\'Sha1\',
                        \'NotificationConfig\': {
                            \'NotificationArn\': \'string\',
                            \'NotificationEvents\': [
                                \'All\'|\'InProgress\'|\'Success\'|\'TimedOut\'|\'Cancelled\'|\'Failed\',
                            ],
                            \'NotificationType\': \'Command\'|\'Invocation\'
                        },
                        \'OutputS3BucketName\': \'string\',
                        \'OutputS3KeyPrefix\': \'string\',
                        \'Parameters\': {
                            \'string\': [
                                \'string\',
                            ]
                        },
                        \'ServiceRoleArn\': \'string\',
                        \'TimeoutSeconds\': 123
                    },
                    \'Automation\': {
                        \'DocumentVersion\': \'string\',
                        \'Parameters\': {
                            \'string\': [
                                \'string\',
                            ]
                        }
                    },
                    \'StepFunctions\': {
                        \'Input\': \'string\',
                        \'Name\': \'string\'
                    },
                    \'Lambda\': {
                        \'ClientContext\': \'string\',
                        \'Qualifier\': \'string\',
                        \'Payload\': b\'bytes\'
                    }
                },
                \'Priority\': 123,
                \'MaxConcurrency\': \'string\',
                \'MaxErrors\': \'string\',
                \'LoggingInfo\': {
                    \'S3BucketName\': \'string\',
                    \'S3KeyPrefix\': \'string\',
                    \'S3Region\': \'string\'
                },
                \'Name\': \'string\',
                \'Description\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **WindowId** *(string) --* 
        
              The ID of the Maintenance Window that was updated.
        
            - **WindowTaskId** *(string) --* 
        
              The task ID of the Maintenance Window that was updated.
        
            - **Targets** *(list) --* 
        
              The updated target values.
        
              - *(dict) --* 
        
                An array of search criteria that targets instances using a Key,Value combination that you specify. ``Targets`` is required if you don\'t provide one or more instance IDs in the call.
        
                - **Key** *(string) --* 
        
                  User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:<Amazon EC2 tag> or InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see `Targeting Multiple Instances <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting>`__ in the *AWS Systems Manager User Guide* .
        
                - **Values** *(list) --* 
        
                  User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see `Sending Commands to a Fleet <http://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html>`__ in the *AWS Systems Manager User Guide* .
        
                  - *(string) --* 
              
            - **TaskArn** *(string) --* 
        
              The updated task ARN value.
        
            - **ServiceRoleArn** *(string) --* 
        
              The updated service role ARN value.
        
            - **TaskParameters** *(dict) --* 
        
              The updated parameter values.
        
              .. note::
        
                 ``TaskParameters`` has been deprecated. To specify parameters to pass to a task when it runs, instead use the ``Parameters`` option in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
        
              - *(string) --* 
                
                - *(dict) --* 
        
                  Defines the values for a task parameter.
        
                  - **Values** *(list) --* 
        
                    This field contains an array of 0 or more strings, each 1 to 255 characters in length.
        
                    - *(string) --* 
                
            - **TaskInvocationParameters** *(dict) --* 
        
              The updated parameter values.
        
              - **RunCommand** *(dict) --* 
        
                The parameters for a RUN_COMMAND task type.
        
                - **Comment** *(string) --* 
        
                  Information about the command(s) to execute.
        
                - **DocumentHash** *(string) --* 
        
                  The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.
        
                - **DocumentHashType** *(string) --* 
        
                  SHA-256 or SHA-1. SHA-1 hashes have been deprecated.
        
                - **NotificationConfig** *(dict) --* 
        
                  Configurations for sending notifications about command status changes on a per-instance basis.
        
                  - **NotificationArn** *(string) --* 
        
                    An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.
        
                  - **NotificationEvents** *(list) --* 
        
                    The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see `Configuring Amazon SNS Notifications for Run Command <http://docs.aws.amazon.com/systems-manager/latest/userguide/rc-sns-notifications.html>`__ in the *AWS Systems Manager User Guide* .
        
                    - *(string) --* 
                
                  - **NotificationType** *(string) --* 
        
                    Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. 
        
                - **OutputS3BucketName** *(string) --* 
        
                  The name of the Amazon S3 bucket.
        
                - **OutputS3KeyPrefix** *(string) --* 
        
                  The Amazon S3 bucket subfolder.
        
                - **Parameters** *(dict) --* 
        
                  The parameters for the RUN_COMMAND task execution.
        
                  - *(string) --* 
                    
                    - *(list) --* 
                      
                      - *(string) --* 
                  
                - **ServiceRoleArn** *(string) --* 
        
                  The IAM service role to assume during task execution.
        
                - **TimeoutSeconds** *(integer) --* 
        
                  If this time is reached and the command has not already started executing, it doesn not execute.
        
              - **Automation** *(dict) --* 
        
                The parameters for an AUTOMATION task type.
        
                - **DocumentVersion** *(string) --* 
        
                  The version of an Automation document to use during task execution.
        
                - **Parameters** *(dict) --* 
        
                  The parameters for the AUTOMATION task.
        
                  For information about specifying and updating task parameters, see  RegisterTaskWithMaintenanceWindow and  UpdateMaintenanceWindowTask .
        
                  .. note::
        
                     ``LoggingInfo`` has been deprecated. To specify an S3 bucket to contain logs, instead use the ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
        
                     ``TaskParameters`` has been deprecated. To specify parameters to pass to a task when it runs, instead use the ``Parameters`` option in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
        
                    For AUTOMATION task types, Systems Manager ignores any values specified for these parameters.
        
                  - *(string) --* 
                    
                    - *(list) --* 
                      
                      - *(string) --* 
                  
              - **StepFunctions** *(dict) --* 
        
                The parameters for a STEP_FUNCTION task type.
        
                - **Input** *(string) --* 
        
                  The inputs for the STEP_FUNCTION task.
        
                - **Name** *(string) --* 
        
                  The name of the STEP_FUNCTION task.
        
              - **Lambda** *(dict) --* 
        
                The parameters for a LAMBDA task type.
        
                - **ClientContext** *(string) --* 
        
                  Pass client-specific information to the Lambda function that you are invoking. You can then process the client information in your Lambda function as you choose through the context variable.
        
                - **Qualifier** *(string) --* 
        
                  (Optional) Specify a Lambda function version or alias name. If you specify a function version, the action uses the qualified function ARN to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version to which the alias points.
        
                - **Payload** *(bytes) --* 
        
                  JSON to provide to your Lambda function as input.
        
            - **Priority** *(integer) --* 
        
              The updated priority value.
        
            - **MaxConcurrency** *(string) --* 
        
              The updated MaxConcurrency value.
        
            - **MaxErrors** *(string) --* 
        
              The updated MaxErrors value.
        
            - **LoggingInfo** *(dict) --* 
        
              The updated logging information in Amazon S3.
        
              .. note::
        
                 ``LoggingInfo`` has been deprecated. To specify an S3 bucket to contain logs, instead use the ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported Maintenance Window task types, see  MaintenanceWindowTaskInvocationParameters .
        
              - **S3BucketName** *(string) --* 
        
                The name of an Amazon S3 bucket where execution logs are stored .
        
              - **S3KeyPrefix** *(string) --* 
        
                (Optional) The Amazon S3 bucket subfolder. 
        
              - **S3Region** *(string) --* 
        
                The region where the Amazon S3 bucket is located.
        
            - **Name** *(string) --* 
        
              The updated task name.
        
            - **Description** *(string) --* 
        
              The updated task description.
        
        """
        pass

    def update_managed_instance_role(self, InstanceId: str, IamRole: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateManagedInstanceRole>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_managed_instance_role(
              InstanceId=\'string\',
              IamRole=\'string\'
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The ID of the managed instance where you want to update the role.
        
        :type IamRole: string
        :param IamRole: **[REQUIRED]** 
        
          The IAM role you want to assign or change.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_patch_baseline(self, BaselineId: str, Name: str = None, GlobalFilters: Dict = None, ApprovalRules: Dict = None, ApprovedPatches: List = None, ApprovedPatchesComplianceLevel: str = None, ApprovedPatchesEnableNonSecurity: bool = None, RejectedPatches: List = None, RejectedPatchesAction: str = None, Description: str = None, Sources: List = None, Replace: bool = None) -> Dict:
        """
        
        .. note::
        
          For information about valid key and value pairs in ``PatchFilters`` for each supported operating system type, see `PatchFilter <http://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdatePatchBaseline>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_patch_baseline(
              BaselineId=\'string\',
              Name=\'string\',
              GlobalFilters={
                  \'PatchFilters\': [
                      {
                          \'Key\': \'PRODUCT\'|\'CLASSIFICATION\'|\'MSRC_SEVERITY\'|\'PATCH_ID\'|\'SECTION\'|\'PRIORITY\'|\'SEVERITY\',
                          \'Values\': [
                              \'string\',
                          ]
                      },
                  ]
              },
              ApprovalRules={
                  \'PatchRules\': [
                      {
                          \'PatchFilterGroup\': {
                              \'PatchFilters\': [
                                  {
                                      \'Key\': \'PRODUCT\'|\'CLASSIFICATION\'|\'MSRC_SEVERITY\'|\'PATCH_ID\'|\'SECTION\'|\'PRIORITY\'|\'SEVERITY\',
                                      \'Values\': [
                                          \'string\',
                                      ]
                                  },
                              ]
                          },
                          \'ComplianceLevel\': \'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'INFORMATIONAL\'|\'UNSPECIFIED\',
                          \'ApproveAfterDays\': 123,
                          \'EnableNonSecurity\': True|False
                      },
                  ]
              },
              ApprovedPatches=[
                  \'string\',
              ],
              ApprovedPatchesComplianceLevel=\'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'INFORMATIONAL\'|\'UNSPECIFIED\',
              ApprovedPatchesEnableNonSecurity=True|False,
              RejectedPatches=[
                  \'string\',
              ],
              RejectedPatchesAction=\'ALLOW_AS_DEPENDENCY\'|\'BLOCK\',
              Description=\'string\',
              Sources=[
                  {
                      \'Name\': \'string\',
                      \'Products\': [
                          \'string\',
                      ],
                      \'Configuration\': \'string\'
                  },
              ],
              Replace=True|False
          )
        :type BaselineId: string
        :param BaselineId: **[REQUIRED]** 
        
          The ID of the patch baseline to update.
        
        :type Name: string
        :param Name: 
        
          The name of the patch baseline.
        
        :type GlobalFilters: dict
        :param GlobalFilters: 
        
          A set of global filters used to exclude patches from the baseline.
        
          - **PatchFilters** *(list) --* **[REQUIRED]** 
        
            The set of patch filters that make up the group.
        
            - *(dict) --* 
        
              Defines a patch filter.
        
              A patch filter consists of key/value pairs, but not all keys are valid for all operating system types. For example, the key ``PRODUCT`` is valid for all supported operating system types. The key ``MSRC_SEVERITY`` , however, is valid only for Windows operating systems, and the key ``SECTION`` is valid only for Ubuntu operating systems.
        
              Refer to the following sections for information about which keys may be used with each major operating system, and which values are valid for each key.
        
               **Windows Operating Systems**  
        
              The supported keys for Windows operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``MSRC_SEVERITY`` . See the following lists for valid values for each of these keys.
        
               *Supported key:*  ``PRODUCT``  
        
               *Supported values:*  
        
              * ``Windows7``   
               
              * ``Windows8``   
               
              * ``Windows8.1``   
               
              * ``Windows8Embedded``   
               
              * ``Windows10``   
               
              * ``Windows10LTSB``   
               
              * ``WindowsServer2008``   
               
              * ``WindowsServer2008R2``   
               
              * ``WindowsServer2012``   
               
              * ``WindowsServer2012R2``   
               
              * ``WindowsServer2016``   
               
              * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
               
               *Supported key:*  ``CLASSIFICATION``  
        
               *Supported values:*  
        
              * ``CriticalUpdates``   
               
              * ``DefinitionUpdates``   
               
              * ``Drivers``   
               
              * ``FeaturePacks``   
               
              * ``SecurityUpdates``   
               
              * ``ServicePacks``   
               
              * ``Tools``   
               
              * ``UpdateRollups``   
               
              * ``Updates``   
               
              * ``Upgrades``   
               
               *Supported key:*  ``MSRC_SEVERITY``  
        
               *Supported values:*  
        
              * ``Critical``   
               
              * ``Important``   
               
              * ``Moderate``   
               
              * ``Low``   
               
              * ``Unspecified``   
               
               **Ubuntu Operating Systems**  
        
              The supported keys for Ubuntu operating systems are ``PRODUCT`` , ``PRIORITY`` , and ``SECTION`` . See the following lists for valid values for each of these keys.
        
               *Supported key:*  ``PRODUCT``  
        
               *Supported values:*  
        
              * ``Ubuntu14.04``   
               
              * ``Ubuntu16.04``   
               
              * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
               
               *Supported key:*  ``PRIORITY``  
        
               *Supported values:*  
        
              * ``Required``   
               
              * ``Important``   
               
              * ``Standard``   
               
              * ``Optional``   
               
              * ``Extra``   
               
               *Supported key:*  ``SECTION``  
        
              Only the length of the key value is validated. Minimum length is 1. Maximum length is 64.
        
               **Amazon Linux Operating Systems**  
        
              The supported keys for Amazon Linux operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
               *Supported key:*  ``PRODUCT``  
        
               *Supported values:*  
        
              * ``AmazonLinux2012.03``   
               
              * ``AmazonLinux2012.09``   
               
              * ``AmazonLinux2013.03``   
               
              * ``AmazonLinux2013.09``   
               
              * ``AmazonLinux2014.03``   
               
              * ``AmazonLinux2014.09``   
               
              * ``AmazonLinux2015.03``   
               
              * ``AmazonLinux2015.09``   
               
              * ``AmazonLinux2016.03``   
               
              * ``AmazonLinux2016.09``   
               
              * ``AmazonLinux2017.03``   
               
              * ``AmazonLinux2017.09``   
               
              * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
               
               *Supported key:*  ``CLASSIFICATION``  
        
               *Supported values:*  
        
              * ``Security``   
               
              * ``Bugfix``   
               
              * ``Enhancement``   
               
              * ``Recommended``   
               
              * ``Newpackage``   
               
               *Supported key:*  ``SEVERITY``  
        
               *Supported values:*  
        
              * ``Critical``   
               
              * ``Important``   
               
              * ``Medium``   
               
              * ``Low``   
               
               **Amazon Linux 2 Operating Systems**  
        
              The supported keys for Amazon Linux 2 operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
               *Supported key:*  ``PRODUCT``  
        
               *Supported values:*  
        
              * ``AmazonLinux2``   
               
              * ``AmazonLinux2.0``   
               
              * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
               
               *Supported key:*  ``CLASSIFICATION``  
        
               *Supported values:*  
        
              * ``Security``   
               
              * ``Bugfix``   
               
              * ``Enhancement``   
               
              * ``Recommended``   
               
              * ``Newpackage``   
               
               *Supported key:*  ``SEVERITY``  
        
               *Supported values:*  
        
              * ``Critical``   
               
              * ``Important``   
               
              * ``Medium``   
               
              * ``Low``   
               
               **RedHat Enterprise Linux (RHEL) Operating Systems**  
        
              The supported keys for RedHat Enterprise Linux operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
               *Supported key:*  ``PRODUCT``  
        
               *Supported values:*  
        
              * ``RedhatEnterpriseLinux6.5``   
               
              * ``RedhatEnterpriseLinux6.6``   
               
              * ``RedhatEnterpriseLinux6.7``   
               
              * ``RedhatEnterpriseLinux6.8``   
               
              * ``RedhatEnterpriseLinux6.9``   
               
              * ``RedhatEnterpriseLinux7.0``   
               
              * ``RedhatEnterpriseLinux7.1``   
               
              * ``RedhatEnterpriseLinux7.2``   
               
              * ``RedhatEnterpriseLinux7.3``   
               
              * ``RedhatEnterpriseLinux7.4``   
               
              * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
               
               *Supported key:*  ``CLASSIFICATION``  
        
               *Supported values:*  
        
              * ``Security``   
               
              * ``Bugfix``   
               
              * ``Enhancement``   
               
              * ``Recommended``   
               
              * ``Newpackage``   
               
               *Supported key:*  ``SEVERITY``  
        
               *Supported values:*  
        
              * ``Critical``   
               
              * ``Important``   
               
              * ``Medium``   
               
              * ``Low``   
               
               **SUSE Linux Enterprise Server (SLES) Operating Systems**  
        
              The supported keys for SLES operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
               *Supported key:*  ``PRODUCT``  
        
               *Supported values:*  
        
              * ``Suse12.0``   
               
              * ``Suse12.1``   
               
              * ``Suse12.2``   
               
              * ``Suse12.3``   
               
              * ``Suse12.4``   
               
              * ``Suse12.5``   
               
              * ``Suse12.6``   
               
              * ``Suse12.7``   
               
              * ``Suse12.8``   
               
              * ``Suse12.9``   
               
              * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
               
               *Supported key:*  ``CLASSIFICATION``  
        
               *Supported values:*  
        
              * ``Security``   
               
              * ``Recommended``   
               
              * ``Optional``   
               
              * ``Feature``   
               
              * ``Document``   
               
              * ``Yast``   
               
               *Supported key:*  ``SEVERITY``  
        
               *Supported values:*  
        
              * ``Critical``   
               
              * ``Important``   
               
              * ``Moderate``   
               
              * ``Low``   
               
               **CentOS Operating Systems**  
        
              The supported keys for CentOS operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
               *Supported key:*  ``PRODUCT``  
        
               *Supported values:*  
        
              * ``CentOS6.5``   
               
              * ``CentOS6.6``   
               
              * ``CentOS6.7``   
               
              * ``CentOS6.8``   
               
              * ``CentOS6.9``   
               
              * ``CentOS7.0``   
               
              * ``CentOS7.1``   
               
              * ``CentOS7.2``   
               
              * ``CentOS7.3``   
               
              * ``CentOS7.4``   
               
              * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
               
               *Supported key:*  ``CLASSIFICATION``  
        
               *Supported values:*  
        
              * ``Security``   
               
              * ``Bugfix``   
               
              * ``Enhancement``   
               
              * ``Recommended``   
               
              * ``Newpackage``   
               
               *Supported key:*  ``SEVERITY``  
        
               *Supported values:*  
        
              * ``Critical``   
               
              * ``Important``   
               
              * ``Medium``   
               
              * ``Low``   
               
              - **Key** *(string) --* **[REQUIRED]** 
        
                The key for the filter.
        
                See  PatchFilter for lists of valid keys for each operating system type.
        
              - **Values** *(list) --* **[REQUIRED]** 
        
                The value for the filter key.
        
                See  PatchFilter for lists of valid values for each key based on operating system type.
        
                - *(string) --* 
        
        :type ApprovalRules: dict
        :param ApprovalRules: 
        
          A set of rules used to include patches in the baseline.
        
          - **PatchRules** *(list) --* **[REQUIRED]** 
        
            The rules that make up the rule group.
        
            - *(dict) --* 
        
              Defines an approval rule for a patch baseline.
        
              - **PatchFilterGroup** *(dict) --* **[REQUIRED]** 
        
                The patch filter group that defines the criteria for the rule.
        
                - **PatchFilters** *(list) --* **[REQUIRED]** 
        
                  The set of patch filters that make up the group.
        
                  - *(dict) --* 
        
                    Defines a patch filter.
        
                    A patch filter consists of key/value pairs, but not all keys are valid for all operating system types. For example, the key ``PRODUCT`` is valid for all supported operating system types. The key ``MSRC_SEVERITY`` , however, is valid only for Windows operating systems, and the key ``SECTION`` is valid only for Ubuntu operating systems.
        
                    Refer to the following sections for information about which keys may be used with each major operating system, and which values are valid for each key.
        
                     **Windows Operating Systems**  
        
                    The supported keys for Windows operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``MSRC_SEVERITY`` . See the following lists for valid values for each of these keys.
        
                     *Supported key:*  ``PRODUCT``  
        
                     *Supported values:*  
        
                    * ``Windows7``   
                     
                    * ``Windows8``   
                     
                    * ``Windows8.1``   
                     
                    * ``Windows8Embedded``   
                     
                    * ``Windows10``   
                     
                    * ``Windows10LTSB``   
                     
                    * ``WindowsServer2008``   
                     
                    * ``WindowsServer2008R2``   
                     
                    * ``WindowsServer2012``   
                     
                    * ``WindowsServer2012R2``   
                     
                    * ``WindowsServer2016``   
                     
                    * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                     
                     *Supported key:*  ``CLASSIFICATION``  
        
                     *Supported values:*  
        
                    * ``CriticalUpdates``   
                     
                    * ``DefinitionUpdates``   
                     
                    * ``Drivers``   
                     
                    * ``FeaturePacks``   
                     
                    * ``SecurityUpdates``   
                     
                    * ``ServicePacks``   
                     
                    * ``Tools``   
                     
                    * ``UpdateRollups``   
                     
                    * ``Updates``   
                     
                    * ``Upgrades``   
                     
                     *Supported key:*  ``MSRC_SEVERITY``  
        
                     *Supported values:*  
        
                    * ``Critical``   
                     
                    * ``Important``   
                     
                    * ``Moderate``   
                     
                    * ``Low``   
                     
                    * ``Unspecified``   
                     
                     **Ubuntu Operating Systems**  
        
                    The supported keys for Ubuntu operating systems are ``PRODUCT`` , ``PRIORITY`` , and ``SECTION`` . See the following lists for valid values for each of these keys.
        
                     *Supported key:*  ``PRODUCT``  
        
                     *Supported values:*  
        
                    * ``Ubuntu14.04``   
                     
                    * ``Ubuntu16.04``   
                     
                    * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                     
                     *Supported key:*  ``PRIORITY``  
        
                     *Supported values:*  
        
                    * ``Required``   
                     
                    * ``Important``   
                     
                    * ``Standard``   
                     
                    * ``Optional``   
                     
                    * ``Extra``   
                     
                     *Supported key:*  ``SECTION``  
        
                    Only the length of the key value is validated. Minimum length is 1. Maximum length is 64.
        
                     **Amazon Linux Operating Systems**  
        
                    The supported keys for Amazon Linux operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                     *Supported key:*  ``PRODUCT``  
        
                     *Supported values:*  
        
                    * ``AmazonLinux2012.03``   
                     
                    * ``AmazonLinux2012.09``   
                     
                    * ``AmazonLinux2013.03``   
                     
                    * ``AmazonLinux2013.09``   
                     
                    * ``AmazonLinux2014.03``   
                     
                    * ``AmazonLinux2014.09``   
                     
                    * ``AmazonLinux2015.03``   
                     
                    * ``AmazonLinux2015.09``   
                     
                    * ``AmazonLinux2016.03``   
                     
                    * ``AmazonLinux2016.09``   
                     
                    * ``AmazonLinux2017.03``   
                     
                    * ``AmazonLinux2017.09``   
                     
                    * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                     
                     *Supported key:*  ``CLASSIFICATION``  
        
                     *Supported values:*  
        
                    * ``Security``   
                     
                    * ``Bugfix``   
                     
                    * ``Enhancement``   
                     
                    * ``Recommended``   
                     
                    * ``Newpackage``   
                     
                     *Supported key:*  ``SEVERITY``  
        
                     *Supported values:*  
        
                    * ``Critical``   
                     
                    * ``Important``   
                     
                    * ``Medium``   
                     
                    * ``Low``   
                     
                     **Amazon Linux 2 Operating Systems**  
        
                    The supported keys for Amazon Linux 2 operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                     *Supported key:*  ``PRODUCT``  
        
                     *Supported values:*  
        
                    * ``AmazonLinux2``   
                     
                    * ``AmazonLinux2.0``   
                     
                    * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                     
                     *Supported key:*  ``CLASSIFICATION``  
        
                     *Supported values:*  
        
                    * ``Security``   
                     
                    * ``Bugfix``   
                     
                    * ``Enhancement``   
                     
                    * ``Recommended``   
                     
                    * ``Newpackage``   
                     
                     *Supported key:*  ``SEVERITY``  
        
                     *Supported values:*  
        
                    * ``Critical``   
                     
                    * ``Important``   
                     
                    * ``Medium``   
                     
                    * ``Low``   
                     
                     **RedHat Enterprise Linux (RHEL) Operating Systems**  
        
                    The supported keys for RedHat Enterprise Linux operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                     *Supported key:*  ``PRODUCT``  
        
                     *Supported values:*  
        
                    * ``RedhatEnterpriseLinux6.5``   
                     
                    * ``RedhatEnterpriseLinux6.6``   
                     
                    * ``RedhatEnterpriseLinux6.7``   
                     
                    * ``RedhatEnterpriseLinux6.8``   
                     
                    * ``RedhatEnterpriseLinux6.9``   
                     
                    * ``RedhatEnterpriseLinux7.0``   
                     
                    * ``RedhatEnterpriseLinux7.1``   
                     
                    * ``RedhatEnterpriseLinux7.2``   
                     
                    * ``RedhatEnterpriseLinux7.3``   
                     
                    * ``RedhatEnterpriseLinux7.4``   
                     
                    * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                     
                     *Supported key:*  ``CLASSIFICATION``  
        
                     *Supported values:*  
        
                    * ``Security``   
                     
                    * ``Bugfix``   
                     
                    * ``Enhancement``   
                     
                    * ``Recommended``   
                     
                    * ``Newpackage``   
                     
                     *Supported key:*  ``SEVERITY``  
        
                     *Supported values:*  
        
                    * ``Critical``   
                     
                    * ``Important``   
                     
                    * ``Medium``   
                     
                    * ``Low``   
                     
                     **SUSE Linux Enterprise Server (SLES) Operating Systems**  
        
                    The supported keys for SLES operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                     *Supported key:*  ``PRODUCT``  
        
                     *Supported values:*  
        
                    * ``Suse12.0``   
                     
                    * ``Suse12.1``   
                     
                    * ``Suse12.2``   
                     
                    * ``Suse12.3``   
                     
                    * ``Suse12.4``   
                     
                    * ``Suse12.5``   
                     
                    * ``Suse12.6``   
                     
                    * ``Suse12.7``   
                     
                    * ``Suse12.8``   
                     
                    * ``Suse12.9``   
                     
                    * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                     
                     *Supported key:*  ``CLASSIFICATION``  
        
                     *Supported values:*  
        
                    * ``Security``   
                     
                    * ``Recommended``   
                     
                    * ``Optional``   
                     
                    * ``Feature``   
                     
                    * ``Document``   
                     
                    * ``Yast``   
                     
                     *Supported key:*  ``SEVERITY``  
        
                     *Supported values:*  
        
                    * ``Critical``   
                     
                    * ``Important``   
                     
                    * ``Moderate``   
                     
                    * ``Low``   
                     
                     **CentOS Operating Systems**  
        
                    The supported keys for CentOS operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                     *Supported key:*  ``PRODUCT``  
        
                     *Supported values:*  
        
                    * ``CentOS6.5``   
                     
                    * ``CentOS6.6``   
                     
                    * ``CentOS6.7``   
                     
                    * ``CentOS6.8``   
                     
                    * ``CentOS6.9``   
                     
                    * ``CentOS7.0``   
                     
                    * ``CentOS7.1``   
                     
                    * ``CentOS7.2``   
                     
                    * ``CentOS7.3``   
                     
                    * ``CentOS7.4``   
                     
                    * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                     
                     *Supported key:*  ``CLASSIFICATION``  
        
                     *Supported values:*  
        
                    * ``Security``   
                     
                    * ``Bugfix``   
                     
                    * ``Enhancement``   
                     
                    * ``Recommended``   
                     
                    * ``Newpackage``   
                     
                     *Supported key:*  ``SEVERITY``  
        
                     *Supported values:*  
        
                    * ``Critical``   
                     
                    * ``Important``   
                     
                    * ``Medium``   
                     
                    * ``Low``   
                     
                    - **Key** *(string) --* **[REQUIRED]** 
        
                      The key for the filter.
        
                      See  PatchFilter for lists of valid keys for each operating system type.
        
                    - **Values** *(list) --* **[REQUIRED]** 
        
                      The value for the filter key.
        
                      See  PatchFilter for lists of valid values for each key based on operating system type.
        
                      - *(string) --* 
        
              - **ComplianceLevel** *(string) --* 
        
                A compliance severity level for all approved patches in a patch baseline. Valid compliance severity levels include the following: Unspecified, Critical, High, Medium, Low, and Informational.
        
              - **ApproveAfterDays** *(integer) --* **[REQUIRED]** 
        
                The number of days after the release date of each patch matched by the rule that the patch is marked as approved in the patch baseline. For example, a value of ``7`` means that patches are approved seven days after they are released. 
        
              - **EnableNonSecurity** *(boolean) --* 
        
                For instances identified by the approval rule filters, enables a patch baseline to apply non-security updates available in the specified repository. The default value is \'false\'. Applies to Linux instances only.
        
        :type ApprovedPatches: list
        :param ApprovedPatches: 
        
          A list of explicitly approved patches for the baseline.
        
          For information about accepted formats for lists of approved patches and rejected patches, see `Package Name Formats for Approved and Rejected Patch Lists <http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html>`__ in the *AWS Systems Manager User Guide* .
        
          - *(string) --* 
        
        :type ApprovedPatchesComplianceLevel: string
        :param ApprovedPatchesComplianceLevel: 
        
          Assigns a new compliance severity level to an existing patch baseline.
        
        :type ApprovedPatchesEnableNonSecurity: boolean
        :param ApprovedPatchesEnableNonSecurity: 
        
          Indicates whether the list of approved patches includes non-security updates that should be applied to the instances. The default value is \'false\'. Applies to Linux instances only.
        
        :type RejectedPatches: list
        :param RejectedPatches: 
        
          A list of explicitly rejected patches for the baseline.
        
          For information about accepted formats for lists of approved patches and rejected patches, see `Package Name Formats for Approved and Rejected Patch Lists <http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html>`__ in the *AWS Systems Manager User Guide* .
        
          - *(string) --* 
        
        :type RejectedPatchesAction: string
        :param RejectedPatchesAction: 
        
          The action for Patch Manager to take on patches included in the RejectedPackages list.
        
          * **ALLOW_AS_DEPENDENCY** : A package in the Rejected patches list is installed only if it is a dependency of another package. It is considered compliant with the patch baseline, and its status is reported as *InstalledOther* . This is the default action if no option is specified. 
           
          * **BLOCK** : Packages in the RejectedPatches list, and packages that include them as dependencies, are not installed under any circumstances. If a package was installed before it was added to the Rejected patches list, it is considered non-compliant with the patch baseline, and its status is reported as *InstalledRejected* . 
           
        :type Description: string
        :param Description: 
        
          A description of the patch baseline.
        
        :type Sources: list
        :param Sources: 
        
          Information about the patches to use to update the instances, including target operating systems and source repositories. Applies to Linux instances only.
        
          - *(dict) --* 
        
            Information about the patches to use to update the instances, including target operating systems and source repository. Applies to Linux instances only.
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name specified to identify the patch source.
        
            - **Products** *(list) --* **[REQUIRED]** 
        
              The specific operating system versions a patch repository applies to, such as \"Ubuntu16.04\", \"AmazonLinux2016.09\", \"RedhatEnterpriseLinux7.2\" or \"Suse12.7\". For lists of supported product values, see  PatchFilter .
        
              - *(string) --* 
        
            - **Configuration** *(string) --* **[REQUIRED]** 
        
              The value of the yum repo configuration. For example:
        
               ``cachedir=/var/cache/yum/$basesearch``  
        
               ``$releasever``  
        
               ``keepcache=0``  
        
               ``debuglevel=2``  
        
        :type Replace: boolean
        :param Replace: 
        
          If True, then all fields that are required by the CreatePatchBaseline action are also required for this API request. Optional fields that are not specified are set to null.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'BaselineId\': \'string\',
                \'Name\': \'string\',
                \'OperatingSystem\': \'WINDOWS\'|\'AMAZON_LINUX\'|\'AMAZON_LINUX_2\'|\'UBUNTU\'|\'REDHAT_ENTERPRISE_LINUX\'|\'SUSE\'|\'CENTOS\',
                \'GlobalFilters\': {
                    \'PatchFilters\': [
                        {
                            \'Key\': \'PRODUCT\'|\'CLASSIFICATION\'|\'MSRC_SEVERITY\'|\'PATCH_ID\'|\'SECTION\'|\'PRIORITY\'|\'SEVERITY\',
                            \'Values\': [
                                \'string\',
                            ]
                        },
                    ]
                },
                \'ApprovalRules\': {
                    \'PatchRules\': [
                        {
                            \'PatchFilterGroup\': {
                                \'PatchFilters\': [
                                    {
                                        \'Key\': \'PRODUCT\'|\'CLASSIFICATION\'|\'MSRC_SEVERITY\'|\'PATCH_ID\'|\'SECTION\'|\'PRIORITY\'|\'SEVERITY\',
                                        \'Values\': [
                                            \'string\',
                                        ]
                                    },
                                ]
                            },
                            \'ComplianceLevel\': \'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'INFORMATIONAL\'|\'UNSPECIFIED\',
                            \'ApproveAfterDays\': 123,
                            \'EnableNonSecurity\': True|False
                        },
                    ]
                },
                \'ApprovedPatches\': [
                    \'string\',
                ],
                \'ApprovedPatchesComplianceLevel\': \'CRITICAL\'|\'HIGH\'|\'MEDIUM\'|\'LOW\'|\'INFORMATIONAL\'|\'UNSPECIFIED\',
                \'ApprovedPatchesEnableNonSecurity\': True|False,
                \'RejectedPatches\': [
                    \'string\',
                ],
                \'RejectedPatchesAction\': \'ALLOW_AS_DEPENDENCY\'|\'BLOCK\',
                \'CreatedDate\': datetime(2015, 1, 1),
                \'ModifiedDate\': datetime(2015, 1, 1),
                \'Description\': \'string\',
                \'Sources\': [
                    {
                        \'Name\': \'string\',
                        \'Products\': [
                            \'string\',
                        ],
                        \'Configuration\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **BaselineId** *(string) --* 
        
              The ID of the deleted patch baseline.
        
            - **Name** *(string) --* 
        
              The name of the patch baseline.
        
            - **OperatingSystem** *(string) --* 
        
              The operating system rule used by the updated patch baseline.
        
            - **GlobalFilters** *(dict) --* 
        
              A set of global filters used to exclude patches from the baseline.
        
              - **PatchFilters** *(list) --* 
        
                The set of patch filters that make up the group.
        
                - *(dict) --* 
        
                  Defines a patch filter.
        
                  A patch filter consists of key/value pairs, but not all keys are valid for all operating system types. For example, the key ``PRODUCT`` is valid for all supported operating system types. The key ``MSRC_SEVERITY`` , however, is valid only for Windows operating systems, and the key ``SECTION`` is valid only for Ubuntu operating systems.
        
                  Refer to the following sections for information about which keys may be used with each major operating system, and which values are valid for each key.
        
                   **Windows Operating Systems**  
        
                  The supported keys for Windows operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``MSRC_SEVERITY`` . See the following lists for valid values for each of these keys.
        
                   *Supported key:*  ``PRODUCT``  
        
                   *Supported values:*  
        
                  * ``Windows7``   
                   
                  * ``Windows8``   
                   
                  * ``Windows8.1``   
                   
                  * ``Windows8Embedded``   
                   
                  * ``Windows10``   
                   
                  * ``Windows10LTSB``   
                   
                  * ``WindowsServer2008``   
                   
                  * ``WindowsServer2008R2``   
                   
                  * ``WindowsServer2012``   
                   
                  * ``WindowsServer2012R2``   
                   
                  * ``WindowsServer2016``   
                   
                  * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                   
                   *Supported key:*  ``CLASSIFICATION``  
        
                   *Supported values:*  
        
                  * ``CriticalUpdates``   
                   
                  * ``DefinitionUpdates``   
                   
                  * ``Drivers``   
                   
                  * ``FeaturePacks``   
                   
                  * ``SecurityUpdates``   
                   
                  * ``ServicePacks``   
                   
                  * ``Tools``   
                   
                  * ``UpdateRollups``   
                   
                  * ``Updates``   
                   
                  * ``Upgrades``   
                   
                   *Supported key:*  ``MSRC_SEVERITY``  
        
                   *Supported values:*  
        
                  * ``Critical``   
                   
                  * ``Important``   
                   
                  * ``Moderate``   
                   
                  * ``Low``   
                   
                  * ``Unspecified``   
                   
                   **Ubuntu Operating Systems**  
        
                  The supported keys for Ubuntu operating systems are ``PRODUCT`` , ``PRIORITY`` , and ``SECTION`` . See the following lists for valid values for each of these keys.
        
                   *Supported key:*  ``PRODUCT``  
        
                   *Supported values:*  
        
                  * ``Ubuntu14.04``   
                   
                  * ``Ubuntu16.04``   
                   
                  * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                   
                   *Supported key:*  ``PRIORITY``  
        
                   *Supported values:*  
        
                  * ``Required``   
                   
                  * ``Important``   
                   
                  * ``Standard``   
                   
                  * ``Optional``   
                   
                  * ``Extra``   
                   
                   *Supported key:*  ``SECTION``  
        
                  Only the length of the key value is validated. Minimum length is 1. Maximum length is 64.
        
                   **Amazon Linux Operating Systems**  
        
                  The supported keys for Amazon Linux operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                   *Supported key:*  ``PRODUCT``  
        
                   *Supported values:*  
        
                  * ``AmazonLinux2012.03``   
                   
                  * ``AmazonLinux2012.09``   
                   
                  * ``AmazonLinux2013.03``   
                   
                  * ``AmazonLinux2013.09``   
                   
                  * ``AmazonLinux2014.03``   
                   
                  * ``AmazonLinux2014.09``   
                   
                  * ``AmazonLinux2015.03``   
                   
                  * ``AmazonLinux2015.09``   
                   
                  * ``AmazonLinux2016.03``   
                   
                  * ``AmazonLinux2016.09``   
                   
                  * ``AmazonLinux2017.03``   
                   
                  * ``AmazonLinux2017.09``   
                   
                  * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                   
                   *Supported key:*  ``CLASSIFICATION``  
        
                   *Supported values:*  
        
                  * ``Security``   
                   
                  * ``Bugfix``   
                   
                  * ``Enhancement``   
                   
                  * ``Recommended``   
                   
                  * ``Newpackage``   
                   
                   *Supported key:*  ``SEVERITY``  
        
                   *Supported values:*  
        
                  * ``Critical``   
                   
                  * ``Important``   
                   
                  * ``Medium``   
                   
                  * ``Low``   
                   
                   **Amazon Linux 2 Operating Systems**  
        
                  The supported keys for Amazon Linux 2 operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                   *Supported key:*  ``PRODUCT``  
        
                   *Supported values:*  
        
                  * ``AmazonLinux2``   
                   
                  * ``AmazonLinux2.0``   
                   
                  * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                   
                   *Supported key:*  ``CLASSIFICATION``  
        
                   *Supported values:*  
        
                  * ``Security``   
                   
                  * ``Bugfix``   
                   
                  * ``Enhancement``   
                   
                  * ``Recommended``   
                   
                  * ``Newpackage``   
                   
                   *Supported key:*  ``SEVERITY``  
        
                   *Supported values:*  
        
                  * ``Critical``   
                   
                  * ``Important``   
                   
                  * ``Medium``   
                   
                  * ``Low``   
                   
                   **RedHat Enterprise Linux (RHEL) Operating Systems**  
        
                  The supported keys for RedHat Enterprise Linux operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                   *Supported key:*  ``PRODUCT``  
        
                   *Supported values:*  
        
                  * ``RedhatEnterpriseLinux6.5``   
                   
                  * ``RedhatEnterpriseLinux6.6``   
                   
                  * ``RedhatEnterpriseLinux6.7``   
                   
                  * ``RedhatEnterpriseLinux6.8``   
                   
                  * ``RedhatEnterpriseLinux6.9``   
                   
                  * ``RedhatEnterpriseLinux7.0``   
                   
                  * ``RedhatEnterpriseLinux7.1``   
                   
                  * ``RedhatEnterpriseLinux7.2``   
                   
                  * ``RedhatEnterpriseLinux7.3``   
                   
                  * ``RedhatEnterpriseLinux7.4``   
                   
                  * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                   
                   *Supported key:*  ``CLASSIFICATION``  
        
                   *Supported values:*  
        
                  * ``Security``   
                   
                  * ``Bugfix``   
                   
                  * ``Enhancement``   
                   
                  * ``Recommended``   
                   
                  * ``Newpackage``   
                   
                   *Supported key:*  ``SEVERITY``  
        
                   *Supported values:*  
        
                  * ``Critical``   
                   
                  * ``Important``   
                   
                  * ``Medium``   
                   
                  * ``Low``   
                   
                   **SUSE Linux Enterprise Server (SLES) Operating Systems**  
        
                  The supported keys for SLES operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                   *Supported key:*  ``PRODUCT``  
        
                   *Supported values:*  
        
                  * ``Suse12.0``   
                   
                  * ``Suse12.1``   
                   
                  * ``Suse12.2``   
                   
                  * ``Suse12.3``   
                   
                  * ``Suse12.4``   
                   
                  * ``Suse12.5``   
                   
                  * ``Suse12.6``   
                   
                  * ``Suse12.7``   
                   
                  * ``Suse12.8``   
                   
                  * ``Suse12.9``   
                   
                  * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                   
                   *Supported key:*  ``CLASSIFICATION``  
        
                   *Supported values:*  
        
                  * ``Security``   
                   
                  * ``Recommended``   
                   
                  * ``Optional``   
                   
                  * ``Feature``   
                   
                  * ``Document``   
                   
                  * ``Yast``   
                   
                   *Supported key:*  ``SEVERITY``  
        
                   *Supported values:*  
        
                  * ``Critical``   
                   
                  * ``Important``   
                   
                  * ``Moderate``   
                   
                  * ``Low``   
                   
                   **CentOS Operating Systems**  
        
                  The supported keys for CentOS operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                   *Supported key:*  ``PRODUCT``  
        
                   *Supported values:*  
        
                  * ``CentOS6.5``   
                   
                  * ``CentOS6.6``   
                   
                  * ``CentOS6.7``   
                   
                  * ``CentOS6.8``   
                   
                  * ``CentOS6.9``   
                   
                  * ``CentOS7.0``   
                   
                  * ``CentOS7.1``   
                   
                  * ``CentOS7.2``   
                   
                  * ``CentOS7.3``   
                   
                  * ``CentOS7.4``   
                   
                  * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                   
                   *Supported key:*  ``CLASSIFICATION``  
        
                   *Supported values:*  
        
                  * ``Security``   
                   
                  * ``Bugfix``   
                   
                  * ``Enhancement``   
                   
                  * ``Recommended``   
                   
                  * ``Newpackage``   
                   
                   *Supported key:*  ``SEVERITY``  
        
                   *Supported values:*  
        
                  * ``Critical``   
                   
                  * ``Important``   
                   
                  * ``Medium``   
                   
                  * ``Low``   
                   
                  - **Key** *(string) --* 
        
                    The key for the filter.
        
                    See  PatchFilter for lists of valid keys for each operating system type.
        
                  - **Values** *(list) --* 
        
                    The value for the filter key.
        
                    See  PatchFilter for lists of valid values for each key based on operating system type.
        
                    - *(string) --* 
                
            - **ApprovalRules** *(dict) --* 
        
              A set of rules used to include patches in the baseline.
        
              - **PatchRules** *(list) --* 
        
                The rules that make up the rule group.
        
                - *(dict) --* 
        
                  Defines an approval rule for a patch baseline.
        
                  - **PatchFilterGroup** *(dict) --* 
        
                    The patch filter group that defines the criteria for the rule.
        
                    - **PatchFilters** *(list) --* 
        
                      The set of patch filters that make up the group.
        
                      - *(dict) --* 
        
                        Defines a patch filter.
        
                        A patch filter consists of key/value pairs, but not all keys are valid for all operating system types. For example, the key ``PRODUCT`` is valid for all supported operating system types. The key ``MSRC_SEVERITY`` , however, is valid only for Windows operating systems, and the key ``SECTION`` is valid only for Ubuntu operating systems.
        
                        Refer to the following sections for information about which keys may be used with each major operating system, and which values are valid for each key.
        
                         **Windows Operating Systems**  
        
                        The supported keys for Windows operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``MSRC_SEVERITY`` . See the following lists for valid values for each of these keys.
        
                         *Supported key:*  ``PRODUCT``  
        
                         *Supported values:*  
        
                        * ``Windows7``   
                         
                        * ``Windows8``   
                         
                        * ``Windows8.1``   
                         
                        * ``Windows8Embedded``   
                         
                        * ``Windows10``   
                         
                        * ``Windows10LTSB``   
                         
                        * ``WindowsServer2008``   
                         
                        * ``WindowsServer2008R2``   
                         
                        * ``WindowsServer2012``   
                         
                        * ``WindowsServer2012R2``   
                         
                        * ``WindowsServer2016``   
                         
                        * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                         
                         *Supported key:*  ``CLASSIFICATION``  
        
                         *Supported values:*  
        
                        * ``CriticalUpdates``   
                         
                        * ``DefinitionUpdates``   
                         
                        * ``Drivers``   
                         
                        * ``FeaturePacks``   
                         
                        * ``SecurityUpdates``   
                         
                        * ``ServicePacks``   
                         
                        * ``Tools``   
                         
                        * ``UpdateRollups``   
                         
                        * ``Updates``   
                         
                        * ``Upgrades``   
                         
                         *Supported key:*  ``MSRC_SEVERITY``  
        
                         *Supported values:*  
        
                        * ``Critical``   
                         
                        * ``Important``   
                         
                        * ``Moderate``   
                         
                        * ``Low``   
                         
                        * ``Unspecified``   
                         
                         **Ubuntu Operating Systems**  
        
                        The supported keys for Ubuntu operating systems are ``PRODUCT`` , ``PRIORITY`` , and ``SECTION`` . See the following lists for valid values for each of these keys.
        
                         *Supported key:*  ``PRODUCT``  
        
                         *Supported values:*  
        
                        * ``Ubuntu14.04``   
                         
                        * ``Ubuntu16.04``   
                         
                        * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                         
                         *Supported key:*  ``PRIORITY``  
        
                         *Supported values:*  
        
                        * ``Required``   
                         
                        * ``Important``   
                         
                        * ``Standard``   
                         
                        * ``Optional``   
                         
                        * ``Extra``   
                         
                         *Supported key:*  ``SECTION``  
        
                        Only the length of the key value is validated. Minimum length is 1. Maximum length is 64.
        
                         **Amazon Linux Operating Systems**  
        
                        The supported keys for Amazon Linux operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                         *Supported key:*  ``PRODUCT``  
        
                         *Supported values:*  
        
                        * ``AmazonLinux2012.03``   
                         
                        * ``AmazonLinux2012.09``   
                         
                        * ``AmazonLinux2013.03``   
                         
                        * ``AmazonLinux2013.09``   
                         
                        * ``AmazonLinux2014.03``   
                         
                        * ``AmazonLinux2014.09``   
                         
                        * ``AmazonLinux2015.03``   
                         
                        * ``AmazonLinux2015.09``   
                         
                        * ``AmazonLinux2016.03``   
                         
                        * ``AmazonLinux2016.09``   
                         
                        * ``AmazonLinux2017.03``   
                         
                        * ``AmazonLinux2017.09``   
                         
                        * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                         
                         *Supported key:*  ``CLASSIFICATION``  
        
                         *Supported values:*  
        
                        * ``Security``   
                         
                        * ``Bugfix``   
                         
                        * ``Enhancement``   
                         
                        * ``Recommended``   
                         
                        * ``Newpackage``   
                         
                         *Supported key:*  ``SEVERITY``  
        
                         *Supported values:*  
        
                        * ``Critical``   
                         
                        * ``Important``   
                         
                        * ``Medium``   
                         
                        * ``Low``   
                         
                         **Amazon Linux 2 Operating Systems**  
        
                        The supported keys for Amazon Linux 2 operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                         *Supported key:*  ``PRODUCT``  
        
                         *Supported values:*  
        
                        * ``AmazonLinux2``   
                         
                        * ``AmazonLinux2.0``   
                         
                        * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                         
                         *Supported key:*  ``CLASSIFICATION``  
        
                         *Supported values:*  
        
                        * ``Security``   
                         
                        * ``Bugfix``   
                         
                        * ``Enhancement``   
                         
                        * ``Recommended``   
                         
                        * ``Newpackage``   
                         
                         *Supported key:*  ``SEVERITY``  
        
                         *Supported values:*  
        
                        * ``Critical``   
                         
                        * ``Important``   
                         
                        * ``Medium``   
                         
                        * ``Low``   
                         
                         **RedHat Enterprise Linux (RHEL) Operating Systems**  
        
                        The supported keys for RedHat Enterprise Linux operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                         *Supported key:*  ``PRODUCT``  
        
                         *Supported values:*  
        
                        * ``RedhatEnterpriseLinux6.5``   
                         
                        * ``RedhatEnterpriseLinux6.6``   
                         
                        * ``RedhatEnterpriseLinux6.7``   
                         
                        * ``RedhatEnterpriseLinux6.8``   
                         
                        * ``RedhatEnterpriseLinux6.9``   
                         
                        * ``RedhatEnterpriseLinux7.0``   
                         
                        * ``RedhatEnterpriseLinux7.1``   
                         
                        * ``RedhatEnterpriseLinux7.2``   
                         
                        * ``RedhatEnterpriseLinux7.3``   
                         
                        * ``RedhatEnterpriseLinux7.4``   
                         
                        * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                         
                         *Supported key:*  ``CLASSIFICATION``  
        
                         *Supported values:*  
        
                        * ``Security``   
                         
                        * ``Bugfix``   
                         
                        * ``Enhancement``   
                         
                        * ``Recommended``   
                         
                        * ``Newpackage``   
                         
                         *Supported key:*  ``SEVERITY``  
        
                         *Supported values:*  
        
                        * ``Critical``   
                         
                        * ``Important``   
                         
                        * ``Medium``   
                         
                        * ``Low``   
                         
                         **SUSE Linux Enterprise Server (SLES) Operating Systems**  
        
                        The supported keys for SLES operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                         *Supported key:*  ``PRODUCT``  
        
                         *Supported values:*  
        
                        * ``Suse12.0``   
                         
                        * ``Suse12.1``   
                         
                        * ``Suse12.2``   
                         
                        * ``Suse12.3``   
                         
                        * ``Suse12.4``   
                         
                        * ``Suse12.5``   
                         
                        * ``Suse12.6``   
                         
                        * ``Suse12.7``   
                         
                        * ``Suse12.8``   
                         
                        * ``Suse12.9``   
                         
                        * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                         
                         *Supported key:*  ``CLASSIFICATION``  
        
                         *Supported values:*  
        
                        * ``Security``   
                         
                        * ``Recommended``   
                         
                        * ``Optional``   
                         
                        * ``Feature``   
                         
                        * ``Document``   
                         
                        * ``Yast``   
                         
                         *Supported key:*  ``SEVERITY``  
        
                         *Supported values:*  
        
                        * ``Critical``   
                         
                        * ``Important``   
                         
                        * ``Moderate``   
                         
                        * ``Low``   
                         
                         **CentOS Operating Systems**  
        
                        The supported keys for CentOS operating systems are ``PRODUCT`` , ``CLASSIFICATION`` , and ``SEVERITY`` . See the following lists for valid values for each of these keys.
        
                         *Supported key:*  ``PRODUCT``  
        
                         *Supported values:*  
        
                        * ``CentOS6.5``   
                         
                        * ``CentOS6.6``   
                         
                        * ``CentOS6.7``   
                         
                        * ``CentOS6.8``   
                         
                        * ``CentOS6.9``   
                         
                        * ``CentOS7.0``   
                         
                        * ``CentOS7.1``   
                         
                        * ``CentOS7.2``   
                         
                        * ``CentOS7.3``   
                         
                        * ``CentOS7.4``   
                         
                        * ``*``    *Use a wildcard character (*) to target all supported operating system versions.*   
                         
                         *Supported key:*  ``CLASSIFICATION``  
        
                         *Supported values:*  
        
                        * ``Security``   
                         
                        * ``Bugfix``   
                         
                        * ``Enhancement``   
                         
                        * ``Recommended``   
                         
                        * ``Newpackage``   
                         
                         *Supported key:*  ``SEVERITY``  
        
                         *Supported values:*  
        
                        * ``Critical``   
                         
                        * ``Important``   
                         
                        * ``Medium``   
                         
                        * ``Low``   
                         
                        - **Key** *(string) --* 
        
                          The key for the filter.
        
                          See  PatchFilter for lists of valid keys for each operating system type.
        
                        - **Values** *(list) --* 
        
                          The value for the filter key.
        
                          See  PatchFilter for lists of valid values for each key based on operating system type.
        
                          - *(string) --* 
                      
                  - **ComplianceLevel** *(string) --* 
        
                    A compliance severity level for all approved patches in a patch baseline. Valid compliance severity levels include the following: Unspecified, Critical, High, Medium, Low, and Informational.
        
                  - **ApproveAfterDays** *(integer) --* 
        
                    The number of days after the release date of each patch matched by the rule that the patch is marked as approved in the patch baseline. For example, a value of ``7`` means that patches are approved seven days after they are released. 
        
                  - **EnableNonSecurity** *(boolean) --* 
        
                    For instances identified by the approval rule filters, enables a patch baseline to apply non-security updates available in the specified repository. The default value is \'false\'. Applies to Linux instances only.
        
            - **ApprovedPatches** *(list) --* 
        
              A list of explicitly approved patches for the baseline.
        
              - *(string) --* 
          
            - **ApprovedPatchesComplianceLevel** *(string) --* 
        
              The compliance severity level assigned to the patch baseline after the update completed.
        
            - **ApprovedPatchesEnableNonSecurity** *(boolean) --* 
        
              Indicates whether the list of approved patches includes non-security updates that should be applied to the instances. The default value is \'false\'. Applies to Linux instances only.
        
            - **RejectedPatches** *(list) --* 
        
              A list of explicitly rejected patches for the baseline.
        
              - *(string) --* 
          
            - **RejectedPatchesAction** *(string) --* 
        
              The action specified to take on patches included in the RejectedPatches list. A patch can be allowed only if it is a dependency of another package, or blocked entirely along with packages that include it as a dependency.
        
            - **CreatedDate** *(datetime) --* 
        
              The date when the patch baseline was created.
        
            - **ModifiedDate** *(datetime) --* 
        
              The date when the patch baseline was last modified.
        
            - **Description** *(string) --* 
        
              A description of the Patch Baseline.
        
            - **Sources** *(list) --* 
        
              Information about the patches to use to update the instances, including target operating systems and source repositories. Applies to Linux instances only.
        
              - *(dict) --* 
        
                Information about the patches to use to update the instances, including target operating systems and source repository. Applies to Linux instances only.
        
                - **Name** *(string) --* 
        
                  The name specified to identify the patch source.
        
                - **Products** *(list) --* 
        
                  The specific operating system versions a patch repository applies to, such as \"Ubuntu16.04\", \"AmazonLinux2016.09\", \"RedhatEnterpriseLinux7.2\" or \"Suse12.7\". For lists of supported product values, see  PatchFilter .
        
                  - *(string) --* 
              
                - **Configuration** *(string) --* 
        
                  The value of the yum repo configuration. For example:
        
                   ``cachedir=/var/cache/yum/$basesearch``  
        
                   ``$releasever``  
        
                   ``keepcache=0``  
        
                   ``debuglevel=2``  
        
        """
        pass
