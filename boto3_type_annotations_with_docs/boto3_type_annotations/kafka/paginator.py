from typing import Dict
from botocore.paginate import Paginator


class ListClusters(Paginator):
    def paginate(self, ClusterNameFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Kafka.Client.list_clusters`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/ListClusters>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ClusterNameFilter='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ClusterInfoList': [
                    {
                        'BrokerNodeGroupInfo': {
                            'BrokerAZDistribution': 'DEFAULT',
                            'ClientSubnets': [
                                'string',
                            ],
                            'InstanceType': 'string',
                            'SecurityGroups': [
                                'string',
                            ],
                            'StorageInfo': {
                                'EbsStorageInfo': {
                                    'VolumeSize': 123
                                }
                            }
                        },
                        'ClusterArn': 'string',
                        'ClusterName': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'CurrentBrokerSoftwareInfo': {
                            'ConfigurationArn': 'string',
                            'ConfigurationRevision': 'string',
                            'KafkaVersion': 'string'
                        },
                        'CurrentVersion': 'string',
                        'EncryptionInfo': {
                            'EncryptionAtRest': {
                                'DataVolumeKMSKeyId': 'string'
                            }
                        },
                        'EnhancedMonitoring': 'DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
                        'NumberOfBrokerNodes': 123,
                        'State': 'ACTIVE'|'CREATING'|'DELETING'|'FAILED',
                        'ZookeeperConnectString': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Successful response.
            - **ClusterInfoList** *(list) --* 
              Information on each of the MSK clusters in the response.
              - *(dict) --* 
                Returns information about a cluster.
                - **BrokerNodeGroupInfo** *(dict) --* 
                  Information about the broker nodes.
                  - **BrokerAZDistribution** *(string) --* 
                    The distribution of broker nodes across Availability Zones.
                  - **ClientSubnets** *(list) --* 
                    The list of subnets to connect to in the client virtual private cloud (VPC). AWS creates elastic network interfaces inside these subnets. Client applications use elastic network interfaces to produce and consume data. Client subnets can't be in Availability Zone us-east-1e.
                    - *(string) --* 
                  - **InstanceType** *(string) --* 
                    The type of Amazon EC2 instances to use for Kafka brokers. The following instance types are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge, kafka.m5.12xlarge, and kafka.m5.24xlarge.
                  - **SecurityGroups** *(list) --* 
                    The AWS security groups to associate with the elastic network interfaces in order to specify who can connect to and communicate with the Amazon MSK cluster.
                    - *(string) --* 
                  - **StorageInfo** *(dict) --* 
                    Contains information about storage volumes attached to MSK broker nodes.
                    - **EbsStorageInfo** *(dict) --* 
                      EBS volume information.
                      - **VolumeSize** *(integer) --* 
                        The size in GiB of the EBS volume for the data drive on each broker node.
                - **ClusterArn** *(string) --* 
                  The Amazon Resource Name (ARN) that uniquely identifies the cluster.
                - **ClusterName** *(string) --* 
                  The name of the cluster.
                - **CreationTime** *(datetime) --* 
                  The time when the cluster was created.
                - **CurrentBrokerSoftwareInfo** *(dict) --* 
                  Information about the version of software currently deployed on the Kafka brokers in the cluster.
                  - **ConfigurationArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the configuration used for the cluster.
                  - **ConfigurationRevision** *(string) --* 
                    The revision of the configuration to use.
                  - **KafkaVersion** *(string) --* 
                    The version of Apache Kafka.
                - **CurrentVersion** *(string) --* 
                  The current version of the MSK cluster.
                - **EncryptionInfo** *(dict) --* 
                  Includes all encryption-related information.
                  - **EncryptionAtRest** *(dict) --* 
                    The data volume encryption details.
                    - **DataVolumeKMSKeyId** *(string) --* 
                      The AWS KMS key used for data encryption.
                - **EnhancedMonitoring** *(string) --* 
                  Specifies which metrics are gathered for the MSK cluster. This property has three possible values: DEFAULT, PER_BROKER, and PER_TOPIC_PER_BROKER.
                - **NumberOfBrokerNodes** *(integer) --* 
                  The number of Kafka broker nodes in the cluster.
                - **State** *(string) --* 
                  The state of the cluster. The possible states are CREATING, ACTIVE, and FAILED.
                - **ZookeeperConnectString** *(string) --* 
                  The connection string to use to connect to the Apache ZooKeeper cluster.
        :type ClusterNameFilter: string
        :param ClusterNameFilter:
          Specify a prefix of the name of the clusters that you want to list. The service lists all the clusters whose names start with this prefix.
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


class ListNodes(Paginator):
    def paginate(self, ClusterArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Kafka.Client.list_nodes`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/ListNodes>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ClusterArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'NodeInfoList': [
                    {
                        'AddedToClusterTime': 'string',
                        'BrokerNodeInfo': {
                            'AttachedENIId': 'string',
                            'BrokerId': 123.0,
                            'ClientSubnet': 'string',
                            'ClientVpcIpAddress': 'string',
                            'CurrentBrokerSoftwareInfo': {
                                'ConfigurationArn': 'string',
                                'ConfigurationRevision': 'string',
                                'KafkaVersion': 'string'
                            }
                        },
                        'InstanceType': 'string',
                        'NodeARN': 'string',
                        'NodeType': 'BROKER',
                        'ZookeeperNodeInfo': {
                            'AttachedENIId': 'string',
                            'ClientVpcIpAddress': 'string',
                            'ZookeeperId': 123.0,
                            'ZookeeperVersion': 'string'
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Successful response.
            - **NodeInfoList** *(list) --* 
              List containing a NodeInfo object.
              - *(dict) --* 
                The node information object.
                - **AddedToClusterTime** *(string) --* 
                  The start time.
                - **BrokerNodeInfo** *(dict) --* 
                  The broker node info.
                  - **AttachedENIId** *(string) --* 
                    The attached elastic network interface of the broker.
                  - **BrokerId** *(float) --* 
                    The ID of the broker.
                  - **ClientSubnet** *(string) --* 
                    The client subnet to which this broker node belongs.
                  - **ClientVpcIpAddress** *(string) --* 
                    The virtual private cloud (VPC) of the client.
                  - **CurrentBrokerSoftwareInfo** *(dict) --* 
                    Information about the version of software currently deployed on the Kafka brokers in the cluster.
                    - **ConfigurationArn** *(string) --* 
                      The Amazon Resource Name (ARN) of the configuration used for the cluster.
                    - **ConfigurationRevision** *(string) --* 
                      The revision of the configuration to use.
                    - **KafkaVersion** *(string) --* 
                      The version of Apache Kafka.
                - **InstanceType** *(string) --* 
                  The instance type.
                - **NodeARN** *(string) --* 
                  The Amazon Resource Name (ARN) of the node.
                - **NodeType** *(string) --* 
                  The node type.
                - **ZookeeperNodeInfo** *(dict) --* 
                  The ZookeeperNodeInfo.
                  - **AttachedENIId** *(string) --* 
                    The attached elastic network interface of the broker.
                  - **ClientVpcIpAddress** *(string) --* 
                    The virtual private cloud (VPC) IP address of the client.
                  - **ZookeeperId** *(float) --* 
                    The role-specific ID for Zookeeper.
                  - **ZookeeperVersion** *(string) --* 
                    The version of Zookeeper.
        :type ClusterArn: string
        :param ClusterArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) that uniquely identifies the cluster.
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
