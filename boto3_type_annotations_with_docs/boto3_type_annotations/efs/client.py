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

    def create_file_system(self, CreationToken: str, PerformanceMode: str = None, Encrypted: bool = None, KmsKeyId: str = None, ThroughputMode: str = None, ProvisionedThroughputInMibps: float = None) -> Dict:
        """
        Creates a new, empty file system. The operation requires a creation token in the request that Amazon EFS uses to ensure idempotent creation (calling the operation with same creation token has no effect). If a file system does not currently exist that is owned by the caller\'s AWS account with the specified creation token, this operation does the following:
        
        * Creates a new, empty file system. The file system will have an Amazon EFS assigned ID, and an initial lifecycle state ``creating`` . 
         
        * Returns with the description of the created file system. 
         
        Otherwise, this operation returns a ``FileSystemAlreadyExists`` error with the ID of the existing file system.
        
        .. note::
        
          For basic use cases, you can use a randomly generated UUID for the creation token.
        
        The idempotent operation allows you to retry a ``CreateFileSystem`` call without risk of creating an extra file system. This can happen when an initial call fails in a way that leaves it uncertain whether or not a file system was actually created. An example might be that a transport level timeout occurred or your connection was reset. As long as you use the same creation token, if the initial call had succeeded in creating a file system, the client can learn of its existence from the ``FileSystemAlreadyExists`` error.
        
        .. note::
        
          The ``CreateFileSystem`` call returns while the file system\'s lifecycle state is still ``creating`` . You can check the file system creation status by calling the  DescribeFileSystems operation, which among other things returns the file system state.
        
        This operation also takes an optional ``PerformanceMode`` parameter that you choose for your file system. We recommend ``generalPurpose`` performance mode for most file systems. File systems using the ``maxIO`` performance mode can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for most file operations. The performance mode can\'t be changed after the file system has been created. For more information, see `Amazon EFS\: Performance Modes <http://docs.aws.amazon.com/efs/latest/ug/performance.html#performancemodes.html>`__ .
        
        After the file system is fully created, Amazon EFS sets its lifecycle state to ``available`` , at which point you can create one or more mount targets for the file system in your VPC. For more information, see  CreateMountTarget . You mount your Amazon EFS file system on an EC2 instances in your VPC via the mount target. For more information, see `Amazon EFS\: How it Works <http://docs.aws.amazon.com/efs/latest/ug/how-it-works.html>`__ . 
        
        This operation requires permissions for the ``elasticfilesystem:CreateFileSystem`` action. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/CreateFileSystem>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_file_system(
              CreationToken=\'string\',
              PerformanceMode=\'generalPurpose\'|\'maxIO\',
              Encrypted=True|False,
              KmsKeyId=\'string\',
              ThroughputMode=\'bursting\'|\'provisioned\',
              ProvisionedThroughputInMibps=123.0
          )
        :type CreationToken: string
        :param CreationToken: **[REQUIRED]** 
        
          String of up to 64 ASCII characters. Amazon EFS uses this to ensure idempotent creation.
        
        :type PerformanceMode: string
        :param PerformanceMode: 
        
          The ``PerformanceMode`` of the file system. We recommend ``generalPurpose`` performance mode for most file systems. File systems using the ``maxIO`` performance mode can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for most file operations. This can\'t be changed after the file system has been created.
        
        :type Encrypted: boolean
        :param Encrypted: 
        
          A Boolean value that, if true, creates an encrypted file system. When creating an encrypted file system, you have the option of specifying a  CreateFileSystemRequest$KmsKeyId for an existing AWS Key Management Service (AWS KMS) customer master key (CMK). If you don\'t specify a CMK, then the default CMK for Amazon EFS, ``/aws/elasticfilesystem`` , is used to protect the encrypted file system. 
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          The ID of the AWS KMS CMK to be used to protect the encrypted file system. This parameter is only required if you want to use a non-default CMK. If this parameter is not specified, the default CMK for Amazon EFS is used. This ID can be in one of the following formats:
        
          * Key ID - A unique identifier of the key, for example, ``1234abcd-12ab-34cd-56ef-1234567890ab`` . 
           
          * ARN - An Amazon Resource Name (ARN) for the key, for example, ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` . 
           
          * Key alias - A previously created display name for a key. For example, ``alias/projectKey1`` . 
           
          * Key alias ARN - An ARN for a key alias, for example, ``arn:aws:kms:us-west-2:444455556666:alias/projectKey1`` . 
           
          If KmsKeyId is specified, the  CreateFileSystemRequest$Encrypted parameter must be set to true.
        
        :type ThroughputMode: string
        :param ThroughputMode: 
        
          The throughput mode for the file system to be created. There are two throughput modes to choose from for your file system: bursting and provisioned. You can decrease your file system\'s throughput in Provisioned Throughput mode or change between the throughput modes as long as it’s been more than 24 hours since the last decrease or throughput mode change.
        
        :type ProvisionedThroughputInMibps: float
        :param ProvisionedThroughputInMibps: 
        
          The throughput, measured in MiB/s, that you want to provision for a file system that you\'re creating. The limit on throughput is 1024 MiB/s. You can get these limits increased by contacting AWS Support. For more information, see `Amazon EFS Limits That You Can Increase <http://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits>`__ in the *Amazon EFS User Guide.*  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OwnerId\': \'string\',
                \'CreationToken\': \'string\',
                \'FileSystemId\': \'string\',
                \'CreationTime\': datetime(2015, 1, 1),
                \'LifeCycleState\': \'creating\'|\'available\'|\'updating\'|\'deleting\'|\'deleted\',
                \'Name\': \'string\',
                \'NumberOfMountTargets\': 123,
                \'SizeInBytes\': {
                    \'Value\': 123,
                    \'Timestamp\': datetime(2015, 1, 1)
                },
                \'PerformanceMode\': \'generalPurpose\'|\'maxIO\',
                \'Encrypted\': True|False,
                \'KmsKeyId\': \'string\',
                \'ThroughputMode\': \'bursting\'|\'provisioned\',
                \'ProvisionedThroughputInMibps\': 123.0
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Description of the file system.
        
            - **OwnerId** *(string) --* 
        
              AWS account that created the file system. If the file system was created by an IAM user, the parent account to which the user belongs is the owner.
        
            - **CreationToken** *(string) --* 
        
              Opaque string specified in the request.
        
            - **FileSystemId** *(string) --* 
        
              ID of the file system, assigned by Amazon EFS.
        
            - **CreationTime** *(datetime) --* 
        
              Time that the file system was created, in seconds (since 1970-01-01T00:00:00Z).
        
            - **LifeCycleState** *(string) --* 
        
              Lifecycle phase of the file system.
        
            - **Name** *(string) --* 
        
              You can add tags to a file system, including a ``Name`` tag. For more information, see  CreateTags . If the file system has a ``Name`` tag, Amazon EFS returns the value in this field. 
        
            - **NumberOfMountTargets** *(integer) --* 
        
              Current number of mount targets that the file system has. For more information, see  CreateMountTarget .
        
            - **SizeInBytes** *(dict) --* 
        
              Latest known metered size (in bytes) of data stored in the file system, in its ``Value`` field, and the time at which that size was determined in its ``Timestamp`` field. The ``Timestamp`` value is the integer number of seconds since 1970-01-01T00:00:00Z. The ``SizeInBytes`` value doesn\'t represent the size of a consistent snapshot of the file system, but it is eventually consistent when there are no writes to the file system. That is, ``SizeInBytes`` represents actual size only if the file system is not modified for a period longer than a couple of hours. Otherwise, the value is not the exact size that the file system was at any point in time. 
        
              - **Value** *(integer) --* 
        
                Latest known metered size (in bytes) of data stored in the file system.
        
              - **Timestamp** *(datetime) --* 
        
                Time at which the size of data, returned in the ``Value`` field, was determined. The value is the integer number of seconds since 1970-01-01T00:00:00Z.
        
            - **PerformanceMode** *(string) --* 
        
              The ``PerformanceMode`` of the file system.
        
            - **Encrypted** *(boolean) --* 
        
              A Boolean value that, if true, indicates that the file system is encrypted.
        
            - **KmsKeyId** *(string) --* 
        
              The ID of an AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to protect the encrypted file system.
        
            - **ThroughputMode** *(string) --* 
        
              The throughput mode for a file system. There are two throughput modes to choose from for your file system: bursting and provisioned. You can decrease your file system\'s throughput in Provisioned Throughput mode or change between the throughput modes as long as it’s been more than 24 hours since the last decrease or throughput mode change.
        
            - **ProvisionedThroughputInMibps** *(float) --* 
        
              The throughput, measured in MiB/s, that you want to provision for a file system. The limit on throughput is 1024 MiB/s. You can get these limits increased by contacting AWS Support. For more information, see `Amazon EFS Limits That You Can Increase <http://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits>`__ in the *Amazon EFS User Guide.*  
        
        """
        pass

    def create_mount_target(self, FileSystemId: str, SubnetId: str, IpAddress: str = None, SecurityGroups: List = None) -> Dict:
        """
        
        You can create one mount target in each Availability Zone in your VPC. All EC2 instances in a VPC within a given Availability Zone share a single mount target for a given file system. If you have multiple subnets in an Availability Zone, you create a mount target in one of the subnets. EC2 instances do not need to be in the same subnet as the mount target in order to access their file system. For more information, see `Amazon EFS\: How it Works <http://docs.aws.amazon.com/efs/latest/ug/how-it-works.html>`__ . 
        
        In the request, you also specify a file system ID for which you are creating the mount target and the file system\'s lifecycle state must be ``available`` . For more information, see  DescribeFileSystems .
        
        In the request, you also provide a subnet ID, which determines the following:
        
        * VPC in which Amazon EFS creates the mount target 
         
        * Availability Zone in which Amazon EFS creates the mount target 
         
        * IP address range from which Amazon EFS selects the IP address of the mount target (if you don\'t specify an IP address in the request) 
         
        After creating the mount target, Amazon EFS returns a response that includes, a ``MountTargetId`` and an ``IpAddress`` . You use this IP address when mounting the file system in an EC2 instance. You can also use the mount target\'s DNS name when mounting the file system. The EC2 instance on which you mount the file system via the mount target can resolve the mount target\'s DNS name to its IP address. For more information, see `How it Works\: Implementation Overview <http://docs.aws.amazon.com/efs/latest/ug/how-it-works.html#how-it-works-implementation>`__ . 
        
        Note that you can create mount targets for a file system in only one VPC, and there can be only one mount target per Availability Zone. That is, if the file system already has one or more mount targets created for it, the subnet specified in the request to add another mount target must meet the following requirements:
        
        * Must belong to the same VPC as the subnets of the existing mount targets 
         
        * Must not be in the same Availability Zone as any of the subnets of the existing mount targets 
         
        If the request satisfies the requirements, Amazon EFS does the following:
        
        * Creates a new mount target in the specified subnet. 
         
        * Also creates a new network interface in the subnet as follows: 
        
          * If the request provides an ``IpAddress`` , Amazon EFS assigns that IP address to the network interface. Otherwise, Amazon EFS assigns a free address in the subnet (in the same way that the Amazon EC2 ``CreateNetworkInterface`` call does when a request does not specify a primary private IP address). 
           
          * If the request provides ``SecurityGroups`` , this network interface is associated with those security groups. Otherwise, it belongs to the default security group for the subnet\'s VPC. 
           
          * Assigns the description ``Mount target *fsmt-id* for file system *fs-id* `` where `` *fsmt-id* `` is the mount target ID, and `` *fs-id* `` is the ``FileSystemId`` . 
           
          * Sets the ``requesterManaged`` property of the network interface to ``true`` , and the ``requesterId`` value to ``EFS`` . 
           
        Each Amazon EFS mount target has one corresponding requester-managed EC2 network interface. After the network interface is created, Amazon EFS sets the ``NetworkInterfaceId`` field in the mount target\'s description to the network interface ID, and the ``IpAddress`` field to its address. If network interface creation fails, the entire ``CreateMountTarget`` operation fails.
        
        .. note::
        
          The ``CreateMountTarget`` call returns only after creating the network interface, but while the mount target state is still ``creating`` , you can check the mount target creation status by calling the  DescribeMountTargets operation, which among other things returns the mount target state.
        
        We recommend you create a mount target in each of the Availability Zones. There are cost considerations for using a file system in an Availability Zone through a mount target created in another Availability Zone. For more information, see `Amazon EFS <http://aws.amazon.com/efs/>`__ . In addition, by always using a mount target local to the instance\'s Availability Zone, you eliminate a partial failure scenario. If the Availability Zone in which your mount target is created goes down, then you won\'t be able to access your file system through that mount target. 
        
        This operation requires permissions for the following action on the file system:
        
        * ``elasticfilesystem:CreateMountTarget``   
         
        This operation also requires permissions for the following Amazon EC2 actions:
        
        * ``ec2:DescribeSubnets``   
         
        * ``ec2:DescribeNetworkInterfaces``   
         
        * ``ec2:CreateNetworkInterface``   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/CreateMountTarget>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_mount_target(
              FileSystemId=\'string\',
              SubnetId=\'string\',
              IpAddress=\'string\',
              SecurityGroups=[
                  \'string\',
              ]
          )
        :type FileSystemId: string
        :param FileSystemId: **[REQUIRED]** 
        
          ID of the file system for which to create the mount target.
        
        :type SubnetId: string
        :param SubnetId: **[REQUIRED]** 
        
          ID of the subnet to add the mount target in.
        
        :type IpAddress: string
        :param IpAddress: 
        
          Valid IPv4 address within the address range of the specified subnet.
        
        :type SecurityGroups: list
        :param SecurityGroups: 
        
          Up to five VPC security group IDs, of the form ``sg-xxxxxxxx`` . These must be for the same VPC as subnet specified.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OwnerId\': \'string\',
                \'MountTargetId\': \'string\',
                \'FileSystemId\': \'string\',
                \'SubnetId\': \'string\',
                \'LifeCycleState\': \'creating\'|\'available\'|\'updating\'|\'deleting\'|\'deleted\',
                \'IpAddress\': \'string\',
                \'NetworkInterfaceId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Provides a description of a mount target.
        
            - **OwnerId** *(string) --* 
        
              AWS account ID that owns the resource.
        
            - **MountTargetId** *(string) --* 
        
              System-assigned mount target ID.
        
            - **FileSystemId** *(string) --* 
        
              ID of the file system for which the mount target is intended.
        
            - **SubnetId** *(string) --* 
        
              ID of the mount target\'s subnet.
        
            - **LifeCycleState** *(string) --* 
        
              Lifecycle state of the mount target.
        
            - **IpAddress** *(string) --* 
        
              Address at which the file system may be mounted via the mount target.
        
            - **NetworkInterfaceId** *(string) --* 
        
              ID of the network interface that Amazon EFS created when it created the mount target.
        
        """
        pass

    def create_tags(self, FileSystemId: str, Tags: List) -> NoReturn:
        """
        
        This operation requires permission for the ``elasticfilesystem:CreateTags`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/CreateTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_tags(
              FileSystemId=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type FileSystemId: string
        :param FileSystemId: **[REQUIRED]** 
        
          ID of the file system whose tags you want to modify (String). This operation modifies the tags only, not the file system.
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          Array of ``Tag`` objects to add. Each ``Tag`` object is a key-value pair. 
        
          - *(dict) --* 
        
            A tag is a key-value pair. Allowed characters: letters, whitespace, and numbers, representable in UTF-8, and the following characters:``+ - = . _ : /``  
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              Tag key (String). The key can\'t start with ``aws:`` .
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              Value of the tag key.
        
        :returns: None
        """
        pass

    def delete_file_system(self, FileSystemId: str) -> NoReturn:
        """
        
        You can\'t delete a file system that is in use. That is, if the file system has any mount targets, you must first delete them. For more information, see  DescribeMountTargets and  DeleteMountTarget . 
        
        .. note::
        
          The ``DeleteFileSystem`` call returns while the file system state is still ``deleting`` . You can check the file system deletion status by calling the  DescribeFileSystems operation, which returns a list of file systems in your account. If you pass file system ID or creation token for the deleted file system, the  DescribeFileSystems returns a ``404 FileSystemNotFound`` error.
        
        This operation requires permissions for the ``elasticfilesystem:DeleteFileSystem`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DeleteFileSystem>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_file_system(
              FileSystemId=\'string\'
          )
        :type FileSystemId: string
        :param FileSystemId: **[REQUIRED]** 
        
          ID of the file system you want to delete.
        
        :returns: None
        """
        pass

    def delete_mount_target(self, MountTargetId: str) -> NoReturn:
        """
        
        This operation forcibly breaks any mounts of the file system via the mount target that is being deleted, which might disrupt instances or applications using those mounts. To avoid applications getting cut off abruptly, you might consider unmounting any mounts of the mount target, if feasible. The operation also deletes the associated network interface. Uncommitted writes may be lost, but breaking a mount target using this operation does not corrupt the file system itself. The file system you created remains. You can mount an EC2 instance in your VPC via another mount target.
        
        This operation requires permissions for the following action on the file system:
        
        * ``elasticfilesystem:DeleteMountTarget``   
         
        .. note::
        
          The ``DeleteMountTarget`` call returns while the mount target state is still ``deleting`` . You can check the mount target deletion by calling the  DescribeMountTargets operation, which returns a list of mount target descriptions for the given file system. 
        
        The operation also requires permissions for the following Amazon EC2 action on the mount target\'s network interface:
        
        * ``ec2:DeleteNetworkInterface``   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DeleteMountTarget>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_mount_target(
              MountTargetId=\'string\'
          )
        :type MountTargetId: string
        :param MountTargetId: **[REQUIRED]** 
        
          ID of the mount target to delete (String).
        
        :returns: None
        """
        pass

    def delete_tags(self, FileSystemId: str, TagKeys: List) -> NoReturn:
        """
        
        This operation requires permissions for the ``elasticfilesystem:DeleteTags`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DeleteTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_tags(
              FileSystemId=\'string\',
              TagKeys=[
                  \'string\',
              ]
          )
        :type FileSystemId: string
        :param FileSystemId: **[REQUIRED]** 
        
          ID of the file system whose tags you want to delete (String).
        
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** 
        
          List of tag keys to delete.
        
          - *(string) --* 
        
        :returns: None
        """
        pass

    def describe_file_systems(self, MaxItems: int = None, Marker: str = None, CreationToken: str = None, FileSystemId: str = None) -> Dict:
        """
        
        When retrieving all file system descriptions, you can optionally specify the ``MaxItems`` parameter to limit the number of descriptions in a response. If more file system descriptions remain, Amazon EFS returns a ``NextMarker`` , an opaque token, in the response. In this case, you should send a subsequent request with the ``Marker`` request parameter set to the value of ``NextMarker`` . 
        
        To retrieve a list of your file system descriptions, this operation is used in an iterative process, where ``DescribeFileSystems`` is called first without the ``Marker`` and then the operation continues to call it with the ``Marker`` parameter set to the value of the ``NextMarker`` from the previous response until the response has no ``NextMarker`` . 
        
        The implementation may return fewer than ``MaxItems`` file system descriptions while still including a ``NextMarker`` value. 
        
        The order of file systems returned in the response of one ``DescribeFileSystems`` call and the order of file systems returned across the responses of a multi-call iteration is unspecified. 
        
        This operation requires permissions for the ``elasticfilesystem:DescribeFileSystems`` action. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DescribeFileSystems>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_file_systems(
              MaxItems=123,
              Marker=\'string\',
              CreationToken=\'string\',
              FileSystemId=\'string\'
          )
        :type MaxItems: integer
        :param MaxItems: 
        
          (Optional) Specifies the maximum number of file systems to return in the response (integer). This parameter value must be greater than 0. The number of items that Amazon EFS returns is the minimum of the ``MaxItems`` parameter specified in the request and the service\'s internal maximum number of items per page. 
        
        :type Marker: string
        :param Marker: 
        
          (Optional) Opaque pagination token returned from a previous ``DescribeFileSystems`` operation (String). If present, specifies to continue the list from where the returning call had left off. 
        
        :type CreationToken: string
        :param CreationToken: 
        
          (Optional) Restricts the list to the file system with this creation token (String). You specify a creation token when you create an Amazon EFS file system.
        
        :type FileSystemId: string
        :param FileSystemId: 
        
          (Optional) ID of the file system whose description you want to retrieve (String).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'FileSystems\': [
                    {
                        \'OwnerId\': \'string\',
                        \'CreationToken\': \'string\',
                        \'FileSystemId\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'LifeCycleState\': \'creating\'|\'available\'|\'updating\'|\'deleting\'|\'deleted\',
                        \'Name\': \'string\',
                        \'NumberOfMountTargets\': 123,
                        \'SizeInBytes\': {
                            \'Value\': 123,
                            \'Timestamp\': datetime(2015, 1, 1)
                        },
                        \'PerformanceMode\': \'generalPurpose\'|\'maxIO\',
                        \'Encrypted\': True|False,
                        \'KmsKeyId\': \'string\',
                        \'ThroughputMode\': \'bursting\'|\'provisioned\',
                        \'ProvisionedThroughputInMibps\': 123.0
                    },
                ],
                \'NextMarker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Marker** *(string) --* 
        
              Present if provided by caller in the request (String).
        
            - **FileSystems** *(list) --* 
        
              Array of file system descriptions.
        
              - *(dict) --* 
        
                Description of the file system.
        
                - **OwnerId** *(string) --* 
        
                  AWS account that created the file system. If the file system was created by an IAM user, the parent account to which the user belongs is the owner.
        
                - **CreationToken** *(string) --* 
        
                  Opaque string specified in the request.
        
                - **FileSystemId** *(string) --* 
        
                  ID of the file system, assigned by Amazon EFS.
        
                - **CreationTime** *(datetime) --* 
        
                  Time that the file system was created, in seconds (since 1970-01-01T00:00:00Z).
        
                - **LifeCycleState** *(string) --* 
        
                  Lifecycle phase of the file system.
        
                - **Name** *(string) --* 
        
                  You can add tags to a file system, including a ``Name`` tag. For more information, see  CreateTags . If the file system has a ``Name`` tag, Amazon EFS returns the value in this field. 
        
                - **NumberOfMountTargets** *(integer) --* 
        
                  Current number of mount targets that the file system has. For more information, see  CreateMountTarget .
        
                - **SizeInBytes** *(dict) --* 
        
                  Latest known metered size (in bytes) of data stored in the file system, in its ``Value`` field, and the time at which that size was determined in its ``Timestamp`` field. The ``Timestamp`` value is the integer number of seconds since 1970-01-01T00:00:00Z. The ``SizeInBytes`` value doesn\'t represent the size of a consistent snapshot of the file system, but it is eventually consistent when there are no writes to the file system. That is, ``SizeInBytes`` represents actual size only if the file system is not modified for a period longer than a couple of hours. Otherwise, the value is not the exact size that the file system was at any point in time. 
        
                  - **Value** *(integer) --* 
        
                    Latest known metered size (in bytes) of data stored in the file system.
        
                  - **Timestamp** *(datetime) --* 
        
                    Time at which the size of data, returned in the ``Value`` field, was determined. The value is the integer number of seconds since 1970-01-01T00:00:00Z.
        
                - **PerformanceMode** *(string) --* 
        
                  The ``PerformanceMode`` of the file system.
        
                - **Encrypted** *(boolean) --* 
        
                  A Boolean value that, if true, indicates that the file system is encrypted.
        
                - **KmsKeyId** *(string) --* 
        
                  The ID of an AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to protect the encrypted file system.
        
                - **ThroughputMode** *(string) --* 
        
                  The throughput mode for a file system. There are two throughput modes to choose from for your file system: bursting and provisioned. You can decrease your file system\'s throughput in Provisioned Throughput mode or change between the throughput modes as long as it’s been more than 24 hours since the last decrease or throughput mode change.
        
                - **ProvisionedThroughputInMibps** *(float) --* 
        
                  The throughput, measured in MiB/s, that you want to provision for a file system. The limit on throughput is 1024 MiB/s. You can get these limits increased by contacting AWS Support. For more information, see `Amazon EFS Limits That You Can Increase <http://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits>`__ in the *Amazon EFS User Guide.*  
        
            - **NextMarker** *(string) --* 
        
              Present if there are more file systems than returned in the response (String). You can use the ``NextMarker`` in the subsequent request to fetch the descriptions.
        
        """
        pass

    def describe_mount_target_security_groups(self, MountTargetId: str) -> Dict:
        """
        
        This operation requires permissions for the following actions:
        
        * ``elasticfilesystem:DescribeMountTargetSecurityGroups`` action on the mount target\'s file system.  
         
        * ``ec2:DescribeNetworkInterfaceAttribute`` action on the mount target\'s network interface.  
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_mount_target_security_groups(
              MountTargetId=\'string\'
          )
        :type MountTargetId: string
        :param MountTargetId: **[REQUIRED]** 
        
          ID of the mount target whose security groups you want to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SecurityGroups\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SecurityGroups** *(list) --* 
        
              Array of security groups.
        
              - *(string) --* 
          
        """
        pass

    def describe_mount_targets(self, MaxItems: int = None, Marker: str = None, FileSystemId: str = None, MountTargetId: str = None) -> Dict:
        """
        
        This operation requires permissions for the ``elasticfilesystem:DescribeMountTargets`` action, on either the file system ID that you specify in ``FileSystemId`` , or on the file system of the mount target that you specify in ``MountTargetId`` .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DescribeMountTargets>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_mount_targets(
              MaxItems=123,
              Marker=\'string\',
              FileSystemId=\'string\',
              MountTargetId=\'string\'
          )
        :type MaxItems: integer
        :param MaxItems: 
        
          (Optional) Maximum number of mount targets to return in the response. It must be an integer with a value greater than zero.
        
        :type Marker: string
        :param Marker: 
        
          (Optional) Opaque pagination token returned from a previous ``DescribeMountTargets`` operation (String). If present, it specifies to continue the list from where the previous returning call left off.
        
        :type FileSystemId: string
        :param FileSystemId: 
        
          (Optional) ID of the file system whose mount targets you want to list (String). It must be included in your request if ``MountTargetId`` is not included.
        
        :type MountTargetId: string
        :param MountTargetId: 
        
          (Optional) ID of the mount target that you want to have described (String). It must be included in your request if ``FileSystemId`` is not included.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'MountTargets\': [
                    {
                        \'OwnerId\': \'string\',
                        \'MountTargetId\': \'string\',
                        \'FileSystemId\': \'string\',
                        \'SubnetId\': \'string\',
                        \'LifeCycleState\': \'creating\'|\'available\'|\'updating\'|\'deleting\'|\'deleted\',
                        \'IpAddress\': \'string\',
                        \'NetworkInterfaceId\': \'string\'
                    },
                ],
                \'NextMarker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              If the request included the ``Marker`` , the response returns that value in this field.
        
            - **MountTargets** *(list) --* 
        
              Returns the file system\'s mount targets as an array of ``MountTargetDescription`` objects.
        
              - *(dict) --* 
        
                Provides a description of a mount target.
        
                - **OwnerId** *(string) --* 
        
                  AWS account ID that owns the resource.
        
                - **MountTargetId** *(string) --* 
        
                  System-assigned mount target ID.
        
                - **FileSystemId** *(string) --* 
        
                  ID of the file system for which the mount target is intended.
        
                - **SubnetId** *(string) --* 
        
                  ID of the mount target\'s subnet.
        
                - **LifeCycleState** *(string) --* 
        
                  Lifecycle state of the mount target.
        
                - **IpAddress** *(string) --* 
        
                  Address at which the file system may be mounted via the mount target.
        
                - **NetworkInterfaceId** *(string) --* 
        
                  ID of the network interface that Amazon EFS created when it created the mount target.
        
            - **NextMarker** *(string) --* 
        
              If a value is present, there are more mount targets to return. In a subsequent request, you can provide ``Marker`` in your request with this value to retrieve the next set of mount targets.
        
        """
        pass

    def describe_tags(self, FileSystemId: str, MaxItems: int = None, Marker: str = None) -> Dict:
        """
        
        This operation requires permissions for the ``elasticfilesystem:DescribeTags`` action. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DescribeTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_tags(
              MaxItems=123,
              Marker=\'string\',
              FileSystemId=\'string\'
          )
        :type MaxItems: integer
        :param MaxItems: 
        
          (Optional) Maximum number of file system tags to return in the response. It must be an integer with a value greater than zero.
        
        :type Marker: string
        :param Marker: 
        
          (Optional) Opaque pagination token returned from a previous ``DescribeTags`` operation (String). If present, it specifies to continue the list from where the previous call left off.
        
        :type FileSystemId: string
        :param FileSystemId: **[REQUIRED]** 
        
          ID of the file system whose tag set you want to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'Tags\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ],
                \'NextMarker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              If the request included a ``Marker`` , the response returns that value in this field.
        
            - **Tags** *(list) --* 
        
              Returns tags associated with the file system as an array of ``Tag`` objects. 
        
              - *(dict) --* 
        
                A tag is a key-value pair. Allowed characters: letters, whitespace, and numbers, representable in UTF-8, and the following characters:``+ - = . _ : /``  
        
                - **Key** *(string) --* 
        
                  Tag key (String). The key can\'t start with ``aws:`` .
        
                - **Value** *(string) --* 
        
                  Value of the tag key.
        
            - **NextMarker** *(string) --* 
        
              If a value is present, there are more tags to return. In a subsequent request, you can provide the value of ``NextMarker`` as the value of the ``Marker`` parameter in your next request to retrieve the next set of tags.
        
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

    def modify_mount_target_security_groups(self, MountTargetId: str, SecurityGroups: List = None) -> NoReturn:
        """
        
        When you create a mount target, Amazon EFS also creates a new network interface. For more information, see  CreateMountTarget . This operation replaces the security groups in effect for the network interface associated with a mount target, with the ``SecurityGroups`` provided in the request. This operation requires that the network interface of the mount target has been created and the lifecycle state of the mount target is not ``deleted`` . 
        
        The operation requires permissions for the following actions:
        
        * ``elasticfilesystem:ModifyMountTargetSecurityGroups`` action on the mount target\'s file system.  
         
        * ``ec2:ModifyNetworkInterfaceAttribute`` action on the mount target\'s network interface.  
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/ModifyMountTargetSecurityGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_mount_target_security_groups(
              MountTargetId=\'string\',
              SecurityGroups=[
                  \'string\',
              ]
          )
        :type MountTargetId: string
        :param MountTargetId: **[REQUIRED]** 
        
          ID of the mount target whose security groups you want to modify.
        
        :type SecurityGroups: list
        :param SecurityGroups: 
        
          Array of up to five VPC security group IDs.
        
          - *(string) --* 
        
        :returns: None
        """
        pass

    def update_file_system(self, FileSystemId: str, ThroughputMode: str = None, ProvisionedThroughputInMibps: float = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/UpdateFileSystem>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_file_system(
              FileSystemId=\'string\',
              ThroughputMode=\'bursting\'|\'provisioned\',
              ProvisionedThroughputInMibps=123.0
          )
        :type FileSystemId: string
        :param FileSystemId: **[REQUIRED]** 
        
          The ID of the file system that you want to update.
        
        :type ThroughputMode: string
        :param ThroughputMode: 
        
          (Optional) The throughput mode that you want your file system to use. If you\'re not updating your throughput mode, you don\'t need to provide this value in your request.
        
        :type ProvisionedThroughputInMibps: float
        :param ProvisionedThroughputInMibps: 
        
          (Optional) The amount of throughput, in MiB/s, that you want to provision for your file system. If you\'re not updating the amount of provisioned throughput for your file system, you don\'t need to provide this value in your request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OwnerId\': \'string\',
                \'CreationToken\': \'string\',
                \'FileSystemId\': \'string\',
                \'CreationTime\': datetime(2015, 1, 1),
                \'LifeCycleState\': \'creating\'|\'available\'|\'updating\'|\'deleting\'|\'deleted\',
                \'Name\': \'string\',
                \'NumberOfMountTargets\': 123,
                \'SizeInBytes\': {
                    \'Value\': 123,
                    \'Timestamp\': datetime(2015, 1, 1)
                },
                \'PerformanceMode\': \'generalPurpose\'|\'maxIO\',
                \'Encrypted\': True|False,
                \'KmsKeyId\': \'string\',
                \'ThroughputMode\': \'bursting\'|\'provisioned\',
                \'ProvisionedThroughputInMibps\': 123.0
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Description of the file system.
        
            - **OwnerId** *(string) --* 
        
              AWS account that created the file system. If the file system was created by an IAM user, the parent account to which the user belongs is the owner.
        
            - **CreationToken** *(string) --* 
        
              Opaque string specified in the request.
        
            - **FileSystemId** *(string) --* 
        
              ID of the file system, assigned by Amazon EFS.
        
            - **CreationTime** *(datetime) --* 
        
              Time that the file system was created, in seconds (since 1970-01-01T00:00:00Z).
        
            - **LifeCycleState** *(string) --* 
        
              Lifecycle phase of the file system.
        
            - **Name** *(string) --* 
        
              You can add tags to a file system, including a ``Name`` tag. For more information, see  CreateTags . If the file system has a ``Name`` tag, Amazon EFS returns the value in this field. 
        
            - **NumberOfMountTargets** *(integer) --* 
        
              Current number of mount targets that the file system has. For more information, see  CreateMountTarget .
        
            - **SizeInBytes** *(dict) --* 
        
              Latest known metered size (in bytes) of data stored in the file system, in its ``Value`` field, and the time at which that size was determined in its ``Timestamp`` field. The ``Timestamp`` value is the integer number of seconds since 1970-01-01T00:00:00Z. The ``SizeInBytes`` value doesn\'t represent the size of a consistent snapshot of the file system, but it is eventually consistent when there are no writes to the file system. That is, ``SizeInBytes`` represents actual size only if the file system is not modified for a period longer than a couple of hours. Otherwise, the value is not the exact size that the file system was at any point in time. 
        
              - **Value** *(integer) --* 
        
                Latest known metered size (in bytes) of data stored in the file system.
        
              - **Timestamp** *(datetime) --* 
        
                Time at which the size of data, returned in the ``Value`` field, was determined. The value is the integer number of seconds since 1970-01-01T00:00:00Z.
        
            - **PerformanceMode** *(string) --* 
        
              The ``PerformanceMode`` of the file system.
        
            - **Encrypted** *(boolean) --* 
        
              A Boolean value that, if true, indicates that the file system is encrypted.
        
            - **KmsKeyId** *(string) --* 
        
              The ID of an AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to protect the encrypted file system.
        
            - **ThroughputMode** *(string) --* 
        
              The throughput mode for a file system. There are two throughput modes to choose from for your file system: bursting and provisioned. You can decrease your file system\'s throughput in Provisioned Throughput mode or change between the throughput modes as long as it’s been more than 24 hours since the last decrease or throughput mode change.
        
            - **ProvisionedThroughputInMibps** *(float) --* 
        
              The throughput, measured in MiB/s, that you want to provision for a file system. The limit on throughput is 1024 MiB/s. You can get these limits increased by contacting AWS Support. For more information, see `Amazon EFS Limits That You Can Increase <http://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits>`__ in the *Amazon EFS User Guide.*  
        
        """
        pass
