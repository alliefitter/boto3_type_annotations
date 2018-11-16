from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
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

    def copy_backup_to_region(self, DestinationRegion: str, BackupId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsmv2-2017-04-28/CopyBackupToRegion>`_
        
        **Request Syntax** 
        ::
        
          response = client.copy_backup_to_region(
              DestinationRegion=\'string\',
              BackupId=\'string\'
          )
        :type DestinationRegion: string
        :param DestinationRegion: **[REQUIRED]** 
        
          The AWS region that will contain your copied CloudHSM cluster backup.
        
        :type BackupId: string
        :param BackupId: **[REQUIRED]** 
        
          The ID of the backup that will be copied to the destination region. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DestinationBackup\': {
                    \'CreateTimestamp\': datetime(2015, 1, 1),
                    \'SourceRegion\': \'string\',
                    \'SourceBackup\': \'string\',
                    \'SourceCluster\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DestinationBackup** *(dict) --* 
        
              Information on the backup that will be copied to the destination region, including CreateTimestamp, SourceBackup, SourceCluster, and Source Region. CreateTimestamp of the destination backup will be the same as that of the source backup.
        
              You will need to use the ``sourceBackupID`` returned in this operation to use the  DescribeBackups operation on the backup that will be copied to the destination region.
        
              - **CreateTimestamp** *(datetime) --* 
              
              - **SourceRegion** *(string) --* 
              
              - **SourceBackup** *(string) --* 
              
              - **SourceCluster** *(string) --* 
          
        """
        pass

    def create_cluster(self, SubnetIds: List, HsmType: str, SourceBackupId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsmv2-2017-04-28/CreateCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_cluster(
              SubnetIds=[
                  \'string\',
              ],
              HsmType=\'string\',
              SourceBackupId=\'string\'
          )
        :type SubnetIds: list
        :param SubnetIds: **[REQUIRED]** 
        
          The identifiers (IDs) of the subnets where you are creating the cluster. You must specify at least one subnet. If you specify multiple subnets, they must meet the following criteria:
        
          * All subnets must be in the same virtual private cloud (VPC). 
           
          * You can specify only one subnet per Availability Zone. 
           
          - *(string) --* 
        
        :type HsmType: string
        :param HsmType: **[REQUIRED]** 
        
          The type of HSM to use in the cluster. Currently the only allowed value is ``hsm1.medium`` .
        
        :type SourceBackupId: string
        :param SourceBackupId: 
        
          The identifier (ID) of the cluster backup to restore. Use this value to restore the cluster from a backup instead of creating a new cluster. To find the backup ID, use  DescribeBackups .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              Information about the cluster that was created.
        
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

    def create_hsm(self, ClusterId: str, AvailabilityZone: str, IpAddress: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsmv2-2017-04-28/CreateHsm>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_hsm(
              ClusterId=\'string\',
              AvailabilityZone=\'string\',
              IpAddress=\'string\'
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]** 
        
          The identifier (ID) of the HSM\'s cluster. To find the cluster ID, use  DescribeClusters .
        
        :type AvailabilityZone: string
        :param AvailabilityZone: **[REQUIRED]** 
        
          The Availability Zone where you are creating the HSM. To find the cluster\'s Availability Zones, use  DescribeClusters .
        
        :type IpAddress: string
        :param IpAddress: 
        
          The HSM\'s IP address. If you specify an IP address, use an available address from the subnet that maps to the Availability Zone where you are creating the HSM. If you don\'t specify an IP address, one is chosen for you from that subnet.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Hsm\': {
                    \'AvailabilityZone\': \'string\',
                    \'ClusterId\': \'string\',
                    \'SubnetId\': \'string\',
                    \'EniId\': \'string\',
                    \'EniIp\': \'string\',
                    \'HsmId\': \'string\',
                    \'State\': \'CREATE_IN_PROGRESS\'|\'ACTIVE\'|\'DEGRADED\'|\'DELETE_IN_PROGRESS\'|\'DELETED\',
                    \'StateMessage\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Hsm** *(dict) --* 
        
              Information about the HSM that was created.
        
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
        
        """
        pass

    def delete_backup(self, BackupId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsmv2-2017-04-28/DeleteBackup>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_backup(
              BackupId=\'string\'
          )
        :type BackupId: string
        :param BackupId: **[REQUIRED]** 
        
          The ID of the backup to be deleted. To find the ID of a backup, use the  DescribeBackups operation.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Backup\': {
                    \'BackupId\': \'string\',
                    \'BackupState\': \'CREATE_IN_PROGRESS\'|\'READY\'|\'DELETED\'|\'PENDING_DELETION\',
                    \'ClusterId\': \'string\',
                    \'CreateTimestamp\': datetime(2015, 1, 1),
                    \'CopyTimestamp\': datetime(2015, 1, 1),
                    \'SourceRegion\': \'string\',
                    \'SourceBackup\': \'string\',
                    \'SourceCluster\': \'string\',
                    \'DeleteTimestamp\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Backup** *(dict) --* 
        
              Information on the ``Backup`` object deleted.
        
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

    def delete_cluster(self, ClusterId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsmv2-2017-04-28/DeleteCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_cluster(
              ClusterId=\'string\'
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]** 
        
          The identifier (ID) of the cluster that you are deleting. To find the cluster ID, use  DescribeClusters .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              Information about the cluster that was deleted.
        
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

    def delete_hsm(self, ClusterId: str, HsmId: str = None, EniId: str = None, EniIp: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsmv2-2017-04-28/DeleteHsm>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_hsm(
              ClusterId=\'string\',
              HsmId=\'string\',
              EniId=\'string\',
              EniIp=\'string\'
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]** 
        
          The identifier (ID) of the cluster that contains the HSM that you are deleting.
        
        :type HsmId: string
        :param HsmId: 
        
          The identifier (ID) of the HSM that you are deleting.
        
        :type EniId: string
        :param EniId: 
        
          The identifier (ID) of the elastic network interface (ENI) of the HSM that you are deleting.
        
        :type EniIp: string
        :param EniIp: 
        
          The IP address of the elastic network interface (ENI) of the HSM that you are deleting.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'HsmId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **HsmId** *(string) --* 
        
              The identifier (ID) of the HSM that was deleted.
        
        """
        pass

    def describe_backups(self, NextToken: str = None, MaxResults: int = None, Filters: Dict = None, SortAscending: bool = None) -> Dict:
        """
        
        This is a paginated operation, which means that each response might contain only a subset of all the backups. When the response contains only a subset of backups, it includes a ``NextToken`` value. Use this value in a subsequent ``DescribeBackups`` request to get more backups. When you receive a response with no ``NextToken`` (or an empty or null value), that means there are no more backups to get.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsmv2-2017-04-28/DescribeBackups>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_backups(
              NextToken=\'string\',
              MaxResults=123,
              Filters={
                  \'string\': [
                      \'string\',
                  ]
              },
              SortAscending=True|False
          )
        :type NextToken: string
        :param NextToken: 
        
          The ``NextToken`` value that you received in the previous response. Use this value to get more backups.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of backups to return in the response. When there are more backups than the number you specify, the response contains a ``NextToken`` value.
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              An opaque string that indicates that the response contains only a subset of backups. Use this value in a subsequent ``DescribeBackups`` request to get more backups.
        
        """
        pass

    def describe_clusters(self, Filters: Dict = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        This is a paginated operation, which means that each response might contain only a subset of all the clusters. When the response contains only a subset of clusters, it includes a ``NextToken`` value. Use this value in a subsequent ``DescribeClusters`` request to get more clusters. When you receive a response with no ``NextToken`` (or an empty or null value), that means there are no more clusters to get.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsmv2-2017-04-28/DescribeClusters>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_clusters(
              Filters={
                  \'string\': [
                      \'string\',
                  ]
              },
              NextToken=\'string\',
              MaxResults=123
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
        
        :type NextToken: string
        :param NextToken: 
        
          The ``NextToken`` value that you received in the previous response. Use this value to get more clusters.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of clusters to return in the response. When there are more clusters than the number you specify, the response contains a ``NextToken`` value.
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              An opaque string that indicates that the response contains only a subset of clusters. Use this value in a subsequent ``DescribeClusters`` request to get more clusters.
        
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

    def initialize_cluster(self, ClusterId: str, SignedCert: str, TrustAnchor: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsmv2-2017-04-28/InitializeCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.initialize_cluster(
              ClusterId=\'string\',
              SignedCert=\'string\',
              TrustAnchor=\'string\'
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]** 
        
          The identifier (ID) of the cluster that you are claiming. To find the cluster ID, use  DescribeClusters .
        
        :type SignedCert: string
        :param SignedCert: **[REQUIRED]** 
        
          The cluster certificate issued (signed) by your issuing certificate authority (CA). The certificate must be in PEM format and can contain a maximum of 5000 characters.
        
        :type TrustAnchor: string
        :param TrustAnchor: **[REQUIRED]** 
        
          The issuing certificate of the issuing certificate authority (CA) that issued (signed) the cluster certificate. This can be a root (self-signed) certificate or a certificate chain that begins with the certificate that issued the cluster certificate and ends with a root certificate. The certificate or certificate chain must be in PEM format and can contain a maximum of 5000 characters.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'State\': \'CREATE_IN_PROGRESS\'|\'UNINITIALIZED\'|\'INITIALIZE_IN_PROGRESS\'|\'INITIALIZED\'|\'ACTIVE\'|\'UPDATE_IN_PROGRESS\'|\'DELETE_IN_PROGRESS\'|\'DELETED\'|\'DEGRADED\',
                \'StateMessage\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **State** *(string) --* 
        
              The cluster\'s state.
        
            - **StateMessage** *(string) --* 
        
              A description of the cluster\'s state.
        
        """
        pass

    def list_tags(self, ResourceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        This is a paginated operation, which means that each response might contain only a subset of all the tags. When the response contains only a subset of tags, it includes a ``NextToken`` value. Use this value in a subsequent ``ListTags`` request to get more tags. When you receive a response with no ``NextToken`` (or an empty or null value), that means there are no more tags to get.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsmv2-2017-04-28/ListTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags(
              ResourceId=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          The cluster identifier (ID) for the cluster whose tags you are getting. To find the cluster ID, use  DescribeClusters .
        
        :type NextToken: string
        :param NextToken: 
        
          The ``NextToken`` value that you received in the previous response. Use this value to get more tags.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of tags to return in the response. When there are more tags than the number you specify, the response contains a ``NextToken`` value.
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              An opaque string that indicates that the response contains only a subset of tags. Use this value in a subsequent ``ListTags`` request to get more tags.
        
        """
        pass

    def restore_backup(self, BackupId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsmv2-2017-04-28/RestoreBackup>`_
        
        **Request Syntax** 
        ::
        
          response = client.restore_backup(
              BackupId=\'string\'
          )
        :type BackupId: string
        :param BackupId: **[REQUIRED]** 
        
          The ID of the backup to be restored. To find the ID of a backup, use the  DescribeBackups operation.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Backup\': {
                    \'BackupId\': \'string\',
                    \'BackupState\': \'CREATE_IN_PROGRESS\'|\'READY\'|\'DELETED\'|\'PENDING_DELETION\',
                    \'ClusterId\': \'string\',
                    \'CreateTimestamp\': datetime(2015, 1, 1),
                    \'CopyTimestamp\': datetime(2015, 1, 1),
                    \'SourceRegion\': \'string\',
                    \'SourceBackup\': \'string\',
                    \'SourceCluster\': \'string\',
                    \'DeleteTimestamp\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Backup** *(dict) --* 
        
              Information on the ``Backup`` object created.
        
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

    def tag_resource(self, ResourceId: str, TagList: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsmv2-2017-04-28/TagResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.tag_resource(
              ResourceId=\'string\',
              TagList=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          The cluster identifier (ID) for the cluster that you are tagging. To find the cluster ID, use  DescribeClusters .
        
        :type TagList: list
        :param TagList: **[REQUIRED]** 
        
          A list of one or more tags.
        
          - *(dict) --* 
        
            Contains a tag. A tag is a key-value pair.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The key of the tag.
        
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

    def untag_resource(self, ResourceId: str, TagKeyList: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsmv2-2017-04-28/UntagResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.untag_resource(
              ResourceId=\'string\',
              TagKeyList=[
                  \'string\',
              ]
          )
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          The cluster identifier (ID) for the cluster whose tags you are removing. To find the cluster ID, use  DescribeClusters .
        
        :type TagKeyList: list
        :param TagKeyList: **[REQUIRED]** 
        
          A list of one or more tag keys for the tags that you are removing. Specify only the tag keys, not the tag values.
        
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
