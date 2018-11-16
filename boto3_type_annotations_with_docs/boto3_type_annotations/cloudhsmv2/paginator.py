from typing import Dict
from botocore.paginate import Paginator


class DescribeBackups(Paginator):
    def paginate(self, Filters: Dict = None, SortAscending: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsmv2-2017-04-28/DescribeBackups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters={
                  \'string\': [
                      \'string\',
                  ]
              },
              SortAscending=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: dict
        :param Filters: 
        
          One or more filters to limit the items returned in the response.
        
          Use the ``backupIds`` filter to return only the specified backups. Specify backups by their backup identifier (ID).
        
          Use the ``sourceBackupIds`` filter to return only the backups created from a source backup. The ``sourceBackupID`` of a source backup is returned by the  CopyBackupToRegion operation.
        
          Use the ``clusterIds`` filter to return only the backups for the specified clusters. Specify clusters by their cluster identifier (ID).
        
          Use the ``states`` filter to return only backups that match the specified state.
        
          - *(string) --* 
        
            - *(list) --* 
        
              - *(string) --* 
        
        :type SortAscending: boolean
        :param SortAscending: 
        
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
                \'Backups\': [
                    {
                        \'BackupId\': \'string\',
                        \'BackupState\': \'CREATE_IN_PROGRESS\'|\'READY\'|\'DELETED\'|\'PENDING_DELETION\',
                        \'ClusterId\': \'string\',
                        \'CreateTimestamp\': datetime(2015, 1, 1),
                        \'CopyTimestamp\': datetime(2015, 1, 1),
                        \'SourceRegion\': \'string\',
                        \'SourceBackup\': \'string\',
                        \'SourceCluster\': \'string\',
                        \'DeleteTimestamp\': datetime(2015, 1, 1)
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Backups** *(list) --* 
        
              A list of backups.
        
              - *(dict) --* 
        
                Contains information about a backup of an AWS CloudHSM cluster.
        
                - **BackupId** *(string) --* 
        
                  The identifier (ID) of the backup.
        
                - **BackupState** *(string) --* 
        
                  The state of the backup.
        
                - **ClusterId** *(string) --* 
        
                  The identifier (ID) of the cluster that was backed up.
        
                - **CreateTimestamp** *(datetime) --* 
        
                  The date and time when the backup was created.
        
                - **CopyTimestamp** *(datetime) --* 
                
                - **SourceRegion** *(string) --* 
                
                - **SourceBackup** *(string) --* 
                
                - **SourceCluster** *(string) --* 
                
                - **DeleteTimestamp** *(datetime) --* 
        
                  The date and time when the backup will be permanently deleted.
        
        """
        pass


class DescribeClusters(Paginator):
    def paginate(self, Filters: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsmv2-2017-04-28/DescribeClusters>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters={
                  \'string\': [
                      \'string\',
                  ]
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: dict
        :param Filters: 
        
          One or more filters to limit the items returned in the response.
        
          Use the ``clusterIds`` filter to return only the specified clusters. Specify clusters by their cluster identifier (ID).
        
          Use the ``vpcIds`` filter to return only the clusters in the specified virtual private clouds (VPCs). Specify VPCs by their VPC identifier (ID).
        
          Use the ``states`` filter to return only clusters that match the specified state.
        
          - *(string) --* 
        
            - *(list) --* 
        
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
                \'Clusters\': [
                    {
                        \'BackupPolicy\': \'DEFAULT\',
                        \'ClusterId\': \'string\',
                        \'CreateTimestamp\': datetime(2015, 1, 1),
                        \'Hsms\': [
                            {
                                \'AvailabilityZone\': \'string\',
                                \'ClusterId\': \'string\',
                                \'SubnetId\': \'string\',
                                \'EniId\': \'string\',
                                \'EniIp\': \'string\',
                                \'HsmId\': \'string\',
                                \'State\': \'CREATE_IN_PROGRESS\'|\'ACTIVE\'|\'DEGRADED\'|\'DELETE_IN_PROGRESS\'|\'DELETED\',
                                \'StateMessage\': \'string\'
                            },
                        ],
                        \'HsmType\': \'string\',
                        \'PreCoPassword\': \'string\',
                        \'SecurityGroup\': \'string\',
                        \'SourceBackupId\': \'string\',
                        \'State\': \'CREATE_IN_PROGRESS\'|\'UNINITIALIZED\'|\'INITIALIZE_IN_PROGRESS\'|\'INITIALIZED\'|\'ACTIVE\'|\'UPDATE_IN_PROGRESS\'|\'DELETE_IN_PROGRESS\'|\'DELETED\'|\'DEGRADED\',
                        \'StateMessage\': \'string\',
                        \'SubnetMapping\': {
                            \'string\': \'string\'
                        },
                        \'VpcId\': \'string\',
                        \'Certificates\': {
                            \'ClusterCsr\': \'string\',
                            \'HsmCertificate\': \'string\',
                            \'AwsHardwareCertificate\': \'string\',
                            \'ManufacturerHardwareCertificate\': \'string\',
                            \'ClusterCertificate\': \'string\'
                        }
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Clusters** *(list) --* 
        
              A list of clusters.
        
              - *(dict) --* 
        
                Contains information about an AWS CloudHSM cluster.
        
                - **BackupPolicy** *(string) --* 
        
                  The cluster\'s backup policy.
        
                - **ClusterId** *(string) --* 
        
                  The cluster\'s identifier (ID).
        
                - **CreateTimestamp** *(datetime) --* 
        
                  The date and time when the cluster was created.
        
                - **Hsms** *(list) --* 
        
                  Contains information about the HSMs in the cluster.
        
                  - *(dict) --* 
        
                    Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.
        
                    - **AvailabilityZone** *(string) --* 
        
                      The Availability Zone that contains the HSM.
        
                    - **ClusterId** *(string) --* 
        
                      The identifier (ID) of the cluster that contains the HSM.
        
                    - **SubnetId** *(string) --* 
        
                      The subnet that contains the HSM\'s elastic network interface (ENI).
        
                    - **EniId** *(string) --* 
        
                      The identifier (ID) of the HSM\'s elastic network interface (ENI).
        
                    - **EniIp** *(string) --* 
        
                      The IP address of the HSM\'s elastic network interface (ENI).
        
                    - **HsmId** *(string) --* 
        
                      The HSM\'s identifier (ID).
        
                    - **State** *(string) --* 
        
                      The HSM\'s state.
        
                    - **StateMessage** *(string) --* 
        
                      A description of the HSM\'s state.
        
                - **HsmType** *(string) --* 
        
                  The type of HSM that the cluster contains.
        
                - **PreCoPassword** *(string) --* 
        
                  The default password for the cluster\'s Pre-Crypto Officer (PRECO) user.
        
                - **SecurityGroup** *(string) --* 
        
                  The identifier (ID) of the cluster\'s security group.
        
                - **SourceBackupId** *(string) --* 
        
                  The identifier (ID) of the backup used to create the cluster. This value exists only when the cluster was created from a backup.
        
                - **State** *(string) --* 
        
                  The cluster\'s state.
        
                - **StateMessage** *(string) --* 
        
                  A description of the cluster\'s state.
        
                - **SubnetMapping** *(dict) --* 
        
                  A map of the cluster\'s subnets and their corresponding Availability Zones.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
                - **VpcId** *(string) --* 
        
                  The identifier (ID) of the virtual private cloud (VPC) that contains the cluster.
        
                - **Certificates** *(dict) --* 
        
                  Contains one or more certificates or a certificate signing request (CSR).
        
                  - **ClusterCsr** *(string) --* 
        
                    The cluster\'s certificate signing request (CSR). The CSR exists only when the cluster\'s state is ``UNINITIALIZED`` .
        
                  - **HsmCertificate** *(string) --* 
        
                    The HSM certificate issued (signed) by the HSM hardware.
        
                  - **AwsHardwareCertificate** *(string) --* 
        
                    The HSM hardware certificate issued (signed) by AWS CloudHSM.
        
                  - **ManufacturerHardwareCertificate** *(string) --* 
        
                    The HSM hardware certificate issued (signed) by the hardware manufacturer.
        
                  - **ClusterCertificate** *(string) --* 
        
                    The cluster certificate issued (signed) by the issuing certificate authority (CA) of the cluster\'s owner.
        
        """
        pass


class ListTags(Paginator):
    def paginate(self, ResourceId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsmv2-2017-04-28/ListTags>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ResourceId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          The cluster identifier (ID) for the cluster whose tags you are getting. To find the cluster ID, use  DescribeClusters .
        
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
                \'TagList\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TagList** *(list) --* 
        
              A list of tags.
        
              - *(dict) --* 
        
                Contains a tag. A tag is a key-value pair.
        
                - **Key** *(string) --* 
        
                  The key of the tag.
        
                - **Value** *(string) --* 
        
                  The value of the tag.
        
        """
        pass
