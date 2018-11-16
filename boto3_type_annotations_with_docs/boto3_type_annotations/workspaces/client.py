from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def associate_ip_groups(self, DirectoryId: str, GroupIds: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/AssociateIpGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_ip_groups(
              DirectoryId=\'string\',
              GroupIds=[
                  \'string\',
              ]
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The ID of the directory.
        
        :type GroupIds: list
        :param GroupIds: **[REQUIRED]** 
        
          The IDs of one or more IP access control groups.
        
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

    def authorize_ip_rules(self, GroupId: str, UserRules: List) -> Dict:
        """
        
        This action gives users permission to access their WorkSpaces from the CIDR address ranges specified in the rules.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/AuthorizeIpRules>`_
        
        **Request Syntax** 
        ::
        
          response = client.authorize_ip_rules(
              GroupId=\'string\',
              UserRules=[
                  {
                      \'ipRule\': \'string\',
                      \'ruleDesc\': \'string\'
                  },
              ]
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** 
        
          The ID of the group.
        
        :type UserRules: list
        :param UserRules: **[REQUIRED]** 
        
          The rules to add to the group.
        
          - *(dict) --* 
        
            Information about a rule for an IP access control group.
        
            - **ipRule** *(string) --* 
        
              The IP address range, in CIDR notation.
        
            - **ruleDesc** *(string) --* 
        
              The description.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def can_paginate(self, operation_name: str = None):
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

    def create_ip_group(self, GroupName: str, GroupDesc: str = None, UserRules: List = None) -> Dict:
        """
        
        An IP access control group provides you with the ability to control the IP addresses from which users are allowed to access their WorkSpaces. To specify the CIDR address ranges, add rules to your IP access control group and then associate the group with your directory. You can add rules when you create the group or at any time using  AuthorizeIpRules .
        
        There is a default IP access control group associated with your directory. If you don\'t associate an IP access control group with your directory, the default group is used. The default group includes a default rule that allows users to access their WorkSpaces from anywhere. You cannot modify the default IP access control group for your directory.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/CreateIpGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_ip_group(
              GroupName=\'string\',
              GroupDesc=\'string\',
              UserRules=[
                  {
                      \'ipRule\': \'string\',
                      \'ruleDesc\': \'string\'
                  },
              ]
          )
        :type GroupName: string
        :param GroupName: **[REQUIRED]** 
        
          The name of the group.
        
        :type GroupDesc: string
        :param GroupDesc: 
        
          The description of the group.
        
        :type UserRules: list
        :param UserRules: 
        
          The rules to add to the group.
        
          - *(dict) --* 
        
            Information about a rule for an IP access control group.
        
            - **ipRule** *(string) --* 
        
              The IP address range, in CIDR notation.
        
            - **ruleDesc** *(string) --* 
        
              The description.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GroupId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **GroupId** *(string) --* 
        
              The ID of the group.
        
        """
        pass

    def create_tags(self, ResourceId: str, Tags: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/CreateTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_tags(
              ResourceId=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          The ID of the WorkSpace. To find this ID, use  DescribeWorkspaces .
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          The tags. Each WorkSpace can have a maximum of 50 tags.
        
          - *(dict) --* 
        
            Information about a tag.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The key of the tag.
        
            - **Value** *(string) --* 
        
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

    def create_workspaces(self, Workspaces: List) -> Dict:
        """
        
        This operation is asynchronous and returns before the WorkSpaces are created.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/CreateWorkspaces>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_workspaces(
              Workspaces=[
                  {
                      \'DirectoryId\': \'string\',
                      \'UserName\': \'string\',
                      \'BundleId\': \'string\',
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
                      \'Tags\': [
                          {
                              \'Key\': \'string\',
                              \'Value\': \'string\'
                          },
                      ]
                  },
              ]
          )
        :type Workspaces: list
        :param Workspaces: **[REQUIRED]** 
        
          The WorkSpaces to create. You can specify up to 25 WorkSpaces.
        
          - *(dict) --* 
        
            Information used to create a WorkSpace.
        
            - **DirectoryId** *(string) --* **[REQUIRED]** 
        
              The identifier of the AWS Directory Service directory for the WorkSpace. You can use  DescribeWorkspaceDirectories to list the available directories.
        
            - **UserName** *(string) --* **[REQUIRED]** 
        
              The username of the user for the WorkSpace. This username must exist in the AWS Directory Service directory for the WorkSpace.
        
            - **BundleId** *(string) --* **[REQUIRED]** 
        
              The identifier of the bundle for the WorkSpace. You can use  DescribeWorkspaceBundles to list the available bundles.
        
            - **VolumeEncryptionKey** *(string) --* 
        
              The KMS key used to encrypt data stored on your WorkSpace.
        
            - **UserVolumeEncryptionEnabled** *(boolean) --* 
        
              Indicates whether the data stored on the user volume is encrypted.
        
            - **RootVolumeEncryptionEnabled** *(boolean) --* 
        
              Indicates whether the data stored on the root volume is encrypted.
        
            - **WorkspaceProperties** *(dict) --* 
        
              The WorkSpace properties.
        
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
        
            - **Tags** *(list) --* 
        
              The tags for the WorkSpace.
        
              - *(dict) --* 
        
                Information about a tag.
        
                - **Key** *(string) --* **[REQUIRED]** 
        
                  The key of the tag.
        
                - **Value** *(string) --* 
        
                  The value of the tag.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FailedRequests\': [
                    {
                        \'WorkspaceRequest\': {
                            \'DirectoryId\': \'string\',
                            \'UserName\': \'string\',
                            \'BundleId\': \'string\',
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
                            \'Tags\': [
                                {
                                    \'Key\': \'string\',
                                    \'Value\': \'string\'
                                },
                            ]
                        },
                        \'ErrorCode\': \'string\',
                        \'ErrorMessage\': \'string\'
                    },
                ],
                \'PendingRequests\': [
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **FailedRequests** *(list) --* 
        
              Information about the WorkSpaces that could not be created.
        
              - *(dict) --* 
        
                Information about a WorkSpace that could not be created.
        
                - **WorkspaceRequest** *(dict) --* 
        
                  Information about the WorkSpace.
        
                  - **DirectoryId** *(string) --* 
        
                    The identifier of the AWS Directory Service directory for the WorkSpace. You can use  DescribeWorkspaceDirectories to list the available directories.
        
                  - **UserName** *(string) --* 
        
                    The username of the user for the WorkSpace. This username must exist in the AWS Directory Service directory for the WorkSpace.
        
                  - **BundleId** *(string) --* 
        
                    The identifier of the bundle for the WorkSpace. You can use  DescribeWorkspaceBundles to list the available bundles.
        
                  - **VolumeEncryptionKey** *(string) --* 
        
                    The KMS key used to encrypt data stored on your WorkSpace.
        
                  - **UserVolumeEncryptionEnabled** *(boolean) --* 
        
                    Indicates whether the data stored on the user volume is encrypted.
        
                  - **RootVolumeEncryptionEnabled** *(boolean) --* 
        
                    Indicates whether the data stored on the root volume is encrypted.
        
                  - **WorkspaceProperties** *(dict) --* 
        
                    The WorkSpace properties.
        
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
        
                  - **Tags** *(list) --* 
        
                    The tags for the WorkSpace.
        
                    - *(dict) --* 
        
                      Information about a tag.
        
                      - **Key** *(string) --* 
        
                        The key of the tag.
        
                      - **Value** *(string) --* 
        
                        The value of the tag.
        
                - **ErrorCode** *(string) --* 
        
                  The error code.
        
                - **ErrorMessage** *(string) --* 
        
                  The textual error message.
        
            - **PendingRequests** *(list) --* 
        
              Information about the WorkSpaces that were created.
        
              Because this operation is asynchronous, the identifier returned is not immediately available for use with other operations. For example, if you call  DescribeWorkspaces before the WorkSpace is created, the information returned can be incomplete.
        
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

    def delete_ip_group(self, GroupId: str) -> Dict:
        """
        
        You cannot delete an IP access control group that is associated with a directory.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DeleteIpGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_ip_group(
              GroupId=\'string\'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** 
        
          The ID of the IP access control group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_tags(self, ResourceId: str, TagKeys: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DeleteTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_tags(
              ResourceId=\'string\',
              TagKeys=[
                  \'string\',
              ]
          )
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          The ID of the WorkSpace. To find this ID, use  DescribeWorkspaces .
        
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** 
        
          The tag keys.
        
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

    def describe_ip_groups(self, GroupIds: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeIpGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_ip_groups(
              GroupIds=[
                  \'string\',
              ],
              NextToken=\'string\',
              MaxResults=123
          )
        :type GroupIds: list
        :param GroupIds: 
        
          The IDs of one or more IP access control groups.
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of results. (You received this token from a previous call.)
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Result\': [
                    {
                        \'groupId\': \'string\',
                        \'groupName\': \'string\',
                        \'groupDesc\': \'string\',
                        \'userRules\': [
                            {
                                \'ipRule\': \'string\',
                                \'ruleDesc\': \'string\'
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Result** *(list) --* 
        
              Information about the IP access control groups.
        
              - *(dict) --* 
        
                Information about an IP access control group.
        
                - **groupId** *(string) --* 
        
                  The ID of the group.
        
                - **groupName** *(string) --* 
        
                  The name of the group.
        
                - **groupDesc** *(string) --* 
        
                  The description of the group.
        
                - **userRules** *(list) --* 
        
                  The rules.
        
                  - *(dict) --* 
        
                    Information about a rule for an IP access control group.
        
                    - **ipRule** *(string) --* 
        
                      The IP address range, in CIDR notation.
        
                    - **ruleDesc** *(string) --* 
        
                      The description.
        
            - **NextToken** *(string) --* 
        
              The token to use to retrieve the next set of results, or null if there are no more results available. This token is valid for one day and must be used within that time frame.
        
        """
        pass

    def describe_tags(self, ResourceId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_tags(
              ResourceId=\'string\'
          )
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          The ID of the WorkSpace. To find this ID, use  DescribeWorkspaces .
        
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
        
              The tags.
        
              - *(dict) --* 
        
                Information about a tag.
        
                - **Key** *(string) --* 
        
                  The key of the tag.
        
                - **Value** *(string) --* 
        
                  The value of the tag.
        
        """
        pass

    def describe_workspace_bundles(self, BundleIds: List = None, Owner: str = None, NextToken: str = None) -> Dict:
        """
        
        You can filter the results using either bundle ID or owner, but not both.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaceBundles>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_workspace_bundles(
              BundleIds=[
                  \'string\',
              ],
              Owner=\'string\',
              NextToken=\'string\'
          )
        :type BundleIds: list
        :param BundleIds: 
        
          The IDs of the bundles. This parameter cannot be combined with any other filter.
        
          - *(string) --* 
        
        :type Owner: string
        :param Owner: 
        
          The owner of the bundles. This parameter cannot be combined with any other filter.
        
          Specify ``AMAZON`` to describe the bundles provided by AWS or null to describe the bundles that belong to your account.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of results. (You received this token from a previous call.)
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token to use to retrieve the next set of results, or null if there are no more results available. This token is valid for one day and must be used within that time frame.
        
        """
        pass

    def describe_workspace_directories(self, DirectoryIds: List = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaceDirectories>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_workspace_directories(
              DirectoryIds=[
                  \'string\',
              ],
              NextToken=\'string\'
          )
        :type DirectoryIds: list
        :param DirectoryIds: 
        
          The identifiers of the directories. If the value is null, all directories are retrieved.
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of results. (You received this token from a previous call.)
        
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
                \'NextToken\': \'string\'
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
              
            - **NextToken** *(string) --* 
        
              The token to use to retrieve the next set of results, or null if there are no more results available. This token is valid for one day and must be used within that time frame.
        
        """
        pass

    def describe_workspaces(self, WorkspaceIds: List = None, DirectoryId: str = None, UserName: str = None, BundleId: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        
        You can filter the results using bundle ID, directory ID, or owner, but you can specify only one filter at a time.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaces>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_workspaces(
              WorkspaceIds=[
                  \'string\',
              ],
              DirectoryId=\'string\',
              UserName=\'string\',
              BundleId=\'string\',
              Limit=123,
              NextToken=\'string\'
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
        
        :type Limit: integer
        :param Limit: 
        
          The maximum number of items to return.
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of results. (You received this token from a previous call.)
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token to use to retrieve the next set of results, or null if there are no more results available. This token is valid for one day and must be used within that time frame.
        
        """
        pass

    def describe_workspaces_connection_status(self, WorkspaceIds: List = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspacesConnectionStatus>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_workspaces_connection_status(
              WorkspaceIds=[
                  \'string\',
              ],
              NextToken=\'string\'
          )
        :type WorkspaceIds: list
        :param WorkspaceIds: 
        
          The identifiers of the WorkSpaces. You can specify up to 25 WorkSpaces.
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          The token for the next set of results. (You received this token from a previous call.)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'WorkspacesConnectionStatus\': [
                    {
                        \'WorkspaceId\': \'string\',
                        \'ConnectionState\': \'CONNECTED\'|\'DISCONNECTED\'|\'UNKNOWN\',
                        \'ConnectionStateCheckTimestamp\': datetime(2015, 1, 1),
                        \'LastKnownUserConnectionTimestamp\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **WorkspacesConnectionStatus** *(list) --* 
        
              Information about the connection status of the WorkSpace.
        
              - *(dict) --* 
        
                Describes the connection status of a WorkSpace.
        
                - **WorkspaceId** *(string) --* 
        
                  The ID of the WorkSpace.
        
                - **ConnectionState** *(string) --* 
        
                  The connection state of the WorkSpace. The connection state is unknown if the WorkSpace is stopped.
        
                - **ConnectionStateCheckTimestamp** *(datetime) --* 
        
                  The timestamp of the connection state check.
        
                - **LastKnownUserConnectionTimestamp** *(datetime) --* 
        
                  The timestamp of the last known user connection.
        
            - **NextToken** *(string) --* 
        
              The token to use to retrieve the next set of results, or null if there are no more results available.
        
        """
        pass

    def disassociate_ip_groups(self, DirectoryId: str, GroupIds: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DisassociateIpGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_ip_groups(
              DirectoryId=\'string\',
              GroupIds=[
                  \'string\',
              ]
          )
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]** 
        
          The ID of the directory.
        
        :type GroupIds: list
        :param GroupIds: **[REQUIRED]** 
        
          The IDs of one or more IP access control groups.
        
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

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
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

    def modify_workspace_properties(self, WorkspaceId: str, WorkspaceProperties: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/ModifyWorkspaceProperties>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_workspace_properties(
              WorkspaceId=\'string\',
              WorkspaceProperties={
                  \'RunningMode\': \'AUTO_STOP\'|\'ALWAYS_ON\',
                  \'RunningModeAutoStopTimeoutInMinutes\': 123,
                  \'RootVolumeSizeGib\': 123,
                  \'UserVolumeSizeGib\': 123,
                  \'ComputeTypeName\': \'VALUE\'|\'STANDARD\'|\'PERFORMANCE\'|\'POWER\'|\'GRAPHICS\'|\'POWERPRO\'|\'GRAPHICSPRO\'
              }
          )
        :type WorkspaceId: string
        :param WorkspaceId: **[REQUIRED]** 
        
          The ID of the WorkSpace.
        
        :type WorkspaceProperties: dict
        :param WorkspaceProperties: **[REQUIRED]** 
        
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
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def modify_workspace_state(self, WorkspaceId: str, WorkspaceState: str) -> Dict:
        """
        
        To maintain a WorkSpace without being interrupted, set the WorkSpace state to ``ADMIN_MAINTENANCE`` . WorkSpaces in this state do not respond to requests to reboot, stop, start, or rebuild. An AutoStop WorkSpace in this state is not stopped. Users can log into a WorkSpace in the ``ADMIN_MAINTENANCE`` state.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/ModifyWorkspaceState>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_workspace_state(
              WorkspaceId=\'string\',
              WorkspaceState=\'AVAILABLE\'|\'ADMIN_MAINTENANCE\'
          )
        :type WorkspaceId: string
        :param WorkspaceId: **[REQUIRED]** 
        
          The ID of the WorkSpace.
        
        :type WorkspaceState: string
        :param WorkspaceState: **[REQUIRED]** 
        
          The WorkSpace state.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def reboot_workspaces(self, RebootWorkspaceRequests: List) -> Dict:
        """
        
        You cannot reboot a WorkSpace unless its state is ``AVAILABLE`` or ``UNHEALTHY`` .
        
        This operation is asynchronous and returns before the WorkSpaces have rebooted.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/RebootWorkspaces>`_
        
        **Request Syntax** 
        ::
        
          response = client.reboot_workspaces(
              RebootWorkspaceRequests=[
                  {
                      \'WorkspaceId\': \'string\'
                  },
              ]
          )
        :type RebootWorkspaceRequests: list
        :param RebootWorkspaceRequests: **[REQUIRED]** 
        
          The WorkSpaces to reboot. You can specify up to 25 WorkSpaces.
        
          - *(dict) --* 
        
            Information used to reboot a WorkSpace.
        
            - **WorkspaceId** *(string) --* **[REQUIRED]** 
        
              The ID of the WorkSpace.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FailedRequests\': [
                    {
                        \'WorkspaceId\': \'string\',
                        \'ErrorCode\': \'string\',
                        \'ErrorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **FailedRequests** *(list) --* 
        
              Information about the WorkSpaces that could not be rebooted.
        
              - *(dict) --* 
        
                Information about a WorkSpace that could not be rebooted ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
        
                - **WorkspaceId** *(string) --* 
        
                  The identifier of the WorkSpace.
        
                - **ErrorCode** *(string) --* 
        
                  The error code.
        
                - **ErrorMessage** *(string) --* 
        
                  The textual error message.
        
        """
        pass

    def rebuild_workspaces(self, RebuildWorkspaceRequests: List) -> Dict:
        """
        
        You cannot rebuild a WorkSpace unless its state is ``AVAILABLE`` , ``ERROR`` , or ``UNHEALTHY`` .
        
        Rebuilding a WorkSpace is a potentially destructive action that can result in the loss of data. For more information, see `Rebuild a WorkSpace <http://docs.aws.amazon.com/workspaces/latest/adminguide/reset-workspace.html>`__ .
        
        This operation is asynchronous and returns before the WorkSpaces have been completely rebuilt.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/RebuildWorkspaces>`_
        
        **Request Syntax** 
        ::
        
          response = client.rebuild_workspaces(
              RebuildWorkspaceRequests=[
                  {
                      \'WorkspaceId\': \'string\'
                  },
              ]
          )
        :type RebuildWorkspaceRequests: list
        :param RebuildWorkspaceRequests: **[REQUIRED]** 
        
          The WorkSpace to rebuild. You can specify a single WorkSpace.
        
          - *(dict) --* 
        
            Information used to rebuild a WorkSpace.
        
            - **WorkspaceId** *(string) --* **[REQUIRED]** 
        
              The ID of the WorkSpace.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FailedRequests\': [
                    {
                        \'WorkspaceId\': \'string\',
                        \'ErrorCode\': \'string\',
                        \'ErrorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **FailedRequests** *(list) --* 
        
              Information about the WorkSpace if it could not be rebuilt.
        
              - *(dict) --* 
        
                Information about a WorkSpace that could not be rebooted ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
        
                - **WorkspaceId** *(string) --* 
        
                  The identifier of the WorkSpace.
        
                - **ErrorCode** *(string) --* 
        
                  The error code.
        
                - **ErrorMessage** *(string) --* 
        
                  The textual error message.
        
        """
        pass

    def revoke_ip_rules(self, GroupId: str, UserRules: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/RevokeIpRules>`_
        
        **Request Syntax** 
        ::
        
          response = client.revoke_ip_rules(
              GroupId=\'string\',
              UserRules=[
                  \'string\',
              ]
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** 
        
          The ID of the group.
        
        :type UserRules: list
        :param UserRules: **[REQUIRED]** 
        
          The rules to remove from the group.
        
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

    def start_workspaces(self, StartWorkspaceRequests: List) -> Dict:
        """
        
        You cannot start a WorkSpace unless it has a running mode of ``AutoStop`` and a state of ``STOPPED`` .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/StartWorkspaces>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_workspaces(
              StartWorkspaceRequests=[
                  {
                      \'WorkspaceId\': \'string\'
                  },
              ]
          )
        :type StartWorkspaceRequests: list
        :param StartWorkspaceRequests: **[REQUIRED]** 
        
          The WorkSpaces to start. You can specify up to 25 WorkSpaces.
        
          - *(dict) --* 
        
            Information used to start a WorkSpace.
        
            - **WorkspaceId** *(string) --* 
        
              The ID of the WorkSpace.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FailedRequests\': [
                    {
                        \'WorkspaceId\': \'string\',
                        \'ErrorCode\': \'string\',
                        \'ErrorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **FailedRequests** *(list) --* 
        
              Information about the WorkSpaces that could not be started.
        
              - *(dict) --* 
        
                Information about a WorkSpace that could not be rebooted ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
        
                - **WorkspaceId** *(string) --* 
        
                  The identifier of the WorkSpace.
        
                - **ErrorCode** *(string) --* 
        
                  The error code.
        
                - **ErrorMessage** *(string) --* 
        
                  The textual error message.
        
        """
        pass

    def stop_workspaces(self, StopWorkspaceRequests: List) -> Dict:
        """
        
        You cannot stop a WorkSpace unless it has a running mode of ``AutoStop`` and a state of ``AVAILABLE`` , ``IMPAIRED`` , ``UNHEALTHY`` , or ``ERROR`` .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/StopWorkspaces>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_workspaces(
              StopWorkspaceRequests=[
                  {
                      \'WorkspaceId\': \'string\'
                  },
              ]
          )
        :type StopWorkspaceRequests: list
        :param StopWorkspaceRequests: **[REQUIRED]** 
        
          The WorkSpaces to stop. You can specify up to 25 WorkSpaces.
        
          - *(dict) --* 
        
            Information used to stop a WorkSpace.
        
            - **WorkspaceId** *(string) --* 
        
              The ID of the WorkSpace.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FailedRequests\': [
                    {
                        \'WorkspaceId\': \'string\',
                        \'ErrorCode\': \'string\',
                        \'ErrorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **FailedRequests** *(list) --* 
        
              Information about the WorkSpaces that could not be stopped.
        
              - *(dict) --* 
        
                Information about a WorkSpace that could not be rebooted ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
        
                - **WorkspaceId** *(string) --* 
        
                  The identifier of the WorkSpace.
        
                - **ErrorCode** *(string) --* 
        
                  The error code.
        
                - **ErrorMessage** *(string) --* 
        
                  The textual error message.
        
        """
        pass

    def terminate_workspaces(self, TerminateWorkspaceRequests: List) -> Dict:
        """
        
        Terminating a WorkSpace is a permanent action and cannot be undone. The user\'s data is destroyed. If you need to archive any user data, contact Amazon Web Services before terminating the WorkSpace.
        
        You can terminate a WorkSpace that is in any state except ``SUSPENDED`` .
        
        This operation is asynchronous and returns before the WorkSpaces have been completely terminated.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/TerminateWorkspaces>`_
        
        **Request Syntax** 
        ::
        
          response = client.terminate_workspaces(
              TerminateWorkspaceRequests=[
                  {
                      \'WorkspaceId\': \'string\'
                  },
              ]
          )
        :type TerminateWorkspaceRequests: list
        :param TerminateWorkspaceRequests: **[REQUIRED]** 
        
          The WorkSpaces to terminate. You can specify up to 25 WorkSpaces.
        
          - *(dict) --* 
        
            Information used to terminate a WorkSpace.
        
            - **WorkspaceId** *(string) --* **[REQUIRED]** 
        
              The ID of the WorkSpace.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FailedRequests\': [
                    {
                        \'WorkspaceId\': \'string\',
                        \'ErrorCode\': \'string\',
                        \'ErrorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **FailedRequests** *(list) --* 
        
              Information about the WorkSpaces that could not be terminated.
        
              - *(dict) --* 
        
                Information about a WorkSpace that could not be rebooted ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
        
                - **WorkspaceId** *(string) --* 
        
                  The identifier of the WorkSpace.
        
                - **ErrorCode** *(string) --* 
        
                  The error code.
        
                - **ErrorMessage** *(string) --* 
        
                  The textual error message.
        
        """
        pass

    def update_rules_of_ip_group(self, GroupId: str, UserRules: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/UpdateRulesOfIpGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_rules_of_ip_group(
              GroupId=\'string\',
              UserRules=[
                  {
                      \'ipRule\': \'string\',
                      \'ruleDesc\': \'string\'
                  },
              ]
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** 
        
          The ID of the group.
        
        :type UserRules: list
        :param UserRules: **[REQUIRED]** 
        
          One or more rules.
        
          - *(dict) --* 
        
            Information about a rule for an IP access control group.
        
            - **ipRule** *(string) --* 
        
              The IP address range, in CIDR notation.
        
            - **ruleDesc** *(string) --* 
        
              The description.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass
