from typing import Dict
from typing import List
from botocore.paginate import Paginator


class DescribeDirectoryConfigs(Paginator):
    def paginate(self, DirectoryNames: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppStream.Client.describe_directory_configs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeDirectoryConfigs>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DirectoryNames=[
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
                'DirectoryConfigs': [
                    {
                        'DirectoryName': 'string',
                        'OrganizationalUnitDistinguishedNames': [
                            'string',
                        ],
                        'ServiceAccountCredentials': {
                            'AccountName': 'string',
                            'AccountPassword': 'string'
                        },
                        'CreatedTime': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DirectoryConfigs** *(list) --* 
              Information about the directory configurations. Note that although the response syntax in this topic includes the account password, this password is not returned in the actual response. 
              - *(dict) --* 
                Describes the configuration information for the directory used to join a streaming instance to a Microsoft Active Directory domain.
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
        :type DirectoryNames: list
        :param DirectoryNames:
          The directory names.
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


class DescribeFleets(Paginator):
    def paginate(self, Names: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppStream.Client.describe_fleets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeFleets>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Names=[
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
                'Fleets': [
                    {
                        'Arn': 'string',
                        'Name': 'string',
                        'DisplayName': 'string',
                        'Description': 'string',
                        'ImageName': 'string',
                        'ImageArn': 'string',
                        'InstanceType': 'string',
                        'FleetType': 'ALWAYS_ON'|'ON_DEMAND',
                        'ComputeCapacityStatus': {
                            'Desired': 123,
                            'Running': 123,
                            'InUse': 123,
                            'Available': 123
                        },
                        'MaxUserDurationInSeconds': 123,
                        'DisconnectTimeoutInSeconds': 123,
                        'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED',
                        'VpcConfig': {
                            'SubnetIds': [
                                'string',
                            ],
                            'SecurityGroupIds': [
                                'string',
                            ]
                        },
                        'CreatedTime': datetime(2015, 1, 1),
                        'FleetErrors': [
                            {
                                'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                                'ErrorMessage': 'string'
                            },
                        ],
                        'EnableDefaultInternetAccess': True|False,
                        'DomainJoinInfo': {
                            'DirectoryName': 'string',
                            'OrganizationalUnitDistinguishedName': 'string'
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Fleets** *(list) --* 
              Information about the fleets.
              - *(dict) --* 
                Describes the parameters for a fleet.
                - **Arn** *(string) --* 
                  The ARN for the fleet.
                - **Name** *(string) --* 
                  The name of the fleet.
                - **DisplayName** *(string) --* 
                  The fleet name to display.
                - **Description** *(string) --* 
                  The description to display.
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
                  The maximum time that a streaming session can run, in seconds. Specify a value between 600 and 360000.
                - **DisconnectTimeoutInSeconds** *(integer) --* 
                  The time after disconnection when a session is considered to have ended, in seconds. If a user who was disconnected reconnects within this time interval, the user is connected to their previous session. Specify a value between 60 and 360000. By default, this value is 900 seconds (15 minutes).
                - **State** *(string) --* 
                  The current state for the fleet.
                - **VpcConfig** *(dict) --* 
                  The VPC configuration for the fleet.
                  - **SubnetIds** *(list) --* 
                    The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or two subnets. Image builder instances use one subnet.
                    - *(string) --* 
                  - **SecurityGroupIds** *(list) --* 
                    The identifiers of the security groups for the fleet or image builder.
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
                  The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft Active Directory domain. 
                  - **DirectoryName** *(string) --* 
                    The fully qualified name of the directory (for example, corp.example.com).
                  - **OrganizationalUnitDistinguishedName** *(string) --* 
                    The distinguished name of the organizational unit for computer accounts.
        :type Names: list
        :param Names:
          The names of the fleets to describe.
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


class DescribeImageBuilders(Paginator):
    def paginate(self, Names: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppStream.Client.describe_image_builders`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeImageBuilders>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Names=[
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
                'ImageBuilders': [
                    {
                        'Name': 'string',
                        'Arn': 'string',
                        'ImageArn': 'string',
                        'Description': 'string',
                        'DisplayName': 'string',
                        'VpcConfig': {
                            'SubnetIds': [
                                'string',
                            ],
                            'SecurityGroupIds': [
                                'string',
                            ]
                        },
                        'InstanceType': 'string',
                        'Platform': 'WINDOWS',
                        'State': 'PENDING'|'UPDATING_AGENT'|'RUNNING'|'STOPPING'|'STOPPED'|'REBOOTING'|'SNAPSHOTTING'|'DELETING'|'FAILED',
                        'StateChangeReason': {
                            'Code': 'INTERNAL_ERROR'|'IMAGE_UNAVAILABLE',
                            'Message': 'string'
                        },
                        'CreatedTime': datetime(2015, 1, 1),
                        'EnableDefaultInternetAccess': True|False,
                        'DomainJoinInfo': {
                            'DirectoryName': 'string',
                            'OrganizationalUnitDistinguishedName': 'string'
                        },
                        'ImageBuilderErrors': [
                            {
                                'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                                'ErrorMessage': 'string',
                                'ErrorTimestamp': datetime(2015, 1, 1)
                            },
                        ],
                        'AppstreamAgentVersion': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ImageBuilders** *(list) --* 
              Information about the image builders.
              - *(dict) --* 
                Describes a virtual machine that is used to create an image. 
                - **Name** *(string) --* 
                  The name of the image builder.
                - **Arn** *(string) --* 
                  The ARN for the image builder.
                - **ImageArn** *(string) --* 
                  The ARN of the image from which this builder was created.
                - **Description** *(string) --* 
                  The description to display.
                - **DisplayName** *(string) --* 
                  The image builder name to display.
                - **VpcConfig** *(dict) --* 
                  The VPC configuration of the image builder.
                  - **SubnetIds** *(list) --* 
                    The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or two subnets. Image builder instances use one subnet.
                    - *(string) --* 
                  - **SecurityGroupIds** *(list) --* 
                    The identifiers of the security groups for the fleet or image builder.
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
                  The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain. 
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
                  The version of the AppStream 2.0 agent that is currently being used by the image builder. 
        :type Names: list
        :param Names:
          The names of the image builders to describe.
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


class DescribeImages(Paginator):
    def paginate(self, Names: List = None, Arns: List = None, Type: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppStream.Client.describe_images`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeImages>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Names=[
                  'string',
              ],
              Arns=[
                  'string',
              ],
              Type='PUBLIC'|'PRIVATE'|'SHARED',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Images': [
                    {
                        'Name': 'string',
                        'Arn': 'string',
                        'BaseImageArn': 'string',
                        'DisplayName': 'string',
                        'State': 'PENDING'|'AVAILABLE'|'FAILED'|'COPYING'|'DELETING',
                        'Visibility': 'PUBLIC'|'PRIVATE'|'SHARED',
                        'ImageBuilderSupported': True|False,
                        'Platform': 'WINDOWS',
                        'Description': 'string',
                        'StateChangeReason': {
                            'Code': 'INTERNAL_ERROR'|'IMAGE_BUILDER_NOT_AVAILABLE'|'IMAGE_COPY_FAILURE',
                            'Message': 'string'
                        },
                        'Applications': [
                            {
                                'Name': 'string',
                                'DisplayName': 'string',
                                'IconURL': 'string',
                                'LaunchPath': 'string',
                                'LaunchParameters': 'string',
                                'Enabled': True|False,
                                'Metadata': {
                                    'string': 'string'
                                }
                            },
                        ],
                        'CreatedTime': datetime(2015, 1, 1),
                        'PublicBaseImageReleasedDate': datetime(2015, 1, 1),
                        'AppstreamAgentVersion': 'string',
                        'ImagePermissions': {
                            'allowFleet': True|False,
                            'allowImageBuilder': True|False
                        }
                    },
                ],
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
                  The image name to display.
                - **State** *(string) --* 
                  The image starts in the ``PENDING`` state. If image creation succeeds, the state is ``AVAILABLE`` . If image creation fails, the state is ``FAILED`` .
                - **Visibility** *(string) --* 
                  Indicates whether the image is public or private.
                - **ImageBuilderSupported** *(boolean) --* 
                  Indicates whether an image builder can be launched from this image.
                - **Platform** *(string) --* 
                  The operating system platform of the image.
                - **Description** *(string) --* 
                  The description to display.
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
                      The application name to display.
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
    def paginate(self, StackName: str, FleetName: str, UserId: str = None, AuthenticationType: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppStream.Client.describe_sessions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeSessions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              StackName='string',
              FleetName='string',
              UserId='string',
              AuthenticationType='API'|'SAML'|'USERPOOL',
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
                        'Id': 'string',
                        'UserId': 'string',
                        'StackName': 'string',
                        'FleetName': 'string',
                        'State': 'ACTIVE'|'PENDING'|'EXPIRED',
                        'ConnectionState': 'CONNECTED'|'NOT_CONNECTED',
                        'StartTime': datetime(2015, 1, 1),
                        'MaxExpirationTime': datetime(2015, 1, 1),
                        'AuthenticationType': 'API'|'SAML'|'USERPOOL',
                        'NetworkAccessConfiguration': {
                            'EniPrivateIpAddress': 'string',
                            'EniId': 'string'
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Sessions** *(list) --* 
              Information about the streaming sessions.
              - *(dict) --* 
                Describes a streaming session.
                - **Id** *(string) --* 
                  The identifier of the streaming session.
                - **UserId** *(string) --* 
                  The identifier of the user for whom the session was created.
                - **StackName** *(string) --* 
                  The name of the stack for the streaming session.
                - **FleetName** *(string) --* 
                  The name of the fleet for the streaming session.
                - **State** *(string) --* 
                  The current state of the streaming session.
                - **ConnectionState** *(string) --* 
                  Specifies whether a user is connected to the streaming session. 
                - **StartTime** *(datetime) --* 
                  The time when a streaming instance is dedicated for the user. 
                - **MaxExpirationTime** *(datetime) --* 
                  The time when the streaming session is set to expire. This time is based on the ``MaxUserDurationinSeconds`` value, which determines the maximum length of time that a streaming session can run. A streaming session might end earlier than the time specified in ``SessionMaxExpirationTime`` , when the ``DisconnectTimeOutInSeconds`` elapses or the user chooses to end his or her session. If the ``DisconnectTimeOutInSeconds`` elapses, or the user chooses to end his or her session, the streaming instance is terminated and the streaming session ends.
                - **AuthenticationType** *(string) --* 
                  The authentication method. The user is authenticated using a streaming URL (``API`` ), SAML 2.0 federation (``SAML`` ), or the AppStream 2.0 user pool (``USERPOOL`` ). The default is to authenticate users using a streaming URL. 
                - **NetworkAccessConfiguration** *(dict) --* 
                  The network details for the streaming session.
                  - **EniPrivateIpAddress** *(string) --* 
                    The private IP address of the elastic network interface that is attached to instances in your VPC.
                  - **EniId** *(string) --* 
                    The resource identifier of the elastic network interface that is attached to instances in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.
        :type StackName: string
        :param StackName: **[REQUIRED]**
          The name of the stack. This value is case-sensitive.
        :type FleetName: string
        :param FleetName: **[REQUIRED]**
          The name of the fleet. This value is case-sensitive.
        :type UserId: string
        :param UserId:
          The user identifier.
        :type AuthenticationType: string
        :param AuthenticationType:
          The authentication method. Specify ``API`` for a user authenticated using a streaming URL, ``SAML`` for a SAML 2.0-federated user, or ``USERPOOL`` for a user in the AppStream 2.0 user pool. The default is to authenticate users using a streaming URL.
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
    def paginate(self, Names: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppStream.Client.describe_stacks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeStacks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Names=[
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
                'Stacks': [
                    {
                        'Arn': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'DisplayName': 'string',
                        'CreatedTime': datetime(2015, 1, 1),
                        'StorageConnectors': [
                            {
                                'ConnectorType': 'HOMEFOLDERS'|'GOOGLE_DRIVE'|'ONE_DRIVE',
                                'ResourceIdentifier': 'string',
                                'Domains': [
                                    'string',
                                ]
                            },
                        ],
                        'RedirectURL': 'string',
                        'FeedbackURL': 'string',
                        'StackErrors': [
                            {
                                'ErrorCode': 'STORAGE_CONNECTOR_ERROR'|'INTERNAL_SERVICE_ERROR',
                                'ErrorMessage': 'string'
                            },
                        ],
                        'UserSettings': [
                            {
                                'Action': 'CLIPBOARD_COPY_FROM_LOCAL_DEVICE'|'CLIPBOARD_COPY_TO_LOCAL_DEVICE'|'FILE_UPLOAD'|'FILE_DOWNLOAD'|'PRINTING_TO_LOCAL_DEVICE',
                                'Permission': 'ENABLED'|'DISABLED'
                            },
                        ],
                        'ApplicationSettings': {
                            'Enabled': True|False,
                            'SettingsGroup': 'string',
                            'S3BucketName': 'string'
                        }
                    },
                ],
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
                  The description to display.
                - **DisplayName** *(string) --* 
                  The stack name to display.
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
                      The names of the domains for the account.
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
        :type Names: list
        :param Names:
          The names of the stacks to describe.
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


class DescribeUserStackAssociations(Paginator):
    def paginate(self, StackName: str = None, UserName: str = None, AuthenticationType: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppStream.Client.describe_user_stack_associations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeUserStackAssociations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              StackName='string',
              UserName='string',
              AuthenticationType='API'|'SAML'|'USERPOOL',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'UserStackAssociations': [
                    {
                        'StackName': 'string',
                        'UserName': 'string',
                        'AuthenticationType': 'API'|'SAML'|'USERPOOL',
                        'SendEmailNotification': True|False
                    },
                ],
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
        :type StackName: string
        :param StackName:
          The name of the stack that is associated with the user.
        :type UserName: string
        :param UserName:
          The email address of the user who is associated with the stack.
        :type AuthenticationType: string
        :param AuthenticationType:
          The authentication type for the user who is associated with the stack. You must specify USERPOOL.
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


class DescribeUsers(Paginator):
    def paginate(self, AuthenticationType: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppStream.Client.describe_users`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeUsers>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AuthenticationType='API'|'SAML'|'USERPOOL',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Users': [
                    {
                        'Arn': 'string',
                        'UserName': 'string',
                        'Enabled': True|False,
                        'Status': 'string',
                        'FirstName': 'string',
                        'LastName': 'string',
                        'CreatedTime': datetime(2015, 1, 1),
                        'AuthenticationType': 'API'|'SAML'|'USERPOOL'
                    },
                ],
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
        :type AuthenticationType: string
        :param AuthenticationType: **[REQUIRED]**
          The authentication type for the users in the user pool to describe. You must specify USERPOOL.
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


class ListAssociatedFleets(Paginator):
    def paginate(self, StackName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppStream.Client.list_associated_fleets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/ListAssociatedFleets>`_
        
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
                'Names': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Names** *(list) --* 
              The name of the fleet.
              - *(string) --* 
        :type StackName: string
        :param StackName: **[REQUIRED]**
          The name of the stack.
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


class ListAssociatedStacks(Paginator):
    def paginate(self, FleetName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppStream.Client.list_associated_stacks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/ListAssociatedStacks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              FleetName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Names': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Names** *(list) --* 
              The name of the stack.
              - *(string) --* 
        :type FleetName: string
        :param FleetName: **[REQUIRED]**
          The name of the fleet.
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
