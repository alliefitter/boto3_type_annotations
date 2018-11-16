from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def associate_fleet(self, FleetName: str, StackName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/AssociateFleet>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_fleet(
              FleetName=\'string\',
              StackName=\'string\'
          )
        :type FleetName: string
        :param FleetName: **[REQUIRED]** 
        
          The name of the fleet. 
        
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name of the stack.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def batch_associate_user_stack(self, UserStackAssociations: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/BatchAssociateUserStack>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_associate_user_stack(
              UserStackAssociations=[
                  {
                      \'StackName\': \'string\',
                      \'UserName\': \'string\',
                      \'AuthenticationType\': \'API\'|\'SAML\'|\'USERPOOL\',
                      \'SendEmailNotification\': True|False
                  },
              ]
          )
        :type UserStackAssociations: list
        :param UserStackAssociations: **[REQUIRED]** 
        
          The list of UserStackAssociation objects.
        
          - *(dict) --* 
        
            Describes a user in the user pool and the associated stack.
        
            - **StackName** *(string) --* **[REQUIRED]** 
        
              The name of the stack that is associated with the user.
        
            - **UserName** *(string) --* **[REQUIRED]** 
        
              The email address of the user who is associated with the stack.
        
            - **AuthenticationType** *(string) --* **[REQUIRED]** 
        
              The authentication type for the user.
        
            - **SendEmailNotification** *(boolean) --* 
        
              Specifies whether a welcome email is sent to a user after the user is created in the user pool.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'errors\': [
                    {
                        \'UserStackAssociation\': {
                            \'StackName\': \'string\',
                            \'UserName\': \'string\',
                            \'AuthenticationType\': \'API\'|\'SAML\'|\'USERPOOL\',
                            \'SendEmailNotification\': True|False
                        },
                        \'ErrorCode\': \'STACK_NOT_FOUND\'|\'USER_NAME_NOT_FOUND\'|\'INTERNAL_ERROR\',
                        \'ErrorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **errors** *(list) --* 
        
              The list of UserStackAssociationError objects.
        
              - *(dict) --* 
        
                Describes the error that is returned when a user can’t be associated with or disassociated from a stack. 
        
                - **UserStackAssociation** *(dict) --* 
        
                  Information about the user and associated stack.
        
                  - **StackName** *(string) --* 
        
                    The name of the stack that is associated with the user.
        
                  - **UserName** *(string) --* 
        
                    The email address of the user who is associated with the stack.
        
                  - **AuthenticationType** *(string) --* 
        
                    The authentication type for the user.
        
                  - **SendEmailNotification** *(boolean) --* 
        
                    Specifies whether a welcome email is sent to a user after the user is created in the user pool.
        
                - **ErrorCode** *(string) --* 
        
                  The error code for the error that is returned when a user can’t be associated with or disassociated from a stack.
        
                - **ErrorMessage** *(string) --* 
        
                  The error message for the error that is returned when a user can’t be associated with or disassociated from a stack.
        
        """
        pass

    def batch_disassociate_user_stack(self, UserStackAssociations: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/BatchDisassociateUserStack>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_disassociate_user_stack(
              UserStackAssociations=[
                  {
                      \'StackName\': \'string\',
                      \'UserName\': \'string\',
                      \'AuthenticationType\': \'API\'|\'SAML\'|\'USERPOOL\',
                      \'SendEmailNotification\': True|False
                  },
              ]
          )
        :type UserStackAssociations: list
        :param UserStackAssociations: **[REQUIRED]** 
        
          The list of UserStackAssociation objects.
        
          - *(dict) --* 
        
            Describes a user in the user pool and the associated stack.
        
            - **StackName** *(string) --* **[REQUIRED]** 
        
              The name of the stack that is associated with the user.
        
            - **UserName** *(string) --* **[REQUIRED]** 
        
              The email address of the user who is associated with the stack.
        
            - **AuthenticationType** *(string) --* **[REQUIRED]** 
        
              The authentication type for the user.
        
            - **SendEmailNotification** *(boolean) --* 
        
              Specifies whether a welcome email is sent to a user after the user is created in the user pool.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'errors\': [
                    {
                        \'UserStackAssociation\': {
                            \'StackName\': \'string\',
                            \'UserName\': \'string\',
                            \'AuthenticationType\': \'API\'|\'SAML\'|\'USERPOOL\',
                            \'SendEmailNotification\': True|False
                        },
                        \'ErrorCode\': \'STACK_NOT_FOUND\'|\'USER_NAME_NOT_FOUND\'|\'INTERNAL_ERROR\',
                        \'ErrorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **errors** *(list) --* 
        
              The list of UserStackAssociationError objects.
        
              - *(dict) --* 
        
                Describes the error that is returned when a user can’t be associated with or disassociated from a stack. 
        
                - **UserStackAssociation** *(dict) --* 
        
                  Information about the user and associated stack.
        
                  - **StackName** *(string) --* 
        
                    The name of the stack that is associated with the user.
        
                  - **UserName** *(string) --* 
        
                    The email address of the user who is associated with the stack.
        
                  - **AuthenticationType** *(string) --* 
        
                    The authentication type for the user.
        
                  - **SendEmailNotification** *(boolean) --* 
        
                    Specifies whether a welcome email is sent to a user after the user is created in the user pool.
        
                - **ErrorCode** *(string) --* 
        
                  The error code for the error that is returned when a user can’t be associated with or disassociated from a stack.
        
                - **ErrorMessage** *(string) --* 
        
                  The error message for the error that is returned when a user can’t be associated with or disassociated from a stack.
        
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

    def copy_image(self, SourceImageName: str, DestinationImageName: str, DestinationRegion: str, DestinationImageDescription: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/CopyImage>`_
        
        **Request Syntax** 
        ::
        
          response = client.copy_image(
              SourceImageName=\'string\',
              DestinationImageName=\'string\',
              DestinationRegion=\'string\',
              DestinationImageDescription=\'string\'
          )
        :type SourceImageName: string
        :param SourceImageName: **[REQUIRED]** 
        
          The name of the image to copy.
        
        :type DestinationImageName: string
        :param DestinationImageName: **[REQUIRED]** 
        
          The name that the image will have when it is copied to the destination.
        
        :type DestinationRegion: string
        :param DestinationRegion: **[REQUIRED]** 
        
          The destination region to which the image will be copied. This parameter is required, even if you are copying an image within the same region.
        
        :type DestinationImageDescription: string
        :param DestinationImageDescription: 
        
          The description that the image will have when it is copied to the destination.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DestinationImageName\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DestinationImageName** *(string) --* 
        
              The name of the destination image.
        
        """
        pass

    def create_directory_config(self, DirectoryName: str, OrganizationalUnitDistinguishedNames: List, ServiceAccountCredentials: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/CreateDirectoryConfig>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_directory_config(
              DirectoryName=\'string\',
              OrganizationalUnitDistinguishedNames=[
                  \'string\',
              ],
              ServiceAccountCredentials={
                  \'AccountName\': \'string\',
                  \'AccountPassword\': \'string\'
              }
          )
        :type DirectoryName: string
        :param DirectoryName: **[REQUIRED]** 
        
          The fully qualified name of the directory (for example, corp.example.com).
        
        :type OrganizationalUnitDistinguishedNames: list
        :param OrganizationalUnitDistinguishedNames: **[REQUIRED]** 
        
          The distinguished names of the organizational units for computer accounts.
        
          - *(string) --* 
        
        :type ServiceAccountCredentials: dict
        :param ServiceAccountCredentials: **[REQUIRED]** 
        
          The credentials for the service account used by the streaming instance to connect to the directory.
        
          - **AccountName** *(string) --* **[REQUIRED]** 
        
            The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.
        
          - **AccountPassword** *(string) --* **[REQUIRED]** 
        
            The password for the account.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DirectoryConfig\': {
                    \'DirectoryName\': \'string\',
                    \'OrganizationalUnitDistinguishedNames\': [
                        \'string\',
                    ],
                    \'ServiceAccountCredentials\': {
                        \'AccountName\': \'string\',
                        \'AccountPassword\': \'string\'
                    },
                    \'CreatedTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DirectoryConfig** *(dict) --* 
        
              Information about the directory configuration.
        
              - **DirectoryName** *(string) --* 
        
                The fully qualified name of the directory (for example, corp.example.com).
        
              - **OrganizationalUnitDistinguishedNames** *(list) --* 
        
                The distinguished names of the organizational units for computer accounts.
        
                - *(string) --* 
            
              - **ServiceAccountCredentials** *(dict) --* 
        
                The credentials for the service account used by the streaming instance to connect to the directory.
        
                - **AccountName** *(string) --* 
        
                  The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.
        
                - **AccountPassword** *(string) --* 
        
                  The password for the account.
        
              - **CreatedTime** *(datetime) --* 
        
                The time the directory configuration was created.
        
        """
        pass

    def create_fleet(self, Name: str, InstanceType: str, ComputeCapacity: Dict, ImageName: str = None, ImageArn: str = None, FleetType: str = None, VpcConfig: Dict = None, MaxUserDurationInSeconds: int = None, DisconnectTimeoutInSeconds: int = None, Description: str = None, DisplayName: str = None, EnableDefaultInternetAccess: bool = None, DomainJoinInfo: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/CreateFleet>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_fleet(
              Name=\'string\',
              ImageName=\'string\',
              ImageArn=\'string\',
              InstanceType=\'string\',
              FleetType=\'ALWAYS_ON\'|\'ON_DEMAND\',
              ComputeCapacity={
                  \'DesiredInstances\': 123
              },
              VpcConfig={
                  \'SubnetIds\': [
                      \'string\',
                  ],
                  \'SecurityGroupIds\': [
                      \'string\',
                  ]
              },
              MaxUserDurationInSeconds=123,
              DisconnectTimeoutInSeconds=123,
              Description=\'string\',
              DisplayName=\'string\',
              EnableDefaultInternetAccess=True|False,
              DomainJoinInfo={
                  \'DirectoryName\': \'string\',
                  \'OrganizationalUnitDistinguishedName\': \'string\'
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          A unique name for the fleet.
        
        :type ImageName: string
        :param ImageName: 
        
          The name of the image used to create the fleet.
        
        :type ImageArn: string
        :param ImageArn: 
        
          The ARN of the public, private, or shared image to use.
        
        :type InstanceType: string
        :param InstanceType: **[REQUIRED]** 
        
          The instance type to use when launching fleet instances. The following instance types are available:
        
          * stream.standard.medium 
           
          * stream.standard.large 
           
          * stream.compute.large 
           
          * stream.compute.xlarge 
           
          * stream.compute.2xlarge 
           
          * stream.compute.4xlarge 
           
          * stream.compute.8xlarge 
           
          * stream.memory.large 
           
          * stream.memory.xlarge 
           
          * stream.memory.2xlarge 
           
          * stream.memory.4xlarge 
           
          * stream.memory.8xlarge 
           
          * stream.graphics-design.large 
           
          * stream.graphics-design.xlarge 
           
          * stream.graphics-design.2xlarge 
           
          * stream.graphics-design.4xlarge 
           
          * stream.graphics-desktop.2xlarge 
           
          * stream.graphics-pro.4xlarge 
           
          * stream.graphics-pro.8xlarge 
           
          * stream.graphics-pro.16xlarge 
           
        :type FleetType: string
        :param FleetType: 
        
          The fleet type.
        
            ALWAYS_ON  
        
          Provides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps.
        
            ON_DEMAND  
        
          Provide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps.
        
        :type ComputeCapacity: dict
        :param ComputeCapacity: **[REQUIRED]** 
        
          The desired capacity for the fleet.
        
          - **DesiredInstances** *(integer) --* **[REQUIRED]** 
        
            The desired number of streaming instances.
        
        :type VpcConfig: dict
        :param VpcConfig: 
        
          The VPC configuration for the fleet.
        
          - **SubnetIds** *(list) --* 
        
            The subnets to which a network interface is established from the fleet instance.
        
            - *(string) --* 
        
          - **SecurityGroupIds** *(list) --* 
        
            The security groups for the fleet.
        
            - *(string) --* 
        
        :type MaxUserDurationInSeconds: integer
        :param MaxUserDurationInSeconds: 
        
          The maximum time that a streaming session can run, in seconds. Specify a value between 600 and 57600.
        
        :type DisconnectTimeoutInSeconds: integer
        :param DisconnectTimeoutInSeconds: 
        
          The time after disconnection when a session is considered to have ended, in seconds. If a user who was disconnected reconnects within this time interval, the user is connected to their previous session. Specify a value between 60 and 57600.
        
        :type Description: string
        :param Description: 
        
          The description for display.
        
        :type DisplayName: string
        :param DisplayName: 
        
          The fleet name for display.
        
        :type EnableDefaultInternetAccess: boolean
        :param EnableDefaultInternetAccess: 
        
          Enables or disables default internet access for the fleet.
        
        :type DomainJoinInfo: dict
        :param DomainJoinInfo: 
        
          The information needed to join a Microsoft Active Directory domain.
        
          - **DirectoryName** *(string) --* 
        
            The fully qualified name of the directory (for example, corp.example.com).
        
          - **OrganizationalUnitDistinguishedName** *(string) --* 
        
            The distinguished name of the organizational unit for computer accounts.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Fleet\': {
                    \'Arn\': \'string\',
                    \'Name\': \'string\',
                    \'DisplayName\': \'string\',
                    \'Description\': \'string\',
                    \'ImageName\': \'string\',
                    \'ImageArn\': \'string\',
                    \'InstanceType\': \'string\',
                    \'FleetType\': \'ALWAYS_ON\'|\'ON_DEMAND\',
                    \'ComputeCapacityStatus\': {
                        \'Desired\': 123,
                        \'Running\': 123,
                        \'InUse\': 123,
                        \'Available\': 123
                    },
                    \'MaxUserDurationInSeconds\': 123,
                    \'DisconnectTimeoutInSeconds\': 123,
                    \'State\': \'STARTING\'|\'RUNNING\'|\'STOPPING\'|\'STOPPED\',
                    \'VpcConfig\': {
                        \'SubnetIds\': [
                            \'string\',
                        ],
                        \'SecurityGroupIds\': [
                            \'string\',
                        ]
                    },
                    \'CreatedTime\': datetime(2015, 1, 1),
                    \'FleetErrors\': [
                        {
                            \'ErrorCode\': \'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION\'|\'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION\'|\'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION\'|\'NETWORK_INTERFACE_LIMIT_EXCEEDED\'|\'INTERNAL_SERVICE_ERROR\'|\'IAM_SERVICE_ROLE_IS_MISSING\'|\'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES\'|\'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION\'|\'SUBNET_NOT_FOUND\'|\'IMAGE_NOT_FOUND\'|\'INVALID_SUBNET_CONFIGURATION\'|\'SECURITY_GROUPS_NOT_FOUND\'|\'IGW_NOT_ATTACHED\'|\'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION\'|\'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND\'|\'DOMAIN_JOIN_ERROR_ACCESS_DENIED\'|\'DOMAIN_JOIN_ERROR_LOGON_FAILURE\'|\'DOMAIN_JOIN_ERROR_INVALID_PARAMETER\'|\'DOMAIN_JOIN_ERROR_MORE_DATA\'|\'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN\'|\'DOMAIN_JOIN_ERROR_NOT_SUPPORTED\'|\'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME\'|\'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED\'|\'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED\'|\'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED\'|\'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR\',
                            \'ErrorMessage\': \'string\'
                        },
                    ],
                    \'EnableDefaultInternetAccess\': True|False,
                    \'DomainJoinInfo\': {
                        \'DirectoryName\': \'string\',
                        \'OrganizationalUnitDistinguishedName\': \'string\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Fleet** *(dict) --* 
        
              Information about the fleet.
        
              - **Arn** *(string) --* 
        
                The ARN for the fleet.
        
              - **Name** *(string) --* 
        
                The name of the fleet.
        
              - **DisplayName** *(string) --* 
        
                The fleet name for display.
        
              - **Description** *(string) --* 
        
                The description for display.
        
              - **ImageName** *(string) --* 
        
                The name of the image used to create the fleet.
        
              - **ImageArn** *(string) --* 
        
                The ARN for the public, private, or shared image.
        
              - **InstanceType** *(string) --* 
        
                The instance type to use when launching fleet instances.
        
              - **FleetType** *(string) --* 
        
                The fleet type.
        
                  ALWAYS_ON  
        
                Provides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps.
        
                  ON_DEMAND  
        
                Provide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps.
        
              - **ComputeCapacityStatus** *(dict) --* 
        
                The capacity status for the fleet.
        
                - **Desired** *(integer) --* 
        
                  The desired number of streaming instances.
        
                - **Running** *(integer) --* 
        
                  The total number of simultaneous streaming instances that are running.
        
                - **InUse** *(integer) --* 
        
                  The number of instances in use for streaming.
        
                - **Available** *(integer) --* 
        
                  The number of currently available instances that can be used to stream sessions.
        
              - **MaxUserDurationInSeconds** *(integer) --* 
        
                The maximum time that a streaming session can run, in seconds. Specify a value between 600 and 57600.
        
              - **DisconnectTimeoutInSeconds** *(integer) --* 
        
                The time after disconnection when a session is considered to have ended, in seconds. If a user who was disconnected reconnects within this time interval, the user is connected to their previous session. Specify a value between 60 and 57600.
        
              - **State** *(string) --* 
        
                The current state for the fleet.
        
              - **VpcConfig** *(dict) --* 
        
                The VPC configuration for the fleet.
        
                - **SubnetIds** *(list) --* 
        
                  The subnets to which a network interface is established from the fleet instance.
        
                  - *(string) --* 
              
                - **SecurityGroupIds** *(list) --* 
        
                  The security groups for the fleet.
        
                  - *(string) --* 
              
              - **CreatedTime** *(datetime) --* 
        
                The time the fleet was created.
        
              - **FleetErrors** *(list) --* 
        
                The fleet errors.
        
                - *(dict) --* 
        
                  Describes a fleet error.
        
                  - **ErrorCode** *(string) --* 
        
                    The error code.
        
                  - **ErrorMessage** *(string) --* 
        
                    The error message.
        
              - **EnableDefaultInternetAccess** *(boolean) --* 
        
                Indicates whether default internet access is enabled for the fleet.
        
              - **DomainJoinInfo** *(dict) --* 
        
                The information needed to join a Microsoft Active Directory domain.
        
                - **DirectoryName** *(string) --* 
        
                  The fully qualified name of the directory (for example, corp.example.com).
        
                - **OrganizationalUnitDistinguishedName** *(string) --* 
        
                  The distinguished name of the organizational unit for computer accounts.
        
        """
        pass

    def create_image_builder(self, Name: str, InstanceType: str, ImageName: str = None, ImageArn: str = None, Description: str = None, DisplayName: str = None, VpcConfig: Dict = None, EnableDefaultInternetAccess: bool = None, DomainJoinInfo: Dict = None, AppstreamAgentVersion: str = None) -> Dict:
        """
        
        The initial state of the builder is ``PENDING`` . When it is ready, the state is ``RUNNING`` .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/CreateImageBuilder>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_image_builder(
              Name=\'string\',
              ImageName=\'string\',
              ImageArn=\'string\',
              InstanceType=\'string\',
              Description=\'string\',
              DisplayName=\'string\',
              VpcConfig={
                  \'SubnetIds\': [
                      \'string\',
                  ],
                  \'SecurityGroupIds\': [
                      \'string\',
                  ]
              },
              EnableDefaultInternetAccess=True|False,
              DomainJoinInfo={
                  \'DirectoryName\': \'string\',
                  \'OrganizationalUnitDistinguishedName\': \'string\'
              },
              AppstreamAgentVersion=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          A unique name for the image builder.
        
        :type ImageName: string
        :param ImageName: 
        
          The name of the image used to create the builder.
        
        :type ImageArn: string
        :param ImageArn: 
        
          The ARN of the public, private, or shared image to use.
        
        :type InstanceType: string
        :param InstanceType: **[REQUIRED]** 
        
          The instance type to use when launching the image builder.
        
        :type Description: string
        :param Description: 
        
          The description for display.
        
        :type DisplayName: string
        :param DisplayName: 
        
          The image builder name for display.
        
        :type VpcConfig: dict
        :param VpcConfig: 
        
          The VPC configuration for the image builder. You can specify only one subnet.
        
          - **SubnetIds** *(list) --* 
        
            The subnets to which a network interface is established from the fleet instance.
        
            - *(string) --* 
        
          - **SecurityGroupIds** *(list) --* 
        
            The security groups for the fleet.
        
            - *(string) --* 
        
        :type EnableDefaultInternetAccess: boolean
        :param EnableDefaultInternetAccess: 
        
          Enables or disables default internet access for the image builder.
        
        :type DomainJoinInfo: dict
        :param DomainJoinInfo: 
        
          The information needed to join a Microsoft Active Directory domain.
        
          - **DirectoryName** *(string) --* 
        
            The fully qualified name of the directory (for example, corp.example.com).
        
          - **OrganizationalUnitDistinguishedName** *(string) --* 
        
            The distinguished name of the organizational unit for computer accounts.
        
        :type AppstreamAgentVersion: string
        :param AppstreamAgentVersion: 
        
          The version of the AppStream 2.0 agent to use for this image builder. To use the latest version of the AppStream 2.0 agent, specify [LATEST]. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ImageBuilder\': {
                    \'Name\': \'string\',
                    \'Arn\': \'string\',
                    \'ImageArn\': \'string\',
                    \'Description\': \'string\',
                    \'DisplayName\': \'string\',
                    \'VpcConfig\': {
                        \'SubnetIds\': [
                            \'string\',
                        ],
                        \'SecurityGroupIds\': [
                            \'string\',
                        ]
                    },
                    \'InstanceType\': \'string\',
                    \'Platform\': \'WINDOWS\',
                    \'State\': \'PENDING\'|\'UPDATING_AGENT\'|\'RUNNING\'|\'STOPPING\'|\'STOPPED\'|\'REBOOTING\'|\'SNAPSHOTTING\'|\'DELETING\'|\'FAILED\',
                    \'StateChangeReason\': {
                        \'Code\': \'INTERNAL_ERROR\'|\'IMAGE_UNAVAILABLE\',
                        \'Message\': \'string\'
                    },
                    \'CreatedTime\': datetime(2015, 1, 1),
                    \'EnableDefaultInternetAccess\': True|False,
                    \'DomainJoinInfo\': {
                        \'DirectoryName\': \'string\',
                        \'OrganizationalUnitDistinguishedName\': \'string\'
                    },
                    \'ImageBuilderErrors\': [
                        {
                            \'ErrorCode\': \'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION\'|\'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION\'|\'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION\'|\'NETWORK_INTERFACE_LIMIT_EXCEEDED\'|\'INTERNAL_SERVICE_ERROR\'|\'IAM_SERVICE_ROLE_IS_MISSING\'|\'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES\'|\'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION\'|\'SUBNET_NOT_FOUND\'|\'IMAGE_NOT_FOUND\'|\'INVALID_SUBNET_CONFIGURATION\'|\'SECURITY_GROUPS_NOT_FOUND\'|\'IGW_NOT_ATTACHED\'|\'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION\'|\'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND\'|\'DOMAIN_JOIN_ERROR_ACCESS_DENIED\'|\'DOMAIN_JOIN_ERROR_LOGON_FAILURE\'|\'DOMAIN_JOIN_ERROR_INVALID_PARAMETER\'|\'DOMAIN_JOIN_ERROR_MORE_DATA\'|\'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN\'|\'DOMAIN_JOIN_ERROR_NOT_SUPPORTED\'|\'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME\'|\'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED\'|\'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED\'|\'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED\'|\'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR\',
                            \'ErrorMessage\': \'string\',
                            \'ErrorTimestamp\': datetime(2015, 1, 1)
                        },
                    ],
                    \'AppstreamAgentVersion\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ImageBuilder** *(dict) --* 
        
              Information about the image builder.
        
              - **Name** *(string) --* 
        
                The name of the image builder.
        
              - **Arn** *(string) --* 
        
                The ARN for the image builder.
        
              - **ImageArn** *(string) --* 
        
                The ARN of the image from which this builder was created.
        
              - **Description** *(string) --* 
        
                The description for display.
        
              - **DisplayName** *(string) --* 
        
                The image builder name for display.
        
              - **VpcConfig** *(dict) --* 
        
                The VPC configuration of the image builder.
        
                - **SubnetIds** *(list) --* 
        
                  The subnets to which a network interface is established from the fleet instance.
        
                  - *(string) --* 
              
                - **SecurityGroupIds** *(list) --* 
        
                  The security groups for the fleet.
        
                  - *(string) --* 
              
              - **InstanceType** *(string) --* 
        
                The instance type for the image builder.
        
              - **Platform** *(string) --* 
        
                The operating system platform of the image builder.
        
              - **State** *(string) --* 
        
                The state of the image builder.
        
              - **StateChangeReason** *(dict) --* 
        
                The reason why the last state change occurred.
        
                - **Code** *(string) --* 
        
                  The state change reason code.
        
                - **Message** *(string) --* 
        
                  The state change reason message.
        
              - **CreatedTime** *(datetime) --* 
        
                The time stamp when the image builder was created.
        
              - **EnableDefaultInternetAccess** *(boolean) --* 
        
                Enables or disables default internet access for the image builder.
        
              - **DomainJoinInfo** *(dict) --* 
        
                The information needed to join a Microsoft Active Directory domain.
        
                - **DirectoryName** *(string) --* 
        
                  The fully qualified name of the directory (for example, corp.example.com).
        
                - **OrganizationalUnitDistinguishedName** *(string) --* 
        
                  The distinguished name of the organizational unit for computer accounts.
        
              - **ImageBuilderErrors** *(list) --* 
        
                The image builder errors.
        
                - *(dict) --* 
        
                  Describes a resource error.
        
                  - **ErrorCode** *(string) --* 
        
                    The error code.
        
                  - **ErrorMessage** *(string) --* 
        
                    The error message.
        
                  - **ErrorTimestamp** *(datetime) --* 
        
                    The time the error occurred.
        
              - **AppstreamAgentVersion** *(string) --* 
        
                The version of the AppStream 2.0 agent that is currently being used by this image builder. 
        
        """
        pass

    def create_image_builder_streaming_url(self, Name: str, Validity: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/CreateImageBuilderStreamingURL>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_image_builder_streaming_url(
              Name=\'string\',
              Validity=123
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the image builder.
        
        :type Validity: integer
        :param Validity: 
        
          The time that the streaming URL will be valid, in seconds. Specify a value between 1 and 604800 seconds. The default is 3600 seconds.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StreamingURL\': \'string\',
                \'Expires\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **StreamingURL** *(string) --* 
        
              The URL to start the AppStream 2.0 streaming session.
        
            - **Expires** *(datetime) --* 
        
              The elapsed time, in seconds after the Unix epoch, when this URL expires.
        
        """
        pass

    def create_stack(self, Name: str, Description: str = None, DisplayName: str = None, StorageConnectors: List = None, RedirectURL: str = None, FeedbackURL: str = None, UserSettings: List = None, ApplicationSettings: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/CreateStack>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_stack(
              Name=\'string\',
              Description=\'string\',
              DisplayName=\'string\',
              StorageConnectors=[
                  {
                      \'ConnectorType\': \'HOMEFOLDERS\'|\'GOOGLE_DRIVE\'|\'ONE_DRIVE\',
                      \'ResourceIdentifier\': \'string\',
                      \'Domains\': [
                          \'string\',
                      ]
                  },
              ],
              RedirectURL=\'string\',
              FeedbackURL=\'string\',
              UserSettings=[
                  {
                      \'Action\': \'CLIPBOARD_COPY_FROM_LOCAL_DEVICE\'|\'CLIPBOARD_COPY_TO_LOCAL_DEVICE\'|\'FILE_UPLOAD\'|\'FILE_DOWNLOAD\'|\'PRINTING_TO_LOCAL_DEVICE\',
                      \'Permission\': \'ENABLED\'|\'DISABLED\'
                  },
              ],
              ApplicationSettings={
                  \'Enabled\': True|False,
                  \'SettingsGroup\': \'string\'
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the stack.
        
        :type Description: string
        :param Description: 
        
          The description for display.
        
        :type DisplayName: string
        :param DisplayName: 
        
          The stack name for display.
        
        :type StorageConnectors: list
        :param StorageConnectors: 
        
          The storage connectors to enable.
        
          - *(dict) --* 
        
            Describes a connector to enable persistent storage for users.
        
            - **ConnectorType** *(string) --* **[REQUIRED]** 
        
              The type of storage connector.
        
            - **ResourceIdentifier** *(string) --* 
        
              The ARN of the storage connector.
        
            - **Domains** *(list) --* 
        
              The names of the domains for the G Suite account.
        
              - *(string) --* GSuite domain for GDrive integration.
        
        :type RedirectURL: string
        :param RedirectURL: 
        
          The URL that users are redirected to after their streaming session ends.
        
        :type FeedbackURL: string
        :param FeedbackURL: 
        
          The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.
        
        :type UserSettings: list
        :param UserSettings: 
        
          The actions that are enabled or disabled for users during their streaming sessions. By default, these actions are enabled. 
        
          - *(dict) --* 
        
            Describes an action and whether the action is enabled or disabled for users during their streaming sessions.
        
            - **Action** *(string) --* **[REQUIRED]** 
        
              The action that is enabled or disabled.
        
            - **Permission** *(string) --* **[REQUIRED]** 
        
              Indicates whether the action is enabled or disabled.
        
        :type ApplicationSettings: dict
        :param ApplicationSettings: 
        
          The persistent application settings for users of a stack. When these settings are enabled, changes that users make to applications and Windows settings are automatically saved after each session and applied to the next session.
        
          - **Enabled** *(boolean) --* **[REQUIRED]** 
        
            Enables or disables persistent application settings for users during their streaming sessions. 
        
          - **SettingsGroup** *(string) --* 
        
            The path prefix for the S3 bucket where users’ persistent application settings are stored. You can allow the same persistent application settings to be used across multiple stacks by specifying the same settings group for each stack. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Stack\': {
                    \'Arn\': \'string\',
                    \'Name\': \'string\',
                    \'Description\': \'string\',
                    \'DisplayName\': \'string\',
                    \'CreatedTime\': datetime(2015, 1, 1),
                    \'StorageConnectors\': [
                        {
                            \'ConnectorType\': \'HOMEFOLDERS\'|\'GOOGLE_DRIVE\'|\'ONE_DRIVE\',
                            \'ResourceIdentifier\': \'string\',
                            \'Domains\': [
                                \'string\',
                            ]
                        },
                    ],
                    \'RedirectURL\': \'string\',
                    \'FeedbackURL\': \'string\',
                    \'StackErrors\': [
                        {
                            \'ErrorCode\': \'STORAGE_CONNECTOR_ERROR\'|\'INTERNAL_SERVICE_ERROR\',
                            \'ErrorMessage\': \'string\'
                        },
                    ],
                    \'UserSettings\': [
                        {
                            \'Action\': \'CLIPBOARD_COPY_FROM_LOCAL_DEVICE\'|\'CLIPBOARD_COPY_TO_LOCAL_DEVICE\'|\'FILE_UPLOAD\'|\'FILE_DOWNLOAD\'|\'PRINTING_TO_LOCAL_DEVICE\',
                            \'Permission\': \'ENABLED\'|\'DISABLED\'
                        },
                    ],
                    \'ApplicationSettings\': {
                        \'Enabled\': True|False,
                        \'SettingsGroup\': \'string\',
                        \'S3BucketName\': \'string\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Stack** *(dict) --* 
        
              Information about the stack.
        
              - **Arn** *(string) --* 
        
                The ARN of the stack.
        
              - **Name** *(string) --* 
        
                The name of the stack.
        
              - **Description** *(string) --* 
        
                The description for display.
        
              - **DisplayName** *(string) --* 
        
                The stack name for display.
        
              - **CreatedTime** *(datetime) --* 
        
                The time the stack was created.
        
              - **StorageConnectors** *(list) --* 
        
                The storage connectors to enable.
        
                - *(dict) --* 
        
                  Describes a connector to enable persistent storage for users.
        
                  - **ConnectorType** *(string) --* 
        
                    The type of storage connector.
        
                  - **ResourceIdentifier** *(string) --* 
        
                    The ARN of the storage connector.
        
                  - **Domains** *(list) --* 
        
                    The names of the domains for the G Suite account.
        
                    - *(string) --* GSuite domain for GDrive integration.
                
              - **RedirectURL** *(string) --* 
        
                The URL that users are redirected to after their streaming session ends.
        
              - **FeedbackURL** *(string) --* 
        
                The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.
        
              - **StackErrors** *(list) --* 
        
                The errors for the stack.
        
                - *(dict) --* 
        
                  Describes a stack error.
        
                  - **ErrorCode** *(string) --* 
        
                    The error code.
        
                  - **ErrorMessage** *(string) --* 
        
                    The error message.
        
              - **UserSettings** *(list) --* 
        
                The actions that are enabled or disabled for users during their streaming sessions. By default these actions are enabled.
        
                - *(dict) --* 
        
                  Describes an action and whether the action is enabled or disabled for users during their streaming sessions.
        
                  - **Action** *(string) --* 
        
                    The action that is enabled or disabled.
        
                  - **Permission** *(string) --* 
        
                    Indicates whether the action is enabled or disabled.
        
              - **ApplicationSettings** *(dict) --* 
        
                The persistent application settings for users of the stack.
        
                - **Enabled** *(boolean) --* 
        
                  Specifies whether persistent application settings are enabled for users during their streaming sessions.
        
                - **SettingsGroup** *(string) --* 
        
                  The path prefix for the S3 bucket where users’ persistent application settings are stored.
        
                - **S3BucketName** *(string) --* 
        
                  The S3 bucket where users’ persistent application settings are stored. When persistent application settings are enabled for the first time for an account in an AWS Region, an S3 bucket is created. The bucket is unique to the AWS account and the Region. 
        
        """
        pass

    def create_streaming_url(self, StackName: str, FleetName: str, UserId: str, ApplicationId: str = None, Validity: int = None, SessionContext: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/CreateStreamingURL>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_streaming_url(
              StackName=\'string\',
              FleetName=\'string\',
              UserId=\'string\',
              ApplicationId=\'string\',
              Validity=123,
              SessionContext=\'string\'
          )
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name of the stack.
        
        :type FleetName: string
        :param FleetName: **[REQUIRED]** 
        
          The name of the fleet.
        
        :type UserId: string
        :param UserId: **[REQUIRED]** 
        
          The ID of the user.
        
        :type ApplicationId: string
        :param ApplicationId: 
        
          The name of the application to launch after the session starts. This is the name that you specified as **Name** in the Image Assistant.
        
        :type Validity: integer
        :param Validity: 
        
          The time that the streaming URL will be valid, in seconds. Specify a value between 1 and 604800 seconds. The default is 60 seconds.
        
        :type SessionContext: string
        :param SessionContext: 
        
          The session context. For more information, see `Session Context <http://docs.aws.amazon.com/appstream2/latest/developerguide/managing-stacks-fleets.html#managing-stacks-fleets-parameters>`__ in the *Amazon AppStream 2.0 Developer Guide* .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StreamingURL\': \'string\',
                \'Expires\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **StreamingURL** *(string) --* 
        
              The URL to start the AppStream 2.0 streaming session.
        
            - **Expires** *(datetime) --* 
        
              The elapsed time, in seconds after the Unix epoch, when this URL expires.
        
        """
        pass

    def create_user(self, UserName: str, AuthenticationType: str, MessageAction: str = None, FirstName: str = None, LastName: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/CreateUser>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_user(
              UserName=\'string\',
              MessageAction=\'SUPPRESS\'|\'RESEND\',
              FirstName=\'string\',
              LastName=\'string\',
              AuthenticationType=\'API\'|\'SAML\'|\'USERPOOL\'
          )
        :type UserName: string
        :param UserName: **[REQUIRED]** 
        
          The email address of the user.
        
        :type MessageAction: string
        :param MessageAction: 
        
          The action to take for the welcome email that is sent to a user after the user is created in the user pool. If you specify SUPPRESS, no email is sent. If you specify RESEND, do not specify the first name or last name of the user. If the value is null, the email is sent. 
        
          .. note::
        
            The temporary password in the welcome email is valid for only 7 days. If users don’t set their passwords within 7 days, you must send them a new welcome email.
        
        :type FirstName: string
        :param FirstName: 
        
          The first name, or given name, of the user.
        
        :type LastName: string
        :param LastName: 
        
          The last name, or surname, of the user.
        
        :type AuthenticationType: string
        :param AuthenticationType: **[REQUIRED]** 
        
          The authentication type for the user. You must specify USERPOOL. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_directory_config(self, DirectoryName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DeleteDirectoryConfig>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_directory_config(
              DirectoryName=\'string\'
          )
        :type DirectoryName: string
        :param DirectoryName: **[REQUIRED]** 
        
          The name of the directory configuration.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_fleet(self, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DeleteFleet>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_fleet(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the fleet.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_image(self, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DeleteImage>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_image(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the image.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Image\': {
                    \'Name\': \'string\',
                    \'Arn\': \'string\',
                    \'BaseImageArn\': \'string\',
                    \'DisplayName\': \'string\',
                    \'State\': \'PENDING\'|\'AVAILABLE\'|\'FAILED\'|\'COPYING\'|\'DELETING\',
                    \'Visibility\': \'PUBLIC\'|\'PRIVATE\'|\'SHARED\',
                    \'ImageBuilderSupported\': True|False,
                    \'Platform\': \'WINDOWS\',
                    \'Description\': \'string\',
                    \'StateChangeReason\': {
                        \'Code\': \'INTERNAL_ERROR\'|\'IMAGE_BUILDER_NOT_AVAILABLE\'|\'IMAGE_COPY_FAILURE\',
                        \'Message\': \'string\'
                    },
                    \'Applications\': [
                        {
                            \'Name\': \'string\',
                            \'DisplayName\': \'string\',
                            \'IconURL\': \'string\',
                            \'LaunchPath\': \'string\',
                            \'LaunchParameters\': \'string\',
                            \'Enabled\': True|False,
                            \'Metadata\': {
                                \'string\': \'string\'
                            }
                        },
                    ],
                    \'CreatedTime\': datetime(2015, 1, 1),
                    \'PublicBaseImageReleasedDate\': datetime(2015, 1, 1),
                    \'AppstreamAgentVersion\': \'string\',
                    \'ImagePermissions\': {
                        \'allowFleet\': True|False,
                        \'allowImageBuilder\': True|False
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Image** *(dict) --* 
        
              Information about the image.
        
              - **Name** *(string) --* 
        
                The name of the image.
        
              - **Arn** *(string) --* 
        
                The ARN of the image.
        
              - **BaseImageArn** *(string) --* 
        
                The ARN of the image from which this image was created.
        
              - **DisplayName** *(string) --* 
        
                The image name for display.
        
              - **State** *(string) --* 
        
                The image starts in the ``PENDING`` state. If image creation succeeds, the state is ``AVAILABLE`` . If image creation fails, the state is ``FAILED`` .
        
              - **Visibility** *(string) --* 
        
                Indicates whether the image is public or private.
        
              - **ImageBuilderSupported** *(boolean) --* 
        
                Indicates whether an image builder can be launched from this image.
        
              - **Platform** *(string) --* 
        
                The operating system platform of the image.
        
              - **Description** *(string) --* 
        
                The description for display.
        
              - **StateChangeReason** *(dict) --* 
        
                The reason why the last state change occurred.
        
                - **Code** *(string) --* 
        
                  The state change reason code.
        
                - **Message** *(string) --* 
        
                  The state change reason message.
        
              - **Applications** *(list) --* 
        
                The applications associated with the image.
        
                - *(dict) --* 
        
                  Describes an application in the application catalog.
        
                  - **Name** *(string) --* 
        
                    The name of the application.
        
                  - **DisplayName** *(string) --* 
        
                    The application name for display.
        
                  - **IconURL** *(string) --* 
        
                    The URL for the application icon. This URL might be time-limited.
        
                  - **LaunchPath** *(string) --* 
        
                    The path to the application executable in the instance.
        
                  - **LaunchParameters** *(string) --* 
        
                    The arguments that are passed to the application at launch.
        
                  - **Enabled** *(boolean) --* 
        
                    If there is a problem, the application can be disabled after image creation.
        
                  - **Metadata** *(dict) --* 
        
                    Additional attributes that describe the application.
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
              - **CreatedTime** *(datetime) --* 
        
                The time the image was created.
        
              - **PublicBaseImageReleasedDate** *(datetime) --* 
        
                The release date of the public base image. For private images, this date is the release date of the base image from which the image was created.
        
              - **AppstreamAgentVersion** *(string) --* 
        
                The version of the AppStream 2.0 agent to use for instances that are launched from this image. 
        
              - **ImagePermissions** *(dict) --* 
        
                The permissions to provide to the destination AWS account for the specified image.
        
                - **allowFleet** *(boolean) --* 
        
                  Indicates whether the image can be used for a fleet.
        
                - **allowImageBuilder** *(boolean) --* 
        
                  Indicates whether the image can be used for an image builder.
        
        """
        pass

    def delete_image_builder(self, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DeleteImageBuilder>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_image_builder(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the image builder.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ImageBuilder\': {
                    \'Name\': \'string\',
                    \'Arn\': \'string\',
                    \'ImageArn\': \'string\',
                    \'Description\': \'string\',
                    \'DisplayName\': \'string\',
                    \'VpcConfig\': {
                        \'SubnetIds\': [
                            \'string\',
                        ],
                        \'SecurityGroupIds\': [
                            \'string\',
                        ]
                    },
                    \'InstanceType\': \'string\',
                    \'Platform\': \'WINDOWS\',
                    \'State\': \'PENDING\'|\'UPDATING_AGENT\'|\'RUNNING\'|\'STOPPING\'|\'STOPPED\'|\'REBOOTING\'|\'SNAPSHOTTING\'|\'DELETING\'|\'FAILED\',
                    \'StateChangeReason\': {
                        \'Code\': \'INTERNAL_ERROR\'|\'IMAGE_UNAVAILABLE\',
                        \'Message\': \'string\'
                    },
                    \'CreatedTime\': datetime(2015, 1, 1),
                    \'EnableDefaultInternetAccess\': True|False,
                    \'DomainJoinInfo\': {
                        \'DirectoryName\': \'string\',
                        \'OrganizationalUnitDistinguishedName\': \'string\'
                    },
                    \'ImageBuilderErrors\': [
                        {
                            \'ErrorCode\': \'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION\'|\'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION\'|\'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION\'|\'NETWORK_INTERFACE_LIMIT_EXCEEDED\'|\'INTERNAL_SERVICE_ERROR\'|\'IAM_SERVICE_ROLE_IS_MISSING\'|\'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES\'|\'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION\'|\'SUBNET_NOT_FOUND\'|\'IMAGE_NOT_FOUND\'|\'INVALID_SUBNET_CONFIGURATION\'|\'SECURITY_GROUPS_NOT_FOUND\'|\'IGW_NOT_ATTACHED\'|\'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION\'|\'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND\'|\'DOMAIN_JOIN_ERROR_ACCESS_DENIED\'|\'DOMAIN_JOIN_ERROR_LOGON_FAILURE\'|\'DOMAIN_JOIN_ERROR_INVALID_PARAMETER\'|\'DOMAIN_JOIN_ERROR_MORE_DATA\'|\'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN\'|\'DOMAIN_JOIN_ERROR_NOT_SUPPORTED\'|\'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME\'|\'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED\'|\'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED\'|\'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED\'|\'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR\',
                            \'ErrorMessage\': \'string\',
                            \'ErrorTimestamp\': datetime(2015, 1, 1)
                        },
                    ],
                    \'AppstreamAgentVersion\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ImageBuilder** *(dict) --* 
        
              Information about the image builder.
        
              - **Name** *(string) --* 
        
                The name of the image builder.
        
              - **Arn** *(string) --* 
        
                The ARN for the image builder.
        
              - **ImageArn** *(string) --* 
        
                The ARN of the image from which this builder was created.
        
              - **Description** *(string) --* 
        
                The description for display.
        
              - **DisplayName** *(string) --* 
        
                The image builder name for display.
        
              - **VpcConfig** *(dict) --* 
        
                The VPC configuration of the image builder.
        
                - **SubnetIds** *(list) --* 
        
                  The subnets to which a network interface is established from the fleet instance.
        
                  - *(string) --* 
              
                - **SecurityGroupIds** *(list) --* 
        
                  The security groups for the fleet.
        
                  - *(string) --* 
              
              - **InstanceType** *(string) --* 
        
                The instance type for the image builder.
        
              - **Platform** *(string) --* 
        
                The operating system platform of the image builder.
        
              - **State** *(string) --* 
        
                The state of the image builder.
        
              - **StateChangeReason** *(dict) --* 
        
                The reason why the last state change occurred.
        
                - **Code** *(string) --* 
        
                  The state change reason code.
        
                - **Message** *(string) --* 
        
                  The state change reason message.
        
              - **CreatedTime** *(datetime) --* 
        
                The time stamp when the image builder was created.
        
              - **EnableDefaultInternetAccess** *(boolean) --* 
        
                Enables or disables default internet access for the image builder.
        
              - **DomainJoinInfo** *(dict) --* 
        
                The information needed to join a Microsoft Active Directory domain.
        
                - **DirectoryName** *(string) --* 
        
                  The fully qualified name of the directory (for example, corp.example.com).
        
                - **OrganizationalUnitDistinguishedName** *(string) --* 
        
                  The distinguished name of the organizational unit for computer accounts.
        
              - **ImageBuilderErrors** *(list) --* 
        
                The image builder errors.
        
                - *(dict) --* 
        
                  Describes a resource error.
        
                  - **ErrorCode** *(string) --* 
        
                    The error code.
        
                  - **ErrorMessage** *(string) --* 
        
                    The error message.
        
                  - **ErrorTimestamp** *(datetime) --* 
        
                    The time the error occurred.
        
              - **AppstreamAgentVersion** *(string) --* 
        
                The version of the AppStream 2.0 agent that is currently being used by this image builder. 
        
        """
        pass

    def delete_image_permissions(self, Name: str, SharedAccountId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DeleteImagePermissions>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_image_permissions(
              Name=\'string\',
              SharedAccountId=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the private image.
        
        :type SharedAccountId: string
        :param SharedAccountId: **[REQUIRED]** 
        
          The 12-digit ID of the AWS account for which to delete image permissions.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_stack(self, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DeleteStack>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_stack(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the stack.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_user(self, UserName: str, AuthenticationType: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DeleteUser>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_user(
              UserName=\'string\',
              AuthenticationType=\'API\'|\'SAML\'|\'USERPOOL\'
          )
        :type UserName: string
        :param UserName: **[REQUIRED]** 
        
          The email address of the user.
        
        :type AuthenticationType: string
        :param AuthenticationType: **[REQUIRED]** 
        
          The authentication type for the user. You must specify USERPOOL.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def describe_directory_configs(self, DirectoryNames: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        Although the response syntax in this topic includes the account password, this password is not returned in the actual response.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeDirectoryConfigs>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_directory_configs(
              DirectoryNames=[
                  \'string\',
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
        :type DirectoryNames: list
        :param DirectoryNames: 
        
          The directory names.
        
          - *(string) --* 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum size of each page of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DirectoryConfigs\': [
                    {
                        \'DirectoryName\': \'string\',
                        \'OrganizationalUnitDistinguishedNames\': [
                            \'string\',
                        ],
                        \'ServiceAccountCredentials\': {
                            \'AccountName\': \'string\',
                            \'AccountPassword\': \'string\'
                        },
                        \'CreatedTime\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DirectoryConfigs** *(list) --* 
        
              Information about the directory configurations. Note that although the response syntax in this topic includes the account password, this password is not returned in the actual response. 
        
              - *(dict) --* 
        
                Configuration information for the directory used to join domains.
        
                - **DirectoryName** *(string) --* 
        
                  The fully qualified name of the directory (for example, corp.example.com).
        
                - **OrganizationalUnitDistinguishedNames** *(list) --* 
        
                  The distinguished names of the organizational units for computer accounts.
        
                  - *(string) --* 
              
                - **ServiceAccountCredentials** *(dict) --* 
        
                  The credentials for the service account used by the streaming instance to connect to the directory.
        
                  - **AccountName** *(string) --* 
        
                    The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.
        
                  - **AccountPassword** *(string) --* 
        
                    The password for the account.
        
                - **CreatedTime** *(datetime) --* 
        
                  The time the directory configuration was created.
        
            - **NextToken** *(string) --* 
        
              The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
        
        """
        pass

    def describe_fleets(self, Names: List = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeFleets>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_fleets(
              Names=[
                  \'string\',
              ],
              NextToken=\'string\'
          )
        :type Names: list
        :param Names: 
        
          The names of the fleets to describe.
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Fleets\': [
                    {
                        \'Arn\': \'string\',
                        \'Name\': \'string\',
                        \'DisplayName\': \'string\',
                        \'Description\': \'string\',
                        \'ImageName\': \'string\',
                        \'ImageArn\': \'string\',
                        \'InstanceType\': \'string\',
                        \'FleetType\': \'ALWAYS_ON\'|\'ON_DEMAND\',
                        \'ComputeCapacityStatus\': {
                            \'Desired\': 123,
                            \'Running\': 123,
                            \'InUse\': 123,
                            \'Available\': 123
                        },
                        \'MaxUserDurationInSeconds\': 123,
                        \'DisconnectTimeoutInSeconds\': 123,
                        \'State\': \'STARTING\'|\'RUNNING\'|\'STOPPING\'|\'STOPPED\',
                        \'VpcConfig\': {
                            \'SubnetIds\': [
                                \'string\',
                            ],
                            \'SecurityGroupIds\': [
                                \'string\',
                            ]
                        },
                        \'CreatedTime\': datetime(2015, 1, 1),
                        \'FleetErrors\': [
                            {
                                \'ErrorCode\': \'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION\'|\'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION\'|\'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION\'|\'NETWORK_INTERFACE_LIMIT_EXCEEDED\'|\'INTERNAL_SERVICE_ERROR\'|\'IAM_SERVICE_ROLE_IS_MISSING\'|\'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES\'|\'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION\'|\'SUBNET_NOT_FOUND\'|\'IMAGE_NOT_FOUND\'|\'INVALID_SUBNET_CONFIGURATION\'|\'SECURITY_GROUPS_NOT_FOUND\'|\'IGW_NOT_ATTACHED\'|\'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION\'|\'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND\'|\'DOMAIN_JOIN_ERROR_ACCESS_DENIED\'|\'DOMAIN_JOIN_ERROR_LOGON_FAILURE\'|\'DOMAIN_JOIN_ERROR_INVALID_PARAMETER\'|\'DOMAIN_JOIN_ERROR_MORE_DATA\'|\'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN\'|\'DOMAIN_JOIN_ERROR_NOT_SUPPORTED\'|\'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME\'|\'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED\'|\'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED\'|\'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED\'|\'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR\',
                                \'ErrorMessage\': \'string\'
                            },
                        ],
                        \'EnableDefaultInternetAccess\': True|False,
                        \'DomainJoinInfo\': {
                            \'DirectoryName\': \'string\',
                            \'OrganizationalUnitDistinguishedName\': \'string\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Fleets** *(list) --* 
        
              Information about the fleets.
        
              - *(dict) --* 
        
                Contains the parameters for a fleet.
        
                - **Arn** *(string) --* 
        
                  The ARN for the fleet.
        
                - **Name** *(string) --* 
        
                  The name of the fleet.
        
                - **DisplayName** *(string) --* 
        
                  The fleet name for display.
        
                - **Description** *(string) --* 
        
                  The description for display.
        
                - **ImageName** *(string) --* 
        
                  The name of the image used to create the fleet.
        
                - **ImageArn** *(string) --* 
        
                  The ARN for the public, private, or shared image.
        
                - **InstanceType** *(string) --* 
        
                  The instance type to use when launching fleet instances.
        
                - **FleetType** *(string) --* 
        
                  The fleet type.
        
                    ALWAYS_ON  
        
                  Provides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps.
        
                    ON_DEMAND  
        
                  Provide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps.
        
                - **ComputeCapacityStatus** *(dict) --* 
        
                  The capacity status for the fleet.
        
                  - **Desired** *(integer) --* 
        
                    The desired number of streaming instances.
        
                  - **Running** *(integer) --* 
        
                    The total number of simultaneous streaming instances that are running.
        
                  - **InUse** *(integer) --* 
        
                    The number of instances in use for streaming.
        
                  - **Available** *(integer) --* 
        
                    The number of currently available instances that can be used to stream sessions.
        
                - **MaxUserDurationInSeconds** *(integer) --* 
        
                  The maximum time that a streaming session can run, in seconds. Specify a value between 600 and 57600.
        
                - **DisconnectTimeoutInSeconds** *(integer) --* 
        
                  The time after disconnection when a session is considered to have ended, in seconds. If a user who was disconnected reconnects within this time interval, the user is connected to their previous session. Specify a value between 60 and 57600.
        
                - **State** *(string) --* 
        
                  The current state for the fleet.
        
                - **VpcConfig** *(dict) --* 
        
                  The VPC configuration for the fleet.
        
                  - **SubnetIds** *(list) --* 
        
                    The subnets to which a network interface is established from the fleet instance.
        
                    - *(string) --* 
                
                  - **SecurityGroupIds** *(list) --* 
        
                    The security groups for the fleet.
        
                    - *(string) --* 
                
                - **CreatedTime** *(datetime) --* 
        
                  The time the fleet was created.
        
                - **FleetErrors** *(list) --* 
        
                  The fleet errors.
        
                  - *(dict) --* 
        
                    Describes a fleet error.
        
                    - **ErrorCode** *(string) --* 
        
                      The error code.
        
                    - **ErrorMessage** *(string) --* 
        
                      The error message.
        
                - **EnableDefaultInternetAccess** *(boolean) --* 
        
                  Indicates whether default internet access is enabled for the fleet.
        
                - **DomainJoinInfo** *(dict) --* 
        
                  The information needed to join a Microsoft Active Directory domain.
        
                  - **DirectoryName** *(string) --* 
        
                    The fully qualified name of the directory (for example, corp.example.com).
        
                  - **OrganizationalUnitDistinguishedName** *(string) --* 
        
                    The distinguished name of the organizational unit for computer accounts.
        
            - **NextToken** *(string) --* 
        
              The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
        
        """
        pass

    def describe_image_builders(self, Names: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeImageBuilders>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_image_builders(
              Names=[
                  \'string\',
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
        :type Names: list
        :param Names: 
        
          The names of the image builders to describe.
        
          - *(string) --* 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum size of each page of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ImageBuilders\': [
                    {
                        \'Name\': \'string\',
                        \'Arn\': \'string\',
                        \'ImageArn\': \'string\',
                        \'Description\': \'string\',
                        \'DisplayName\': \'string\',
                        \'VpcConfig\': {
                            \'SubnetIds\': [
                                \'string\',
                            ],
                            \'SecurityGroupIds\': [
                                \'string\',
                            ]
                        },
                        \'InstanceType\': \'string\',
                        \'Platform\': \'WINDOWS\',
                        \'State\': \'PENDING\'|\'UPDATING_AGENT\'|\'RUNNING\'|\'STOPPING\'|\'STOPPED\'|\'REBOOTING\'|\'SNAPSHOTTING\'|\'DELETING\'|\'FAILED\',
                        \'StateChangeReason\': {
                            \'Code\': \'INTERNAL_ERROR\'|\'IMAGE_UNAVAILABLE\',
                            \'Message\': \'string\'
                        },
                        \'CreatedTime\': datetime(2015, 1, 1),
                        \'EnableDefaultInternetAccess\': True|False,
                        \'DomainJoinInfo\': {
                            \'DirectoryName\': \'string\',
                            \'OrganizationalUnitDistinguishedName\': \'string\'
                        },
                        \'ImageBuilderErrors\': [
                            {
                                \'ErrorCode\': \'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION\'|\'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION\'|\'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION\'|\'NETWORK_INTERFACE_LIMIT_EXCEEDED\'|\'INTERNAL_SERVICE_ERROR\'|\'IAM_SERVICE_ROLE_IS_MISSING\'|\'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES\'|\'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION\'|\'SUBNET_NOT_FOUND\'|\'IMAGE_NOT_FOUND\'|\'INVALID_SUBNET_CONFIGURATION\'|\'SECURITY_GROUPS_NOT_FOUND\'|\'IGW_NOT_ATTACHED\'|\'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION\'|\'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND\'|\'DOMAIN_JOIN_ERROR_ACCESS_DENIED\'|\'DOMAIN_JOIN_ERROR_LOGON_FAILURE\'|\'DOMAIN_JOIN_ERROR_INVALID_PARAMETER\'|\'DOMAIN_JOIN_ERROR_MORE_DATA\'|\'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN\'|\'DOMAIN_JOIN_ERROR_NOT_SUPPORTED\'|\'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME\'|\'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED\'|\'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED\'|\'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED\'|\'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR\',
                                \'ErrorMessage\': \'string\',
                                \'ErrorTimestamp\': datetime(2015, 1, 1)
                            },
                        ],
                        \'AppstreamAgentVersion\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ImageBuilders** *(list) --* 
        
              Information about the image builders.
        
              - *(dict) --* 
        
                Describes a streaming instance used for editing an image. New images are created from a snapshot through an image builder.
        
                - **Name** *(string) --* 
        
                  The name of the image builder.
        
                - **Arn** *(string) --* 
        
                  The ARN for the image builder.
        
                - **ImageArn** *(string) --* 
        
                  The ARN of the image from which this builder was created.
        
                - **Description** *(string) --* 
        
                  The description for display.
        
                - **DisplayName** *(string) --* 
        
                  The image builder name for display.
        
                - **VpcConfig** *(dict) --* 
        
                  The VPC configuration of the image builder.
        
                  - **SubnetIds** *(list) --* 
        
                    The subnets to which a network interface is established from the fleet instance.
        
                    - *(string) --* 
                
                  - **SecurityGroupIds** *(list) --* 
        
                    The security groups for the fleet.
        
                    - *(string) --* 
                
                - **InstanceType** *(string) --* 
        
                  The instance type for the image builder.
        
                - **Platform** *(string) --* 
        
                  The operating system platform of the image builder.
        
                - **State** *(string) --* 
        
                  The state of the image builder.
        
                - **StateChangeReason** *(dict) --* 
        
                  The reason why the last state change occurred.
        
                  - **Code** *(string) --* 
        
                    The state change reason code.
        
                  - **Message** *(string) --* 
        
                    The state change reason message.
        
                - **CreatedTime** *(datetime) --* 
        
                  The time stamp when the image builder was created.
        
                - **EnableDefaultInternetAccess** *(boolean) --* 
        
                  Enables or disables default internet access for the image builder.
        
                - **DomainJoinInfo** *(dict) --* 
        
                  The information needed to join a Microsoft Active Directory domain.
        
                  - **DirectoryName** *(string) --* 
        
                    The fully qualified name of the directory (for example, corp.example.com).
        
                  - **OrganizationalUnitDistinguishedName** *(string) --* 
        
                    The distinguished name of the organizational unit for computer accounts.
        
                - **ImageBuilderErrors** *(list) --* 
        
                  The image builder errors.
        
                  - *(dict) --* 
        
                    Describes a resource error.
        
                    - **ErrorCode** *(string) --* 
        
                      The error code.
        
                    - **ErrorMessage** *(string) --* 
        
                      The error message.
        
                    - **ErrorTimestamp** *(datetime) --* 
        
                      The time the error occurred.
        
                - **AppstreamAgentVersion** *(string) --* 
        
                  The version of the AppStream 2.0 agent that is currently being used by this image builder. 
        
            - **NextToken** *(string) --* 
        
              The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
        
        """
        pass

    def describe_image_permissions(self, Name: str, MaxResults: int = None, SharedAwsAccountIds: List = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeImagePermissions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_image_permissions(
              Name=\'string\',
              MaxResults=123,
              SharedAwsAccountIds=[
                  \'string\',
              ],
              NextToken=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the private image for which to describe permissions. The image must be one that you own. 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum size of each page of results.
        
        :type SharedAwsAccountIds: list
        :param SharedAwsAccountIds: 
        
          The 12-digit ID of one or more AWS accounts with which the image is shared.
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Name\': \'string\',
                \'SharedImagePermissionsList\': [
                    {
                        \'sharedAccountId\': \'string\',
                        \'imagePermissions\': {
                            \'allowFleet\': True|False,
                            \'allowImageBuilder\': True|False
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Name** *(string) --* 
        
              The name of the private image.
        
            - **SharedImagePermissionsList** *(list) --* 
        
              The permissions for a private image that you own. 
        
              - *(dict) --* 
        
                Describes the permissions that are available to the specified AWS account for a shared image.
        
                - **sharedAccountId** *(string) --* 
        
                  The 12-digit ID of the AWS account with which the image is shared.
        
                - **imagePermissions** *(dict) --* 
        
                  Describes the permissions for a shared image.
        
                  - **allowFleet** *(boolean) --* 
        
                    Indicates whether the image can be used for a fleet.
        
                  - **allowImageBuilder** *(boolean) --* 
        
                    Indicates whether the image can be used for an image builder.
        
            - **NextToken** *(string) --* 
        
              The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
        
        """
        pass

    def describe_images(self, Names: List = None, Arns: List = None, Type: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeImages>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_images(
              Names=[
                  \'string\',
              ],
              Arns=[
                  \'string\',
              ],
              Type=\'PUBLIC\'|\'PRIVATE\'|\'SHARED\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type Names: list
        :param Names: 
        
          The names of the public or private images to describe.
        
          - *(string) --* 
        
        :type Arns: list
        :param Arns: 
        
          The ARNs of the public, private, and shared images to describe.
        
          - *(string) --* 
        
        :type Type: string
        :param Type: 
        
          The type of image (public, private, or shared) to describe. 
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum size of each page of results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Images\': [
                    {
                        \'Name\': \'string\',
                        \'Arn\': \'string\',
                        \'BaseImageArn\': \'string\',
                        \'DisplayName\': \'string\',
                        \'State\': \'PENDING\'|\'AVAILABLE\'|\'FAILED\'|\'COPYING\'|\'DELETING\',
                        \'Visibility\': \'PUBLIC\'|\'PRIVATE\'|\'SHARED\',
                        \'ImageBuilderSupported\': True|False,
                        \'Platform\': \'WINDOWS\',
                        \'Description\': \'string\',
                        \'StateChangeReason\': {
                            \'Code\': \'INTERNAL_ERROR\'|\'IMAGE_BUILDER_NOT_AVAILABLE\'|\'IMAGE_COPY_FAILURE\',
                            \'Message\': \'string\'
                        },
                        \'Applications\': [
                            {
                                \'Name\': \'string\',
                                \'DisplayName\': \'string\',
                                \'IconURL\': \'string\',
                                \'LaunchPath\': \'string\',
                                \'LaunchParameters\': \'string\',
                                \'Enabled\': True|False,
                                \'Metadata\': {
                                    \'string\': \'string\'
                                }
                            },
                        ],
                        \'CreatedTime\': datetime(2015, 1, 1),
                        \'PublicBaseImageReleasedDate\': datetime(2015, 1, 1),
                        \'AppstreamAgentVersion\': \'string\',
                        \'ImagePermissions\': {
                            \'allowFleet\': True|False,
                            \'allowImageBuilder\': True|False
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Images** *(list) --* 
        
              Information about the images.
        
              - *(dict) --* 
        
                Describes an image.
        
                - **Name** *(string) --* 
        
                  The name of the image.
        
                - **Arn** *(string) --* 
        
                  The ARN of the image.
        
                - **BaseImageArn** *(string) --* 
        
                  The ARN of the image from which this image was created.
        
                - **DisplayName** *(string) --* 
        
                  The image name for display.
        
                - **State** *(string) --* 
        
                  The image starts in the ``PENDING`` state. If image creation succeeds, the state is ``AVAILABLE`` . If image creation fails, the state is ``FAILED`` .
        
                - **Visibility** *(string) --* 
        
                  Indicates whether the image is public or private.
        
                - **ImageBuilderSupported** *(boolean) --* 
        
                  Indicates whether an image builder can be launched from this image.
        
                - **Platform** *(string) --* 
        
                  The operating system platform of the image.
        
                - **Description** *(string) --* 
        
                  The description for display.
        
                - **StateChangeReason** *(dict) --* 
        
                  The reason why the last state change occurred.
        
                  - **Code** *(string) --* 
        
                    The state change reason code.
        
                  - **Message** *(string) --* 
        
                    The state change reason message.
        
                - **Applications** *(list) --* 
        
                  The applications associated with the image.
        
                  - *(dict) --* 
        
                    Describes an application in the application catalog.
        
                    - **Name** *(string) --* 
        
                      The name of the application.
        
                    - **DisplayName** *(string) --* 
        
                      The application name for display.
        
                    - **IconURL** *(string) --* 
        
                      The URL for the application icon. This URL might be time-limited.
        
                    - **LaunchPath** *(string) --* 
        
                      The path to the application executable in the instance.
        
                    - **LaunchParameters** *(string) --* 
        
                      The arguments that are passed to the application at launch.
        
                    - **Enabled** *(boolean) --* 
        
                      If there is a problem, the application can be disabled after image creation.
        
                    - **Metadata** *(dict) --* 
        
                      Additional attributes that describe the application.
        
                      - *(string) --* 
                        
                        - *(string) --* 
                  
                - **CreatedTime** *(datetime) --* 
        
                  The time the image was created.
        
                - **PublicBaseImageReleasedDate** *(datetime) --* 
        
                  The release date of the public base image. For private images, this date is the release date of the base image from which the image was created.
        
                - **AppstreamAgentVersion** *(string) --* 
        
                  The version of the AppStream 2.0 agent to use for instances that are launched from this image. 
        
                - **ImagePermissions** *(dict) --* 
        
                  The permissions to provide to the destination AWS account for the specified image.
        
                  - **allowFleet** *(boolean) --* 
        
                    Indicates whether the image can be used for a fleet.
        
                  - **allowImageBuilder** *(boolean) --* 
        
                    Indicates whether the image can be used for an image builder.
        
            - **NextToken** *(string) --* 
        
              The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
        
        """
        pass

    def describe_sessions(self, StackName: str, FleetName: str, UserId: str = None, NextToken: str = None, Limit: int = None, AuthenticationType: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeSessions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_sessions(
              StackName=\'string\',
              FleetName=\'string\',
              UserId=\'string\',
              NextToken=\'string\',
              Limit=123,
              AuthenticationType=\'API\'|\'SAML\'|\'USERPOOL\'
          )
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name of the stack. This value is case-sensitive.
        
        :type FleetName: string
        :param FleetName: **[REQUIRED]** 
        
          The name of the fleet. This value is case-sensitive.
        
        :type UserId: string
        :param UserId: 
        
          The user ID.
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
        
        :type Limit: integer
        :param Limit: 
        
          The size of each page of results. The default value is 20 and the maximum value is 50.
        
        :type AuthenticationType: string
        :param AuthenticationType: 
        
          The authentication method. Specify ``API`` for a user authenticated using a streaming URL or ``SAML`` for a SAML federated user. The default is to authenticate users using a streaming URL.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Sessions\': [
                    {
                        \'Id\': \'string\',
                        \'UserId\': \'string\',
                        \'StackName\': \'string\',
                        \'FleetName\': \'string\',
                        \'State\': \'ACTIVE\'|\'PENDING\'|\'EXPIRED\',
                        \'AuthenticationType\': \'API\'|\'SAML\'|\'USERPOOL\',
                        \'NetworkAccessConfiguration\': {
                            \'EniPrivateIpAddress\': \'string\',
                            \'EniId\': \'string\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Sessions** *(list) --* 
        
              Information about the streaming sessions.
        
              - *(dict) --* 
        
                Describes a streaming session.
        
                - **Id** *(string) --* 
        
                  The ID of the streaming session.
        
                - **UserId** *(string) --* 
        
                  The identifier of the user for whom the session was created.
        
                - **StackName** *(string) --* 
        
                  The name of the stack for the streaming session.
        
                - **FleetName** *(string) --* 
        
                  The name of the fleet for the streaming session.
        
                - **State** *(string) --* 
        
                  The current state of the streaming session.
        
                - **AuthenticationType** *(string) --* 
        
                  The authentication method. The user is authenticated using a streaming URL (``API`` ) or SAML federation (``SAML`` ).
        
                - **NetworkAccessConfiguration** *(dict) --* 
        
                  The network details for the streaming session.
        
                  - **EniPrivateIpAddress** *(string) --* 
        
                    The private IP address of the elastic network interface that is attached to instances in your VPC.
        
                  - **EniId** *(string) --* 
        
                    The resource identifier of the elastic network interface that is attached to instances in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.
        
            - **NextToken** *(string) --* 
        
              The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
        
        """
        pass

    def describe_stacks(self, Names: List = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeStacks>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_stacks(
              Names=[
                  \'string\',
              ],
              NextToken=\'string\'
          )
        :type Names: list
        :param Names: 
        
          The names of the stacks to describe.
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Stacks\': [
                    {
                        \'Arn\': \'string\',
                        \'Name\': \'string\',
                        \'Description\': \'string\',
                        \'DisplayName\': \'string\',
                        \'CreatedTime\': datetime(2015, 1, 1),
                        \'StorageConnectors\': [
                            {
                                \'ConnectorType\': \'HOMEFOLDERS\'|\'GOOGLE_DRIVE\'|\'ONE_DRIVE\',
                                \'ResourceIdentifier\': \'string\',
                                \'Domains\': [
                                    \'string\',
                                ]
                            },
                        ],
                        \'RedirectURL\': \'string\',
                        \'FeedbackURL\': \'string\',
                        \'StackErrors\': [
                            {
                                \'ErrorCode\': \'STORAGE_CONNECTOR_ERROR\'|\'INTERNAL_SERVICE_ERROR\',
                                \'ErrorMessage\': \'string\'
                            },
                        ],
                        \'UserSettings\': [
                            {
                                \'Action\': \'CLIPBOARD_COPY_FROM_LOCAL_DEVICE\'|\'CLIPBOARD_COPY_TO_LOCAL_DEVICE\'|\'FILE_UPLOAD\'|\'FILE_DOWNLOAD\'|\'PRINTING_TO_LOCAL_DEVICE\',
                                \'Permission\': \'ENABLED\'|\'DISABLED\'
                            },
                        ],
                        \'ApplicationSettings\': {
                            \'Enabled\': True|False,
                            \'SettingsGroup\': \'string\',
                            \'S3BucketName\': \'string\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Stacks** *(list) --* 
        
              Information about the stacks.
        
              - *(dict) --* 
        
                Describes a stack.
        
                - **Arn** *(string) --* 
        
                  The ARN of the stack.
        
                - **Name** *(string) --* 
        
                  The name of the stack.
        
                - **Description** *(string) --* 
        
                  The description for display.
        
                - **DisplayName** *(string) --* 
        
                  The stack name for display.
        
                - **CreatedTime** *(datetime) --* 
        
                  The time the stack was created.
        
                - **StorageConnectors** *(list) --* 
        
                  The storage connectors to enable.
        
                  - *(dict) --* 
        
                    Describes a connector to enable persistent storage for users.
        
                    - **ConnectorType** *(string) --* 
        
                      The type of storage connector.
        
                    - **ResourceIdentifier** *(string) --* 
        
                      The ARN of the storage connector.
        
                    - **Domains** *(list) --* 
        
                      The names of the domains for the G Suite account.
        
                      - *(string) --* GSuite domain for GDrive integration.
                  
                - **RedirectURL** *(string) --* 
        
                  The URL that users are redirected to after their streaming session ends.
        
                - **FeedbackURL** *(string) --* 
        
                  The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.
        
                - **StackErrors** *(list) --* 
        
                  The errors for the stack.
        
                  - *(dict) --* 
        
                    Describes a stack error.
        
                    - **ErrorCode** *(string) --* 
        
                      The error code.
        
                    - **ErrorMessage** *(string) --* 
        
                      The error message.
        
                - **UserSettings** *(list) --* 
        
                  The actions that are enabled or disabled for users during their streaming sessions. By default these actions are enabled.
        
                  - *(dict) --* 
        
                    Describes an action and whether the action is enabled or disabled for users during their streaming sessions.
        
                    - **Action** *(string) --* 
        
                      The action that is enabled or disabled.
        
                    - **Permission** *(string) --* 
        
                      Indicates whether the action is enabled or disabled.
        
                - **ApplicationSettings** *(dict) --* 
        
                  The persistent application settings for users of the stack.
        
                  - **Enabled** *(boolean) --* 
        
                    Specifies whether persistent application settings are enabled for users during their streaming sessions.
        
                  - **SettingsGroup** *(string) --* 
        
                    The path prefix for the S3 bucket where users’ persistent application settings are stored.
        
                  - **S3BucketName** *(string) --* 
        
                    The S3 bucket where users’ persistent application settings are stored. When persistent application settings are enabled for the first time for an account in an AWS Region, an S3 bucket is created. The bucket is unique to the AWS account and the Region. 
        
            - **NextToken** *(string) --* 
        
              The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
        
        """
        pass

    def describe_user_stack_associations(self, StackName: str = None, UserName: str = None, AuthenticationType: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Retrieves a list that describes the UserStackAssociation objects. You must specify either or both of the following:
        
        * The stack name 
         
        * The user name (email address of the user associated with the stack) and the authentication type for the user 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeUserStackAssociations>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_user_stack_associations(
              StackName=\'string\',
              UserName=\'string\',
              AuthenticationType=\'API\'|\'SAML\'|\'USERPOOL\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type StackName: string
        :param StackName: 
        
          The name of the stack that is associated with the user.
        
        :type UserName: string
        :param UserName: 
        
          The email address of the user who is associated with the stack.
        
        :type AuthenticationType: string
        :param AuthenticationType: 
        
          The authentication type for the user who is associated with the stack. You must specify USERPOOL.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum size of each page of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UserStackAssociations\': [
                    {
                        \'StackName\': \'string\',
                        \'UserName\': \'string\',
                        \'AuthenticationType\': \'API\'|\'SAML\'|\'USERPOOL\',
                        \'SendEmailNotification\': True|False
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **UserStackAssociations** *(list) --* 
        
              The UserStackAssociation objects.
        
              - *(dict) --* 
        
                Describes a user in the user pool and the associated stack.
        
                - **StackName** *(string) --* 
        
                  The name of the stack that is associated with the user.
        
                - **UserName** *(string) --* 
        
                  The email address of the user who is associated with the stack.
        
                - **AuthenticationType** *(string) --* 
        
                  The authentication type for the user.
        
                - **SendEmailNotification** *(boolean) --* 
        
                  Specifies whether a welcome email is sent to a user after the user is created in the user pool.
        
            - **NextToken** *(string) --* 
        
              The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
        
        """
        pass

    def describe_users(self, AuthenticationType: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeUsers>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_users(
              AuthenticationType=\'API\'|\'SAML\'|\'USERPOOL\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type AuthenticationType: string
        :param AuthenticationType: **[REQUIRED]** 
        
          The authentication type for the users in the user pool to describe. You must specify USERPOOL.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum size of each page of results.
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Users\': [
                    {
                        \'Arn\': \'string\',
                        \'UserName\': \'string\',
                        \'Enabled\': True|False,
                        \'Status\': \'string\',
                        \'FirstName\': \'string\',
                        \'LastName\': \'string\',
                        \'CreatedTime\': datetime(2015, 1, 1),
                        \'AuthenticationType\': \'API\'|\'SAML\'|\'USERPOOL\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Users** *(list) --* 
        
              Information about users in the user pool.
        
              - *(dict) --* 
        
                Describes a user in the user pool.
        
                - **Arn** *(string) --* 
        
                  The ARN of the user.
        
                - **UserName** *(string) --* 
        
                  The email address of the user.
        
                - **Enabled** *(boolean) --* 
        
                  Specifies whether the user in the user pool is enabled.
        
                - **Status** *(string) --* 
        
                  The status of the user in the user pool. The status can be one of the following:
        
                  * UNCONFIRMED – The user is created but not confirmed. 
                   
                  * CONFIRMED – The user is confirmed. 
                   
                  * ARCHIVED – The user is no longer active. 
                   
                  * COMPROMISED – The user is disabled because of a potential security threat. 
                   
                  * UNKNOWN – The user status is not known. 
                   
                - **FirstName** *(string) --* 
        
                  The first name, or given name, of the user.
        
                - **LastName** *(string) --* 
        
                  The last name, or surname, of the user.
        
                - **CreatedTime** *(datetime) --* 
        
                  The date and time the user was created in the user pool.
        
                - **AuthenticationType** *(string) --* 
        
                  The authentication type for the user.
        
            - **NextToken** *(string) --* 
        
              The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
        
        """
        pass

    def disable_user(self, UserName: str, AuthenticationType: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DisableUser>`_
        
        **Request Syntax** 
        ::
        
          response = client.disable_user(
              UserName=\'string\',
              AuthenticationType=\'API\'|\'SAML\'|\'USERPOOL\'
          )
        :type UserName: string
        :param UserName: **[REQUIRED]** 
        
          The email address of the user.
        
        :type AuthenticationType: string
        :param AuthenticationType: **[REQUIRED]** 
        
          The authentication type for the user. You must specify USERPOOL.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def disassociate_fleet(self, FleetName: str, StackName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DisassociateFleet>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_fleet(
              FleetName=\'string\',
              StackName=\'string\'
          )
        :type FleetName: string
        :param FleetName: **[REQUIRED]** 
        
          The name of the fleet.
        
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name of the stack.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def enable_user(self, UserName: str, AuthenticationType: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/EnableUser>`_
        
        **Request Syntax** 
        ::
        
          response = client.enable_user(
              UserName=\'string\',
              AuthenticationType=\'API\'|\'SAML\'|\'USERPOOL\'
          )
        :type UserName: string
        :param UserName: **[REQUIRED]** 
        
          The email address of the user.
        
        :type AuthenticationType: string
        :param AuthenticationType: **[REQUIRED]** 
        
          The authentication type for the user. You must specify USERPOOL.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def expire_session(self, SessionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/ExpireSession>`_
        
        **Request Syntax** 
        ::
        
          response = client.expire_session(
              SessionId=\'string\'
          )
        :type SessionId: string
        :param SessionId: **[REQUIRED]** 
        
          The ID of the streaming session.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
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

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def list_associated_fleets(self, StackName: str, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/ListAssociatedFleets>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_associated_fleets(
              StackName=\'string\',
              NextToken=\'string\'
          )
        :type StackName: string
        :param StackName: **[REQUIRED]** 
        
          The name of the stack.
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Names\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Names** *(list) --* 
        
              The name of the fleet.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
        
        """
        pass

    def list_associated_stacks(self, FleetName: str, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/ListAssociatedStacks>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_associated_stacks(
              FleetName=\'string\',
              NextToken=\'string\'
          )
        :type FleetName: string
        :param FleetName: **[REQUIRED]** 
        
          The name of the fleet.
        
        :type NextToken: string
        :param NextToken: 
        
          The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Names\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Names** *(list) --* 
        
              The name of the stack.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
        
        """
        pass

    def list_tags_for_resource(self, ResourceArn: str) -> Dict:
        """
        
        For more information about tags, see `Tagging Your Resources <http://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html>`__ in the *Amazon AppStream 2.0 Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/ListTagsForResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags_for_resource(
              ResourceArn=\'string\'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the resource.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Tags\': {
                    \'string\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Tags** *(dict) --* 
        
              The information about the tags.
        
              - *(string) --* 
                
                - *(string) --* 
          
        """
        pass

    def start_fleet(self, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/StartFleet>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_fleet(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the fleet.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def start_image_builder(self, Name: str, AppstreamAgentVersion: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/StartImageBuilder>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_image_builder(
              Name=\'string\',
              AppstreamAgentVersion=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the image builder.
        
        :type AppstreamAgentVersion: string
        :param AppstreamAgentVersion: 
        
          The version of the AppStream 2.0 agent to use for this image builder. To use the latest version of the AppStream 2.0 agent, specify [LATEST]. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ImageBuilder\': {
                    \'Name\': \'string\',
                    \'Arn\': \'string\',
                    \'ImageArn\': \'string\',
                    \'Description\': \'string\',
                    \'DisplayName\': \'string\',
                    \'VpcConfig\': {
                        \'SubnetIds\': [
                            \'string\',
                        ],
                        \'SecurityGroupIds\': [
                            \'string\',
                        ]
                    },
                    \'InstanceType\': \'string\',
                    \'Platform\': \'WINDOWS\',
                    \'State\': \'PENDING\'|\'UPDATING_AGENT\'|\'RUNNING\'|\'STOPPING\'|\'STOPPED\'|\'REBOOTING\'|\'SNAPSHOTTING\'|\'DELETING\'|\'FAILED\',
                    \'StateChangeReason\': {
                        \'Code\': \'INTERNAL_ERROR\'|\'IMAGE_UNAVAILABLE\',
                        \'Message\': \'string\'
                    },
                    \'CreatedTime\': datetime(2015, 1, 1),
                    \'EnableDefaultInternetAccess\': True|False,
                    \'DomainJoinInfo\': {
                        \'DirectoryName\': \'string\',
                        \'OrganizationalUnitDistinguishedName\': \'string\'
                    },
                    \'ImageBuilderErrors\': [
                        {
                            \'ErrorCode\': \'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION\'|\'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION\'|\'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION\'|\'NETWORK_INTERFACE_LIMIT_EXCEEDED\'|\'INTERNAL_SERVICE_ERROR\'|\'IAM_SERVICE_ROLE_IS_MISSING\'|\'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES\'|\'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION\'|\'SUBNET_NOT_FOUND\'|\'IMAGE_NOT_FOUND\'|\'INVALID_SUBNET_CONFIGURATION\'|\'SECURITY_GROUPS_NOT_FOUND\'|\'IGW_NOT_ATTACHED\'|\'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION\'|\'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND\'|\'DOMAIN_JOIN_ERROR_ACCESS_DENIED\'|\'DOMAIN_JOIN_ERROR_LOGON_FAILURE\'|\'DOMAIN_JOIN_ERROR_INVALID_PARAMETER\'|\'DOMAIN_JOIN_ERROR_MORE_DATA\'|\'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN\'|\'DOMAIN_JOIN_ERROR_NOT_SUPPORTED\'|\'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME\'|\'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED\'|\'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED\'|\'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED\'|\'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR\',
                            \'ErrorMessage\': \'string\',
                            \'ErrorTimestamp\': datetime(2015, 1, 1)
                        },
                    ],
                    \'AppstreamAgentVersion\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ImageBuilder** *(dict) --* 
        
              Information about the image builder.
        
              - **Name** *(string) --* 
        
                The name of the image builder.
        
              - **Arn** *(string) --* 
        
                The ARN for the image builder.
        
              - **ImageArn** *(string) --* 
        
                The ARN of the image from which this builder was created.
        
              - **Description** *(string) --* 
        
                The description for display.
        
              - **DisplayName** *(string) --* 
        
                The image builder name for display.
        
              - **VpcConfig** *(dict) --* 
        
                The VPC configuration of the image builder.
        
                - **SubnetIds** *(list) --* 
        
                  The subnets to which a network interface is established from the fleet instance.
        
                  - *(string) --* 
              
                - **SecurityGroupIds** *(list) --* 
        
                  The security groups for the fleet.
        
                  - *(string) --* 
              
              - **InstanceType** *(string) --* 
        
                The instance type for the image builder.
        
              - **Platform** *(string) --* 
        
                The operating system platform of the image builder.
        
              - **State** *(string) --* 
        
                The state of the image builder.
        
              - **StateChangeReason** *(dict) --* 
        
                The reason why the last state change occurred.
        
                - **Code** *(string) --* 
        
                  The state change reason code.
        
                - **Message** *(string) --* 
        
                  The state change reason message.
        
              - **CreatedTime** *(datetime) --* 
        
                The time stamp when the image builder was created.
        
              - **EnableDefaultInternetAccess** *(boolean) --* 
        
                Enables or disables default internet access for the image builder.
        
              - **DomainJoinInfo** *(dict) --* 
        
                The information needed to join a Microsoft Active Directory domain.
        
                - **DirectoryName** *(string) --* 
        
                  The fully qualified name of the directory (for example, corp.example.com).
        
                - **OrganizationalUnitDistinguishedName** *(string) --* 
        
                  The distinguished name of the organizational unit for computer accounts.
        
              - **ImageBuilderErrors** *(list) --* 
        
                The image builder errors.
        
                - *(dict) --* 
        
                  Describes a resource error.
        
                  - **ErrorCode** *(string) --* 
        
                    The error code.
        
                  - **ErrorMessage** *(string) --* 
        
                    The error message.
        
                  - **ErrorTimestamp** *(datetime) --* 
        
                    The time the error occurred.
        
              - **AppstreamAgentVersion** *(string) --* 
        
                The version of the AppStream 2.0 agent that is currently being used by this image builder. 
        
        """
        pass

    def stop_fleet(self, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/StopFleet>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_fleet(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the fleet.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def stop_image_builder(self, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/StopImageBuilder>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_image_builder(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the image builder.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ImageBuilder\': {
                    \'Name\': \'string\',
                    \'Arn\': \'string\',
                    \'ImageArn\': \'string\',
                    \'Description\': \'string\',
                    \'DisplayName\': \'string\',
                    \'VpcConfig\': {
                        \'SubnetIds\': [
                            \'string\',
                        ],
                        \'SecurityGroupIds\': [
                            \'string\',
                        ]
                    },
                    \'InstanceType\': \'string\',
                    \'Platform\': \'WINDOWS\',
                    \'State\': \'PENDING\'|\'UPDATING_AGENT\'|\'RUNNING\'|\'STOPPING\'|\'STOPPED\'|\'REBOOTING\'|\'SNAPSHOTTING\'|\'DELETING\'|\'FAILED\',
                    \'StateChangeReason\': {
                        \'Code\': \'INTERNAL_ERROR\'|\'IMAGE_UNAVAILABLE\',
                        \'Message\': \'string\'
                    },
                    \'CreatedTime\': datetime(2015, 1, 1),
                    \'EnableDefaultInternetAccess\': True|False,
                    \'DomainJoinInfo\': {
                        \'DirectoryName\': \'string\',
                        \'OrganizationalUnitDistinguishedName\': \'string\'
                    },
                    \'ImageBuilderErrors\': [
                        {
                            \'ErrorCode\': \'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION\'|\'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION\'|\'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION\'|\'NETWORK_INTERFACE_LIMIT_EXCEEDED\'|\'INTERNAL_SERVICE_ERROR\'|\'IAM_SERVICE_ROLE_IS_MISSING\'|\'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES\'|\'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION\'|\'SUBNET_NOT_FOUND\'|\'IMAGE_NOT_FOUND\'|\'INVALID_SUBNET_CONFIGURATION\'|\'SECURITY_GROUPS_NOT_FOUND\'|\'IGW_NOT_ATTACHED\'|\'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION\'|\'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND\'|\'DOMAIN_JOIN_ERROR_ACCESS_DENIED\'|\'DOMAIN_JOIN_ERROR_LOGON_FAILURE\'|\'DOMAIN_JOIN_ERROR_INVALID_PARAMETER\'|\'DOMAIN_JOIN_ERROR_MORE_DATA\'|\'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN\'|\'DOMAIN_JOIN_ERROR_NOT_SUPPORTED\'|\'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME\'|\'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED\'|\'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED\'|\'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED\'|\'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR\',
                            \'ErrorMessage\': \'string\',
                            \'ErrorTimestamp\': datetime(2015, 1, 1)
                        },
                    ],
                    \'AppstreamAgentVersion\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ImageBuilder** *(dict) --* 
        
              Information about the image builder.
        
              - **Name** *(string) --* 
        
                The name of the image builder.
        
              - **Arn** *(string) --* 
        
                The ARN for the image builder.
        
              - **ImageArn** *(string) --* 
        
                The ARN of the image from which this builder was created.
        
              - **Description** *(string) --* 
        
                The description for display.
        
              - **DisplayName** *(string) --* 
        
                The image builder name for display.
        
              - **VpcConfig** *(dict) --* 
        
                The VPC configuration of the image builder.
        
                - **SubnetIds** *(list) --* 
        
                  The subnets to which a network interface is established from the fleet instance.
        
                  - *(string) --* 
              
                - **SecurityGroupIds** *(list) --* 
        
                  The security groups for the fleet.
        
                  - *(string) --* 
              
              - **InstanceType** *(string) --* 
        
                The instance type for the image builder.
        
              - **Platform** *(string) --* 
        
                The operating system platform of the image builder.
        
              - **State** *(string) --* 
        
                The state of the image builder.
        
              - **StateChangeReason** *(dict) --* 
        
                The reason why the last state change occurred.
        
                - **Code** *(string) --* 
        
                  The state change reason code.
        
                - **Message** *(string) --* 
        
                  The state change reason message.
        
              - **CreatedTime** *(datetime) --* 
        
                The time stamp when the image builder was created.
        
              - **EnableDefaultInternetAccess** *(boolean) --* 
        
                Enables or disables default internet access for the image builder.
        
              - **DomainJoinInfo** *(dict) --* 
        
                The information needed to join a Microsoft Active Directory domain.
        
                - **DirectoryName** *(string) --* 
        
                  The fully qualified name of the directory (for example, corp.example.com).
        
                - **OrganizationalUnitDistinguishedName** *(string) --* 
        
                  The distinguished name of the organizational unit for computer accounts.
        
              - **ImageBuilderErrors** *(list) --* 
        
                The image builder errors.
        
                - *(dict) --* 
        
                  Describes a resource error.
        
                  - **ErrorCode** *(string) --* 
        
                    The error code.
        
                  - **ErrorMessage** *(string) --* 
        
                    The error message.
        
                  - **ErrorTimestamp** *(datetime) --* 
        
                    The time the error occurred.
        
              - **AppstreamAgentVersion** *(string) --* 
        
                The version of the AppStream 2.0 agent that is currently being used by this image builder. 
        
        """
        pass

    def tag_resource(self, ResourceArn: str, Tags: Dict) -> Dict:
        """
        
        Each tag consists of a key and an optional value. If a resource already has a tag with the same key, this operation updates its value.
        
        To list the current tags for your resources, use  ListTagsForResource . To disassociate tags from your resources, use  UntagResource .
        
        For more information about tags, see `Tagging Your Resources <http://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html>`__ in the *Amazon AppStream 2.0 Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/TagResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.tag_resource(
              ResourceArn=\'string\',
              Tags={
                  \'string\': \'string\'
              }
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the resource.
        
        :type Tags: dict
        :param Tags: **[REQUIRED]** 
        
          The tags to associate. A tag is a key-value pair (the value is optional). For example, ``Environment=Test`` , or, if you do not specify a value, ``Environment=`` . 
        
          If you do not specify a value, we set the value to an empty string.
        
          - *(string) --* 
        
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

    def untag_resource(self, ResourceArn: str, TagKeys: List) -> Dict:
        """
        
        To list the current tags for your resources, use  ListTagsForResource .
        
        For more information about tags, see `Tagging Your Resources <http://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html>`__ in the *Amazon AppStream 2.0 Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/UntagResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.untag_resource(
              ResourceArn=\'string\',
              TagKeys=[
                  \'string\',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the resource.
        
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** 
        
          The tag keys for the tags to disassociate.
        
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

    def update_directory_config(self, DirectoryName: str, OrganizationalUnitDistinguishedNames: List = None, ServiceAccountCredentials: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/UpdateDirectoryConfig>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_directory_config(
              DirectoryName=\'string\',
              OrganizationalUnitDistinguishedNames=[
                  \'string\',
              ],
              ServiceAccountCredentials={
                  \'AccountName\': \'string\',
                  \'AccountPassword\': \'string\'
              }
          )
        :type DirectoryName: string
        :param DirectoryName: **[REQUIRED]** 
        
          The name of the Directory Config object.
        
        :type OrganizationalUnitDistinguishedNames: list
        :param OrganizationalUnitDistinguishedNames: 
        
          The distinguished names of the organizational units for computer accounts.
        
          - *(string) --* 
        
        :type ServiceAccountCredentials: dict
        :param ServiceAccountCredentials: 
        
          The credentials for the service account used by the streaming instance to connect to the directory.
        
          - **AccountName** *(string) --* **[REQUIRED]** 
        
            The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.
        
          - **AccountPassword** *(string) --* **[REQUIRED]** 
        
            The password for the account.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DirectoryConfig\': {
                    \'DirectoryName\': \'string\',
                    \'OrganizationalUnitDistinguishedNames\': [
                        \'string\',
                    ],
                    \'ServiceAccountCredentials\': {
                        \'AccountName\': \'string\',
                        \'AccountPassword\': \'string\'
                    },
                    \'CreatedTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DirectoryConfig** *(dict) --* 
        
              Information about the Directory Config object.
        
              - **DirectoryName** *(string) --* 
        
                The fully qualified name of the directory (for example, corp.example.com).
        
              - **OrganizationalUnitDistinguishedNames** *(list) --* 
        
                The distinguished names of the organizational units for computer accounts.
        
                - *(string) --* 
            
              - **ServiceAccountCredentials** *(dict) --* 
        
                The credentials for the service account used by the streaming instance to connect to the directory.
        
                - **AccountName** *(string) --* 
        
                  The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.
        
                - **AccountPassword** *(string) --* 
        
                  The password for the account.
        
              - **CreatedTime** *(datetime) --* 
        
                The time the directory configuration was created.
        
        """
        pass

    def update_fleet(self, ImageName: str = None, ImageArn: str = None, Name: str = None, InstanceType: str = None, ComputeCapacity: Dict = None, VpcConfig: Dict = None, MaxUserDurationInSeconds: int = None, DisconnectTimeoutInSeconds: int = None, DeleteVpcConfig: bool = None, Description: str = None, DisplayName: str = None, EnableDefaultInternetAccess: bool = None, DomainJoinInfo: Dict = None, AttributesToDelete: List = None) -> Dict:
        """
        
        If the fleet is in the ``STOPPED`` state, you can update any attribute except the fleet name. If the fleet is in the ``RUNNING`` state, you can update the ``DisplayName`` and ``ComputeCapacity`` attributes. If the fleet is in the ``STARTING`` or ``STOPPING`` state, you can\'t update it.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/UpdateFleet>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_fleet(
              ImageName=\'string\',
              ImageArn=\'string\',
              Name=\'string\',
              InstanceType=\'string\',
              ComputeCapacity={
                  \'DesiredInstances\': 123
              },
              VpcConfig={
                  \'SubnetIds\': [
                      \'string\',
                  ],
                  \'SecurityGroupIds\': [
                      \'string\',
                  ]
              },
              MaxUserDurationInSeconds=123,
              DisconnectTimeoutInSeconds=123,
              DeleteVpcConfig=True|False,
              Description=\'string\',
              DisplayName=\'string\',
              EnableDefaultInternetAccess=True|False,
              DomainJoinInfo={
                  \'DirectoryName\': \'string\',
                  \'OrganizationalUnitDistinguishedName\': \'string\'
              },
              AttributesToDelete=[
                  \'VPC_CONFIGURATION\'|\'VPC_CONFIGURATION_SECURITY_GROUP_IDS\'|\'DOMAIN_JOIN_INFO\',
              ]
          )
        :type ImageName: string
        :param ImageName: 
        
          The name of the image used to create the fleet.
        
        :type ImageArn: string
        :param ImageArn: 
        
          The ARN of the public, private, or shared image to use.
        
        :type Name: string
        :param Name: 
        
          A unique name for the fleet.
        
        :type InstanceType: string
        :param InstanceType: 
        
          The instance type to use when launching fleet instances. The following instance types are available:
        
          * stream.standard.medium 
           
          * stream.standard.large 
           
          * stream.compute.large 
           
          * stream.compute.xlarge 
           
          * stream.compute.2xlarge 
           
          * stream.compute.4xlarge 
           
          * stream.compute.8xlarge 
           
          * stream.memory.large 
           
          * stream.memory.xlarge 
           
          * stream.memory.2xlarge 
           
          * stream.memory.4xlarge 
           
          * stream.memory.8xlarge 
           
          * stream.graphics-design.large 
           
          * stream.graphics-design.xlarge 
           
          * stream.graphics-design.2xlarge 
           
          * stream.graphics-design.4xlarge 
           
          * stream.graphics-desktop.2xlarge 
           
          * stream.graphics-pro.4xlarge 
           
          * stream.graphics-pro.8xlarge 
           
          * stream.graphics-pro.16xlarge 
           
        :type ComputeCapacity: dict
        :param ComputeCapacity: 
        
          The desired capacity for the fleet.
        
          - **DesiredInstances** *(integer) --* **[REQUIRED]** 
        
            The desired number of streaming instances.
        
        :type VpcConfig: dict
        :param VpcConfig: 
        
          The VPC configuration for the fleet.
        
          - **SubnetIds** *(list) --* 
        
            The subnets to which a network interface is established from the fleet instance.
        
            - *(string) --* 
        
          - **SecurityGroupIds** *(list) --* 
        
            The security groups for the fleet.
        
            - *(string) --* 
        
        :type MaxUserDurationInSeconds: integer
        :param MaxUserDurationInSeconds: 
        
          The maximum time that a streaming session can run, in seconds. Specify a value between 600 and 57600.
        
        :type DisconnectTimeoutInSeconds: integer
        :param DisconnectTimeoutInSeconds: 
        
          The time after disconnection when a session is considered to have ended, in seconds. If a user who was disconnected reconnects within this time interval, the user is connected to their previous session. Specify a value between 60 and 57600.
        
        :type DeleteVpcConfig: boolean
        :param DeleteVpcConfig: 
        
          Deletes the VPC association for the specified fleet.
        
        :type Description: string
        :param Description: 
        
          The description for display.
        
        :type DisplayName: string
        :param DisplayName: 
        
          The fleet name for display.
        
        :type EnableDefaultInternetAccess: boolean
        :param EnableDefaultInternetAccess: 
        
          Enables or disables default internet access for the fleet.
        
        :type DomainJoinInfo: dict
        :param DomainJoinInfo: 
        
          The information needed to join a Microsoft Active Directory domain.
        
          - **DirectoryName** *(string) --* 
        
            The fully qualified name of the directory (for example, corp.example.com).
        
          - **OrganizationalUnitDistinguishedName** *(string) --* 
        
            The distinguished name of the organizational unit for computer accounts.
        
        :type AttributesToDelete: list
        :param AttributesToDelete: 
        
          The fleet attributes to delete.
        
          - *(string) --* 
        
            The fleet attribute.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Fleet\': {
                    \'Arn\': \'string\',
                    \'Name\': \'string\',
                    \'DisplayName\': \'string\',
                    \'Description\': \'string\',
                    \'ImageName\': \'string\',
                    \'ImageArn\': \'string\',
                    \'InstanceType\': \'string\',
                    \'FleetType\': \'ALWAYS_ON\'|\'ON_DEMAND\',
                    \'ComputeCapacityStatus\': {
                        \'Desired\': 123,
                        \'Running\': 123,
                        \'InUse\': 123,
                        \'Available\': 123
                    },
                    \'MaxUserDurationInSeconds\': 123,
                    \'DisconnectTimeoutInSeconds\': 123,
                    \'State\': \'STARTING\'|\'RUNNING\'|\'STOPPING\'|\'STOPPED\',
                    \'VpcConfig\': {
                        \'SubnetIds\': [
                            \'string\',
                        ],
                        \'SecurityGroupIds\': [
                            \'string\',
                        ]
                    },
                    \'CreatedTime\': datetime(2015, 1, 1),
                    \'FleetErrors\': [
                        {
                            \'ErrorCode\': \'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION\'|\'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION\'|\'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION\'|\'NETWORK_INTERFACE_LIMIT_EXCEEDED\'|\'INTERNAL_SERVICE_ERROR\'|\'IAM_SERVICE_ROLE_IS_MISSING\'|\'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES\'|\'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION\'|\'SUBNET_NOT_FOUND\'|\'IMAGE_NOT_FOUND\'|\'INVALID_SUBNET_CONFIGURATION\'|\'SECURITY_GROUPS_NOT_FOUND\'|\'IGW_NOT_ATTACHED\'|\'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION\'|\'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND\'|\'DOMAIN_JOIN_ERROR_ACCESS_DENIED\'|\'DOMAIN_JOIN_ERROR_LOGON_FAILURE\'|\'DOMAIN_JOIN_ERROR_INVALID_PARAMETER\'|\'DOMAIN_JOIN_ERROR_MORE_DATA\'|\'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN\'|\'DOMAIN_JOIN_ERROR_NOT_SUPPORTED\'|\'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME\'|\'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED\'|\'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED\'|\'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED\'|\'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR\',
                            \'ErrorMessage\': \'string\'
                        },
                    ],
                    \'EnableDefaultInternetAccess\': True|False,
                    \'DomainJoinInfo\': {
                        \'DirectoryName\': \'string\',
                        \'OrganizationalUnitDistinguishedName\': \'string\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Fleet** *(dict) --* 
        
              Information about the fleet.
        
              - **Arn** *(string) --* 
        
                The ARN for the fleet.
        
              - **Name** *(string) --* 
        
                The name of the fleet.
        
              - **DisplayName** *(string) --* 
        
                The fleet name for display.
        
              - **Description** *(string) --* 
        
                The description for display.
        
              - **ImageName** *(string) --* 
        
                The name of the image used to create the fleet.
        
              - **ImageArn** *(string) --* 
        
                The ARN for the public, private, or shared image.
        
              - **InstanceType** *(string) --* 
        
                The instance type to use when launching fleet instances.
        
              - **FleetType** *(string) --* 
        
                The fleet type.
        
                  ALWAYS_ON  
        
                Provides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps.
        
                  ON_DEMAND  
        
                Provide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps.
        
              - **ComputeCapacityStatus** *(dict) --* 
        
                The capacity status for the fleet.
        
                - **Desired** *(integer) --* 
        
                  The desired number of streaming instances.
        
                - **Running** *(integer) --* 
        
                  The total number of simultaneous streaming instances that are running.
        
                - **InUse** *(integer) --* 
        
                  The number of instances in use for streaming.
        
                - **Available** *(integer) --* 
        
                  The number of currently available instances that can be used to stream sessions.
        
              - **MaxUserDurationInSeconds** *(integer) --* 
        
                The maximum time that a streaming session can run, in seconds. Specify a value between 600 and 57600.
        
              - **DisconnectTimeoutInSeconds** *(integer) --* 
        
                The time after disconnection when a session is considered to have ended, in seconds. If a user who was disconnected reconnects within this time interval, the user is connected to their previous session. Specify a value between 60 and 57600.
        
              - **State** *(string) --* 
        
                The current state for the fleet.
        
              - **VpcConfig** *(dict) --* 
        
                The VPC configuration for the fleet.
        
                - **SubnetIds** *(list) --* 
        
                  The subnets to which a network interface is established from the fleet instance.
        
                  - *(string) --* 
              
                - **SecurityGroupIds** *(list) --* 
        
                  The security groups for the fleet.
        
                  - *(string) --* 
              
              - **CreatedTime** *(datetime) --* 
        
                The time the fleet was created.
        
              - **FleetErrors** *(list) --* 
        
                The fleet errors.
        
                - *(dict) --* 
        
                  Describes a fleet error.
        
                  - **ErrorCode** *(string) --* 
        
                    The error code.
        
                  - **ErrorMessage** *(string) --* 
        
                    The error message.
        
              - **EnableDefaultInternetAccess** *(boolean) --* 
        
                Indicates whether default internet access is enabled for the fleet.
        
              - **DomainJoinInfo** *(dict) --* 
        
                The information needed to join a Microsoft Active Directory domain.
        
                - **DirectoryName** *(string) --* 
        
                  The fully qualified name of the directory (for example, corp.example.com).
        
                - **OrganizationalUnitDistinguishedName** *(string) --* 
        
                  The distinguished name of the organizational unit for computer accounts.
        
        """
        pass

    def update_image_permissions(self, Name: str, SharedAccountId: str, ImagePermissions: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/UpdateImagePermissions>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_image_permissions(
              Name=\'string\',
              SharedAccountId=\'string\',
              ImagePermissions={
                  \'allowFleet\': True|False,
                  \'allowImageBuilder\': True|False
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the private image.
        
        :type SharedAccountId: string
        :param SharedAccountId: **[REQUIRED]** 
        
          The 12-digit ID of the AWS account for which you want add or update image permissions.
        
        :type ImagePermissions: dict
        :param ImagePermissions: **[REQUIRED]** 
        
          The permissions for the image.
        
          - **allowFleet** *(boolean) --* 
        
            Indicates whether the image can be used for a fleet.
        
          - **allowImageBuilder** *(boolean) --* 
        
            Indicates whether the image can be used for an image builder.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_stack(self, Name: str, DisplayName: str = None, Description: str = None, StorageConnectors: List = None, DeleteStorageConnectors: bool = None, RedirectURL: str = None, FeedbackURL: str = None, AttributesToDelete: List = None, UserSettings: List = None, ApplicationSettings: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/UpdateStack>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_stack(
              DisplayName=\'string\',
              Description=\'string\',
              Name=\'string\',
              StorageConnectors=[
                  {
                      \'ConnectorType\': \'HOMEFOLDERS\'|\'GOOGLE_DRIVE\'|\'ONE_DRIVE\',
                      \'ResourceIdentifier\': \'string\',
                      \'Domains\': [
                          \'string\',
                      ]
                  },
              ],
              DeleteStorageConnectors=True|False,
              RedirectURL=\'string\',
              FeedbackURL=\'string\',
              AttributesToDelete=[
                  \'STORAGE_CONNECTORS\'|\'STORAGE_CONNECTOR_HOMEFOLDERS\'|\'STORAGE_CONNECTOR_GOOGLE_DRIVE\'|\'STORAGE_CONNECTOR_ONE_DRIVE\'|\'REDIRECT_URL\'|\'FEEDBACK_URL\'|\'THEME_NAME\'|\'USER_SETTINGS\',
              ],
              UserSettings=[
                  {
                      \'Action\': \'CLIPBOARD_COPY_FROM_LOCAL_DEVICE\'|\'CLIPBOARD_COPY_TO_LOCAL_DEVICE\'|\'FILE_UPLOAD\'|\'FILE_DOWNLOAD\'|\'PRINTING_TO_LOCAL_DEVICE\',
                      \'Permission\': \'ENABLED\'|\'DISABLED\'
                  },
              ],
              ApplicationSettings={
                  \'Enabled\': True|False,
                  \'SettingsGroup\': \'string\'
              }
          )
        :type DisplayName: string
        :param DisplayName: 
        
          The stack name for display.
        
        :type Description: string
        :param Description: 
        
          The description for display.
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the stack.
        
        :type StorageConnectors: list
        :param StorageConnectors: 
        
          The storage connectors to enable.
        
          - *(dict) --* 
        
            Describes a connector to enable persistent storage for users.
        
            - **ConnectorType** *(string) --* **[REQUIRED]** 
        
              The type of storage connector.
        
            - **ResourceIdentifier** *(string) --* 
        
              The ARN of the storage connector.
        
            - **Domains** *(list) --* 
        
              The names of the domains for the G Suite account.
        
              - *(string) --* GSuite domain for GDrive integration.
        
        :type DeleteStorageConnectors: boolean
        :param DeleteStorageConnectors: 
        
          Deletes the storage connectors currently enabled for the stack.
        
        :type RedirectURL: string
        :param RedirectURL: 
        
          The URL that users are redirected to after their streaming session ends.
        
        :type FeedbackURL: string
        :param FeedbackURL: 
        
          The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.
        
        :type AttributesToDelete: list
        :param AttributesToDelete: 
        
          The stack attributes to delete.
        
          - *(string) --* 
        
        :type UserSettings: list
        :param UserSettings: 
        
          The actions that are enabled or disabled for users during their streaming sessions. By default, these actions are enabled.
        
          - *(dict) --* 
        
            Describes an action and whether the action is enabled or disabled for users during their streaming sessions.
        
            - **Action** *(string) --* **[REQUIRED]** 
        
              The action that is enabled or disabled.
        
            - **Permission** *(string) --* **[REQUIRED]** 
        
              Indicates whether the action is enabled or disabled.
        
        :type ApplicationSettings: dict
        :param ApplicationSettings: 
        
          The persistent application settings for users of a stack. When these settings are enabled, changes that users make to applications and Windows settings are automatically saved after each session and applied to the next session.
        
          - **Enabled** *(boolean) --* **[REQUIRED]** 
        
            Enables or disables persistent application settings for users during their streaming sessions. 
        
          - **SettingsGroup** *(string) --* 
        
            The path prefix for the S3 bucket where users’ persistent application settings are stored. You can allow the same persistent application settings to be used across multiple stacks by specifying the same settings group for each stack. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Stack\': {
                    \'Arn\': \'string\',
                    \'Name\': \'string\',
                    \'Description\': \'string\',
                    \'DisplayName\': \'string\',
                    \'CreatedTime\': datetime(2015, 1, 1),
                    \'StorageConnectors\': [
                        {
                            \'ConnectorType\': \'HOMEFOLDERS\'|\'GOOGLE_DRIVE\'|\'ONE_DRIVE\',
                            \'ResourceIdentifier\': \'string\',
                            \'Domains\': [
                                \'string\',
                            ]
                        },
                    ],
                    \'RedirectURL\': \'string\',
                    \'FeedbackURL\': \'string\',
                    \'StackErrors\': [
                        {
                            \'ErrorCode\': \'STORAGE_CONNECTOR_ERROR\'|\'INTERNAL_SERVICE_ERROR\',
                            \'ErrorMessage\': \'string\'
                        },
                    ],
                    \'UserSettings\': [
                        {
                            \'Action\': \'CLIPBOARD_COPY_FROM_LOCAL_DEVICE\'|\'CLIPBOARD_COPY_TO_LOCAL_DEVICE\'|\'FILE_UPLOAD\'|\'FILE_DOWNLOAD\'|\'PRINTING_TO_LOCAL_DEVICE\',
                            \'Permission\': \'ENABLED\'|\'DISABLED\'
                        },
                    ],
                    \'ApplicationSettings\': {
                        \'Enabled\': True|False,
                        \'SettingsGroup\': \'string\',
                        \'S3BucketName\': \'string\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Stack** *(dict) --* 
        
              Information about the stack.
        
              - **Arn** *(string) --* 
        
                The ARN of the stack.
        
              - **Name** *(string) --* 
        
                The name of the stack.
        
              - **Description** *(string) --* 
        
                The description for display.
        
              - **DisplayName** *(string) --* 
        
                The stack name for display.
        
              - **CreatedTime** *(datetime) --* 
        
                The time the stack was created.
        
              - **StorageConnectors** *(list) --* 
        
                The storage connectors to enable.
        
                - *(dict) --* 
        
                  Describes a connector to enable persistent storage for users.
        
                  - **ConnectorType** *(string) --* 
        
                    The type of storage connector.
        
                  - **ResourceIdentifier** *(string) --* 
        
                    The ARN of the storage connector.
        
                  - **Domains** *(list) --* 
        
                    The names of the domains for the G Suite account.
        
                    - *(string) --* GSuite domain for GDrive integration.
                
              - **RedirectURL** *(string) --* 
        
                The URL that users are redirected to after their streaming session ends.
        
              - **FeedbackURL** *(string) --* 
        
                The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.
        
              - **StackErrors** *(list) --* 
        
                The errors for the stack.
        
                - *(dict) --* 
        
                  Describes a stack error.
        
                  - **ErrorCode** *(string) --* 
        
                    The error code.
        
                  - **ErrorMessage** *(string) --* 
        
                    The error message.
        
              - **UserSettings** *(list) --* 
        
                The actions that are enabled or disabled for users during their streaming sessions. By default these actions are enabled.
        
                - *(dict) --* 
        
                  Describes an action and whether the action is enabled or disabled for users during their streaming sessions.
        
                  - **Action** *(string) --* 
        
                    The action that is enabled or disabled.
        
                  - **Permission** *(string) --* 
        
                    Indicates whether the action is enabled or disabled.
        
              - **ApplicationSettings** *(dict) --* 
        
                The persistent application settings for users of the stack.
        
                - **Enabled** *(boolean) --* 
        
                  Specifies whether persistent application settings are enabled for users during their streaming sessions.
        
                - **SettingsGroup** *(string) --* 
        
                  The path prefix for the S3 bucket where users’ persistent application settings are stored.
        
                - **S3BucketName** *(string) --* 
        
                  The S3 bucket where users’ persistent application settings are stored. When persistent application settings are enabled for the first time for an account in an AWS Region, an S3 bucket is created. The bucket is unique to the AWS account and the Region. 
        
        """
        pass
