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
    def accept_reserved_node_exchange(self, ReservedNodeId: str, TargetReservedNodeOfferingId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/AcceptReservedNodeExchange>`_
        
        **Request Syntax** 
        ::
        
          response = client.accept_reserved_node_exchange(
              ReservedNodeId=\'string\',
              TargetReservedNodeOfferingId=\'string\'
          )
        :type ReservedNodeId: string
        :param ReservedNodeId: **[REQUIRED]** 
        
          A string representing the node identifier of the DC1 Reserved Node to be exchanged.
        
        :type TargetReservedNodeOfferingId: string
        :param TargetReservedNodeOfferingId: **[REQUIRED]** 
        
          The unique identifier of the DC2 Reserved Node offering to be used for the exchange. You can obtain the value for the parameter by calling  GetReservedNodeExchangeOfferings  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ExchangedReservedNode\': {
                    \'ReservedNodeId\': \'string\',
                    \'ReservedNodeOfferingId\': \'string\',
                    \'NodeType\': \'string\',
                    \'StartTime\': datetime(2015, 1, 1),
                    \'Duration\': 123,
                    \'FixedPrice\': 123.0,
                    \'UsagePrice\': 123.0,
                    \'CurrencyCode\': \'string\',
                    \'NodeCount\': 123,
                    \'State\': \'string\',
                    \'OfferingType\': \'string\',
                    \'RecurringCharges\': [
                        {
                            \'RecurringChargeAmount\': 123.0,
                            \'RecurringChargeFrequency\': \'string\'
                        },
                    ],
                    \'ReservedNodeOfferingType\': \'Regular\'|\'Upgradable\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ExchangedReservedNode** *(dict) --* 
        
              Describes a reserved node. You can call the  DescribeReservedNodeOfferings API to obtain the available reserved node offerings. 
        
              - **ReservedNodeId** *(string) --* 
        
                The unique identifier for the reservation.
        
              - **ReservedNodeOfferingId** *(string) --* 
        
                The identifier for the reserved node offering.
        
              - **NodeType** *(string) --* 
        
                The node type of the reserved node.
        
              - **StartTime** *(datetime) --* 
        
                The time the reservation started. You purchase a reserved node offering for a duration. This is the start time of that duration.
        
              - **Duration** *(integer) --* 
        
                The duration of the node reservation in seconds.
        
              - **FixedPrice** *(float) --* 
        
                The fixed cost Amazon Redshift charges you for this reserved node.
        
              - **UsagePrice** *(float) --* 
        
                The hourly rate Amazon Redshift charges you for this reserved node.
        
              - **CurrencyCode** *(string) --* 
        
                The currency code for the reserved cluster.
        
              - **NodeCount** *(integer) --* 
        
                The number of reserved compute nodes.
        
              - **State** *(string) --* 
        
                The state of the reserved compute node.
        
                Possible Values:
        
                * pending-payment-This reserved node has recently been purchased, and the sale has been approved, but payment has not yet been confirmed. 
                 
                * active-This reserved node is owned by the caller and is available for use. 
                 
                * payment-failed-Payment failed for the purchase attempt. 
                 
                * retired-The reserved node is no longer available.  
                 
                * exchanging-The owner is exchanging the reserved node for another reserved node. 
                 
              - **OfferingType** *(string) --* 
        
                The anticipated utilization of the reserved node, as defined in the reserved node offering.
        
              - **RecurringCharges** *(list) --* 
        
                The recurring charges for the reserved node.
        
                - *(dict) --* 
        
                  Describes a recurring charge.
        
                  - **RecurringChargeAmount** *(float) --* 
        
                    The amount charged per the period of time specified by the recurring charge frequency.
        
                  - **RecurringChargeFrequency** *(string) --* 
        
                    The frequency at which the recurring charge amount is applied.
        
              - **ReservedNodeOfferingType** *(string) --* 
          
        """
        pass

    def authorize_cluster_security_group_ingress(self, ClusterSecurityGroupName: str, CIDRIP: str = None, EC2SecurityGroupName: str = None, EC2SecurityGroupOwnerId: str = None) -> Dict:
        """
        
        If you authorize access to an Amazon EC2 security group, specify *EC2SecurityGroupName* and *EC2SecurityGroupOwnerId* . The Amazon EC2 security group and Amazon Redshift cluster must be in the same AWS region. 
        
        If you authorize access to a CIDR/IP address range, specify *CIDRIP* . For an overview of CIDR blocks, see the Wikipedia article on `Classless Inter-Domain Routing <http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__ . 
        
        You must also associate the security group with a cluster so that clients running on these IP addresses or the EC2 instance are authorized to connect to the cluster. For information about managing security groups, go to `Working with Security Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/AuthorizeClusterSecurityGroupIngress>`_
        
        **Request Syntax** 
        ::
        
          response = client.authorize_cluster_security_group_ingress(
              ClusterSecurityGroupName=\'string\',
              CIDRIP=\'string\',
              EC2SecurityGroupName=\'string\',
              EC2SecurityGroupOwnerId=\'string\'
          )
        :type ClusterSecurityGroupName: string
        :param ClusterSecurityGroupName: **[REQUIRED]** 
        
          The name of the security group to which the ingress rule is added.
        
        :type CIDRIP: string
        :param CIDRIP: 
        
          The IP range to be added the Amazon Redshift security group.
        
        :type EC2SecurityGroupName: string
        :param EC2SecurityGroupName: 
        
          The EC2 security group to be added the Amazon Redshift security group.
        
        :type EC2SecurityGroupOwnerId: string
        :param EC2SecurityGroupOwnerId: 
        
          The AWS account number of the owner of the security group specified by the *EC2SecurityGroupName* parameter. The AWS Access Key ID is not an acceptable value. 
        
          Example: ``111122223333``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ClusterSecurityGroup\': {
                    \'ClusterSecurityGroupName\': \'string\',
                    \'Description\': \'string\',
                    \'EC2SecurityGroups\': [
                        {
                            \'Status\': \'string\',
                            \'EC2SecurityGroupName\': \'string\',
                            \'EC2SecurityGroupOwnerId\': \'string\',
                            \'Tags\': [
                                {
                                    \'Key\': \'string\',
                                    \'Value\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'IPRanges\': [
                        {
                            \'Status\': \'string\',
                            \'CIDRIP\': \'string\',
                            \'Tags\': [
                                {
                                    \'Key\': \'string\',
                                    \'Value\': \'string\'
                                },
                            ]
                        },
                    ],
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
            
            - **ClusterSecurityGroup** *(dict) --* 
        
              Describes a security group.
        
              - **ClusterSecurityGroupName** *(string) --* 
        
                The name of the cluster security group to which the operation was applied.
        
              - **Description** *(string) --* 
        
                A description of the security group.
        
              - **EC2SecurityGroups** *(list) --* 
        
                A list of EC2 security groups that are permitted to access clusters associated with this cluster security group.
        
                - *(dict) --* 
        
                  Describes an Amazon EC2 security group.
        
                  - **Status** *(string) --* 
        
                    The status of the EC2 security group.
        
                  - **EC2SecurityGroupName** *(string) --* 
        
                    The name of the EC2 Security Group.
        
                  - **EC2SecurityGroupOwnerId** *(string) --* 
        
                    The AWS ID of the owner of the EC2 security group specified in the ``EC2SecurityGroupName`` field. 
        
                  - **Tags** *(list) --* 
        
                    The list of tags for the EC2 security group.
        
                    - *(dict) --* 
        
                      A tag consisting of a name/value pair for a resource.
        
                      - **Key** *(string) --* 
        
                        The key, or name, for the resource tag.
        
                      - **Value** *(string) --* 
        
                        The value for the resource tag.
        
              - **IPRanges** *(list) --* 
        
                A list of IP ranges (CIDR blocks) that are permitted to access clusters associated with this cluster security group.
        
                - *(dict) --* 
        
                  Describes an IP range used in a security group.
        
                  - **Status** *(string) --* 
        
                    The status of the IP range, for example, \"authorized\".
        
                  - **CIDRIP** *(string) --* 
        
                    The IP range in Classless Inter-Domain Routing (CIDR) notation.
        
                  - **Tags** *(list) --* 
        
                    The list of tags for the IP range.
        
                    - *(dict) --* 
        
                      A tag consisting of a name/value pair for a resource.
        
                      - **Key** *(string) --* 
        
                        The key, or name, for the resource tag.
        
                      - **Value** *(string) --* 
        
                        The value for the resource tag.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster security group.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
        """
        pass

    def authorize_snapshot_access(self, SnapshotIdentifier: str, AccountWithRestoreAccess: str, SnapshotClusterIdentifier: str = None) -> Dict:
        """
        
        For more information about working with snapshots, go to `Amazon Redshift Snapshots <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/AuthorizeSnapshotAccess>`_
        
        **Request Syntax** 
        ::
        
          response = client.authorize_snapshot_access(
              SnapshotIdentifier=\'string\',
              SnapshotClusterIdentifier=\'string\',
              AccountWithRestoreAccess=\'string\'
          )
        :type SnapshotIdentifier: string
        :param SnapshotIdentifier: **[REQUIRED]** 
        
          The identifier of the snapshot the account is authorized to restore.
        
        :type SnapshotClusterIdentifier: string
        :param SnapshotClusterIdentifier: 
        
          The identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
        
        :type AccountWithRestoreAccess: string
        :param AccountWithRestoreAccess: **[REQUIRED]** 
        
          The identifier of the AWS customer account authorized to restore the specified snapshot.
        
          To share a snapshot with AWS support, specify amazon-redshift-support.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Snapshot\': {
                    \'SnapshotIdentifier\': \'string\',
                    \'ClusterIdentifier\': \'string\',
                    \'SnapshotCreateTime\': datetime(2015, 1, 1),
                    \'Status\': \'string\',
                    \'Port\': 123,
                    \'AvailabilityZone\': \'string\',
                    \'ClusterCreateTime\': datetime(2015, 1, 1),
                    \'MasterUsername\': \'string\',
                    \'ClusterVersion\': \'string\',
                    \'SnapshotType\': \'string\',
                    \'NodeType\': \'string\',
                    \'NumberOfNodes\': 123,
                    \'DBName\': \'string\',
                    \'VpcId\': \'string\',
                    \'Encrypted\': True|False,
                    \'KmsKeyId\': \'string\',
                    \'EncryptedWithHSM\': True|False,
                    \'AccountsWithRestoreAccess\': [
                        {
                            \'AccountId\': \'string\',
                            \'AccountAlias\': \'string\'
                        },
                    ],
                    \'OwnerAccount\': \'string\',
                    \'TotalBackupSizeInMegaBytes\': 123.0,
                    \'ActualIncrementalBackupSizeInMegaBytes\': 123.0,
                    \'BackupProgressInMegaBytes\': 123.0,
                    \'CurrentBackupRateInMegaBytesPerSecond\': 123.0,
                    \'EstimatedSecondsToCompletion\': 123,
                    \'ElapsedTimeInSeconds\': 123,
                    \'SourceRegion\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'RestorableNodeTypes\': [
                        \'string\',
                    ],
                    \'EnhancedVpcRouting\': True|False,
                    \'MaintenanceTrackName\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Snapshot** *(dict) --* 
        
              Describes a snapshot.
        
              - **SnapshotIdentifier** *(string) --* 
        
                The snapshot identifier that is provided in the request.
        
              - **ClusterIdentifier** *(string) --* 
        
                The identifier of the cluster for which the snapshot was taken.
        
              - **SnapshotCreateTime** *(datetime) --* 
        
                The time (UTC) when Amazon Redshift began the snapshot. A snapshot contains a copy of the cluster data as of this exact time.
        
              - **Status** *(string) --* 
        
                The snapshot status. The value of the status depends on the API operation used. 
        
                *  CreateClusterSnapshot and  CopyClusterSnapshot returns status as \"creating\".  
                 
                *  DescribeClusterSnapshots returns status as \"creating\", \"available\", \"final snapshot\", or \"failed\". 
                 
                *  DeleteClusterSnapshot returns status as \"deleted\". 
                 
              - **Port** *(integer) --* 
        
                The port that the cluster is listening on.
        
              - **AvailabilityZone** *(string) --* 
        
                The Availability Zone in which the cluster was created.
        
              - **ClusterCreateTime** *(datetime) --* 
        
                The time (UTC) when the cluster was originally created.
        
              - **MasterUsername** *(string) --* 
        
                The master user name for the cluster.
        
              - **ClusterVersion** *(string) --* 
        
                The version ID of the Amazon Redshift engine that is running on the cluster.
        
              - **SnapshotType** *(string) --* 
        
                The snapshot type. Snapshots created using  CreateClusterSnapshot and  CopyClusterSnapshot will be of type \"manual\". 
        
              - **NodeType** *(string) --* 
        
                The node type of the nodes in the cluster.
        
              - **NumberOfNodes** *(integer) --* 
        
                The number of nodes in the cluster.
        
              - **DBName** *(string) --* 
        
                The name of the database that was created when the cluster was created.
        
              - **VpcId** *(string) --* 
        
                The VPC identifier of the cluster if the snapshot is from a cluster in a VPC. Otherwise, this field is not in the output.
        
              - **Encrypted** *(boolean) --* 
        
                If ``true`` , the data in the snapshot is encrypted at rest.
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.
        
              - **EncryptedWithHSM** *(boolean) --* 
        
                A boolean that indicates whether the snapshot data is encrypted using the HSM keys of the source cluster. ``true`` indicates that the data is encrypted using HSM keys.
        
              - **AccountsWithRestoreAccess** *(list) --* 
        
                A list of the AWS customer accounts authorized to restore the snapshot. Returns ``null`` if no accounts are authorized. Visible only to the snapshot owner. 
        
                - *(dict) --* 
        
                  Describes an AWS customer account authorized to restore a snapshot.
        
                  - **AccountId** *(string) --* 
        
                    The identifier of an AWS customer account authorized to restore a snapshot.
        
                  - **AccountAlias** *(string) --* 
        
                    The identifier of an AWS support account authorized to restore a snapshot. For AWS support, the identifier is ``amazon-redshift-support`` . 
        
              - **OwnerAccount** *(string) --* 
        
                For manual snapshots, the AWS customer account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.
        
              - **TotalBackupSizeInMegaBytes** *(float) --* 
        
                The size of the complete set of backup data that would be used to restore the cluster.
        
              - **ActualIncrementalBackupSizeInMegaBytes** *(float) --* 
        
                The size of the incremental backup.
        
              - **BackupProgressInMegaBytes** *(float) --* 
        
                The number of megabytes that have been transferred to the snapshot backup.
        
              - **CurrentBackupRateInMegaBytesPerSecond** *(float) --* 
        
                The number of megabytes per second being transferred to the snapshot backup. Returns ``0`` for a completed backup. 
        
              - **EstimatedSecondsToCompletion** *(integer) --* 
        
                The estimate of the time remaining before the snapshot backup will complete. Returns ``0`` for a completed backup. 
        
              - **ElapsedTimeInSeconds** *(integer) --* 
        
                The amount of time an in-progress snapshot backup has been running, or the amount of time it took a completed backup to finish.
        
              - **SourceRegion** *(string) --* 
        
                The source region from which the snapshot was copied.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster snapshot.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
              - **RestorableNodeTypes** *(list) --* 
        
                The list of node types that this cluster snapshot is able to restore into.
        
                - *(string) --* 
            
              - **EnhancedVpcRouting** *(boolean) --* 
        
                An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                If this option is ``true`` , enhanced VPC routing is enabled. 
        
                Default: false
        
              - **MaintenanceTrackName** *(string) --* 
        
                The name of the maintenance track for the snapshot.
        
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

    def copy_cluster_snapshot(self, SourceSnapshotIdentifier: str, TargetSnapshotIdentifier: str, SourceSnapshotClusterIdentifier: str = None) -> Dict:
        """
        
        When you delete a cluster, Amazon Redshift deletes any automated snapshots of the cluster. Also, when the retention period of the snapshot expires, Amazon Redshift automatically deletes it. If you want to keep an automated snapshot for a longer period, you can make a manual copy of the snapshot. Manual snapshots are retained until you delete them.
        
        For more information about working with snapshots, go to `Amazon Redshift Snapshots <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/CopyClusterSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.copy_cluster_snapshot(
              SourceSnapshotIdentifier=\'string\',
              SourceSnapshotClusterIdentifier=\'string\',
              TargetSnapshotIdentifier=\'string\'
          )
        :type SourceSnapshotIdentifier: string
        :param SourceSnapshotIdentifier: **[REQUIRED]** 
        
          The identifier for the source snapshot.
        
          Constraints:
        
          * Must be the identifier for a valid automated snapshot whose state is ``available`` . 
           
        :type SourceSnapshotClusterIdentifier: string
        :param SourceSnapshotClusterIdentifier: 
        
          The identifier of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
        
          Constraints:
        
          * Must be the identifier for a valid cluster. 
           
        :type TargetSnapshotIdentifier: string
        :param TargetSnapshotIdentifier: **[REQUIRED]** 
        
          The identifier given to the new manual snapshot.
        
          Constraints:
        
          * Cannot be null, empty, or blank. 
           
          * Must contain from 1 to 255 alphanumeric characters or hyphens. 
           
          * First character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
          * Must be unique for the AWS account that is making the request. 
           
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Snapshot\': {
                    \'SnapshotIdentifier\': \'string\',
                    \'ClusterIdentifier\': \'string\',
                    \'SnapshotCreateTime\': datetime(2015, 1, 1),
                    \'Status\': \'string\',
                    \'Port\': 123,
                    \'AvailabilityZone\': \'string\',
                    \'ClusterCreateTime\': datetime(2015, 1, 1),
                    \'MasterUsername\': \'string\',
                    \'ClusterVersion\': \'string\',
                    \'SnapshotType\': \'string\',
                    \'NodeType\': \'string\',
                    \'NumberOfNodes\': 123,
                    \'DBName\': \'string\',
                    \'VpcId\': \'string\',
                    \'Encrypted\': True|False,
                    \'KmsKeyId\': \'string\',
                    \'EncryptedWithHSM\': True|False,
                    \'AccountsWithRestoreAccess\': [
                        {
                            \'AccountId\': \'string\',
                            \'AccountAlias\': \'string\'
                        },
                    ],
                    \'OwnerAccount\': \'string\',
                    \'TotalBackupSizeInMegaBytes\': 123.0,
                    \'ActualIncrementalBackupSizeInMegaBytes\': 123.0,
                    \'BackupProgressInMegaBytes\': 123.0,
                    \'CurrentBackupRateInMegaBytesPerSecond\': 123.0,
                    \'EstimatedSecondsToCompletion\': 123,
                    \'ElapsedTimeInSeconds\': 123,
                    \'SourceRegion\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'RestorableNodeTypes\': [
                        \'string\',
                    ],
                    \'EnhancedVpcRouting\': True|False,
                    \'MaintenanceTrackName\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Snapshot** *(dict) --* 
        
              Describes a snapshot.
        
              - **SnapshotIdentifier** *(string) --* 
        
                The snapshot identifier that is provided in the request.
        
              - **ClusterIdentifier** *(string) --* 
        
                The identifier of the cluster for which the snapshot was taken.
        
              - **SnapshotCreateTime** *(datetime) --* 
        
                The time (UTC) when Amazon Redshift began the snapshot. A snapshot contains a copy of the cluster data as of this exact time.
        
              - **Status** *(string) --* 
        
                The snapshot status. The value of the status depends on the API operation used. 
        
                *  CreateClusterSnapshot and  CopyClusterSnapshot returns status as \"creating\".  
                 
                *  DescribeClusterSnapshots returns status as \"creating\", \"available\", \"final snapshot\", or \"failed\". 
                 
                *  DeleteClusterSnapshot returns status as \"deleted\". 
                 
              - **Port** *(integer) --* 
        
                The port that the cluster is listening on.
        
              - **AvailabilityZone** *(string) --* 
        
                The Availability Zone in which the cluster was created.
        
              - **ClusterCreateTime** *(datetime) --* 
        
                The time (UTC) when the cluster was originally created.
        
              - **MasterUsername** *(string) --* 
        
                The master user name for the cluster.
        
              - **ClusterVersion** *(string) --* 
        
                The version ID of the Amazon Redshift engine that is running on the cluster.
        
              - **SnapshotType** *(string) --* 
        
                The snapshot type. Snapshots created using  CreateClusterSnapshot and  CopyClusterSnapshot will be of type \"manual\". 
        
              - **NodeType** *(string) --* 
        
                The node type of the nodes in the cluster.
        
              - **NumberOfNodes** *(integer) --* 
        
                The number of nodes in the cluster.
        
              - **DBName** *(string) --* 
        
                The name of the database that was created when the cluster was created.
        
              - **VpcId** *(string) --* 
        
                The VPC identifier of the cluster if the snapshot is from a cluster in a VPC. Otherwise, this field is not in the output.
        
              - **Encrypted** *(boolean) --* 
        
                If ``true`` , the data in the snapshot is encrypted at rest.
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.
        
              - **EncryptedWithHSM** *(boolean) --* 
        
                A boolean that indicates whether the snapshot data is encrypted using the HSM keys of the source cluster. ``true`` indicates that the data is encrypted using HSM keys.
        
              - **AccountsWithRestoreAccess** *(list) --* 
        
                A list of the AWS customer accounts authorized to restore the snapshot. Returns ``null`` if no accounts are authorized. Visible only to the snapshot owner. 
        
                - *(dict) --* 
        
                  Describes an AWS customer account authorized to restore a snapshot.
        
                  - **AccountId** *(string) --* 
        
                    The identifier of an AWS customer account authorized to restore a snapshot.
        
                  - **AccountAlias** *(string) --* 
        
                    The identifier of an AWS support account authorized to restore a snapshot. For AWS support, the identifier is ``amazon-redshift-support`` . 
        
              - **OwnerAccount** *(string) --* 
        
                For manual snapshots, the AWS customer account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.
        
              - **TotalBackupSizeInMegaBytes** *(float) --* 
        
                The size of the complete set of backup data that would be used to restore the cluster.
        
              - **ActualIncrementalBackupSizeInMegaBytes** *(float) --* 
        
                The size of the incremental backup.
        
              - **BackupProgressInMegaBytes** *(float) --* 
        
                The number of megabytes that have been transferred to the snapshot backup.
        
              - **CurrentBackupRateInMegaBytesPerSecond** *(float) --* 
        
                The number of megabytes per second being transferred to the snapshot backup. Returns ``0`` for a completed backup. 
        
              - **EstimatedSecondsToCompletion** *(integer) --* 
        
                The estimate of the time remaining before the snapshot backup will complete. Returns ``0`` for a completed backup. 
        
              - **ElapsedTimeInSeconds** *(integer) --* 
        
                The amount of time an in-progress snapshot backup has been running, or the amount of time it took a completed backup to finish.
        
              - **SourceRegion** *(string) --* 
        
                The source region from which the snapshot was copied.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster snapshot.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
              - **RestorableNodeTypes** *(list) --* 
        
                The list of node types that this cluster snapshot is able to restore into.
        
                - *(string) --* 
            
              - **EnhancedVpcRouting** *(boolean) --* 
        
                An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                If this option is ``true`` , enhanced VPC routing is enabled. 
        
                Default: false
        
              - **MaintenanceTrackName** *(string) --* 
        
                The name of the maintenance track for the snapshot.
        
        """
        pass

    def create_cluster(self, ClusterIdentifier: str, NodeType: str, MasterUsername: str, MasterUserPassword: str, DBName: str = None, ClusterType: str = None, ClusterSecurityGroups: List = None, VpcSecurityGroupIds: List = None, ClusterSubnetGroupName: str = None, AvailabilityZone: str = None, PreferredMaintenanceWindow: str = None, ClusterParameterGroupName: str = None, AutomatedSnapshotRetentionPeriod: int = None, Port: int = None, ClusterVersion: str = None, AllowVersionUpgrade: bool = None, NumberOfNodes: int = None, PubliclyAccessible: bool = None, Encrypted: bool = None, HsmClientCertificateIdentifier: str = None, HsmConfigurationIdentifier: str = None, ElasticIp: str = None, Tags: List = None, KmsKeyId: str = None, EnhancedVpcRouting: bool = None, AdditionalInfo: str = None, IamRoles: List = None, MaintenanceTrackName: str = None) -> Dict:
        """
        
        To create a cluster in Virtual Private Cloud (VPC), you must provide a cluster subnet group name. The cluster subnet group identifies the subnets of your VPC that Amazon Redshift uses when creating the cluster. For more information about managing clusters, go to `Amazon Redshift Clusters <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/CreateCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_cluster(
              DBName=\'string\',
              ClusterIdentifier=\'string\',
              ClusterType=\'string\',
              NodeType=\'string\',
              MasterUsername=\'string\',
              MasterUserPassword=\'string\',
              ClusterSecurityGroups=[
                  \'string\',
              ],
              VpcSecurityGroupIds=[
                  \'string\',
              ],
              ClusterSubnetGroupName=\'string\',
              AvailabilityZone=\'string\',
              PreferredMaintenanceWindow=\'string\',
              ClusterParameterGroupName=\'string\',
              AutomatedSnapshotRetentionPeriod=123,
              Port=123,
              ClusterVersion=\'string\',
              AllowVersionUpgrade=True|False,
              NumberOfNodes=123,
              PubliclyAccessible=True|False,
              Encrypted=True|False,
              HsmClientCertificateIdentifier=\'string\',
              HsmConfigurationIdentifier=\'string\',
              ElasticIp=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              KmsKeyId=\'string\',
              EnhancedVpcRouting=True|False,
              AdditionalInfo=\'string\',
              IamRoles=[
                  \'string\',
              ],
              MaintenanceTrackName=\'string\'
          )
        :type DBName: string
        :param DBName: 
        
          The name of the first database to be created when the cluster is created.
        
          To create additional databases after the cluster is created, connect to the cluster with a SQL client and use SQL commands to create a database. For more information, go to `Create a Database <http://docs.aws.amazon.com/redshift/latest/dg/t_creating_database.html>`__ in the Amazon Redshift Database Developer Guide. 
        
          Default: ``dev``  
        
          Constraints:
        
          * Must contain 1 to 64 alphanumeric characters. 
           
          * Must contain only lowercase letters. 
           
          * Cannot be a word that is reserved by the service. A list of reserved words can be found in `Reserved Words <http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`__ in the Amazon Redshift Database Developer Guide.  
           
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. The identifier also appears in the Amazon Redshift console.
        
          Constraints:
        
          * Must contain from 1 to 63 alphanumeric characters or hyphens. 
           
          * Alphabetic characters must be lowercase. 
           
          * First character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
          * Must be unique for all clusters within an AWS account. 
           
          Example: ``myexamplecluster``  
        
        :type ClusterType: string
        :param ClusterType: 
        
          The type of the cluster. When cluster type is specified as
        
          * ``single-node`` , the **NumberOfNodes** parameter is not required. 
           
          * ``multi-node`` , the **NumberOfNodes** parameter is required. 
           
          Valid Values: ``multi-node`` | ``single-node``  
        
          Default: ``multi-node``  
        
        :type NodeType: string
        :param NodeType: **[REQUIRED]** 
        
          The node type to be provisioned for the cluster. For information about node types, go to `Working with Clusters <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes>`__ in the *Amazon Redshift Cluster Management Guide* . 
        
          Valid Values: ``ds2.xlarge`` | ``ds2.8xlarge`` | ``ds2.xlarge`` | ``ds2.8xlarge`` | ``dc1.large`` | ``dc1.8xlarge`` | ``dc2.large`` | ``dc2.8xlarge``  
        
        :type MasterUsername: string
        :param MasterUsername: **[REQUIRED]** 
        
          The user name associated with the master user account for the cluster that is being created.
        
          Constraints:
        
          * Must be 1 - 128 alphanumeric characters. The user name can\'t be ``PUBLIC`` . 
           
          * First character must be a letter. 
           
          * Cannot be a reserved word. A list of reserved words can be found in `Reserved Words <http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`__ in the Amazon Redshift Database Developer Guide.  
           
        :type MasterUserPassword: string
        :param MasterUserPassword: **[REQUIRED]** 
        
          The password associated with the master user account for the cluster that is being created.
        
          Constraints:
        
          * Must be between 8 and 64 characters in length. 
           
          * Must contain at least one uppercase letter. 
           
          * Must contain at least one lowercase letter. 
           
          * Must contain one number. 
           
          * Can be any printable ASCII character (ASCII code 33 to 126) except \' (single quote), \" (double quote), \, /, @, or space. 
           
        :type ClusterSecurityGroups: list
        :param ClusterSecurityGroups: 
        
          A list of security groups to be associated with this cluster.
        
          Default: The default cluster security group for Amazon Redshift.
        
          - *(string) --* 
        
        :type VpcSecurityGroupIds: list
        :param VpcSecurityGroupIds: 
        
          A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.
        
          Default: The default VPC security group is associated with the cluster.
        
          - *(string) --* 
        
        :type ClusterSubnetGroupName: string
        :param ClusterSubnetGroupName: 
        
          The name of a cluster subnet group to be associated with this cluster.
        
          If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).
        
        :type AvailabilityZone: string
        :param AvailabilityZone: 
        
          The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.
        
          Default: A random, system-chosen Availability Zone in the region that is specified by the endpoint.
        
          Example: ``us-east-1d``  
        
          Constraint: The specified Availability Zone must be in the same region as the current endpoint.
        
        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow: 
        
          The weekly time range (in UTC) during which automated cluster maintenance can occur.
        
          Format: ``ddd:hh24:mi-ddd:hh24:mi``  
        
          Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. For more information about the time blocks for each region, see `Maintenance Windows <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-maintenance-windows>`__ in Amazon Redshift Cluster Management Guide.
        
          Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun
        
          Constraints: Minimum 30-minute window.
        
        :type ClusterParameterGroupName: string
        :param ClusterParameterGroupName: 
        
          The name of the parameter group to be associated with this cluster.
        
          Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to `Working with Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__  
        
          Constraints:
        
          * Must be 1 to 255 alphanumeric characters or hyphens. 
           
          * First character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
        :type AutomatedSnapshotRetentionPeriod: integer
        :param AutomatedSnapshotRetentionPeriod: 
        
          The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with  CreateClusterSnapshot . 
        
          Default: ``1``  
        
          Constraints: Must be a value from 0 to 35.
        
        :type Port: integer
        :param Port: 
        
          The port number on which the cluster accepts incoming connections.
        
          The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections.
        
          Default: ``5439``  
        
          Valid Values: ``1150-65535``  
        
        :type ClusterVersion: string
        :param ClusterVersion: 
        
          The version of the Amazon Redshift engine software that you want to deploy on the cluster.
        
          The version selected runs on all the nodes in the cluster.
        
          Constraints: Only version 1.0 is currently available.
        
          Example: ``1.0``  
        
        :type AllowVersionUpgrade: boolean
        :param AllowVersionUpgrade: 
        
          If ``true`` , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster.
        
          When a new major version of the Amazon Redshift engine is released, you can request that the service automatically apply upgrades during the maintenance window to the Amazon Redshift engine that is running on your cluster.
        
          Default: ``true``  
        
        :type NumberOfNodes: integer
        :param NumberOfNodes: 
        
          The number of compute nodes in the cluster. This parameter is required when the **ClusterType** parameter is specified as ``multi-node`` . 
        
          For information about determining how many nodes you need, go to `Working with Clusters <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes>`__ in the *Amazon Redshift Cluster Management Guide* . 
        
          If you don\'t specify this parameter, you get a single-node cluster. When requesting a multi-node cluster, you must specify the number of nodes that you want in the cluster.
        
          Default: ``1``  
        
          Constraints: Value must be at least 1 and no more than 100.
        
        :type PubliclyAccessible: boolean
        :param PubliclyAccessible: 
        
          If ``true`` , the cluster can be accessed from a public network. 
        
        :type Encrypted: boolean
        :param Encrypted: 
        
          If ``true`` , the data in the cluster is encrypted at rest. 
        
          Default: false
        
        :type HsmClientCertificateIdentifier: string
        :param HsmClientCertificateIdentifier: 
        
          Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        
        :type HsmConfigurationIdentifier: string
        :param HsmConfigurationIdentifier: 
        
          Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        
        :type ElasticIp: string
        :param ElasticIp: 
        
          The Elastic IP (EIP) address for the cluster.
        
          Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. For more information about provisioning clusters in EC2-VPC, go to `Supported Platforms to Launch Your Cluster <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms>`__ in the Amazon Redshift Cluster Management Guide.
        
        :type Tags: list
        :param Tags: 
        
          A list of tag instances.
        
          - *(dict) --* 
        
            A tag consisting of a name/value pair for a resource.
        
            - **Key** *(string) --* 
        
              The key, or name, for the resource tag.
        
            - **Value** *(string) --* 
        
              The value for the resource tag.
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.
        
        :type EnhancedVpcRouting: boolean
        :param EnhancedVpcRouting: 
        
          An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
          If this option is ``true`` , enhanced VPC routing is enabled. 
        
          Default: false
        
        :type AdditionalInfo: string
        :param AdditionalInfo: 
        
          Reserved.
        
        :type IamRoles: list
        :param IamRoles: 
        
          A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. You can supply up to 10 IAM roles in a single request.
        
          A cluster can have up to 10 IAM roles associated with it at any time.
        
          - *(string) --* 
        
        :type MaintenanceTrackName: string
        :param MaintenanceTrackName: 
        
          An optional parameter for the name of the maintenance track for the cluster. If you don\'t provide a maintenance track name, the cluster is assigned to the ``current`` track.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
                    \'ClusterIdentifier\': \'string\',
                    \'NodeType\': \'string\',
                    \'ClusterStatus\': \'string\',
                    \'ModifyStatus\': \'string\',
                    \'MasterUsername\': \'string\',
                    \'DBName\': \'string\',
                    \'Endpoint\': {
                        \'Address\': \'string\',
                        \'Port\': 123
                    },
                    \'ClusterCreateTime\': datetime(2015, 1, 1),
                    \'AutomatedSnapshotRetentionPeriod\': 123,
                    \'ClusterSecurityGroups\': [
                        {
                            \'ClusterSecurityGroupName\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'VpcSecurityGroups\': [
                        {
                            \'VpcSecurityGroupId\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'ClusterParameterGroups\': [
                        {
                            \'ParameterGroupName\': \'string\',
                            \'ParameterApplyStatus\': \'string\',
                            \'ClusterParameterStatusList\': [
                                {
                                    \'ParameterName\': \'string\',
                                    \'ParameterApplyStatus\': \'string\',
                                    \'ParameterApplyErrorDescription\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'ClusterSubnetGroupName\': \'string\',
                    \'VpcId\': \'string\',
                    \'AvailabilityZone\': \'string\',
                    \'PreferredMaintenanceWindow\': \'string\',
                    \'PendingModifiedValues\': {
                        \'MasterUserPassword\': \'string\',
                        \'NodeType\': \'string\',
                        \'NumberOfNodes\': 123,
                        \'ClusterType\': \'string\',
                        \'ClusterVersion\': \'string\',
                        \'AutomatedSnapshotRetentionPeriod\': 123,
                        \'ClusterIdentifier\': \'string\',
                        \'PubliclyAccessible\': True|False,
                        \'EnhancedVpcRouting\': True|False,
                        \'MaintenanceTrackName\': \'string\',
                        \'EncryptionType\': \'string\'
                    },
                    \'ClusterVersion\': \'string\',
                    \'AllowVersionUpgrade\': True|False,
                    \'NumberOfNodes\': 123,
                    \'PubliclyAccessible\': True|False,
                    \'Encrypted\': True|False,
                    \'RestoreStatus\': {
                        \'Status\': \'string\',
                        \'CurrentRestoreRateInMegaBytesPerSecond\': 123.0,
                        \'SnapshotSizeInMegaBytes\': 123,
                        \'ProgressInMegaBytes\': 123,
                        \'ElapsedTimeInSeconds\': 123,
                        \'EstimatedTimeToCompletionInSeconds\': 123
                    },
                    \'HsmStatus\': {
                        \'HsmClientCertificateIdentifier\': \'string\',
                        \'HsmConfigurationIdentifier\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterSnapshotCopyStatus\': {
                        \'DestinationRegion\': \'string\',
                        \'RetentionPeriod\': 123,
                        \'SnapshotCopyGrantName\': \'string\'
                    },
                    \'ClusterPublicKey\': \'string\',
                    \'ClusterNodes\': [
                        {
                            \'NodeRole\': \'string\',
                            \'PrivateIPAddress\': \'string\',
                            \'PublicIPAddress\': \'string\'
                        },
                    ],
                    \'ElasticIpStatus\': {
                        \'ElasticIp\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterRevisionNumber\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'KmsKeyId\': \'string\',
                    \'EnhancedVpcRouting\': True|False,
                    \'IamRoles\': [
                        {
                            \'IamRoleArn\': \'string\',
                            \'ApplyStatus\': \'string\'
                        },
                    ],
                    \'PendingActions\': [
                        \'string\',
                    ],
                    \'MaintenanceTrackName\': \'string\',
                    \'ElasticResizeNumberOfNodeOptions\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              Describes a cluster.
        
              - **ClusterIdentifier** *(string) --* 
        
                The unique identifier of the cluster.
        
              - **NodeType** *(string) --* 
        
                The node type for the nodes in the cluster.
        
              - **ClusterStatus** *(string) --* 
        
                The current state of the cluster. Possible values are the following:
        
                * ``available``   
                 
                * ``creating``   
                 
                * ``deleting``   
                 
                * ``final-snapshot``   
                 
                * ``hardware-failure``   
                 
                * ``incompatible-hsm``   
                 
                * ``incompatible-network``   
                 
                * ``incompatible-parameters``   
                 
                * ``incompatible-restore``   
                 
                * ``modifying``   
                 
                * ``rebooting``   
                 
                * ``renaming``   
                 
                * ``resizing``   
                 
                * ``rotating-keys``   
                 
                * ``storage-full``   
                 
                * ``updating-hsm``   
                 
              - **ModifyStatus** *(string) --* 
        
                The status of a modify operation, if any, initiated for the cluster.
        
              - **MasterUsername** *(string) --* 
        
                The master user name for the cluster. This name is used to connect to the database that is specified in the **DBName** parameter. 
        
              - **DBName** *(string) --* 
        
                The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named ``dev`` dev was created by default. 
        
              - **Endpoint** *(dict) --* 
        
                The connection endpoint.
        
                - **Address** *(string) --* 
        
                  The DNS address of the Cluster.
        
                - **Port** *(integer) --* 
        
                  The port that the database engine is listening on.
        
              - **ClusterCreateTime** *(datetime) --* 
        
                The date and time that the cluster was created.
        
              - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                The number of days that automatic cluster snapshots are retained.
        
              - **ClusterSecurityGroups** *(list) --* 
        
                A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ``ClusterSecurityGroup.Name`` and ``ClusterSecurityGroup.Status`` subelements. 
        
                Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the **VpcSecurityGroups** parameter. 
        
                - *(dict) --* 
        
                  Describes a cluster security group.
        
                  - **ClusterSecurityGroupName** *(string) --* 
        
                    The name of the cluster security group.
        
                  - **Status** *(string) --* 
        
                    The status of the cluster security group.
        
              - **VpcSecurityGroups** *(list) --* 
        
                A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.
        
                - *(dict) --* 
        
                  Describes the members of a VPC security group.
        
                  - **VpcSecurityGroupId** *(string) --* 
        
                    The identifier of the VPC security group.
        
                  - **Status** *(string) --* 
        
                    The status of the VPC security group.
        
              - **ClusterParameterGroups** *(list) --* 
        
                The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.
        
                - *(dict) --* 
        
                  Describes the status of a parameter group.
        
                  - **ParameterGroupName** *(string) --* 
        
                    The name of the cluster parameter group.
        
                  - **ParameterApplyStatus** *(string) --* 
        
                    The status of parameter updates.
        
                  - **ClusterParameterStatusList** *(list) --* 
        
                    The list of parameter statuses.
        
                    For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
                    - *(dict) --* 
        
                      Describes the status of a parameter group.
        
                      - **ParameterName** *(string) --* 
        
                        The name of the parameter.
        
                      - **ParameterApplyStatus** *(string) --* 
        
                        The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
        
                        The following are possible statuses and descriptions.
        
                        * ``in-sync`` : The parameter value is in sync with the database. 
                         
                        * ``pending-reboot`` : The parameter value will be applied after the cluster reboots. 
                         
                        * ``applying`` : The parameter value is being applied to the database. 
                         
                        * ``invalid-parameter`` : Cannot apply the parameter value because it has an invalid value or syntax. 
                         
                        * ``apply-deferred`` : The parameter contains static property changes. The changes are deferred until the cluster reboots. 
                         
                        * ``apply-error`` : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots. 
                         
                        * ``unknown-error`` : Cannot apply the parameter change right now. The change will be applied after the cluster reboots. 
                         
                      - **ParameterApplyErrorDescription** *(string) --* 
        
                        The error that prevented the parameter from being applied to the database.
        
              - **ClusterSubnetGroupName** *(string) --* 
        
                The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.
        
              - **VpcId** *(string) --* 
        
                The identifier of the VPC the cluster is in, if the cluster is in a VPC.
        
              - **AvailabilityZone** *(string) --* 
        
                The name of the Availability Zone in which the cluster is located.
        
              - **PreferredMaintenanceWindow** *(string) --* 
        
                The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.
        
              - **PendingModifiedValues** *(dict) --* 
        
                A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.
        
                - **MasterUserPassword** *(string) --* 
        
                  The pending or in-progress change of the master user password for the cluster.
        
                - **NodeType** *(string) --* 
        
                  The pending or in-progress change of the cluster\'s node type.
        
                - **NumberOfNodes** *(integer) --* 
        
                  The pending or in-progress change of the number of nodes in the cluster.
        
                - **ClusterType** *(string) --* 
        
                  The pending or in-progress change of the cluster type.
        
                - **ClusterVersion** *(string) --* 
        
                  The pending or in-progress change of the service version.
        
                - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                  The pending or in-progress change of the automated snapshot retention period.
        
                - **ClusterIdentifier** *(string) --* 
        
                  The pending or in-progress change of the new identifier for the cluster.
        
                - **PubliclyAccessible** *(boolean) --* 
        
                  The pending or in-progress change of the ability to connect to the cluster from the public network.
        
                - **EnhancedVpcRouting** *(boolean) --* 
        
                  An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                  If this option is ``true`` , enhanced VPC routing is enabled. 
        
                  Default: false
        
                - **MaintenanceTrackName** *(string) --* 
        
                  The name of the maintenance track that the cluster will change to during the next maintenance window.
        
                - **EncryptionType** *(string) --* 
        
                  The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy. 
        
              - **ClusterVersion** *(string) --* 
        
                The version ID of the Amazon Redshift engine that is running on the cluster.
        
              - **AllowVersionUpgrade** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window. 
        
              - **NumberOfNodes** *(integer) --* 
        
                The number of compute nodes in the cluster.
        
              - **PubliclyAccessible** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that the cluster can be accessed from a public network.
        
              - **Encrypted** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that data in the cluster is encrypted at rest.
        
              - **RestoreStatus** *(dict) --* 
        
                A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.
        
                - **Status** *(string) --* 
        
                  The status of the restore action. Returns starting, restoring, completed, or failed.
        
                - **CurrentRestoreRateInMegaBytesPerSecond** *(float) --* 
        
                  The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.
        
                - **SnapshotSizeInMegaBytes** *(integer) --* 
        
                  The size of the set of snapshot data used to restore the cluster.
        
                - **ProgressInMegaBytes** *(integer) --* 
        
                  The number of megabytes that have been transferred from snapshot storage.
        
                - **ElapsedTimeInSeconds** *(integer) --* 
        
                  The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.
        
                - **EstimatedTimeToCompletionInSeconds** *(integer) --* 
        
                  The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore.
        
              - **HsmStatus** *(dict) --* 
        
                A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
        
                Values: active, applying
        
                - **HsmClientCertificateIdentifier** *(string) --* 
        
                  Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        
                - **HsmConfigurationIdentifier** *(string) --* 
        
                  Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        
                - **Status** *(string) --* 
        
                  Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
        
                  Values: active, applying
        
              - **ClusterSnapshotCopyStatus** *(dict) --* 
        
                A value that returns the destination region and retention period that are configured for cross-region snapshot copy.
        
                - **DestinationRegion** *(string) --* 
        
                  The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
        
                - **RetentionPeriod** *(integer) --* 
        
                  The number of days that automated snapshots are retained in the destination region after they are copied from a source region.
        
                - **SnapshotCopyGrantName** *(string) --* 
        
                  The name of the snapshot copy grant.
        
              - **ClusterPublicKey** *(string) --* 
        
                The public key for the cluster.
        
              - **ClusterNodes** *(list) --* 
        
                The nodes in the cluster.
        
                - *(dict) --* 
        
                  The identifier of a node in a cluster.
        
                  - **NodeRole** *(string) --* 
        
                    Whether the node is a leader node or a compute node.
        
                  - **PrivateIPAddress** *(string) --* 
        
                    The private IP address of a node within a cluster.
        
                  - **PublicIPAddress** *(string) --* 
        
                    The public IP address of a node within a cluster.
        
              - **ElasticIpStatus** *(dict) --* 
        
                The status of the elastic IP (EIP) address.
        
                - **ElasticIp** *(string) --* 
        
                  The elastic IP (EIP) address for the cluster.
        
                - **Status** *(string) --* 
        
                  The status of the elastic IP (EIP) address.
        
              - **ClusterRevisionNumber** *(string) --* 
        
                The specific revision number of the database in the cluster.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.
        
              - **EnhancedVpcRouting** *(boolean) --* 
        
                An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                If this option is ``true`` , enhanced VPC routing is enabled. 
        
                Default: false
        
              - **IamRoles** *(list) --* 
        
                A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.
        
                - *(dict) --* 
        
                  An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.
        
                  - **IamRoleArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the IAM role, for example, ``arn:aws:iam::123456789012:role/RedshiftCopyUnload`` . 
        
                  - **ApplyStatus** *(string) --* 
        
                    A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
        
                    The following are possible statuses and descriptions.
        
                    * ``in-sync`` : The role is available for use by the cluster. 
                     
                    * ``adding`` : The role is in the process of being associated with the cluster. 
                     
                    * ``removing`` : The role is in the process of being disassociated with the cluster. 
                     
              - **PendingActions** *(list) --* 
        
                Cluster operations that are waiting to be started.
        
                - *(string) --* 
            
              - **MaintenanceTrackName** *(string) --* 
        
                The name of the maintenance track for the cluster.
        
              - **ElasticResizeNumberOfNodeOptions** *(string) --* 
        
                Indicates the number of nodes the cluster can be resized to with the elastic resize method. 
        
        """
        pass

    def create_cluster_parameter_group(self, ParameterGroupName: str, ParameterGroupFamily: str, Description: str, Tags: List = None) -> Dict:
        """
        
        Creating parameter groups is independent of creating clusters. You can associate a cluster with a parameter group when you create the cluster. You can also associate an existing cluster with a parameter group after the cluster is created by using  ModifyCluster . 
        
        Parameters in the parameter group define specific behavior that applies to the databases you create on the cluster. For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/CreateClusterParameterGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_cluster_parameter_group(
              ParameterGroupName=\'string\',
              ParameterGroupFamily=\'string\',
              Description=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type ParameterGroupName: string
        :param ParameterGroupName: **[REQUIRED]** 
        
          The name of the cluster parameter group.
        
          Constraints:
        
          * Must be 1 to 255 alphanumeric characters or hyphens 
           
          * First character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
          * Must be unique withing your AWS account. 
           
          .. note::
        
            This value is stored as a lower-case string.
        
        :type ParameterGroupFamily: string
        :param ParameterGroupFamily: **[REQUIRED]** 
        
          The Amazon Redshift engine version to which the cluster parameter group applies. The cluster engine version determines the set of parameters.
        
          To get a list of valid parameter group family names, you can call  DescribeClusterParameterGroups . By default, Amazon Redshift returns a list of all the parameter groups that are owned by your AWS account, including the default parameter groups for each Amazon Redshift engine version. The parameter group family names associated with the default parameter groups provide you the valid values. For example, a valid family name is \"redshift-1.0\". 
        
        :type Description: string
        :param Description: **[REQUIRED]** 
        
          A description of the parameter group.
        
        :type Tags: list
        :param Tags: 
        
          A list of tag instances.
        
          - *(dict) --* 
        
            A tag consisting of a name/value pair for a resource.
        
            - **Key** *(string) --* 
        
              The key, or name, for the resource tag.
        
            - **Value** *(string) --* 
        
              The value for the resource tag.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ClusterParameterGroup\': {
                    \'ParameterGroupName\': \'string\',
                    \'ParameterGroupFamily\': \'string\',
                    \'Description\': \'string\',
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
            
            - **ClusterParameterGroup** *(dict) --* 
        
              Describes a parameter group.
        
              - **ParameterGroupName** *(string) --* 
        
                The name of the cluster parameter group.
        
              - **ParameterGroupFamily** *(string) --* 
        
                The name of the cluster parameter group family that this cluster parameter group is compatible with.
        
              - **Description** *(string) --* 
        
                The description of the parameter group.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster parameter group.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
        """
        pass

    def create_cluster_security_group(self, ClusterSecurityGroupName: str, Description: str, Tags: List = None) -> Dict:
        """
        
        For information about managing security groups, go to `Amazon Redshift Cluster Security Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/CreateClusterSecurityGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_cluster_security_group(
              ClusterSecurityGroupName=\'string\',
              Description=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type ClusterSecurityGroupName: string
        :param ClusterSecurityGroupName: **[REQUIRED]** 
        
          The name for the security group. Amazon Redshift stores the value as a lowercase string.
        
          Constraints:
        
          * Must contain no more than 255 alphanumeric characters or hyphens. 
           
          * Must not be \"Default\". 
           
          * Must be unique for all security groups that are created by your AWS account. 
           
          Example: ``examplesecuritygroup``  
        
        :type Description: string
        :param Description: **[REQUIRED]** 
        
          A description for the security group.
        
        :type Tags: list
        :param Tags: 
        
          A list of tag instances.
        
          - *(dict) --* 
        
            A tag consisting of a name/value pair for a resource.
        
            - **Key** *(string) --* 
        
              The key, or name, for the resource tag.
        
            - **Value** *(string) --* 
        
              The value for the resource tag.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ClusterSecurityGroup\': {
                    \'ClusterSecurityGroupName\': \'string\',
                    \'Description\': \'string\',
                    \'EC2SecurityGroups\': [
                        {
                            \'Status\': \'string\',
                            \'EC2SecurityGroupName\': \'string\',
                            \'EC2SecurityGroupOwnerId\': \'string\',
                            \'Tags\': [
                                {
                                    \'Key\': \'string\',
                                    \'Value\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'IPRanges\': [
                        {
                            \'Status\': \'string\',
                            \'CIDRIP\': \'string\',
                            \'Tags\': [
                                {
                                    \'Key\': \'string\',
                                    \'Value\': \'string\'
                                },
                            ]
                        },
                    ],
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
            
            - **ClusterSecurityGroup** *(dict) --* 
        
              Describes a security group.
        
              - **ClusterSecurityGroupName** *(string) --* 
        
                The name of the cluster security group to which the operation was applied.
        
              - **Description** *(string) --* 
        
                A description of the security group.
        
              - **EC2SecurityGroups** *(list) --* 
        
                A list of EC2 security groups that are permitted to access clusters associated with this cluster security group.
        
                - *(dict) --* 
        
                  Describes an Amazon EC2 security group.
        
                  - **Status** *(string) --* 
        
                    The status of the EC2 security group.
        
                  - **EC2SecurityGroupName** *(string) --* 
        
                    The name of the EC2 Security Group.
        
                  - **EC2SecurityGroupOwnerId** *(string) --* 
        
                    The AWS ID of the owner of the EC2 security group specified in the ``EC2SecurityGroupName`` field. 
        
                  - **Tags** *(list) --* 
        
                    The list of tags for the EC2 security group.
        
                    - *(dict) --* 
        
                      A tag consisting of a name/value pair for a resource.
        
                      - **Key** *(string) --* 
        
                        The key, or name, for the resource tag.
        
                      - **Value** *(string) --* 
        
                        The value for the resource tag.
        
              - **IPRanges** *(list) --* 
        
                A list of IP ranges (CIDR blocks) that are permitted to access clusters associated with this cluster security group.
        
                - *(dict) --* 
        
                  Describes an IP range used in a security group.
        
                  - **Status** *(string) --* 
        
                    The status of the IP range, for example, \"authorized\".
        
                  - **CIDRIP** *(string) --* 
        
                    The IP range in Classless Inter-Domain Routing (CIDR) notation.
        
                  - **Tags** *(list) --* 
        
                    The list of tags for the IP range.
        
                    - *(dict) --* 
        
                      A tag consisting of a name/value pair for a resource.
        
                      - **Key** *(string) --* 
        
                        The key, or name, for the resource tag.
        
                      - **Value** *(string) --* 
        
                        The value for the resource tag.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster security group.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
        """
        pass

    def create_cluster_snapshot(self, SnapshotIdentifier: str, ClusterIdentifier: str, Tags: List = None) -> Dict:
        """
        
        For more information about working with snapshots, go to `Amazon Redshift Snapshots <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/CreateClusterSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_cluster_snapshot(
              SnapshotIdentifier=\'string\',
              ClusterIdentifier=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type SnapshotIdentifier: string
        :param SnapshotIdentifier: **[REQUIRED]** 
        
          A unique identifier for the snapshot that you are requesting. This identifier must be unique for all snapshots within the AWS account.
        
          Constraints:
        
          * Cannot be null, empty, or blank 
           
          * Must contain from 1 to 255 alphanumeric characters or hyphens 
           
          * First character must be a letter 
           
          * Cannot end with a hyphen or contain two consecutive hyphens 
           
          Example: ``my-snapshot-id``  
        
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          The cluster identifier for which you want a snapshot.
        
        :type Tags: list
        :param Tags: 
        
          A list of tag instances.
        
          - *(dict) --* 
        
            A tag consisting of a name/value pair for a resource.
        
            - **Key** *(string) --* 
        
              The key, or name, for the resource tag.
        
            - **Value** *(string) --* 
        
              The value for the resource tag.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Snapshot\': {
                    \'SnapshotIdentifier\': \'string\',
                    \'ClusterIdentifier\': \'string\',
                    \'SnapshotCreateTime\': datetime(2015, 1, 1),
                    \'Status\': \'string\',
                    \'Port\': 123,
                    \'AvailabilityZone\': \'string\',
                    \'ClusterCreateTime\': datetime(2015, 1, 1),
                    \'MasterUsername\': \'string\',
                    \'ClusterVersion\': \'string\',
                    \'SnapshotType\': \'string\',
                    \'NodeType\': \'string\',
                    \'NumberOfNodes\': 123,
                    \'DBName\': \'string\',
                    \'VpcId\': \'string\',
                    \'Encrypted\': True|False,
                    \'KmsKeyId\': \'string\',
                    \'EncryptedWithHSM\': True|False,
                    \'AccountsWithRestoreAccess\': [
                        {
                            \'AccountId\': \'string\',
                            \'AccountAlias\': \'string\'
                        },
                    ],
                    \'OwnerAccount\': \'string\',
                    \'TotalBackupSizeInMegaBytes\': 123.0,
                    \'ActualIncrementalBackupSizeInMegaBytes\': 123.0,
                    \'BackupProgressInMegaBytes\': 123.0,
                    \'CurrentBackupRateInMegaBytesPerSecond\': 123.0,
                    \'EstimatedSecondsToCompletion\': 123,
                    \'ElapsedTimeInSeconds\': 123,
                    \'SourceRegion\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'RestorableNodeTypes\': [
                        \'string\',
                    ],
                    \'EnhancedVpcRouting\': True|False,
                    \'MaintenanceTrackName\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Snapshot** *(dict) --* 
        
              Describes a snapshot.
        
              - **SnapshotIdentifier** *(string) --* 
        
                The snapshot identifier that is provided in the request.
        
              - **ClusterIdentifier** *(string) --* 
        
                The identifier of the cluster for which the snapshot was taken.
        
              - **SnapshotCreateTime** *(datetime) --* 
        
                The time (UTC) when Amazon Redshift began the snapshot. A snapshot contains a copy of the cluster data as of this exact time.
        
              - **Status** *(string) --* 
        
                The snapshot status. The value of the status depends on the API operation used. 
        
                *  CreateClusterSnapshot and  CopyClusterSnapshot returns status as \"creating\".  
                 
                *  DescribeClusterSnapshots returns status as \"creating\", \"available\", \"final snapshot\", or \"failed\". 
                 
                *  DeleteClusterSnapshot returns status as \"deleted\". 
                 
              - **Port** *(integer) --* 
        
                The port that the cluster is listening on.
        
              - **AvailabilityZone** *(string) --* 
        
                The Availability Zone in which the cluster was created.
        
              - **ClusterCreateTime** *(datetime) --* 
        
                The time (UTC) when the cluster was originally created.
        
              - **MasterUsername** *(string) --* 
        
                The master user name for the cluster.
        
              - **ClusterVersion** *(string) --* 
        
                The version ID of the Amazon Redshift engine that is running on the cluster.
        
              - **SnapshotType** *(string) --* 
        
                The snapshot type. Snapshots created using  CreateClusterSnapshot and  CopyClusterSnapshot will be of type \"manual\". 
        
              - **NodeType** *(string) --* 
        
                The node type of the nodes in the cluster.
        
              - **NumberOfNodes** *(integer) --* 
        
                The number of nodes in the cluster.
        
              - **DBName** *(string) --* 
        
                The name of the database that was created when the cluster was created.
        
              - **VpcId** *(string) --* 
        
                The VPC identifier of the cluster if the snapshot is from a cluster in a VPC. Otherwise, this field is not in the output.
        
              - **Encrypted** *(boolean) --* 
        
                If ``true`` , the data in the snapshot is encrypted at rest.
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.
        
              - **EncryptedWithHSM** *(boolean) --* 
        
                A boolean that indicates whether the snapshot data is encrypted using the HSM keys of the source cluster. ``true`` indicates that the data is encrypted using HSM keys.
        
              - **AccountsWithRestoreAccess** *(list) --* 
        
                A list of the AWS customer accounts authorized to restore the snapshot. Returns ``null`` if no accounts are authorized. Visible only to the snapshot owner. 
        
                - *(dict) --* 
        
                  Describes an AWS customer account authorized to restore a snapshot.
        
                  - **AccountId** *(string) --* 
        
                    The identifier of an AWS customer account authorized to restore a snapshot.
        
                  - **AccountAlias** *(string) --* 
        
                    The identifier of an AWS support account authorized to restore a snapshot. For AWS support, the identifier is ``amazon-redshift-support`` . 
        
              - **OwnerAccount** *(string) --* 
        
                For manual snapshots, the AWS customer account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.
        
              - **TotalBackupSizeInMegaBytes** *(float) --* 
        
                The size of the complete set of backup data that would be used to restore the cluster.
        
              - **ActualIncrementalBackupSizeInMegaBytes** *(float) --* 
        
                The size of the incremental backup.
        
              - **BackupProgressInMegaBytes** *(float) --* 
        
                The number of megabytes that have been transferred to the snapshot backup.
        
              - **CurrentBackupRateInMegaBytesPerSecond** *(float) --* 
        
                The number of megabytes per second being transferred to the snapshot backup. Returns ``0`` for a completed backup. 
        
              - **EstimatedSecondsToCompletion** *(integer) --* 
        
                The estimate of the time remaining before the snapshot backup will complete. Returns ``0`` for a completed backup. 
        
              - **ElapsedTimeInSeconds** *(integer) --* 
        
                The amount of time an in-progress snapshot backup has been running, or the amount of time it took a completed backup to finish.
        
              - **SourceRegion** *(string) --* 
        
                The source region from which the snapshot was copied.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster snapshot.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
              - **RestorableNodeTypes** *(list) --* 
        
                The list of node types that this cluster snapshot is able to restore into.
        
                - *(string) --* 
            
              - **EnhancedVpcRouting** *(boolean) --* 
        
                An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                If this option is ``true`` , enhanced VPC routing is enabled. 
        
                Default: false
        
              - **MaintenanceTrackName** *(string) --* 
        
                The name of the maintenance track for the snapshot.
        
        """
        pass

    def create_cluster_subnet_group(self, ClusterSubnetGroupName: str, Description: str, SubnetIds: List, Tags: List = None) -> Dict:
        """
        
        For information about subnet groups, go to `Amazon Redshift Cluster Subnet Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-cluster-subnet-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/CreateClusterSubnetGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_cluster_subnet_group(
              ClusterSubnetGroupName=\'string\',
              Description=\'string\',
              SubnetIds=[
                  \'string\',
              ],
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type ClusterSubnetGroupName: string
        :param ClusterSubnetGroupName: **[REQUIRED]** 
        
          The name for the subnet group. Amazon Redshift stores the value as a lowercase string.
        
          Constraints:
        
          * Must contain no more than 255 alphanumeric characters or hyphens. 
           
          * Must not be \"Default\". 
           
          * Must be unique for all subnet groups that are created by your AWS account. 
           
          Example: ``examplesubnetgroup``  
        
        :type Description: string
        :param Description: **[REQUIRED]** 
        
          A description for the subnet group.
        
        :type SubnetIds: list
        :param SubnetIds: **[REQUIRED]** 
        
          An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.
        
          - *(string) --* 
        
        :type Tags: list
        :param Tags: 
        
          A list of tag instances.
        
          - *(dict) --* 
        
            A tag consisting of a name/value pair for a resource.
        
            - **Key** *(string) --* 
        
              The key, or name, for the resource tag.
        
            - **Value** *(string) --* 
        
              The value for the resource tag.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ClusterSubnetGroup\': {
                    \'ClusterSubnetGroupName\': \'string\',
                    \'Description\': \'string\',
                    \'VpcId\': \'string\',
                    \'SubnetGroupStatus\': \'string\',
                    \'Subnets\': [
                        {
                            \'SubnetIdentifier\': \'string\',
                            \'SubnetAvailabilityZone\': {
                                \'Name\': \'string\',
                                \'SupportedPlatforms\': [
                                    {
                                        \'Name\': \'string\'
                                    },
                                ]
                            },
                            \'SubnetStatus\': \'string\'
                        },
                    ],
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
            
            - **ClusterSubnetGroup** *(dict) --* 
        
              Describes a subnet group.
        
              - **ClusterSubnetGroupName** *(string) --* 
        
                The name of the cluster subnet group.
        
              - **Description** *(string) --* 
        
                The description of the cluster subnet group.
        
              - **VpcId** *(string) --* 
        
                The VPC ID of the cluster subnet group.
        
              - **SubnetGroupStatus** *(string) --* 
        
                The status of the cluster subnet group. Possible values are ``Complete`` , ``Incomplete`` and ``Invalid`` . 
        
              - **Subnets** *(list) --* 
        
                A list of the VPC  Subnet elements. 
        
                - *(dict) --* 
        
                  Describes a subnet.
        
                  - **SubnetIdentifier** *(string) --* 
        
                    The identifier of the subnet.
        
                  - **SubnetAvailabilityZone** *(dict) --* 
        
                    Describes an availability zone.
        
                    - **Name** *(string) --* 
        
                      The name of the availability zone.
        
                    - **SupportedPlatforms** *(list) --* 
                      
                      - *(dict) --* 
        
                        A list of supported platforms for orderable clusters.
        
                        - **Name** *(string) --* 
                    
                  - **SubnetStatus** *(string) --* 
        
                    The status of the subnet.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster subnet group.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
        """
        pass

    def create_event_subscription(self, SubscriptionName: str, SnsTopicArn: str, SourceType: str = None, SourceIds: List = None, EventCategories: List = None, Severity: str = None, Enabled: bool = None, Tags: List = None) -> Dict:
        """
        
        You can specify the source type, and lists of Amazon Redshift source IDs, event categories, and event severities. Notifications will be sent for all events you want that match those criteria. For example, you can specify source type = cluster, source ID = my-cluster-1 and mycluster2, event categories = Availability, Backup, and severity = ERROR. The subscription will only send notifications for those ERROR events in the Availability and Backup categories for the specified clusters.
        
        If you specify both the source type and source IDs, such as source type = cluster and source identifier = my-cluster-1, notifications will be sent for all the cluster events for my-cluster-1. If you specify a source type but do not specify a source identifier, you will receive notice of the events for the objects of that type in your AWS account. If you do not specify either the SourceType nor the SourceIdentifier, you will be notified of events generated from all Amazon Redshift sources belonging to your AWS account. You must specify a source type if you specify a source ID.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/CreateEventSubscription>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_event_subscription(
              SubscriptionName=\'string\',
              SnsTopicArn=\'string\',
              SourceType=\'string\',
              SourceIds=[
                  \'string\',
              ],
              EventCategories=[
                  \'string\',
              ],
              Severity=\'string\',
              Enabled=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type SubscriptionName: string
        :param SubscriptionName: **[REQUIRED]** 
        
          The name of the event subscription to be created.
        
          Constraints:
        
          * Cannot be null, empty, or blank. 
           
          * Must contain from 1 to 255 alphanumeric characters or hyphens. 
           
          * First character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
        :type SnsTopicArn: string
        :param SnsTopicArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
        
        :type SourceType: string
        :param SourceType: 
        
          The type of source that will be generating the events. For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your AWS account. You must specify a source type in order to specify source IDs.
        
          Valid values: cluster, cluster-parameter-group, cluster-security-group, and cluster-snapshot.
        
        :type SourceIds: list
        :param SourceIds: 
        
          A list of one or more identifiers of Amazon Redshift source objects. All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified.
        
          Example: my-cluster-1, my-cluster-2
        
          Example: my-snapshot-20131010
        
          - *(string) --* 
        
        :type EventCategories: list
        :param EventCategories: 
        
          Specifies the Amazon Redshift event categories to be published by the event notification subscription.
        
          Values: Configuration, Management, Monitoring, Security
        
          - *(string) --* 
        
        :type Severity: string
        :param Severity: 
        
          Specifies the Amazon Redshift event severity to be published by the event notification subscription.
        
          Values: ERROR, INFO
        
        :type Enabled: boolean
        :param Enabled: 
        
          A Boolean value; set to ``true`` to activate the subscription, set to ``false`` to create the subscription but not active it. 
        
        :type Tags: list
        :param Tags: 
        
          A list of tag instances.
        
          - *(dict) --* 
        
            A tag consisting of a name/value pair for a resource.
        
            - **Key** *(string) --* 
        
              The key, or name, for the resource tag.
        
            - **Value** *(string) --* 
        
              The value for the resource tag.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EventSubscription\': {
                    \'CustomerAwsId\': \'string\',
                    \'CustSubscriptionId\': \'string\',
                    \'SnsTopicArn\': \'string\',
                    \'Status\': \'string\',
                    \'SubscriptionCreationTime\': datetime(2015, 1, 1),
                    \'SourceType\': \'string\',
                    \'SourceIdsList\': [
                        \'string\',
                    ],
                    \'EventCategoriesList\': [
                        \'string\',
                    ],
                    \'Severity\': \'string\',
                    \'Enabled\': True|False,
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
            
            - **EventSubscription** *(dict) --* 
        
              Describes event subscriptions.
        
              - **CustomerAwsId** *(string) --* 
        
                The AWS customer account associated with the Amazon Redshift event notification subscription.
        
              - **CustSubscriptionId** *(string) --* 
        
                The name of the Amazon Redshift event notification subscription.
        
              - **SnsTopicArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the Amazon SNS topic used by the event notification subscription.
        
              - **Status** *(string) --* 
        
                The status of the Amazon Redshift event notification subscription.
        
                Constraints:
        
                * Can be one of the following: active | no-permission | topic-not-exist 
                 
                * The status \"no-permission\" indicates that Amazon Redshift no longer has permission to post to the Amazon SNS topic. The status \"topic-not-exist\" indicates that the topic was deleted after the subscription was created. 
                 
              - **SubscriptionCreationTime** *(datetime) --* 
        
                The date and time the Amazon Redshift event notification subscription was created.
        
              - **SourceType** *(string) --* 
        
                The source type of the events returned the Amazon Redshift event notification, such as cluster, or cluster-snapshot.
        
              - **SourceIdsList** *(list) --* 
        
                A list of the sources that publish events to the Amazon Redshift event notification subscription.
        
                - *(string) --* 
            
              - **EventCategoriesList** *(list) --* 
        
                The list of Amazon Redshift event categories specified in the event notification subscription.
        
                Values: Configuration, Management, Monitoring, Security
        
                - *(string) --* 
            
              - **Severity** *(string) --* 
        
                The event severity specified in the Amazon Redshift event notification subscription.
        
                Values: ERROR, INFO
        
              - **Enabled** *(boolean) --* 
        
                A Boolean value indicating whether the subscription is enabled. ``true`` indicates the subscription is enabled.
        
              - **Tags** *(list) --* 
        
                The list of tags for the event subscription.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
        """
        pass

    def create_hsm_client_certificate(self, HsmClientCertificateIdentifier: str, Tags: List = None) -> Dict:
        """
        
        The command returns a public key, which you must store in the HSM. In addition to creating the HSM certificate, you must create an Amazon Redshift HSM configuration that provides a cluster the information needed to store and use encryption keys in the HSM. For more information, go to `Hardware Security Modules <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-HSM.html>`__ in the Amazon Redshift Cluster Management Guide.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/CreateHsmClientCertificate>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_hsm_client_certificate(
              HsmClientCertificateIdentifier=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type HsmClientCertificateIdentifier: string
        :param HsmClientCertificateIdentifier: **[REQUIRED]** 
        
          The identifier to be assigned to the new HSM client certificate that the cluster will use to connect to the HSM to use the database encryption keys.
        
        :type Tags: list
        :param Tags: 
        
          A list of tag instances.
        
          - *(dict) --* 
        
            A tag consisting of a name/value pair for a resource.
        
            - **Key** *(string) --* 
        
              The key, or name, for the resource tag.
        
            - **Value** *(string) --* 
        
              The value for the resource tag.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'HsmClientCertificate\': {
                    \'HsmClientCertificateIdentifier\': \'string\',
                    \'HsmClientCertificatePublicKey\': \'string\',
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
            
            - **HsmClientCertificate** *(dict) --* 
        
              Returns information about an HSM client certificate. The certificate is stored in a secure Hardware Storage Module (HSM), and used by the Amazon Redshift cluster to encrypt data files.
        
              - **HsmClientCertificateIdentifier** *(string) --* 
        
                The identifier of the HSM client certificate.
        
              - **HsmClientCertificatePublicKey** *(string) --* 
        
                The public key that the Amazon Redshift cluster will use to connect to the HSM. You must register the public key in the HSM.
        
              - **Tags** *(list) --* 
        
                The list of tags for the HSM client certificate.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
        """
        pass

    def create_hsm_configuration(self, HsmConfigurationIdentifier: str, Description: str, HsmIpAddress: str, HsmPartitionName: str, HsmPartitionPassword: str, HsmServerPublicCertificate: str, Tags: List = None) -> Dict:
        """
        
        In addition to creating an HSM configuration, you must also create an HSM client certificate. For more information, go to `Hardware Security Modules <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-HSM.html>`__ in the Amazon Redshift Cluster Management Guide.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/CreateHsmConfiguration>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_hsm_configuration(
              HsmConfigurationIdentifier=\'string\',
              Description=\'string\',
              HsmIpAddress=\'string\',
              HsmPartitionName=\'string\',
              HsmPartitionPassword=\'string\',
              HsmServerPublicCertificate=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type HsmConfigurationIdentifier: string
        :param HsmConfigurationIdentifier: **[REQUIRED]** 
        
          The identifier to be assigned to the new Amazon Redshift HSM configuration.
        
        :type Description: string
        :param Description: **[REQUIRED]** 
        
          A text description of the HSM configuration to be created.
        
        :type HsmIpAddress: string
        :param HsmIpAddress: **[REQUIRED]** 
        
          The IP address that the Amazon Redshift cluster must use to access the HSM.
        
        :type HsmPartitionName: string
        :param HsmPartitionName: **[REQUIRED]** 
        
          The name of the partition in the HSM where the Amazon Redshift clusters will store their database encryption keys.
        
        :type HsmPartitionPassword: string
        :param HsmPartitionPassword: **[REQUIRED]** 
        
          The password required to access the HSM partition.
        
        :type HsmServerPublicCertificate: string
        :param HsmServerPublicCertificate: **[REQUIRED]** 
        
          The HSMs public certificate file. When using Cloud HSM, the file name is server.pem.
        
        :type Tags: list
        :param Tags: 
        
          A list of tag instances.
        
          - *(dict) --* 
        
            A tag consisting of a name/value pair for a resource.
        
            - **Key** *(string) --* 
        
              The key, or name, for the resource tag.
        
            - **Value** *(string) --* 
        
              The value for the resource tag.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'HsmConfiguration\': {
                    \'HsmConfigurationIdentifier\': \'string\',
                    \'Description\': \'string\',
                    \'HsmIpAddress\': \'string\',
                    \'HsmPartitionName\': \'string\',
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
            
            - **HsmConfiguration** *(dict) --* 
        
              Returns information about an HSM configuration, which is an object that describes to Amazon Redshift clusters the information they require to connect to an HSM where they can store database encryption keys.
        
              - **HsmConfigurationIdentifier** *(string) --* 
        
                The name of the Amazon Redshift HSM configuration.
        
              - **Description** *(string) --* 
        
                A text description of the HSM configuration.
        
              - **HsmIpAddress** *(string) --* 
        
                The IP address that the Amazon Redshift cluster must use to access the HSM.
        
              - **HsmPartitionName** *(string) --* 
        
                The name of the partition in the HSM where the Amazon Redshift clusters will store their database encryption keys.
        
              - **Tags** *(list) --* 
        
                The list of tags for the HSM configuration.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
        """
        pass

    def create_snapshot_copy_grant(self, SnapshotCopyGrantName: str, KmsKeyId: str = None, Tags: List = None) -> Dict:
        """
        
        For more information about managing snapshot copy grants, go to `Amazon Redshift Database Encryption <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html>`__ in the *Amazon Redshift Cluster Management Guide* . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/CreateSnapshotCopyGrant>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_snapshot_copy_grant(
              SnapshotCopyGrantName=\'string\',
              KmsKeyId=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type SnapshotCopyGrantName: string
        :param SnapshotCopyGrantName: **[REQUIRED]** 
        
          The name of the snapshot copy grant. This name must be unique in the region for the AWS account.
        
          Constraints:
        
          * Must contain from 1 to 63 alphanumeric characters or hyphens. 
           
          * Alphabetic characters must be lowercase. 
           
          * First character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
          * Must be unique for all clusters within an AWS account. 
           
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          The unique identifier of the customer master key (CMK) to which to grant Amazon Redshift permission. If no key is specified, the default key is used.
        
        :type Tags: list
        :param Tags: 
        
          A list of tag instances.
        
          - *(dict) --* 
        
            A tag consisting of a name/value pair for a resource.
        
            - **Key** *(string) --* 
        
              The key, or name, for the resource tag.
        
            - **Value** *(string) --* 
        
              The value for the resource tag.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SnapshotCopyGrant\': {
                    \'SnapshotCopyGrantName\': \'string\',
                    \'KmsKeyId\': \'string\',
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
            
            - **SnapshotCopyGrant** *(dict) --* 
        
              The snapshot copy grant that grants Amazon Redshift permission to encrypt copied snapshots with the specified customer master key (CMK) from AWS KMS in the destination region.
        
              For more information about managing snapshot copy grants, go to `Amazon Redshift Database Encryption <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html>`__ in the *Amazon Redshift Cluster Management Guide* . 
        
              - **SnapshotCopyGrantName** *(string) --* 
        
                The name of the snapshot copy grant.
        
              - **KmsKeyId** *(string) --* 
        
                The unique identifier of the customer master key (CMK) in AWS KMS to which Amazon Redshift is granted permission.
        
              - **Tags** *(list) --* 
        
                A list of tag instances.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
        """
        pass

    def create_tags(self, ResourceName: str, Tags: List) -> NoReturn:
        """
        
        A resource can have up to 50 tags. If you try to create more than 50 tags for a resource, you will receive an error and the attempt will fail.
        
        If you specify a key that already exists for the resource, the value for that key will be updated with the new value.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/CreateTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_tags(
              ResourceName=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type ResourceName: string
        :param ResourceName: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) to which you want to add the tag or tags. For example, ``arn:aws:redshift:us-east-1:123456789:cluster:t1`` . 
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          One or more name/value pairs to add as tags to the specified resource. Each tag name is passed in with the parameter ``Key`` and the corresponding value is passed in with the parameter ``Value`` . The ``Key`` and ``Value`` parameters are separated by a comma (,). Separate multiple tags with a space. For example, ``--tags \"Key\"=\"owner\",\"Value\"=\"admin\" \"Key\"=\"environment\",\"Value\"=\"test\" \"Key\"=\"version\",\"Value\"=\"1.0\"`` . 
        
          - *(dict) --* 
        
            A tag consisting of a name/value pair for a resource.
        
            - **Key** *(string) --* 
        
              The key, or name, for the resource tag.
        
            - **Value** *(string) --* 
        
              The value for the resource tag.
        
        :returns: None
        """
        pass

    def delete_cluster(self, ClusterIdentifier: str, SkipFinalClusterSnapshot: bool = None, FinalClusterSnapshotIdentifier: str = None) -> Dict:
        """
        
        If you want to shut down the cluster and retain it for future use, set *SkipFinalClusterSnapshot* to ``false`` and specify a name for *FinalClusterSnapshotIdentifier* . You can later restore this snapshot to resume using the cluster. If a final cluster snapshot is requested, the status of the cluster will be \"final-snapshot\" while the snapshot is being taken, then it\'s \"deleting\" once Amazon Redshift begins deleting the cluster. 
        
        For more information about managing clusters, go to `Amazon Redshift Clusters <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DeleteCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_cluster(
              ClusterIdentifier=\'string\',
              SkipFinalClusterSnapshot=True|False,
              FinalClusterSnapshotIdentifier=\'string\'
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          The identifier of the cluster to be deleted.
        
          Constraints:
        
          * Must contain lowercase characters. 
           
          * Must contain from 1 to 63 alphanumeric characters or hyphens. 
           
          * First character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
        :type SkipFinalClusterSnapshot: boolean
        :param SkipFinalClusterSnapshot: 
        
          Determines whether a final snapshot of the cluster is created before Amazon Redshift deletes the cluster. If ``true`` , a final cluster snapshot is not created. If ``false`` , a final cluster snapshot is created before the cluster is deleted. 
        
          .. note::
        
            The *FinalClusterSnapshotIdentifier* parameter must be specified if *SkipFinalClusterSnapshot* is ``false`` .
        
          Default: ``false``  
        
        :type FinalClusterSnapshotIdentifier: string
        :param FinalClusterSnapshotIdentifier: 
        
          The identifier of the final snapshot that is to be created immediately before deleting the cluster. If this parameter is provided, *SkipFinalClusterSnapshot* must be ``false`` . 
        
          Constraints:
        
          * Must be 1 to 255 alphanumeric characters. 
           
          * First character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
                    \'ClusterIdentifier\': \'string\',
                    \'NodeType\': \'string\',
                    \'ClusterStatus\': \'string\',
                    \'ModifyStatus\': \'string\',
                    \'MasterUsername\': \'string\',
                    \'DBName\': \'string\',
                    \'Endpoint\': {
                        \'Address\': \'string\',
                        \'Port\': 123
                    },
                    \'ClusterCreateTime\': datetime(2015, 1, 1),
                    \'AutomatedSnapshotRetentionPeriod\': 123,
                    \'ClusterSecurityGroups\': [
                        {
                            \'ClusterSecurityGroupName\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'VpcSecurityGroups\': [
                        {
                            \'VpcSecurityGroupId\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'ClusterParameterGroups\': [
                        {
                            \'ParameterGroupName\': \'string\',
                            \'ParameterApplyStatus\': \'string\',
                            \'ClusterParameterStatusList\': [
                                {
                                    \'ParameterName\': \'string\',
                                    \'ParameterApplyStatus\': \'string\',
                                    \'ParameterApplyErrorDescription\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'ClusterSubnetGroupName\': \'string\',
                    \'VpcId\': \'string\',
                    \'AvailabilityZone\': \'string\',
                    \'PreferredMaintenanceWindow\': \'string\',
                    \'PendingModifiedValues\': {
                        \'MasterUserPassword\': \'string\',
                        \'NodeType\': \'string\',
                        \'NumberOfNodes\': 123,
                        \'ClusterType\': \'string\',
                        \'ClusterVersion\': \'string\',
                        \'AutomatedSnapshotRetentionPeriod\': 123,
                        \'ClusterIdentifier\': \'string\',
                        \'PubliclyAccessible\': True|False,
                        \'EnhancedVpcRouting\': True|False,
                        \'MaintenanceTrackName\': \'string\',
                        \'EncryptionType\': \'string\'
                    },
                    \'ClusterVersion\': \'string\',
                    \'AllowVersionUpgrade\': True|False,
                    \'NumberOfNodes\': 123,
                    \'PubliclyAccessible\': True|False,
                    \'Encrypted\': True|False,
                    \'RestoreStatus\': {
                        \'Status\': \'string\',
                        \'CurrentRestoreRateInMegaBytesPerSecond\': 123.0,
                        \'SnapshotSizeInMegaBytes\': 123,
                        \'ProgressInMegaBytes\': 123,
                        \'ElapsedTimeInSeconds\': 123,
                        \'EstimatedTimeToCompletionInSeconds\': 123
                    },
                    \'HsmStatus\': {
                        \'HsmClientCertificateIdentifier\': \'string\',
                        \'HsmConfigurationIdentifier\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterSnapshotCopyStatus\': {
                        \'DestinationRegion\': \'string\',
                        \'RetentionPeriod\': 123,
                        \'SnapshotCopyGrantName\': \'string\'
                    },
                    \'ClusterPublicKey\': \'string\',
                    \'ClusterNodes\': [
                        {
                            \'NodeRole\': \'string\',
                            \'PrivateIPAddress\': \'string\',
                            \'PublicIPAddress\': \'string\'
                        },
                    ],
                    \'ElasticIpStatus\': {
                        \'ElasticIp\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterRevisionNumber\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'KmsKeyId\': \'string\',
                    \'EnhancedVpcRouting\': True|False,
                    \'IamRoles\': [
                        {
                            \'IamRoleArn\': \'string\',
                            \'ApplyStatus\': \'string\'
                        },
                    ],
                    \'PendingActions\': [
                        \'string\',
                    ],
                    \'MaintenanceTrackName\': \'string\',
                    \'ElasticResizeNumberOfNodeOptions\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              Describes a cluster.
        
              - **ClusterIdentifier** *(string) --* 
        
                The unique identifier of the cluster.
        
              - **NodeType** *(string) --* 
        
                The node type for the nodes in the cluster.
        
              - **ClusterStatus** *(string) --* 
        
                The current state of the cluster. Possible values are the following:
        
                * ``available``   
                 
                * ``creating``   
                 
                * ``deleting``   
                 
                * ``final-snapshot``   
                 
                * ``hardware-failure``   
                 
                * ``incompatible-hsm``   
                 
                * ``incompatible-network``   
                 
                * ``incompatible-parameters``   
                 
                * ``incompatible-restore``   
                 
                * ``modifying``   
                 
                * ``rebooting``   
                 
                * ``renaming``   
                 
                * ``resizing``   
                 
                * ``rotating-keys``   
                 
                * ``storage-full``   
                 
                * ``updating-hsm``   
                 
              - **ModifyStatus** *(string) --* 
        
                The status of a modify operation, if any, initiated for the cluster.
        
              - **MasterUsername** *(string) --* 
        
                The master user name for the cluster. This name is used to connect to the database that is specified in the **DBName** parameter. 
        
              - **DBName** *(string) --* 
        
                The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named ``dev`` dev was created by default. 
        
              - **Endpoint** *(dict) --* 
        
                The connection endpoint.
        
                - **Address** *(string) --* 
        
                  The DNS address of the Cluster.
        
                - **Port** *(integer) --* 
        
                  The port that the database engine is listening on.
        
              - **ClusterCreateTime** *(datetime) --* 
        
                The date and time that the cluster was created.
        
              - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                The number of days that automatic cluster snapshots are retained.
        
              - **ClusterSecurityGroups** *(list) --* 
        
                A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ``ClusterSecurityGroup.Name`` and ``ClusterSecurityGroup.Status`` subelements. 
        
                Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the **VpcSecurityGroups** parameter. 
        
                - *(dict) --* 
        
                  Describes a cluster security group.
        
                  - **ClusterSecurityGroupName** *(string) --* 
        
                    The name of the cluster security group.
        
                  - **Status** *(string) --* 
        
                    The status of the cluster security group.
        
              - **VpcSecurityGroups** *(list) --* 
        
                A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.
        
                - *(dict) --* 
        
                  Describes the members of a VPC security group.
        
                  - **VpcSecurityGroupId** *(string) --* 
        
                    The identifier of the VPC security group.
        
                  - **Status** *(string) --* 
        
                    The status of the VPC security group.
        
              - **ClusterParameterGroups** *(list) --* 
        
                The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.
        
                - *(dict) --* 
        
                  Describes the status of a parameter group.
        
                  - **ParameterGroupName** *(string) --* 
        
                    The name of the cluster parameter group.
        
                  - **ParameterApplyStatus** *(string) --* 
        
                    The status of parameter updates.
        
                  - **ClusterParameterStatusList** *(list) --* 
        
                    The list of parameter statuses.
        
                    For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
                    - *(dict) --* 
        
                      Describes the status of a parameter group.
        
                      - **ParameterName** *(string) --* 
        
                        The name of the parameter.
        
                      - **ParameterApplyStatus** *(string) --* 
        
                        The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
        
                        The following are possible statuses and descriptions.
        
                        * ``in-sync`` : The parameter value is in sync with the database. 
                         
                        * ``pending-reboot`` : The parameter value will be applied after the cluster reboots. 
                         
                        * ``applying`` : The parameter value is being applied to the database. 
                         
                        * ``invalid-parameter`` : Cannot apply the parameter value because it has an invalid value or syntax. 
                         
                        * ``apply-deferred`` : The parameter contains static property changes. The changes are deferred until the cluster reboots. 
                         
                        * ``apply-error`` : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots. 
                         
                        * ``unknown-error`` : Cannot apply the parameter change right now. The change will be applied after the cluster reboots. 
                         
                      - **ParameterApplyErrorDescription** *(string) --* 
        
                        The error that prevented the parameter from being applied to the database.
        
              - **ClusterSubnetGroupName** *(string) --* 
        
                The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.
        
              - **VpcId** *(string) --* 
        
                The identifier of the VPC the cluster is in, if the cluster is in a VPC.
        
              - **AvailabilityZone** *(string) --* 
        
                The name of the Availability Zone in which the cluster is located.
        
              - **PreferredMaintenanceWindow** *(string) --* 
        
                The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.
        
              - **PendingModifiedValues** *(dict) --* 
        
                A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.
        
                - **MasterUserPassword** *(string) --* 
        
                  The pending or in-progress change of the master user password for the cluster.
        
                - **NodeType** *(string) --* 
        
                  The pending or in-progress change of the cluster\'s node type.
        
                - **NumberOfNodes** *(integer) --* 
        
                  The pending or in-progress change of the number of nodes in the cluster.
        
                - **ClusterType** *(string) --* 
        
                  The pending or in-progress change of the cluster type.
        
                - **ClusterVersion** *(string) --* 
        
                  The pending or in-progress change of the service version.
        
                - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                  The pending or in-progress change of the automated snapshot retention period.
        
                - **ClusterIdentifier** *(string) --* 
        
                  The pending or in-progress change of the new identifier for the cluster.
        
                - **PubliclyAccessible** *(boolean) --* 
        
                  The pending or in-progress change of the ability to connect to the cluster from the public network.
        
                - **EnhancedVpcRouting** *(boolean) --* 
        
                  An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                  If this option is ``true`` , enhanced VPC routing is enabled. 
        
                  Default: false
        
                - **MaintenanceTrackName** *(string) --* 
        
                  The name of the maintenance track that the cluster will change to during the next maintenance window.
        
                - **EncryptionType** *(string) --* 
        
                  The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy. 
        
              - **ClusterVersion** *(string) --* 
        
                The version ID of the Amazon Redshift engine that is running on the cluster.
        
              - **AllowVersionUpgrade** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window. 
        
              - **NumberOfNodes** *(integer) --* 
        
                The number of compute nodes in the cluster.
        
              - **PubliclyAccessible** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that the cluster can be accessed from a public network.
        
              - **Encrypted** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that data in the cluster is encrypted at rest.
        
              - **RestoreStatus** *(dict) --* 
        
                A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.
        
                - **Status** *(string) --* 
        
                  The status of the restore action. Returns starting, restoring, completed, or failed.
        
                - **CurrentRestoreRateInMegaBytesPerSecond** *(float) --* 
        
                  The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.
        
                - **SnapshotSizeInMegaBytes** *(integer) --* 
        
                  The size of the set of snapshot data used to restore the cluster.
        
                - **ProgressInMegaBytes** *(integer) --* 
        
                  The number of megabytes that have been transferred from snapshot storage.
        
                - **ElapsedTimeInSeconds** *(integer) --* 
        
                  The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.
        
                - **EstimatedTimeToCompletionInSeconds** *(integer) --* 
        
                  The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore.
        
              - **HsmStatus** *(dict) --* 
        
                A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
        
                Values: active, applying
        
                - **HsmClientCertificateIdentifier** *(string) --* 
        
                  Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        
                - **HsmConfigurationIdentifier** *(string) --* 
        
                  Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        
                - **Status** *(string) --* 
        
                  Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
        
                  Values: active, applying
        
              - **ClusterSnapshotCopyStatus** *(dict) --* 
        
                A value that returns the destination region and retention period that are configured for cross-region snapshot copy.
        
                - **DestinationRegion** *(string) --* 
        
                  The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
        
                - **RetentionPeriod** *(integer) --* 
        
                  The number of days that automated snapshots are retained in the destination region after they are copied from a source region.
        
                - **SnapshotCopyGrantName** *(string) --* 
        
                  The name of the snapshot copy grant.
        
              - **ClusterPublicKey** *(string) --* 
        
                The public key for the cluster.
        
              - **ClusterNodes** *(list) --* 
        
                The nodes in the cluster.
        
                - *(dict) --* 
        
                  The identifier of a node in a cluster.
        
                  - **NodeRole** *(string) --* 
        
                    Whether the node is a leader node or a compute node.
        
                  - **PrivateIPAddress** *(string) --* 
        
                    The private IP address of a node within a cluster.
        
                  - **PublicIPAddress** *(string) --* 
        
                    The public IP address of a node within a cluster.
        
              - **ElasticIpStatus** *(dict) --* 
        
                The status of the elastic IP (EIP) address.
        
                - **ElasticIp** *(string) --* 
        
                  The elastic IP (EIP) address for the cluster.
        
                - **Status** *(string) --* 
        
                  The status of the elastic IP (EIP) address.
        
              - **ClusterRevisionNumber** *(string) --* 
        
                The specific revision number of the database in the cluster.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.
        
              - **EnhancedVpcRouting** *(boolean) --* 
        
                An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                If this option is ``true`` , enhanced VPC routing is enabled. 
        
                Default: false
        
              - **IamRoles** *(list) --* 
        
                A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.
        
                - *(dict) --* 
        
                  An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.
        
                  - **IamRoleArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the IAM role, for example, ``arn:aws:iam::123456789012:role/RedshiftCopyUnload`` . 
        
                  - **ApplyStatus** *(string) --* 
        
                    A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
        
                    The following are possible statuses and descriptions.
        
                    * ``in-sync`` : The role is available for use by the cluster. 
                     
                    * ``adding`` : The role is in the process of being associated with the cluster. 
                     
                    * ``removing`` : The role is in the process of being disassociated with the cluster. 
                     
              - **PendingActions** *(list) --* 
        
                Cluster operations that are waiting to be started.
        
                - *(string) --* 
            
              - **MaintenanceTrackName** *(string) --* 
        
                The name of the maintenance track for the cluster.
        
              - **ElasticResizeNumberOfNodeOptions** *(string) --* 
        
                Indicates the number of nodes the cluster can be resized to with the elastic resize method. 
        
        """
        pass

    def delete_cluster_parameter_group(self, ParameterGroupName: str) -> NoReturn:
        """
        
        .. note::
        
          You cannot delete a parameter group if it is associated with a cluster.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DeleteClusterParameterGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_cluster_parameter_group(
              ParameterGroupName=\'string\'
          )
        :type ParameterGroupName: string
        :param ParameterGroupName: **[REQUIRED]** 
        
          The name of the parameter group to be deleted.
        
          Constraints:
        
          * Must be the name of an existing cluster parameter group. 
           
          * Cannot delete a default cluster parameter group. 
           
        :returns: None
        """
        pass

    def delete_cluster_security_group(self, ClusterSecurityGroupName: str) -> NoReturn:
        """
        
        .. note::
        
          You cannot delete a security group that is associated with any clusters. You cannot delete the default security group.
        
        For information about managing security groups, go to `Amazon Redshift Cluster Security Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DeleteClusterSecurityGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_cluster_security_group(
              ClusterSecurityGroupName=\'string\'
          )
        :type ClusterSecurityGroupName: string
        :param ClusterSecurityGroupName: **[REQUIRED]** 
        
          The name of the cluster security group to be deleted.
        
        :returns: None
        """
        pass

    def delete_cluster_snapshot(self, SnapshotIdentifier: str, SnapshotClusterIdentifier: str = None) -> Dict:
        """
        
        Unlike automated snapshots, manual snapshots are retained even after you delete your cluster. Amazon Redshift does not delete your manual snapshots. You must delete manual snapshot explicitly to avoid getting charged. If other accounts are authorized to access the snapshot, you must revoke all of the authorizations before you can delete the snapshot.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DeleteClusterSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_cluster_snapshot(
              SnapshotIdentifier=\'string\',
              SnapshotClusterIdentifier=\'string\'
          )
        :type SnapshotIdentifier: string
        :param SnapshotIdentifier: **[REQUIRED]** 
        
          The unique identifier of the manual snapshot to be deleted.
        
          Constraints: Must be the name of an existing snapshot that is in the ``available`` state.
        
        :type SnapshotClusterIdentifier: string
        :param SnapshotClusterIdentifier: 
        
          The unique identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
        
          Constraints: Must be the name of valid cluster.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Snapshot\': {
                    \'SnapshotIdentifier\': \'string\',
                    \'ClusterIdentifier\': \'string\',
                    \'SnapshotCreateTime\': datetime(2015, 1, 1),
                    \'Status\': \'string\',
                    \'Port\': 123,
                    \'AvailabilityZone\': \'string\',
                    \'ClusterCreateTime\': datetime(2015, 1, 1),
                    \'MasterUsername\': \'string\',
                    \'ClusterVersion\': \'string\',
                    \'SnapshotType\': \'string\',
                    \'NodeType\': \'string\',
                    \'NumberOfNodes\': 123,
                    \'DBName\': \'string\',
                    \'VpcId\': \'string\',
                    \'Encrypted\': True|False,
                    \'KmsKeyId\': \'string\',
                    \'EncryptedWithHSM\': True|False,
                    \'AccountsWithRestoreAccess\': [
                        {
                            \'AccountId\': \'string\',
                            \'AccountAlias\': \'string\'
                        },
                    ],
                    \'OwnerAccount\': \'string\',
                    \'TotalBackupSizeInMegaBytes\': 123.0,
                    \'ActualIncrementalBackupSizeInMegaBytes\': 123.0,
                    \'BackupProgressInMegaBytes\': 123.0,
                    \'CurrentBackupRateInMegaBytesPerSecond\': 123.0,
                    \'EstimatedSecondsToCompletion\': 123,
                    \'ElapsedTimeInSeconds\': 123,
                    \'SourceRegion\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'RestorableNodeTypes\': [
                        \'string\',
                    ],
                    \'EnhancedVpcRouting\': True|False,
                    \'MaintenanceTrackName\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Snapshot** *(dict) --* 
        
              Describes a snapshot.
        
              - **SnapshotIdentifier** *(string) --* 
        
                The snapshot identifier that is provided in the request.
        
              - **ClusterIdentifier** *(string) --* 
        
                The identifier of the cluster for which the snapshot was taken.
        
              - **SnapshotCreateTime** *(datetime) --* 
        
                The time (UTC) when Amazon Redshift began the snapshot. A snapshot contains a copy of the cluster data as of this exact time.
        
              - **Status** *(string) --* 
        
                The snapshot status. The value of the status depends on the API operation used. 
        
                *  CreateClusterSnapshot and  CopyClusterSnapshot returns status as \"creating\".  
                 
                *  DescribeClusterSnapshots returns status as \"creating\", \"available\", \"final snapshot\", or \"failed\". 
                 
                *  DeleteClusterSnapshot returns status as \"deleted\". 
                 
              - **Port** *(integer) --* 
        
                The port that the cluster is listening on.
        
              - **AvailabilityZone** *(string) --* 
        
                The Availability Zone in which the cluster was created.
        
              - **ClusterCreateTime** *(datetime) --* 
        
                The time (UTC) when the cluster was originally created.
        
              - **MasterUsername** *(string) --* 
        
                The master user name for the cluster.
        
              - **ClusterVersion** *(string) --* 
        
                The version ID of the Amazon Redshift engine that is running on the cluster.
        
              - **SnapshotType** *(string) --* 
        
                The snapshot type. Snapshots created using  CreateClusterSnapshot and  CopyClusterSnapshot will be of type \"manual\". 
        
              - **NodeType** *(string) --* 
        
                The node type of the nodes in the cluster.
        
              - **NumberOfNodes** *(integer) --* 
        
                The number of nodes in the cluster.
        
              - **DBName** *(string) --* 
        
                The name of the database that was created when the cluster was created.
        
              - **VpcId** *(string) --* 
        
                The VPC identifier of the cluster if the snapshot is from a cluster in a VPC. Otherwise, this field is not in the output.
        
              - **Encrypted** *(boolean) --* 
        
                If ``true`` , the data in the snapshot is encrypted at rest.
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.
        
              - **EncryptedWithHSM** *(boolean) --* 
        
                A boolean that indicates whether the snapshot data is encrypted using the HSM keys of the source cluster. ``true`` indicates that the data is encrypted using HSM keys.
        
              - **AccountsWithRestoreAccess** *(list) --* 
        
                A list of the AWS customer accounts authorized to restore the snapshot. Returns ``null`` if no accounts are authorized. Visible only to the snapshot owner. 
        
                - *(dict) --* 
        
                  Describes an AWS customer account authorized to restore a snapshot.
        
                  - **AccountId** *(string) --* 
        
                    The identifier of an AWS customer account authorized to restore a snapshot.
        
                  - **AccountAlias** *(string) --* 
        
                    The identifier of an AWS support account authorized to restore a snapshot. For AWS support, the identifier is ``amazon-redshift-support`` . 
        
              - **OwnerAccount** *(string) --* 
        
                For manual snapshots, the AWS customer account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.
        
              - **TotalBackupSizeInMegaBytes** *(float) --* 
        
                The size of the complete set of backup data that would be used to restore the cluster.
        
              - **ActualIncrementalBackupSizeInMegaBytes** *(float) --* 
        
                The size of the incremental backup.
        
              - **BackupProgressInMegaBytes** *(float) --* 
        
                The number of megabytes that have been transferred to the snapshot backup.
        
              - **CurrentBackupRateInMegaBytesPerSecond** *(float) --* 
        
                The number of megabytes per second being transferred to the snapshot backup. Returns ``0`` for a completed backup. 
        
              - **EstimatedSecondsToCompletion** *(integer) --* 
        
                The estimate of the time remaining before the snapshot backup will complete. Returns ``0`` for a completed backup. 
        
              - **ElapsedTimeInSeconds** *(integer) --* 
        
                The amount of time an in-progress snapshot backup has been running, or the amount of time it took a completed backup to finish.
        
              - **SourceRegion** *(string) --* 
        
                The source region from which the snapshot was copied.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster snapshot.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
              - **RestorableNodeTypes** *(list) --* 
        
                The list of node types that this cluster snapshot is able to restore into.
        
                - *(string) --* 
            
              - **EnhancedVpcRouting** *(boolean) --* 
        
                An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                If this option is ``true`` , enhanced VPC routing is enabled. 
        
                Default: false
        
              - **MaintenanceTrackName** *(string) --* 
        
                The name of the maintenance track for the snapshot.
        
        """
        pass

    def delete_cluster_subnet_group(self, ClusterSubnetGroupName: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DeleteClusterSubnetGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_cluster_subnet_group(
              ClusterSubnetGroupName=\'string\'
          )
        :type ClusterSubnetGroupName: string
        :param ClusterSubnetGroupName: **[REQUIRED]** 
        
          The name of the cluster subnet group name to be deleted.
        
        :returns: None
        """
        pass

    def delete_event_subscription(self, SubscriptionName: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DeleteEventSubscription>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_event_subscription(
              SubscriptionName=\'string\'
          )
        :type SubscriptionName: string
        :param SubscriptionName: **[REQUIRED]** 
        
          The name of the Amazon Redshift event notification subscription to be deleted.
        
        :returns: None
        """
        pass

    def delete_hsm_client_certificate(self, HsmClientCertificateIdentifier: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DeleteHsmClientCertificate>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_hsm_client_certificate(
              HsmClientCertificateIdentifier=\'string\'
          )
        :type HsmClientCertificateIdentifier: string
        :param HsmClientCertificateIdentifier: **[REQUIRED]** 
        
          The identifier of the HSM client certificate to be deleted.
        
        :returns: None
        """
        pass

    def delete_hsm_configuration(self, HsmConfigurationIdentifier: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DeleteHsmConfiguration>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_hsm_configuration(
              HsmConfigurationIdentifier=\'string\'
          )
        :type HsmConfigurationIdentifier: string
        :param HsmConfigurationIdentifier: **[REQUIRED]** 
        
          The identifier of the Amazon Redshift HSM configuration to be deleted.
        
        :returns: None
        """
        pass

    def delete_snapshot_copy_grant(self, SnapshotCopyGrantName: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DeleteSnapshotCopyGrant>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_snapshot_copy_grant(
              SnapshotCopyGrantName=\'string\'
          )
        :type SnapshotCopyGrantName: string
        :param SnapshotCopyGrantName: **[REQUIRED]** 
        
          The name of the snapshot copy grant to delete.
        
        :returns: None
        """
        pass

    def delete_tags(self, ResourceName: str, TagKeys: List) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DeleteTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_tags(
              ResourceName=\'string\',
              TagKeys=[
                  \'string\',
              ]
          )
        :type ResourceName: string
        :param ResourceName: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) from which you want to remove the tag or tags. For example, ``arn:aws:redshift:us-east-1:123456789:cluster:t1`` . 
        
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** 
        
          The tag key that you want to delete.
        
          - *(string) --* 
        
        :returns: None
        """
        pass

    def describe_cluster_db_revisions(self, ClusterIdentifier: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusterDbRevisions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_cluster_db_revisions(
              ClusterIdentifier=\'string\',
              MaxRecords=123,
              Marker=\'string\'
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: 
        
          A unique identifier for a cluster whose ``ClusterDbRevisions`` you are requesting. This parameter is case sensitive. All clusters defined for an account are returned by default.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in the ``marker`` field of the response. You can retrieve the next set of response records by providing the returned ``marker`` value in the ``marker`` parameter and retrying the request. 
        
          Default: 100
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point for returning a set of response records. When the results of a ``DescribeClusterDbRevisions`` request exceed the value specified in ``MaxRecords`` , Amazon Redshift returns a value in the ``marker`` field of the response. You can retrieve the next set of response records by providing the returned ``marker`` value in the ``marker`` parameter and retrying the request. 
        
          Constraints: You can specify either the ``ClusterIdentifier`` parameter, or the ``marker`` parameter, but not both.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'ClusterDbRevisions\': [
                    {
                        \'ClusterIdentifier\': \'string\',
                        \'CurrentDatabaseRevision\': \'string\',
                        \'DatabaseRevisionReleaseDate\': datetime(2015, 1, 1),
                        \'RevisionTargets\': [
                            {
                                \'DatabaseRevision\': \'string\',
                                \'Description\': \'string\',
                                \'DatabaseRevisionReleaseDate\': datetime(2015, 1, 1)
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Marker** *(string) --* 
        
              A string representing the starting point for the next set of revisions. If a value is returned in a response, you can retrieve the next set of revisions by providing the value in the ``marker`` parameter and retrying the command. If the ``marker`` field is empty, all revisions have already been returned.
        
            - **ClusterDbRevisions** *(list) --* 
        
              A list of revisions.
        
              - *(dict) --* 
        
                Describes a ``ClusterDbRevision`` .
        
                - **ClusterIdentifier** *(string) --* 
        
                  The unique identifier of the cluster.
        
                - **CurrentDatabaseRevision** *(string) --* 
        
                  A string representing the current cluster version.
        
                - **DatabaseRevisionReleaseDate** *(datetime) --* 
        
                  The date on which the database revision was released.
        
                - **RevisionTargets** *(list) --* 
        
                  A list of ``RevisionTarget`` objects, where each object describes the database revision that a cluster can be updated to.
        
                  - *(dict) --* 
        
                    Describes a ``RevisionTarget`` .
        
                    - **DatabaseRevision** *(string) --* 
        
                      A unique string that identifies the version to update the cluster to. You can use this value in  ModifyClusterDbRevision .
        
                    - **Description** *(string) --* 
        
                      A string that describes the changes and features that will be applied to the cluster when it is updated to the corresponding  ClusterDbRevision .
        
                    - **DatabaseRevisionReleaseDate** *(datetime) --* 
        
                      The date on which the database revision was released.
        
        """
        pass

    def describe_cluster_parameter_groups(self, ParameterGroupName: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None) -> Dict:
        """
        
        For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        If you specify both tag keys and tag values in the same request, Amazon Redshift returns all parameter groups that match any combination of the specified keys and values. For example, if you have ``owner`` and ``environment`` for tag keys, and ``admin`` and ``test`` for tag values, all parameter groups that have any combination of those values are returned.
        
        If both tag keys and values are omitted from the request, parameter groups are returned regardless of whether they have tag keys or values associated with them.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusterParameterGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_cluster_parameter_groups(
              ParameterGroupName=\'string\',
              MaxRecords=123,
              Marker=\'string\',
              TagKeys=[
                  \'string\',
              ],
              TagValues=[
                  \'string\',
              ]
          )
        :type ParameterGroupName: string
        :param ParameterGroupName: 
        
          The name of a specific parameter group for which to return details. By default, details about all parameter groups and the default parameter group are returned.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeClusterParameterGroups request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
        :type TagKeys: list
        :param TagKeys: 
        
          A tag key or keys for which you want to return all matching cluster parameter groups that are associated with the specified key or keys. For example, suppose that you have parameter groups that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the parameter groups that have either or both of these tag keys associated with them.
        
          - *(string) --* 
        
        :type TagValues: list
        :param TagValues: 
        
          A tag value or values for which you want to return all matching cluster parameter groups that are associated with the specified tag value or values. For example, suppose that you have parameter groups that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the parameter groups that have either or both of these tag values associated with them.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'ParameterGroups\': [
                    {
                        \'ParameterGroupName\': \'string\',
                        \'ParameterGroupFamily\': \'string\',
                        \'Description\': \'string\',
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output from the  DescribeClusterParameterGroups action. 
        
            - **Marker** *(string) --* 
        
              A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the ``Marker`` parameter and retrying the command. If the ``Marker`` field is empty, all response records have been retrieved for the request. 
        
            - **ParameterGroups** *(list) --* 
        
              A list of  ClusterParameterGroup instances. Each instance describes one cluster parameter group. 
        
              - *(dict) --* 
        
                Describes a parameter group.
        
                - **ParameterGroupName** *(string) --* 
        
                  The name of the cluster parameter group.
        
                - **ParameterGroupFamily** *(string) --* 
        
                  The name of the cluster parameter group family that this cluster parameter group is compatible with.
        
                - **Description** *(string) --* 
        
                  The description of the parameter group.
        
                - **Tags** *(list) --* 
        
                  The list of tags for the cluster parameter group.
        
                  - *(dict) --* 
        
                    A tag consisting of a name/value pair for a resource.
        
                    - **Key** *(string) --* 
        
                      The key, or name, for the resource tag.
        
                    - **Value** *(string) --* 
        
                      The value for the resource tag.
        
        """
        pass

    def describe_cluster_parameters(self, ParameterGroupName: str, Source: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        You can specify *source* filter to retrieve parameters of only specific type. For example, to retrieve parameters that were modified by a user action such as from  ModifyClusterParameterGroup , you can specify *source* equal to *user* .
        
        For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusterParameters>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_cluster_parameters(
              ParameterGroupName=\'string\',
              Source=\'string\',
              MaxRecords=123,
              Marker=\'string\'
          )
        :type ParameterGroupName: string
        :param ParameterGroupName: **[REQUIRED]** 
        
          The name of a cluster parameter group for which to return details.
        
        :type Source: string
        :param Source: 
        
          The parameter types to return. Specify ``user`` to show parameters that are different form the default. Similarly, specify ``engine-default`` to show parameters that are the same as the default parameter group. 
        
          Default: All parameter types returned.
        
          Valid Values: ``user`` | ``engine-default``  
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeClusterParameters request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Parameters\': [
                    {
                        \'ParameterName\': \'string\',
                        \'ParameterValue\': \'string\',
                        \'Description\': \'string\',
                        \'Source\': \'string\',
                        \'DataType\': \'string\',
                        \'AllowedValues\': \'string\',
                        \'ApplyType\': \'static\'|\'dynamic\',
                        \'IsModifiable\': True|False,
                        \'MinimumEngineVersion\': \'string\'
                    },
                ],
                \'Marker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output from the  DescribeClusterParameters action. 
        
            - **Parameters** *(list) --* 
        
              A list of  Parameter instances. Each instance lists the parameters of one cluster parameter group. 
        
              - *(dict) --* 
        
                Describes a parameter in a cluster parameter group.
        
                - **ParameterName** *(string) --* 
        
                  The name of the parameter.
        
                - **ParameterValue** *(string) --* 
        
                  The value of the parameter.
        
                - **Description** *(string) --* 
        
                  A description of the parameter.
        
                - **Source** *(string) --* 
        
                  The source of the parameter value, such as \"engine-default\" or \"user\".
        
                - **DataType** *(string) --* 
        
                  The data type of the parameter.
        
                - **AllowedValues** *(string) --* 
        
                  The valid range of values for the parameter.
        
                - **ApplyType** *(string) --* 
        
                  Specifies how to apply the WLM configuration parameter. Some properties can be applied dynamically, while other properties require that any associated clusters be rebooted for the configuration changes to be applied. For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
                - **IsModifiable** *(boolean) --* 
        
                  If ``true`` , the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed. 
        
                - **MinimumEngineVersion** *(string) --* 
        
                  The earliest engine version to which the parameter can apply.
        
            - **Marker** *(string) --* 
        
              A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the ``Marker`` parameter and retrying the command. If the ``Marker`` field is empty, all response records have been retrieved for the request. 
        
        """
        pass

    def describe_cluster_security_groups(self, ClusterSecurityGroupName: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None) -> Dict:
        """
        
        For information about managing security groups, go to `Amazon Redshift Cluster Security Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        If you specify both tag keys and tag values in the same request, Amazon Redshift returns all security groups that match any combination of the specified keys and values. For example, if you have ``owner`` and ``environment`` for tag keys, and ``admin`` and ``test`` for tag values, all security groups that have any combination of those values are returned.
        
        If both tag keys and values are omitted from the request, security groups are returned regardless of whether they have tag keys or values associated with them.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusterSecurityGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_cluster_security_groups(
              ClusterSecurityGroupName=\'string\',
              MaxRecords=123,
              Marker=\'string\',
              TagKeys=[
                  \'string\',
              ],
              TagValues=[
                  \'string\',
              ]
          )
        :type ClusterSecurityGroupName: string
        :param ClusterSecurityGroupName: 
        
          The name of a cluster security group for which you are requesting details. You can specify either the **Marker** parameter or a **ClusterSecurityGroupName** parameter, but not both. 
        
          Example: ``securitygroup1``  
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeClusterSecurityGroups request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
          Constraints: You can specify either the **ClusterSecurityGroupName** parameter or the **Marker** parameter, but not both. 
        
        :type TagKeys: list
        :param TagKeys: 
        
          A tag key or keys for which you want to return all matching cluster security groups that are associated with the specified key or keys. For example, suppose that you have security groups that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the security groups that have either or both of these tag keys associated with them.
        
          - *(string) --* 
        
        :type TagValues: list
        :param TagValues: 
        
          A tag value or values for which you want to return all matching cluster security groups that are associated with the specified tag value or values. For example, suppose that you have security groups that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the security groups that have either or both of these tag values associated with them.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'ClusterSecurityGroups\': [
                    {
                        \'ClusterSecurityGroupName\': \'string\',
                        \'Description\': \'string\',
                        \'EC2SecurityGroups\': [
                            {
                                \'Status\': \'string\',
                                \'EC2SecurityGroupName\': \'string\',
                                \'EC2SecurityGroupOwnerId\': \'string\',
                                \'Tags\': [
                                    {
                                        \'Key\': \'string\',
                                        \'Value\': \'string\'
                                    },
                                ]
                            },
                        ],
                        \'IPRanges\': [
                            {
                                \'Status\': \'string\',
                                \'CIDRIP\': \'string\',
                                \'Tags\': [
                                    {
                                        \'Key\': \'string\',
                                        \'Value\': \'string\'
                                    },
                                ]
                            },
                        ],
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the ``Marker`` parameter and retrying the command. If the ``Marker`` field is empty, all response records have been retrieved for the request. 
        
            - **ClusterSecurityGroups** *(list) --* 
        
              A list of  ClusterSecurityGroup instances. 
        
              - *(dict) --* 
        
                Describes a security group.
        
                - **ClusterSecurityGroupName** *(string) --* 
        
                  The name of the cluster security group to which the operation was applied.
        
                - **Description** *(string) --* 
        
                  A description of the security group.
        
                - **EC2SecurityGroups** *(list) --* 
        
                  A list of EC2 security groups that are permitted to access clusters associated with this cluster security group.
        
                  - *(dict) --* 
        
                    Describes an Amazon EC2 security group.
        
                    - **Status** *(string) --* 
        
                      The status of the EC2 security group.
        
                    - **EC2SecurityGroupName** *(string) --* 
        
                      The name of the EC2 Security Group.
        
                    - **EC2SecurityGroupOwnerId** *(string) --* 
        
                      The AWS ID of the owner of the EC2 security group specified in the ``EC2SecurityGroupName`` field. 
        
                    - **Tags** *(list) --* 
        
                      The list of tags for the EC2 security group.
        
                      - *(dict) --* 
        
                        A tag consisting of a name/value pair for a resource.
        
                        - **Key** *(string) --* 
        
                          The key, or name, for the resource tag.
        
                        - **Value** *(string) --* 
        
                          The value for the resource tag.
        
                - **IPRanges** *(list) --* 
        
                  A list of IP ranges (CIDR blocks) that are permitted to access clusters associated with this cluster security group.
        
                  - *(dict) --* 
        
                    Describes an IP range used in a security group.
        
                    - **Status** *(string) --* 
        
                      The status of the IP range, for example, \"authorized\".
        
                    - **CIDRIP** *(string) --* 
        
                      The IP range in Classless Inter-Domain Routing (CIDR) notation.
        
                    - **Tags** *(list) --* 
        
                      The list of tags for the IP range.
        
                      - *(dict) --* 
        
                        A tag consisting of a name/value pair for a resource.
        
                        - **Key** *(string) --* 
        
                          The key, or name, for the resource tag.
        
                        - **Value** *(string) --* 
        
                          The value for the resource tag.
        
                - **Tags** *(list) --* 
        
                  The list of tags for the cluster security group.
        
                  - *(dict) --* 
        
                    A tag consisting of a name/value pair for a resource.
        
                    - **Key** *(string) --* 
        
                      The key, or name, for the resource tag.
        
                    - **Value** *(string) --* 
        
                      The value for the resource tag.
        
        """
        pass

    def describe_cluster_snapshots(self, ClusterIdentifier: str = None, SnapshotIdentifier: str = None, SnapshotType: str = None, StartTime: datetime = None, EndTime: datetime = None, MaxRecords: int = None, Marker: str = None, OwnerAccount: str = None, TagKeys: List = None, TagValues: List = None, ClusterExists: bool = None) -> Dict:
        """
        
        If you specify both tag keys and tag values in the same request, Amazon Redshift returns all snapshots that match any combination of the specified keys and values. For example, if you have ``owner`` and ``environment`` for tag keys, and ``admin`` and ``test`` for tag values, all snapshots that have any combination of those values are returned. Only snapshots that you own are returned in the response; shared snapshots are not returned with the tag key and tag value request parameters.
        
        If both tag keys and values are omitted from the request, snapshots are returned regardless of whether they have tag keys or values associated with them.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusterSnapshots>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_cluster_snapshots(
              ClusterIdentifier=\'string\',
              SnapshotIdentifier=\'string\',
              SnapshotType=\'string\',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              MaxRecords=123,
              Marker=\'string\',
              OwnerAccount=\'string\',
              TagKeys=[
                  \'string\',
              ],
              TagValues=[
                  \'string\',
              ],
              ClusterExists=True|False
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: 
        
          The identifier of the cluster for which information about snapshots is requested.
        
        :type SnapshotIdentifier: string
        :param SnapshotIdentifier: 
        
          The snapshot identifier of the snapshot about which to return information.
        
        :type SnapshotType: string
        :param SnapshotType: 
        
          The type of snapshots for which you are requesting information. By default, snapshots of all types are returned.
        
          Valid Values: ``automated`` | ``manual``  
        
        :type StartTime: datetime
        :param StartTime: 
        
          A value that requests only snapshots created at or after the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the `ISO8601 Wikipedia page. <http://en.wikipedia.org/wiki/ISO_8601>`__  
        
          Example: ``2012-07-16T18:00:00Z``  
        
        :type EndTime: datetime
        :param EndTime: 
        
          A time value that requests only snapshots created at or before the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the `ISO8601 Wikipedia page. <http://en.wikipedia.org/wiki/ISO_8601>`__  
        
          Example: ``2012-07-16T18:00:00Z``  
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeClusterSnapshots request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
        :type OwnerAccount: string
        :param OwnerAccount: 
        
          The AWS customer account used to create or copy the snapshot. Use this field to filter the results to snapshots owned by a particular account. To describe snapshots you own, either specify your AWS customer account, or do not specify the parameter.
        
        :type TagKeys: list
        :param TagKeys: 
        
          A tag key or keys for which you want to return all matching cluster snapshots that are associated with the specified key or keys. For example, suppose that you have snapshots that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag keys associated with them.
        
          - *(string) --* 
        
        :type TagValues: list
        :param TagValues: 
        
          A tag value or values for which you want to return all matching cluster snapshots that are associated with the specified tag value or values. For example, suppose that you have snapshots that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag values associated with them.
        
          - *(string) --* 
        
        :type ClusterExists: boolean
        :param ClusterExists: 
        
          A value that indicates whether to return snapshots only for an existing cluster. Table-level restore can be performed only using a snapshot of an existing cluster, that is, a cluster that has not been deleted. If ``ClusterExists`` is set to ``true`` , ``ClusterIdentifier`` is required.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'Snapshots\': [
                    {
                        \'SnapshotIdentifier\': \'string\',
                        \'ClusterIdentifier\': \'string\',
                        \'SnapshotCreateTime\': datetime(2015, 1, 1),
                        \'Status\': \'string\',
                        \'Port\': 123,
                        \'AvailabilityZone\': \'string\',
                        \'ClusterCreateTime\': datetime(2015, 1, 1),
                        \'MasterUsername\': \'string\',
                        \'ClusterVersion\': \'string\',
                        \'SnapshotType\': \'string\',
                        \'NodeType\': \'string\',
                        \'NumberOfNodes\': 123,
                        \'DBName\': \'string\',
                        \'VpcId\': \'string\',
                        \'Encrypted\': True|False,
                        \'KmsKeyId\': \'string\',
                        \'EncryptedWithHSM\': True|False,
                        \'AccountsWithRestoreAccess\': [
                            {
                                \'AccountId\': \'string\',
                                \'AccountAlias\': \'string\'
                            },
                        ],
                        \'OwnerAccount\': \'string\',
                        \'TotalBackupSizeInMegaBytes\': 123.0,
                        \'ActualIncrementalBackupSizeInMegaBytes\': 123.0,
                        \'BackupProgressInMegaBytes\': 123.0,
                        \'CurrentBackupRateInMegaBytesPerSecond\': 123.0,
                        \'EstimatedSecondsToCompletion\': 123,
                        \'ElapsedTimeInSeconds\': 123,
                        \'SourceRegion\': \'string\',
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'RestorableNodeTypes\': [
                            \'string\',
                        ],
                        \'EnhancedVpcRouting\': True|False,
                        \'MaintenanceTrackName\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output from the  DescribeClusterSnapshots action. 
        
            - **Marker** *(string) --* 
        
              A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the ``Marker`` parameter and retrying the command. If the ``Marker`` field is empty, all response records have been retrieved for the request. 
        
            - **Snapshots** *(list) --* 
        
              A list of  Snapshot instances. 
        
              - *(dict) --* 
        
                Describes a snapshot.
        
                - **SnapshotIdentifier** *(string) --* 
        
                  The snapshot identifier that is provided in the request.
        
                - **ClusterIdentifier** *(string) --* 
        
                  The identifier of the cluster for which the snapshot was taken.
        
                - **SnapshotCreateTime** *(datetime) --* 
        
                  The time (UTC) when Amazon Redshift began the snapshot. A snapshot contains a copy of the cluster data as of this exact time.
        
                - **Status** *(string) --* 
        
                  The snapshot status. The value of the status depends on the API operation used. 
        
                  *  CreateClusterSnapshot and  CopyClusterSnapshot returns status as \"creating\".  
                   
                  *  DescribeClusterSnapshots returns status as \"creating\", \"available\", \"final snapshot\", or \"failed\". 
                   
                  *  DeleteClusterSnapshot returns status as \"deleted\". 
                   
                - **Port** *(integer) --* 
        
                  The port that the cluster is listening on.
        
                - **AvailabilityZone** *(string) --* 
        
                  The Availability Zone in which the cluster was created.
        
                - **ClusterCreateTime** *(datetime) --* 
        
                  The time (UTC) when the cluster was originally created.
        
                - **MasterUsername** *(string) --* 
        
                  The master user name for the cluster.
        
                - **ClusterVersion** *(string) --* 
        
                  The version ID of the Amazon Redshift engine that is running on the cluster.
        
                - **SnapshotType** *(string) --* 
        
                  The snapshot type. Snapshots created using  CreateClusterSnapshot and  CopyClusterSnapshot will be of type \"manual\". 
        
                - **NodeType** *(string) --* 
        
                  The node type of the nodes in the cluster.
        
                - **NumberOfNodes** *(integer) --* 
        
                  The number of nodes in the cluster.
        
                - **DBName** *(string) --* 
        
                  The name of the database that was created when the cluster was created.
        
                - **VpcId** *(string) --* 
        
                  The VPC identifier of the cluster if the snapshot is from a cluster in a VPC. Otherwise, this field is not in the output.
        
                - **Encrypted** *(boolean) --* 
        
                  If ``true`` , the data in the snapshot is encrypted at rest.
        
                - **KmsKeyId** *(string) --* 
        
                  The AWS Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.
        
                - **EncryptedWithHSM** *(boolean) --* 
        
                  A boolean that indicates whether the snapshot data is encrypted using the HSM keys of the source cluster. ``true`` indicates that the data is encrypted using HSM keys.
        
                - **AccountsWithRestoreAccess** *(list) --* 
        
                  A list of the AWS customer accounts authorized to restore the snapshot. Returns ``null`` if no accounts are authorized. Visible only to the snapshot owner. 
        
                  - *(dict) --* 
        
                    Describes an AWS customer account authorized to restore a snapshot.
        
                    - **AccountId** *(string) --* 
        
                      The identifier of an AWS customer account authorized to restore a snapshot.
        
                    - **AccountAlias** *(string) --* 
        
                      The identifier of an AWS support account authorized to restore a snapshot. For AWS support, the identifier is ``amazon-redshift-support`` . 
        
                - **OwnerAccount** *(string) --* 
        
                  For manual snapshots, the AWS customer account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.
        
                - **TotalBackupSizeInMegaBytes** *(float) --* 
        
                  The size of the complete set of backup data that would be used to restore the cluster.
        
                - **ActualIncrementalBackupSizeInMegaBytes** *(float) --* 
        
                  The size of the incremental backup.
        
                - **BackupProgressInMegaBytes** *(float) --* 
        
                  The number of megabytes that have been transferred to the snapshot backup.
        
                - **CurrentBackupRateInMegaBytesPerSecond** *(float) --* 
        
                  The number of megabytes per second being transferred to the snapshot backup. Returns ``0`` for a completed backup. 
        
                - **EstimatedSecondsToCompletion** *(integer) --* 
        
                  The estimate of the time remaining before the snapshot backup will complete. Returns ``0`` for a completed backup. 
        
                - **ElapsedTimeInSeconds** *(integer) --* 
        
                  The amount of time an in-progress snapshot backup has been running, or the amount of time it took a completed backup to finish.
        
                - **SourceRegion** *(string) --* 
        
                  The source region from which the snapshot was copied.
        
                - **Tags** *(list) --* 
        
                  The list of tags for the cluster snapshot.
        
                  - *(dict) --* 
        
                    A tag consisting of a name/value pair for a resource.
        
                    - **Key** *(string) --* 
        
                      The key, or name, for the resource tag.
        
                    - **Value** *(string) --* 
        
                      The value for the resource tag.
        
                - **RestorableNodeTypes** *(list) --* 
        
                  The list of node types that this cluster snapshot is able to restore into.
        
                  - *(string) --* 
              
                - **EnhancedVpcRouting** *(boolean) --* 
        
                  An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                  If this option is ``true`` , enhanced VPC routing is enabled. 
        
                  Default: false
        
                - **MaintenanceTrackName** *(string) --* 
        
                  The name of the maintenance track for the snapshot.
        
        """
        pass

    def describe_cluster_subnet_groups(self, ClusterSubnetGroupName: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None) -> Dict:
        """
        
        If you specify both tag keys and tag values in the same request, Amazon Redshift returns all subnet groups that match any combination of the specified keys and values. For example, if you have ``owner`` and ``environment`` for tag keys, and ``admin`` and ``test`` for tag values, all subnet groups that have any combination of those values are returned.
        
        If both tag keys and values are omitted from the request, subnet groups are returned regardless of whether they have tag keys or values associated with them.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusterSubnetGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_cluster_subnet_groups(
              ClusterSubnetGroupName=\'string\',
              MaxRecords=123,
              Marker=\'string\',
              TagKeys=[
                  \'string\',
              ],
              TagValues=[
                  \'string\',
              ]
          )
        :type ClusterSubnetGroupName: string
        :param ClusterSubnetGroupName: 
        
          The name of the cluster subnet group for which information is requested.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeClusterSubnetGroups request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
        :type TagKeys: list
        :param TagKeys: 
        
          A tag key or keys for which you want to return all matching cluster subnet groups that are associated with the specified key or keys. For example, suppose that you have subnet groups that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the subnet groups that have either or both of these tag keys associated with them.
        
          - *(string) --* 
        
        :type TagValues: list
        :param TagValues: 
        
          A tag value or values for which you want to return all matching cluster subnet groups that are associated with the specified tag value or values. For example, suppose that you have subnet groups that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the subnet groups that have either or both of these tag values associated with them.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'ClusterSubnetGroups\': [
                    {
                        \'ClusterSubnetGroupName\': \'string\',
                        \'Description\': \'string\',
                        \'VpcId\': \'string\',
                        \'SubnetGroupStatus\': \'string\',
                        \'Subnets\': [
                            {
                                \'SubnetIdentifier\': \'string\',
                                \'SubnetAvailabilityZone\': {
                                    \'Name\': \'string\',
                                    \'SupportedPlatforms\': [
                                        {
                                            \'Name\': \'string\'
                                        },
                                    ]
                                },
                                \'SubnetStatus\': \'string\'
                            },
                        ],
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output from the  DescribeClusterSubnetGroups action. 
        
            - **Marker** *(string) --* 
        
              A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the ``Marker`` parameter and retrying the command. If the ``Marker`` field is empty, all response records have been retrieved for the request. 
        
            - **ClusterSubnetGroups** *(list) --* 
        
              A list of  ClusterSubnetGroup instances. 
        
              - *(dict) --* 
        
                Describes a subnet group.
        
                - **ClusterSubnetGroupName** *(string) --* 
        
                  The name of the cluster subnet group.
        
                - **Description** *(string) --* 
        
                  The description of the cluster subnet group.
        
                - **VpcId** *(string) --* 
        
                  The VPC ID of the cluster subnet group.
        
                - **SubnetGroupStatus** *(string) --* 
        
                  The status of the cluster subnet group. Possible values are ``Complete`` , ``Incomplete`` and ``Invalid`` . 
        
                - **Subnets** *(list) --* 
        
                  A list of the VPC  Subnet elements. 
        
                  - *(dict) --* 
        
                    Describes a subnet.
        
                    - **SubnetIdentifier** *(string) --* 
        
                      The identifier of the subnet.
        
                    - **SubnetAvailabilityZone** *(dict) --* 
        
                      Describes an availability zone.
        
                      - **Name** *(string) --* 
        
                        The name of the availability zone.
        
                      - **SupportedPlatforms** *(list) --* 
                        
                        - *(dict) --* 
        
                          A list of supported platforms for orderable clusters.
        
                          - **Name** *(string) --* 
                      
                    - **SubnetStatus** *(string) --* 
        
                      The status of the subnet.
        
                - **Tags** *(list) --* 
        
                  The list of tags for the cluster subnet group.
        
                  - *(dict) --* 
        
                    A tag consisting of a name/value pair for a resource.
        
                    - **Key** *(string) --* 
        
                      The key, or name, for the resource tag.
        
                    - **Value** *(string) --* 
        
                      The value for the resource tag.
        
        """
        pass

    def describe_cluster_tracks(self, MaintenanceTrackName: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusterTracks>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_cluster_tracks(
              MaintenanceTrackName=\'string\',
              MaxRecords=123,
              Marker=\'string\'
          )
        :type MaintenanceTrackName: string
        :param MaintenanceTrackName: 
        
          The name of the maintenance track. 
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          An integer value for the maximum number of maintenance tracks to return.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a ``DescribeClusterTracks`` request exceed the value specified in ``MaxRecords`` , Amazon Redshift returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'MaintenanceTracks\': [
                    {
                        \'MaintenanceTrackName\': \'string\',
                        \'DatabaseVersion\': \'string\',
                        \'UpdateTargets\': [
                            {
                                \'MaintenanceTrackName\': \'string\',
                                \'DatabaseVersion\': \'string\'
                            },
                        ]
                    },
                ],
                \'Marker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **MaintenanceTracks** *(list) --* 
        
              A list of maintenance tracks output by the ``DescribeClusterTracks`` operation. 
        
              - *(dict) --* 
        
                Defines a maintenance track that determines which Amazon Redshift version to apply during a maintenance window. If the value for ``MaintenanceTrack`` is ``current`` , the cluster is updated to the most recently certified maintenance release. If the value is ``trailing`` , the cluster is updated to the previously certified maintenance release. 
        
                - **MaintenanceTrackName** *(string) --* 
        
                  The name of the maintenance track. Possible values are ``current`` and ``trailing`` .
        
                - **DatabaseVersion** *(string) --* 
        
                  The version number for the cluster release.
        
                - **UpdateTargets** *(list) --* 
        
                  An array of  UpdateTarget objects to update with the maintenance track. 
        
                  - *(dict) --* 
        
                    A maintenance track that you can switch the current track to.
        
                    - **MaintenanceTrackName** *(string) --* 
        
                      The name of the new maintenance track.
        
                    - **DatabaseVersion** *(string) --* 
        
                      The cluster version for the new maintenance track.
        
            - **Marker** *(string) --* 
        
              The starting point to return a set of response tracklist records. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request.
        
        """
        pass

    def describe_cluster_versions(self, ClusterVersion: str = None, ClusterParameterGroupFamily: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusterVersions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_cluster_versions(
              ClusterVersion=\'string\',
              ClusterParameterGroupFamily=\'string\',
              MaxRecords=123,
              Marker=\'string\'
          )
        :type ClusterVersion: string
        :param ClusterVersion: 
        
          The specific cluster version to return.
        
          Example: ``1.0``  
        
        :type ClusterParameterGroupFamily: string
        :param ClusterParameterGroupFamily: 
        
          The name of a specific cluster parameter group family to return details for.
        
          Constraints:
        
          * Must be 1 to 255 alphanumeric characters 
           
          * First character must be a letter 
           
          * Cannot end with a hyphen or contain two consecutive hyphens 
           
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeClusterVersions request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'ClusterVersions\': [
                    {
                        \'ClusterVersion\': \'string\',
                        \'ClusterParameterGroupFamily\': \'string\',
                        \'Description\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output from the  DescribeClusterVersions action. 
        
            - **Marker** *(string) --* 
        
              A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the ``Marker`` parameter and retrying the command. If the ``Marker`` field is empty, all response records have been retrieved for the request. 
        
            - **ClusterVersions** *(list) --* 
        
              A list of ``Version`` elements. 
        
              - *(dict) --* 
        
                Describes a cluster version, including the parameter group family and description of the version.
        
                - **ClusterVersion** *(string) --* 
        
                  The version number used by the cluster.
        
                - **ClusterParameterGroupFamily** *(string) --* 
        
                  The name of the cluster parameter group family for the cluster.
        
                - **Description** *(string) --* 
        
                  The description of the cluster version.
        
        """
        pass

    def describe_clusters(self, ClusterIdentifier: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None) -> Dict:
        """
        
        If you specify both tag keys and tag values in the same request, Amazon Redshift returns all clusters that match any combination of the specified keys and values. For example, if you have ``owner`` and ``environment`` for tag keys, and ``admin`` and ``test`` for tag values, all clusters that have any combination of those values are returned.
        
        If both tag keys and values are omitted from the request, clusters are returned regardless of whether they have tag keys or values associated with them.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusters>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_clusters(
              ClusterIdentifier=\'string\',
              MaxRecords=123,
              Marker=\'string\',
              TagKeys=[
                  \'string\',
              ],
              TagValues=[
                  \'string\',
              ]
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: 
        
          The unique identifier of a cluster whose properties you are requesting. This parameter is case sensitive.
        
          The default is that all clusters defined for an account are returned.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeClusters request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
          Constraints: You can specify either the **ClusterIdentifier** parameter or the **Marker** parameter, but not both. 
        
        :type TagKeys: list
        :param TagKeys: 
        
          A tag key or keys for which you want to return all matching clusters that are associated with the specified key or keys. For example, suppose that you have clusters that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag keys associated with them.
        
          - *(string) --* 
        
        :type TagValues: list
        :param TagValues: 
        
          A tag value or values for which you want to return all matching clusters that are associated with the specified tag value or values. For example, suppose that you have clusters that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag values associated with them.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'Clusters\': [
                    {
                        \'ClusterIdentifier\': \'string\',
                        \'NodeType\': \'string\',
                        \'ClusterStatus\': \'string\',
                        \'ModifyStatus\': \'string\',
                        \'MasterUsername\': \'string\',
                        \'DBName\': \'string\',
                        \'Endpoint\': {
                            \'Address\': \'string\',
                            \'Port\': 123
                        },
                        \'ClusterCreateTime\': datetime(2015, 1, 1),
                        \'AutomatedSnapshotRetentionPeriod\': 123,
                        \'ClusterSecurityGroups\': [
                            {
                                \'ClusterSecurityGroupName\': \'string\',
                                \'Status\': \'string\'
                            },
                        ],
                        \'VpcSecurityGroups\': [
                            {
                                \'VpcSecurityGroupId\': \'string\',
                                \'Status\': \'string\'
                            },
                        ],
                        \'ClusterParameterGroups\': [
                            {
                                \'ParameterGroupName\': \'string\',
                                \'ParameterApplyStatus\': \'string\',
                                \'ClusterParameterStatusList\': [
                                    {
                                        \'ParameterName\': \'string\',
                                        \'ParameterApplyStatus\': \'string\',
                                        \'ParameterApplyErrorDescription\': \'string\'
                                    },
                                ]
                            },
                        ],
                        \'ClusterSubnetGroupName\': \'string\',
                        \'VpcId\': \'string\',
                        \'AvailabilityZone\': \'string\',
                        \'PreferredMaintenanceWindow\': \'string\',
                        \'PendingModifiedValues\': {
                            \'MasterUserPassword\': \'string\',
                            \'NodeType\': \'string\',
                            \'NumberOfNodes\': 123,
                            \'ClusterType\': \'string\',
                            \'ClusterVersion\': \'string\',
                            \'AutomatedSnapshotRetentionPeriod\': 123,
                            \'ClusterIdentifier\': \'string\',
                            \'PubliclyAccessible\': True|False,
                            \'EnhancedVpcRouting\': True|False,
                            \'MaintenanceTrackName\': \'string\',
                            \'EncryptionType\': \'string\'
                        },
                        \'ClusterVersion\': \'string\',
                        \'AllowVersionUpgrade\': True|False,
                        \'NumberOfNodes\': 123,
                        \'PubliclyAccessible\': True|False,
                        \'Encrypted\': True|False,
                        \'RestoreStatus\': {
                            \'Status\': \'string\',
                            \'CurrentRestoreRateInMegaBytesPerSecond\': 123.0,
                            \'SnapshotSizeInMegaBytes\': 123,
                            \'ProgressInMegaBytes\': 123,
                            \'ElapsedTimeInSeconds\': 123,
                            \'EstimatedTimeToCompletionInSeconds\': 123
                        },
                        \'HsmStatus\': {
                            \'HsmClientCertificateIdentifier\': \'string\',
                            \'HsmConfigurationIdentifier\': \'string\',
                            \'Status\': \'string\'
                        },
                        \'ClusterSnapshotCopyStatus\': {
                            \'DestinationRegion\': \'string\',
                            \'RetentionPeriod\': 123,
                            \'SnapshotCopyGrantName\': \'string\'
                        },
                        \'ClusterPublicKey\': \'string\',
                        \'ClusterNodes\': [
                            {
                                \'NodeRole\': \'string\',
                                \'PrivateIPAddress\': \'string\',
                                \'PublicIPAddress\': \'string\'
                            },
                        ],
                        \'ElasticIpStatus\': {
                            \'ElasticIp\': \'string\',
                            \'Status\': \'string\'
                        },
                        \'ClusterRevisionNumber\': \'string\',
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'KmsKeyId\': \'string\',
                        \'EnhancedVpcRouting\': True|False,
                        \'IamRoles\': [
                            {
                                \'IamRoleArn\': \'string\',
                                \'ApplyStatus\': \'string\'
                            },
                        ],
                        \'PendingActions\': [
                            \'string\',
                        ],
                        \'MaintenanceTrackName\': \'string\',
                        \'ElasticResizeNumberOfNodeOptions\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output from the  DescribeClusters action. 
        
            - **Marker** *(string) --* 
        
              A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the ``Marker`` parameter and retrying the command. If the ``Marker`` field is empty, all response records have been retrieved for the request. 
        
            - **Clusters** *(list) --* 
        
              A list of ``Cluster`` objects, where each object describes one cluster. 
        
              - *(dict) --* 
        
                Describes a cluster.
        
                - **ClusterIdentifier** *(string) --* 
        
                  The unique identifier of the cluster.
        
                - **NodeType** *(string) --* 
        
                  The node type for the nodes in the cluster.
        
                - **ClusterStatus** *(string) --* 
        
                  The current state of the cluster. Possible values are the following:
        
                  * ``available``   
                   
                  * ``creating``   
                   
                  * ``deleting``   
                   
                  * ``final-snapshot``   
                   
                  * ``hardware-failure``   
                   
                  * ``incompatible-hsm``   
                   
                  * ``incompatible-network``   
                   
                  * ``incompatible-parameters``   
                   
                  * ``incompatible-restore``   
                   
                  * ``modifying``   
                   
                  * ``rebooting``   
                   
                  * ``renaming``   
                   
                  * ``resizing``   
                   
                  * ``rotating-keys``   
                   
                  * ``storage-full``   
                   
                  * ``updating-hsm``   
                   
                - **ModifyStatus** *(string) --* 
        
                  The status of a modify operation, if any, initiated for the cluster.
        
                - **MasterUsername** *(string) --* 
        
                  The master user name for the cluster. This name is used to connect to the database that is specified in the **DBName** parameter. 
        
                - **DBName** *(string) --* 
        
                  The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named ``dev`` dev was created by default. 
        
                - **Endpoint** *(dict) --* 
        
                  The connection endpoint.
        
                  - **Address** *(string) --* 
        
                    The DNS address of the Cluster.
        
                  - **Port** *(integer) --* 
        
                    The port that the database engine is listening on.
        
                - **ClusterCreateTime** *(datetime) --* 
        
                  The date and time that the cluster was created.
        
                - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                  The number of days that automatic cluster snapshots are retained.
        
                - **ClusterSecurityGroups** *(list) --* 
        
                  A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ``ClusterSecurityGroup.Name`` and ``ClusterSecurityGroup.Status`` subelements. 
        
                  Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the **VpcSecurityGroups** parameter. 
        
                  - *(dict) --* 
        
                    Describes a cluster security group.
        
                    - **ClusterSecurityGroupName** *(string) --* 
        
                      The name of the cluster security group.
        
                    - **Status** *(string) --* 
        
                      The status of the cluster security group.
        
                - **VpcSecurityGroups** *(list) --* 
        
                  A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.
        
                  - *(dict) --* 
        
                    Describes the members of a VPC security group.
        
                    - **VpcSecurityGroupId** *(string) --* 
        
                      The identifier of the VPC security group.
        
                    - **Status** *(string) --* 
        
                      The status of the VPC security group.
        
                - **ClusterParameterGroups** *(list) --* 
        
                  The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.
        
                  - *(dict) --* 
        
                    Describes the status of a parameter group.
        
                    - **ParameterGroupName** *(string) --* 
        
                      The name of the cluster parameter group.
        
                    - **ParameterApplyStatus** *(string) --* 
        
                      The status of parameter updates.
        
                    - **ClusterParameterStatusList** *(list) --* 
        
                      The list of parameter statuses.
        
                      For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
                      - *(dict) --* 
        
                        Describes the status of a parameter group.
        
                        - **ParameterName** *(string) --* 
        
                          The name of the parameter.
        
                        - **ParameterApplyStatus** *(string) --* 
        
                          The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
        
                          The following are possible statuses and descriptions.
        
                          * ``in-sync`` : The parameter value is in sync with the database. 
                           
                          * ``pending-reboot`` : The parameter value will be applied after the cluster reboots. 
                           
                          * ``applying`` : The parameter value is being applied to the database. 
                           
                          * ``invalid-parameter`` : Cannot apply the parameter value because it has an invalid value or syntax. 
                           
                          * ``apply-deferred`` : The parameter contains static property changes. The changes are deferred until the cluster reboots. 
                           
                          * ``apply-error`` : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots. 
                           
                          * ``unknown-error`` : Cannot apply the parameter change right now. The change will be applied after the cluster reboots. 
                           
                        - **ParameterApplyErrorDescription** *(string) --* 
        
                          The error that prevented the parameter from being applied to the database.
        
                - **ClusterSubnetGroupName** *(string) --* 
        
                  The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.
        
                - **VpcId** *(string) --* 
        
                  The identifier of the VPC the cluster is in, if the cluster is in a VPC.
        
                - **AvailabilityZone** *(string) --* 
        
                  The name of the Availability Zone in which the cluster is located.
        
                - **PreferredMaintenanceWindow** *(string) --* 
        
                  The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.
        
                - **PendingModifiedValues** *(dict) --* 
        
                  A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.
        
                  - **MasterUserPassword** *(string) --* 
        
                    The pending or in-progress change of the master user password for the cluster.
        
                  - **NodeType** *(string) --* 
        
                    The pending or in-progress change of the cluster\'s node type.
        
                  - **NumberOfNodes** *(integer) --* 
        
                    The pending or in-progress change of the number of nodes in the cluster.
        
                  - **ClusterType** *(string) --* 
        
                    The pending or in-progress change of the cluster type.
        
                  - **ClusterVersion** *(string) --* 
        
                    The pending or in-progress change of the service version.
        
                  - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                    The pending or in-progress change of the automated snapshot retention period.
        
                  - **ClusterIdentifier** *(string) --* 
        
                    The pending or in-progress change of the new identifier for the cluster.
        
                  - **PubliclyAccessible** *(boolean) --* 
        
                    The pending or in-progress change of the ability to connect to the cluster from the public network.
        
                  - **EnhancedVpcRouting** *(boolean) --* 
        
                    An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                    If this option is ``true`` , enhanced VPC routing is enabled. 
        
                    Default: false
        
                  - **MaintenanceTrackName** *(string) --* 
        
                    The name of the maintenance track that the cluster will change to during the next maintenance window.
        
                  - **EncryptionType** *(string) --* 
        
                    The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy. 
        
                - **ClusterVersion** *(string) --* 
        
                  The version ID of the Amazon Redshift engine that is running on the cluster.
        
                - **AllowVersionUpgrade** *(boolean) --* 
        
                  A Boolean value that, if ``true`` , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window. 
        
                - **NumberOfNodes** *(integer) --* 
        
                  The number of compute nodes in the cluster.
        
                - **PubliclyAccessible** *(boolean) --* 
        
                  A Boolean value that, if ``true`` , indicates that the cluster can be accessed from a public network.
        
                - **Encrypted** *(boolean) --* 
        
                  A Boolean value that, if ``true`` , indicates that data in the cluster is encrypted at rest.
        
                - **RestoreStatus** *(dict) --* 
        
                  A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.
        
                  - **Status** *(string) --* 
        
                    The status of the restore action. Returns starting, restoring, completed, or failed.
        
                  - **CurrentRestoreRateInMegaBytesPerSecond** *(float) --* 
        
                    The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.
        
                  - **SnapshotSizeInMegaBytes** *(integer) --* 
        
                    The size of the set of snapshot data used to restore the cluster.
        
                  - **ProgressInMegaBytes** *(integer) --* 
        
                    The number of megabytes that have been transferred from snapshot storage.
        
                  - **ElapsedTimeInSeconds** *(integer) --* 
        
                    The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.
        
                  - **EstimatedTimeToCompletionInSeconds** *(integer) --* 
        
                    The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore.
        
                - **HsmStatus** *(dict) --* 
        
                  A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
        
                  Values: active, applying
        
                  - **HsmClientCertificateIdentifier** *(string) --* 
        
                    Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        
                  - **HsmConfigurationIdentifier** *(string) --* 
        
                    Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        
                  - **Status** *(string) --* 
        
                    Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
        
                    Values: active, applying
        
                - **ClusterSnapshotCopyStatus** *(dict) --* 
        
                  A value that returns the destination region and retention period that are configured for cross-region snapshot copy.
        
                  - **DestinationRegion** *(string) --* 
        
                    The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
        
                  - **RetentionPeriod** *(integer) --* 
        
                    The number of days that automated snapshots are retained in the destination region after they are copied from a source region.
        
                  - **SnapshotCopyGrantName** *(string) --* 
        
                    The name of the snapshot copy grant.
        
                - **ClusterPublicKey** *(string) --* 
        
                  The public key for the cluster.
        
                - **ClusterNodes** *(list) --* 
        
                  The nodes in the cluster.
        
                  - *(dict) --* 
        
                    The identifier of a node in a cluster.
        
                    - **NodeRole** *(string) --* 
        
                      Whether the node is a leader node or a compute node.
        
                    - **PrivateIPAddress** *(string) --* 
        
                      The private IP address of a node within a cluster.
        
                    - **PublicIPAddress** *(string) --* 
        
                      The public IP address of a node within a cluster.
        
                - **ElasticIpStatus** *(dict) --* 
        
                  The status of the elastic IP (EIP) address.
        
                  - **ElasticIp** *(string) --* 
        
                    The elastic IP (EIP) address for the cluster.
        
                  - **Status** *(string) --* 
        
                    The status of the elastic IP (EIP) address.
        
                - **ClusterRevisionNumber** *(string) --* 
        
                  The specific revision number of the database in the cluster.
        
                - **Tags** *(list) --* 
        
                  The list of tags for the cluster.
        
                  - *(dict) --* 
        
                    A tag consisting of a name/value pair for a resource.
        
                    - **Key** *(string) --* 
        
                      The key, or name, for the resource tag.
        
                    - **Value** *(string) --* 
        
                      The value for the resource tag.
        
                - **KmsKeyId** *(string) --* 
        
                  The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.
        
                - **EnhancedVpcRouting** *(boolean) --* 
        
                  An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                  If this option is ``true`` , enhanced VPC routing is enabled. 
        
                  Default: false
        
                - **IamRoles** *(list) --* 
        
                  A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.
        
                  - *(dict) --* 
        
                    An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.
        
                    - **IamRoleArn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the IAM role, for example, ``arn:aws:iam::123456789012:role/RedshiftCopyUnload`` . 
        
                    - **ApplyStatus** *(string) --* 
        
                      A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
        
                      The following are possible statuses and descriptions.
        
                      * ``in-sync`` : The role is available for use by the cluster. 
                       
                      * ``adding`` : The role is in the process of being associated with the cluster. 
                       
                      * ``removing`` : The role is in the process of being disassociated with the cluster. 
                       
                - **PendingActions** *(list) --* 
        
                  Cluster operations that are waiting to be started.
        
                  - *(string) --* 
              
                - **MaintenanceTrackName** *(string) --* 
        
                  The name of the maintenance track for the cluster.
        
                - **ElasticResizeNumberOfNodeOptions** *(string) --* 
        
                  Indicates the number of nodes the cluster can be resized to with the elastic resize method. 
        
        """
        pass

    def describe_default_cluster_parameters(self, ParameterGroupFamily: str, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeDefaultClusterParameters>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_default_cluster_parameters(
              ParameterGroupFamily=\'string\',
              MaxRecords=123,
              Marker=\'string\'
          )
        :type ParameterGroupFamily: string
        :param ParameterGroupFamily: **[REQUIRED]** 
        
          The name of the cluster parameter group family.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeDefaultClusterParameters request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DefaultClusterParameters\': {
                    \'ParameterGroupFamily\': \'string\',
                    \'Marker\': \'string\',
                    \'Parameters\': [
                        {
                            \'ParameterName\': \'string\',
                            \'ParameterValue\': \'string\',
                            \'Description\': \'string\',
                            \'Source\': \'string\',
                            \'DataType\': \'string\',
                            \'AllowedValues\': \'string\',
                            \'ApplyType\': \'static\'|\'dynamic\',
                            \'IsModifiable\': True|False,
                            \'MinimumEngineVersion\': \'string\'
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DefaultClusterParameters** *(dict) --* 
        
              Describes the default cluster parameters for a parameter group family.
        
              - **ParameterGroupFamily** *(string) --* 
        
                The name of the cluster parameter group family to which the engine default parameters apply.
        
              - **Marker** *(string) --* 
        
                A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the ``Marker`` parameter and retrying the command. If the ``Marker`` field is empty, all response records have been retrieved for the request. 
        
              - **Parameters** *(list) --* 
        
                The list of cluster default parameters.
        
                - *(dict) --* 
        
                  Describes a parameter in a cluster parameter group.
        
                  - **ParameterName** *(string) --* 
        
                    The name of the parameter.
        
                  - **ParameterValue** *(string) --* 
        
                    The value of the parameter.
        
                  - **Description** *(string) --* 
        
                    A description of the parameter.
        
                  - **Source** *(string) --* 
        
                    The source of the parameter value, such as \"engine-default\" or \"user\".
        
                  - **DataType** *(string) --* 
        
                    The data type of the parameter.
        
                  - **AllowedValues** *(string) --* 
        
                    The valid range of values for the parameter.
        
                  - **ApplyType** *(string) --* 
        
                    Specifies how to apply the WLM configuration parameter. Some properties can be applied dynamically, while other properties require that any associated clusters be rebooted for the configuration changes to be applied. For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
                  - **IsModifiable** *(boolean) --* 
        
                    If ``true`` , the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed. 
        
                  - **MinimumEngineVersion** *(string) --* 
        
                    The earliest engine version to which the parameter can apply.
        
        """
        pass

    def describe_event_categories(self, SourceType: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeEventCategories>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_event_categories(
              SourceType=\'string\'
          )
        :type SourceType: string
        :param SourceType: 
        
          The source type, such as cluster or parameter group, to which the described event categories apply.
        
          Valid values: cluster, cluster-snapshot, cluster-parameter-group, and cluster-security-group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EventCategoriesMapList\': [
                    {
                        \'SourceType\': \'string\',
                        \'Events\': [
                            {
                                \'EventId\': \'string\',
                                \'EventCategories\': [
                                    \'string\',
                                ],
                                \'EventDescription\': \'string\',
                                \'Severity\': \'string\'
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **EventCategoriesMapList** *(list) --* 
        
              A list of event categories descriptions.
        
              - *(dict) --* 
        
                Describes event categories.
        
                - **SourceType** *(string) --* 
        
                  The source type, such as cluster or cluster-snapshot, that the returned categories belong to.
        
                - **Events** *(list) --* 
        
                  The events in the event category.
        
                  - *(dict) --* 
        
                    Describes event information.
        
                    - **EventId** *(string) --* 
        
                      The identifier of an Amazon Redshift event.
        
                    - **EventCategories** *(list) --* 
        
                      The category of an Amazon Redshift event.
        
                      - *(string) --* 
                  
                    - **EventDescription** *(string) --* 
        
                      The description of an Amazon Redshift event.
        
                    - **Severity** *(string) --* 
        
                      The severity of the event.
        
                      Values: ERROR, INFO
        
        """
        pass

    def describe_event_subscriptions(self, SubscriptionName: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None) -> Dict:
        """
        
        If you specify both tag keys and tag values in the same request, Amazon Redshift returns all event notification subscriptions that match any combination of the specified keys and values. For example, if you have ``owner`` and ``environment`` for tag keys, and ``admin`` and ``test`` for tag values, all subscriptions that have any combination of those values are returned.
        
        If both tag keys and values are omitted from the request, subscriptions are returned regardless of whether they have tag keys or values associated with them.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeEventSubscriptions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_event_subscriptions(
              SubscriptionName=\'string\',
              MaxRecords=123,
              Marker=\'string\',
              TagKeys=[
                  \'string\',
              ],
              TagValues=[
                  \'string\',
              ]
          )
        :type SubscriptionName: string
        :param SubscriptionName: 
        
          The name of the Amazon Redshift event notification subscription to be described.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeEventSubscriptions request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
        :type TagKeys: list
        :param TagKeys: 
        
          A tag key or keys for which you want to return all matching event notification subscriptions that are associated with the specified key or keys. For example, suppose that you have subscriptions that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the subscriptions that have either or both of these tag keys associated with them.
        
          - *(string) --* 
        
        :type TagValues: list
        :param TagValues: 
        
          A tag value or values for which you want to return all matching event notification subscriptions that are associated with the specified tag value or values. For example, suppose that you have subscriptions that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the subscriptions that have either or both of these tag values associated with them.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'EventSubscriptionsList\': [
                    {
                        \'CustomerAwsId\': \'string\',
                        \'CustSubscriptionId\': \'string\',
                        \'SnsTopicArn\': \'string\',
                        \'Status\': \'string\',
                        \'SubscriptionCreationTime\': datetime(2015, 1, 1),
                        \'SourceType\': \'string\',
                        \'SourceIdsList\': [
                            \'string\',
                        ],
                        \'EventCategoriesList\': [
                            \'string\',
                        ],
                        \'Severity\': \'string\',
                        \'Enabled\': True|False,
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the ``Marker`` parameter and retrying the command. If the ``Marker`` field is empty, all response records have been retrieved for the request. 
        
            - **EventSubscriptionsList** *(list) --* 
        
              A list of event subscriptions.
        
              - *(dict) --* 
        
                Describes event subscriptions.
        
                - **CustomerAwsId** *(string) --* 
        
                  The AWS customer account associated with the Amazon Redshift event notification subscription.
        
                - **CustSubscriptionId** *(string) --* 
        
                  The name of the Amazon Redshift event notification subscription.
        
                - **SnsTopicArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the Amazon SNS topic used by the event notification subscription.
        
                - **Status** *(string) --* 
        
                  The status of the Amazon Redshift event notification subscription.
        
                  Constraints:
        
                  * Can be one of the following: active | no-permission | topic-not-exist 
                   
                  * The status \"no-permission\" indicates that Amazon Redshift no longer has permission to post to the Amazon SNS topic. The status \"topic-not-exist\" indicates that the topic was deleted after the subscription was created. 
                   
                - **SubscriptionCreationTime** *(datetime) --* 
        
                  The date and time the Amazon Redshift event notification subscription was created.
        
                - **SourceType** *(string) --* 
        
                  The source type of the events returned the Amazon Redshift event notification, such as cluster, or cluster-snapshot.
        
                - **SourceIdsList** *(list) --* 
        
                  A list of the sources that publish events to the Amazon Redshift event notification subscription.
        
                  - *(string) --* 
              
                - **EventCategoriesList** *(list) --* 
        
                  The list of Amazon Redshift event categories specified in the event notification subscription.
        
                  Values: Configuration, Management, Monitoring, Security
        
                  - *(string) --* 
              
                - **Severity** *(string) --* 
        
                  The event severity specified in the Amazon Redshift event notification subscription.
        
                  Values: ERROR, INFO
        
                - **Enabled** *(boolean) --* 
        
                  A Boolean value indicating whether the subscription is enabled. ``true`` indicates the subscription is enabled.
        
                - **Tags** *(list) --* 
        
                  The list of tags for the event subscription.
        
                  - *(dict) --* 
        
                    A tag consisting of a name/value pair for a resource.
        
                    - **Key** *(string) --* 
        
                      The key, or name, for the resource tag.
        
                    - **Value** *(string) --* 
        
                      The value for the resource tag.
        
        """
        pass

    def describe_events(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeEvents>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_events(
              SourceIdentifier=\'string\',
              SourceType=\'cluster\'|\'cluster-parameter-group\'|\'cluster-security-group\'|\'cluster-snapshot\',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Duration=123,
              MaxRecords=123,
              Marker=\'string\'
          )
        :type SourceIdentifier: string
        :param SourceIdentifier: 
        
          The identifier of the event source for which events will be returned. If this parameter is not specified, then all sources are included in the response.
        
          Constraints:
        
          If *SourceIdentifier* is supplied, *SourceType* must also be provided.
        
          * Specify a cluster identifier when *SourceType* is ``cluster`` . 
           
          * Specify a cluster security group name when *SourceType* is ``cluster-security-group`` . 
           
          * Specify a cluster parameter group name when *SourceType* is ``cluster-parameter-group`` . 
           
          * Specify a cluster snapshot identifier when *SourceType* is ``cluster-snapshot`` . 
           
        :type SourceType: string
        :param SourceType: 
        
          The event source to retrieve events for. If no value is specified, all events are returned.
        
          Constraints:
        
          If *SourceType* is supplied, *SourceIdentifier* must also be provided.
        
          * Specify ``cluster`` when *SourceIdentifier* is a cluster identifier. 
           
          * Specify ``cluster-security-group`` when *SourceIdentifier* is a cluster security group name. 
           
          * Specify ``cluster-parameter-group`` when *SourceIdentifier* is a cluster parameter group name. 
           
          * Specify ``cluster-snapshot`` when *SourceIdentifier* is a cluster snapshot identifier. 
           
        :type StartTime: datetime
        :param StartTime: 
        
          The beginning of the time interval to retrieve events for, specified in ISO 8601 format. For more information about ISO 8601, go to the `ISO8601 Wikipedia page. <http://en.wikipedia.org/wiki/ISO_8601>`__  
        
          Example: ``2009-07-08T18:00Z``  
        
        :type EndTime: datetime
        :param EndTime: 
        
          The end of the time interval for which to retrieve events, specified in ISO 8601 format. For more information about ISO 8601, go to the `ISO8601 Wikipedia page. <http://en.wikipedia.org/wiki/ISO_8601>`__  
        
          Example: ``2009-07-08T18:00Z``  
        
        :type Duration: integer
        :param Duration: 
        
          The number of minutes prior to the time of the request for which to retrieve events. For example, if the request is sent at 18:00 and you specify a duration of 60, then only events which have occurred after 17:00 will be returned.
        
          Default: ``60``  
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeEvents request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'Events\': [
                    {
                        \'SourceIdentifier\': \'string\',
                        \'SourceType\': \'cluster\'|\'cluster-parameter-group\'|\'cluster-security-group\'|\'cluster-snapshot\',
                        \'Message\': \'string\',
                        \'EventCategories\': [
                            \'string\',
                        ],
                        \'Severity\': \'string\',
                        \'Date\': datetime(2015, 1, 1),
                        \'EventId\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the ``Marker`` parameter and retrying the command. If the ``Marker`` field is empty, all response records have been retrieved for the request. 
        
            - **Events** *(list) --* 
        
              A list of ``Event`` instances. 
        
              - *(dict) --* 
        
                Describes an event.
        
                - **SourceIdentifier** *(string) --* 
        
                  The identifier for the source of the event.
        
                - **SourceType** *(string) --* 
        
                  The source type for this event.
        
                - **Message** *(string) --* 
        
                  The text of this event.
        
                - **EventCategories** *(list) --* 
        
                  A list of the event categories.
        
                  Values: Configuration, Management, Monitoring, Security
        
                  - *(string) --* 
              
                - **Severity** *(string) --* 
        
                  The severity of the event.
        
                  Values: ERROR, INFO
        
                - **Date** *(datetime) --* 
        
                  The date and time of the event.
        
                - **EventId** *(string) --* 
        
                  The identifier of the event.
        
        """
        pass

    def describe_hsm_client_certificates(self, HsmClientCertificateIdentifier: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None) -> Dict:
        """
        
        If you specify both tag keys and tag values in the same request, Amazon Redshift returns all HSM client certificates that match any combination of the specified keys and values. For example, if you have ``owner`` and ``environment`` for tag keys, and ``admin`` and ``test`` for tag values, all HSM client certificates that have any combination of those values are returned.
        
        If both tag keys and values are omitted from the request, HSM client certificates are returned regardless of whether they have tag keys or values associated with them.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeHsmClientCertificates>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_hsm_client_certificates(
              HsmClientCertificateIdentifier=\'string\',
              MaxRecords=123,
              Marker=\'string\',
              TagKeys=[
                  \'string\',
              ],
              TagValues=[
                  \'string\',
              ]
          )
        :type HsmClientCertificateIdentifier: string
        :param HsmClientCertificateIdentifier: 
        
          The identifier of a specific HSM client certificate for which you want information. If no identifier is specified, information is returned for all HSM client certificates owned by your AWS customer account.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeHsmClientCertificates request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
        :type TagKeys: list
        :param TagKeys: 
        
          A tag key or keys for which you want to return all matching HSM client certificates that are associated with the specified key or keys. For example, suppose that you have HSM client certificates that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the HSM client certificates that have either or both of these tag keys associated with them.
        
          - *(string) --* 
        
        :type TagValues: list
        :param TagValues: 
        
          A tag value or values for which you want to return all matching HSM client certificates that are associated with the specified tag value or values. For example, suppose that you have HSM client certificates that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the HSM client certificates that have either or both of these tag values associated with them.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'HsmClientCertificates\': [
                    {
                        \'HsmClientCertificateIdentifier\': \'string\',
                        \'HsmClientCertificatePublicKey\': \'string\',
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the ``Marker`` parameter and retrying the command. If the ``Marker`` field is empty, all response records have been retrieved for the request. 
        
            - **HsmClientCertificates** *(list) --* 
        
              A list of the identifiers for one or more HSM client certificates used by Amazon Redshift clusters to store and retrieve database encryption keys in an HSM.
        
              - *(dict) --* 
        
                Returns information about an HSM client certificate. The certificate is stored in a secure Hardware Storage Module (HSM), and used by the Amazon Redshift cluster to encrypt data files.
        
                - **HsmClientCertificateIdentifier** *(string) --* 
        
                  The identifier of the HSM client certificate.
        
                - **HsmClientCertificatePublicKey** *(string) --* 
        
                  The public key that the Amazon Redshift cluster will use to connect to the HSM. You must register the public key in the HSM.
        
                - **Tags** *(list) --* 
        
                  The list of tags for the HSM client certificate.
        
                  - *(dict) --* 
        
                    A tag consisting of a name/value pair for a resource.
        
                    - **Key** *(string) --* 
        
                      The key, or name, for the resource tag.
        
                    - **Value** *(string) --* 
        
                      The value for the resource tag.
        
        """
        pass

    def describe_hsm_configurations(self, HsmConfigurationIdentifier: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None) -> Dict:
        """
        
        If you specify both tag keys and tag values in the same request, Amazon Redshift returns all HSM connections that match any combination of the specified keys and values. For example, if you have ``owner`` and ``environment`` for tag keys, and ``admin`` and ``test`` for tag values, all HSM connections that have any combination of those values are returned.
        
        If both tag keys and values are omitted from the request, HSM connections are returned regardless of whether they have tag keys or values associated with them.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeHsmConfigurations>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_hsm_configurations(
              HsmConfigurationIdentifier=\'string\',
              MaxRecords=123,
              Marker=\'string\',
              TagKeys=[
                  \'string\',
              ],
              TagValues=[
                  \'string\',
              ]
          )
        :type HsmConfigurationIdentifier: string
        :param HsmConfigurationIdentifier: 
        
          The identifier of a specific Amazon Redshift HSM configuration to be described. If no identifier is specified, information is returned for all HSM configurations owned by your AWS customer account.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeHsmConfigurations request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
        :type TagKeys: list
        :param TagKeys: 
        
          A tag key or keys for which you want to return all matching HSM configurations that are associated with the specified key or keys. For example, suppose that you have HSM configurations that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the HSM configurations that have either or both of these tag keys associated with them.
        
          - *(string) --* 
        
        :type TagValues: list
        :param TagValues: 
        
          A tag value or values for which you want to return all matching HSM configurations that are associated with the specified tag value or values. For example, suppose that you have HSM configurations that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the HSM configurations that have either or both of these tag values associated with them.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'HsmConfigurations\': [
                    {
                        \'HsmConfigurationIdentifier\': \'string\',
                        \'Description\': \'string\',
                        \'HsmIpAddress\': \'string\',
                        \'HsmPartitionName\': \'string\',
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the ``Marker`` parameter and retrying the command. If the ``Marker`` field is empty, all response records have been retrieved for the request. 
        
            - **HsmConfigurations** *(list) --* 
        
              A list of ``HsmConfiguration`` objects.
        
              - *(dict) --* 
        
                Returns information about an HSM configuration, which is an object that describes to Amazon Redshift clusters the information they require to connect to an HSM where they can store database encryption keys.
        
                - **HsmConfigurationIdentifier** *(string) --* 
        
                  The name of the Amazon Redshift HSM configuration.
        
                - **Description** *(string) --* 
        
                  A text description of the HSM configuration.
        
                - **HsmIpAddress** *(string) --* 
        
                  The IP address that the Amazon Redshift cluster must use to access the HSM.
        
                - **HsmPartitionName** *(string) --* 
        
                  The name of the partition in the HSM where the Amazon Redshift clusters will store their database encryption keys.
        
                - **Tags** *(list) --* 
        
                  The list of tags for the HSM configuration.
        
                  - *(dict) --* 
        
                    A tag consisting of a name/value pair for a resource.
        
                    - **Key** *(string) --* 
        
                      The key, or name, for the resource tag.
        
                    - **Value** *(string) --* 
        
                      The value for the resource tag.
        
        """
        pass

    def describe_logging_status(self, ClusterIdentifier: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeLoggingStatus>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_logging_status(
              ClusterIdentifier=\'string\'
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          The identifier of the cluster from which to get the logging status.
        
          Example: ``examplecluster``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'LoggingEnabled\': True|False,
                \'BucketName\': \'string\',
                \'S3KeyPrefix\': \'string\',
                \'LastSuccessfulDeliveryTime\': datetime(2015, 1, 1),
                \'LastFailureTime\': datetime(2015, 1, 1),
                \'LastFailureMessage\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Describes the status of logging for a cluster.
        
            - **LoggingEnabled** *(boolean) --* 
        
               ``true`` if logging is on, ``false`` if logging is off.
        
            - **BucketName** *(string) --* 
        
              The name of the S3 bucket where the log files are stored.
        
            - **S3KeyPrefix** *(string) --* 
        
              The prefix applied to the log file names.
        
            - **LastSuccessfulDeliveryTime** *(datetime) --* 
        
              The last time that logs were delivered.
        
            - **LastFailureTime** *(datetime) --* 
        
              The last time when logs failed to be delivered.
        
            - **LastFailureMessage** *(string) --* 
        
              The message indicating that logs failed to be delivered.
        
        """
        pass

    def describe_orderable_cluster_options(self, ClusterVersion: str = None, NodeType: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeOrderableClusterOptions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_orderable_cluster_options(
              ClusterVersion=\'string\',
              NodeType=\'string\',
              MaxRecords=123,
              Marker=\'string\'
          )
        :type ClusterVersion: string
        :param ClusterVersion: 
        
          The version filter value. Specify this parameter to show only the available offerings matching the specified version.
        
          Default: All versions.
        
          Constraints: Must be one of the version returned from  DescribeClusterVersions .
        
        :type NodeType: string
        :param NodeType: 
        
          The node type filter value. Specify this parameter to show only the available offerings matching the specified node type.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeOrderableClusterOptions request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OrderableClusterOptions\': [
                    {
                        \'ClusterVersion\': \'string\',
                        \'ClusterType\': \'string\',
                        \'NodeType\': \'string\',
                        \'AvailabilityZones\': [
                            {
                                \'Name\': \'string\',
                                \'SupportedPlatforms\': [
                                    {
                                        \'Name\': \'string\'
                                    },
                                ]
                            },
                        ]
                    },
                ],
                \'Marker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output from the  DescribeOrderableClusterOptions action. 
        
            - **OrderableClusterOptions** *(list) --* 
        
              An ``OrderableClusterOption`` structure containing information about orderable options for the cluster.
        
              - *(dict) --* 
        
                Describes an orderable cluster option.
        
                - **ClusterVersion** *(string) --* 
        
                  The version of the orderable cluster.
        
                - **ClusterType** *(string) --* 
        
                  The cluster type, for example ``multi-node`` . 
        
                - **NodeType** *(string) --* 
        
                  The node type for the orderable cluster.
        
                - **AvailabilityZones** *(list) --* 
        
                  A list of availability zones for the orderable cluster.
        
                  - *(dict) --* 
        
                    Describes an availability zone.
        
                    - **Name** *(string) --* 
        
                      The name of the availability zone.
        
                    - **SupportedPlatforms** *(list) --* 
                      
                      - *(dict) --* 
        
                        A list of supported platforms for orderable clusters.
        
                        - **Name** *(string) --* 
                    
            - **Marker** *(string) --* 
        
              A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the ``Marker`` parameter and retrying the command. If the ``Marker`` field is empty, all response records have been retrieved for the request. 
        
        """
        pass

    def describe_reserved_node_offerings(self, ReservedNodeOfferingId: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        For more information about reserved node offerings, go to `Purchasing Reserved Nodes <http://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeReservedNodeOfferings>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_reserved_node_offerings(
              ReservedNodeOfferingId=\'string\',
              MaxRecords=123,
              Marker=\'string\'
          )
        :type ReservedNodeOfferingId: string
        :param ReservedNodeOfferingId: 
        
          The unique identifier for the offering.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeReservedNodeOfferings request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'ReservedNodeOfferings\': [
                    {
                        \'ReservedNodeOfferingId\': \'string\',
                        \'NodeType\': \'string\',
                        \'Duration\': 123,
                        \'FixedPrice\': 123.0,
                        \'UsagePrice\': 123.0,
                        \'CurrencyCode\': \'string\',
                        \'OfferingType\': \'string\',
                        \'RecurringCharges\': [
                            {
                                \'RecurringChargeAmount\': 123.0,
                                \'RecurringChargeFrequency\': \'string\'
                            },
                        ],
                        \'ReservedNodeOfferingType\': \'Regular\'|\'Upgradable\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the ``Marker`` parameter and retrying the command. If the ``Marker`` field is empty, all response records have been retrieved for the request. 
        
            - **ReservedNodeOfferings** *(list) --* 
        
              A list of ``ReservedNodeOffering`` objects.
        
              - *(dict) --* 
        
                Describes a reserved node offering.
        
                - **ReservedNodeOfferingId** *(string) --* 
        
                  The offering identifier.
        
                - **NodeType** *(string) --* 
        
                  The node type offered by the reserved node offering.
        
                - **Duration** *(integer) --* 
        
                  The duration, in seconds, for which the offering will reserve the node.
        
                - **FixedPrice** *(float) --* 
        
                  The upfront fixed charge you will pay to purchase the specific reserved node offering.
        
                - **UsagePrice** *(float) --* 
        
                  The rate you are charged for each hour the cluster that is using the offering is running.
        
                - **CurrencyCode** *(string) --* 
        
                  The currency code for the compute nodes offering.
        
                - **OfferingType** *(string) --* 
        
                  The anticipated utilization of the reserved node, as defined in the reserved node offering.
        
                - **RecurringCharges** *(list) --* 
        
                  The charge to your account regardless of whether you are creating any clusters using the node offering. Recurring charges are only in effect for heavy-utilization reserved nodes.
        
                  - *(dict) --* 
        
                    Describes a recurring charge.
        
                    - **RecurringChargeAmount** *(float) --* 
        
                      The amount charged per the period of time specified by the recurring charge frequency.
        
                    - **RecurringChargeFrequency** *(string) --* 
        
                      The frequency at which the recurring charge amount is applied.
        
                - **ReservedNodeOfferingType** *(string) --* 
            
        """
        pass

    def describe_reserved_nodes(self, ReservedNodeId: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeReservedNodes>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_reserved_nodes(
              ReservedNodeId=\'string\',
              MaxRecords=123,
              Marker=\'string\'
          )
        :type ReservedNodeId: string
        :param ReservedNodeId: 
        
          Identifier for the node reservation.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeReservedNodes request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'ReservedNodes\': [
                    {
                        \'ReservedNodeId\': \'string\',
                        \'ReservedNodeOfferingId\': \'string\',
                        \'NodeType\': \'string\',
                        \'StartTime\': datetime(2015, 1, 1),
                        \'Duration\': 123,
                        \'FixedPrice\': 123.0,
                        \'UsagePrice\': 123.0,
                        \'CurrencyCode\': \'string\',
                        \'NodeCount\': 123,
                        \'State\': \'string\',
                        \'OfferingType\': \'string\',
                        \'RecurringCharges\': [
                            {
                                \'RecurringChargeAmount\': 123.0,
                                \'RecurringChargeFrequency\': \'string\'
                            },
                        ],
                        \'ReservedNodeOfferingType\': \'Regular\'|\'Upgradable\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the ``Marker`` parameter and retrying the command. If the ``Marker`` field is empty, all response records have been retrieved for the request. 
        
            - **ReservedNodes** *(list) --* 
        
              The list of ``ReservedNode`` objects.
        
              - *(dict) --* 
        
                Describes a reserved node. You can call the  DescribeReservedNodeOfferings API to obtain the available reserved node offerings. 
        
                - **ReservedNodeId** *(string) --* 
        
                  The unique identifier for the reservation.
        
                - **ReservedNodeOfferingId** *(string) --* 
        
                  The identifier for the reserved node offering.
        
                - **NodeType** *(string) --* 
        
                  The node type of the reserved node.
        
                - **StartTime** *(datetime) --* 
        
                  The time the reservation started. You purchase a reserved node offering for a duration. This is the start time of that duration.
        
                - **Duration** *(integer) --* 
        
                  The duration of the node reservation in seconds.
        
                - **FixedPrice** *(float) --* 
        
                  The fixed cost Amazon Redshift charges you for this reserved node.
        
                - **UsagePrice** *(float) --* 
        
                  The hourly rate Amazon Redshift charges you for this reserved node.
        
                - **CurrencyCode** *(string) --* 
        
                  The currency code for the reserved cluster.
        
                - **NodeCount** *(integer) --* 
        
                  The number of reserved compute nodes.
        
                - **State** *(string) --* 
        
                  The state of the reserved compute node.
        
                  Possible Values:
        
                  * pending-payment-This reserved node has recently been purchased, and the sale has been approved, but payment has not yet been confirmed. 
                   
                  * active-This reserved node is owned by the caller and is available for use. 
                   
                  * payment-failed-Payment failed for the purchase attempt. 
                   
                  * retired-The reserved node is no longer available.  
                   
                  * exchanging-The owner is exchanging the reserved node for another reserved node. 
                   
                - **OfferingType** *(string) --* 
        
                  The anticipated utilization of the reserved node, as defined in the reserved node offering.
        
                - **RecurringCharges** *(list) --* 
        
                  The recurring charges for the reserved node.
        
                  - *(dict) --* 
        
                    Describes a recurring charge.
        
                    - **RecurringChargeAmount** *(float) --* 
        
                      The amount charged per the period of time specified by the recurring charge frequency.
        
                    - **RecurringChargeFrequency** *(string) --* 
        
                      The frequency at which the recurring charge amount is applied.
        
                - **ReservedNodeOfferingType** *(string) --* 
            
        """
        pass

    def describe_resize(self, ClusterIdentifier: str) -> Dict:
        """
        
        A resize operation can be requested using  ModifyCluster and specifying a different number or type of nodes for the cluster. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeResize>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_resize(
              ClusterIdentifier=\'string\'
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          The unique identifier of a cluster whose resize progress you are requesting. This parameter is case-sensitive.
        
          By default, resize operations for all clusters defined for an AWS account are returned.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TargetNodeType\': \'string\',
                \'TargetNumberOfNodes\': 123,
                \'TargetClusterType\': \'string\',
                \'Status\': \'string\',
                \'ImportTablesCompleted\': [
                    \'string\',
                ],
                \'ImportTablesInProgress\': [
                    \'string\',
                ],
                \'ImportTablesNotStarted\': [
                    \'string\',
                ],
                \'AvgResizeRateInMegaBytesPerSecond\': 123.0,
                \'TotalResizeDataInMegaBytes\': 123,
                \'ProgressInMegaBytes\': 123,
                \'ElapsedTimeInSeconds\': 123,
                \'EstimatedTimeToCompletionInSeconds\': 123,
                \'ResizeType\': \'string\',
                \'Message\': \'string\',
                \'TargetEncryptionType\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Describes the result of a cluster resize operation.
        
            - **TargetNodeType** *(string) --* 
        
              The node type that the cluster will have after the resize operation is complete.
        
            - **TargetNumberOfNodes** *(integer) --* 
        
              The number of nodes that the cluster will have after the resize operation is complete.
        
            - **TargetClusterType** *(string) --* 
        
              The cluster type after the resize operation is complete.
        
              Valid Values: ``multi-node`` | ``single-node``  
        
            - **Status** *(string) --* 
        
              The status of the resize operation.
        
              Valid Values: ``NONE`` | ``IN_PROGRESS`` | ``FAILED`` | ``SUCCEEDED``  
        
            - **ImportTablesCompleted** *(list) --* 
        
              The names of tables that have been completely imported .
        
              Valid Values: List of table names.
        
              - *(string) --* 
          
            - **ImportTablesInProgress** *(list) --* 
        
              The names of tables that are being currently imported.
        
              Valid Values: List of table names.
        
              - *(string) --* 
          
            - **ImportTablesNotStarted** *(list) --* 
        
              The names of tables that have not been yet imported.
        
              Valid Values: List of table names
        
              - *(string) --* 
          
            - **AvgResizeRateInMegaBytesPerSecond** *(float) --* 
        
              The average rate of the resize operation over the last few minutes, measured in megabytes per second. After the resize operation completes, this value shows the average rate of the entire resize operation.
        
            - **TotalResizeDataInMegaBytes** *(integer) --* 
        
              The estimated total amount of data, in megabytes, on the cluster before the resize operation began.
        
            - **ProgressInMegaBytes** *(integer) --* 
        
              While the resize operation is in progress, this value shows the current amount of data, in megabytes, that has been processed so far. When the resize operation is complete, this value shows the total amount of data, in megabytes, on the cluster, which may be more or less than TotalResizeDataInMegaBytes (the estimated total amount of data before resize).
        
            - **ElapsedTimeInSeconds** *(integer) --* 
        
              The amount of seconds that have elapsed since the resize operation began. After the resize operation completes, this value shows the total actual time, in seconds, for the resize operation.
        
            - **EstimatedTimeToCompletionInSeconds** *(integer) --* 
        
              The estimated time remaining, in seconds, until the resize operation is complete. This value is calculated based on the average resize rate and the estimated amount of data remaining to be processed. Once the resize operation is complete, this value will be 0.
        
            - **ResizeType** *(string) --* 
        
              An enum with possible values of ClassicResize and ElasticResize. These values describe the type of resize operation being performed. 
        
            - **Message** *(string) --* 
        
              An optional string to provide additional details about the resize action.
        
            - **TargetEncryptionType** *(string) --* 
        
              The type of encryption for the cluster after the resize is complete.
        
              Possible values are ``KMS`` and ``None`` . In the China region possible values are: ``Legacy`` and ``None`` .
        
        """
        pass

    def describe_snapshot_copy_grants(self, SnapshotCopyGrantName: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None) -> Dict:
        """
        
        For more information about managing snapshot copy grants, go to `Amazon Redshift Database Encryption <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html>`__ in the *Amazon Redshift Cluster Management Guide* . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeSnapshotCopyGrants>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_snapshot_copy_grants(
              SnapshotCopyGrantName=\'string\',
              MaxRecords=123,
              Marker=\'string\',
              TagKeys=[
                  \'string\',
              ],
              TagValues=[
                  \'string\',
              ]
          )
        :type SnapshotCopyGrantName: string
        :param SnapshotCopyGrantName: 
        
          The name of the snapshot copy grant.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
        
          Default: ``100``  
        
          Constraints: minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional parameter that specifies the starting point to return a set of response records. When the results of a ``DescribeSnapshotCopyGrant`` request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
          Constraints: You can specify either the **SnapshotCopyGrantName** parameter or the **Marker** parameter, but not both. 
        
        :type TagKeys: list
        :param TagKeys: 
        
          A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.
        
          - *(string) --* 
        
        :type TagValues: list
        :param TagValues: 
        
          A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'SnapshotCopyGrants\': [
                    {
                        \'SnapshotCopyGrantName\': \'string\',
                        \'KmsKeyId\': \'string\',
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              An optional parameter that specifies the starting point to return a set of response records. When the results of a ``DescribeSnapshotCopyGrant`` request exceed the value specified in ``MaxRecords`` , AWS returns a value in the ``Marker`` field of the response. You can retrieve the next set of response records by providing the returned marker value in the ``Marker`` parameter and retrying the request. 
        
              Constraints: You can specify either the **SnapshotCopyGrantName** parameter or the **Marker** parameter, but not both. 
        
            - **SnapshotCopyGrants** *(list) --* 
        
              The list of ``SnapshotCopyGrant`` objects.
        
              - *(dict) --* 
        
                The snapshot copy grant that grants Amazon Redshift permission to encrypt copied snapshots with the specified customer master key (CMK) from AWS KMS in the destination region.
        
                For more information about managing snapshot copy grants, go to `Amazon Redshift Database Encryption <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html>`__ in the *Amazon Redshift Cluster Management Guide* . 
        
                - **SnapshotCopyGrantName** *(string) --* 
        
                  The name of the snapshot copy grant.
        
                - **KmsKeyId** *(string) --* 
        
                  The unique identifier of the customer master key (CMK) in AWS KMS to which Amazon Redshift is granted permission.
        
                - **Tags** *(list) --* 
        
                  A list of tag instances.
        
                  - *(dict) --* 
        
                    A tag consisting of a name/value pair for a resource.
        
                    - **Key** *(string) --* 
        
                      The key, or name, for the resource tag.
        
                    - **Value** *(string) --* 
        
                      The value for the resource tag.
        
        """
        pass

    def describe_table_restore_status(self, ClusterIdentifier: str = None, TableRestoreRequestId: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeTableRestoreStatus>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_table_restore_status(
              ClusterIdentifier=\'string\',
              TableRestoreRequestId=\'string\',
              MaxRecords=123,
              Marker=\'string\'
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: 
        
          The Amazon Redshift cluster that the table is being restored to.
        
        :type TableRestoreRequestId: string
        :param TableRestoreRequestId: 
        
          The identifier of the table restore request to return status for. If you don\'t specify a ``TableRestoreRequestId`` value, then ``DescribeTableRestoreStatus`` returns the status of all in-progress table restore requests.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous ``DescribeTableRestoreStatus`` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the ``MaxRecords`` parameter.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TableRestoreStatusDetails\': [
                    {
                        \'TableRestoreRequestId\': \'string\',
                        \'Status\': \'PENDING\'|\'IN_PROGRESS\'|\'SUCCEEDED\'|\'FAILED\'|\'CANCELED\',
                        \'Message\': \'string\',
                        \'RequestTime\': datetime(2015, 1, 1),
                        \'ProgressInMegaBytes\': 123,
                        \'TotalDataInMegaBytes\': 123,
                        \'ClusterIdentifier\': \'string\',
                        \'SnapshotIdentifier\': \'string\',
                        \'SourceDatabaseName\': \'string\',
                        \'SourceSchemaName\': \'string\',
                        \'SourceTableName\': \'string\',
                        \'TargetDatabaseName\': \'string\',
                        \'TargetSchemaName\': \'string\',
                        \'NewTableName\': \'string\'
                    },
                ],
                \'Marker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **TableRestoreStatusDetails** *(list) --* 
        
              A list of status details for one or more table restore requests.
        
              - *(dict) --* 
        
                Describes the status of a  RestoreTableFromClusterSnapshot operation.
        
                - **TableRestoreRequestId** *(string) --* 
        
                  The unique identifier for the table restore request.
        
                - **Status** *(string) --* 
        
                  A value that describes the current state of the table restore request.
        
                  Valid Values: ``SUCCEEDED`` , ``FAILED`` , ``CANCELED`` , ``PENDING`` , ``IN_PROGRESS``  
        
                - **Message** *(string) --* 
        
                  A description of the status of the table restore request. Status values include ``SUCCEEDED`` , ``FAILED`` , ``CANCELED`` , ``PENDING`` , ``IN_PROGRESS`` .
        
                - **RequestTime** *(datetime) --* 
        
                  The time that the table restore request was made, in Universal Coordinated Time (UTC).
        
                - **ProgressInMegaBytes** *(integer) --* 
        
                  The amount of data restored to the new table so far, in megabytes (MB).
        
                - **TotalDataInMegaBytes** *(integer) --* 
        
                  The total amount of data to restore to the new table, in megabytes (MB).
        
                - **ClusterIdentifier** *(string) --* 
        
                  The identifier of the Amazon Redshift cluster that the table is being restored to.
        
                - **SnapshotIdentifier** *(string) --* 
        
                  The identifier of the snapshot that the table is being restored from.
        
                - **SourceDatabaseName** *(string) --* 
        
                  The name of the source database that contains the table being restored.
        
                - **SourceSchemaName** *(string) --* 
        
                  The name of the source schema that contains the table being restored.
        
                - **SourceTableName** *(string) --* 
        
                  The name of the source table being restored.
        
                - **TargetDatabaseName** *(string) --* 
        
                  The name of the database to restore the table to.
        
                - **TargetSchemaName** *(string) --* 
        
                  The name of the schema to restore the table to.
        
                - **NewTableName** *(string) --* 
        
                  The name of the table to create as a result of the table restore request.
        
            - **Marker** *(string) --* 
        
              A pagination token that can be used in a subsequent  DescribeTableRestoreStatus request.
        
        """
        pass

    def describe_tags(self, ResourceName: str = None, ResourceType: str = None, MaxRecords: int = None, Marker: str = None, TagKeys: List = None, TagValues: List = None) -> Dict:
        """
        
        The following are limitations for ``DescribeTags`` : 
        
        * You cannot specify an ARN and a resource-type value together in the same request. 
         
        * You cannot use the ``MaxRecords`` and ``Marker`` parameters together with the ARN parameter. 
         
        * The ``MaxRecords`` parameter can be a range from 10 to 50 results to return in a request. 
         
        If you specify both tag keys and tag values in the same request, Amazon Redshift returns all resources that match any combination of the specified keys and values. For example, if you have ``owner`` and ``environment`` for tag keys, and ``admin`` and ``test`` for tag values, all resources that have any combination of those values are returned.
        
        If both tag keys and values are omitted from the request, resources are returned regardless of whether they have tag keys or values associated with them.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_tags(
              ResourceName=\'string\',
              ResourceType=\'string\',
              MaxRecords=123,
              Marker=\'string\',
              TagKeys=[
                  \'string\',
              ],
              TagValues=[
                  \'string\',
              ]
          )
        :type ResourceName: string
        :param ResourceName: 
        
          The Amazon Resource Name (ARN) for which you want to describe the tag or tags. For example, ``arn:aws:redshift:us-east-1:123456789:cluster:t1`` . 
        
        :type ResourceType: string
        :param ResourceType: 
        
          The type of resource with which you want to view tags. Valid resource types are: 
        
          * Cluster 
           
          * CIDR/IP 
           
          * EC2 security group 
           
          * Snapshot 
           
          * Cluster security group 
           
          * Subnet group 
           
          * HSM connection 
           
          * HSM certificate 
           
          * Parameter group 
           
          * Snapshot copy grant 
           
          For more information about Amazon Redshift resource types and constructing ARNs, go to `Specifying Policy Elements\: Actions, Effects, Resources, and Principals <http://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-iam-access-control-specify-actions>`__ in the Amazon Redshift Cluster Management Guide. 
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number or response records to return in each call. If the number of remaining response records exceeds the specified ``MaxRecords`` value, a value is returned in a ``marker`` field of the response. You can retrieve the next set of records by retrying the command with the returned ``marker`` value. 
        
        :type Marker: string
        :param Marker: 
        
          A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the ``marker`` parameter and retrying the command. If the ``marker`` field is empty, all response records have been retrieved for the request. 
        
        :type TagKeys: list
        :param TagKeys: 
        
          A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.
        
          - *(string) --* 
        
        :type TagValues: list
        :param TagValues: 
        
          A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TaggedResources\': [
                    {
                        \'Tag\': {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                        \'ResourceName\': \'string\',
                        \'ResourceType\': \'string\'
                    },
                ],
                \'Marker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **TaggedResources** *(list) --* 
        
              A list of tags with their associated resources.
        
              - *(dict) --* 
        
                A tag and its associated resource.
        
                - **Tag** *(dict) --* 
        
                  The tag for the resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
                - **ResourceName** *(string) --* 
        
                  The Amazon Resource Name (ARN) with which the tag is associated. For example, ``arn:aws:redshift:us-east-1:123456789:cluster:t1`` .
        
                - **ResourceType** *(string) --* 
        
                  The type of resource with which the tag is associated. Valid resource types are: 
        
                  * Cluster 
                   
                  * CIDR/IP 
                   
                  * EC2 security group 
                   
                  * Snapshot 
                   
                  * Cluster security group 
                   
                  * Subnet group 
                   
                  * HSM connection 
                   
                  * HSM certificate 
                   
                  * Parameter group 
                   
                  For more information about Amazon Redshift resource types and constructing ARNs, go to `Constructing an Amazon Redshift Amazon Resource Name (ARN) <http://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-iam-access-control-specify-actions>`__ in the Amazon Redshift Cluster Management Guide. 
        
            - **Marker** *(string) --* 
        
              A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the ``Marker`` parameter and retrying the command. If the ``Marker`` field is empty, all response records have been retrieved for the request. 
        
        """
        pass

    def disable_logging(self, ClusterIdentifier: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DisableLogging>`_
        
        **Request Syntax** 
        ::
        
          response = client.disable_logging(
              ClusterIdentifier=\'string\'
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          The identifier of the cluster on which logging is to be stopped.
        
          Example: ``examplecluster``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'LoggingEnabled\': True|False,
                \'BucketName\': \'string\',
                \'S3KeyPrefix\': \'string\',
                \'LastSuccessfulDeliveryTime\': datetime(2015, 1, 1),
                \'LastFailureTime\': datetime(2015, 1, 1),
                \'LastFailureMessage\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Describes the status of logging for a cluster.
        
            - **LoggingEnabled** *(boolean) --* 
        
               ``true`` if logging is on, ``false`` if logging is off.
        
            - **BucketName** *(string) --* 
        
              The name of the S3 bucket where the log files are stored.
        
            - **S3KeyPrefix** *(string) --* 
        
              The prefix applied to the log file names.
        
            - **LastSuccessfulDeliveryTime** *(datetime) --* 
        
              The last time that logs were delivered.
        
            - **LastFailureTime** *(datetime) --* 
        
              The last time when logs failed to be delivered.
        
            - **LastFailureMessage** *(string) --* 
        
              The message indicating that logs failed to be delivered.
        
        """
        pass

    def disable_snapshot_copy(self, ClusterIdentifier: str) -> Dict:
        """
        
        If your cluster and its snapshots are encrypted using a customer master key (CMK) from AWS KMS, use  DeleteSnapshotCopyGrant to delete the grant that grants Amazon Redshift permission to the CMK in the destination region. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DisableSnapshotCopy>`_
        
        **Request Syntax** 
        ::
        
          response = client.disable_snapshot_copy(
              ClusterIdentifier=\'string\'
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          The unique identifier of the source cluster that you want to disable copying of snapshots to a destination region.
        
          Constraints: Must be the valid name of an existing cluster that has cross-region snapshot copy enabled.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
                    \'ClusterIdentifier\': \'string\',
                    \'NodeType\': \'string\',
                    \'ClusterStatus\': \'string\',
                    \'ModifyStatus\': \'string\',
                    \'MasterUsername\': \'string\',
                    \'DBName\': \'string\',
                    \'Endpoint\': {
                        \'Address\': \'string\',
                        \'Port\': 123
                    },
                    \'ClusterCreateTime\': datetime(2015, 1, 1),
                    \'AutomatedSnapshotRetentionPeriod\': 123,
                    \'ClusterSecurityGroups\': [
                        {
                            \'ClusterSecurityGroupName\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'VpcSecurityGroups\': [
                        {
                            \'VpcSecurityGroupId\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'ClusterParameterGroups\': [
                        {
                            \'ParameterGroupName\': \'string\',
                            \'ParameterApplyStatus\': \'string\',
                            \'ClusterParameterStatusList\': [
                                {
                                    \'ParameterName\': \'string\',
                                    \'ParameterApplyStatus\': \'string\',
                                    \'ParameterApplyErrorDescription\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'ClusterSubnetGroupName\': \'string\',
                    \'VpcId\': \'string\',
                    \'AvailabilityZone\': \'string\',
                    \'PreferredMaintenanceWindow\': \'string\',
                    \'PendingModifiedValues\': {
                        \'MasterUserPassword\': \'string\',
                        \'NodeType\': \'string\',
                        \'NumberOfNodes\': 123,
                        \'ClusterType\': \'string\',
                        \'ClusterVersion\': \'string\',
                        \'AutomatedSnapshotRetentionPeriod\': 123,
                        \'ClusterIdentifier\': \'string\',
                        \'PubliclyAccessible\': True|False,
                        \'EnhancedVpcRouting\': True|False,
                        \'MaintenanceTrackName\': \'string\',
                        \'EncryptionType\': \'string\'
                    },
                    \'ClusterVersion\': \'string\',
                    \'AllowVersionUpgrade\': True|False,
                    \'NumberOfNodes\': 123,
                    \'PubliclyAccessible\': True|False,
                    \'Encrypted\': True|False,
                    \'RestoreStatus\': {
                        \'Status\': \'string\',
                        \'CurrentRestoreRateInMegaBytesPerSecond\': 123.0,
                        \'SnapshotSizeInMegaBytes\': 123,
                        \'ProgressInMegaBytes\': 123,
                        \'ElapsedTimeInSeconds\': 123,
                        \'EstimatedTimeToCompletionInSeconds\': 123
                    },
                    \'HsmStatus\': {
                        \'HsmClientCertificateIdentifier\': \'string\',
                        \'HsmConfigurationIdentifier\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterSnapshotCopyStatus\': {
                        \'DestinationRegion\': \'string\',
                        \'RetentionPeriod\': 123,
                        \'SnapshotCopyGrantName\': \'string\'
                    },
                    \'ClusterPublicKey\': \'string\',
                    \'ClusterNodes\': [
                        {
                            \'NodeRole\': \'string\',
                            \'PrivateIPAddress\': \'string\',
                            \'PublicIPAddress\': \'string\'
                        },
                    ],
                    \'ElasticIpStatus\': {
                        \'ElasticIp\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterRevisionNumber\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'KmsKeyId\': \'string\',
                    \'EnhancedVpcRouting\': True|False,
                    \'IamRoles\': [
                        {
                            \'IamRoleArn\': \'string\',
                            \'ApplyStatus\': \'string\'
                        },
                    ],
                    \'PendingActions\': [
                        \'string\',
                    ],
                    \'MaintenanceTrackName\': \'string\',
                    \'ElasticResizeNumberOfNodeOptions\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              Describes a cluster.
        
              - **ClusterIdentifier** *(string) --* 
        
                The unique identifier of the cluster.
        
              - **NodeType** *(string) --* 
        
                The node type for the nodes in the cluster.
        
              - **ClusterStatus** *(string) --* 
        
                The current state of the cluster. Possible values are the following:
        
                * ``available``   
                 
                * ``creating``   
                 
                * ``deleting``   
                 
                * ``final-snapshot``   
                 
                * ``hardware-failure``   
                 
                * ``incompatible-hsm``   
                 
                * ``incompatible-network``   
                 
                * ``incompatible-parameters``   
                 
                * ``incompatible-restore``   
                 
                * ``modifying``   
                 
                * ``rebooting``   
                 
                * ``renaming``   
                 
                * ``resizing``   
                 
                * ``rotating-keys``   
                 
                * ``storage-full``   
                 
                * ``updating-hsm``   
                 
              - **ModifyStatus** *(string) --* 
        
                The status of a modify operation, if any, initiated for the cluster.
        
              - **MasterUsername** *(string) --* 
        
                The master user name for the cluster. This name is used to connect to the database that is specified in the **DBName** parameter. 
        
              - **DBName** *(string) --* 
        
                The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named ``dev`` dev was created by default. 
        
              - **Endpoint** *(dict) --* 
        
                The connection endpoint.
        
                - **Address** *(string) --* 
        
                  The DNS address of the Cluster.
        
                - **Port** *(integer) --* 
        
                  The port that the database engine is listening on.
        
              - **ClusterCreateTime** *(datetime) --* 
        
                The date and time that the cluster was created.
        
              - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                The number of days that automatic cluster snapshots are retained.
        
              - **ClusterSecurityGroups** *(list) --* 
        
                A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ``ClusterSecurityGroup.Name`` and ``ClusterSecurityGroup.Status`` subelements. 
        
                Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the **VpcSecurityGroups** parameter. 
        
                - *(dict) --* 
        
                  Describes a cluster security group.
        
                  - **ClusterSecurityGroupName** *(string) --* 
        
                    The name of the cluster security group.
        
                  - **Status** *(string) --* 
        
                    The status of the cluster security group.
        
              - **VpcSecurityGroups** *(list) --* 
        
                A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.
        
                - *(dict) --* 
        
                  Describes the members of a VPC security group.
        
                  - **VpcSecurityGroupId** *(string) --* 
        
                    The identifier of the VPC security group.
        
                  - **Status** *(string) --* 
        
                    The status of the VPC security group.
        
              - **ClusterParameterGroups** *(list) --* 
        
                The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.
        
                - *(dict) --* 
        
                  Describes the status of a parameter group.
        
                  - **ParameterGroupName** *(string) --* 
        
                    The name of the cluster parameter group.
        
                  - **ParameterApplyStatus** *(string) --* 
        
                    The status of parameter updates.
        
                  - **ClusterParameterStatusList** *(list) --* 
        
                    The list of parameter statuses.
        
                    For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
                    - *(dict) --* 
        
                      Describes the status of a parameter group.
        
                      - **ParameterName** *(string) --* 
        
                        The name of the parameter.
        
                      - **ParameterApplyStatus** *(string) --* 
        
                        The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
        
                        The following are possible statuses and descriptions.
        
                        * ``in-sync`` : The parameter value is in sync with the database. 
                         
                        * ``pending-reboot`` : The parameter value will be applied after the cluster reboots. 
                         
                        * ``applying`` : The parameter value is being applied to the database. 
                         
                        * ``invalid-parameter`` : Cannot apply the parameter value because it has an invalid value or syntax. 
                         
                        * ``apply-deferred`` : The parameter contains static property changes. The changes are deferred until the cluster reboots. 
                         
                        * ``apply-error`` : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots. 
                         
                        * ``unknown-error`` : Cannot apply the parameter change right now. The change will be applied after the cluster reboots. 
                         
                      - **ParameterApplyErrorDescription** *(string) --* 
        
                        The error that prevented the parameter from being applied to the database.
        
              - **ClusterSubnetGroupName** *(string) --* 
        
                The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.
        
              - **VpcId** *(string) --* 
        
                The identifier of the VPC the cluster is in, if the cluster is in a VPC.
        
              - **AvailabilityZone** *(string) --* 
        
                The name of the Availability Zone in which the cluster is located.
        
              - **PreferredMaintenanceWindow** *(string) --* 
        
                The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.
        
              - **PendingModifiedValues** *(dict) --* 
        
                A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.
        
                - **MasterUserPassword** *(string) --* 
        
                  The pending or in-progress change of the master user password for the cluster.
        
                - **NodeType** *(string) --* 
        
                  The pending or in-progress change of the cluster\'s node type.
        
                - **NumberOfNodes** *(integer) --* 
        
                  The pending or in-progress change of the number of nodes in the cluster.
        
                - **ClusterType** *(string) --* 
        
                  The pending or in-progress change of the cluster type.
        
                - **ClusterVersion** *(string) --* 
        
                  The pending or in-progress change of the service version.
        
                - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                  The pending or in-progress change of the automated snapshot retention period.
        
                - **ClusterIdentifier** *(string) --* 
        
                  The pending or in-progress change of the new identifier for the cluster.
        
                - **PubliclyAccessible** *(boolean) --* 
        
                  The pending or in-progress change of the ability to connect to the cluster from the public network.
        
                - **EnhancedVpcRouting** *(boolean) --* 
        
                  An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                  If this option is ``true`` , enhanced VPC routing is enabled. 
        
                  Default: false
        
                - **MaintenanceTrackName** *(string) --* 
        
                  The name of the maintenance track that the cluster will change to during the next maintenance window.
        
                - **EncryptionType** *(string) --* 
        
                  The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy. 
        
              - **ClusterVersion** *(string) --* 
        
                The version ID of the Amazon Redshift engine that is running on the cluster.
        
              - **AllowVersionUpgrade** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window. 
        
              - **NumberOfNodes** *(integer) --* 
        
                The number of compute nodes in the cluster.
        
              - **PubliclyAccessible** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that the cluster can be accessed from a public network.
        
              - **Encrypted** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that data in the cluster is encrypted at rest.
        
              - **RestoreStatus** *(dict) --* 
        
                A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.
        
                - **Status** *(string) --* 
        
                  The status of the restore action. Returns starting, restoring, completed, or failed.
        
                - **CurrentRestoreRateInMegaBytesPerSecond** *(float) --* 
        
                  The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.
        
                - **SnapshotSizeInMegaBytes** *(integer) --* 
        
                  The size of the set of snapshot data used to restore the cluster.
        
                - **ProgressInMegaBytes** *(integer) --* 
        
                  The number of megabytes that have been transferred from snapshot storage.
        
                - **ElapsedTimeInSeconds** *(integer) --* 
        
                  The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.
        
                - **EstimatedTimeToCompletionInSeconds** *(integer) --* 
        
                  The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore.
        
              - **HsmStatus** *(dict) --* 
        
                A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
        
                Values: active, applying
        
                - **HsmClientCertificateIdentifier** *(string) --* 
        
                  Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        
                - **HsmConfigurationIdentifier** *(string) --* 
        
                  Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        
                - **Status** *(string) --* 
        
                  Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
        
                  Values: active, applying
        
              - **ClusterSnapshotCopyStatus** *(dict) --* 
        
                A value that returns the destination region and retention period that are configured for cross-region snapshot copy.
        
                - **DestinationRegion** *(string) --* 
        
                  The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
        
                - **RetentionPeriod** *(integer) --* 
        
                  The number of days that automated snapshots are retained in the destination region after they are copied from a source region.
        
                - **SnapshotCopyGrantName** *(string) --* 
        
                  The name of the snapshot copy grant.
        
              - **ClusterPublicKey** *(string) --* 
        
                The public key for the cluster.
        
              - **ClusterNodes** *(list) --* 
        
                The nodes in the cluster.
        
                - *(dict) --* 
        
                  The identifier of a node in a cluster.
        
                  - **NodeRole** *(string) --* 
        
                    Whether the node is a leader node or a compute node.
        
                  - **PrivateIPAddress** *(string) --* 
        
                    The private IP address of a node within a cluster.
        
                  - **PublicIPAddress** *(string) --* 
        
                    The public IP address of a node within a cluster.
        
              - **ElasticIpStatus** *(dict) --* 
        
                The status of the elastic IP (EIP) address.
        
                - **ElasticIp** *(string) --* 
        
                  The elastic IP (EIP) address for the cluster.
        
                - **Status** *(string) --* 
        
                  The status of the elastic IP (EIP) address.
        
              - **ClusterRevisionNumber** *(string) --* 
        
                The specific revision number of the database in the cluster.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.
        
              - **EnhancedVpcRouting** *(boolean) --* 
        
                An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                If this option is ``true`` , enhanced VPC routing is enabled. 
        
                Default: false
        
              - **IamRoles** *(list) --* 
        
                A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.
        
                - *(dict) --* 
        
                  An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.
        
                  - **IamRoleArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the IAM role, for example, ``arn:aws:iam::123456789012:role/RedshiftCopyUnload`` . 
        
                  - **ApplyStatus** *(string) --* 
        
                    A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
        
                    The following are possible statuses and descriptions.
        
                    * ``in-sync`` : The role is available for use by the cluster. 
                     
                    * ``adding`` : The role is in the process of being associated with the cluster. 
                     
                    * ``removing`` : The role is in the process of being disassociated with the cluster. 
                     
              - **PendingActions** *(list) --* 
        
                Cluster operations that are waiting to be started.
        
                - *(string) --* 
            
              - **MaintenanceTrackName** *(string) --* 
        
                The name of the maintenance track for the cluster.
        
              - **ElasticResizeNumberOfNodeOptions** *(string) --* 
        
                Indicates the number of nodes the cluster can be resized to with the elastic resize method. 
        
        """
        pass

    def enable_logging(self, ClusterIdentifier: str, BucketName: str, S3KeyPrefix: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/EnableLogging>`_
        
        **Request Syntax** 
        ::
        
          response = client.enable_logging(
              ClusterIdentifier=\'string\',
              BucketName=\'string\',
              S3KeyPrefix=\'string\'
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          The identifier of the cluster on which logging is to be started.
        
          Example: ``examplecluster``  
        
        :type BucketName: string
        :param BucketName: **[REQUIRED]** 
        
          The name of an existing S3 bucket where the log files are to be stored.
        
          Constraints:
        
          * Must be in the same region as the cluster 
           
          * The cluster must have read bucket and put object permissions 
           
        :type S3KeyPrefix: string
        :param S3KeyPrefix: 
        
          The prefix applied to the log file names.
        
          Constraints:
        
          * Cannot exceed 512 characters 
           
          * Cannot contain spaces( ), double quotes (\"), single quotes (\'), a backslash (\), or control characters. The hexadecimal codes for invalid characters are:  
        
            * x00 to x20 
             
            * x22 
             
            * x27 
             
            * x5c 
             
            * x7f or larger 
             
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'LoggingEnabled\': True|False,
                \'BucketName\': \'string\',
                \'S3KeyPrefix\': \'string\',
                \'LastSuccessfulDeliveryTime\': datetime(2015, 1, 1),
                \'LastFailureTime\': datetime(2015, 1, 1),
                \'LastFailureMessage\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Describes the status of logging for a cluster.
        
            - **LoggingEnabled** *(boolean) --* 
        
               ``true`` if logging is on, ``false`` if logging is off.
        
            - **BucketName** *(string) --* 
        
              The name of the S3 bucket where the log files are stored.
        
            - **S3KeyPrefix** *(string) --* 
        
              The prefix applied to the log file names.
        
            - **LastSuccessfulDeliveryTime** *(datetime) --* 
        
              The last time that logs were delivered.
        
            - **LastFailureTime** *(datetime) --* 
        
              The last time when logs failed to be delivered.
        
            - **LastFailureMessage** *(string) --* 
        
              The message indicating that logs failed to be delivered.
        
        """
        pass

    def enable_snapshot_copy(self, ClusterIdentifier: str, DestinationRegion: str, RetentionPeriod: int = None, SnapshotCopyGrantName: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/EnableSnapshotCopy>`_
        
        **Request Syntax** 
        ::
        
          response = client.enable_snapshot_copy(
              ClusterIdentifier=\'string\',
              DestinationRegion=\'string\',
              RetentionPeriod=123,
              SnapshotCopyGrantName=\'string\'
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          The unique identifier of the source cluster to copy snapshots from.
        
          Constraints: Must be the valid name of an existing cluster that does not already have cross-region snapshot copy enabled.
        
        :type DestinationRegion: string
        :param DestinationRegion: **[REQUIRED]** 
        
          The destination region that you want to copy snapshots to.
        
          Constraints: Must be the name of a valid region. For more information, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html#redshift_region>`__ in the Amazon Web Services General Reference. 
        
        :type RetentionPeriod: integer
        :param RetentionPeriod: 
        
          The number of days to retain automated snapshots in the destination region after they are copied from the source region.
        
          Default: 7.
        
          Constraints: Must be at least 1 and no more than 35.
        
        :type SnapshotCopyGrantName: string
        :param SnapshotCopyGrantName: 
        
          The name of the snapshot copy grant to use when snapshots of an AWS KMS-encrypted cluster are copied to the destination region.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
                    \'ClusterIdentifier\': \'string\',
                    \'NodeType\': \'string\',
                    \'ClusterStatus\': \'string\',
                    \'ModifyStatus\': \'string\',
                    \'MasterUsername\': \'string\',
                    \'DBName\': \'string\',
                    \'Endpoint\': {
                        \'Address\': \'string\',
                        \'Port\': 123
                    },
                    \'ClusterCreateTime\': datetime(2015, 1, 1),
                    \'AutomatedSnapshotRetentionPeriod\': 123,
                    \'ClusterSecurityGroups\': [
                        {
                            \'ClusterSecurityGroupName\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'VpcSecurityGroups\': [
                        {
                            \'VpcSecurityGroupId\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'ClusterParameterGroups\': [
                        {
                            \'ParameterGroupName\': \'string\',
                            \'ParameterApplyStatus\': \'string\',
                            \'ClusterParameterStatusList\': [
                                {
                                    \'ParameterName\': \'string\',
                                    \'ParameterApplyStatus\': \'string\',
                                    \'ParameterApplyErrorDescription\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'ClusterSubnetGroupName\': \'string\',
                    \'VpcId\': \'string\',
                    \'AvailabilityZone\': \'string\',
                    \'PreferredMaintenanceWindow\': \'string\',
                    \'PendingModifiedValues\': {
                        \'MasterUserPassword\': \'string\',
                        \'NodeType\': \'string\',
                        \'NumberOfNodes\': 123,
                        \'ClusterType\': \'string\',
                        \'ClusterVersion\': \'string\',
                        \'AutomatedSnapshotRetentionPeriod\': 123,
                        \'ClusterIdentifier\': \'string\',
                        \'PubliclyAccessible\': True|False,
                        \'EnhancedVpcRouting\': True|False,
                        \'MaintenanceTrackName\': \'string\',
                        \'EncryptionType\': \'string\'
                    },
                    \'ClusterVersion\': \'string\',
                    \'AllowVersionUpgrade\': True|False,
                    \'NumberOfNodes\': 123,
                    \'PubliclyAccessible\': True|False,
                    \'Encrypted\': True|False,
                    \'RestoreStatus\': {
                        \'Status\': \'string\',
                        \'CurrentRestoreRateInMegaBytesPerSecond\': 123.0,
                        \'SnapshotSizeInMegaBytes\': 123,
                        \'ProgressInMegaBytes\': 123,
                        \'ElapsedTimeInSeconds\': 123,
                        \'EstimatedTimeToCompletionInSeconds\': 123
                    },
                    \'HsmStatus\': {
                        \'HsmClientCertificateIdentifier\': \'string\',
                        \'HsmConfigurationIdentifier\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterSnapshotCopyStatus\': {
                        \'DestinationRegion\': \'string\',
                        \'RetentionPeriod\': 123,
                        \'SnapshotCopyGrantName\': \'string\'
                    },
                    \'ClusterPublicKey\': \'string\',
                    \'ClusterNodes\': [
                        {
                            \'NodeRole\': \'string\',
                            \'PrivateIPAddress\': \'string\',
                            \'PublicIPAddress\': \'string\'
                        },
                    ],
                    \'ElasticIpStatus\': {
                        \'ElasticIp\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterRevisionNumber\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'KmsKeyId\': \'string\',
                    \'EnhancedVpcRouting\': True|False,
                    \'IamRoles\': [
                        {
                            \'IamRoleArn\': \'string\',
                            \'ApplyStatus\': \'string\'
                        },
                    ],
                    \'PendingActions\': [
                        \'string\',
                    ],
                    \'MaintenanceTrackName\': \'string\',
                    \'ElasticResizeNumberOfNodeOptions\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              Describes a cluster.
        
              - **ClusterIdentifier** *(string) --* 
        
                The unique identifier of the cluster.
        
              - **NodeType** *(string) --* 
        
                The node type for the nodes in the cluster.
        
              - **ClusterStatus** *(string) --* 
        
                The current state of the cluster. Possible values are the following:
        
                * ``available``   
                 
                * ``creating``   
                 
                * ``deleting``   
                 
                * ``final-snapshot``   
                 
                * ``hardware-failure``   
                 
                * ``incompatible-hsm``   
                 
                * ``incompatible-network``   
                 
                * ``incompatible-parameters``   
                 
                * ``incompatible-restore``   
                 
                * ``modifying``   
                 
                * ``rebooting``   
                 
                * ``renaming``   
                 
                * ``resizing``   
                 
                * ``rotating-keys``   
                 
                * ``storage-full``   
                 
                * ``updating-hsm``   
                 
              - **ModifyStatus** *(string) --* 
        
                The status of a modify operation, if any, initiated for the cluster.
        
              - **MasterUsername** *(string) --* 
        
                The master user name for the cluster. This name is used to connect to the database that is specified in the **DBName** parameter. 
        
              - **DBName** *(string) --* 
        
                The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named ``dev`` dev was created by default. 
        
              - **Endpoint** *(dict) --* 
        
                The connection endpoint.
        
                - **Address** *(string) --* 
        
                  The DNS address of the Cluster.
        
                - **Port** *(integer) --* 
        
                  The port that the database engine is listening on.
        
              - **ClusterCreateTime** *(datetime) --* 
        
                The date and time that the cluster was created.
        
              - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                The number of days that automatic cluster snapshots are retained.
        
              - **ClusterSecurityGroups** *(list) --* 
        
                A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ``ClusterSecurityGroup.Name`` and ``ClusterSecurityGroup.Status`` subelements. 
        
                Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the **VpcSecurityGroups** parameter. 
        
                - *(dict) --* 
        
                  Describes a cluster security group.
        
                  - **ClusterSecurityGroupName** *(string) --* 
        
                    The name of the cluster security group.
        
                  - **Status** *(string) --* 
        
                    The status of the cluster security group.
        
              - **VpcSecurityGroups** *(list) --* 
        
                A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.
        
                - *(dict) --* 
        
                  Describes the members of a VPC security group.
        
                  - **VpcSecurityGroupId** *(string) --* 
        
                    The identifier of the VPC security group.
        
                  - **Status** *(string) --* 
        
                    The status of the VPC security group.
        
              - **ClusterParameterGroups** *(list) --* 
        
                The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.
        
                - *(dict) --* 
        
                  Describes the status of a parameter group.
        
                  - **ParameterGroupName** *(string) --* 
        
                    The name of the cluster parameter group.
        
                  - **ParameterApplyStatus** *(string) --* 
        
                    The status of parameter updates.
        
                  - **ClusterParameterStatusList** *(list) --* 
        
                    The list of parameter statuses.
        
                    For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
                    - *(dict) --* 
        
                      Describes the status of a parameter group.
        
                      - **ParameterName** *(string) --* 
        
                        The name of the parameter.
        
                      - **ParameterApplyStatus** *(string) --* 
        
                        The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
        
                        The following are possible statuses and descriptions.
        
                        * ``in-sync`` : The parameter value is in sync with the database. 
                         
                        * ``pending-reboot`` : The parameter value will be applied after the cluster reboots. 
                         
                        * ``applying`` : The parameter value is being applied to the database. 
                         
                        * ``invalid-parameter`` : Cannot apply the parameter value because it has an invalid value or syntax. 
                         
                        * ``apply-deferred`` : The parameter contains static property changes. The changes are deferred until the cluster reboots. 
                         
                        * ``apply-error`` : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots. 
                         
                        * ``unknown-error`` : Cannot apply the parameter change right now. The change will be applied after the cluster reboots. 
                         
                      - **ParameterApplyErrorDescription** *(string) --* 
        
                        The error that prevented the parameter from being applied to the database.
        
              - **ClusterSubnetGroupName** *(string) --* 
        
                The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.
        
              - **VpcId** *(string) --* 
        
                The identifier of the VPC the cluster is in, if the cluster is in a VPC.
        
              - **AvailabilityZone** *(string) --* 
        
                The name of the Availability Zone in which the cluster is located.
        
              - **PreferredMaintenanceWindow** *(string) --* 
        
                The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.
        
              - **PendingModifiedValues** *(dict) --* 
        
                A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.
        
                - **MasterUserPassword** *(string) --* 
        
                  The pending or in-progress change of the master user password for the cluster.
        
                - **NodeType** *(string) --* 
        
                  The pending or in-progress change of the cluster\'s node type.
        
                - **NumberOfNodes** *(integer) --* 
        
                  The pending or in-progress change of the number of nodes in the cluster.
        
                - **ClusterType** *(string) --* 
        
                  The pending or in-progress change of the cluster type.
        
                - **ClusterVersion** *(string) --* 
        
                  The pending or in-progress change of the service version.
        
                - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                  The pending or in-progress change of the automated snapshot retention period.
        
                - **ClusterIdentifier** *(string) --* 
        
                  The pending or in-progress change of the new identifier for the cluster.
        
                - **PubliclyAccessible** *(boolean) --* 
        
                  The pending or in-progress change of the ability to connect to the cluster from the public network.
        
                - **EnhancedVpcRouting** *(boolean) --* 
        
                  An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                  If this option is ``true`` , enhanced VPC routing is enabled. 
        
                  Default: false
        
                - **MaintenanceTrackName** *(string) --* 
        
                  The name of the maintenance track that the cluster will change to during the next maintenance window.
        
                - **EncryptionType** *(string) --* 
        
                  The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy. 
        
              - **ClusterVersion** *(string) --* 
        
                The version ID of the Amazon Redshift engine that is running on the cluster.
        
              - **AllowVersionUpgrade** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window. 
        
              - **NumberOfNodes** *(integer) --* 
        
                The number of compute nodes in the cluster.
        
              - **PubliclyAccessible** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that the cluster can be accessed from a public network.
        
              - **Encrypted** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that data in the cluster is encrypted at rest.
        
              - **RestoreStatus** *(dict) --* 
        
                A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.
        
                - **Status** *(string) --* 
        
                  The status of the restore action. Returns starting, restoring, completed, or failed.
        
                - **CurrentRestoreRateInMegaBytesPerSecond** *(float) --* 
        
                  The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.
        
                - **SnapshotSizeInMegaBytes** *(integer) --* 
        
                  The size of the set of snapshot data used to restore the cluster.
        
                - **ProgressInMegaBytes** *(integer) --* 
        
                  The number of megabytes that have been transferred from snapshot storage.
        
                - **ElapsedTimeInSeconds** *(integer) --* 
        
                  The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.
        
                - **EstimatedTimeToCompletionInSeconds** *(integer) --* 
        
                  The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore.
        
              - **HsmStatus** *(dict) --* 
        
                A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
        
                Values: active, applying
        
                - **HsmClientCertificateIdentifier** *(string) --* 
        
                  Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        
                - **HsmConfigurationIdentifier** *(string) --* 
        
                  Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        
                - **Status** *(string) --* 
        
                  Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
        
                  Values: active, applying
        
              - **ClusterSnapshotCopyStatus** *(dict) --* 
        
                A value that returns the destination region and retention period that are configured for cross-region snapshot copy.
        
                - **DestinationRegion** *(string) --* 
        
                  The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
        
                - **RetentionPeriod** *(integer) --* 
        
                  The number of days that automated snapshots are retained in the destination region after they are copied from a source region.
        
                - **SnapshotCopyGrantName** *(string) --* 
        
                  The name of the snapshot copy grant.
        
              - **ClusterPublicKey** *(string) --* 
        
                The public key for the cluster.
        
              - **ClusterNodes** *(list) --* 
        
                The nodes in the cluster.
        
                - *(dict) --* 
        
                  The identifier of a node in a cluster.
        
                  - **NodeRole** *(string) --* 
        
                    Whether the node is a leader node or a compute node.
        
                  - **PrivateIPAddress** *(string) --* 
        
                    The private IP address of a node within a cluster.
        
                  - **PublicIPAddress** *(string) --* 
        
                    The public IP address of a node within a cluster.
        
              - **ElasticIpStatus** *(dict) --* 
        
                The status of the elastic IP (EIP) address.
        
                - **ElasticIp** *(string) --* 
        
                  The elastic IP (EIP) address for the cluster.
        
                - **Status** *(string) --* 
        
                  The status of the elastic IP (EIP) address.
        
              - **ClusterRevisionNumber** *(string) --* 
        
                The specific revision number of the database in the cluster.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.
        
              - **EnhancedVpcRouting** *(boolean) --* 
        
                An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                If this option is ``true`` , enhanced VPC routing is enabled. 
        
                Default: false
        
              - **IamRoles** *(list) --* 
        
                A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.
        
                - *(dict) --* 
        
                  An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.
        
                  - **IamRoleArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the IAM role, for example, ``arn:aws:iam::123456789012:role/RedshiftCopyUnload`` . 
        
                  - **ApplyStatus** *(string) --* 
        
                    A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
        
                    The following are possible statuses and descriptions.
        
                    * ``in-sync`` : The role is available for use by the cluster. 
                     
                    * ``adding`` : The role is in the process of being associated with the cluster. 
                     
                    * ``removing`` : The role is in the process of being disassociated with the cluster. 
                     
              - **PendingActions** *(list) --* 
        
                Cluster operations that are waiting to be started.
        
                - *(string) --* 
            
              - **MaintenanceTrackName** *(string) --* 
        
                The name of the maintenance track for the cluster.
        
              - **ElasticResizeNumberOfNodeOptions** *(string) --* 
        
                Indicates the number of nodes the cluster can be resized to with the elastic resize method. 
        
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

    def get_cluster_credentials(self, DbUser: str, ClusterIdentifier: str, DbName: str = None, DurationSeconds: int = None, AutoCreate: bool = None, DbGroups: List = None) -> Dict:
        """
        
        The AWS Identity and Access Management (IAM)user or role that executes GetClusterCredentials must have an IAM policy attached that allows access to all necessary actions and resources. For more information about permissions, see `Resource Policies for GetClusterCredentials <http://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html#redshift-policy-resources.getclustercredentials-resources>`__ in the Amazon Redshift Cluster Management Guide.
        
        If the ``DbGroups`` parameter is specified, the IAM policy must allow the ``redshift:JoinGroup`` action with access to the listed ``dbgroups`` . 
        
        In addition, if the ``AutoCreate`` parameter is set to ``True`` , then the policy must include the ``redshift:CreateClusterUser`` privilege.
        
        If the ``DbName`` parameter is specified, the IAM policy must allow access to the resource ``dbname`` for the specified database name. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/GetClusterCredentials>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_cluster_credentials(
              DbUser=\'string\',
              DbName=\'string\',
              ClusterIdentifier=\'string\',
              DurationSeconds=123,
              AutoCreate=True|False,
              DbGroups=[
                  \'string\',
              ]
          )
        :type DbUser: string
        :param DbUser: **[REQUIRED]** 
        
          The name of a database user. If a user name matching ``DbUser`` exists in the database, the temporary user credentials have the same permissions as the existing user. If ``DbUser`` doesn\'t exist in the database and ``Autocreate`` is ``True`` , a new user is created using the value for ``DbUser`` with PUBLIC permissions. If a database user matching the value for ``DbUser`` doesn\'t exist and ``Autocreate`` is ``False`` , then the command succeeds but the connection attempt will fail because the user doesn\'t exist in the database.
        
          For more information, see `CREATE USER <http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html>`__ in the Amazon Redshift Database Developer Guide. 
        
          Constraints:
        
          * Must be 1 to 64 alphanumeric characters or hyphens. The user name can\'t be ``PUBLIC`` . 
           
          * Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen. 
           
          * First character must be a letter. 
           
          * Must not contain a colon ( : ) or slash ( / ).  
           
          * Cannot be a reserved word. A list of reserved words can be found in `Reserved Words <http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`__ in the Amazon Redshift Database Developer Guide. 
           
        :type DbName: string
        :param DbName: 
        
          The name of a database that ``DbUser`` is authorized to log on to. If ``DbName`` is not specified, ``DbUser`` can log on to any existing database.
        
          Constraints:
        
          * Must be 1 to 64 alphanumeric characters or hyphens 
           
          * Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen. 
           
          * First character must be a letter. 
           
          * Must not contain a colon ( : ) or slash ( / ).  
           
          * Cannot be a reserved word. A list of reserved words can be found in `Reserved Words <http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`__ in the Amazon Redshift Database Developer Guide. 
           
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          The unique identifier of the cluster that contains the database for which your are requesting credentials. This parameter is case sensitive.
        
        :type DurationSeconds: integer
        :param DurationSeconds: 
        
          The number of seconds until the returned temporary password expires.
        
          Constraint: minimum 900, maximum 3600.
        
          Default: 900
        
        :type AutoCreate: boolean
        :param AutoCreate: 
        
          Create a database user with the name specified for the user named in ``DbUser`` if one does not exist.
        
        :type DbGroups: list
        :param DbGroups: 
        
          A list of the names of existing database groups that the user named in ``DbUser`` will join for the current session, in addition to any group memberships for an existing user. If not specified, a new user is added only to PUBLIC.
        
          Database group name constraints
        
          * Must be 1 to 64 alphanumeric characters or hyphens 
           
          * Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen. 
           
          * First character must be a letter. 
           
          * Must not contain a colon ( : ) or slash ( / ).  
           
          * Cannot be a reserved word. A list of reserved words can be found in `Reserved Words <http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`__ in the Amazon Redshift Database Developer Guide. 
           
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DbUser\': \'string\',
                \'DbPassword\': \'string\',
                \'Expiration\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Temporary credentials with authorization to log on to an Amazon Redshift database. 
        
            - **DbUser** *(string) --* 
        
              A database user name that is authorized to log on to the database ``DbName`` using the password ``DbPassword`` . If the specified DbUser exists in the database, the new user name has the same database privileges as the the user named in DbUser. By default, the user is added to PUBLIC. If the ``DbGroups`` parameter is specifed, ``DbUser`` is added to the listed groups for any sessions created using these credentials.
        
            - **DbPassword** *(string) --* 
        
              A temporary password that authorizes the user name returned by ``DbUser`` to log on to the database ``DbName`` . 
        
            - **Expiration** *(datetime) --* 
        
              The date and time the password in ``DbPassword`` expires.
        
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

    def get_reserved_node_exchange_offerings(self, ReservedNodeId: str, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/GetReservedNodeExchangeOfferings>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_reserved_node_exchange_offerings(
              ReservedNodeId=\'string\',
              MaxRecords=123,
              Marker=\'string\'
          )
        :type ReservedNodeId: string
        :param ReservedNodeId: **[REQUIRED]** 
        
          A string representing the node identifier for the DC1 Reserved Node to be exchanged.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          An integer setting the maximum number of ReservedNodeOfferings to retrieve.
        
        :type Marker: string
        :param Marker: 
        
          A value that indicates the starting point for the next set of ReservedNodeOfferings.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'ReservedNodeOfferings\': [
                    {
                        \'ReservedNodeOfferingId\': \'string\',
                        \'NodeType\': \'string\',
                        \'Duration\': 123,
                        \'FixedPrice\': 123.0,
                        \'UsagePrice\': 123.0,
                        \'CurrencyCode\': \'string\',
                        \'OfferingType\': \'string\',
                        \'RecurringCharges\': [
                            {
                                \'RecurringChargeAmount\': 123.0,
                                \'RecurringChargeFrequency\': \'string\'
                            },
                        ],
                        \'ReservedNodeOfferingType\': \'Regular\'|\'Upgradable\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Marker** *(string) --* 
        
              An optional parameter that specifies the starting point for returning a set of response records. When the results of a ``GetReservedNodeExchangeOfferings`` request exceed the value specified in MaxRecords, Amazon Redshift returns a value in the marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the marker parameter and retrying the request. 
        
            - **ReservedNodeOfferings** *(list) --* 
        
              Returns an array of  ReservedNodeOffering objects.
        
              - *(dict) --* 
        
                Describes a reserved node offering.
        
                - **ReservedNodeOfferingId** *(string) --* 
        
                  The offering identifier.
        
                - **NodeType** *(string) --* 
        
                  The node type offered by the reserved node offering.
        
                - **Duration** *(integer) --* 
        
                  The duration, in seconds, for which the offering will reserve the node.
        
                - **FixedPrice** *(float) --* 
        
                  The upfront fixed charge you will pay to purchase the specific reserved node offering.
        
                - **UsagePrice** *(float) --* 
        
                  The rate you are charged for each hour the cluster that is using the offering is running.
        
                - **CurrencyCode** *(string) --* 
        
                  The currency code for the compute nodes offering.
        
                - **OfferingType** *(string) --* 
        
                  The anticipated utilization of the reserved node, as defined in the reserved node offering.
        
                - **RecurringCharges** *(list) --* 
        
                  The charge to your account regardless of whether you are creating any clusters using the node offering. Recurring charges are only in effect for heavy-utilization reserved nodes.
        
                  - *(dict) --* 
        
                    Describes a recurring charge.
        
                    - **RecurringChargeAmount** *(float) --* 
        
                      The amount charged per the period of time specified by the recurring charge frequency.
        
                    - **RecurringChargeFrequency** *(string) --* 
        
                      The frequency at which the recurring charge amount is applied.
        
                - **ReservedNodeOfferingType** *(string) --* 
            
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

    def modify_cluster(self, ClusterIdentifier: str, ClusterType: str = None, NodeType: str = None, NumberOfNodes: int = None, ClusterSecurityGroups: List = None, VpcSecurityGroupIds: List = None, MasterUserPassword: str = None, ClusterParameterGroupName: str = None, AutomatedSnapshotRetentionPeriod: int = None, PreferredMaintenanceWindow: str = None, ClusterVersion: str = None, AllowVersionUpgrade: bool = None, HsmClientCertificateIdentifier: str = None, HsmConfigurationIdentifier: str = None, NewClusterIdentifier: str = None, PubliclyAccessible: bool = None, ElasticIp: str = None, EnhancedVpcRouting: bool = None, MaintenanceTrackName: str = None, Encrypted: bool = None, KmsKeyId: str = None) -> Dict:
        """
        
        You can also change node type and the number of nodes to scale up or down the cluster. When resizing a cluster, you must specify both the number of nodes and the node type even if one of the parameters does not change.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/ModifyCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_cluster(
              ClusterIdentifier=\'string\',
              ClusterType=\'string\',
              NodeType=\'string\',
              NumberOfNodes=123,
              ClusterSecurityGroups=[
                  \'string\',
              ],
              VpcSecurityGroupIds=[
                  \'string\',
              ],
              MasterUserPassword=\'string\',
              ClusterParameterGroupName=\'string\',
              AutomatedSnapshotRetentionPeriod=123,
              PreferredMaintenanceWindow=\'string\',
              ClusterVersion=\'string\',
              AllowVersionUpgrade=True|False,
              HsmClientCertificateIdentifier=\'string\',
              HsmConfigurationIdentifier=\'string\',
              NewClusterIdentifier=\'string\',
              PubliclyAccessible=True|False,
              ElasticIp=\'string\',
              EnhancedVpcRouting=True|False,
              MaintenanceTrackName=\'string\',
              Encrypted=True|False,
              KmsKeyId=\'string\'
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          The unique identifier of the cluster to be modified.
        
          Example: ``examplecluster``  
        
        :type ClusterType: string
        :param ClusterType: 
        
          The new cluster type.
        
          When you submit your cluster resize request, your existing cluster goes into a read-only mode. After Amazon Redshift provisions a new cluster based on your resize requirements, there will be outage for a period while the old cluster is deleted and your connection is switched to the new cluster. You can use  DescribeResize to track the progress of the resize request. 
        
          Valid Values: ``multi-node | single-node``  
        
        :type NodeType: string
        :param NodeType: 
        
          The new node type of the cluster. If you specify a new node type, you must also specify the number of nodes parameter.
        
          When you submit your request to resize a cluster, Amazon Redshift sets access permissions for the cluster to read-only. After Amazon Redshift provisions a new cluster according to your resize requirements, there will be a temporary outage while the old cluster is deleted and your connection is switched to the new cluster. When the new connection is complete, the original access permissions for the cluster are restored. You can use  DescribeResize to track the progress of the resize request. 
        
          Valid Values: ``ds2.xlarge`` | ``ds2.8xlarge`` | ``dc1.large`` | ``dc1.8xlarge`` | ``dc2.large`` | ``dc2.8xlarge``  
        
        :type NumberOfNodes: integer
        :param NumberOfNodes: 
        
          The new number of nodes of the cluster. If you specify a new number of nodes, you must also specify the node type parameter.
        
          When you submit your request to resize a cluster, Amazon Redshift sets access permissions for the cluster to read-only. After Amazon Redshift provisions a new cluster according to your resize requirements, there will be a temporary outage while the old cluster is deleted and your connection is switched to the new cluster. When the new connection is complete, the original access permissions for the cluster are restored. You can use  DescribeResize to track the progress of the resize request. 
        
          Valid Values: Integer greater than ``0`` .
        
        :type ClusterSecurityGroups: list
        :param ClusterSecurityGroups: 
        
          A list of cluster security groups to be authorized on this cluster. This change is asynchronously applied as soon as possible.
        
          Security groups currently associated with the cluster, and not in the list of groups to apply, will be revoked from the cluster.
        
          Constraints:
        
          * Must be 1 to 255 alphanumeric characters or hyphens 
           
          * First character must be a letter 
           
          * Cannot end with a hyphen or contain two consecutive hyphens 
           
          - *(string) --* 
        
        :type VpcSecurityGroupIds: list
        :param VpcSecurityGroupIds: 
        
          A list of virtual private cloud (VPC) security groups to be associated with the cluster. This change is asynchronously applied as soon as possible.
        
          - *(string) --* 
        
        :type MasterUserPassword: string
        :param MasterUserPassword: 
        
          The new password for the cluster master user. This change is asynchronously applied as soon as possible. Between the time of the request and the completion of the request, the ``MasterUserPassword`` element exists in the ``PendingModifiedValues`` element of the operation response. 
        
          .. note::
        
            Operations never return the password, so this operation provides a way to regain access to the master user account for a cluster if the password is lost.
        
          Default: Uses existing setting.
        
          Constraints:
        
          * Must be between 8 and 64 characters in length. 
           
          * Must contain at least one uppercase letter. 
           
          * Must contain at least one lowercase letter. 
           
          * Must contain one number. 
           
          * Can be any printable ASCII character (ASCII code 33 to 126) except \' (single quote), \" (double quote), \, /, @, or space. 
           
        :type ClusterParameterGroupName: string
        :param ClusterParameterGroupName: 
        
          The name of the cluster parameter group to apply to this cluster. This change is applied only after the cluster is rebooted. To reboot a cluster use  RebootCluster . 
        
          Default: Uses existing setting.
        
          Constraints: The cluster parameter group must be in the same parameter group family that matches the cluster version.
        
        :type AutomatedSnapshotRetentionPeriod: integer
        :param AutomatedSnapshotRetentionPeriod: 
        
          The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with  CreateClusterSnapshot . 
        
          If you decrease the automated snapshot retention period from its current value, existing automated snapshots that fall outside of the new retention period will be immediately deleted.
        
          Default: Uses existing setting.
        
          Constraints: Must be a value from 0 to 35.
        
        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow: 
        
          The weekly time range (in UTC) during which system maintenance can occur, if necessary. If system maintenance is necessary during the window, it may result in an outage.
        
          This maintenance window change is made immediately. If the new maintenance window indicates the current time, there must be at least 120 minutes between the current time and end of the window in order to ensure that pending changes are applied.
        
          Default: Uses existing setting.
        
          Format: ddd:hh24:mi-ddd:hh24:mi, for example ``wed:07:30-wed:08:00`` .
        
          Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun
        
          Constraints: Must be at least 30 minutes.
        
        :type ClusterVersion: string
        :param ClusterVersion: 
        
          The new version number of the Amazon Redshift engine to upgrade to.
        
          For major version upgrades, if a non-default cluster parameter group is currently in use, a new cluster parameter group in the cluster parameter group family for the new version must be specified. The new cluster parameter group can be the default for that cluster parameter group family. For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
          Example: ``1.0``  
        
        :type AllowVersionUpgrade: boolean
        :param AllowVersionUpgrade: 
        
          If ``true`` , major version upgrades will be applied automatically to the cluster during the maintenance window. 
        
          Default: ``false``  
        
        :type HsmClientCertificateIdentifier: string
        :param HsmClientCertificateIdentifier: 
        
          Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        
        :type HsmConfigurationIdentifier: string
        :param HsmConfigurationIdentifier: 
        
          Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        
        :type NewClusterIdentifier: string
        :param NewClusterIdentifier: 
        
          The new identifier for the cluster.
        
          Constraints:
        
          * Must contain from 1 to 63 alphanumeric characters or hyphens. 
           
          * Alphabetic characters must be lowercase. 
           
          * First character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
          * Must be unique for all clusters within an AWS account. 
           
          Example: ``examplecluster``  
        
        :type PubliclyAccessible: boolean
        :param PubliclyAccessible: 
        
          If ``true`` , the cluster can be accessed from a public network. Only clusters in VPCs can be set to be publicly available.
        
        :type ElasticIp: string
        :param ElasticIp: 
        
          The Elastic IP (EIP) address for the cluster.
        
          Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. For more information about provisioning clusters in EC2-VPC, go to `Supported Platforms to Launch Your Cluster <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms>`__ in the Amazon Redshift Cluster Management Guide.
        
        :type EnhancedVpcRouting: boolean
        :param EnhancedVpcRouting: 
        
          An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
          If this option is ``true`` , enhanced VPC routing is enabled. 
        
          Default: false
        
        :type MaintenanceTrackName: string
        :param MaintenanceTrackName: 
        
          The name for the maintenance track that you want to assign for the cluster. This name change is asynchronous. The new track name stays in the ``PendingModifiedValues`` for the cluster until the next maintenance window. When the maintenance track changes, the cluster is switched to the latest cluster release available for the maintenance track. At this point, the maintenance track name is applied.
        
        :type Encrypted: boolean
        :param Encrypted: 
        
          Indicates whether the cluster is encrypted. If the cluster is encrypted and you provide a value for the ``KmsKeyId`` parameter, we will encrypt the cluster with the provided ``KmsKeyId`` . If you don\'t provide a ``KmsKeyId`` , we will encrypt with the default key. In the China region we will use legacy encryption if you specify that the cluster is encrypted.
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
                    \'ClusterIdentifier\': \'string\',
                    \'NodeType\': \'string\',
                    \'ClusterStatus\': \'string\',
                    \'ModifyStatus\': \'string\',
                    \'MasterUsername\': \'string\',
                    \'DBName\': \'string\',
                    \'Endpoint\': {
                        \'Address\': \'string\',
                        \'Port\': 123
                    },
                    \'ClusterCreateTime\': datetime(2015, 1, 1),
                    \'AutomatedSnapshotRetentionPeriod\': 123,
                    \'ClusterSecurityGroups\': [
                        {
                            \'ClusterSecurityGroupName\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'VpcSecurityGroups\': [
                        {
                            \'VpcSecurityGroupId\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'ClusterParameterGroups\': [
                        {
                            \'ParameterGroupName\': \'string\',
                            \'ParameterApplyStatus\': \'string\',
                            \'ClusterParameterStatusList\': [
                                {
                                    \'ParameterName\': \'string\',
                                    \'ParameterApplyStatus\': \'string\',
                                    \'ParameterApplyErrorDescription\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'ClusterSubnetGroupName\': \'string\',
                    \'VpcId\': \'string\',
                    \'AvailabilityZone\': \'string\',
                    \'PreferredMaintenanceWindow\': \'string\',
                    \'PendingModifiedValues\': {
                        \'MasterUserPassword\': \'string\',
                        \'NodeType\': \'string\',
                        \'NumberOfNodes\': 123,
                        \'ClusterType\': \'string\',
                        \'ClusterVersion\': \'string\',
                        \'AutomatedSnapshotRetentionPeriod\': 123,
                        \'ClusterIdentifier\': \'string\',
                        \'PubliclyAccessible\': True|False,
                        \'EnhancedVpcRouting\': True|False,
                        \'MaintenanceTrackName\': \'string\',
                        \'EncryptionType\': \'string\'
                    },
                    \'ClusterVersion\': \'string\',
                    \'AllowVersionUpgrade\': True|False,
                    \'NumberOfNodes\': 123,
                    \'PubliclyAccessible\': True|False,
                    \'Encrypted\': True|False,
                    \'RestoreStatus\': {
                        \'Status\': \'string\',
                        \'CurrentRestoreRateInMegaBytesPerSecond\': 123.0,
                        \'SnapshotSizeInMegaBytes\': 123,
                        \'ProgressInMegaBytes\': 123,
                        \'ElapsedTimeInSeconds\': 123,
                        \'EstimatedTimeToCompletionInSeconds\': 123
                    },
                    \'HsmStatus\': {
                        \'HsmClientCertificateIdentifier\': \'string\',
                        \'HsmConfigurationIdentifier\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterSnapshotCopyStatus\': {
                        \'DestinationRegion\': \'string\',
                        \'RetentionPeriod\': 123,
                        \'SnapshotCopyGrantName\': \'string\'
                    },
                    \'ClusterPublicKey\': \'string\',
                    \'ClusterNodes\': [
                        {
                            \'NodeRole\': \'string\',
                            \'PrivateIPAddress\': \'string\',
                            \'PublicIPAddress\': \'string\'
                        },
                    ],
                    \'ElasticIpStatus\': {
                        \'ElasticIp\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterRevisionNumber\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'KmsKeyId\': \'string\',
                    \'EnhancedVpcRouting\': True|False,
                    \'IamRoles\': [
                        {
                            \'IamRoleArn\': \'string\',
                            \'ApplyStatus\': \'string\'
                        },
                    ],
                    \'PendingActions\': [
                        \'string\',
                    ],
                    \'MaintenanceTrackName\': \'string\',
                    \'ElasticResizeNumberOfNodeOptions\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              Describes a cluster.
        
              - **ClusterIdentifier** *(string) --* 
        
                The unique identifier of the cluster.
        
              - **NodeType** *(string) --* 
        
                The node type for the nodes in the cluster.
        
              - **ClusterStatus** *(string) --* 
        
                The current state of the cluster. Possible values are the following:
        
                * ``available``   
                 
                * ``creating``   
                 
                * ``deleting``   
                 
                * ``final-snapshot``   
                 
                * ``hardware-failure``   
                 
                * ``incompatible-hsm``   
                 
                * ``incompatible-network``   
                 
                * ``incompatible-parameters``   
                 
                * ``incompatible-restore``   
                 
                * ``modifying``   
                 
                * ``rebooting``   
                 
                * ``renaming``   
                 
                * ``resizing``   
                 
                * ``rotating-keys``   
                 
                * ``storage-full``   
                 
                * ``updating-hsm``   
                 
              - **ModifyStatus** *(string) --* 
        
                The status of a modify operation, if any, initiated for the cluster.
        
              - **MasterUsername** *(string) --* 
        
                The master user name for the cluster. This name is used to connect to the database that is specified in the **DBName** parameter. 
        
              - **DBName** *(string) --* 
        
                The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named ``dev`` dev was created by default. 
        
              - **Endpoint** *(dict) --* 
        
                The connection endpoint.
        
                - **Address** *(string) --* 
        
                  The DNS address of the Cluster.
        
                - **Port** *(integer) --* 
        
                  The port that the database engine is listening on.
        
              - **ClusterCreateTime** *(datetime) --* 
        
                The date and time that the cluster was created.
        
              - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                The number of days that automatic cluster snapshots are retained.
        
              - **ClusterSecurityGroups** *(list) --* 
        
                A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ``ClusterSecurityGroup.Name`` and ``ClusterSecurityGroup.Status`` subelements. 
        
                Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the **VpcSecurityGroups** parameter. 
        
                - *(dict) --* 
        
                  Describes a cluster security group.
        
                  - **ClusterSecurityGroupName** *(string) --* 
        
                    The name of the cluster security group.
        
                  - **Status** *(string) --* 
        
                    The status of the cluster security group.
        
              - **VpcSecurityGroups** *(list) --* 
        
                A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.
        
                - *(dict) --* 
        
                  Describes the members of a VPC security group.
        
                  - **VpcSecurityGroupId** *(string) --* 
        
                    The identifier of the VPC security group.
        
                  - **Status** *(string) --* 
        
                    The status of the VPC security group.
        
              - **ClusterParameterGroups** *(list) --* 
        
                The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.
        
                - *(dict) --* 
        
                  Describes the status of a parameter group.
        
                  - **ParameterGroupName** *(string) --* 
        
                    The name of the cluster parameter group.
        
                  - **ParameterApplyStatus** *(string) --* 
        
                    The status of parameter updates.
        
                  - **ClusterParameterStatusList** *(list) --* 
        
                    The list of parameter statuses.
        
                    For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
                    - *(dict) --* 
        
                      Describes the status of a parameter group.
        
                      - **ParameterName** *(string) --* 
        
                        The name of the parameter.
        
                      - **ParameterApplyStatus** *(string) --* 
        
                        The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
        
                        The following are possible statuses and descriptions.
        
                        * ``in-sync`` : The parameter value is in sync with the database. 
                         
                        * ``pending-reboot`` : The parameter value will be applied after the cluster reboots. 
                         
                        * ``applying`` : The parameter value is being applied to the database. 
                         
                        * ``invalid-parameter`` : Cannot apply the parameter value because it has an invalid value or syntax. 
                         
                        * ``apply-deferred`` : The parameter contains static property changes. The changes are deferred until the cluster reboots. 
                         
                        * ``apply-error`` : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots. 
                         
                        * ``unknown-error`` : Cannot apply the parameter change right now. The change will be applied after the cluster reboots. 
                         
                      - **ParameterApplyErrorDescription** *(string) --* 
        
                        The error that prevented the parameter from being applied to the database.
        
              - **ClusterSubnetGroupName** *(string) --* 
        
                The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.
        
              - **VpcId** *(string) --* 
        
                The identifier of the VPC the cluster is in, if the cluster is in a VPC.
        
              - **AvailabilityZone** *(string) --* 
        
                The name of the Availability Zone in which the cluster is located.
        
              - **PreferredMaintenanceWindow** *(string) --* 
        
                The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.
        
              - **PendingModifiedValues** *(dict) --* 
        
                A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.
        
                - **MasterUserPassword** *(string) --* 
        
                  The pending or in-progress change of the master user password for the cluster.
        
                - **NodeType** *(string) --* 
        
                  The pending or in-progress change of the cluster\'s node type.
        
                - **NumberOfNodes** *(integer) --* 
        
                  The pending or in-progress change of the number of nodes in the cluster.
        
                - **ClusterType** *(string) --* 
        
                  The pending or in-progress change of the cluster type.
        
                - **ClusterVersion** *(string) --* 
        
                  The pending or in-progress change of the service version.
        
                - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                  The pending or in-progress change of the automated snapshot retention period.
        
                - **ClusterIdentifier** *(string) --* 
        
                  The pending or in-progress change of the new identifier for the cluster.
        
                - **PubliclyAccessible** *(boolean) --* 
        
                  The pending or in-progress change of the ability to connect to the cluster from the public network.
        
                - **EnhancedVpcRouting** *(boolean) --* 
        
                  An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                  If this option is ``true`` , enhanced VPC routing is enabled. 
        
                  Default: false
        
                - **MaintenanceTrackName** *(string) --* 
        
                  The name of the maintenance track that the cluster will change to during the next maintenance window.
        
                - **EncryptionType** *(string) --* 
        
                  The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy. 
        
              - **ClusterVersion** *(string) --* 
        
                The version ID of the Amazon Redshift engine that is running on the cluster.
        
              - **AllowVersionUpgrade** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window. 
        
              - **NumberOfNodes** *(integer) --* 
        
                The number of compute nodes in the cluster.
        
              - **PubliclyAccessible** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that the cluster can be accessed from a public network.
        
              - **Encrypted** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that data in the cluster is encrypted at rest.
        
              - **RestoreStatus** *(dict) --* 
        
                A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.
        
                - **Status** *(string) --* 
        
                  The status of the restore action. Returns starting, restoring, completed, or failed.
        
                - **CurrentRestoreRateInMegaBytesPerSecond** *(float) --* 
        
                  The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.
        
                - **SnapshotSizeInMegaBytes** *(integer) --* 
        
                  The size of the set of snapshot data used to restore the cluster.
        
                - **ProgressInMegaBytes** *(integer) --* 
        
                  The number of megabytes that have been transferred from snapshot storage.
        
                - **ElapsedTimeInSeconds** *(integer) --* 
        
                  The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.
        
                - **EstimatedTimeToCompletionInSeconds** *(integer) --* 
        
                  The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore.
        
              - **HsmStatus** *(dict) --* 
        
                A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
        
                Values: active, applying
        
                - **HsmClientCertificateIdentifier** *(string) --* 
        
                  Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        
                - **HsmConfigurationIdentifier** *(string) --* 
        
                  Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        
                - **Status** *(string) --* 
        
                  Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
        
                  Values: active, applying
        
              - **ClusterSnapshotCopyStatus** *(dict) --* 
        
                A value that returns the destination region and retention period that are configured for cross-region snapshot copy.
        
                - **DestinationRegion** *(string) --* 
        
                  The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
        
                - **RetentionPeriod** *(integer) --* 
        
                  The number of days that automated snapshots are retained in the destination region after they are copied from a source region.
        
                - **SnapshotCopyGrantName** *(string) --* 
        
                  The name of the snapshot copy grant.
        
              - **ClusterPublicKey** *(string) --* 
        
                The public key for the cluster.
        
              - **ClusterNodes** *(list) --* 
        
                The nodes in the cluster.
        
                - *(dict) --* 
        
                  The identifier of a node in a cluster.
        
                  - **NodeRole** *(string) --* 
        
                    Whether the node is a leader node or a compute node.
        
                  - **PrivateIPAddress** *(string) --* 
        
                    The private IP address of a node within a cluster.
        
                  - **PublicIPAddress** *(string) --* 
        
                    The public IP address of a node within a cluster.
        
              - **ElasticIpStatus** *(dict) --* 
        
                The status of the elastic IP (EIP) address.
        
                - **ElasticIp** *(string) --* 
        
                  The elastic IP (EIP) address for the cluster.
        
                - **Status** *(string) --* 
        
                  The status of the elastic IP (EIP) address.
        
              - **ClusterRevisionNumber** *(string) --* 
        
                The specific revision number of the database in the cluster.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.
        
              - **EnhancedVpcRouting** *(boolean) --* 
        
                An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                If this option is ``true`` , enhanced VPC routing is enabled. 
        
                Default: false
        
              - **IamRoles** *(list) --* 
        
                A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.
        
                - *(dict) --* 
        
                  An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.
        
                  - **IamRoleArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the IAM role, for example, ``arn:aws:iam::123456789012:role/RedshiftCopyUnload`` . 
        
                  - **ApplyStatus** *(string) --* 
        
                    A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
        
                    The following are possible statuses and descriptions.
        
                    * ``in-sync`` : The role is available for use by the cluster. 
                     
                    * ``adding`` : The role is in the process of being associated with the cluster. 
                     
                    * ``removing`` : The role is in the process of being disassociated with the cluster. 
                     
              - **PendingActions** *(list) --* 
        
                Cluster operations that are waiting to be started.
        
                - *(string) --* 
            
              - **MaintenanceTrackName** *(string) --* 
        
                The name of the maintenance track for the cluster.
        
              - **ElasticResizeNumberOfNodeOptions** *(string) --* 
        
                Indicates the number of nodes the cluster can be resized to with the elastic resize method. 
        
        """
        pass

    def modify_cluster_db_revision(self, ClusterIdentifier: str, RevisionTarget: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/ModifyClusterDbRevision>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_cluster_db_revision(
              ClusterIdentifier=\'string\',
              RevisionTarget=\'string\'
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          The unique identifier of a cluster whose database revision you want to modify. 
        
          Example: ``examplecluster``  
        
        :type RevisionTarget: string
        :param RevisionTarget: **[REQUIRED]** 
        
          The identifier of the database revision. You can retrieve this value from the response to the  DescribeClusterDbRevisions request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
                    \'ClusterIdentifier\': \'string\',
                    \'NodeType\': \'string\',
                    \'ClusterStatus\': \'string\',
                    \'ModifyStatus\': \'string\',
                    \'MasterUsername\': \'string\',
                    \'DBName\': \'string\',
                    \'Endpoint\': {
                        \'Address\': \'string\',
                        \'Port\': 123
                    },
                    \'ClusterCreateTime\': datetime(2015, 1, 1),
                    \'AutomatedSnapshotRetentionPeriod\': 123,
                    \'ClusterSecurityGroups\': [
                        {
                            \'ClusterSecurityGroupName\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'VpcSecurityGroups\': [
                        {
                            \'VpcSecurityGroupId\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'ClusterParameterGroups\': [
                        {
                            \'ParameterGroupName\': \'string\',
                            \'ParameterApplyStatus\': \'string\',
                            \'ClusterParameterStatusList\': [
                                {
                                    \'ParameterName\': \'string\',
                                    \'ParameterApplyStatus\': \'string\',
                                    \'ParameterApplyErrorDescription\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'ClusterSubnetGroupName\': \'string\',
                    \'VpcId\': \'string\',
                    \'AvailabilityZone\': \'string\',
                    \'PreferredMaintenanceWindow\': \'string\',
                    \'PendingModifiedValues\': {
                        \'MasterUserPassword\': \'string\',
                        \'NodeType\': \'string\',
                        \'NumberOfNodes\': 123,
                        \'ClusterType\': \'string\',
                        \'ClusterVersion\': \'string\',
                        \'AutomatedSnapshotRetentionPeriod\': 123,
                        \'ClusterIdentifier\': \'string\',
                        \'PubliclyAccessible\': True|False,
                        \'EnhancedVpcRouting\': True|False,
                        \'MaintenanceTrackName\': \'string\',
                        \'EncryptionType\': \'string\'
                    },
                    \'ClusterVersion\': \'string\',
                    \'AllowVersionUpgrade\': True|False,
                    \'NumberOfNodes\': 123,
                    \'PubliclyAccessible\': True|False,
                    \'Encrypted\': True|False,
                    \'RestoreStatus\': {
                        \'Status\': \'string\',
                        \'CurrentRestoreRateInMegaBytesPerSecond\': 123.0,
                        \'SnapshotSizeInMegaBytes\': 123,
                        \'ProgressInMegaBytes\': 123,
                        \'ElapsedTimeInSeconds\': 123,
                        \'EstimatedTimeToCompletionInSeconds\': 123
                    },
                    \'HsmStatus\': {
                        \'HsmClientCertificateIdentifier\': \'string\',
                        \'HsmConfigurationIdentifier\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterSnapshotCopyStatus\': {
                        \'DestinationRegion\': \'string\',
                        \'RetentionPeriod\': 123,
                        \'SnapshotCopyGrantName\': \'string\'
                    },
                    \'ClusterPublicKey\': \'string\',
                    \'ClusterNodes\': [
                        {
                            \'NodeRole\': \'string\',
                            \'PrivateIPAddress\': \'string\',
                            \'PublicIPAddress\': \'string\'
                        },
                    ],
                    \'ElasticIpStatus\': {
                        \'ElasticIp\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterRevisionNumber\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'KmsKeyId\': \'string\',
                    \'EnhancedVpcRouting\': True|False,
                    \'IamRoles\': [
                        {
                            \'IamRoleArn\': \'string\',
                            \'ApplyStatus\': \'string\'
                        },
                    ],
                    \'PendingActions\': [
                        \'string\',
                    ],
                    \'MaintenanceTrackName\': \'string\',
                    \'ElasticResizeNumberOfNodeOptions\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              Describes a cluster.
        
              - **ClusterIdentifier** *(string) --* 
        
                The unique identifier of the cluster.
        
              - **NodeType** *(string) --* 
        
                The node type for the nodes in the cluster.
        
              - **ClusterStatus** *(string) --* 
        
                The current state of the cluster. Possible values are the following:
        
                * ``available``   
                 
                * ``creating``   
                 
                * ``deleting``   
                 
                * ``final-snapshot``   
                 
                * ``hardware-failure``   
                 
                * ``incompatible-hsm``   
                 
                * ``incompatible-network``   
                 
                * ``incompatible-parameters``   
                 
                * ``incompatible-restore``   
                 
                * ``modifying``   
                 
                * ``rebooting``   
                 
                * ``renaming``   
                 
                * ``resizing``   
                 
                * ``rotating-keys``   
                 
                * ``storage-full``   
                 
                * ``updating-hsm``   
                 
              - **ModifyStatus** *(string) --* 
        
                The status of a modify operation, if any, initiated for the cluster.
        
              - **MasterUsername** *(string) --* 
        
                The master user name for the cluster. This name is used to connect to the database that is specified in the **DBName** parameter. 
        
              - **DBName** *(string) --* 
        
                The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named ``dev`` dev was created by default. 
        
              - **Endpoint** *(dict) --* 
        
                The connection endpoint.
        
                - **Address** *(string) --* 
        
                  The DNS address of the Cluster.
        
                - **Port** *(integer) --* 
        
                  The port that the database engine is listening on.
        
              - **ClusterCreateTime** *(datetime) --* 
        
                The date and time that the cluster was created.
        
              - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                The number of days that automatic cluster snapshots are retained.
        
              - **ClusterSecurityGroups** *(list) --* 
        
                A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ``ClusterSecurityGroup.Name`` and ``ClusterSecurityGroup.Status`` subelements. 
        
                Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the **VpcSecurityGroups** parameter. 
        
                - *(dict) --* 
        
                  Describes a cluster security group.
        
                  - **ClusterSecurityGroupName** *(string) --* 
        
                    The name of the cluster security group.
        
                  - **Status** *(string) --* 
        
                    The status of the cluster security group.
        
              - **VpcSecurityGroups** *(list) --* 
        
                A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.
        
                - *(dict) --* 
        
                  Describes the members of a VPC security group.
        
                  - **VpcSecurityGroupId** *(string) --* 
        
                    The identifier of the VPC security group.
        
                  - **Status** *(string) --* 
        
                    The status of the VPC security group.
        
              - **ClusterParameterGroups** *(list) --* 
        
                The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.
        
                - *(dict) --* 
        
                  Describes the status of a parameter group.
        
                  - **ParameterGroupName** *(string) --* 
        
                    The name of the cluster parameter group.
        
                  - **ParameterApplyStatus** *(string) --* 
        
                    The status of parameter updates.
        
                  - **ClusterParameterStatusList** *(list) --* 
        
                    The list of parameter statuses.
        
                    For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
                    - *(dict) --* 
        
                      Describes the status of a parameter group.
        
                      - **ParameterName** *(string) --* 
        
                        The name of the parameter.
        
                      - **ParameterApplyStatus** *(string) --* 
        
                        The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
        
                        The following are possible statuses and descriptions.
        
                        * ``in-sync`` : The parameter value is in sync with the database. 
                         
                        * ``pending-reboot`` : The parameter value will be applied after the cluster reboots. 
                         
                        * ``applying`` : The parameter value is being applied to the database. 
                         
                        * ``invalid-parameter`` : Cannot apply the parameter value because it has an invalid value or syntax. 
                         
                        * ``apply-deferred`` : The parameter contains static property changes. The changes are deferred until the cluster reboots. 
                         
                        * ``apply-error`` : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots. 
                         
                        * ``unknown-error`` : Cannot apply the parameter change right now. The change will be applied after the cluster reboots. 
                         
                      - **ParameterApplyErrorDescription** *(string) --* 
        
                        The error that prevented the parameter from being applied to the database.
        
              - **ClusterSubnetGroupName** *(string) --* 
        
                The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.
        
              - **VpcId** *(string) --* 
        
                The identifier of the VPC the cluster is in, if the cluster is in a VPC.
        
              - **AvailabilityZone** *(string) --* 
        
                The name of the Availability Zone in which the cluster is located.
        
              - **PreferredMaintenanceWindow** *(string) --* 
        
                The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.
        
              - **PendingModifiedValues** *(dict) --* 
        
                A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.
        
                - **MasterUserPassword** *(string) --* 
        
                  The pending or in-progress change of the master user password for the cluster.
        
                - **NodeType** *(string) --* 
        
                  The pending or in-progress change of the cluster\'s node type.
        
                - **NumberOfNodes** *(integer) --* 
        
                  The pending or in-progress change of the number of nodes in the cluster.
        
                - **ClusterType** *(string) --* 
        
                  The pending or in-progress change of the cluster type.
        
                - **ClusterVersion** *(string) --* 
        
                  The pending or in-progress change of the service version.
        
                - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                  The pending or in-progress change of the automated snapshot retention period.
        
                - **ClusterIdentifier** *(string) --* 
        
                  The pending or in-progress change of the new identifier for the cluster.
        
                - **PubliclyAccessible** *(boolean) --* 
        
                  The pending or in-progress change of the ability to connect to the cluster from the public network.
        
                - **EnhancedVpcRouting** *(boolean) --* 
        
                  An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                  If this option is ``true`` , enhanced VPC routing is enabled. 
        
                  Default: false
        
                - **MaintenanceTrackName** *(string) --* 
        
                  The name of the maintenance track that the cluster will change to during the next maintenance window.
        
                - **EncryptionType** *(string) --* 
        
                  The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy. 
        
              - **ClusterVersion** *(string) --* 
        
                The version ID of the Amazon Redshift engine that is running on the cluster.
        
              - **AllowVersionUpgrade** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window. 
        
              - **NumberOfNodes** *(integer) --* 
        
                The number of compute nodes in the cluster.
        
              - **PubliclyAccessible** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that the cluster can be accessed from a public network.
        
              - **Encrypted** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that data in the cluster is encrypted at rest.
        
              - **RestoreStatus** *(dict) --* 
        
                A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.
        
                - **Status** *(string) --* 
        
                  The status of the restore action. Returns starting, restoring, completed, or failed.
        
                - **CurrentRestoreRateInMegaBytesPerSecond** *(float) --* 
        
                  The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.
        
                - **SnapshotSizeInMegaBytes** *(integer) --* 
        
                  The size of the set of snapshot data used to restore the cluster.
        
                - **ProgressInMegaBytes** *(integer) --* 
        
                  The number of megabytes that have been transferred from snapshot storage.
        
                - **ElapsedTimeInSeconds** *(integer) --* 
        
                  The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.
        
                - **EstimatedTimeToCompletionInSeconds** *(integer) --* 
        
                  The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore.
        
              - **HsmStatus** *(dict) --* 
        
                A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
        
                Values: active, applying
        
                - **HsmClientCertificateIdentifier** *(string) --* 
        
                  Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        
                - **HsmConfigurationIdentifier** *(string) --* 
        
                  Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        
                - **Status** *(string) --* 
        
                  Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
        
                  Values: active, applying
        
              - **ClusterSnapshotCopyStatus** *(dict) --* 
        
                A value that returns the destination region and retention period that are configured for cross-region snapshot copy.
        
                - **DestinationRegion** *(string) --* 
        
                  The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
        
                - **RetentionPeriod** *(integer) --* 
        
                  The number of days that automated snapshots are retained in the destination region after they are copied from a source region.
        
                - **SnapshotCopyGrantName** *(string) --* 
        
                  The name of the snapshot copy grant.
        
              - **ClusterPublicKey** *(string) --* 
        
                The public key for the cluster.
        
              - **ClusterNodes** *(list) --* 
        
                The nodes in the cluster.
        
                - *(dict) --* 
        
                  The identifier of a node in a cluster.
        
                  - **NodeRole** *(string) --* 
        
                    Whether the node is a leader node or a compute node.
        
                  - **PrivateIPAddress** *(string) --* 
        
                    The private IP address of a node within a cluster.
        
                  - **PublicIPAddress** *(string) --* 
        
                    The public IP address of a node within a cluster.
        
              - **ElasticIpStatus** *(dict) --* 
        
                The status of the elastic IP (EIP) address.
        
                - **ElasticIp** *(string) --* 
        
                  The elastic IP (EIP) address for the cluster.
        
                - **Status** *(string) --* 
        
                  The status of the elastic IP (EIP) address.
        
              - **ClusterRevisionNumber** *(string) --* 
        
                The specific revision number of the database in the cluster.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.
        
              - **EnhancedVpcRouting** *(boolean) --* 
        
                An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                If this option is ``true`` , enhanced VPC routing is enabled. 
        
                Default: false
        
              - **IamRoles** *(list) --* 
        
                A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.
        
                - *(dict) --* 
        
                  An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.
        
                  - **IamRoleArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the IAM role, for example, ``arn:aws:iam::123456789012:role/RedshiftCopyUnload`` . 
        
                  - **ApplyStatus** *(string) --* 
        
                    A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
        
                    The following are possible statuses and descriptions.
        
                    * ``in-sync`` : The role is available for use by the cluster. 
                     
                    * ``adding`` : The role is in the process of being associated with the cluster. 
                     
                    * ``removing`` : The role is in the process of being disassociated with the cluster. 
                     
              - **PendingActions** *(list) --* 
        
                Cluster operations that are waiting to be started.
        
                - *(string) --* 
            
              - **MaintenanceTrackName** *(string) --* 
        
                The name of the maintenance track for the cluster.
        
              - **ElasticResizeNumberOfNodeOptions** *(string) --* 
        
                Indicates the number of nodes the cluster can be resized to with the elastic resize method. 
        
        """
        pass

    def modify_cluster_iam_roles(self, ClusterIdentifier: str, AddIamRoles: List = None, RemoveIamRoles: List = None) -> Dict:
        """
        
        A cluster can have up to 10 IAM roles associated at any time.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/ModifyClusterIamRoles>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_cluster_iam_roles(
              ClusterIdentifier=\'string\',
              AddIamRoles=[
                  \'string\',
              ],
              RemoveIamRoles=[
                  \'string\',
              ]
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          The unique identifier of the cluster for which you want to associate or disassociate IAM roles.
        
        :type AddIamRoles: list
        :param AddIamRoles: 
        
          Zero or more IAM roles to associate with the cluster. The roles must be in their Amazon Resource Name (ARN) format. You can associate up to 10 IAM roles with a single cluster in a single request.
        
          - *(string) --* 
        
        :type RemoveIamRoles: list
        :param RemoveIamRoles: 
        
          Zero or more IAM roles in ARN format to disassociate from the cluster. You can disassociate up to 10 IAM roles from a single cluster in a single request.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
                    \'ClusterIdentifier\': \'string\',
                    \'NodeType\': \'string\',
                    \'ClusterStatus\': \'string\',
                    \'ModifyStatus\': \'string\',
                    \'MasterUsername\': \'string\',
                    \'DBName\': \'string\',
                    \'Endpoint\': {
                        \'Address\': \'string\',
                        \'Port\': 123
                    },
                    \'ClusterCreateTime\': datetime(2015, 1, 1),
                    \'AutomatedSnapshotRetentionPeriod\': 123,
                    \'ClusterSecurityGroups\': [
                        {
                            \'ClusterSecurityGroupName\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'VpcSecurityGroups\': [
                        {
                            \'VpcSecurityGroupId\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'ClusterParameterGroups\': [
                        {
                            \'ParameterGroupName\': \'string\',
                            \'ParameterApplyStatus\': \'string\',
                            \'ClusterParameterStatusList\': [
                                {
                                    \'ParameterName\': \'string\',
                                    \'ParameterApplyStatus\': \'string\',
                                    \'ParameterApplyErrorDescription\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'ClusterSubnetGroupName\': \'string\',
                    \'VpcId\': \'string\',
                    \'AvailabilityZone\': \'string\',
                    \'PreferredMaintenanceWindow\': \'string\',
                    \'PendingModifiedValues\': {
                        \'MasterUserPassword\': \'string\',
                        \'NodeType\': \'string\',
                        \'NumberOfNodes\': 123,
                        \'ClusterType\': \'string\',
                        \'ClusterVersion\': \'string\',
                        \'AutomatedSnapshotRetentionPeriod\': 123,
                        \'ClusterIdentifier\': \'string\',
                        \'PubliclyAccessible\': True|False,
                        \'EnhancedVpcRouting\': True|False,
                        \'MaintenanceTrackName\': \'string\',
                        \'EncryptionType\': \'string\'
                    },
                    \'ClusterVersion\': \'string\',
                    \'AllowVersionUpgrade\': True|False,
                    \'NumberOfNodes\': 123,
                    \'PubliclyAccessible\': True|False,
                    \'Encrypted\': True|False,
                    \'RestoreStatus\': {
                        \'Status\': \'string\',
                        \'CurrentRestoreRateInMegaBytesPerSecond\': 123.0,
                        \'SnapshotSizeInMegaBytes\': 123,
                        \'ProgressInMegaBytes\': 123,
                        \'ElapsedTimeInSeconds\': 123,
                        \'EstimatedTimeToCompletionInSeconds\': 123
                    },
                    \'HsmStatus\': {
                        \'HsmClientCertificateIdentifier\': \'string\',
                        \'HsmConfigurationIdentifier\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterSnapshotCopyStatus\': {
                        \'DestinationRegion\': \'string\',
                        \'RetentionPeriod\': 123,
                        \'SnapshotCopyGrantName\': \'string\'
                    },
                    \'ClusterPublicKey\': \'string\',
                    \'ClusterNodes\': [
                        {
                            \'NodeRole\': \'string\',
                            \'PrivateIPAddress\': \'string\',
                            \'PublicIPAddress\': \'string\'
                        },
                    ],
                    \'ElasticIpStatus\': {
                        \'ElasticIp\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterRevisionNumber\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'KmsKeyId\': \'string\',
                    \'EnhancedVpcRouting\': True|False,
                    \'IamRoles\': [
                        {
                            \'IamRoleArn\': \'string\',
                            \'ApplyStatus\': \'string\'
                        },
                    ],
                    \'PendingActions\': [
                        \'string\',
                    ],
                    \'MaintenanceTrackName\': \'string\',
                    \'ElasticResizeNumberOfNodeOptions\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              Describes a cluster.
        
              - **ClusterIdentifier** *(string) --* 
        
                The unique identifier of the cluster.
        
              - **NodeType** *(string) --* 
        
                The node type for the nodes in the cluster.
        
              - **ClusterStatus** *(string) --* 
        
                The current state of the cluster. Possible values are the following:
        
                * ``available``   
                 
                * ``creating``   
                 
                * ``deleting``   
                 
                * ``final-snapshot``   
                 
                * ``hardware-failure``   
                 
                * ``incompatible-hsm``   
                 
                * ``incompatible-network``   
                 
                * ``incompatible-parameters``   
                 
                * ``incompatible-restore``   
                 
                * ``modifying``   
                 
                * ``rebooting``   
                 
                * ``renaming``   
                 
                * ``resizing``   
                 
                * ``rotating-keys``   
                 
                * ``storage-full``   
                 
                * ``updating-hsm``   
                 
              - **ModifyStatus** *(string) --* 
        
                The status of a modify operation, if any, initiated for the cluster.
        
              - **MasterUsername** *(string) --* 
        
                The master user name for the cluster. This name is used to connect to the database that is specified in the **DBName** parameter. 
        
              - **DBName** *(string) --* 
        
                The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named ``dev`` dev was created by default. 
        
              - **Endpoint** *(dict) --* 
        
                The connection endpoint.
        
                - **Address** *(string) --* 
        
                  The DNS address of the Cluster.
        
                - **Port** *(integer) --* 
        
                  The port that the database engine is listening on.
        
              - **ClusterCreateTime** *(datetime) --* 
        
                The date and time that the cluster was created.
        
              - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                The number of days that automatic cluster snapshots are retained.
        
              - **ClusterSecurityGroups** *(list) --* 
        
                A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ``ClusterSecurityGroup.Name`` and ``ClusterSecurityGroup.Status`` subelements. 
        
                Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the **VpcSecurityGroups** parameter. 
        
                - *(dict) --* 
        
                  Describes a cluster security group.
        
                  - **ClusterSecurityGroupName** *(string) --* 
        
                    The name of the cluster security group.
        
                  - **Status** *(string) --* 
        
                    The status of the cluster security group.
        
              - **VpcSecurityGroups** *(list) --* 
        
                A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.
        
                - *(dict) --* 
        
                  Describes the members of a VPC security group.
        
                  - **VpcSecurityGroupId** *(string) --* 
        
                    The identifier of the VPC security group.
        
                  - **Status** *(string) --* 
        
                    The status of the VPC security group.
        
              - **ClusterParameterGroups** *(list) --* 
        
                The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.
        
                - *(dict) --* 
        
                  Describes the status of a parameter group.
        
                  - **ParameterGroupName** *(string) --* 
        
                    The name of the cluster parameter group.
        
                  - **ParameterApplyStatus** *(string) --* 
        
                    The status of parameter updates.
        
                  - **ClusterParameterStatusList** *(list) --* 
        
                    The list of parameter statuses.
        
                    For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
                    - *(dict) --* 
        
                      Describes the status of a parameter group.
        
                      - **ParameterName** *(string) --* 
        
                        The name of the parameter.
        
                      - **ParameterApplyStatus** *(string) --* 
        
                        The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
        
                        The following are possible statuses and descriptions.
        
                        * ``in-sync`` : The parameter value is in sync with the database. 
                         
                        * ``pending-reboot`` : The parameter value will be applied after the cluster reboots. 
                         
                        * ``applying`` : The parameter value is being applied to the database. 
                         
                        * ``invalid-parameter`` : Cannot apply the parameter value because it has an invalid value or syntax. 
                         
                        * ``apply-deferred`` : The parameter contains static property changes. The changes are deferred until the cluster reboots. 
                         
                        * ``apply-error`` : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots. 
                         
                        * ``unknown-error`` : Cannot apply the parameter change right now. The change will be applied after the cluster reboots. 
                         
                      - **ParameterApplyErrorDescription** *(string) --* 
        
                        The error that prevented the parameter from being applied to the database.
        
              - **ClusterSubnetGroupName** *(string) --* 
        
                The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.
        
              - **VpcId** *(string) --* 
        
                The identifier of the VPC the cluster is in, if the cluster is in a VPC.
        
              - **AvailabilityZone** *(string) --* 
        
                The name of the Availability Zone in which the cluster is located.
        
              - **PreferredMaintenanceWindow** *(string) --* 
        
                The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.
        
              - **PendingModifiedValues** *(dict) --* 
        
                A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.
        
                - **MasterUserPassword** *(string) --* 
        
                  The pending or in-progress change of the master user password for the cluster.
        
                - **NodeType** *(string) --* 
        
                  The pending or in-progress change of the cluster\'s node type.
        
                - **NumberOfNodes** *(integer) --* 
        
                  The pending or in-progress change of the number of nodes in the cluster.
        
                - **ClusterType** *(string) --* 
        
                  The pending or in-progress change of the cluster type.
        
                - **ClusterVersion** *(string) --* 
        
                  The pending or in-progress change of the service version.
        
                - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                  The pending or in-progress change of the automated snapshot retention period.
        
                - **ClusterIdentifier** *(string) --* 
        
                  The pending or in-progress change of the new identifier for the cluster.
        
                - **PubliclyAccessible** *(boolean) --* 
        
                  The pending or in-progress change of the ability to connect to the cluster from the public network.
        
                - **EnhancedVpcRouting** *(boolean) --* 
        
                  An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                  If this option is ``true`` , enhanced VPC routing is enabled. 
        
                  Default: false
        
                - **MaintenanceTrackName** *(string) --* 
        
                  The name of the maintenance track that the cluster will change to during the next maintenance window.
        
                - **EncryptionType** *(string) --* 
        
                  The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy. 
        
              - **ClusterVersion** *(string) --* 
        
                The version ID of the Amazon Redshift engine that is running on the cluster.
        
              - **AllowVersionUpgrade** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window. 
        
              - **NumberOfNodes** *(integer) --* 
        
                The number of compute nodes in the cluster.
        
              - **PubliclyAccessible** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that the cluster can be accessed from a public network.
        
              - **Encrypted** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that data in the cluster is encrypted at rest.
        
              - **RestoreStatus** *(dict) --* 
        
                A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.
        
                - **Status** *(string) --* 
        
                  The status of the restore action. Returns starting, restoring, completed, or failed.
        
                - **CurrentRestoreRateInMegaBytesPerSecond** *(float) --* 
        
                  The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.
        
                - **SnapshotSizeInMegaBytes** *(integer) --* 
        
                  The size of the set of snapshot data used to restore the cluster.
        
                - **ProgressInMegaBytes** *(integer) --* 
        
                  The number of megabytes that have been transferred from snapshot storage.
        
                - **ElapsedTimeInSeconds** *(integer) --* 
        
                  The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.
        
                - **EstimatedTimeToCompletionInSeconds** *(integer) --* 
        
                  The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore.
        
              - **HsmStatus** *(dict) --* 
        
                A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
        
                Values: active, applying
        
                - **HsmClientCertificateIdentifier** *(string) --* 
        
                  Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        
                - **HsmConfigurationIdentifier** *(string) --* 
        
                  Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        
                - **Status** *(string) --* 
        
                  Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
        
                  Values: active, applying
        
              - **ClusterSnapshotCopyStatus** *(dict) --* 
        
                A value that returns the destination region and retention period that are configured for cross-region snapshot copy.
        
                - **DestinationRegion** *(string) --* 
        
                  The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
        
                - **RetentionPeriod** *(integer) --* 
        
                  The number of days that automated snapshots are retained in the destination region after they are copied from a source region.
        
                - **SnapshotCopyGrantName** *(string) --* 
        
                  The name of the snapshot copy grant.
        
              - **ClusterPublicKey** *(string) --* 
        
                The public key for the cluster.
        
              - **ClusterNodes** *(list) --* 
        
                The nodes in the cluster.
        
                - *(dict) --* 
        
                  The identifier of a node in a cluster.
        
                  - **NodeRole** *(string) --* 
        
                    Whether the node is a leader node or a compute node.
        
                  - **PrivateIPAddress** *(string) --* 
        
                    The private IP address of a node within a cluster.
        
                  - **PublicIPAddress** *(string) --* 
        
                    The public IP address of a node within a cluster.
        
              - **ElasticIpStatus** *(dict) --* 
        
                The status of the elastic IP (EIP) address.
        
                - **ElasticIp** *(string) --* 
        
                  The elastic IP (EIP) address for the cluster.
        
                - **Status** *(string) --* 
        
                  The status of the elastic IP (EIP) address.
        
              - **ClusterRevisionNumber** *(string) --* 
        
                The specific revision number of the database in the cluster.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.
        
              - **EnhancedVpcRouting** *(boolean) --* 
        
                An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                If this option is ``true`` , enhanced VPC routing is enabled. 
        
                Default: false
        
              - **IamRoles** *(list) --* 
        
                A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.
        
                - *(dict) --* 
        
                  An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.
        
                  - **IamRoleArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the IAM role, for example, ``arn:aws:iam::123456789012:role/RedshiftCopyUnload`` . 
        
                  - **ApplyStatus** *(string) --* 
        
                    A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
        
                    The following are possible statuses and descriptions.
        
                    * ``in-sync`` : The role is available for use by the cluster. 
                     
                    * ``adding`` : The role is in the process of being associated with the cluster. 
                     
                    * ``removing`` : The role is in the process of being disassociated with the cluster. 
                     
              - **PendingActions** *(list) --* 
        
                Cluster operations that are waiting to be started.
        
                - *(string) --* 
            
              - **MaintenanceTrackName** *(string) --* 
        
                The name of the maintenance track for the cluster.
        
              - **ElasticResizeNumberOfNodeOptions** *(string) --* 
        
                Indicates the number of nodes the cluster can be resized to with the elastic resize method. 
        
        """
        pass

    def modify_cluster_parameter_group(self, ParameterGroupName: str, Parameters: List) -> Dict:
        """
        
        For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/ModifyClusterParameterGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_cluster_parameter_group(
              ParameterGroupName=\'string\',
              Parameters=[
                  {
                      \'ParameterName\': \'string\',
                      \'ParameterValue\': \'string\',
                      \'Description\': \'string\',
                      \'Source\': \'string\',
                      \'DataType\': \'string\',
                      \'AllowedValues\': \'string\',
                      \'ApplyType\': \'static\'|\'dynamic\',
                      \'IsModifiable\': True|False,
                      \'MinimumEngineVersion\': \'string\'
                  },
              ]
          )
        :type ParameterGroupName: string
        :param ParameterGroupName: **[REQUIRED]** 
        
          The name of the parameter group to be modified.
        
        :type Parameters: list
        :param Parameters: **[REQUIRED]** 
        
          An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.
        
          For each parameter to be modified, you must supply at least the parameter name and parameter value; other name-value pairs of the parameter are optional.
        
          For the workload management (WLM) configuration, you must supply all the name-value pairs in the wlm_json_configuration parameter.
        
          - *(dict) --* 
        
            Describes a parameter in a cluster parameter group.
        
            - **ParameterName** *(string) --* 
        
              The name of the parameter.
        
            - **ParameterValue** *(string) --* 
        
              The value of the parameter.
        
            - **Description** *(string) --* 
        
              A description of the parameter.
        
            - **Source** *(string) --* 
        
              The source of the parameter value, such as \"engine-default\" or \"user\".
        
            - **DataType** *(string) --* 
        
              The data type of the parameter.
        
            - **AllowedValues** *(string) --* 
        
              The valid range of values for the parameter.
        
            - **ApplyType** *(string) --* 
        
              Specifies how to apply the WLM configuration parameter. Some properties can be applied dynamically, while other properties require that any associated clusters be rebooted for the configuration changes to be applied. For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
            - **IsModifiable** *(boolean) --* 
        
              If ``true`` , the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed. 
        
            - **MinimumEngineVersion** *(string) --* 
        
              The earliest engine version to which the parameter can apply.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ParameterGroupName\': \'string\',
                \'ParameterGroupStatus\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ParameterGroupName** *(string) --* 
        
              The name of the cluster parameter group.
        
            - **ParameterGroupStatus** *(string) --* 
        
              The status of the parameter group. For example, if you made a change to a parameter group name-value pair, then the change could be pending a reboot of an associated cluster.
        
        """
        pass

    def modify_cluster_subnet_group(self, ClusterSubnetGroupName: str, SubnetIds: List, Description: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/ModifyClusterSubnetGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_cluster_subnet_group(
              ClusterSubnetGroupName=\'string\',
              Description=\'string\',
              SubnetIds=[
                  \'string\',
              ]
          )
        :type ClusterSubnetGroupName: string
        :param ClusterSubnetGroupName: **[REQUIRED]** 
        
          The name of the subnet group to be modified.
        
        :type Description: string
        :param Description: 
        
          A text description of the subnet group to be modified.
        
        :type SubnetIds: list
        :param SubnetIds: **[REQUIRED]** 
        
          An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ClusterSubnetGroup\': {
                    \'ClusterSubnetGroupName\': \'string\',
                    \'Description\': \'string\',
                    \'VpcId\': \'string\',
                    \'SubnetGroupStatus\': \'string\',
                    \'Subnets\': [
                        {
                            \'SubnetIdentifier\': \'string\',
                            \'SubnetAvailabilityZone\': {
                                \'Name\': \'string\',
                                \'SupportedPlatforms\': [
                                    {
                                        \'Name\': \'string\'
                                    },
                                ]
                            },
                            \'SubnetStatus\': \'string\'
                        },
                    ],
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
            
            - **ClusterSubnetGroup** *(dict) --* 
        
              Describes a subnet group.
        
              - **ClusterSubnetGroupName** *(string) --* 
        
                The name of the cluster subnet group.
        
              - **Description** *(string) --* 
        
                The description of the cluster subnet group.
        
              - **VpcId** *(string) --* 
        
                The VPC ID of the cluster subnet group.
        
              - **SubnetGroupStatus** *(string) --* 
        
                The status of the cluster subnet group. Possible values are ``Complete`` , ``Incomplete`` and ``Invalid`` . 
        
              - **Subnets** *(list) --* 
        
                A list of the VPC  Subnet elements. 
        
                - *(dict) --* 
        
                  Describes a subnet.
        
                  - **SubnetIdentifier** *(string) --* 
        
                    The identifier of the subnet.
        
                  - **SubnetAvailabilityZone** *(dict) --* 
        
                    Describes an availability zone.
        
                    - **Name** *(string) --* 
        
                      The name of the availability zone.
        
                    - **SupportedPlatforms** *(list) --* 
                      
                      - *(dict) --* 
        
                        A list of supported platforms for orderable clusters.
        
                        - **Name** *(string) --* 
                    
                  - **SubnetStatus** *(string) --* 
        
                    The status of the subnet.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster subnet group.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
        """
        pass

    def modify_event_subscription(self, SubscriptionName: str, SnsTopicArn: str = None, SourceType: str = None, SourceIds: List = None, EventCategories: List = None, Severity: str = None, Enabled: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/ModifyEventSubscription>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_event_subscription(
              SubscriptionName=\'string\',
              SnsTopicArn=\'string\',
              SourceType=\'string\',
              SourceIds=[
                  \'string\',
              ],
              EventCategories=[
                  \'string\',
              ],
              Severity=\'string\',
              Enabled=True|False
          )
        :type SubscriptionName: string
        :param SubscriptionName: **[REQUIRED]** 
        
          The name of the modified Amazon Redshift event notification subscription.
        
        :type SnsTopicArn: string
        :param SnsTopicArn: 
        
          The Amazon Resource Name (ARN) of the SNS topic to be used by the event notification subscription.
        
        :type SourceType: string
        :param SourceType: 
        
          The type of source that will be generating the events. For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your AWS account. You must specify a source type in order to specify source IDs.
        
          Valid values: cluster, cluster-parameter-group, cluster-security-group, and cluster-snapshot.
        
        :type SourceIds: list
        :param SourceIds: 
        
          A list of one or more identifiers of Amazon Redshift source objects. All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified.
        
          Example: my-cluster-1, my-cluster-2
        
          Example: my-snapshot-20131010
        
          - *(string) --* 
        
        :type EventCategories: list
        :param EventCategories: 
        
          Specifies the Amazon Redshift event categories to be published by the event notification subscription.
        
          Values: Configuration, Management, Monitoring, Security
        
          - *(string) --* 
        
        :type Severity: string
        :param Severity: 
        
          Specifies the Amazon Redshift event severity to be published by the event notification subscription.
        
          Values: ERROR, INFO
        
        :type Enabled: boolean
        :param Enabled: 
        
          A Boolean value indicating if the subscription is enabled. ``true`` indicates the subscription is enabled 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EventSubscription\': {
                    \'CustomerAwsId\': \'string\',
                    \'CustSubscriptionId\': \'string\',
                    \'SnsTopicArn\': \'string\',
                    \'Status\': \'string\',
                    \'SubscriptionCreationTime\': datetime(2015, 1, 1),
                    \'SourceType\': \'string\',
                    \'SourceIdsList\': [
                        \'string\',
                    ],
                    \'EventCategoriesList\': [
                        \'string\',
                    ],
                    \'Severity\': \'string\',
                    \'Enabled\': True|False,
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
            
            - **EventSubscription** *(dict) --* 
        
              Describes event subscriptions.
        
              - **CustomerAwsId** *(string) --* 
        
                The AWS customer account associated with the Amazon Redshift event notification subscription.
        
              - **CustSubscriptionId** *(string) --* 
        
                The name of the Amazon Redshift event notification subscription.
        
              - **SnsTopicArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the Amazon SNS topic used by the event notification subscription.
        
              - **Status** *(string) --* 
        
                The status of the Amazon Redshift event notification subscription.
        
                Constraints:
        
                * Can be one of the following: active | no-permission | topic-not-exist 
                 
                * The status \"no-permission\" indicates that Amazon Redshift no longer has permission to post to the Amazon SNS topic. The status \"topic-not-exist\" indicates that the topic was deleted after the subscription was created. 
                 
              - **SubscriptionCreationTime** *(datetime) --* 
        
                The date and time the Amazon Redshift event notification subscription was created.
        
              - **SourceType** *(string) --* 
        
                The source type of the events returned the Amazon Redshift event notification, such as cluster, or cluster-snapshot.
        
              - **SourceIdsList** *(list) --* 
        
                A list of the sources that publish events to the Amazon Redshift event notification subscription.
        
                - *(string) --* 
            
              - **EventCategoriesList** *(list) --* 
        
                The list of Amazon Redshift event categories specified in the event notification subscription.
        
                Values: Configuration, Management, Monitoring, Security
        
                - *(string) --* 
            
              - **Severity** *(string) --* 
        
                The event severity specified in the Amazon Redshift event notification subscription.
        
                Values: ERROR, INFO
        
              - **Enabled** *(boolean) --* 
        
                A Boolean value indicating whether the subscription is enabled. ``true`` indicates the subscription is enabled.
        
              - **Tags** *(list) --* 
        
                The list of tags for the event subscription.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
        """
        pass

    def modify_snapshot_copy_retention_period(self, ClusterIdentifier: str, RetentionPeriod: int) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/ModifySnapshotCopyRetentionPeriod>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_snapshot_copy_retention_period(
              ClusterIdentifier=\'string\',
              RetentionPeriod=123
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          The unique identifier of the cluster for which you want to change the retention period for automated snapshots that are copied to a destination region.
        
          Constraints: Must be the valid name of an existing cluster that has cross-region snapshot copy enabled.
        
        :type RetentionPeriod: integer
        :param RetentionPeriod: **[REQUIRED]** 
        
          The number of days to retain automated snapshots in the destination region after they are copied from the source region.
        
          If you decrease the retention period for automated snapshots that are copied to a destination region, Amazon Redshift will delete any existing automated snapshots that were copied to the destination region and that fall outside of the new retention period.
        
          Constraints: Must be at least 1 and no more than 35.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
                    \'ClusterIdentifier\': \'string\',
                    \'NodeType\': \'string\',
                    \'ClusterStatus\': \'string\',
                    \'ModifyStatus\': \'string\',
                    \'MasterUsername\': \'string\',
                    \'DBName\': \'string\',
                    \'Endpoint\': {
                        \'Address\': \'string\',
                        \'Port\': 123
                    },
                    \'ClusterCreateTime\': datetime(2015, 1, 1),
                    \'AutomatedSnapshotRetentionPeriod\': 123,
                    \'ClusterSecurityGroups\': [
                        {
                            \'ClusterSecurityGroupName\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'VpcSecurityGroups\': [
                        {
                            \'VpcSecurityGroupId\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'ClusterParameterGroups\': [
                        {
                            \'ParameterGroupName\': \'string\',
                            \'ParameterApplyStatus\': \'string\',
                            \'ClusterParameterStatusList\': [
                                {
                                    \'ParameterName\': \'string\',
                                    \'ParameterApplyStatus\': \'string\',
                                    \'ParameterApplyErrorDescription\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'ClusterSubnetGroupName\': \'string\',
                    \'VpcId\': \'string\',
                    \'AvailabilityZone\': \'string\',
                    \'PreferredMaintenanceWindow\': \'string\',
                    \'PendingModifiedValues\': {
                        \'MasterUserPassword\': \'string\',
                        \'NodeType\': \'string\',
                        \'NumberOfNodes\': 123,
                        \'ClusterType\': \'string\',
                        \'ClusterVersion\': \'string\',
                        \'AutomatedSnapshotRetentionPeriod\': 123,
                        \'ClusterIdentifier\': \'string\',
                        \'PubliclyAccessible\': True|False,
                        \'EnhancedVpcRouting\': True|False,
                        \'MaintenanceTrackName\': \'string\',
                        \'EncryptionType\': \'string\'
                    },
                    \'ClusterVersion\': \'string\',
                    \'AllowVersionUpgrade\': True|False,
                    \'NumberOfNodes\': 123,
                    \'PubliclyAccessible\': True|False,
                    \'Encrypted\': True|False,
                    \'RestoreStatus\': {
                        \'Status\': \'string\',
                        \'CurrentRestoreRateInMegaBytesPerSecond\': 123.0,
                        \'SnapshotSizeInMegaBytes\': 123,
                        \'ProgressInMegaBytes\': 123,
                        \'ElapsedTimeInSeconds\': 123,
                        \'EstimatedTimeToCompletionInSeconds\': 123
                    },
                    \'HsmStatus\': {
                        \'HsmClientCertificateIdentifier\': \'string\',
                        \'HsmConfigurationIdentifier\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterSnapshotCopyStatus\': {
                        \'DestinationRegion\': \'string\',
                        \'RetentionPeriod\': 123,
                        \'SnapshotCopyGrantName\': \'string\'
                    },
                    \'ClusterPublicKey\': \'string\',
                    \'ClusterNodes\': [
                        {
                            \'NodeRole\': \'string\',
                            \'PrivateIPAddress\': \'string\',
                            \'PublicIPAddress\': \'string\'
                        },
                    ],
                    \'ElasticIpStatus\': {
                        \'ElasticIp\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterRevisionNumber\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'KmsKeyId\': \'string\',
                    \'EnhancedVpcRouting\': True|False,
                    \'IamRoles\': [
                        {
                            \'IamRoleArn\': \'string\',
                            \'ApplyStatus\': \'string\'
                        },
                    ],
                    \'PendingActions\': [
                        \'string\',
                    ],
                    \'MaintenanceTrackName\': \'string\',
                    \'ElasticResizeNumberOfNodeOptions\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              Describes a cluster.
        
              - **ClusterIdentifier** *(string) --* 
        
                The unique identifier of the cluster.
        
              - **NodeType** *(string) --* 
        
                The node type for the nodes in the cluster.
        
              - **ClusterStatus** *(string) --* 
        
                The current state of the cluster. Possible values are the following:
        
                * ``available``   
                 
                * ``creating``   
                 
                * ``deleting``   
                 
                * ``final-snapshot``   
                 
                * ``hardware-failure``   
                 
                * ``incompatible-hsm``   
                 
                * ``incompatible-network``   
                 
                * ``incompatible-parameters``   
                 
                * ``incompatible-restore``   
                 
                * ``modifying``   
                 
                * ``rebooting``   
                 
                * ``renaming``   
                 
                * ``resizing``   
                 
                * ``rotating-keys``   
                 
                * ``storage-full``   
                 
                * ``updating-hsm``   
                 
              - **ModifyStatus** *(string) --* 
        
                The status of a modify operation, if any, initiated for the cluster.
        
              - **MasterUsername** *(string) --* 
        
                The master user name for the cluster. This name is used to connect to the database that is specified in the **DBName** parameter. 
        
              - **DBName** *(string) --* 
        
                The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named ``dev`` dev was created by default. 
        
              - **Endpoint** *(dict) --* 
        
                The connection endpoint.
        
                - **Address** *(string) --* 
        
                  The DNS address of the Cluster.
        
                - **Port** *(integer) --* 
        
                  The port that the database engine is listening on.
        
              - **ClusterCreateTime** *(datetime) --* 
        
                The date and time that the cluster was created.
        
              - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                The number of days that automatic cluster snapshots are retained.
        
              - **ClusterSecurityGroups** *(list) --* 
        
                A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ``ClusterSecurityGroup.Name`` and ``ClusterSecurityGroup.Status`` subelements. 
        
                Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the **VpcSecurityGroups** parameter. 
        
                - *(dict) --* 
        
                  Describes a cluster security group.
        
                  - **ClusterSecurityGroupName** *(string) --* 
        
                    The name of the cluster security group.
        
                  - **Status** *(string) --* 
        
                    The status of the cluster security group.
        
              - **VpcSecurityGroups** *(list) --* 
        
                A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.
        
                - *(dict) --* 
        
                  Describes the members of a VPC security group.
        
                  - **VpcSecurityGroupId** *(string) --* 
        
                    The identifier of the VPC security group.
        
                  - **Status** *(string) --* 
        
                    The status of the VPC security group.
        
              - **ClusterParameterGroups** *(list) --* 
        
                The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.
        
                - *(dict) --* 
        
                  Describes the status of a parameter group.
        
                  - **ParameterGroupName** *(string) --* 
        
                    The name of the cluster parameter group.
        
                  - **ParameterApplyStatus** *(string) --* 
        
                    The status of parameter updates.
        
                  - **ClusterParameterStatusList** *(list) --* 
        
                    The list of parameter statuses.
        
                    For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
                    - *(dict) --* 
        
                      Describes the status of a parameter group.
        
                      - **ParameterName** *(string) --* 
        
                        The name of the parameter.
        
                      - **ParameterApplyStatus** *(string) --* 
        
                        The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
        
                        The following are possible statuses and descriptions.
        
                        * ``in-sync`` : The parameter value is in sync with the database. 
                         
                        * ``pending-reboot`` : The parameter value will be applied after the cluster reboots. 
                         
                        * ``applying`` : The parameter value is being applied to the database. 
                         
                        * ``invalid-parameter`` : Cannot apply the parameter value because it has an invalid value or syntax. 
                         
                        * ``apply-deferred`` : The parameter contains static property changes. The changes are deferred until the cluster reboots. 
                         
                        * ``apply-error`` : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots. 
                         
                        * ``unknown-error`` : Cannot apply the parameter change right now. The change will be applied after the cluster reboots. 
                         
                      - **ParameterApplyErrorDescription** *(string) --* 
        
                        The error that prevented the parameter from being applied to the database.
        
              - **ClusterSubnetGroupName** *(string) --* 
        
                The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.
        
              - **VpcId** *(string) --* 
        
                The identifier of the VPC the cluster is in, if the cluster is in a VPC.
        
              - **AvailabilityZone** *(string) --* 
        
                The name of the Availability Zone in which the cluster is located.
        
              - **PreferredMaintenanceWindow** *(string) --* 
        
                The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.
        
              - **PendingModifiedValues** *(dict) --* 
        
                A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.
        
                - **MasterUserPassword** *(string) --* 
        
                  The pending or in-progress change of the master user password for the cluster.
        
                - **NodeType** *(string) --* 
        
                  The pending or in-progress change of the cluster\'s node type.
        
                - **NumberOfNodes** *(integer) --* 
        
                  The pending or in-progress change of the number of nodes in the cluster.
        
                - **ClusterType** *(string) --* 
        
                  The pending or in-progress change of the cluster type.
        
                - **ClusterVersion** *(string) --* 
        
                  The pending or in-progress change of the service version.
        
                - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                  The pending or in-progress change of the automated snapshot retention period.
        
                - **ClusterIdentifier** *(string) --* 
        
                  The pending or in-progress change of the new identifier for the cluster.
        
                - **PubliclyAccessible** *(boolean) --* 
        
                  The pending or in-progress change of the ability to connect to the cluster from the public network.
        
                - **EnhancedVpcRouting** *(boolean) --* 
        
                  An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                  If this option is ``true`` , enhanced VPC routing is enabled. 
        
                  Default: false
        
                - **MaintenanceTrackName** *(string) --* 
        
                  The name of the maintenance track that the cluster will change to during the next maintenance window.
        
                - **EncryptionType** *(string) --* 
        
                  The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy. 
        
              - **ClusterVersion** *(string) --* 
        
                The version ID of the Amazon Redshift engine that is running on the cluster.
        
              - **AllowVersionUpgrade** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window. 
        
              - **NumberOfNodes** *(integer) --* 
        
                The number of compute nodes in the cluster.
        
              - **PubliclyAccessible** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that the cluster can be accessed from a public network.
        
              - **Encrypted** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that data in the cluster is encrypted at rest.
        
              - **RestoreStatus** *(dict) --* 
        
                A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.
        
                - **Status** *(string) --* 
        
                  The status of the restore action. Returns starting, restoring, completed, or failed.
        
                - **CurrentRestoreRateInMegaBytesPerSecond** *(float) --* 
        
                  The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.
        
                - **SnapshotSizeInMegaBytes** *(integer) --* 
        
                  The size of the set of snapshot data used to restore the cluster.
        
                - **ProgressInMegaBytes** *(integer) --* 
        
                  The number of megabytes that have been transferred from snapshot storage.
        
                - **ElapsedTimeInSeconds** *(integer) --* 
        
                  The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.
        
                - **EstimatedTimeToCompletionInSeconds** *(integer) --* 
        
                  The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore.
        
              - **HsmStatus** *(dict) --* 
        
                A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
        
                Values: active, applying
        
                - **HsmClientCertificateIdentifier** *(string) --* 
        
                  Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        
                - **HsmConfigurationIdentifier** *(string) --* 
        
                  Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        
                - **Status** *(string) --* 
        
                  Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
        
                  Values: active, applying
        
              - **ClusterSnapshotCopyStatus** *(dict) --* 
        
                A value that returns the destination region and retention period that are configured for cross-region snapshot copy.
        
                - **DestinationRegion** *(string) --* 
        
                  The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
        
                - **RetentionPeriod** *(integer) --* 
        
                  The number of days that automated snapshots are retained in the destination region after they are copied from a source region.
        
                - **SnapshotCopyGrantName** *(string) --* 
        
                  The name of the snapshot copy grant.
        
              - **ClusterPublicKey** *(string) --* 
        
                The public key for the cluster.
        
              - **ClusterNodes** *(list) --* 
        
                The nodes in the cluster.
        
                - *(dict) --* 
        
                  The identifier of a node in a cluster.
        
                  - **NodeRole** *(string) --* 
        
                    Whether the node is a leader node or a compute node.
        
                  - **PrivateIPAddress** *(string) --* 
        
                    The private IP address of a node within a cluster.
        
                  - **PublicIPAddress** *(string) --* 
        
                    The public IP address of a node within a cluster.
        
              - **ElasticIpStatus** *(dict) --* 
        
                The status of the elastic IP (EIP) address.
        
                - **ElasticIp** *(string) --* 
        
                  The elastic IP (EIP) address for the cluster.
        
                - **Status** *(string) --* 
        
                  The status of the elastic IP (EIP) address.
        
              - **ClusterRevisionNumber** *(string) --* 
        
                The specific revision number of the database in the cluster.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.
        
              - **EnhancedVpcRouting** *(boolean) --* 
        
                An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                If this option is ``true`` , enhanced VPC routing is enabled. 
        
                Default: false
        
              - **IamRoles** *(list) --* 
        
                A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.
        
                - *(dict) --* 
        
                  An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.
        
                  - **IamRoleArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the IAM role, for example, ``arn:aws:iam::123456789012:role/RedshiftCopyUnload`` . 
        
                  - **ApplyStatus** *(string) --* 
        
                    A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
        
                    The following are possible statuses and descriptions.
        
                    * ``in-sync`` : The role is available for use by the cluster. 
                     
                    * ``adding`` : The role is in the process of being associated with the cluster. 
                     
                    * ``removing`` : The role is in the process of being disassociated with the cluster. 
                     
              - **PendingActions** *(list) --* 
        
                Cluster operations that are waiting to be started.
        
                - *(string) --* 
            
              - **MaintenanceTrackName** *(string) --* 
        
                The name of the maintenance track for the cluster.
        
              - **ElasticResizeNumberOfNodeOptions** *(string) --* 
        
                Indicates the number of nodes the cluster can be resized to with the elastic resize method. 
        
        """
        pass

    def purchase_reserved_node_offering(self, ReservedNodeOfferingId: str, NodeCount: int = None) -> Dict:
        """
        
        For more information about reserved node offerings, go to `Purchasing Reserved Nodes <http://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/PurchaseReservedNodeOffering>`_
        
        **Request Syntax** 
        ::
        
          response = client.purchase_reserved_node_offering(
              ReservedNodeOfferingId=\'string\',
              NodeCount=123
          )
        :type ReservedNodeOfferingId: string
        :param ReservedNodeOfferingId: **[REQUIRED]** 
        
          The unique identifier of the reserved node offering you want to purchase.
        
        :type NodeCount: integer
        :param NodeCount: 
        
          The number of reserved nodes that you want to purchase.
        
          Default: ``1``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ReservedNode\': {
                    \'ReservedNodeId\': \'string\',
                    \'ReservedNodeOfferingId\': \'string\',
                    \'NodeType\': \'string\',
                    \'StartTime\': datetime(2015, 1, 1),
                    \'Duration\': 123,
                    \'FixedPrice\': 123.0,
                    \'UsagePrice\': 123.0,
                    \'CurrencyCode\': \'string\',
                    \'NodeCount\': 123,
                    \'State\': \'string\',
                    \'OfferingType\': \'string\',
                    \'RecurringCharges\': [
                        {
                            \'RecurringChargeAmount\': 123.0,
                            \'RecurringChargeFrequency\': \'string\'
                        },
                    ],
                    \'ReservedNodeOfferingType\': \'Regular\'|\'Upgradable\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ReservedNode** *(dict) --* 
        
              Describes a reserved node. You can call the  DescribeReservedNodeOfferings API to obtain the available reserved node offerings. 
        
              - **ReservedNodeId** *(string) --* 
        
                The unique identifier for the reservation.
        
              - **ReservedNodeOfferingId** *(string) --* 
        
                The identifier for the reserved node offering.
        
              - **NodeType** *(string) --* 
        
                The node type of the reserved node.
        
              - **StartTime** *(datetime) --* 
        
                The time the reservation started. You purchase a reserved node offering for a duration. This is the start time of that duration.
        
              - **Duration** *(integer) --* 
        
                The duration of the node reservation in seconds.
        
              - **FixedPrice** *(float) --* 
        
                The fixed cost Amazon Redshift charges you for this reserved node.
        
              - **UsagePrice** *(float) --* 
        
                The hourly rate Amazon Redshift charges you for this reserved node.
        
              - **CurrencyCode** *(string) --* 
        
                The currency code for the reserved cluster.
        
              - **NodeCount** *(integer) --* 
        
                The number of reserved compute nodes.
        
              - **State** *(string) --* 
        
                The state of the reserved compute node.
        
                Possible Values:
        
                * pending-payment-This reserved node has recently been purchased, and the sale has been approved, but payment has not yet been confirmed. 
                 
                * active-This reserved node is owned by the caller and is available for use. 
                 
                * payment-failed-Payment failed for the purchase attempt. 
                 
                * retired-The reserved node is no longer available.  
                 
                * exchanging-The owner is exchanging the reserved node for another reserved node. 
                 
              - **OfferingType** *(string) --* 
        
                The anticipated utilization of the reserved node, as defined in the reserved node offering.
        
              - **RecurringCharges** *(list) --* 
        
                The recurring charges for the reserved node.
        
                - *(dict) --* 
        
                  Describes a recurring charge.
        
                  - **RecurringChargeAmount** *(float) --* 
        
                    The amount charged per the period of time specified by the recurring charge frequency.
        
                  - **RecurringChargeFrequency** *(string) --* 
        
                    The frequency at which the recurring charge amount is applied.
        
              - **ReservedNodeOfferingType** *(string) --* 
          
        """
        pass

    def reboot_cluster(self, ClusterIdentifier: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/RebootCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.reboot_cluster(
              ClusterIdentifier=\'string\'
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          The cluster identifier.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
                    \'ClusterIdentifier\': \'string\',
                    \'NodeType\': \'string\',
                    \'ClusterStatus\': \'string\',
                    \'ModifyStatus\': \'string\',
                    \'MasterUsername\': \'string\',
                    \'DBName\': \'string\',
                    \'Endpoint\': {
                        \'Address\': \'string\',
                        \'Port\': 123
                    },
                    \'ClusterCreateTime\': datetime(2015, 1, 1),
                    \'AutomatedSnapshotRetentionPeriod\': 123,
                    \'ClusterSecurityGroups\': [
                        {
                            \'ClusterSecurityGroupName\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'VpcSecurityGroups\': [
                        {
                            \'VpcSecurityGroupId\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'ClusterParameterGroups\': [
                        {
                            \'ParameterGroupName\': \'string\',
                            \'ParameterApplyStatus\': \'string\',
                            \'ClusterParameterStatusList\': [
                                {
                                    \'ParameterName\': \'string\',
                                    \'ParameterApplyStatus\': \'string\',
                                    \'ParameterApplyErrorDescription\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'ClusterSubnetGroupName\': \'string\',
                    \'VpcId\': \'string\',
                    \'AvailabilityZone\': \'string\',
                    \'PreferredMaintenanceWindow\': \'string\',
                    \'PendingModifiedValues\': {
                        \'MasterUserPassword\': \'string\',
                        \'NodeType\': \'string\',
                        \'NumberOfNodes\': 123,
                        \'ClusterType\': \'string\',
                        \'ClusterVersion\': \'string\',
                        \'AutomatedSnapshotRetentionPeriod\': 123,
                        \'ClusterIdentifier\': \'string\',
                        \'PubliclyAccessible\': True|False,
                        \'EnhancedVpcRouting\': True|False,
                        \'MaintenanceTrackName\': \'string\',
                        \'EncryptionType\': \'string\'
                    },
                    \'ClusterVersion\': \'string\',
                    \'AllowVersionUpgrade\': True|False,
                    \'NumberOfNodes\': 123,
                    \'PubliclyAccessible\': True|False,
                    \'Encrypted\': True|False,
                    \'RestoreStatus\': {
                        \'Status\': \'string\',
                        \'CurrentRestoreRateInMegaBytesPerSecond\': 123.0,
                        \'SnapshotSizeInMegaBytes\': 123,
                        \'ProgressInMegaBytes\': 123,
                        \'ElapsedTimeInSeconds\': 123,
                        \'EstimatedTimeToCompletionInSeconds\': 123
                    },
                    \'HsmStatus\': {
                        \'HsmClientCertificateIdentifier\': \'string\',
                        \'HsmConfigurationIdentifier\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterSnapshotCopyStatus\': {
                        \'DestinationRegion\': \'string\',
                        \'RetentionPeriod\': 123,
                        \'SnapshotCopyGrantName\': \'string\'
                    },
                    \'ClusterPublicKey\': \'string\',
                    \'ClusterNodes\': [
                        {
                            \'NodeRole\': \'string\',
                            \'PrivateIPAddress\': \'string\',
                            \'PublicIPAddress\': \'string\'
                        },
                    ],
                    \'ElasticIpStatus\': {
                        \'ElasticIp\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterRevisionNumber\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'KmsKeyId\': \'string\',
                    \'EnhancedVpcRouting\': True|False,
                    \'IamRoles\': [
                        {
                            \'IamRoleArn\': \'string\',
                            \'ApplyStatus\': \'string\'
                        },
                    ],
                    \'PendingActions\': [
                        \'string\',
                    ],
                    \'MaintenanceTrackName\': \'string\',
                    \'ElasticResizeNumberOfNodeOptions\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              Describes a cluster.
        
              - **ClusterIdentifier** *(string) --* 
        
                The unique identifier of the cluster.
        
              - **NodeType** *(string) --* 
        
                The node type for the nodes in the cluster.
        
              - **ClusterStatus** *(string) --* 
        
                The current state of the cluster. Possible values are the following:
        
                * ``available``   
                 
                * ``creating``   
                 
                * ``deleting``   
                 
                * ``final-snapshot``   
                 
                * ``hardware-failure``   
                 
                * ``incompatible-hsm``   
                 
                * ``incompatible-network``   
                 
                * ``incompatible-parameters``   
                 
                * ``incompatible-restore``   
                 
                * ``modifying``   
                 
                * ``rebooting``   
                 
                * ``renaming``   
                 
                * ``resizing``   
                 
                * ``rotating-keys``   
                 
                * ``storage-full``   
                 
                * ``updating-hsm``   
                 
              - **ModifyStatus** *(string) --* 
        
                The status of a modify operation, if any, initiated for the cluster.
        
              - **MasterUsername** *(string) --* 
        
                The master user name for the cluster. This name is used to connect to the database that is specified in the **DBName** parameter. 
        
              - **DBName** *(string) --* 
        
                The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named ``dev`` dev was created by default. 
        
              - **Endpoint** *(dict) --* 
        
                The connection endpoint.
        
                - **Address** *(string) --* 
        
                  The DNS address of the Cluster.
        
                - **Port** *(integer) --* 
        
                  The port that the database engine is listening on.
        
              - **ClusterCreateTime** *(datetime) --* 
        
                The date and time that the cluster was created.
        
              - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                The number of days that automatic cluster snapshots are retained.
        
              - **ClusterSecurityGroups** *(list) --* 
        
                A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ``ClusterSecurityGroup.Name`` and ``ClusterSecurityGroup.Status`` subelements. 
        
                Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the **VpcSecurityGroups** parameter. 
        
                - *(dict) --* 
        
                  Describes a cluster security group.
        
                  - **ClusterSecurityGroupName** *(string) --* 
        
                    The name of the cluster security group.
        
                  - **Status** *(string) --* 
        
                    The status of the cluster security group.
        
              - **VpcSecurityGroups** *(list) --* 
        
                A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.
        
                - *(dict) --* 
        
                  Describes the members of a VPC security group.
        
                  - **VpcSecurityGroupId** *(string) --* 
        
                    The identifier of the VPC security group.
        
                  - **Status** *(string) --* 
        
                    The status of the VPC security group.
        
              - **ClusterParameterGroups** *(list) --* 
        
                The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.
        
                - *(dict) --* 
        
                  Describes the status of a parameter group.
        
                  - **ParameterGroupName** *(string) --* 
        
                    The name of the cluster parameter group.
        
                  - **ParameterApplyStatus** *(string) --* 
        
                    The status of parameter updates.
        
                  - **ClusterParameterStatusList** *(list) --* 
        
                    The list of parameter statuses.
        
                    For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
                    - *(dict) --* 
        
                      Describes the status of a parameter group.
        
                      - **ParameterName** *(string) --* 
        
                        The name of the parameter.
        
                      - **ParameterApplyStatus** *(string) --* 
        
                        The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
        
                        The following are possible statuses and descriptions.
        
                        * ``in-sync`` : The parameter value is in sync with the database. 
                         
                        * ``pending-reboot`` : The parameter value will be applied after the cluster reboots. 
                         
                        * ``applying`` : The parameter value is being applied to the database. 
                         
                        * ``invalid-parameter`` : Cannot apply the parameter value because it has an invalid value or syntax. 
                         
                        * ``apply-deferred`` : The parameter contains static property changes. The changes are deferred until the cluster reboots. 
                         
                        * ``apply-error`` : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots. 
                         
                        * ``unknown-error`` : Cannot apply the parameter change right now. The change will be applied after the cluster reboots. 
                         
                      - **ParameterApplyErrorDescription** *(string) --* 
        
                        The error that prevented the parameter from being applied to the database.
        
              - **ClusterSubnetGroupName** *(string) --* 
        
                The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.
        
              - **VpcId** *(string) --* 
        
                The identifier of the VPC the cluster is in, if the cluster is in a VPC.
        
              - **AvailabilityZone** *(string) --* 
        
                The name of the Availability Zone in which the cluster is located.
        
              - **PreferredMaintenanceWindow** *(string) --* 
        
                The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.
        
              - **PendingModifiedValues** *(dict) --* 
        
                A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.
        
                - **MasterUserPassword** *(string) --* 
        
                  The pending or in-progress change of the master user password for the cluster.
        
                - **NodeType** *(string) --* 
        
                  The pending or in-progress change of the cluster\'s node type.
        
                - **NumberOfNodes** *(integer) --* 
        
                  The pending or in-progress change of the number of nodes in the cluster.
        
                - **ClusterType** *(string) --* 
        
                  The pending or in-progress change of the cluster type.
        
                - **ClusterVersion** *(string) --* 
        
                  The pending or in-progress change of the service version.
        
                - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                  The pending or in-progress change of the automated snapshot retention period.
        
                - **ClusterIdentifier** *(string) --* 
        
                  The pending or in-progress change of the new identifier for the cluster.
        
                - **PubliclyAccessible** *(boolean) --* 
        
                  The pending or in-progress change of the ability to connect to the cluster from the public network.
        
                - **EnhancedVpcRouting** *(boolean) --* 
        
                  An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                  If this option is ``true`` , enhanced VPC routing is enabled. 
        
                  Default: false
        
                - **MaintenanceTrackName** *(string) --* 
        
                  The name of the maintenance track that the cluster will change to during the next maintenance window.
        
                - **EncryptionType** *(string) --* 
        
                  The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy. 
        
              - **ClusterVersion** *(string) --* 
        
                The version ID of the Amazon Redshift engine that is running on the cluster.
        
              - **AllowVersionUpgrade** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window. 
        
              - **NumberOfNodes** *(integer) --* 
        
                The number of compute nodes in the cluster.
        
              - **PubliclyAccessible** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that the cluster can be accessed from a public network.
        
              - **Encrypted** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that data in the cluster is encrypted at rest.
        
              - **RestoreStatus** *(dict) --* 
        
                A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.
        
                - **Status** *(string) --* 
        
                  The status of the restore action. Returns starting, restoring, completed, or failed.
        
                - **CurrentRestoreRateInMegaBytesPerSecond** *(float) --* 
        
                  The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.
        
                - **SnapshotSizeInMegaBytes** *(integer) --* 
        
                  The size of the set of snapshot data used to restore the cluster.
        
                - **ProgressInMegaBytes** *(integer) --* 
        
                  The number of megabytes that have been transferred from snapshot storage.
        
                - **ElapsedTimeInSeconds** *(integer) --* 
        
                  The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.
        
                - **EstimatedTimeToCompletionInSeconds** *(integer) --* 
        
                  The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore.
        
              - **HsmStatus** *(dict) --* 
        
                A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
        
                Values: active, applying
        
                - **HsmClientCertificateIdentifier** *(string) --* 
        
                  Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        
                - **HsmConfigurationIdentifier** *(string) --* 
        
                  Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        
                - **Status** *(string) --* 
        
                  Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
        
                  Values: active, applying
        
              - **ClusterSnapshotCopyStatus** *(dict) --* 
        
                A value that returns the destination region and retention period that are configured for cross-region snapshot copy.
        
                - **DestinationRegion** *(string) --* 
        
                  The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
        
                - **RetentionPeriod** *(integer) --* 
        
                  The number of days that automated snapshots are retained in the destination region after they are copied from a source region.
        
                - **SnapshotCopyGrantName** *(string) --* 
        
                  The name of the snapshot copy grant.
        
              - **ClusterPublicKey** *(string) --* 
        
                The public key for the cluster.
        
              - **ClusterNodes** *(list) --* 
        
                The nodes in the cluster.
        
                - *(dict) --* 
        
                  The identifier of a node in a cluster.
        
                  - **NodeRole** *(string) --* 
        
                    Whether the node is a leader node or a compute node.
        
                  - **PrivateIPAddress** *(string) --* 
        
                    The private IP address of a node within a cluster.
        
                  - **PublicIPAddress** *(string) --* 
        
                    The public IP address of a node within a cluster.
        
              - **ElasticIpStatus** *(dict) --* 
        
                The status of the elastic IP (EIP) address.
        
                - **ElasticIp** *(string) --* 
        
                  The elastic IP (EIP) address for the cluster.
        
                - **Status** *(string) --* 
        
                  The status of the elastic IP (EIP) address.
        
              - **ClusterRevisionNumber** *(string) --* 
        
                The specific revision number of the database in the cluster.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.
        
              - **EnhancedVpcRouting** *(boolean) --* 
        
                An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                If this option is ``true`` , enhanced VPC routing is enabled. 
        
                Default: false
        
              - **IamRoles** *(list) --* 
        
                A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.
        
                - *(dict) --* 
        
                  An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.
        
                  - **IamRoleArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the IAM role, for example, ``arn:aws:iam::123456789012:role/RedshiftCopyUnload`` . 
        
                  - **ApplyStatus** *(string) --* 
        
                    A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
        
                    The following are possible statuses and descriptions.
        
                    * ``in-sync`` : The role is available for use by the cluster. 
                     
                    * ``adding`` : The role is in the process of being associated with the cluster. 
                     
                    * ``removing`` : The role is in the process of being disassociated with the cluster. 
                     
              - **PendingActions** *(list) --* 
        
                Cluster operations that are waiting to be started.
        
                - *(string) --* 
            
              - **MaintenanceTrackName** *(string) --* 
        
                The name of the maintenance track for the cluster.
        
              - **ElasticResizeNumberOfNodeOptions** *(string) --* 
        
                Indicates the number of nodes the cluster can be resized to with the elastic resize method. 
        
        """
        pass

    def reset_cluster_parameter_group(self, ParameterGroupName: str, ResetAllParameters: bool = None, Parameters: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/ResetClusterParameterGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.reset_cluster_parameter_group(
              ParameterGroupName=\'string\',
              ResetAllParameters=True|False,
              Parameters=[
                  {
                      \'ParameterName\': \'string\',
                      \'ParameterValue\': \'string\',
                      \'Description\': \'string\',
                      \'Source\': \'string\',
                      \'DataType\': \'string\',
                      \'AllowedValues\': \'string\',
                      \'ApplyType\': \'static\'|\'dynamic\',
                      \'IsModifiable\': True|False,
                      \'MinimumEngineVersion\': \'string\'
                  },
              ]
          )
        :type ParameterGroupName: string
        :param ParameterGroupName: **[REQUIRED]** 
        
          The name of the cluster parameter group to be reset.
        
        :type ResetAllParameters: boolean
        :param ResetAllParameters: 
        
          If ``true`` , all parameters in the specified parameter group will be reset to their default values. 
        
          Default: ``true``  
        
        :type Parameters: list
        :param Parameters: 
        
          An array of names of parameters to be reset. If *ResetAllParameters* option is not used, then at least one parameter name must be supplied. 
        
          Constraints: A maximum of 20 parameters can be reset in a single request.
        
          - *(dict) --* 
        
            Describes a parameter in a cluster parameter group.
        
            - **ParameterName** *(string) --* 
        
              The name of the parameter.
        
            - **ParameterValue** *(string) --* 
        
              The value of the parameter.
        
            - **Description** *(string) --* 
        
              A description of the parameter.
        
            - **Source** *(string) --* 
        
              The source of the parameter value, such as \"engine-default\" or \"user\".
        
            - **DataType** *(string) --* 
        
              The data type of the parameter.
        
            - **AllowedValues** *(string) --* 
        
              The valid range of values for the parameter.
        
            - **ApplyType** *(string) --* 
        
              Specifies how to apply the WLM configuration parameter. Some properties can be applied dynamically, while other properties require that any associated clusters be rebooted for the configuration changes to be applied. For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
            - **IsModifiable** *(boolean) --* 
        
              If ``true`` , the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed. 
        
            - **MinimumEngineVersion** *(string) --* 
        
              The earliest engine version to which the parameter can apply.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ParameterGroupName\': \'string\',
                \'ParameterGroupStatus\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ParameterGroupName** *(string) --* 
        
              The name of the cluster parameter group.
        
            - **ParameterGroupStatus** *(string) --* 
        
              The status of the parameter group. For example, if you made a change to a parameter group name-value pair, then the change could be pending a reboot of an associated cluster.
        
        """
        pass

    def resize_cluster(self, ClusterIdentifier: str, NumberOfNodes: int, ClusterType: str = None, NodeType: str = None, Classic: bool = None) -> Dict:
        """
        
        Elastic resize operations have the following restrictions:
        
        * You can only resize clusters of the following types: 
        
          * dc2.large 
           
          * dc2.8xlarge 
           
          * ds2.xlarge 
           
          * ds2.8xlarge 
           
        * The type of nodes you add must match the node type for the cluster. 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/ResizeCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.resize_cluster(
              ClusterIdentifier=\'string\',
              ClusterType=\'string\',
              NodeType=\'string\',
              NumberOfNodes=123,
              Classic=True|False
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          The unique identifier for the cluster to resize.
        
        :type ClusterType: string
        :param ClusterType: 
        
          The new cluster type for the specified cluster.
        
        :type NodeType: string
        :param NodeType: 
        
          The new node type for the nodes you are adding.
        
        :type NumberOfNodes: integer
        :param NumberOfNodes: **[REQUIRED]** 
        
          The new number of nodes for the cluster.
        
        :type Classic: boolean
        :param Classic: 
        
          A boolean value indicating whether the resize operation is using the classic resize process. If you don\'t provide this parameter or set the value to ``false`` the resize type is elastic. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
                    \'ClusterIdentifier\': \'string\',
                    \'NodeType\': \'string\',
                    \'ClusterStatus\': \'string\',
                    \'ModifyStatus\': \'string\',
                    \'MasterUsername\': \'string\',
                    \'DBName\': \'string\',
                    \'Endpoint\': {
                        \'Address\': \'string\',
                        \'Port\': 123
                    },
                    \'ClusterCreateTime\': datetime(2015, 1, 1),
                    \'AutomatedSnapshotRetentionPeriod\': 123,
                    \'ClusterSecurityGroups\': [
                        {
                            \'ClusterSecurityGroupName\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'VpcSecurityGroups\': [
                        {
                            \'VpcSecurityGroupId\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'ClusterParameterGroups\': [
                        {
                            \'ParameterGroupName\': \'string\',
                            \'ParameterApplyStatus\': \'string\',
                            \'ClusterParameterStatusList\': [
                                {
                                    \'ParameterName\': \'string\',
                                    \'ParameterApplyStatus\': \'string\',
                                    \'ParameterApplyErrorDescription\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'ClusterSubnetGroupName\': \'string\',
                    \'VpcId\': \'string\',
                    \'AvailabilityZone\': \'string\',
                    \'PreferredMaintenanceWindow\': \'string\',
                    \'PendingModifiedValues\': {
                        \'MasterUserPassword\': \'string\',
                        \'NodeType\': \'string\',
                        \'NumberOfNodes\': 123,
                        \'ClusterType\': \'string\',
                        \'ClusterVersion\': \'string\',
                        \'AutomatedSnapshotRetentionPeriod\': 123,
                        \'ClusterIdentifier\': \'string\',
                        \'PubliclyAccessible\': True|False,
                        \'EnhancedVpcRouting\': True|False,
                        \'MaintenanceTrackName\': \'string\',
                        \'EncryptionType\': \'string\'
                    },
                    \'ClusterVersion\': \'string\',
                    \'AllowVersionUpgrade\': True|False,
                    \'NumberOfNodes\': 123,
                    \'PubliclyAccessible\': True|False,
                    \'Encrypted\': True|False,
                    \'RestoreStatus\': {
                        \'Status\': \'string\',
                        \'CurrentRestoreRateInMegaBytesPerSecond\': 123.0,
                        \'SnapshotSizeInMegaBytes\': 123,
                        \'ProgressInMegaBytes\': 123,
                        \'ElapsedTimeInSeconds\': 123,
                        \'EstimatedTimeToCompletionInSeconds\': 123
                    },
                    \'HsmStatus\': {
                        \'HsmClientCertificateIdentifier\': \'string\',
                        \'HsmConfigurationIdentifier\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterSnapshotCopyStatus\': {
                        \'DestinationRegion\': \'string\',
                        \'RetentionPeriod\': 123,
                        \'SnapshotCopyGrantName\': \'string\'
                    },
                    \'ClusterPublicKey\': \'string\',
                    \'ClusterNodes\': [
                        {
                            \'NodeRole\': \'string\',
                            \'PrivateIPAddress\': \'string\',
                            \'PublicIPAddress\': \'string\'
                        },
                    ],
                    \'ElasticIpStatus\': {
                        \'ElasticIp\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterRevisionNumber\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'KmsKeyId\': \'string\',
                    \'EnhancedVpcRouting\': True|False,
                    \'IamRoles\': [
                        {
                            \'IamRoleArn\': \'string\',
                            \'ApplyStatus\': \'string\'
                        },
                    ],
                    \'PendingActions\': [
                        \'string\',
                    ],
                    \'MaintenanceTrackName\': \'string\',
                    \'ElasticResizeNumberOfNodeOptions\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              Describes a cluster.
        
              - **ClusterIdentifier** *(string) --* 
        
                The unique identifier of the cluster.
        
              - **NodeType** *(string) --* 
        
                The node type for the nodes in the cluster.
        
              - **ClusterStatus** *(string) --* 
        
                The current state of the cluster. Possible values are the following:
        
                * ``available``   
                 
                * ``creating``   
                 
                * ``deleting``   
                 
                * ``final-snapshot``   
                 
                * ``hardware-failure``   
                 
                * ``incompatible-hsm``   
                 
                * ``incompatible-network``   
                 
                * ``incompatible-parameters``   
                 
                * ``incompatible-restore``   
                 
                * ``modifying``   
                 
                * ``rebooting``   
                 
                * ``renaming``   
                 
                * ``resizing``   
                 
                * ``rotating-keys``   
                 
                * ``storage-full``   
                 
                * ``updating-hsm``   
                 
              - **ModifyStatus** *(string) --* 
        
                The status of a modify operation, if any, initiated for the cluster.
        
              - **MasterUsername** *(string) --* 
        
                The master user name for the cluster. This name is used to connect to the database that is specified in the **DBName** parameter. 
        
              - **DBName** *(string) --* 
        
                The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named ``dev`` dev was created by default. 
        
              - **Endpoint** *(dict) --* 
        
                The connection endpoint.
        
                - **Address** *(string) --* 
        
                  The DNS address of the Cluster.
        
                - **Port** *(integer) --* 
        
                  The port that the database engine is listening on.
        
              - **ClusterCreateTime** *(datetime) --* 
        
                The date and time that the cluster was created.
        
              - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                The number of days that automatic cluster snapshots are retained.
        
              - **ClusterSecurityGroups** *(list) --* 
        
                A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ``ClusterSecurityGroup.Name`` and ``ClusterSecurityGroup.Status`` subelements. 
        
                Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the **VpcSecurityGroups** parameter. 
        
                - *(dict) --* 
        
                  Describes a cluster security group.
        
                  - **ClusterSecurityGroupName** *(string) --* 
        
                    The name of the cluster security group.
        
                  - **Status** *(string) --* 
        
                    The status of the cluster security group.
        
              - **VpcSecurityGroups** *(list) --* 
        
                A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.
        
                - *(dict) --* 
        
                  Describes the members of a VPC security group.
        
                  - **VpcSecurityGroupId** *(string) --* 
        
                    The identifier of the VPC security group.
        
                  - **Status** *(string) --* 
        
                    The status of the VPC security group.
        
              - **ClusterParameterGroups** *(list) --* 
        
                The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.
        
                - *(dict) --* 
        
                  Describes the status of a parameter group.
        
                  - **ParameterGroupName** *(string) --* 
        
                    The name of the cluster parameter group.
        
                  - **ParameterApplyStatus** *(string) --* 
        
                    The status of parameter updates.
        
                  - **ClusterParameterStatusList** *(list) --* 
        
                    The list of parameter statuses.
        
                    For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
                    - *(dict) --* 
        
                      Describes the status of a parameter group.
        
                      - **ParameterName** *(string) --* 
        
                        The name of the parameter.
        
                      - **ParameterApplyStatus** *(string) --* 
        
                        The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
        
                        The following are possible statuses and descriptions.
        
                        * ``in-sync`` : The parameter value is in sync with the database. 
                         
                        * ``pending-reboot`` : The parameter value will be applied after the cluster reboots. 
                         
                        * ``applying`` : The parameter value is being applied to the database. 
                         
                        * ``invalid-parameter`` : Cannot apply the parameter value because it has an invalid value or syntax. 
                         
                        * ``apply-deferred`` : The parameter contains static property changes. The changes are deferred until the cluster reboots. 
                         
                        * ``apply-error`` : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots. 
                         
                        * ``unknown-error`` : Cannot apply the parameter change right now. The change will be applied after the cluster reboots. 
                         
                      - **ParameterApplyErrorDescription** *(string) --* 
        
                        The error that prevented the parameter from being applied to the database.
        
              - **ClusterSubnetGroupName** *(string) --* 
        
                The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.
        
              - **VpcId** *(string) --* 
        
                The identifier of the VPC the cluster is in, if the cluster is in a VPC.
        
              - **AvailabilityZone** *(string) --* 
        
                The name of the Availability Zone in which the cluster is located.
        
              - **PreferredMaintenanceWindow** *(string) --* 
        
                The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.
        
              - **PendingModifiedValues** *(dict) --* 
        
                A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.
        
                - **MasterUserPassword** *(string) --* 
        
                  The pending or in-progress change of the master user password for the cluster.
        
                - **NodeType** *(string) --* 
        
                  The pending or in-progress change of the cluster\'s node type.
        
                - **NumberOfNodes** *(integer) --* 
        
                  The pending or in-progress change of the number of nodes in the cluster.
        
                - **ClusterType** *(string) --* 
        
                  The pending or in-progress change of the cluster type.
        
                - **ClusterVersion** *(string) --* 
        
                  The pending or in-progress change of the service version.
        
                - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                  The pending or in-progress change of the automated snapshot retention period.
        
                - **ClusterIdentifier** *(string) --* 
        
                  The pending or in-progress change of the new identifier for the cluster.
        
                - **PubliclyAccessible** *(boolean) --* 
        
                  The pending or in-progress change of the ability to connect to the cluster from the public network.
        
                - **EnhancedVpcRouting** *(boolean) --* 
        
                  An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                  If this option is ``true`` , enhanced VPC routing is enabled. 
        
                  Default: false
        
                - **MaintenanceTrackName** *(string) --* 
        
                  The name of the maintenance track that the cluster will change to during the next maintenance window.
        
                - **EncryptionType** *(string) --* 
        
                  The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy. 
        
              - **ClusterVersion** *(string) --* 
        
                The version ID of the Amazon Redshift engine that is running on the cluster.
        
              - **AllowVersionUpgrade** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window. 
        
              - **NumberOfNodes** *(integer) --* 
        
                The number of compute nodes in the cluster.
        
              - **PubliclyAccessible** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that the cluster can be accessed from a public network.
        
              - **Encrypted** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that data in the cluster is encrypted at rest.
        
              - **RestoreStatus** *(dict) --* 
        
                A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.
        
                - **Status** *(string) --* 
        
                  The status of the restore action. Returns starting, restoring, completed, or failed.
        
                - **CurrentRestoreRateInMegaBytesPerSecond** *(float) --* 
        
                  The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.
        
                - **SnapshotSizeInMegaBytes** *(integer) --* 
        
                  The size of the set of snapshot data used to restore the cluster.
        
                - **ProgressInMegaBytes** *(integer) --* 
        
                  The number of megabytes that have been transferred from snapshot storage.
        
                - **ElapsedTimeInSeconds** *(integer) --* 
        
                  The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.
        
                - **EstimatedTimeToCompletionInSeconds** *(integer) --* 
        
                  The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore.
        
              - **HsmStatus** *(dict) --* 
        
                A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
        
                Values: active, applying
        
                - **HsmClientCertificateIdentifier** *(string) --* 
        
                  Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        
                - **HsmConfigurationIdentifier** *(string) --* 
        
                  Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        
                - **Status** *(string) --* 
        
                  Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
        
                  Values: active, applying
        
              - **ClusterSnapshotCopyStatus** *(dict) --* 
        
                A value that returns the destination region and retention period that are configured for cross-region snapshot copy.
        
                - **DestinationRegion** *(string) --* 
        
                  The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
        
                - **RetentionPeriod** *(integer) --* 
        
                  The number of days that automated snapshots are retained in the destination region after they are copied from a source region.
        
                - **SnapshotCopyGrantName** *(string) --* 
        
                  The name of the snapshot copy grant.
        
              - **ClusterPublicKey** *(string) --* 
        
                The public key for the cluster.
        
              - **ClusterNodes** *(list) --* 
        
                The nodes in the cluster.
        
                - *(dict) --* 
        
                  The identifier of a node in a cluster.
        
                  - **NodeRole** *(string) --* 
        
                    Whether the node is a leader node or a compute node.
        
                  - **PrivateIPAddress** *(string) --* 
        
                    The private IP address of a node within a cluster.
        
                  - **PublicIPAddress** *(string) --* 
        
                    The public IP address of a node within a cluster.
        
              - **ElasticIpStatus** *(dict) --* 
        
                The status of the elastic IP (EIP) address.
        
                - **ElasticIp** *(string) --* 
        
                  The elastic IP (EIP) address for the cluster.
        
                - **Status** *(string) --* 
        
                  The status of the elastic IP (EIP) address.
        
              - **ClusterRevisionNumber** *(string) --* 
        
                The specific revision number of the database in the cluster.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.
        
              - **EnhancedVpcRouting** *(boolean) --* 
        
                An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                If this option is ``true`` , enhanced VPC routing is enabled. 
        
                Default: false
        
              - **IamRoles** *(list) --* 
        
                A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.
        
                - *(dict) --* 
        
                  An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.
        
                  - **IamRoleArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the IAM role, for example, ``arn:aws:iam::123456789012:role/RedshiftCopyUnload`` . 
        
                  - **ApplyStatus** *(string) --* 
        
                    A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
        
                    The following are possible statuses and descriptions.
        
                    * ``in-sync`` : The role is available for use by the cluster. 
                     
                    * ``adding`` : The role is in the process of being associated with the cluster. 
                     
                    * ``removing`` : The role is in the process of being disassociated with the cluster. 
                     
              - **PendingActions** *(list) --* 
        
                Cluster operations that are waiting to be started.
        
                - *(string) --* 
            
              - **MaintenanceTrackName** *(string) --* 
        
                The name of the maintenance track for the cluster.
        
              - **ElasticResizeNumberOfNodeOptions** *(string) --* 
        
                Indicates the number of nodes the cluster can be resized to with the elastic resize method. 
        
        """
        pass

    def restore_from_cluster_snapshot(self, ClusterIdentifier: str, SnapshotIdentifier: str, SnapshotClusterIdentifier: str = None, Port: int = None, AvailabilityZone: str = None, AllowVersionUpgrade: bool = None, ClusterSubnetGroupName: str = None, PubliclyAccessible: bool = None, OwnerAccount: str = None, HsmClientCertificateIdentifier: str = None, HsmConfigurationIdentifier: str = None, ElasticIp: str = None, ClusterParameterGroupName: str = None, ClusterSecurityGroups: List = None, VpcSecurityGroupIds: List = None, PreferredMaintenanceWindow: str = None, AutomatedSnapshotRetentionPeriod: int = None, KmsKeyId: str = None, NodeType: str = None, EnhancedVpcRouting: bool = None, AdditionalInfo: str = None, IamRoles: List = None, MaintenanceTrackName: str = None) -> Dict:
        """
        
        If you restore a cluster into a VPC, you must provide a cluster subnet group where you want the cluster restored.
        
        For more information about working with snapshots, go to `Amazon Redshift Snapshots <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/RestoreFromClusterSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.restore_from_cluster_snapshot(
              ClusterIdentifier=\'string\',
              SnapshotIdentifier=\'string\',
              SnapshotClusterIdentifier=\'string\',
              Port=123,
              AvailabilityZone=\'string\',
              AllowVersionUpgrade=True|False,
              ClusterSubnetGroupName=\'string\',
              PubliclyAccessible=True|False,
              OwnerAccount=\'string\',
              HsmClientCertificateIdentifier=\'string\',
              HsmConfigurationIdentifier=\'string\',
              ElasticIp=\'string\',
              ClusterParameterGroupName=\'string\',
              ClusterSecurityGroups=[
                  \'string\',
              ],
              VpcSecurityGroupIds=[
                  \'string\',
              ],
              PreferredMaintenanceWindow=\'string\',
              AutomatedSnapshotRetentionPeriod=123,
              KmsKeyId=\'string\',
              NodeType=\'string\',
              EnhancedVpcRouting=True|False,
              AdditionalInfo=\'string\',
              IamRoles=[
                  \'string\',
              ],
              MaintenanceTrackName=\'string\'
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          The identifier of the cluster that will be created from restoring the snapshot.
        
          Constraints:
        
          * Must contain from 1 to 63 alphanumeric characters or hyphens. 
           
          * Alphabetic characters must be lowercase. 
           
          * First character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
          * Must be unique for all clusters within an AWS account. 
           
        :type SnapshotIdentifier: string
        :param SnapshotIdentifier: **[REQUIRED]** 
        
          The name of the snapshot from which to create the new cluster. This parameter isn\'t case sensitive.
        
          Example: ``my-snapshot-id``  
        
        :type SnapshotClusterIdentifier: string
        :param SnapshotClusterIdentifier: 
        
          The name of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
        
        :type Port: integer
        :param Port: 
        
          The port number on which the cluster accepts connections.
        
          Default: The same port as the original cluster.
        
          Constraints: Must be between ``1115`` and ``65535`` .
        
        :type AvailabilityZone: string
        :param AvailabilityZone: 
        
          The Amazon EC2 Availability Zone in which to restore the cluster.
        
          Default: A random, system-chosen Availability Zone.
        
          Example: ``us-east-1a``  
        
        :type AllowVersionUpgrade: boolean
        :param AllowVersionUpgrade: 
        
          If ``true`` , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. 
        
          Default: ``true``  
        
        :type ClusterSubnetGroupName: string
        :param ClusterSubnetGroupName: 
        
          The name of the subnet group where you want to cluster restored.
        
          A snapshot of cluster in VPC can be restored only in VPC. Therefore, you must provide subnet group name where you want the cluster restored.
        
        :type PubliclyAccessible: boolean
        :param PubliclyAccessible: 
        
          If ``true`` , the cluster can be accessed from a public network. 
        
        :type OwnerAccount: string
        :param OwnerAccount: 
        
          The AWS customer account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.
        
        :type HsmClientCertificateIdentifier: string
        :param HsmClientCertificateIdentifier: 
        
          Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        
        :type HsmConfigurationIdentifier: string
        :param HsmConfigurationIdentifier: 
        
          Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        
        :type ElasticIp: string
        :param ElasticIp: 
        
          The elastic IP (EIP) address for the cluster.
        
        :type ClusterParameterGroupName: string
        :param ClusterParameterGroupName: 
        
          The name of the parameter group to be associated with this cluster.
        
          Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to `Working with Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ .
        
          Constraints:
        
          * Must be 1 to 255 alphanumeric characters or hyphens. 
           
          * First character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
        :type ClusterSecurityGroups: list
        :param ClusterSecurityGroups: 
        
          A list of security groups to be associated with this cluster.
        
          Default: The default cluster security group for Amazon Redshift.
        
          Cluster security groups only apply to clusters outside of VPCs.
        
          - *(string) --* 
        
        :type VpcSecurityGroupIds: list
        :param VpcSecurityGroupIds: 
        
          A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.
        
          Default: The default VPC security group is associated with the cluster.
        
          VPC security groups only apply to clusters in VPCs.
        
          - *(string) --* 
        
        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow: 
        
          The weekly time range (in UTC) during which automated cluster maintenance can occur.
        
          Format: ``ddd:hh24:mi-ddd:hh24:mi``  
        
          Default: The value selected for the cluster from which the snapshot was taken. For more information about the time blocks for each region, see `Maintenance Windows <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-maintenance-windows>`__ in Amazon Redshift Cluster Management Guide. 
        
          Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun
        
          Constraints: Minimum 30-minute window.
        
        :type AutomatedSnapshotRetentionPeriod: integer
        :param AutomatedSnapshotRetentionPeriod: 
        
          The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with  CreateClusterSnapshot . 
        
          Default: The value selected for the cluster from which the snapshot was taken.
        
          Constraints: Must be a value from 0 to 35.
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster that you restore from a shared snapshot.
        
        :type NodeType: string
        :param NodeType: 
        
          The node type that the restored cluster will be provisioned with.
        
          Default: The node type of the cluster from which the snapshot was taken. You can modify this if you are using any DS node type. In that case, you can choose to restore into another DS node type of the same size. For example, you can restore ds1.8xlarge into ds2.8xlarge, or ds1.xlarge into ds2.xlarge. If you have a DC instance type, you must restore into that same instance type and size. In other words, you can only restore a dc1.large instance type into another dc1.large instance type or dc2.large instance type. You can\'t restore dc1.8xlarge to dc2.8xlarge. First restore to a dc1.8xlareg cluster, then resize to a dc2.8large cluster. For more information about node types, see `About Clusters and Nodes <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-about-clusters-and-nodes>`__ in the *Amazon Redshift Cluster Management Guide* . 
        
        :type EnhancedVpcRouting: boolean
        :param EnhancedVpcRouting: 
        
          An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
          If this option is ``true`` , enhanced VPC routing is enabled. 
        
          Default: false
        
        :type AdditionalInfo: string
        :param AdditionalInfo: 
        
          Reserved.
        
        :type IamRoles: list
        :param IamRoles: 
        
          A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. You can supply up to 10 IAM roles in a single request.
        
          A cluster can have up to 10 IAM roles associated at any time.
        
          - *(string) --* 
        
        :type MaintenanceTrackName: string
        :param MaintenanceTrackName: 
        
          The name of the maintenance track for the restored cluster. When you take a snapshot, the snapshot inherits the ``MaintenanceTrack`` value from the cluster. The snapshot might be on a different track than the cluster that was the source for the snapshot. For example, suppose that you take a snapshot of a cluster that is on the current track and then change the cluster to be on the trailing track. In this case, the snapshot and the source cluster are on different tracks.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
                    \'ClusterIdentifier\': \'string\',
                    \'NodeType\': \'string\',
                    \'ClusterStatus\': \'string\',
                    \'ModifyStatus\': \'string\',
                    \'MasterUsername\': \'string\',
                    \'DBName\': \'string\',
                    \'Endpoint\': {
                        \'Address\': \'string\',
                        \'Port\': 123
                    },
                    \'ClusterCreateTime\': datetime(2015, 1, 1),
                    \'AutomatedSnapshotRetentionPeriod\': 123,
                    \'ClusterSecurityGroups\': [
                        {
                            \'ClusterSecurityGroupName\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'VpcSecurityGroups\': [
                        {
                            \'VpcSecurityGroupId\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'ClusterParameterGroups\': [
                        {
                            \'ParameterGroupName\': \'string\',
                            \'ParameterApplyStatus\': \'string\',
                            \'ClusterParameterStatusList\': [
                                {
                                    \'ParameterName\': \'string\',
                                    \'ParameterApplyStatus\': \'string\',
                                    \'ParameterApplyErrorDescription\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'ClusterSubnetGroupName\': \'string\',
                    \'VpcId\': \'string\',
                    \'AvailabilityZone\': \'string\',
                    \'PreferredMaintenanceWindow\': \'string\',
                    \'PendingModifiedValues\': {
                        \'MasterUserPassword\': \'string\',
                        \'NodeType\': \'string\',
                        \'NumberOfNodes\': 123,
                        \'ClusterType\': \'string\',
                        \'ClusterVersion\': \'string\',
                        \'AutomatedSnapshotRetentionPeriod\': 123,
                        \'ClusterIdentifier\': \'string\',
                        \'PubliclyAccessible\': True|False,
                        \'EnhancedVpcRouting\': True|False,
                        \'MaintenanceTrackName\': \'string\',
                        \'EncryptionType\': \'string\'
                    },
                    \'ClusterVersion\': \'string\',
                    \'AllowVersionUpgrade\': True|False,
                    \'NumberOfNodes\': 123,
                    \'PubliclyAccessible\': True|False,
                    \'Encrypted\': True|False,
                    \'RestoreStatus\': {
                        \'Status\': \'string\',
                        \'CurrentRestoreRateInMegaBytesPerSecond\': 123.0,
                        \'SnapshotSizeInMegaBytes\': 123,
                        \'ProgressInMegaBytes\': 123,
                        \'ElapsedTimeInSeconds\': 123,
                        \'EstimatedTimeToCompletionInSeconds\': 123
                    },
                    \'HsmStatus\': {
                        \'HsmClientCertificateIdentifier\': \'string\',
                        \'HsmConfigurationIdentifier\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterSnapshotCopyStatus\': {
                        \'DestinationRegion\': \'string\',
                        \'RetentionPeriod\': 123,
                        \'SnapshotCopyGrantName\': \'string\'
                    },
                    \'ClusterPublicKey\': \'string\',
                    \'ClusterNodes\': [
                        {
                            \'NodeRole\': \'string\',
                            \'PrivateIPAddress\': \'string\',
                            \'PublicIPAddress\': \'string\'
                        },
                    ],
                    \'ElasticIpStatus\': {
                        \'ElasticIp\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterRevisionNumber\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'KmsKeyId\': \'string\',
                    \'EnhancedVpcRouting\': True|False,
                    \'IamRoles\': [
                        {
                            \'IamRoleArn\': \'string\',
                            \'ApplyStatus\': \'string\'
                        },
                    ],
                    \'PendingActions\': [
                        \'string\',
                    ],
                    \'MaintenanceTrackName\': \'string\',
                    \'ElasticResizeNumberOfNodeOptions\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              Describes a cluster.
        
              - **ClusterIdentifier** *(string) --* 
        
                The unique identifier of the cluster.
        
              - **NodeType** *(string) --* 
        
                The node type for the nodes in the cluster.
        
              - **ClusterStatus** *(string) --* 
        
                The current state of the cluster. Possible values are the following:
        
                * ``available``   
                 
                * ``creating``   
                 
                * ``deleting``   
                 
                * ``final-snapshot``   
                 
                * ``hardware-failure``   
                 
                * ``incompatible-hsm``   
                 
                * ``incompatible-network``   
                 
                * ``incompatible-parameters``   
                 
                * ``incompatible-restore``   
                 
                * ``modifying``   
                 
                * ``rebooting``   
                 
                * ``renaming``   
                 
                * ``resizing``   
                 
                * ``rotating-keys``   
                 
                * ``storage-full``   
                 
                * ``updating-hsm``   
                 
              - **ModifyStatus** *(string) --* 
        
                The status of a modify operation, if any, initiated for the cluster.
        
              - **MasterUsername** *(string) --* 
        
                The master user name for the cluster. This name is used to connect to the database that is specified in the **DBName** parameter. 
        
              - **DBName** *(string) --* 
        
                The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named ``dev`` dev was created by default. 
        
              - **Endpoint** *(dict) --* 
        
                The connection endpoint.
        
                - **Address** *(string) --* 
        
                  The DNS address of the Cluster.
        
                - **Port** *(integer) --* 
        
                  The port that the database engine is listening on.
        
              - **ClusterCreateTime** *(datetime) --* 
        
                The date and time that the cluster was created.
        
              - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                The number of days that automatic cluster snapshots are retained.
        
              - **ClusterSecurityGroups** *(list) --* 
        
                A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ``ClusterSecurityGroup.Name`` and ``ClusterSecurityGroup.Status`` subelements. 
        
                Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the **VpcSecurityGroups** parameter. 
        
                - *(dict) --* 
        
                  Describes a cluster security group.
        
                  - **ClusterSecurityGroupName** *(string) --* 
        
                    The name of the cluster security group.
        
                  - **Status** *(string) --* 
        
                    The status of the cluster security group.
        
              - **VpcSecurityGroups** *(list) --* 
        
                A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.
        
                - *(dict) --* 
        
                  Describes the members of a VPC security group.
        
                  - **VpcSecurityGroupId** *(string) --* 
        
                    The identifier of the VPC security group.
        
                  - **Status** *(string) --* 
        
                    The status of the VPC security group.
        
              - **ClusterParameterGroups** *(list) --* 
        
                The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.
        
                - *(dict) --* 
        
                  Describes the status of a parameter group.
        
                  - **ParameterGroupName** *(string) --* 
        
                    The name of the cluster parameter group.
        
                  - **ParameterApplyStatus** *(string) --* 
        
                    The status of parameter updates.
        
                  - **ClusterParameterStatusList** *(list) --* 
        
                    The list of parameter statuses.
        
                    For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
                    - *(dict) --* 
        
                      Describes the status of a parameter group.
        
                      - **ParameterName** *(string) --* 
        
                        The name of the parameter.
        
                      - **ParameterApplyStatus** *(string) --* 
        
                        The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
        
                        The following are possible statuses and descriptions.
        
                        * ``in-sync`` : The parameter value is in sync with the database. 
                         
                        * ``pending-reboot`` : The parameter value will be applied after the cluster reboots. 
                         
                        * ``applying`` : The parameter value is being applied to the database. 
                         
                        * ``invalid-parameter`` : Cannot apply the parameter value because it has an invalid value or syntax. 
                         
                        * ``apply-deferred`` : The parameter contains static property changes. The changes are deferred until the cluster reboots. 
                         
                        * ``apply-error`` : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots. 
                         
                        * ``unknown-error`` : Cannot apply the parameter change right now. The change will be applied after the cluster reboots. 
                         
                      - **ParameterApplyErrorDescription** *(string) --* 
        
                        The error that prevented the parameter from being applied to the database.
        
              - **ClusterSubnetGroupName** *(string) --* 
        
                The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.
        
              - **VpcId** *(string) --* 
        
                The identifier of the VPC the cluster is in, if the cluster is in a VPC.
        
              - **AvailabilityZone** *(string) --* 
        
                The name of the Availability Zone in which the cluster is located.
        
              - **PreferredMaintenanceWindow** *(string) --* 
        
                The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.
        
              - **PendingModifiedValues** *(dict) --* 
        
                A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.
        
                - **MasterUserPassword** *(string) --* 
        
                  The pending or in-progress change of the master user password for the cluster.
        
                - **NodeType** *(string) --* 
        
                  The pending or in-progress change of the cluster\'s node type.
        
                - **NumberOfNodes** *(integer) --* 
        
                  The pending or in-progress change of the number of nodes in the cluster.
        
                - **ClusterType** *(string) --* 
        
                  The pending or in-progress change of the cluster type.
        
                - **ClusterVersion** *(string) --* 
        
                  The pending or in-progress change of the service version.
        
                - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                  The pending or in-progress change of the automated snapshot retention period.
        
                - **ClusterIdentifier** *(string) --* 
        
                  The pending or in-progress change of the new identifier for the cluster.
        
                - **PubliclyAccessible** *(boolean) --* 
        
                  The pending or in-progress change of the ability to connect to the cluster from the public network.
        
                - **EnhancedVpcRouting** *(boolean) --* 
        
                  An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                  If this option is ``true`` , enhanced VPC routing is enabled. 
        
                  Default: false
        
                - **MaintenanceTrackName** *(string) --* 
        
                  The name of the maintenance track that the cluster will change to during the next maintenance window.
        
                - **EncryptionType** *(string) --* 
        
                  The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy. 
        
              - **ClusterVersion** *(string) --* 
        
                The version ID of the Amazon Redshift engine that is running on the cluster.
        
              - **AllowVersionUpgrade** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window. 
        
              - **NumberOfNodes** *(integer) --* 
        
                The number of compute nodes in the cluster.
        
              - **PubliclyAccessible** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that the cluster can be accessed from a public network.
        
              - **Encrypted** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that data in the cluster is encrypted at rest.
        
              - **RestoreStatus** *(dict) --* 
        
                A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.
        
                - **Status** *(string) --* 
        
                  The status of the restore action. Returns starting, restoring, completed, or failed.
        
                - **CurrentRestoreRateInMegaBytesPerSecond** *(float) --* 
        
                  The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.
        
                - **SnapshotSizeInMegaBytes** *(integer) --* 
        
                  The size of the set of snapshot data used to restore the cluster.
        
                - **ProgressInMegaBytes** *(integer) --* 
        
                  The number of megabytes that have been transferred from snapshot storage.
        
                - **ElapsedTimeInSeconds** *(integer) --* 
        
                  The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.
        
                - **EstimatedTimeToCompletionInSeconds** *(integer) --* 
        
                  The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore.
        
              - **HsmStatus** *(dict) --* 
        
                A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
        
                Values: active, applying
        
                - **HsmClientCertificateIdentifier** *(string) --* 
        
                  Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        
                - **HsmConfigurationIdentifier** *(string) --* 
        
                  Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        
                - **Status** *(string) --* 
        
                  Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
        
                  Values: active, applying
        
              - **ClusterSnapshotCopyStatus** *(dict) --* 
        
                A value that returns the destination region and retention period that are configured for cross-region snapshot copy.
        
                - **DestinationRegion** *(string) --* 
        
                  The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
        
                - **RetentionPeriod** *(integer) --* 
        
                  The number of days that automated snapshots are retained in the destination region after they are copied from a source region.
        
                - **SnapshotCopyGrantName** *(string) --* 
        
                  The name of the snapshot copy grant.
        
              - **ClusterPublicKey** *(string) --* 
        
                The public key for the cluster.
        
              - **ClusterNodes** *(list) --* 
        
                The nodes in the cluster.
        
                - *(dict) --* 
        
                  The identifier of a node in a cluster.
        
                  - **NodeRole** *(string) --* 
        
                    Whether the node is a leader node or a compute node.
        
                  - **PrivateIPAddress** *(string) --* 
        
                    The private IP address of a node within a cluster.
        
                  - **PublicIPAddress** *(string) --* 
        
                    The public IP address of a node within a cluster.
        
              - **ElasticIpStatus** *(dict) --* 
        
                The status of the elastic IP (EIP) address.
        
                - **ElasticIp** *(string) --* 
        
                  The elastic IP (EIP) address for the cluster.
        
                - **Status** *(string) --* 
        
                  The status of the elastic IP (EIP) address.
        
              - **ClusterRevisionNumber** *(string) --* 
        
                The specific revision number of the database in the cluster.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.
        
              - **EnhancedVpcRouting** *(boolean) --* 
        
                An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                If this option is ``true`` , enhanced VPC routing is enabled. 
        
                Default: false
        
              - **IamRoles** *(list) --* 
        
                A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.
        
                - *(dict) --* 
        
                  An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.
        
                  - **IamRoleArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the IAM role, for example, ``arn:aws:iam::123456789012:role/RedshiftCopyUnload`` . 
        
                  - **ApplyStatus** *(string) --* 
        
                    A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
        
                    The following are possible statuses and descriptions.
        
                    * ``in-sync`` : The role is available for use by the cluster. 
                     
                    * ``adding`` : The role is in the process of being associated with the cluster. 
                     
                    * ``removing`` : The role is in the process of being disassociated with the cluster. 
                     
              - **PendingActions** *(list) --* 
        
                Cluster operations that are waiting to be started.
        
                - *(string) --* 
            
              - **MaintenanceTrackName** *(string) --* 
        
                The name of the maintenance track for the cluster.
        
              - **ElasticResizeNumberOfNodeOptions** *(string) --* 
        
                Indicates the number of nodes the cluster can be resized to with the elastic resize method. 
        
        """
        pass

    def restore_table_from_cluster_snapshot(self, ClusterIdentifier: str, SnapshotIdentifier: str, SourceDatabaseName: str, SourceTableName: str, NewTableName: str, SourceSchemaName: str = None, TargetDatabaseName: str = None, TargetSchemaName: str = None) -> Dict:
        """
        
        You cannot use ``RestoreTableFromClusterSnapshot`` to restore a table with the same name as an existing table in an Amazon Redshift cluster. That is, you cannot overwrite an existing table in a cluster with a restored table. If you want to replace your original table with a new, restored table, then rename or drop your original table before you call ``RestoreTableFromClusterSnapshot`` . When you have renamed your original table, then you can pass the original name of the table as the ``NewTableName`` parameter value in the call to ``RestoreTableFromClusterSnapshot`` . This way, you can replace the original table with the table created from the snapshot.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/RestoreTableFromClusterSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.restore_table_from_cluster_snapshot(
              ClusterIdentifier=\'string\',
              SnapshotIdentifier=\'string\',
              SourceDatabaseName=\'string\',
              SourceSchemaName=\'string\',
              SourceTableName=\'string\',
              TargetDatabaseName=\'string\',
              TargetSchemaName=\'string\',
              NewTableName=\'string\'
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          The identifier of the Amazon Redshift cluster to restore the table to.
        
        :type SnapshotIdentifier: string
        :param SnapshotIdentifier: **[REQUIRED]** 
        
          The identifier of the snapshot to restore the table from. This snapshot must have been created from the Amazon Redshift cluster specified by the ``ClusterIdentifier`` parameter.
        
        :type SourceDatabaseName: string
        :param SourceDatabaseName: **[REQUIRED]** 
        
          The name of the source database that contains the table to restore from.
        
        :type SourceSchemaName: string
        :param SourceSchemaName: 
        
          The name of the source schema that contains the table to restore from. If you do not specify a ``SourceSchemaName`` value, the default is ``public`` .
        
        :type SourceTableName: string
        :param SourceTableName: **[REQUIRED]** 
        
          The name of the source table to restore from.
        
        :type TargetDatabaseName: string
        :param TargetDatabaseName: 
        
          The name of the database to restore the table to.
        
        :type TargetSchemaName: string
        :param TargetSchemaName: 
        
          The name of the schema to restore the table to.
        
        :type NewTableName: string
        :param NewTableName: **[REQUIRED]** 
        
          The name of the table to create as a result of the current request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TableRestoreStatus\': {
                    \'TableRestoreRequestId\': \'string\',
                    \'Status\': \'PENDING\'|\'IN_PROGRESS\'|\'SUCCEEDED\'|\'FAILED\'|\'CANCELED\',
                    \'Message\': \'string\',
                    \'RequestTime\': datetime(2015, 1, 1),
                    \'ProgressInMegaBytes\': 123,
                    \'TotalDataInMegaBytes\': 123,
                    \'ClusterIdentifier\': \'string\',
                    \'SnapshotIdentifier\': \'string\',
                    \'SourceDatabaseName\': \'string\',
                    \'SourceSchemaName\': \'string\',
                    \'SourceTableName\': \'string\',
                    \'TargetDatabaseName\': \'string\',
                    \'TargetSchemaName\': \'string\',
                    \'NewTableName\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TableRestoreStatus** *(dict) --* 
        
              Describes the status of a  RestoreTableFromClusterSnapshot operation.
        
              - **TableRestoreRequestId** *(string) --* 
        
                The unique identifier for the table restore request.
        
              - **Status** *(string) --* 
        
                A value that describes the current state of the table restore request.
        
                Valid Values: ``SUCCEEDED`` , ``FAILED`` , ``CANCELED`` , ``PENDING`` , ``IN_PROGRESS``  
        
              - **Message** *(string) --* 
        
                A description of the status of the table restore request. Status values include ``SUCCEEDED`` , ``FAILED`` , ``CANCELED`` , ``PENDING`` , ``IN_PROGRESS`` .
        
              - **RequestTime** *(datetime) --* 
        
                The time that the table restore request was made, in Universal Coordinated Time (UTC).
        
              - **ProgressInMegaBytes** *(integer) --* 
        
                The amount of data restored to the new table so far, in megabytes (MB).
        
              - **TotalDataInMegaBytes** *(integer) --* 
        
                The total amount of data to restore to the new table, in megabytes (MB).
        
              - **ClusterIdentifier** *(string) --* 
        
                The identifier of the Amazon Redshift cluster that the table is being restored to.
        
              - **SnapshotIdentifier** *(string) --* 
        
                The identifier of the snapshot that the table is being restored from.
        
              - **SourceDatabaseName** *(string) --* 
        
                The name of the source database that contains the table being restored.
        
              - **SourceSchemaName** *(string) --* 
        
                The name of the source schema that contains the table being restored.
        
              - **SourceTableName** *(string) --* 
        
                The name of the source table being restored.
        
              - **TargetDatabaseName** *(string) --* 
        
                The name of the database to restore the table to.
        
              - **TargetSchemaName** *(string) --* 
        
                The name of the schema to restore the table to.
        
              - **NewTableName** *(string) --* 
        
                The name of the table to create as a result of the table restore request.
        
        """
        pass

    def revoke_cluster_security_group_ingress(self, ClusterSecurityGroupName: str, CIDRIP: str = None, EC2SecurityGroupName: str = None, EC2SecurityGroupOwnerId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/RevokeClusterSecurityGroupIngress>`_
        
        **Request Syntax** 
        ::
        
          response = client.revoke_cluster_security_group_ingress(
              ClusterSecurityGroupName=\'string\',
              CIDRIP=\'string\',
              EC2SecurityGroupName=\'string\',
              EC2SecurityGroupOwnerId=\'string\'
          )
        :type ClusterSecurityGroupName: string
        :param ClusterSecurityGroupName: **[REQUIRED]** 
        
          The name of the security Group from which to revoke the ingress rule.
        
        :type CIDRIP: string
        :param CIDRIP: 
        
          The IP range for which to revoke access. This range must be a valid Classless Inter-Domain Routing (CIDR) block of IP addresses. If ``CIDRIP`` is specified, ``EC2SecurityGroupName`` and ``EC2SecurityGroupOwnerId`` cannot be provided. 
        
        :type EC2SecurityGroupName: string
        :param EC2SecurityGroupName: 
        
          The name of the EC2 Security Group whose access is to be revoked. If ``EC2SecurityGroupName`` is specified, ``EC2SecurityGroupOwnerId`` must also be provided and ``CIDRIP`` cannot be provided. 
        
        :type EC2SecurityGroupOwnerId: string
        :param EC2SecurityGroupOwnerId: 
        
          The AWS account number of the owner of the security group specified in the ``EC2SecurityGroupName`` parameter. The AWS access key ID is not an acceptable value. If ``EC2SecurityGroupOwnerId`` is specified, ``EC2SecurityGroupName`` must also be provided. and ``CIDRIP`` cannot be provided. 
        
          Example: ``111122223333``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ClusterSecurityGroup\': {
                    \'ClusterSecurityGroupName\': \'string\',
                    \'Description\': \'string\',
                    \'EC2SecurityGroups\': [
                        {
                            \'Status\': \'string\',
                            \'EC2SecurityGroupName\': \'string\',
                            \'EC2SecurityGroupOwnerId\': \'string\',
                            \'Tags\': [
                                {
                                    \'Key\': \'string\',
                                    \'Value\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'IPRanges\': [
                        {
                            \'Status\': \'string\',
                            \'CIDRIP\': \'string\',
                            \'Tags\': [
                                {
                                    \'Key\': \'string\',
                                    \'Value\': \'string\'
                                },
                            ]
                        },
                    ],
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
            
            - **ClusterSecurityGroup** *(dict) --* 
        
              Describes a security group.
        
              - **ClusterSecurityGroupName** *(string) --* 
        
                The name of the cluster security group to which the operation was applied.
        
              - **Description** *(string) --* 
        
                A description of the security group.
        
              - **EC2SecurityGroups** *(list) --* 
        
                A list of EC2 security groups that are permitted to access clusters associated with this cluster security group.
        
                - *(dict) --* 
        
                  Describes an Amazon EC2 security group.
        
                  - **Status** *(string) --* 
        
                    The status of the EC2 security group.
        
                  - **EC2SecurityGroupName** *(string) --* 
        
                    The name of the EC2 Security Group.
        
                  - **EC2SecurityGroupOwnerId** *(string) --* 
        
                    The AWS ID of the owner of the EC2 security group specified in the ``EC2SecurityGroupName`` field. 
        
                  - **Tags** *(list) --* 
        
                    The list of tags for the EC2 security group.
        
                    - *(dict) --* 
        
                      A tag consisting of a name/value pair for a resource.
        
                      - **Key** *(string) --* 
        
                        The key, or name, for the resource tag.
        
                      - **Value** *(string) --* 
        
                        The value for the resource tag.
        
              - **IPRanges** *(list) --* 
        
                A list of IP ranges (CIDR blocks) that are permitted to access clusters associated with this cluster security group.
        
                - *(dict) --* 
        
                  Describes an IP range used in a security group.
        
                  - **Status** *(string) --* 
        
                    The status of the IP range, for example, \"authorized\".
        
                  - **CIDRIP** *(string) --* 
        
                    The IP range in Classless Inter-Domain Routing (CIDR) notation.
        
                  - **Tags** *(list) --* 
        
                    The list of tags for the IP range.
        
                    - *(dict) --* 
        
                      A tag consisting of a name/value pair for a resource.
        
                      - **Key** *(string) --* 
        
                        The key, or name, for the resource tag.
        
                      - **Value** *(string) --* 
        
                        The value for the resource tag.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster security group.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
        """
        pass

    def revoke_snapshot_access(self, SnapshotIdentifier: str, AccountWithRestoreAccess: str, SnapshotClusterIdentifier: str = None) -> Dict:
        """
        
        For more information about working with snapshots, go to `Amazon Redshift Snapshots <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/RevokeSnapshotAccess>`_
        
        **Request Syntax** 
        ::
        
          response = client.revoke_snapshot_access(
              SnapshotIdentifier=\'string\',
              SnapshotClusterIdentifier=\'string\',
              AccountWithRestoreAccess=\'string\'
          )
        :type SnapshotIdentifier: string
        :param SnapshotIdentifier: **[REQUIRED]** 
        
          The identifier of the snapshot that the account can no longer access.
        
        :type SnapshotClusterIdentifier: string
        :param SnapshotClusterIdentifier: 
        
          The identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
        
        :type AccountWithRestoreAccess: string
        :param AccountWithRestoreAccess: **[REQUIRED]** 
        
          The identifier of the AWS customer account that can no longer restore the specified snapshot.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Snapshot\': {
                    \'SnapshotIdentifier\': \'string\',
                    \'ClusterIdentifier\': \'string\',
                    \'SnapshotCreateTime\': datetime(2015, 1, 1),
                    \'Status\': \'string\',
                    \'Port\': 123,
                    \'AvailabilityZone\': \'string\',
                    \'ClusterCreateTime\': datetime(2015, 1, 1),
                    \'MasterUsername\': \'string\',
                    \'ClusterVersion\': \'string\',
                    \'SnapshotType\': \'string\',
                    \'NodeType\': \'string\',
                    \'NumberOfNodes\': 123,
                    \'DBName\': \'string\',
                    \'VpcId\': \'string\',
                    \'Encrypted\': True|False,
                    \'KmsKeyId\': \'string\',
                    \'EncryptedWithHSM\': True|False,
                    \'AccountsWithRestoreAccess\': [
                        {
                            \'AccountId\': \'string\',
                            \'AccountAlias\': \'string\'
                        },
                    ],
                    \'OwnerAccount\': \'string\',
                    \'TotalBackupSizeInMegaBytes\': 123.0,
                    \'ActualIncrementalBackupSizeInMegaBytes\': 123.0,
                    \'BackupProgressInMegaBytes\': 123.0,
                    \'CurrentBackupRateInMegaBytesPerSecond\': 123.0,
                    \'EstimatedSecondsToCompletion\': 123,
                    \'ElapsedTimeInSeconds\': 123,
                    \'SourceRegion\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'RestorableNodeTypes\': [
                        \'string\',
                    ],
                    \'EnhancedVpcRouting\': True|False,
                    \'MaintenanceTrackName\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Snapshot** *(dict) --* 
        
              Describes a snapshot.
        
              - **SnapshotIdentifier** *(string) --* 
        
                The snapshot identifier that is provided in the request.
        
              - **ClusterIdentifier** *(string) --* 
        
                The identifier of the cluster for which the snapshot was taken.
        
              - **SnapshotCreateTime** *(datetime) --* 
        
                The time (UTC) when Amazon Redshift began the snapshot. A snapshot contains a copy of the cluster data as of this exact time.
        
              - **Status** *(string) --* 
        
                The snapshot status. The value of the status depends on the API operation used. 
        
                *  CreateClusterSnapshot and  CopyClusterSnapshot returns status as \"creating\".  
                 
                *  DescribeClusterSnapshots returns status as \"creating\", \"available\", \"final snapshot\", or \"failed\". 
                 
                *  DeleteClusterSnapshot returns status as \"deleted\". 
                 
              - **Port** *(integer) --* 
        
                The port that the cluster is listening on.
        
              - **AvailabilityZone** *(string) --* 
        
                The Availability Zone in which the cluster was created.
        
              - **ClusterCreateTime** *(datetime) --* 
        
                The time (UTC) when the cluster was originally created.
        
              - **MasterUsername** *(string) --* 
        
                The master user name for the cluster.
        
              - **ClusterVersion** *(string) --* 
        
                The version ID of the Amazon Redshift engine that is running on the cluster.
        
              - **SnapshotType** *(string) --* 
        
                The snapshot type. Snapshots created using  CreateClusterSnapshot and  CopyClusterSnapshot will be of type \"manual\". 
        
              - **NodeType** *(string) --* 
        
                The node type of the nodes in the cluster.
        
              - **NumberOfNodes** *(integer) --* 
        
                The number of nodes in the cluster.
        
              - **DBName** *(string) --* 
        
                The name of the database that was created when the cluster was created.
        
              - **VpcId** *(string) --* 
        
                The VPC identifier of the cluster if the snapshot is from a cluster in a VPC. Otherwise, this field is not in the output.
        
              - **Encrypted** *(boolean) --* 
        
                If ``true`` , the data in the snapshot is encrypted at rest.
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.
        
              - **EncryptedWithHSM** *(boolean) --* 
        
                A boolean that indicates whether the snapshot data is encrypted using the HSM keys of the source cluster. ``true`` indicates that the data is encrypted using HSM keys.
        
              - **AccountsWithRestoreAccess** *(list) --* 
        
                A list of the AWS customer accounts authorized to restore the snapshot. Returns ``null`` if no accounts are authorized. Visible only to the snapshot owner. 
        
                - *(dict) --* 
        
                  Describes an AWS customer account authorized to restore a snapshot.
        
                  - **AccountId** *(string) --* 
        
                    The identifier of an AWS customer account authorized to restore a snapshot.
        
                  - **AccountAlias** *(string) --* 
        
                    The identifier of an AWS support account authorized to restore a snapshot. For AWS support, the identifier is ``amazon-redshift-support`` . 
        
              - **OwnerAccount** *(string) --* 
        
                For manual snapshots, the AWS customer account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.
        
              - **TotalBackupSizeInMegaBytes** *(float) --* 
        
                The size of the complete set of backup data that would be used to restore the cluster.
        
              - **ActualIncrementalBackupSizeInMegaBytes** *(float) --* 
        
                The size of the incremental backup.
        
              - **BackupProgressInMegaBytes** *(float) --* 
        
                The number of megabytes that have been transferred to the snapshot backup.
        
              - **CurrentBackupRateInMegaBytesPerSecond** *(float) --* 
        
                The number of megabytes per second being transferred to the snapshot backup. Returns ``0`` for a completed backup. 
        
              - **EstimatedSecondsToCompletion** *(integer) --* 
        
                The estimate of the time remaining before the snapshot backup will complete. Returns ``0`` for a completed backup. 
        
              - **ElapsedTimeInSeconds** *(integer) --* 
        
                The amount of time an in-progress snapshot backup has been running, or the amount of time it took a completed backup to finish.
        
              - **SourceRegion** *(string) --* 
        
                The source region from which the snapshot was copied.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster snapshot.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
              - **RestorableNodeTypes** *(list) --* 
        
                The list of node types that this cluster snapshot is able to restore into.
        
                - *(string) --* 
            
              - **EnhancedVpcRouting** *(boolean) --* 
        
                An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                If this option is ``true`` , enhanced VPC routing is enabled. 
        
                Default: false
        
              - **MaintenanceTrackName** *(string) --* 
        
                The name of the maintenance track for the snapshot.
        
        """
        pass

    def rotate_encryption_key(self, ClusterIdentifier: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/RotateEncryptionKey>`_
        
        **Request Syntax** 
        ::
        
          response = client.rotate_encryption_key(
              ClusterIdentifier=\'string\'
          )
        :type ClusterIdentifier: string
        :param ClusterIdentifier: **[REQUIRED]** 
        
          The unique identifier of the cluster that you want to rotate the encryption keys for.
        
          Constraints: Must be the name of valid cluster that has encryption enabled.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
                    \'ClusterIdentifier\': \'string\',
                    \'NodeType\': \'string\',
                    \'ClusterStatus\': \'string\',
                    \'ModifyStatus\': \'string\',
                    \'MasterUsername\': \'string\',
                    \'DBName\': \'string\',
                    \'Endpoint\': {
                        \'Address\': \'string\',
                        \'Port\': 123
                    },
                    \'ClusterCreateTime\': datetime(2015, 1, 1),
                    \'AutomatedSnapshotRetentionPeriod\': 123,
                    \'ClusterSecurityGroups\': [
                        {
                            \'ClusterSecurityGroupName\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'VpcSecurityGroups\': [
                        {
                            \'VpcSecurityGroupId\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'ClusterParameterGroups\': [
                        {
                            \'ParameterGroupName\': \'string\',
                            \'ParameterApplyStatus\': \'string\',
                            \'ClusterParameterStatusList\': [
                                {
                                    \'ParameterName\': \'string\',
                                    \'ParameterApplyStatus\': \'string\',
                                    \'ParameterApplyErrorDescription\': \'string\'
                                },
                            ]
                        },
                    ],
                    \'ClusterSubnetGroupName\': \'string\',
                    \'VpcId\': \'string\',
                    \'AvailabilityZone\': \'string\',
                    \'PreferredMaintenanceWindow\': \'string\',
                    \'PendingModifiedValues\': {
                        \'MasterUserPassword\': \'string\',
                        \'NodeType\': \'string\',
                        \'NumberOfNodes\': 123,
                        \'ClusterType\': \'string\',
                        \'ClusterVersion\': \'string\',
                        \'AutomatedSnapshotRetentionPeriod\': 123,
                        \'ClusterIdentifier\': \'string\',
                        \'PubliclyAccessible\': True|False,
                        \'EnhancedVpcRouting\': True|False,
                        \'MaintenanceTrackName\': \'string\',
                        \'EncryptionType\': \'string\'
                    },
                    \'ClusterVersion\': \'string\',
                    \'AllowVersionUpgrade\': True|False,
                    \'NumberOfNodes\': 123,
                    \'PubliclyAccessible\': True|False,
                    \'Encrypted\': True|False,
                    \'RestoreStatus\': {
                        \'Status\': \'string\',
                        \'CurrentRestoreRateInMegaBytesPerSecond\': 123.0,
                        \'SnapshotSizeInMegaBytes\': 123,
                        \'ProgressInMegaBytes\': 123,
                        \'ElapsedTimeInSeconds\': 123,
                        \'EstimatedTimeToCompletionInSeconds\': 123
                    },
                    \'HsmStatus\': {
                        \'HsmClientCertificateIdentifier\': \'string\',
                        \'HsmConfigurationIdentifier\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterSnapshotCopyStatus\': {
                        \'DestinationRegion\': \'string\',
                        \'RetentionPeriod\': 123,
                        \'SnapshotCopyGrantName\': \'string\'
                    },
                    \'ClusterPublicKey\': \'string\',
                    \'ClusterNodes\': [
                        {
                            \'NodeRole\': \'string\',
                            \'PrivateIPAddress\': \'string\',
                            \'PublicIPAddress\': \'string\'
                        },
                    ],
                    \'ElasticIpStatus\': {
                        \'ElasticIp\': \'string\',
                        \'Status\': \'string\'
                    },
                    \'ClusterRevisionNumber\': \'string\',
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'KmsKeyId\': \'string\',
                    \'EnhancedVpcRouting\': True|False,
                    \'IamRoles\': [
                        {
                            \'IamRoleArn\': \'string\',
                            \'ApplyStatus\': \'string\'
                        },
                    ],
                    \'PendingActions\': [
                        \'string\',
                    ],
                    \'MaintenanceTrackName\': \'string\',
                    \'ElasticResizeNumberOfNodeOptions\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              Describes a cluster.
        
              - **ClusterIdentifier** *(string) --* 
        
                The unique identifier of the cluster.
        
              - **NodeType** *(string) --* 
        
                The node type for the nodes in the cluster.
        
              - **ClusterStatus** *(string) --* 
        
                The current state of the cluster. Possible values are the following:
        
                * ``available``   
                 
                * ``creating``   
                 
                * ``deleting``   
                 
                * ``final-snapshot``   
                 
                * ``hardware-failure``   
                 
                * ``incompatible-hsm``   
                 
                * ``incompatible-network``   
                 
                * ``incompatible-parameters``   
                 
                * ``incompatible-restore``   
                 
                * ``modifying``   
                 
                * ``rebooting``   
                 
                * ``renaming``   
                 
                * ``resizing``   
                 
                * ``rotating-keys``   
                 
                * ``storage-full``   
                 
                * ``updating-hsm``   
                 
              - **ModifyStatus** *(string) --* 
        
                The status of a modify operation, if any, initiated for the cluster.
        
              - **MasterUsername** *(string) --* 
        
                The master user name for the cluster. This name is used to connect to the database that is specified in the **DBName** parameter. 
        
              - **DBName** *(string) --* 
        
                The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named ``dev`` dev was created by default. 
        
              - **Endpoint** *(dict) --* 
        
                The connection endpoint.
        
                - **Address** *(string) --* 
        
                  The DNS address of the Cluster.
        
                - **Port** *(integer) --* 
        
                  The port that the database engine is listening on.
        
              - **ClusterCreateTime** *(datetime) --* 
        
                The date and time that the cluster was created.
        
              - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                The number of days that automatic cluster snapshots are retained.
        
              - **ClusterSecurityGroups** *(list) --* 
        
                A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ``ClusterSecurityGroup.Name`` and ``ClusterSecurityGroup.Status`` subelements. 
        
                Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the **VpcSecurityGroups** parameter. 
        
                - *(dict) --* 
        
                  Describes a cluster security group.
        
                  - **ClusterSecurityGroupName** *(string) --* 
        
                    The name of the cluster security group.
        
                  - **Status** *(string) --* 
        
                    The status of the cluster security group.
        
              - **VpcSecurityGroups** *(list) --* 
        
                A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.
        
                - *(dict) --* 
        
                  Describes the members of a VPC security group.
        
                  - **VpcSecurityGroupId** *(string) --* 
        
                    The identifier of the VPC security group.
        
                  - **Status** *(string) --* 
        
                    The status of the VPC security group.
        
              - **ClusterParameterGroups** *(list) --* 
        
                The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.
        
                - *(dict) --* 
        
                  Describes the status of a parameter group.
        
                  - **ParameterGroupName** *(string) --* 
        
                    The name of the cluster parameter group.
        
                  - **ParameterApplyStatus** *(string) --* 
        
                    The status of parameter updates.
        
                  - **ClusterParameterStatusList** *(list) --* 
        
                    The list of parameter statuses.
        
                    For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
        
                    - *(dict) --* 
        
                      Describes the status of a parameter group.
        
                      - **ParameterName** *(string) --* 
        
                        The name of the parameter.
        
                      - **ParameterApplyStatus** *(string) --* 
        
                        The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
        
                        The following are possible statuses and descriptions.
        
                        * ``in-sync`` : The parameter value is in sync with the database. 
                         
                        * ``pending-reboot`` : The parameter value will be applied after the cluster reboots. 
                         
                        * ``applying`` : The parameter value is being applied to the database. 
                         
                        * ``invalid-parameter`` : Cannot apply the parameter value because it has an invalid value or syntax. 
                         
                        * ``apply-deferred`` : The parameter contains static property changes. The changes are deferred until the cluster reboots. 
                         
                        * ``apply-error`` : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots. 
                         
                        * ``unknown-error`` : Cannot apply the parameter change right now. The change will be applied after the cluster reboots. 
                         
                      - **ParameterApplyErrorDescription** *(string) --* 
        
                        The error that prevented the parameter from being applied to the database.
        
              - **ClusterSubnetGroupName** *(string) --* 
        
                The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.
        
              - **VpcId** *(string) --* 
        
                The identifier of the VPC the cluster is in, if the cluster is in a VPC.
        
              - **AvailabilityZone** *(string) --* 
        
                The name of the Availability Zone in which the cluster is located.
        
              - **PreferredMaintenanceWindow** *(string) --* 
        
                The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.
        
              - **PendingModifiedValues** *(dict) --* 
        
                A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.
        
                - **MasterUserPassword** *(string) --* 
        
                  The pending or in-progress change of the master user password for the cluster.
        
                - **NodeType** *(string) --* 
        
                  The pending or in-progress change of the cluster\'s node type.
        
                - **NumberOfNodes** *(integer) --* 
        
                  The pending or in-progress change of the number of nodes in the cluster.
        
                - **ClusterType** *(string) --* 
        
                  The pending or in-progress change of the cluster type.
        
                - **ClusterVersion** *(string) --* 
        
                  The pending or in-progress change of the service version.
        
                - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
        
                  The pending or in-progress change of the automated snapshot retention period.
        
                - **ClusterIdentifier** *(string) --* 
        
                  The pending or in-progress change of the new identifier for the cluster.
        
                - **PubliclyAccessible** *(boolean) --* 
        
                  The pending or in-progress change of the ability to connect to the cluster from the public network.
        
                - **EnhancedVpcRouting** *(boolean) --* 
        
                  An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                  If this option is ``true`` , enhanced VPC routing is enabled. 
        
                  Default: false
        
                - **MaintenanceTrackName** *(string) --* 
        
                  The name of the maintenance track that the cluster will change to during the next maintenance window.
        
                - **EncryptionType** *(string) --* 
        
                  The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy. 
        
              - **ClusterVersion** *(string) --* 
        
                The version ID of the Amazon Redshift engine that is running on the cluster.
        
              - **AllowVersionUpgrade** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window. 
        
              - **NumberOfNodes** *(integer) --* 
        
                The number of compute nodes in the cluster.
        
              - **PubliclyAccessible** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that the cluster can be accessed from a public network.
        
              - **Encrypted** *(boolean) --* 
        
                A Boolean value that, if ``true`` , indicates that data in the cluster is encrypted at rest.
        
              - **RestoreStatus** *(dict) --* 
        
                A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.
        
                - **Status** *(string) --* 
        
                  The status of the restore action. Returns starting, restoring, completed, or failed.
        
                - **CurrentRestoreRateInMegaBytesPerSecond** *(float) --* 
        
                  The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.
        
                - **SnapshotSizeInMegaBytes** *(integer) --* 
        
                  The size of the set of snapshot data used to restore the cluster.
        
                - **ProgressInMegaBytes** *(integer) --* 
        
                  The number of megabytes that have been transferred from snapshot storage.
        
                - **ElapsedTimeInSeconds** *(integer) --* 
        
                  The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.
        
                - **EstimatedTimeToCompletionInSeconds** *(integer) --* 
        
                  The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore.
        
              - **HsmStatus** *(dict) --* 
        
                A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
        
                Values: active, applying
        
                - **HsmClientCertificateIdentifier** *(string) --* 
        
                  Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        
                - **HsmConfigurationIdentifier** *(string) --* 
        
                  Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        
                - **Status** *(string) --* 
        
                  Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
        
                  Values: active, applying
        
              - **ClusterSnapshotCopyStatus** *(dict) --* 
        
                A value that returns the destination region and retention period that are configured for cross-region snapshot copy.
        
                - **DestinationRegion** *(string) --* 
        
                  The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
        
                - **RetentionPeriod** *(integer) --* 
        
                  The number of days that automated snapshots are retained in the destination region after they are copied from a source region.
        
                - **SnapshotCopyGrantName** *(string) --* 
        
                  The name of the snapshot copy grant.
        
              - **ClusterPublicKey** *(string) --* 
        
                The public key for the cluster.
        
              - **ClusterNodes** *(list) --* 
        
                The nodes in the cluster.
        
                - *(dict) --* 
        
                  The identifier of a node in a cluster.
        
                  - **NodeRole** *(string) --* 
        
                    Whether the node is a leader node or a compute node.
        
                  - **PrivateIPAddress** *(string) --* 
        
                    The private IP address of a node within a cluster.
        
                  - **PublicIPAddress** *(string) --* 
        
                    The public IP address of a node within a cluster.
        
              - **ElasticIpStatus** *(dict) --* 
        
                The status of the elastic IP (EIP) address.
        
                - **ElasticIp** *(string) --* 
        
                  The elastic IP (EIP) address for the cluster.
        
                - **Status** *(string) --* 
        
                  The status of the elastic IP (EIP) address.
        
              - **ClusterRevisionNumber** *(string) --* 
        
                The specific revision number of the database in the cluster.
        
              - **Tags** *(list) --* 
        
                The list of tags for the cluster.
        
                - *(dict) --* 
        
                  A tag consisting of a name/value pair for a resource.
        
                  - **Key** *(string) --* 
        
                    The key, or name, for the resource tag.
        
                  - **Value** *(string) --* 
        
                    The value for the resource tag.
        
              - **KmsKeyId** *(string) --* 
        
                The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.
        
              - **EnhancedVpcRouting** *(boolean) --* 
        
                An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <http://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
        
                If this option is ``true`` , enhanced VPC routing is enabled. 
        
                Default: false
        
              - **IamRoles** *(list) --* 
        
                A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.
        
                - *(dict) --* 
        
                  An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.
        
                  - **IamRoleArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the IAM role, for example, ``arn:aws:iam::123456789012:role/RedshiftCopyUnload`` . 
        
                  - **ApplyStatus** *(string) --* 
        
                    A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
        
                    The following are possible statuses and descriptions.
        
                    * ``in-sync`` : The role is available for use by the cluster. 
                     
                    * ``adding`` : The role is in the process of being associated with the cluster. 
                     
                    * ``removing`` : The role is in the process of being disassociated with the cluster. 
                     
              - **PendingActions** *(list) --* 
        
                Cluster operations that are waiting to be started.
        
                - *(string) --* 
            
              - **MaintenanceTrackName** *(string) --* 
        
                The name of the maintenance track for the cluster.
        
              - **ElasticResizeNumberOfNodeOptions** *(string) --* 
        
                Indicates the number of nodes the cluster can be resized to with the elastic resize method. 
        
        """
        pass
