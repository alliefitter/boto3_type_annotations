from typing import Union
from typing import List
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Optional
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        """
        Check if an operation can be paginated.
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

    def cancel_task_execution(self, TaskExecutionArn: str) -> Dict:
        """
        Cancels execution of a task. 
        When you cancel a task execution, the transfer of some files are abruptly interrupted. The contents of files that are transferred to the destination might be incomplete or inconsistent with the source files. However, if you start a new task execution on the same task and you allow the task execution to complete, file content on the destination is complete and consistent. This applies to other unexpected failures that interrupt a task execution. In all of these cases, AWS DataSync successfully complete the transfer when you start the next task execution. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/CancelTaskExecution>`_
        
        **Request Syntax**
        ::
          response = client.cancel_task_execution(
              TaskExecutionArn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type TaskExecutionArn: string
        :param TaskExecutionArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the task execution to cancel.
        :rtype: dict
        :returns:
        """
        pass

    def create_agent(self, ActivationKey: str, AgentName: str = None, Tags: List = None) -> Dict:
        """
        Activates an AWS DataSync agent that you have deployed on your host. The activation process associates your agent with your account. In the activation process, you specify information such as the AWS Region that you want to activate the agent in. You activate the agent in the AWS Region where your target locations (in Amazon S3 or Amazon EFS) reside. Your tasks are created in this AWS Region. 
        You can use an agent for more than one location. If a task uses multiple agents, all of them need to have status AVAILABLE for the task to run. If you use multiple agents for a source location, the status of all the agents must be AVAILABLE for the task to run. For more information, see `Activating a Sync Agent <https://docs.aws.amazon.com/sync-service/latest/userguide/working-with-sync-agents.html#activating-sync-agent>`__ in the *AWS DataSync User Guide.*  
        Agents are automatically updated by AWS on a regular basis, using a mechanism that ensures minimal interruption to your tasks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/CreateAgent>`_
        
        **Request Syntax**
        ::
          response = client.create_agent(
              ActivationKey='string',
              AgentName='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'AgentArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            CreateAgentResponse
            - **AgentArn** *(string) --* 
              The Amazon Resource Name (ARN) of the agent. Use the ``ListAgents`` operation to return a list of agents for your account and AWS Region.
        :type ActivationKey: string
        :param ActivationKey: **[REQUIRED]**
          Your agent activation key. You can get the activation key either by sending an HTTP GET request with redirects that enable you to get the agent IP address (port 80). Alternatively, you can get it from the AWS DataSync console.
          The redirect URL returned in the response provides you the activation key for your agent in the query string parameter ``activationKey`` . It might also include other activation-related parameters; however, these are merely defaults. The arguments you pass to this API call determine the actual configuration of your agent. For more information, see `Activating a Sync Agent <https://docs.aws.amazon.com/sync-service/latest/userguide/working-with-sync-agents.html#activating-sync-agent>`__ in the *AWS DataSync User Guide.*
        :type AgentName: string
        :param AgentName:
          The name you configured for your agent. This value is a text reference that is used to identify the agent in the console.
        :type Tags: list
        :param Tags:
          The key-value pair that represents the tag you want to associate with the agent. The value can be an empty string. This value helps you manage, filter, and search for your agents.
          .. note::
            Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @.
          - *(dict) --*
            Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array that contains a list of tasks when the  ListTagsForResource operation is called.
            - **Key** *(string) --*
              The key for an AWS resource tag.
            - **Value** *(string) --*
              The value for an AWS resource tag.
        :rtype: dict
        :returns:
        """
        pass

    def create_location_efs(self, Subdirectory: str, EfsFilesystemArn: str, Ec2Config: Dict, Tags: List = None) -> Dict:
        """
        Creates an endpoint for an Amazon EFS file system.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/CreateLocationEfs>`_
        
        **Request Syntax**
        ::
          response = client.create_location_efs(
              Subdirectory='string',
              EfsFilesystemArn='string',
              Ec2Config={
                  'SubnetArn': 'string',
                  'SecurityGroupArns': [
                      'string',
                  ]
              },
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'LocationArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            CreateLocationEfs
            - **LocationArn** *(string) --* 
              The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.
        :type Subdirectory: string
        :param Subdirectory: **[REQUIRED]**
          A subdirectory in the location’s path. This subdirectory in the EFS file system is used to read data from the EFS source location or write data to the EFS destination. By default, AWS DataSync uses the root directory.
        :type EfsFilesystemArn: string
        :param EfsFilesystemArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) for the Amazon EFS file system.
        :type Ec2Config: dict
        :param Ec2Config: **[REQUIRED]**
          The subnet and security group that the Amazon EFS file system uses.
          - **SubnetArn** *(string) --* **[REQUIRED]**
            The ARN of the subnet that the Amazon EC2 resource belongs in.
          - **SecurityGroupArns** *(list) --* **[REQUIRED]**
            The Amazon Resource Names (ARNs) of the security groups that are configured for the Amazon EC2 resource.
            - *(string) --*
        :type Tags: list
        :param Tags:
          The key-value pair that represents a tag that you want to add to the resource. The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.
          - *(dict) --*
            Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array that contains a list of tasks when the  ListTagsForResource operation is called.
            - **Key** *(string) --*
              The key for an AWS resource tag.
            - **Value** *(string) --*
              The value for an AWS resource tag.
        :rtype: dict
        :returns:
        """
        pass

    def create_location_nfs(self, Subdirectory: str, ServerHostname: str, OnPremConfig: Dict, Tags: List = None) -> Dict:
        """
        Creates an endpoint for a Network File System (NFS) file system.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/CreateLocationNfs>`_
        
        **Request Syntax**
        ::
          response = client.create_location_nfs(
              Subdirectory='string',
              ServerHostname='string',
              OnPremConfig={
                  'AgentArns': [
                      'string',
                  ]
              },
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'LocationArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            CreateLocationNfsResponse
            - **LocationArn** *(string) --* 
              The Amazon Resource Name (ARN) of the source NFS file system location that is created.
        :type Subdirectory: string
        :param Subdirectory: **[REQUIRED]**
          The subdirectory in the NFS file system that is used to read data from the NFS source location or write data to the NFS destination. The NFS path should be a path that\'s exported by the NFS server, or a subdirectory of that path. The path should be such that it can be mounted by other NFS clients in your network.
          To see all the paths exported by your NFS server. run \"``showmount -e nfs-server-name`` \" from an NFS client that has access to your server. You can specify any directory that appears in the results, and any subdirectory of that directory. Ensure that the NFS export is accessible without Kerberos authentication.
          To transfer all the data in the folder you specified, DataSync needs to have permissions to read all the data. To ensure this, either configure the NFS export with ``no_root_squash,`` or ensure that the permissions for all of the files that you want sync allow read access for all users. Doing either enables the agent to read the files. For the agent to access directories, you must additionally enable all execute access. For information about NFS export configuration, see `18.7. The /etc/exports Configuration File <https://www.centos.org/docs/5/html/Deployment_Guide-en-US/s1-nfs-server-config-exports.html>`__ in the Centos documentation.
        :type ServerHostname: string
        :param ServerHostname: **[REQUIRED]**
          The name of the NFS server. This value is the IP address or Domain Name Service (DNS) name of the NFS server. An agent that is installed on-premises uses this host name to mount the NFS server in a network.
          .. note::
            This name must either be DNS-compliant or must be an IP version 4 (IPv4) address.
        :type OnPremConfig: dict
        :param OnPremConfig: **[REQUIRED]**
          Contains a list of Amazon Resource Names (ARNs) of agents that are used to connect to an NFS server.
          - **AgentArns** *(list) --* **[REQUIRED]**
            ARNs)of the agents to use for an NFS location.
            - *(string) --*
        :type Tags: list
        :param Tags:
          The key-value pair that represents the tag that you want to add to the location. The value can be an empty string. We recommend using tags to name your resources.
          - *(dict) --*
            Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array that contains a list of tasks when the  ListTagsForResource operation is called.
            - **Key** *(string) --*
              The key for an AWS resource tag.
            - **Value** *(string) --*
              The value for an AWS resource tag.
        :rtype: dict
        :returns:
        """
        pass

    def create_location_s3(self, Subdirectory: str, S3BucketArn: str, S3Config: Dict, Tags: List = None) -> Dict:
        """
        Creates an endpoint for an Amazon S3 bucket.
        For AWS DataSync to access a destination S3 bucket, it needs an AWS Identity and Access Management (IAM) role that has the required permissions. You can set up the required permissions by creating an IAM policy that grants the required permissions and attaching the policy to the role. An example of such a policy is shown in the examples section. For more information, see `Configuring Amazon S3 Location Settings <https://docs.aws.amazon.com/sync-service/latest/userguide/configuring-s3-locations.html>`__ in the *AWS DataSync User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/CreateLocationS3>`_
        
        **Request Syntax**
        ::
          response = client.create_location_s3(
              Subdirectory='string',
              S3BucketArn='string',
              S3Config={
                  'BucketAccessRoleArn': 'string'
              },
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'LocationArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            CreateLocationS3Response
            - **LocationArn** *(string) --* 
              The Amazon Resource Name (ARN) of the source Amazon S3 bucket location that is created.
        :type Subdirectory: string
        :param Subdirectory: **[REQUIRED]**
          A subdirectory in the Amazon S3 bucket. This subdirectory in Amazon S3 is used to read data from the S3 source location or write data to the S3 destination.
        :type S3BucketArn: string
        :param S3BucketArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the Amazon S3 bucket.
        :type S3Config: dict
        :param S3Config: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that is used to access an Amazon S3 bucket. For detailed information about using such a role, see `Components and Terminology <https://alpha-aws-docs.aws.amazon.com/sync-service/latest/userguide/create-locations-cli.html#create-location-s3-cli>`__ in the *AWS DataSync User Guide* .
          - **BucketAccessRoleArn** *(string) --* **[REQUIRED]**
            The Amazon S3 bucket to access. This bucket is used as a parameter in the  CreateLocationS3 operation.
        :type Tags: list
        :param Tags:
          The key-value pair that represents the tag that you want to add to the location. The value can be an empty string. We recommend using tags to name your resources.
          - *(dict) --*
            Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array that contains a list of tasks when the  ListTagsForResource operation is called.
            - **Key** *(string) --*
              The key for an AWS resource tag.
            - **Value** *(string) --*
              The value for an AWS resource tag.
        :rtype: dict
        :returns:
        """
        pass

    def create_task(self, SourceLocationArn: str, DestinationLocationArn: str, CloudWatchLogGroupArn: str = None, Name: str = None, Options: Dict = None, Tags: List = None) -> Dict:
        """
        Creates a task. A task is a set of two locations (source and destination) and a set of default ``OverrideOptions`` that you use to control the behavior of a task. If you don't specify default values for ``Options`` when you create a task, AWS DataSync populates them with safe service defaults.
        When you initially create a task, it enters the INITIALIZING status and then the CREATING status. In CREATING status, AWS DataSync attempts to mount the source Network File System (NFS) location. The task transitions to the AVAILABLE status without waiting for the destination location to mount. Instead, AWS DataSync mounts a destination before every task execution and then unmounts it after every task execution. 
        If an agent that is associated with a source (NFS) location goes offline, the task transitions to the UNAVAILABLE status. If the status of the task remains in the CREATING status for more than a few minutes, it means that your agent might be having trouble mounting the source NFS file system. Check the task's ``ErrorCode`` and ``ErrorDetail`` . Mount issues are often caused by either a misconfigured firewall or a mistyped NFS server host name.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/CreateTask>`_
        
        **Request Syntax**
        ::
          response = client.create_task(
              SourceLocationArn='string',
              DestinationLocationArn='string',
              CloudWatchLogGroupArn='string',
              Name='string',
              Options={
                  'VerifyMode': 'POINT_IN_TIME_CONSISTENT'|'NONE',
                  'Atime': 'NONE'|'BEST_EFFORT',
                  'Mtime': 'NONE'|'PRESERVE',
                  'Uid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
                  'Gid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
                  'PreserveDeletedFiles': 'PRESERVE'|'REMOVE',
                  'PreserveDevices': 'NONE'|'PRESERVE',
                  'PosixPermissions': 'NONE'|'BEST_EFFORT'|'PRESERVE',
                  'BytesPerSecond': 123
              },
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'TaskArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            CreateTaskResponse
            - **TaskArn** *(string) --* 
              The Amazon Resource Name (ARN) of the task.
        :type SourceLocationArn: string
        :param SourceLocationArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the source location for the task.
        :type DestinationLocationArn: string
        :param DestinationLocationArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of an AWS storage resource\'s location.
        :type CloudWatchLogGroupArn: string
        :param CloudWatchLogGroupArn:
          The Amazon Resource Name (ARN) of the Amazon CloudWatch log group that is used to monitor and log events in the task. For more information on these groups, see `Working with Log Groups and Log Streams <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__ in the *Amazon CloudWatch User Guide.*
          For more information about how to useCloudWatchLogs with DataSync, see `Monitoring Your Task <https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html>`__ .
        :type Name: string
        :param Name:
          The name of a task. This value is a text reference that is used to identify the task in the console.
        :type Options: dict
        :param Options:
          The set of configuration options that control the behavior of a single execution of the task that occurs when you call ``StartTaskExecution`` . You can configure these options to preserve metadata such as user ID (UID) and group ID (GID), file permissions, data integrity verification, and so on.
          For each individual task execution, you can override these options by specifying the ``OverrideOptions`` before starting a the task execution. For more information, see the operation.
          - **VerifyMode** *(string) --*
            A value that determines whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred.
            Default value: POINT_IN_TIME_CONSISTENT.
            POINT_IN_TIME_CONSISTENT: Perform verification (recommended).
            NONE: Skip verification.
          - **Atime** *(string) --*
            A file metadata value that shows the last time a file was accessed (that is, when the file was read or written to). If you set ``Atime`` to BEST_EFFORT, DataSync attempts to preserve the original ``Atime`` attribute on all source files (that is, the version before the PREPARING phase). However, ``Atime`` \'s behavior is not fully standard across platforms, so AWS DataSync can only do this on a best-effort basis.
            Default value: BEST_EFFORT.
            BEST_EFFORT: Attempt to preserve the per-file ``Atime`` value (recommended).
            NONE: Ignore ``Atime`` .
            .. note::
              If ``Atime`` is set to BEST_EFFORT, ``Mtime`` must be set to PRESERVE.
              If ``Atime`` is set to NONE, ``Mtime`` must also be NONE.
          - **Mtime** *(string) --*
            A value that indicates the last time that a file was modified (that is, a file was written to) before the PREPARING phase.
            Default value: PRESERVE.
            PRESERVE: Preserve original ``Mtime`` (recommended)
            NONE: Ignore ``Mtime`` .
            .. note::
              If ``Mtime`` is set to PRESERVE, ``Atime`` must be set to BEST_EFFORT.
              If ``Mtime`` is set to NONE, ``Atime`` must also be set to NONE.
          - **Uid** *(string) --*
            The user ID (UID) of the file\'s owner.
            Default value: INT_VALUE. This preserves the integer value of the ID.
            INT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).
            NONE: Ignore UID and GID.
          - **Gid** *(string) --*
            The group ID (GID) of the file\'s owners.
            Default value: INT_VALUE. This preserves the integer value of the ID.
            INT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).
            NONE: Ignore UID and GID.
          - **PreserveDeletedFiles** *(string) --*
            A value that specifies whether files in the destination that don\'t exist in the source file system should be preserved.
            Default value: PRESERVE.
            PRESERVE: Ignore such destination files (recommended).
            REMOVE: Delete destination files that aren’t present in the source.
          - **PreserveDevices** *(string) --*
            A value that determines whether AWS DataSync should preserve the metadata of block and character devices in the source file system, and recreate the files with that device name and metadata on the destination.
            .. note::
              AWS DataSync can\'t sync the actual contents of such devices, because they are nonterminal and don\'t return an end-of-file (EOF) marker.
            Default value: NONE.
            NONE: Ignore special devices (recommended).
            PRESERVE: Preserve character and block device metadata. This option isn\'t currently supported for Amazon EFS.
          - **PosixPermissions** *(string) --*
            A value that determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file.
            Default value: PRESERVE.
            PRESERVE: Preserve POSIX-style permissions (recommended).
            NONE: Ignore permissions.
            .. note::
              AWS DataSync can preserve extant permissions of a source location.
          - **BytesPerSecond** *(integer) --*
            A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS DataSync to use a maximum of 1 MB, set this value to ``1048576`` (``=1024*1024`` ).
        :type Tags: list
        :param Tags:
          The key-value pair that represents the tag that you want to add to the resource. The value can be an empty string.
          - *(dict) --*
            Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array that contains a list of tasks when the  ListTagsForResource operation is called.
            - **Key** *(string) --*
              The key for an AWS resource tag.
            - **Value** *(string) --*
              The value for an AWS resource tag.
        :rtype: dict
        :returns:
        """
        pass

    def delete_agent(self, AgentArn: str) -> Dict:
        """
        Deletes an agent. To specify which agent to delete, use the Amazon Resource Name (ARN) of the agent in your request. The operation disassociates the agent from your AWS account. However, it doesn't delete the agent virtual machine (VM) from your on-premises environment.
        .. note::
          After you delete an agent, you can't reactivate it and you longer pay software charges for it.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/DeleteAgent>`_
        
        **Request Syntax**
        ::
          response = client.delete_agent(
              AgentArn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AgentArn: string
        :param AgentArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the agent to delete. Use the ``ListAgents`` operation to return a list of agents for your account and AWS Region.
        :rtype: dict
        :returns:
        """
        pass

    def delete_location(self, LocationArn: str) -> Dict:
        """
        Deletes the configuration of a location used by AWS DataSync. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/DeleteLocation>`_
        
        **Request Syntax**
        ::
          response = client.delete_location(
              LocationArn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type LocationArn: string
        :param LocationArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the location to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_task(self, TaskArn: str) -> Dict:
        """
        Deletes a task.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/DeleteTask>`_
        
        **Request Syntax**
        ::
          response = client.delete_task(
              TaskArn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type TaskArn: string
        :param TaskArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the task to delete.
        :rtype: dict
        :returns:
        """
        pass

    def describe_agent(self, AgentArn: str) -> Dict:
        """
        Returns metadata such as the name, the network interfaces, and the status (that is, whether the agent is running or not) for an agent. To specify which agent to describe, use the Amazon Resource Name (ARN) of the agent in your request. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/DescribeAgent>`_
        
        **Request Syntax**
        ::
          response = client.describe_agent(
              AgentArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'AgentArn': 'string',
                'Name': 'string',
                'Status': 'ONLINE'|'OFFLINE',
                'LastConnectionTime': datetime(2015, 1, 1),
                'CreationTime': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            DescribeAgentResponse
            - **AgentArn** *(string) --* 
              The Amazon Resource Name (ARN) of the agent.
            - **Name** *(string) --* 
              The name of the agent.
            - **Status** *(string) --* 
              The status of the agent. If the status is ONLINE, then the agent is configured properly and is available to use. The Running status is the normal running status for an agent. If the status is OFFLINE, the agent's VM is turned off or the agent is in an unhealthy state. When the issue that caused the unhealthy state is resolved, the agent returns to ONLINE status.
            - **LastConnectionTime** *(datetime) --* 
              The time that the agent was last connected.
            - **CreationTime** *(datetime) --* 
              The time that the agent was activated (that is, created in your account).
        :type AgentArn: string
        :param AgentArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the agent to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_location_efs(self, LocationArn: str) -> Dict:
        """
        Returns metadata, such as the path information about an Amazon EFS location.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/DescribeLocationEfs>`_
        
        **Request Syntax**
        ::
          response = client.describe_location_efs(
              LocationArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'LocationArn': 'string',
                'LocationUri': 'string',
                'Ec2Config': {
                    'SubnetArn': 'string',
                    'SecurityGroupArns': [
                        'string',
                    ]
                },
                'CreationTime': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            DescribeLocationEfsResponse
            - **LocationArn** *(string) --* 
              The Amazon resource Name (ARN) of the EFS location that was described.
            - **LocationUri** *(string) --* 
              The URL of the EFS location that was described.
            - **Ec2Config** *(dict) --* 
              The subnet and the security group that the target Amazon EFS file system uses. The subnet must have at least one mount target for that file system. The security group that you provide needs to be able to communicate with the security group on the mount target in the subnet specified. 
              The exact relationship between security group M (of the mount target) and security group S (which you provide for DataSync to use at this stage) is as follows: 
              * Security group M (which you associate with the mount target) must allow inbound access for the Transmission Control Protocol (TCP) on the NFS port (2049) from security group S. You can enable inbound connections either by IP address (CIDR range) or security group.  
              * Security group S (provided to DataSync to access EFS) should have a rule that enables outbound connections to the NFS port on one of the file system’s mount targets. You can enable outbound connections either by IP address (CIDR range) or security group. For information about security groups and mount targets, see `Security Groups for Amazon EC2 Instances and Mount Targets <https://docs.aws.amazon.com/efs/latest/ug/security-considerations.html#network-access>`__ in the *Amazon EFS User Guide.*   
              - **SubnetArn** *(string) --* 
                The ARN of the subnet that the Amazon EC2 resource belongs in. 
              - **SecurityGroupArns** *(list) --* 
                The Amazon Resource Names (ARNs) of the security groups that are configured for the Amazon EC2 resource.
                - *(string) --* 
            - **CreationTime** *(datetime) --* 
              The time that the EFS location was created.
        :type LocationArn: string
        :param LocationArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the EFS location to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_location_nfs(self, LocationArn: str) -> Dict:
        """
        Returns metadata, such as the path information, about a NFS location.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/DescribeLocationNfs>`_
        
        **Request Syntax**
        ::
          response = client.describe_location_nfs(
              LocationArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'LocationArn': 'string',
                'LocationUri': 'string',
                'OnPremConfig': {
                    'AgentArns': [
                        'string',
                    ]
                },
                'CreationTime': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            DescribeLocationNfsResponse
            - **LocationArn** *(string) --* 
              The Amazon resource Name (ARN) of the NFS location that was described.
            - **LocationUri** *(string) --* 
              The URL of the source NFS location that was described.
            - **OnPremConfig** *(dict) --* 
              A list of Amazon Resource Names (ARNs) of agents to use for a Network File System (NFS) location.
              - **AgentArns** *(list) --* 
                ARNs)of the agents to use for an NFS location.
                - *(string) --* 
            - **CreationTime** *(datetime) --* 
              The time that the NFS location was created.
        :type LocationArn: string
        :param LocationArn: **[REQUIRED]**
          The Amazon resource Name (ARN) of the NFS location to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_location_s3(self, LocationArn: str) -> Dict:
        """
        Returns metadata, such as bucket name, about an Amazon S3 bucket location.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/DescribeLocationS3>`_
        
        **Request Syntax**
        ::
          response = client.describe_location_s3(
              LocationArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'LocationArn': 'string',
                'LocationUri': 'string',
                'S3Config': {
                    'BucketAccessRoleArn': 'string'
                },
                'CreationTime': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            DescribeLocationS3Response
            - **LocationArn** *(string) --* 
              The Amazon Resource Name (ARN) of the Amazon S3 bucket location.
            - **LocationUri** *(string) --* 
              The URL of the Amazon S3 location that was described.
            - **S3Config** *(dict) --* 
              The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that is used to access an Amazon S3 bucket. For detailed information about using such a role, see `Components and Terminology <https://alpha-aws-docs.aws.amazon.com/sync-service/latest/userguide/create-locations-cli.html#create-location-s3-cli>`__ in the *AWS DataSync User Guide* .
              - **BucketAccessRoleArn** *(string) --* 
                The Amazon S3 bucket to access. This bucket is used as a parameter in the  CreateLocationS3 operation. 
            - **CreationTime** *(datetime) --* 
              The time that the Amazon S3 bucket location was created.
        :type LocationArn: string
        :param LocationArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the Amazon S3 bucket location to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_task(self, TaskArn: str) -> Dict:
        """
        Returns metadata about a task.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/DescribeTask>`_
        
        **Request Syntax**
        ::
          response = client.describe_task(
              TaskArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'TaskArn': 'string',
                'Status': 'AVAILABLE'|'CREATING'|'RUNNING'|'UNAVAILABLE',
                'Name': 'string',
                'CurrentTaskExecutionArn': 'string',
                'SourceLocationArn': 'string',
                'DestinationLocationArn': 'string',
                'CloudWatchLogGroupArn': 'string',
                'Options': {
                    'VerifyMode': 'POINT_IN_TIME_CONSISTENT'|'NONE',
                    'Atime': 'NONE'|'BEST_EFFORT',
                    'Mtime': 'NONE'|'PRESERVE',
                    'Uid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
                    'Gid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
                    'PreserveDeletedFiles': 'PRESERVE'|'REMOVE',
                    'PreserveDevices': 'NONE'|'PRESERVE',
                    'PosixPermissions': 'NONE'|'BEST_EFFORT'|'PRESERVE',
                    'BytesPerSecond': 123
                },
                'ErrorCode': 'string',
                'ErrorDetail': 'string',
                'CreationTime': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            DescribeTaskResponse
            - **TaskArn** *(string) --* 
              The Amazon Resource Name (ARN) of the task that was described.
            - **Status** *(string) --* 
              The status of the task that was described. For detailed information about sync statuses, see `Understanding Sync Task Statuses <https://docs.aws.amazon.com/sync-service/latest/userguide/understand-sync-task-statuses.html>`__ .
            - **Name** *(string) --* 
              The name of the task that was described.
            - **CurrentTaskExecutionArn** *(string) --* 
              The Amazon Resource Name (ARN) of the task execution that is syncing files.
            - **SourceLocationArn** *(string) --* 
              The Amazon Resource Name (ARN) of the source file system's location.
            - **DestinationLocationArn** *(string) --* 
              The Amazon Resource Name (ARN) of the AWS storage resource's location.
            - **CloudWatchLogGroupArn** *(string) --* 
              The Amazon Resource Name (ARN) of the Amazon CloudWatch log group that was used to monitor and log events in the task. For more information on these groups, see `Working with Log Groups and Log Streams <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__ in the *Amazon CloudWatch User Guide.*  
            - **Options** *(dict) --* 
              The set of configuration options that control the behavior of a single execution of the task that occurs when you call ``StartTaskExecution`` . You can configure these options to preserve metadata such as user ID (UID) and group (GID), file permissions, data integrity verification, and so on.
              For each individual task execution, you can override these options by specifying the overriding ``OverrideOptions`` value to operation. 
              - **VerifyMode** *(string) --* 
                A value that determines whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred. 
                Default value: POINT_IN_TIME_CONSISTENT.
                POINT_IN_TIME_CONSISTENT: Perform verification (recommended). 
                NONE: Skip verification.
              - **Atime** *(string) --* 
                A file metadata value that shows the last time a file was accessed (that is, when the file was read or written to). If you set ``Atime`` to BEST_EFFORT, DataSync attempts to preserve the original ``Atime`` attribute on all source files (that is, the version before the PREPARING phase). However, ``Atime`` 's behavior is not fully standard across platforms, so AWS DataSync can only do this on a best-effort basis. 
                Default value: BEST_EFFORT.
                BEST_EFFORT: Attempt to preserve the per-file ``Atime`` value (recommended).
                NONE: Ignore ``Atime`` .
                .. note::
                  If ``Atime`` is set to BEST_EFFORT, ``Mtime`` must be set to PRESERVE. 
                  If ``Atime`` is set to NONE, ``Mtime`` must also be NONE. 
              - **Mtime** *(string) --* 
                A value that indicates the last time that a file was modified (that is, a file was written to) before the PREPARING phase. 
                Default value: PRESERVE. 
                PRESERVE: Preserve original ``Mtime`` (recommended)
                NONE: Ignore ``Mtime`` . 
                .. note::
                  If ``Mtime`` is set to PRESERVE, ``Atime`` must be set to BEST_EFFORT.
                  If ``Mtime`` is set to NONE, ``Atime`` must also be set to NONE. 
              - **Uid** *(string) --* 
                The user ID (UID) of the file's owner. 
                Default value: INT_VALUE. This preserves the integer value of the ID.
                INT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).
                NONE: Ignore UID and GID. 
              - **Gid** *(string) --* 
                The group ID (GID) of the file's owners. 
                Default value: INT_VALUE. This preserves the integer value of the ID.
                INT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).
                NONE: Ignore UID and GID. 
              - **PreserveDeletedFiles** *(string) --* 
                A value that specifies whether files in the destination that don't exist in the source file system should be preserved. 
                Default value: PRESERVE.
                PRESERVE: Ignore such destination files (recommended). 
                REMOVE: Delete destination files that aren’t present in the source.
              - **PreserveDevices** *(string) --* 
                A value that determines whether AWS DataSync should preserve the metadata of block and character devices in the source file system, and recreate the files with that device name and metadata on the destination.
                .. note::
                  AWS DataSync can't sync the actual contents of such devices, because they are nonterminal and don't return an end-of-file (EOF) marker.
                Default value: NONE.
                NONE: Ignore special devices (recommended). 
                PRESERVE: Preserve character and block device metadata. This option isn't currently supported for Amazon EFS. 
              - **PosixPermissions** *(string) --* 
                A value that determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file. 
                Default value: PRESERVE.
                PRESERVE: Preserve POSIX-style permissions (recommended).
                NONE: Ignore permissions. 
                .. note::
                  AWS DataSync can preserve extant permissions of a source location.
              - **BytesPerSecond** *(integer) --* 
                A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS DataSync to use a maximum of 1 MB, set this value to ``1048576`` (``=1024*1024`` ).
            - **ErrorCode** *(string) --* 
              Errors that AWS DataSync encountered during execution of the task. You can use this error code to help troubleshoot issues.
            - **ErrorDetail** *(string) --* 
              Detailed description of an error that was encountered during the task execution. You can use this information to help troubleshoot issues. 
            - **CreationTime** *(datetime) --* 
              The time that the task was created.
        :type TaskArn: string
        :param TaskArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the task to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_task_execution(self, TaskExecutionArn: str) -> Dict:
        """
        Returns detailed metadata about a task that is being executed.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/DescribeTaskExecution>`_
        
        **Request Syntax**
        ::
          response = client.describe_task_execution(
              TaskExecutionArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'TaskExecutionArn': 'string',
                'Status': 'LAUNCHING'|'PREPARING'|'TRANSFERRING'|'VERIFYING'|'SUCCESS'|'ERROR',
                'Options': {
                    'VerifyMode': 'POINT_IN_TIME_CONSISTENT'|'NONE',
                    'Atime': 'NONE'|'BEST_EFFORT',
                    'Mtime': 'NONE'|'PRESERVE',
                    'Uid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
                    'Gid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
                    'PreserveDeletedFiles': 'PRESERVE'|'REMOVE',
                    'PreserveDevices': 'NONE'|'PRESERVE',
                    'PosixPermissions': 'NONE'|'BEST_EFFORT'|'PRESERVE',
                    'BytesPerSecond': 123
                },
                'StartTime': datetime(2015, 1, 1),
                'EstimatedFilesToTransfer': 123,
                'EstimatedBytesToTransfer': 123,
                'FilesTransferred': 123,
                'BytesWritten': 123,
                'BytesTransferred': 123,
                'Result': {
                    'PrepareDuration': 123,
                    'PrepareStatus': 'PENDING'|'SUCCESS'|'ERROR',
                    'TransferDuration': 123,
                    'TransferStatus': 'PENDING'|'SUCCESS'|'ERROR',
                    'VerifyDuration': 123,
                    'VerifyStatus': 'PENDING'|'SUCCESS'|'ERROR',
                    'ErrorCode': 'string',
                    'ErrorDetail': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            DescribeTaskExecutionResponse
            - **TaskExecutionArn** *(string) --* 
              The Amazon Resource Name (ARN) of the task execution that was described. ``TaskExecutionArn`` is hierarchical and includes ``TaskArn`` for the task that was executed. 
              For example, a ``TaskExecution`` value with the ARN ``arn:aws:sync:us-east-1:209870788375:task/task-0208075f79cedf4a2/execution/exec-08ef1e88ec491019b`` executed the task with the ARN ``arn:aws:sync:us-east-1:209870788375:task/task-0208075f79cedf4a2`` . 
            - **Status** *(string) --* 
              The status of the task. For detailed information about sync statuses, see `Understanding Sync Task Statuses <https://docs.aws.amazon.com/sync-service/latest/userguide/understand-sync-task-statuses.html>`__ .
            - **Options** *(dict) --* 
              Represents the options that are available to control the behavior of a  StartTaskExecution operation. Behavior includes preserving metadata such as user ID (UID), group ID (GID), and file permissions, and also overwriting files in the destination, data integrity verification, and so on.
              A task has a set of default options associated with it. If you don't specify an option in  StartTaskExecution , the default value is used. You can override the defaults options on each task execution by specifying an overriding ``Options`` value to  StartTaskExecution .
              - **VerifyMode** *(string) --* 
                A value that determines whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred. 
                Default value: POINT_IN_TIME_CONSISTENT.
                POINT_IN_TIME_CONSISTENT: Perform verification (recommended). 
                NONE: Skip verification.
              - **Atime** *(string) --* 
                A file metadata value that shows the last time a file was accessed (that is, when the file was read or written to). If you set ``Atime`` to BEST_EFFORT, DataSync attempts to preserve the original ``Atime`` attribute on all source files (that is, the version before the PREPARING phase). However, ``Atime`` 's behavior is not fully standard across platforms, so AWS DataSync can only do this on a best-effort basis. 
                Default value: BEST_EFFORT.
                BEST_EFFORT: Attempt to preserve the per-file ``Atime`` value (recommended).
                NONE: Ignore ``Atime`` .
                .. note::
                  If ``Atime`` is set to BEST_EFFORT, ``Mtime`` must be set to PRESERVE. 
                  If ``Atime`` is set to NONE, ``Mtime`` must also be NONE. 
              - **Mtime** *(string) --* 
                A value that indicates the last time that a file was modified (that is, a file was written to) before the PREPARING phase. 
                Default value: PRESERVE. 
                PRESERVE: Preserve original ``Mtime`` (recommended)
                NONE: Ignore ``Mtime`` . 
                .. note::
                  If ``Mtime`` is set to PRESERVE, ``Atime`` must be set to BEST_EFFORT.
                  If ``Mtime`` is set to NONE, ``Atime`` must also be set to NONE. 
              - **Uid** *(string) --* 
                The user ID (UID) of the file's owner. 
                Default value: INT_VALUE. This preserves the integer value of the ID.
                INT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).
                NONE: Ignore UID and GID. 
              - **Gid** *(string) --* 
                The group ID (GID) of the file's owners. 
                Default value: INT_VALUE. This preserves the integer value of the ID.
                INT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).
                NONE: Ignore UID and GID. 
              - **PreserveDeletedFiles** *(string) --* 
                A value that specifies whether files in the destination that don't exist in the source file system should be preserved. 
                Default value: PRESERVE.
                PRESERVE: Ignore such destination files (recommended). 
                REMOVE: Delete destination files that aren’t present in the source.
              - **PreserveDevices** *(string) --* 
                A value that determines whether AWS DataSync should preserve the metadata of block and character devices in the source file system, and recreate the files with that device name and metadata on the destination.
                .. note::
                  AWS DataSync can't sync the actual contents of such devices, because they are nonterminal and don't return an end-of-file (EOF) marker.
                Default value: NONE.
                NONE: Ignore special devices (recommended). 
                PRESERVE: Preserve character and block device metadata. This option isn't currently supported for Amazon EFS. 
              - **PosixPermissions** *(string) --* 
                A value that determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file. 
                Default value: PRESERVE.
                PRESERVE: Preserve POSIX-style permissions (recommended).
                NONE: Ignore permissions. 
                .. note::
                  AWS DataSync can preserve extant permissions of a source location.
              - **BytesPerSecond** *(integer) --* 
                A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS DataSync to use a maximum of 1 MB, set this value to ``1048576`` (``=1024*1024`` ).
            - **StartTime** *(datetime) --* 
              The time that the task execution was started.
            - **EstimatedFilesToTransfer** *(integer) --* 
              The expected number of files that is to be transferred over the network. This value is calculated during the PREPARING phase, before the TRANSFERRING phase. This value is the expected number of files to be transferred. It's calculated based on comparing the content of the source and destination locations and finding the delta that needs to be transferred. 
            - **EstimatedBytesToTransfer** *(integer) --* 
              The estimated physical number of bytes that is to be transferred over the network.
            - **FilesTransferred** *(integer) --* 
              The actual number of files that was transferred over the network. This value is calculated and updated on an ongoing basis during the TRANSFERRING phase. It's updated periodically when each file is read from the source and sent over the network. 
              If failures occur during a transfer, this value can be less than ``EstimatedFilesToTransfer`` . This value can also be greater than ``EstimatedFilesTransferred`` in some cases. This element is implementation-specific for some location types, so don't use it as an indicator for a correct file number or to monitor your task execution.
            - **BytesWritten** *(integer) --* 
              The number of logical bytes written to the destination AWS storage resource.
            - **BytesTransferred** *(integer) --* 
              The physical number of bytes transferred over the network.
            - **Result** *(dict) --* 
              The result of the task execution.
              - **PrepareDuration** *(integer) --* 
                The total time in milliseconds that AWS DataSync spent in the PREPARING phase. 
              - **PrepareStatus** *(string) --* 
                The status of the PREPARING phase.
              - **TransferDuration** *(integer) --* 
                The total time in milliseconds that AWS DataSync spent in the TRANSFERRING phase.
              - **TransferStatus** *(string) --* 
                The status of the TRANSFERRING Phase.
              - **VerifyDuration** *(integer) --* 
                The total time in milliseconds that AWS DataSync spent in the VERIFYING phase.
              - **VerifyStatus** *(string) --* 
                The status of the VERIFYING Phase.
              - **ErrorCode** *(string) --* 
                Errors that AWS DataSync encountered during execution of the task. You can use this error code to help troubleshoot issues.
              - **ErrorDetail** *(string) --* 
                Detailed description of an error that was encountered during the task execution. You can use this information to help troubleshoot issues. 
        :type TaskExecutionArn: string
        :param TaskExecutionArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the task that is being executed.
        :rtype: dict
        :returns:
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        """
        Generate a presigned url given a client, its method, and arguments
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
        Create a paginator for an operation.
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
        Returns an object that can wait for some condition.
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def list_agents(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Returns a list of agents owned by an AWS account in the AWS Region specified in the request. The returned list is ordered by agent Amazon Resource Name (ARN).
        By default, this operation returns a maximum of 100 agents. This operation supports pagination that enables you to optionally reduce the number of agents returned in a response.
        If you have more agents than are returned in a response (that is, the response returns only a truncated list of your agents), the response contains a marker that you can specify in your next request to fetch the next page of agents.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/ListAgents>`_
        
        **Request Syntax**
        ::
          response = client.list_agents(
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Agents': [
                    {
                        'AgentArn': 'string',
                        'Name': 'string',
                        'Status': 'ONLINE'|'OFFLINE'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            ListAgentsResponse
            - **Agents** *(list) --* 
              A list of agents in your account.
              - *(dict) --* 
                Represents a single entry in a list of agents. ``AgentListEntry`` returns an array that contains a list of agents when the  ListAgents operation is called.
                - **AgentArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the agent.
                - **Name** *(string) --* 
                  The name of the agent.
                - **Status** *(string) --* 
                  The status of the agent.
            - **NextToken** *(string) --* 
              An opaque string that indicates the position at which to begin returning the next list of agents.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of agents to list.
        :type NextToken: string
        :param NextToken:
          An opaque string that indicates the position at which to begin the next list of agents.
        :rtype: dict
        :returns:
        """
        pass

    def list_locations(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Returns a lists of source and destination locations.
        If you have more locations than are returned in a response (that is, the response returns only a truncated list of your agents), the response contains a token that you can specify in your next request to fetch the next page of locations.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/ListLocations>`_
        
        **Request Syntax**
        ::
          response = client.list_locations(
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Locations': [
                    {
                        'LocationArn': 'string',
                        'LocationUri': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            ListLocationsResponse
            - **Locations** *(list) --* 
              An array that contains a list of locations.
              - *(dict) --* 
                Represents a single entry in a list of locations. ``LocationListEntry`` returns an array that contains a list of locations when the  ListLocations operation is called.
                - **LocationArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the location. For Network File System (NFS) or Amazon EFS, the location is the export path. For Amazon S3, the location is the prefix path that you want to mount and use as the root of the location.
                - **LocationUri** *(string) --* 
                  Represents a list of URLs of a location. ``LocationUri`` returns an array that contains a list of locations when the  ListLocations operation is called.
                  Format: ``TYPE://GLOBAL_ID/SUBDIR`` .
                  TYPE designates the type of location. Valid values: NFS | EFS | S3.
                  GLOBAL_ID is the globally unique identifier of the resource that backs the location. An example for EFS is ``us-east-2.fs-abcd1234`` . An example for Amazon S3 is the bucket name, such as ``myBucket`` . An example for NFS is a valid IPv4 address or a host name compliant with Domain Name Service (DNS).
                  SUBDIR is a valid file system path, delimited by forward slashes as is the *nix convention. For NFS and Amazon EFS, it's the export path to mount the location. For Amazon S3, it's the prefix path that you mount to and treat as the root of the location.
            - **NextToken** *(string) --* 
              An opaque string that indicates the position at which to begin returning the next list of locations.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of locations to return.
        :type NextToken: string
        :param NextToken:
          An opaque string that indicates the position at which to begin the next list of locations.
        :rtype: dict
        :returns:
        """
        pass

    def list_tags_for_resource(self, ResourceArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Returns all the tags associated with a specified resources. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/ListTagsForResource>`_
        
        **Request Syntax**
        ::
          response = client.list_tags_for_resource(
              ResourceArn='string',
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            ListTagsForResourceResponse
            - **Tags** *(list) --* 
              Array of resource tags.
              - *(dict) --* 
                Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array that contains a list of tasks when the  ListTagsForResource operation is called.
                - **Key** *(string) --* 
                  The key for an AWS resource tag.
                - **Value** *(string) --* 
                  The value for an AWS resource tag.
            - **NextToken** *(string) --* 
              An opaque string that indicates the position at which to begin returning the next list of resource tags.
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the resource whose tags to list.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of locations to return.
        :type NextToken: string
        :param NextToken:
          An opaque string that indicates the position at which to begin the next list of locations.
        :rtype: dict
        :returns:
        """
        pass

    def list_task_executions(self, TaskArn: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Returns a list of executed tasks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/ListTaskExecutions>`_
        
        **Request Syntax**
        ::
          response = client.list_task_executions(
              TaskArn='string',
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'TaskExecutions': [
                    {
                        'TaskExecutionArn': 'string',
                        'Status': 'LAUNCHING'|'PREPARING'|'TRANSFERRING'|'VERIFYING'|'SUCCESS'|'ERROR'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            ListTaskExecutionsResponse
            - **TaskExecutions** *(list) --* 
              A list of executed tasks.
              - *(dict) --* 
                Represents a single entry in a list of task executions. ``TaskExecutionListEntry`` returns an array that contains a list of specific invocations of a task when  ListTaskExecutions operation is called.
                - **TaskExecutionArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the task that was executed.
                - **Status** *(string) --* 
                  The status of a task execution.
            - **NextToken** *(string) --* 
              An opaque string that indicates the position at which to begin returning the next list of executed tasks.
        :type TaskArn: string
        :param TaskArn:
          The Amazon Resource Name (ARN) of the task whose tasks you want to list.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of executed tasks to list.
        :type NextToken: string
        :param NextToken:
          An opaque string that indicates the position at which to begin the next list of the executed tasks.
        :rtype: dict
        :returns:
        """
        pass

    def list_tasks(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Returns a list of all the tasks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/ListTasks>`_
        
        **Request Syntax**
        ::
          response = client.list_tasks(
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Tasks': [
                    {
                        'TaskArn': 'string',
                        'Status': 'AVAILABLE'|'CREATING'|'RUNNING'|'UNAVAILABLE',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            ListTasksResponse
            - **Tasks** *(list) --* 
              A list of all the tasks that are returned.
              - *(dict) --* 
                Represents a single entry in a list of tasks. ``TaskListEntry`` returns an array that contains a list of tasks when the  ListTasks operation is called. A task includes the source and destination file systems to sync and the options to use for the tasks.
                - **TaskArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the task.
                - **Status** *(string) --* 
                  The status of the task.
                - **Name** *(string) --* 
                  The name of the task.
            - **NextToken** *(string) --* 
              An opaque string that indicates the position at which to begin returning the next list of tasks.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of tasks to return.
        :type NextToken: string
        :param NextToken:
          An opaque string that indicates the position at which to begin the next list of tasks.
        :rtype: dict
        :returns:
        """
        pass

    def start_task_execution(self, TaskArn: str, OverrideOptions: Dict = None) -> Dict:
        """
        Starts a specific invocation of a task. A ``TaskExecution`` value represents an individual run of a task. Each task can have at most one ``TaskExecution`` at a time.
         ``TaskExecution`` has the following transition phases: INITIALIZING | PREPARING | TRANSFERRING | VERIFYING | SUCCESS/FAILURE. 
        For detailed information, see *Task Execution* in `Components and Terminology <https://docs.aws.amazon.com/sync-service/latest/userguide/how-awssync-works.html#terminology>`__ in the *AWS DataSync User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/StartTaskExecution>`_
        
        **Request Syntax**
        ::
          response = client.start_task_execution(
              TaskArn='string',
              OverrideOptions={
                  'VerifyMode': 'POINT_IN_TIME_CONSISTENT'|'NONE',
                  'Atime': 'NONE'|'BEST_EFFORT',
                  'Mtime': 'NONE'|'PRESERVE',
                  'Uid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
                  'Gid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
                  'PreserveDeletedFiles': 'PRESERVE'|'REMOVE',
                  'PreserveDevices': 'NONE'|'PRESERVE',
                  'PosixPermissions': 'NONE'|'BEST_EFFORT'|'PRESERVE',
                  'BytesPerSecond': 123
              }
          )
        
        **Response Syntax**
        ::
            {
                'TaskExecutionArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            StartTaskExecutionResponse
            - **TaskExecutionArn** *(string) --* 
              The Amazon Resource Name (ARN) of the specific task execution that was started.
        :type TaskArn: string
        :param TaskArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the task to start.
        :type OverrideOptions: dict
        :param OverrideOptions:
          Represents the options that are available to control the behavior of a  StartTaskExecution operation. Behavior includes preserving metadata such as user ID (UID), group ID (GID), and file permissions, and also overwriting files in the destination, data integrity verification, and so on.
          A task has a set of default options associated with it. If you don\'t specify an option in  StartTaskExecution , the default value is used. You can override the defaults options on each task execution by specifying an overriding ``Options`` value to  StartTaskExecution .
          - **VerifyMode** *(string) --*
            A value that determines whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred.
            Default value: POINT_IN_TIME_CONSISTENT.
            POINT_IN_TIME_CONSISTENT: Perform verification (recommended).
            NONE: Skip verification.
          - **Atime** *(string) --*
            A file metadata value that shows the last time a file was accessed (that is, when the file was read or written to). If you set ``Atime`` to BEST_EFFORT, DataSync attempts to preserve the original ``Atime`` attribute on all source files (that is, the version before the PREPARING phase). However, ``Atime`` \'s behavior is not fully standard across platforms, so AWS DataSync can only do this on a best-effort basis.
            Default value: BEST_EFFORT.
            BEST_EFFORT: Attempt to preserve the per-file ``Atime`` value (recommended).
            NONE: Ignore ``Atime`` .
            .. note::
              If ``Atime`` is set to BEST_EFFORT, ``Mtime`` must be set to PRESERVE.
              If ``Atime`` is set to NONE, ``Mtime`` must also be NONE.
          - **Mtime** *(string) --*
            A value that indicates the last time that a file was modified (that is, a file was written to) before the PREPARING phase.
            Default value: PRESERVE.
            PRESERVE: Preserve original ``Mtime`` (recommended)
            NONE: Ignore ``Mtime`` .
            .. note::
              If ``Mtime`` is set to PRESERVE, ``Atime`` must be set to BEST_EFFORT.
              If ``Mtime`` is set to NONE, ``Atime`` must also be set to NONE.
          - **Uid** *(string) --*
            The user ID (UID) of the file\'s owner.
            Default value: INT_VALUE. This preserves the integer value of the ID.
            INT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).
            NONE: Ignore UID and GID.
          - **Gid** *(string) --*
            The group ID (GID) of the file\'s owners.
            Default value: INT_VALUE. This preserves the integer value of the ID.
            INT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).
            NONE: Ignore UID and GID.
          - **PreserveDeletedFiles** *(string) --*
            A value that specifies whether files in the destination that don\'t exist in the source file system should be preserved.
            Default value: PRESERVE.
            PRESERVE: Ignore such destination files (recommended).
            REMOVE: Delete destination files that aren’t present in the source.
          - **PreserveDevices** *(string) --*
            A value that determines whether AWS DataSync should preserve the metadata of block and character devices in the source file system, and recreate the files with that device name and metadata on the destination.
            .. note::
              AWS DataSync can\'t sync the actual contents of such devices, because they are nonterminal and don\'t return an end-of-file (EOF) marker.
            Default value: NONE.
            NONE: Ignore special devices (recommended).
            PRESERVE: Preserve character and block device metadata. This option isn\'t currently supported for Amazon EFS.
          - **PosixPermissions** *(string) --*
            A value that determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file.
            Default value: PRESERVE.
            PRESERVE: Preserve POSIX-style permissions (recommended).
            NONE: Ignore permissions.
            .. note::
              AWS DataSync can preserve extant permissions of a source location.
          - **BytesPerSecond** *(integer) --*
            A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS DataSync to use a maximum of 1 MB, set this value to ``1048576`` (``=1024*1024`` ).
        :rtype: dict
        :returns:
        """
        pass

    def tag_resource(self, ResourceArn: str, Tags: List) -> Dict:
        """
        Applies a key-value pair to an AWS resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/TagResource>`_
        
        **Request Syntax**
        ::
          response = client.tag_resource(
              ResourceArn='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the resource to apply the tag to.
        :type Tags: list
        :param Tags: **[REQUIRED]**
          The tags to apply.
          - *(dict) --*
            Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array that contains a list of tasks when the  ListTagsForResource operation is called.
            - **Key** *(string) --*
              The key for an AWS resource tag.
            - **Value** *(string) --*
              The value for an AWS resource tag.
        :rtype: dict
        :returns:
        """
        pass

    def untag_resource(self, ResourceArn: str, Keys: List) -> Dict:
        """
        Removes a tag from an AWS resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/UntagResource>`_
        
        **Request Syntax**
        ::
          response = client.untag_resource(
              ResourceArn='string',
              Keys=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the resource to remove the tag from.
        :type Keys: list
        :param Keys: **[REQUIRED]**
          The keys in the key-value pair in the tag to remove.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def update_agent(self, AgentArn: str, Name: str = None) -> Dict:
        """
        Updates the name of an agent.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/UpdateAgent>`_
        
        **Request Syntax**
        ::
          response = client.update_agent(
              AgentArn='string',
              Name='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AgentArn: string
        :param AgentArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the agent to update.
        :type Name: string
        :param Name:
          The name that you want to use to configure the agent.
        :rtype: dict
        :returns:
        """
        pass

    def update_task(self, TaskArn: str, Options: Dict = None, Name: str = None) -> Dict:
        """
        Updates the metadata associated with a task.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/UpdateTask>`_
        
        **Request Syntax**
        ::
          response = client.update_task(
              TaskArn='string',
              Options={
                  'VerifyMode': 'POINT_IN_TIME_CONSISTENT'|'NONE',
                  'Atime': 'NONE'|'BEST_EFFORT',
                  'Mtime': 'NONE'|'PRESERVE',
                  'Uid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
                  'Gid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
                  'PreserveDeletedFiles': 'PRESERVE'|'REMOVE',
                  'PreserveDevices': 'NONE'|'PRESERVE',
                  'PosixPermissions': 'NONE'|'BEST_EFFORT'|'PRESERVE',
                  'BytesPerSecond': 123
              },
              Name='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type TaskArn: string
        :param TaskArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the resource name of the task to update.
        :type Options: dict
        :param Options:
          Represents the options that are available to control the behavior of a  StartTaskExecution operation. Behavior includes preserving metadata such as user ID (UID), group ID (GID), and file permissions, and also overwriting files in the destination, data integrity verification, and so on.
          A task has a set of default options associated with it. If you don\'t specify an option in  StartTaskExecution , the default value is used. You can override the defaults options on each task execution by specifying an overriding ``Options`` value to  StartTaskExecution .
          - **VerifyMode** *(string) --*
            A value that determines whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred.
            Default value: POINT_IN_TIME_CONSISTENT.
            POINT_IN_TIME_CONSISTENT: Perform verification (recommended).
            NONE: Skip verification.
          - **Atime** *(string) --*
            A file metadata value that shows the last time a file was accessed (that is, when the file was read or written to). If you set ``Atime`` to BEST_EFFORT, DataSync attempts to preserve the original ``Atime`` attribute on all source files (that is, the version before the PREPARING phase). However, ``Atime`` \'s behavior is not fully standard across platforms, so AWS DataSync can only do this on a best-effort basis.
            Default value: BEST_EFFORT.
            BEST_EFFORT: Attempt to preserve the per-file ``Atime`` value (recommended).
            NONE: Ignore ``Atime`` .
            .. note::
              If ``Atime`` is set to BEST_EFFORT, ``Mtime`` must be set to PRESERVE.
              If ``Atime`` is set to NONE, ``Mtime`` must also be NONE.
          - **Mtime** *(string) --*
            A value that indicates the last time that a file was modified (that is, a file was written to) before the PREPARING phase.
            Default value: PRESERVE.
            PRESERVE: Preserve original ``Mtime`` (recommended)
            NONE: Ignore ``Mtime`` .
            .. note::
              If ``Mtime`` is set to PRESERVE, ``Atime`` must be set to BEST_EFFORT.
              If ``Mtime`` is set to NONE, ``Atime`` must also be set to NONE.
          - **Uid** *(string) --*
            The user ID (UID) of the file\'s owner.
            Default value: INT_VALUE. This preserves the integer value of the ID.
            INT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).
            NONE: Ignore UID and GID.
          - **Gid** *(string) --*
            The group ID (GID) of the file\'s owners.
            Default value: INT_VALUE. This preserves the integer value of the ID.
            INT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).
            NONE: Ignore UID and GID.
          - **PreserveDeletedFiles** *(string) --*
            A value that specifies whether files in the destination that don\'t exist in the source file system should be preserved.
            Default value: PRESERVE.
            PRESERVE: Ignore such destination files (recommended).
            REMOVE: Delete destination files that aren’t present in the source.
          - **PreserveDevices** *(string) --*
            A value that determines whether AWS DataSync should preserve the metadata of block and character devices in the source file system, and recreate the files with that device name and metadata on the destination.
            .. note::
              AWS DataSync can\'t sync the actual contents of such devices, because they are nonterminal and don\'t return an end-of-file (EOF) marker.
            Default value: NONE.
            NONE: Ignore special devices (recommended).
            PRESERVE: Preserve character and block device metadata. This option isn\'t currently supported for Amazon EFS.
          - **PosixPermissions** *(string) --*
            A value that determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file.
            Default value: PRESERVE.
            PRESERVE: Preserve POSIX-style permissions (recommended).
            NONE: Ignore permissions.
            .. note::
              AWS DataSync can preserve extant permissions of a source location.
          - **BytesPerSecond** *(integer) --*
            A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS DataSync to use a maximum of 1 MB, set this value to ``1048576`` (``=1024*1024`` ).
        :type Name: string
        :param Name:
          The name of the task to update.
        :rtype: dict
        :returns:
        """
        pass
