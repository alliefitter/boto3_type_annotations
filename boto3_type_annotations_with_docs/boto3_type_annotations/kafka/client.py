from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Union
from typing import List


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

    def create_cluster(self, BrokerNodeGroupInfo: Dict, ClusterName: str, KafkaVersion: str, NumberOfBrokerNodes: int, EncryptionInfo: Dict = None, EnhancedMonitoring: str = None) -> Dict:
        """
        Creates a new MSK cluster.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/CreateCluster>`_
        
        **Request Syntax**
        ::
          response = client.create_cluster(
              BrokerNodeGroupInfo={
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
              ClusterName='string',
              EncryptionInfo={
                  'EncryptionAtRest': {
                      'DataVolumeKMSKeyId': 'string'
                  }
              },
              EnhancedMonitoring='DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
              KafkaVersion='string',
              NumberOfBrokerNodes=123
          )
        
        **Response Syntax**
        ::
            {
                'ClusterArn': 'string',
                'ClusterName': 'string',
                'State': 'ACTIVE'|'CREATING'|'DELETING'|'FAILED'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ClusterArn** *(string) --* 
              The Amazon Resource Name (ARN) of the cluster.
            - **ClusterName** *(string) --* 
              The name of the MSK cluster.
            - **State** *(string) --* 
              The state of the cluster. The possible states are CREATING, ACTIVE, and FAILED.
        :type BrokerNodeGroupInfo: dict
        :param BrokerNodeGroupInfo: **[REQUIRED]**
          Information about the broker nodes in the cluster.
          - **BrokerAZDistribution** *(string) --*
            The distribution of broker nodes across Availability Zones.
          - **ClientSubnets** *(list) --* **[REQUIRED]**
            The list of subnets to connect to in the client virtual private cloud (VPC). AWS creates elastic network interfaces inside these subnets. Client applications use elastic network interfaces to produce and consume data. Client subnets can\'t be in Availability Zone us-east-1e.
            - *(string) --*
          - **InstanceType** *(string) --* **[REQUIRED]**
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
        :type ClusterName: string
        :param ClusterName: **[REQUIRED]**
          The name of the cluster.
        :type EncryptionInfo: dict
        :param EncryptionInfo:
          Includes all encryption-related information.
          - **EncryptionAtRest** *(dict) --*
            The data volume encryption details.
            - **DataVolumeKMSKeyId** *(string) --* **[REQUIRED]**
              The AWS KMS key used for data encryption.
        :type EnhancedMonitoring: string
        :param EnhancedMonitoring:
          Specifies the level of monitoring for the MSK cluster. The possible values are DEFAULT, PER_BROKER, and PER_TOPIC_PER_BROKER.
        :type KafkaVersion: string
        :param KafkaVersion: **[REQUIRED]**
          The version of Apache Kafka.
        :type NumberOfBrokerNodes: integer
        :param NumberOfBrokerNodes: **[REQUIRED]**
          The number of Kafka broker nodes in the Amazon MSK cluster.
        :rtype: dict
        :returns:
        """
        pass

    def delete_cluster(self, ClusterArn: str, CurrentVersion: str = None) -> Dict:
        """
        Deletes the MSK cluster specified by the Amazon Resource Name (ARN) in the request.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/DeleteCluster>`_
        
        **Request Syntax**
        ::
          response = client.delete_cluster(
              ClusterArn='string',
              CurrentVersion='string'
          )
        
        **Response Syntax**
        ::
            {
                'ClusterArn': 'string',
                'State': 'ACTIVE'|'CREATING'|'DELETING'|'FAILED'
            }
        
        **Response Structure**
          - *(dict) --* 
            Successful response.
            - **ClusterArn** *(string) --* 
              The Amazon Resource Name (ARN) of the cluster.
            - **State** *(string) --* 
              The state of the cluster. The possible states are CREATING, ACTIVE, and FAILED.
        :type ClusterArn: string
        :param ClusterArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) that uniquely identifies the cluster.
        :type CurrentVersion: string
        :param CurrentVersion:
          The current version of the MSK cluster.
        :rtype: dict
        :returns:
        """
        pass

    def describe_cluster(self, ClusterArn: str) -> Dict:
        """
        Returns a description of the MSK cluster whose Amazon Resource Name (ARN) is specified in the request.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/DescribeCluster>`_
        
        **Request Syntax**
        ::
          response = client.describe_cluster(
              ClusterArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'ClusterInfo': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Successful response.
            - **ClusterInfo** *(dict) --* 
              The cluster information.
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
        :type ClusterArn: string
        :param ClusterArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) that uniquely identifies the cluster.
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

    def get_bootstrap_brokers(self, ClusterArn: str) -> Dict:
        """
        A list of brokers that a client application can use to bootstrap.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/GetBootstrapBrokers>`_
        
        **Request Syntax**
        ::
          response = client.get_bootstrap_brokers(
              ClusterArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'BootstrapBrokerString': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Successful response.
            - **BootstrapBrokerString** *(string) --* 
              A string containing one or more hostname:port pairs.
        :type ClusterArn: string
        :param ClusterArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) that uniquely identifies the cluster.
        :rtype: dict
        :returns:
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

    def list_clusters(self, ClusterNameFilter: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Returns a list of clusters in an account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/ListClusters>`_
        
        **Request Syntax**
        ::
          response = client.list_clusters(
              ClusterNameFilter='string',
              MaxResults=123,
              NextToken='string'
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              The paginated results marker. When the result of a ListClusters operation is truncated, the call returns NextToken in the response. To get another batch of clusters, provide this token in your next request.
        :type ClusterNameFilter: string
        :param ClusterNameFilter:
          Specify a prefix of the name of the clusters that you want to list. The service lists all the clusters whose names start with this prefix.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of clusters to return in the response. If there are more clusters, the response includes a NextToken parameter.
        :type NextToken: string
        :param NextToken:
          The paginated results marker. When the result of a ListClusters operation is truncated, the call returns NextToken in the response. To get another batch of clusters, provide this token in your next request.
        :rtype: dict
        :returns:
        """
        pass

    def list_nodes(self, ClusterArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Returns a list of the broker nodes in the cluster.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/ListNodes>`_
        
        **Request Syntax**
        ::
          response = client.list_nodes(
              ClusterArn='string',
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'NextToken': 'string',
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
            - **NextToken** *(string) --* 
              The paginated results marker. When the result of a ListNodes operation is truncated, the call returns NextToken in the response. To get another batch of nodes, provide this token in your next request.
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
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of clusters to return in the response. If there are more clusters, the response includes a NextToken parameter.
        :type NextToken: string
        :param NextToken:
          The paginated results marker. When the result of a ListClusters operation is truncated, the call returns NextToken in the response. To get another batch of clusters, provide this token in your next request.
        :rtype: dict
        :returns:
        """
        pass

    def list_tags_for_resource(self, ResourceArn: str) -> Dict:
        """
        Returns a list of tags attached to a resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/ListTagsForResource>`_
        
        **Request Syntax**
        ::
          response = client.list_tags_for_resource(
              ResourceArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'Tags': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Successful response.
            - **Tags** *(dict) --* 
              The key-value pairs for the resource tags
              - *(string) --* 
                - *(string) --* 
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) that uniquely identifies the resource.
        :rtype: dict
        :returns:
        """
        pass

    def tag_resource(self, ResourceArn: str, Tags: Dict):
        """
        Tag a resource with given tags.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/TagResource>`_
        
        **Request Syntax**
        ::
          response = client.tag_resource(
              ResourceArn='string',
              Tags={
                  'string': 'string'
              }
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) that uniquely identifies the resource.
        :type Tags: dict
        :param Tags: **[REQUIRED]**
          The key-value pairs for the resource tags
          - *(string) --*
            - *(string) --*
        :returns: None
        """
        pass

    def untag_resource(self, ResourceArn: str, TagKeys: List):
        """
        Remove tags of a resource by given tag keys.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/UntagResource>`_
        
        **Request Syntax**
        ::
          response = client.untag_resource(
              ResourceArn='string',
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) that uniquely identifies the resource.
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**
          The list of tag keys.
          - *(string) --*
        :returns: None
        """
        pass
