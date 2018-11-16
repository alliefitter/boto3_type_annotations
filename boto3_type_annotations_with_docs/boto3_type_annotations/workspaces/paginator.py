from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeWorkspaceBundles(Paginator):
    def paginate(self, BundleIds: List = None, Owner: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaceBundles>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              BundleIds=[
                  \'string\',
              ],
              Owner=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type BundleIds: list
        :param BundleIds: 
        
          The IDs of the bundles. This parameter cannot be combined with any other filter.
        
          - *(string) --* 
        
        :type Owner: string
        :param Owner: 
        
          The owner of the bundles. This parameter cannot be combined with any other filter.
        
          Specify ``AMAZON`` to describe the bundles provided by AWS or null to describe the bundles that belong to your account.
        
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
                \'Bundles\': [
                    {
                        \'BundleId\': \'string\',
                        \'Name\': \'string\',
                        \'Owner\': \'string\',
                        \'Description\': \'string\',
                        \'RootStorage\': {
                            \'Capacity\': \'string\'
                        },
                        \'UserStorage\': {
                            \'Capacity\': \'string\'
                        },
                        \'ComputeType\': {
                            \'Name\': \'VALUE\'|\'STANDARD\'|\'PERFORMANCE\'|\'POWER\'|\'GRAPHICS\'|\'POWERPRO\'|\'GRAPHICSPRO\'
                        }
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Bundles** *(list) --* 
        
              Information about the bundles.
        
              - *(dict) --* 
        
                Information about a WorkSpace bundle.
        
                - **BundleId** *(string) --* 
        
                  The bundle identifier.
        
                - **Name** *(string) --* 
        
                  The name of the bundle.
        
                - **Owner** *(string) --* 
        
                  The owner of the bundle. This is the account identifier of the owner, or ``AMAZON`` if the bundle is provided by AWS.
        
                - **Description** *(string) --* 
        
                  A description.
        
                - **RootStorage** *(dict) --* 
        
                  The size of the root volume.
        
                  - **Capacity** *(string) --* 
        
                    The size of the root volume.
        
                - **UserStorage** *(dict) --* 
        
                  The size of the user storage.
        
                  - **Capacity** *(string) --* 
        
                    The size of the user storage.
        
                - **ComputeType** *(dict) --* 
        
                  The compute type. For more information, see `Amazon WorkSpaces Bundles <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .
        
                  - **Name** *(string) --* 
        
                    The compute type.
        
        """
        pass


class DescribeWorkspaceDirectories(Paginator):
    def paginate(self, DirectoryIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaceDirectories>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DirectoryIds=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type DirectoryIds: list
        :param DirectoryIds: 
        
          The identifiers of the directories. If the value is null, all directories are retrieved.
        
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
                \'Directories\': [
                    {
                        \'DirectoryId\': \'string\',
                        \'Alias\': \'string\',
                        \'DirectoryName\': \'string\',
                        \'RegistrationCode\': \'string\',
                        \'SubnetIds\': [
                            \'string\',
                        ],
                        \'DnsIpAddresses\': [
                            \'string\',
                        ],
                        \'CustomerUserName\': \'string\',
                        \'IamRoleId\': \'string\',
                        \'DirectoryType\': \'SIMPLE_AD\'|\'AD_CONNECTOR\',
                        \'WorkspaceSecurityGroupId\': \'string\',
                        \'State\': \'REGISTERING\'|\'REGISTERED\'|\'DEREGISTERING\'|\'DEREGISTERED\'|\'ERROR\',
                        \'WorkspaceCreationProperties\': {
                            \'EnableWorkDocs\': True|False,
                            \'EnableInternetAccess\': True|False,
                            \'DefaultOu\': \'string\',
                            \'CustomSecurityGroupId\': \'string\',
                            \'UserEnabledAsLocalAdministrator\': True|False
                        },
                        \'ipGroupIds\': [
                            \'string\',
                        ]
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Directories** *(list) --* 
        
              Information about the directories.
        
              - *(dict) --* 
        
                Information about an AWS Directory Service directory for use with Amazon WorkSpaces.
        
                - **DirectoryId** *(string) --* 
        
                  The directory identifier.
        
                - **Alias** *(string) --* 
        
                  The directory alias.
        
                - **DirectoryName** *(string) --* 
        
                  The name of the directory.
        
                - **RegistrationCode** *(string) --* 
        
                  The registration code for the directory. This is the code that users enter in their Amazon WorkSpaces client application to connect to the directory.
        
                - **SubnetIds** *(list) --* 
        
                  The identifiers of the subnets used with the directory.
        
                  - *(string) --* 
              
                - **DnsIpAddresses** *(list) --* 
        
                  The IP addresses of the DNS servers for the directory.
        
                  - *(string) --* 
              
                - **CustomerUserName** *(string) --* 
        
                  The user name for the service account.
        
                - **IamRoleId** *(string) --* 
        
                  The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make calls to other services, such as Amazon EC2, on your behalf.
        
                - **DirectoryType** *(string) --* 
        
                  The directory type.
        
                - **WorkspaceSecurityGroupId** *(string) --* 
        
                  The identifier of the security group that is assigned to new WorkSpaces.
        
                - **State** *(string) --* 
        
                  The state of the directory\'s registration with Amazon WorkSpaces
        
                - **WorkspaceCreationProperties** *(dict) --* 
        
                  The default creation properties for all WorkSpaces in the directory.
        
                  - **EnableWorkDocs** *(boolean) --* 
        
                    Indicates whether the directory is enabled for Amazon WorkDocs.
        
                  - **EnableInternetAccess** *(boolean) --* 
        
                    The public IP address to attach to all WorkSpaces that are created or rebuilt.
        
                  - **DefaultOu** *(string) --* 
        
                    The organizational unit (OU) in the directory for the WorkSpace machine accounts.
        
                  - **CustomSecurityGroupId** *(string) --* 
        
                    The identifier of any security groups to apply to WorkSpaces when they are created.
        
                  - **UserEnabledAsLocalAdministrator** *(boolean) --* 
        
                    Indicates whether the WorkSpace user is an administrator on the WorkSpace.
        
                - **ipGroupIds** *(list) --* 
        
                  The identifiers of the IP access control groups associated with the directory.
        
                  - *(string) --* 
              
        """
        pass


class DescribeWorkspaces(Paginator):
    def paginate(self, WorkspaceIds: List = None, DirectoryId: str = None, UserName: str = None, BundleId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaces>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              WorkspaceIds=[
                  \'string\',
              ],
              DirectoryId=\'string\',
              UserName=\'string\',
              BundleId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type WorkspaceIds: list
        :param WorkspaceIds: 
        
          The IDs of the WorkSpaces. This parameter cannot be combined with any other filter.
        
          Because the  CreateWorkspaces operation is asynchronous, the identifier it returns is not immediately available. If you immediately call  DescribeWorkspaces with this identifier, no information is returned.
        
          - *(string) --* 
        
        :type DirectoryId: string
        :param DirectoryId: 
        
          The ID of the directory. In addition, you can optionally specify a specific directory user (see ``UserName`` ). This parameter cannot be combined with any other filter.
        
        :type UserName: string
        :param UserName: 
        
          The name of the directory user. You must specify this parameter with ``DirectoryId`` .
        
        :type BundleId: string
        :param BundleId: 
        
          The ID of the bundle. All WorkSpaces that are created from this bundle are retrieved. This parameter cannot be combined with any other filter.
        
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
                \'Workspaces\': [
                    {
                        \'WorkspaceId\': \'string\',
                        \'DirectoryId\': \'string\',
                        \'UserName\': \'string\',
                        \'IpAddress\': \'string\',
                        \'State\': \'PENDING\'|\'AVAILABLE\'|\'IMPAIRED\'|\'UNHEALTHY\'|\'REBOOTING\'|\'STARTING\'|\'REBUILDING\'|\'MAINTENANCE\'|\'ADMIN_MAINTENANCE\'|\'TERMINATING\'|\'TERMINATED\'|\'SUSPENDED\'|\'UPDATING\'|\'STOPPING\'|\'STOPPED\'|\'ERROR\',
                        \'BundleId\': \'string\',
                        \'SubnetId\': \'string\',
                        \'ErrorMessage\': \'string\',
                        \'ErrorCode\': \'string\',
                        \'ComputerName\': \'string\',
                        \'VolumeEncryptionKey\': \'string\',
                        \'UserVolumeEncryptionEnabled\': True|False,
                        \'RootVolumeEncryptionEnabled\': True|False,
                        \'WorkspaceProperties\': {
                            \'RunningMode\': \'AUTO_STOP\'|\'ALWAYS_ON\',
                            \'RunningModeAutoStopTimeoutInMinutes\': 123,
                            \'RootVolumeSizeGib\': 123,
                            \'UserVolumeSizeGib\': 123,
                            \'ComputeTypeName\': \'VALUE\'|\'STANDARD\'|\'PERFORMANCE\'|\'POWER\'|\'GRAPHICS\'|\'POWERPRO\'|\'GRAPHICSPRO\'
                        },
                        \'ModificationStates\': [
                            {
                                \'Resource\': \'ROOT_VOLUME\'|\'USER_VOLUME\'|\'COMPUTE_TYPE\',
                                \'State\': \'UPDATE_INITIATED\'|\'UPDATE_IN_PROGRESS\'
                            },
                        ]
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Workspaces** *(list) --* 
        
              Information about the WorkSpaces.
        
              Because  CreateWorkspaces is an asynchronous operation, some of the returned information could be incomplete.
        
              - *(dict) --* 
        
                Information about a WorkSpace.
        
                - **WorkspaceId** *(string) --* 
        
                  The identifier of the WorkSpace.
        
                - **DirectoryId** *(string) --* 
        
                  The identifier of the AWS Directory Service directory for the WorkSpace.
        
                - **UserName** *(string) --* 
        
                  The user for the WorkSpace.
        
                - **IpAddress** *(string) --* 
        
                  The IP address of the WorkSpace.
        
                - **State** *(string) --* 
        
                  The operational state of the WorkSpace.
        
                - **BundleId** *(string) --* 
        
                  The identifier of the bundle used to create the WorkSpace.
        
                - **SubnetId** *(string) --* 
        
                  The identifier of the subnet for the WorkSpace.
        
                - **ErrorMessage** *(string) --* 
        
                  If the WorkSpace could not be created, contains a textual error message that describes the failure.
        
                - **ErrorCode** *(string) --* 
        
                  If the WorkSpace could not be created, contains the error code.
        
                - **ComputerName** *(string) --* 
        
                  The name of the WorkSpace, as seen by the operating system.
        
                - **VolumeEncryptionKey** *(string) --* 
        
                  The KMS key used to encrypt data stored on your WorkSpace.
        
                - **UserVolumeEncryptionEnabled** *(boolean) --* 
        
                  Indicates whether the data stored on the user volume is encrypted.
        
                - **RootVolumeEncryptionEnabled** *(boolean) --* 
        
                  Indicates whether the data stored on the root volume is encrypted.
        
                - **WorkspaceProperties** *(dict) --* 
        
                  The properties of the WorkSpace.
        
                  - **RunningMode** *(string) --* 
        
                    The running mode. For more information, see `Manage the WorkSpace Running Mode <http://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .
        
                  - **RunningModeAutoStopTimeoutInMinutes** *(integer) --* 
        
                    The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.
        
                  - **RootVolumeSizeGib** *(integer) --* 
        
                    The size of the root volume.
        
                  - **UserVolumeSizeGib** *(integer) --* 
        
                    The size of the user storage.
        
                  - **ComputeTypeName** *(string) --* 
        
                    The compute type. For more information, see `Amazon WorkSpaces Bundles <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .
        
                - **ModificationStates** *(list) --* 
        
                  The modification states of the WorkSpace.
        
                  - *(dict) --* 
        
                    Information about a WorkSpace modification.
        
                    - **Resource** *(string) --* 
        
                      The resource.
        
                    - **State** *(string) --* 
        
                      The modification state.
        
        """
        pass
