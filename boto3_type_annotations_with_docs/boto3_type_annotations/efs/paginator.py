from typing import Dict
from botocore.paginate import Paginator


class DescribeFileSystems(Paginator):
    def paginate(self, CreationToken: str = None, FileSystemId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DescribeFileSystems>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CreationToken=\'string\',
              FileSystemId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CreationToken: string
        :param CreationToken: 
        
          (Optional) Restricts the list to the file system with this creation token (String). You specify a creation token when you create an Amazon EFS file system.
        
        :type FileSystemId: string
        :param FileSystemId: 
        
          (Optional) ID of the file system whose description you want to retrieve (String).
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeMountTargets(Paginator):
    def paginate(self, FileSystemId: str = None, MountTargetId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DescribeMountTargets>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              FileSystemId=\'string\',
              MountTargetId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type FileSystemId: string
        :param FileSystemId: 
        
          (Optional) ID of the file system whose mount targets you want to list (String). It must be included in your request if ``MountTargetId`` is not included.
        
        :type MountTargetId: string
        :param MountTargetId: 
        
          (Optional) ID of the mount target that you want to have described (String). It must be included in your request if ``FileSystemId`` is not included.
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeTags(Paginator):
    def paginate(self, FileSystemId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DescribeTags>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              FileSystemId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type FileSystemId: string
        :param FileSystemId: **[REQUIRED]** 
        
          ID of the file system whose tag set you want to retrieve.
        
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
                \'Marker\': \'string\',
                \'Tags\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
