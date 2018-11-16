from datetime import datetime
from typing import Dict
from botocore.paginate import Paginator


class DescribeCacheClusters(Paginator):
    def paginate(self, CacheClusterId: str = None, ShowCacheNodeInfo: bool = None, ShowCacheClustersNotInReplicationGroups: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheClusters>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CacheClusterId=\'string\',
              ShowCacheNodeInfo=True|False,
              ShowCacheClustersNotInReplicationGroups=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CacheClusterId: string
        :param CacheClusterId: 
        
          The user-supplied cluster identifier. If this parameter is specified, only information about that specific cluster is returned. This parameter isn\'t case sensitive.
        
        :type ShowCacheNodeInfo: boolean
        :param ShowCacheNodeInfo: 
        
          An optional flag that can be included in the ``DescribeCacheCluster`` request to retrieve information about the individual cache nodes.
        
        :type ShowCacheClustersNotInReplicationGroups: boolean
        :param ShowCacheClustersNotInReplicationGroups: 
        
          An optional flag that can be included in the ``DescribeCacheCluster`` request to show only nodes (API/CLI: clusters) that are not members of a replication group. In practice, this mean Memcached and single node Redis clusters.
        
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
                \'CacheClusters\': [
                    {
                        \'CacheClusterId\': \'string\',
                        \'ConfigurationEndpoint\': {
                            \'Address\': \'string\',
                            \'Port\': 123
                        },
                        \'ClientDownloadLandingPage\': \'string\',
                        \'CacheNodeType\': \'string\',
                        \'Engine\': \'string\',
                        \'EngineVersion\': \'string\',
                        \'CacheClusterStatus\': \'string\',
                        \'NumCacheNodes\': 123,
                        \'PreferredAvailabilityZone\': \'string\',
                        \'CacheClusterCreateTime\': datetime(2015, 1, 1),
                        \'PreferredMaintenanceWindow\': \'string\',
                        \'PendingModifiedValues\': {
                            \'NumCacheNodes\': 123,
                            \'CacheNodeIdsToRemove\': [
                                \'string\',
                            ],
                            \'EngineVersion\': \'string\',
                            \'CacheNodeType\': \'string\'
                        },
                        \'NotificationConfiguration\': {
                            \'TopicArn\': \'string\',
                            \'TopicStatus\': \'string\'
                        },
                        \'CacheSecurityGroups\': [
                            {
                                \'CacheSecurityGroupName\': \'string\',
                                \'Status\': \'string\'
                            },
                        ],
                        \'CacheParameterGroup\': {
                            \'CacheParameterGroupName\': \'string\',
                            \'ParameterApplyStatus\': \'string\',
                            \'CacheNodeIdsToReboot\': [
                                \'string\',
                            ]
                        },
                        \'CacheSubnetGroupName\': \'string\',
                        \'CacheNodes\': [
                            {
                                \'CacheNodeId\': \'string\',
                                \'CacheNodeStatus\': \'string\',
                                \'CacheNodeCreateTime\': datetime(2015, 1, 1),
                                \'Endpoint\': {
                                    \'Address\': \'string\',
                                    \'Port\': 123
                                },
                                \'ParameterGroupStatus\': \'string\',
                                \'SourceCacheNodeId\': \'string\',
                                \'CustomerAvailabilityZone\': \'string\'
                            },
                        ],
                        \'AutoMinorVersionUpgrade\': True|False,
                        \'SecurityGroups\': [
                            {
                                \'SecurityGroupId\': \'string\',
                                \'Status\': \'string\'
                            },
                        ],
                        \'ReplicationGroupId\': \'string\',
                        \'SnapshotRetentionLimit\': 123,
                        \'SnapshotWindow\': \'string\',
                        \'AuthTokenEnabled\': True|False,
                        \'TransitEncryptionEnabled\': True|False,
                        \'AtRestEncryptionEnabled\': True|False
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ``DescribeCacheClusters`` operation.
        
            - **CacheClusters** *(list) --* 
        
              A list of clusters. Each item in the list contains detailed information about one cluster.
        
              - *(dict) --* 
        
                Contains all of the attributes of a specific cluster.
        
                - **CacheClusterId** *(string) --* 
        
                  The user-supplied identifier of the cluster. This identifier is a unique key that identifies a cluster.
        
                - **ConfigurationEndpoint** *(dict) --* 
        
                  Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the cluster, can be used by an application to connect to any node in the cluster. The configuration endpoint will always have ``.cfg`` in it.
        
                  Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``  
        
                  - **Address** *(string) --* 
        
                    The DNS hostname of the cache node.
        
                  - **Port** *(integer) --* 
        
                    The port number that the cache engine is listening on.
        
                - **ClientDownloadLandingPage** *(string) --* 
        
                  The URL of the web page where you can download the latest ElastiCache client library.
        
                - **CacheNodeType** *(string) --* 
        
                  The name of the compute and memory capacity node type for the cluster.
        
                  The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.
        
                  * General purpose: 
        
                    * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                     
                    * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                     
                  * Compute optimized: 
        
                    * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                     
                  * Memory optimized: 
        
                    * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``    **R4 node types;**  ``cache.r4.large`` , ``cache.r4.xlarge`` , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``   
                     
                    * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                     
                   **Notes:**  
        
                  * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
                   
                  * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
                   
                  * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
                   
                  * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
                   
                  For a complete listing of node types and specifications, see:
        
                  * `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__   
                   
                  * `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/ParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__   
                   
                  * `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/ParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__   
                   
                - **Engine** *(string) --* 
        
                  The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.
        
                - **EngineVersion** *(string) --* 
        
                  The version of the cache engine that is used in this cluster.
        
                - **CacheClusterStatus** *(string) --* 
        
                  The current state of this cluster, one of the following values: ``available`` , ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` , ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .
        
                - **NumCacheNodes** *(integer) --* 
        
                  The number of cache nodes in the cluster.
        
                  For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.
        
                - **PreferredAvailabilityZone** *(string) --* 
        
                  The name of the Availability Zone in which the cluster is located or \"Multiple\" if the cache nodes are located in different Availability Zones.
        
                - **CacheClusterCreateTime** *(datetime) --* 
        
                  The date and time when the cluster was created.
        
                - **PreferredMaintenanceWindow** *(string) --* 
        
                  Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
        
                  Valid values for ``ddd`` are:
        
                  * ``sun``   
                   
                  * ``mon``   
                   
                  * ``tue``   
                   
                  * ``wed``   
                   
                  * ``thu``   
                   
                  * ``fri``   
                   
                  * ``sat``   
                   
                  Example: ``sun:23:00-mon:01:30``  
        
                - **PendingModifiedValues** *(dict) --* 
        
                  A group of settings that are applied to the cluster in the future, or that are currently being applied.
        
                  - **NumCacheNodes** *(integer) --* 
        
                    The new number of cache nodes for the cluster.
        
                    For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.
        
                  - **CacheNodeIdsToRemove** *(list) --* 
        
                    A list of cache node IDs that are being removed (or will be removed) from the cluster. A node ID is a 4-digit numeric identifier (0001, 0002, etc.).
        
                    - *(string) --* 
                
                  - **EngineVersion** *(string) --* 
        
                    The new cache engine version that the cluster runs.
        
                  - **CacheNodeType** *(string) --* 
        
                    The cache node type that this cluster or replication group is scaled to.
        
                - **NotificationConfiguration** *(dict) --* 
        
                  Describes a notification topic and its status. Notification topics are used for publishing ElastiCache events to subscribers using Amazon Simple Notification Service (SNS). 
        
                  - **TopicArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) that identifies the topic.
        
                  - **TopicStatus** *(string) --* 
        
                    The current state of the topic.
        
                - **CacheSecurityGroups** *(list) --* 
        
                  A list of cache security group elements, composed of name and status sub-elements.
        
                  - *(dict) --* 
        
                    Represents a cluster\'s status within a particular cache security group.
        
                    - **CacheSecurityGroupName** *(string) --* 
        
                      The name of the cache security group.
        
                    - **Status** *(string) --* 
        
                      The membership status in the cache security group. The status changes when a cache security group is modified, or when the cache security groups assigned to a cluster are modified.
        
                - **CacheParameterGroup** *(dict) --* 
        
                  Status of the cache parameter group.
        
                  - **CacheParameterGroupName** *(string) --* 
        
                    The name of the cache parameter group.
        
                  - **ParameterApplyStatus** *(string) --* 
        
                    The status of parameter updates.
        
                  - **CacheNodeIdsToReboot** *(list) --* 
        
                    A list of the cache node IDs which need to be rebooted for parameter changes to be applied. A node ID is a numeric identifier (0001, 0002, etc.).
        
                    - *(string) --* 
                
                - **CacheSubnetGroupName** *(string) --* 
        
                  The name of the cache subnet group associated with the cluster.
        
                - **CacheNodes** *(list) --* 
        
                  A list of cache nodes that are members of the cluster.
        
                  - *(dict) --* 
        
                    Represents an individual cache node within a cluster. Each cache node runs its own instance of the cluster\'s protocol-compliant caching software - either Memcached or Redis.
        
                    The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.
        
                    * General purpose: 
        
                      * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                       
                      * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                       
                    * Compute optimized: 
        
                      * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                       
                    * Memory optimized: 
        
                      * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``    **R4 node types;**  ``cache.r4.large`` , ``cache.r4.xlarge`` , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``   
                       
                      * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                       
                     **Notes:**  
        
                    * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
                     
                    * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
                     
                    * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
                     
                    * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
                     
                    For a complete listing of node types and specifications, see:
        
                    * `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__   
                     
                    * `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/ParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__   
                     
                    * `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/ParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__   
                     
                    - **CacheNodeId** *(string) --* 
        
                      The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The combination of cluster ID and node ID uniquely identifies every cache node used in a customer\'s AWS account.
        
                    - **CacheNodeStatus** *(string) --* 
        
                      The current state of this cache node.
        
                    - **CacheNodeCreateTime** *(datetime) --* 
        
                      The date and time when the cache node was created.
        
                    - **Endpoint** *(dict) --* 
        
                      The hostname for connecting to this cache node.
        
                      - **Address** *(string) --* 
        
                        The DNS hostname of the cache node.
        
                      - **Port** *(integer) --* 
        
                        The port number that the cache engine is listening on.
        
                    - **ParameterGroupStatus** *(string) --* 
        
                      The status of the parameter group applied to this cache node.
        
                    - **SourceCacheNodeId** *(string) --* 
        
                      The ID of the primary node to which this read replica node is synchronized. If this field is empty, this node is not associated with a primary cluster.
        
                    - **CustomerAvailabilityZone** *(string) --* 
        
                      The Availability Zone where this node was created and now resides.
        
                - **AutoMinorVersionUpgrade** *(boolean) --* 
        
                  This parameter is currently disabled.
        
                - **SecurityGroups** *(list) --* 
        
                  A list of VPC Security Groups associated with the cluster.
        
                  - *(dict) --* 
        
                    Represents a single cache security group and its status.
        
                    - **SecurityGroupId** *(string) --* 
        
                      The identifier of the cache security group.
        
                    - **Status** *(string) --* 
        
                      The status of the cache security group membership. The status changes whenever a cache security group is modified, or when the cache security groups assigned to a cluster are modified.
        
                - **ReplicationGroupId** *(string) --* 
        
                  The replication group to which this cluster belongs. If this field is empty, the cluster is not associated with any replication group.
        
                - **SnapshotRetentionLimit** *(integer) --* 
        
                  The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.
        
                  .. warning::
        
                    If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
        
                - **SnapshotWindow** *(string) --* 
        
                  The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster.
        
                  Example: ``05:00-09:00``  
        
                - **AuthTokenEnabled** *(boolean) --* 
        
                  A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.
        
                  Default: ``false``  
        
                - **TransitEncryptionEnabled** *(boolean) --* 
        
                  A flag that enables in-transit encryption when set to ``true`` .
        
                  You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster.
        
                   **Required:** Only available when creating a replication group in an Amazon VPC using redis version ``3.2.6`` or ``4.x`` .
        
                  Default: ``false``  
        
                - **AtRestEncryptionEnabled** *(boolean) --* 
        
                  A flag that enables encryption at-rest when set to ``true`` .
        
                  You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true`` when you create a cluster.
        
                   **Required:** Only available when creating a replication group in an Amazon VPC using redis version ``3.2.6`` or ``4.x`` .
        
                  Default: ``false``  
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeCacheEngineVersions(Paginator):
    def paginate(self, Engine: str = None, EngineVersion: str = None, CacheParameterGroupFamily: str = None, DefaultOnly: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheEngineVersions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Engine=\'string\',
              EngineVersion=\'string\',
              CacheParameterGroupFamily=\'string\',
              DefaultOnly=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Engine: string
        :param Engine: 
        
          The cache engine to return. Valid values: ``memcached`` | ``redis``  
        
        :type EngineVersion: string
        :param EngineVersion: 
        
          The cache engine version to return.
        
          Example: ``1.4.14``  
        
        :type CacheParameterGroupFamily: string
        :param CacheParameterGroupFamily: 
        
          The name of a specific cache parameter group family to return details for.
        
          Valid values are: ``memcached1.4`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2`` | ``redis4.0``  
        
          Constraints:
        
          * Must be 1 to 255 alphanumeric characters 
           
          * First character must be a letter 
           
          * Cannot end with a hyphen or contain two consecutive hyphens 
           
        :type DefaultOnly: boolean
        :param DefaultOnly: 
        
          If ``true`` , specifies that only the default version of the specified engine or engine and major version combination is to be returned.
        
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
                \'CacheEngineVersions\': [
                    {
                        \'Engine\': \'string\',
                        \'EngineVersion\': \'string\',
                        \'CacheParameterGroupFamily\': \'string\',
                        \'CacheEngineDescription\': \'string\',
                        \'CacheEngineVersionDescription\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a  DescribeCacheEngineVersions operation.
        
            - **CacheEngineVersions** *(list) --* 
        
              A list of cache engine version details. Each element in the list contains detailed information about one cache engine version.
        
              - *(dict) --* 
        
                Provides all of the details about a particular cache engine version.
        
                - **Engine** *(string) --* 
        
                  The name of the cache engine.
        
                - **EngineVersion** *(string) --* 
        
                  The version number of the cache engine.
        
                - **CacheParameterGroupFamily** *(string) --* 
        
                  The name of the cache parameter group family associated with this cache engine.
        
                  Valid values are: ``memcached1.4`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2`` | ``redis4.0``  
        
                - **CacheEngineDescription** *(string) --* 
        
                  The description of the cache engine.
        
                - **CacheEngineVersionDescription** *(string) --* 
        
                  The description of the cache engine version.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeCacheParameterGroups(Paginator):
    def paginate(self, CacheParameterGroupName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheParameterGroups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CacheParameterGroupName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CacheParameterGroupName: string
        :param CacheParameterGroupName: 
        
          The name of a specific cache parameter group to return details for.
        
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
                \'CacheParameterGroups\': [
                    {
                        \'CacheParameterGroupName\': \'string\',
                        \'CacheParameterGroupFamily\': \'string\',
                        \'Description\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ``DescribeCacheParameterGroups`` operation.
        
            - **CacheParameterGroups** *(list) --* 
        
              A list of cache parameter groups. Each element in the list contains detailed information about one cache parameter group.
        
              - *(dict) --* 
        
                Represents the output of a ``CreateCacheParameterGroup`` operation.
        
                - **CacheParameterGroupName** *(string) --* 
        
                  The name of the cache parameter group.
        
                - **CacheParameterGroupFamily** *(string) --* 
        
                  The name of the cache parameter group family that this cache parameter group is compatible with.
        
                  Valid values are: ``memcached1.4`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2`` | ``redis4.0``  
        
                - **Description** *(string) --* 
        
                  The description for this cache parameter group.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeCacheParameters(Paginator):
    def paginate(self, CacheParameterGroupName: str, Source: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheParameters>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CacheParameterGroupName=\'string\',
              Source=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CacheParameterGroupName: string
        :param CacheParameterGroupName: **[REQUIRED]** 
        
          The name of a specific cache parameter group to return details for.
        
        :type Source: string
        :param Source: 
        
          The parameter types to return.
        
          Valid values: ``user`` | ``system`` | ``engine-default``  
        
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
                \'Parameters\': [
                    {
                        \'ParameterName\': \'string\',
                        \'ParameterValue\': \'string\',
                        \'Description\': \'string\',
                        \'Source\': \'string\',
                        \'DataType\': \'string\',
                        \'AllowedValues\': \'string\',
                        \'IsModifiable\': True|False,
                        \'MinimumEngineVersion\': \'string\',
                        \'ChangeType\': \'immediate\'|\'requires-reboot\'
                    },
                ],
                \'CacheNodeTypeSpecificParameters\': [
                    {
                        \'ParameterName\': \'string\',
                        \'Description\': \'string\',
                        \'Source\': \'string\',
                        \'DataType\': \'string\',
                        \'AllowedValues\': \'string\',
                        \'IsModifiable\': True|False,
                        \'MinimumEngineVersion\': \'string\',
                        \'CacheNodeTypeSpecificValues\': [
                            {
                                \'CacheNodeType\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'ChangeType\': \'immediate\'|\'requires-reboot\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ``DescribeCacheParameters`` operation.
        
            - **Parameters** *(list) --* 
        
              A list of  Parameter instances.
        
              - *(dict) --* 
        
                Describes an individual setting that controls some aspect of ElastiCache behavior.
        
                - **ParameterName** *(string) --* 
        
                  The name of the parameter.
        
                - **ParameterValue** *(string) --* 
        
                  The value of the parameter.
        
                - **Description** *(string) --* 
        
                  A description of the parameter.
        
                - **Source** *(string) --* 
        
                  The source of the parameter.
        
                - **DataType** *(string) --* 
        
                  The valid data type for the parameter.
        
                - **AllowedValues** *(string) --* 
        
                  The valid range of values for the parameter.
        
                - **IsModifiable** *(boolean) --* 
        
                  Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
        
                - **MinimumEngineVersion** *(string) --* 
        
                  The earliest cache engine version to which the parameter can apply.
        
                - **ChangeType** *(string) --* 
        
                  Indicates whether a change to the parameter is applied immediately or requires a reboot for the change to be applied. You can force a reboot or wait until the next maintenance window\'s reboot. For more information, see `Rebooting a Cluster <http://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__ .
        
            - **CacheNodeTypeSpecificParameters** *(list) --* 
        
              A list of parameters specific to a particular cache node type. Each element in the list contains detailed information about one parameter.
        
              - *(dict) --* 
        
                A parameter that has a different value for each cache node type it is applied to. For example, in a Redis cluster, a ``cache.m1.large`` cache node type would have a larger ``maxmemory`` value than a ``cache.m1.small`` type.
        
                - **ParameterName** *(string) --* 
        
                  The name of the parameter.
        
                - **Description** *(string) --* 
        
                  A description of the parameter.
        
                - **Source** *(string) --* 
        
                  The source of the parameter value.
        
                - **DataType** *(string) --* 
        
                  The valid data type for the parameter.
        
                - **AllowedValues** *(string) --* 
        
                  The valid range of values for the parameter.
        
                - **IsModifiable** *(boolean) --* 
        
                  Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
        
                - **MinimumEngineVersion** *(string) --* 
        
                  The earliest cache engine version to which the parameter can apply.
        
                - **CacheNodeTypeSpecificValues** *(list) --* 
        
                  A list of cache node types and their corresponding values for this parameter.
        
                  - *(dict) --* 
        
                    A value that applies only to a certain cache node type.
        
                    - **CacheNodeType** *(string) --* 
        
                      The cache node type for which this value applies.
        
                    - **Value** *(string) --* 
        
                      The value for the cache node type.
        
                - **ChangeType** *(string) --* 
        
                  Indicates whether a change to the parameter is applied immediately or requires a reboot for the change to be applied. You can force a reboot or wait until the next maintenance window\'s reboot. For more information, see `Rebooting a Cluster <http://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__ .
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeCacheSecurityGroups(Paginator):
    def paginate(self, CacheSecurityGroupName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheSecurityGroups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CacheSecurityGroupName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CacheSecurityGroupName: string
        :param CacheSecurityGroupName: 
        
          The name of the cache security group to return details for.
        
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
                \'CacheSecurityGroups\': [
                    {
                        \'OwnerId\': \'string\',
                        \'CacheSecurityGroupName\': \'string\',
                        \'Description\': \'string\',
                        \'EC2SecurityGroups\': [
                            {
                                \'Status\': \'string\',
                                \'EC2SecurityGroupName\': \'string\',
                                \'EC2SecurityGroupOwnerId\': \'string\'
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ``DescribeCacheSecurityGroups`` operation.
        
            - **CacheSecurityGroups** *(list) --* 
        
              A list of cache security groups. Each element in the list contains detailed information about one group.
        
              - *(dict) --* 
        
                Represents the output of one of the following operations:
        
                * ``AuthorizeCacheSecurityGroupIngress``   
                 
                * ``CreateCacheSecurityGroup``   
                 
                * ``RevokeCacheSecurityGroupIngress``   
                 
                - **OwnerId** *(string) --* 
        
                  The AWS account ID of the cache security group owner.
        
                - **CacheSecurityGroupName** *(string) --* 
        
                  The name of the cache security group.
        
                - **Description** *(string) --* 
        
                  The description of the cache security group.
        
                - **EC2SecurityGroups** *(list) --* 
        
                  A list of Amazon EC2 security groups that are associated with this cache security group.
        
                  - *(dict) --* 
        
                    Provides ownership and status information for an Amazon EC2 security group.
        
                    - **Status** *(string) --* 
        
                      The status of the Amazon EC2 security group.
        
                    - **EC2SecurityGroupName** *(string) --* 
        
                      The name of the Amazon EC2 security group.
        
                    - **EC2SecurityGroupOwnerId** *(string) --* 
        
                      The AWS account ID of the Amazon EC2 security group owner.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeCacheSubnetGroups(Paginator):
    def paginate(self, CacheSubnetGroupName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheSubnetGroups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CacheSubnetGroupName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CacheSubnetGroupName: string
        :param CacheSubnetGroupName: 
        
          The name of the cache subnet group to return details for.
        
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
                \'CacheSubnetGroups\': [
                    {
                        \'CacheSubnetGroupName\': \'string\',
                        \'CacheSubnetGroupDescription\': \'string\',
                        \'VpcId\': \'string\',
                        \'Subnets\': [
                            {
                                \'SubnetIdentifier\': \'string\',
                                \'SubnetAvailabilityZone\': {
                                    \'Name\': \'string\'
                                }
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ``DescribeCacheSubnetGroups`` operation.
        
            - **CacheSubnetGroups** *(list) --* 
        
              A list of cache subnet groups. Each element in the list contains detailed information about one group.
        
              - *(dict) --* 
        
                Represents the output of one of the following operations:
        
                * ``CreateCacheSubnetGroup``   
                 
                * ``ModifyCacheSubnetGroup``   
                 
                - **CacheSubnetGroupName** *(string) --* 
        
                  The name of the cache subnet group.
        
                - **CacheSubnetGroupDescription** *(string) --* 
        
                  The description of the cache subnet group.
        
                - **VpcId** *(string) --* 
        
                  The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.
        
                - **Subnets** *(list) --* 
        
                  A list of subnets associated with the cache subnet group.
        
                  - *(dict) --* 
        
                    Represents the subnet associated with a cluster. This parameter refers to subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.
        
                    - **SubnetIdentifier** *(string) --* 
        
                      The unique identifier for the subnet.
        
                    - **SubnetAvailabilityZone** *(dict) --* 
        
                      The Availability Zone associated with the subnet.
        
                      - **Name** *(string) --* 
        
                        The name of the Availability Zone.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeEngineDefaultParameters(Paginator):
    def paginate(self, CacheParameterGroupFamily: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeEngineDefaultParameters>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CacheParameterGroupFamily=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CacheParameterGroupFamily: string
        :param CacheParameterGroupFamily: **[REQUIRED]** 
        
          The name of the cache parameter group family.
        
          Valid values are: ``memcached1.4`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2`` | ``redis4.0``  
        
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
                \'EngineDefaults\': {
                    \'CacheParameterGroupFamily\': \'string\',
                    \'Marker\': \'string\',
                    \'Parameters\': [
                        {
                            \'ParameterName\': \'string\',
                            \'ParameterValue\': \'string\',
                            \'Description\': \'string\',
                            \'Source\': \'string\',
                            \'DataType\': \'string\',
                            \'AllowedValues\': \'string\',
                            \'IsModifiable\': True|False,
                            \'MinimumEngineVersion\': \'string\',
                            \'ChangeType\': \'immediate\'|\'requires-reboot\'
                        },
                    ],
                    \'CacheNodeTypeSpecificParameters\': [
                        {
                            \'ParameterName\': \'string\',
                            \'Description\': \'string\',
                            \'Source\': \'string\',
                            \'DataType\': \'string\',
                            \'AllowedValues\': \'string\',
                            \'IsModifiable\': True|False,
                            \'MinimumEngineVersion\': \'string\',
                            \'CacheNodeTypeSpecificValues\': [
                                {
                                    \'CacheNodeType\': \'string\',
                                    \'Value\': \'string\'
                                },
                            ],
                            \'ChangeType\': \'immediate\'|\'requires-reboot\'
                        },
                    ]
                },
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **EngineDefaults** *(dict) --* 
        
              Represents the output of a ``DescribeEngineDefaultParameters`` operation.
        
              - **CacheParameterGroupFamily** *(string) --* 
        
                Specifies the name of the cache parameter group family to which the engine default parameters apply.
        
                Valid values are: ``memcached1.4`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2`` | ``redis4.0``  
        
              - **Marker** *(string) --* 
        
                Provides an identifier to allow retrieval of paginated results.
        
              - **Parameters** *(list) --* 
        
                Contains a list of engine default parameters.
        
                - *(dict) --* 
        
                  Describes an individual setting that controls some aspect of ElastiCache behavior.
        
                  - **ParameterName** *(string) --* 
        
                    The name of the parameter.
        
                  - **ParameterValue** *(string) --* 
        
                    The value of the parameter.
        
                  - **Description** *(string) --* 
        
                    A description of the parameter.
        
                  - **Source** *(string) --* 
        
                    The source of the parameter.
        
                  - **DataType** *(string) --* 
        
                    The valid data type for the parameter.
        
                  - **AllowedValues** *(string) --* 
        
                    The valid range of values for the parameter.
        
                  - **IsModifiable** *(boolean) --* 
        
                    Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
        
                  - **MinimumEngineVersion** *(string) --* 
        
                    The earliest cache engine version to which the parameter can apply.
        
                  - **ChangeType** *(string) --* 
        
                    Indicates whether a change to the parameter is applied immediately or requires a reboot for the change to be applied. You can force a reboot or wait until the next maintenance window\'s reboot. For more information, see `Rebooting a Cluster <http://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__ .
        
              - **CacheNodeTypeSpecificParameters** *(list) --* 
        
                A list of parameters specific to a particular cache node type. Each element in the list contains detailed information about one parameter.
        
                - *(dict) --* 
        
                  A parameter that has a different value for each cache node type it is applied to. For example, in a Redis cluster, a ``cache.m1.large`` cache node type would have a larger ``maxmemory`` value than a ``cache.m1.small`` type.
        
                  - **ParameterName** *(string) --* 
        
                    The name of the parameter.
        
                  - **Description** *(string) --* 
        
                    A description of the parameter.
        
                  - **Source** *(string) --* 
        
                    The source of the parameter value.
        
                  - **DataType** *(string) --* 
        
                    The valid data type for the parameter.
        
                  - **AllowedValues** *(string) --* 
        
                    The valid range of values for the parameter.
        
                  - **IsModifiable** *(boolean) --* 
        
                    Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
        
                  - **MinimumEngineVersion** *(string) --* 
        
                    The earliest cache engine version to which the parameter can apply.
        
                  - **CacheNodeTypeSpecificValues** *(list) --* 
        
                    A list of cache node types and their corresponding values for this parameter.
        
                    - *(dict) --* 
        
                      A value that applies only to a certain cache node type.
        
                      - **CacheNodeType** *(string) --* 
        
                        The cache node type for which this value applies.
        
                      - **Value** *(string) --* 
        
                        The value for the cache node type.
        
                  - **ChangeType** *(string) --* 
        
                    Indicates whether a change to the parameter is applied immediately or requires a reboot for the change to be applied. You can force a reboot or wait until the next maintenance window\'s reboot. For more information, see `Rebooting a Cluster <http://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__ .
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeEvents(Paginator):
    def paginate(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeEvents>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              SourceIdentifier=\'string\',
              SourceType=\'cache-cluster\'|\'cache-parameter-group\'|\'cache-security-group\'|\'cache-subnet-group\'|\'replication-group\',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Duration=123,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type SourceIdentifier: string
        :param SourceIdentifier: 
        
          The identifier of the event source for which events are returned. If not specified, all sources are included in the response.
        
        :type SourceType: string
        :param SourceType: 
        
          The event source to retrieve events for. If no value is specified, all events are returned.
        
        :type StartTime: datetime
        :param StartTime: 
        
          The beginning of the time interval to retrieve events for, specified in ISO 8601 format.
        
           **Example:** 2017-03-30T07:03:49.555Z
        
        :type EndTime: datetime
        :param EndTime: 
        
          The end of the time interval for which to retrieve events, specified in ISO 8601 format.
        
           **Example:** 2017-03-30T07:03:49.555Z
        
        :type Duration: integer
        :param Duration: 
        
          The number of minutes worth of events to retrieve.
        
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
                \'Events\': [
                    {
                        \'SourceIdentifier\': \'string\',
                        \'SourceType\': \'cache-cluster\'|\'cache-parameter-group\'|\'cache-security-group\'|\'cache-subnet-group\'|\'replication-group\',
                        \'Message\': \'string\',
                        \'Date\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ``DescribeEvents`` operation.
        
            - **Events** *(list) --* 
        
              A list of events. Each element in the list contains detailed information about one event.
        
              - *(dict) --* 
        
                Represents a single occurrence of something interesting within the system. Some examples of events are creating a cluster, adding or removing a cache node, or rebooting a node.
        
                - **SourceIdentifier** *(string) --* 
        
                  The identifier for the source of the event. For example, if the event occurred at the cluster level, the identifier would be the name of the cluster.
        
                - **SourceType** *(string) --* 
        
                  Specifies the origin of this event - a cluster, a parameter group, a security group, etc.
        
                - **Message** *(string) --* 
        
                  The text of the event.
        
                - **Date** *(datetime) --* 
        
                  The date and time when the event occurred.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeReplicationGroups(Paginator):
    def paginate(self, ReplicationGroupId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeReplicationGroups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ReplicationGroupId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ReplicationGroupId: string
        :param ReplicationGroupId: 
        
          The identifier for the replication group to be described. This parameter is not case sensitive.
        
          If you do not specify this parameter, information about all replication groups is returned.
        
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
                \'ReplicationGroups\': [
                    {
                        \'ReplicationGroupId\': \'string\',
                        \'Description\': \'string\',
                        \'Status\': \'string\',
                        \'PendingModifiedValues\': {
                            \'PrimaryClusterId\': \'string\',
                            \'AutomaticFailoverStatus\': \'enabled\'|\'disabled\',
                            \'Resharding\': {
                                \'SlotMigration\': {
                                    \'ProgressPercentage\': 123.0
                                }
                            }
                        },
                        \'MemberClusters\': [
                            \'string\',
                        ],
                        \'NodeGroups\': [
                            {
                                \'NodeGroupId\': \'string\',
                                \'Status\': \'string\',
                                \'PrimaryEndpoint\': {
                                    \'Address\': \'string\',
                                    \'Port\': 123
                                },
                                \'Slots\': \'string\',
                                \'NodeGroupMembers\': [
                                    {
                                        \'CacheClusterId\': \'string\',
                                        \'CacheNodeId\': \'string\',
                                        \'ReadEndpoint\': {
                                            \'Address\': \'string\',
                                            \'Port\': 123
                                        },
                                        \'PreferredAvailabilityZone\': \'string\',
                                        \'CurrentRole\': \'string\'
                                    },
                                ]
                            },
                        ],
                        \'SnapshottingClusterId\': \'string\',
                        \'AutomaticFailover\': \'enabled\'|\'disabled\'|\'enabling\'|\'disabling\',
                        \'ConfigurationEndpoint\': {
                            \'Address\': \'string\',
                            \'Port\': 123
                        },
                        \'SnapshotRetentionLimit\': 123,
                        \'SnapshotWindow\': \'string\',
                        \'ClusterEnabled\': True|False,
                        \'CacheNodeType\': \'string\',
                        \'AuthTokenEnabled\': True|False,
                        \'TransitEncryptionEnabled\': True|False,
                        \'AtRestEncryptionEnabled\': True|False
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ``DescribeReplicationGroups`` operation.
        
            - **ReplicationGroups** *(list) --* 
        
              A list of replication groups. Each item in the list contains detailed information about one replication group.
        
              - *(dict) --* 
        
                Contains all of the attributes of a specific Redis replication group.
        
                - **ReplicationGroupId** *(string) --* 
        
                  The identifier for the replication group.
        
                - **Description** *(string) --* 
        
                  The user supplied description of the replication group.
        
                - **Status** *(string) --* 
        
                  The current state of this replication group - ``creating`` , ``available`` , ``modifying`` , ``deleting`` , ``create-failed`` , ``snapshotting`` .
        
                - **PendingModifiedValues** *(dict) --* 
        
                  A group of settings to be applied to the replication group, either immediately or during the next maintenance window.
        
                  - **PrimaryClusterId** *(string) --* 
        
                    The primary cluster ID that is applied immediately (if ``--apply-immediately`` was specified), or during the next maintenance window.
        
                  - **AutomaticFailoverStatus** *(string) --* 
        
                    Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
        
                    Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:
        
                    * Redis versions earlier than 2.8.6. 
                     
                    * Redis (cluster mode disabled): T1 and T2 cache node types. 
                     
                    * Redis (cluster mode enabled): T1 node types. 
                     
                  - **Resharding** *(dict) --* 
        
                    The status of an online resharding operation.
        
                    - **SlotMigration** *(dict) --* 
        
                      Represents the progress of an online resharding operation.
        
                      - **ProgressPercentage** *(float) --* 
        
                        The percentage of the slot migration that is complete.
        
                - **MemberClusters** *(list) --* 
        
                  The names of all the cache clusters that are part of this replication group.
        
                  - *(string) --* 
              
                - **NodeGroups** *(list) --* 
        
                  A list of node groups in this replication group. For Redis (cluster mode disabled) replication groups, this is a single-element list. For Redis (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).
        
                  - *(dict) --* 
        
                    Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.
        
                    - **NodeGroupId** *(string) --* 
        
                      The identifier for the node group (shard). A Redis (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Redis (cluster mode enabled) replication group contains 1 to 15 node groups numbered 0001 to 0015. 
        
                    - **Status** *(string) --* 
        
                      The current state of this replication group - ``creating`` , ``available`` , etc.
        
                    - **PrimaryEndpoint** *(dict) --* 
        
                      The endpoint of the primary node in this node group (shard).
        
                      - **Address** *(string) --* 
        
                        The DNS hostname of the cache node.
        
                      - **Port** *(integer) --* 
        
                        The port number that the cache engine is listening on.
        
                    - **Slots** *(string) --* 
        
                      The keyspace for this node group (shard).
        
                    - **NodeGroupMembers** *(list) --* 
        
                      A list containing information about individual nodes within the node group (shard).
        
                      - *(dict) --* 
        
                        Represents a single node within a node group (shard).
        
                        - **CacheClusterId** *(string) --* 
        
                          The ID of the cluster to which the node belongs.
        
                        - **CacheNodeId** *(string) --* 
        
                          The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).
        
                        - **ReadEndpoint** *(dict) --* 
        
                          The information required for client programs to connect to a node for read operations. The read endpoint is only applicable on Redis (cluster mode disabled) clusters.
        
                          - **Address** *(string) --* 
        
                            The DNS hostname of the cache node.
        
                          - **Port** *(integer) --* 
        
                            The port number that the cache engine is listening on.
        
                        - **PreferredAvailabilityZone** *(string) --* 
        
                          The name of the Availability Zone in which the node is located.
        
                        - **CurrentRole** *(string) --* 
        
                          The role that is currently assigned to the node - ``primary`` or ``replica`` . This member is only applicable for Redis (cluster mode disabled) replication groups.
        
                - **SnapshottingClusterId** *(string) --* 
        
                  The cluster ID that is used as the daily snapshot source for the replication group.
        
                - **AutomaticFailover** *(string) --* 
        
                  Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
        
                  Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:
        
                  * Redis versions earlier than 2.8.6. 
                   
                  * Redis (cluster mode disabled): T1 and T2 cache node types. 
                   
                  * Redis (cluster mode enabled): T1 node types. 
                   
                - **ConfigurationEndpoint** *(dict) --* 
        
                  The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.
        
                  - **Address** *(string) --* 
        
                    The DNS hostname of the cache node.
        
                  - **Port** *(integer) --* 
        
                    The port number that the cache engine is listening on.
        
                - **SnapshotRetentionLimit** *(integer) --* 
        
                  The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.
        
                  .. warning::
        
                    If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.
        
                - **SnapshotWindow** *(string) --* 
        
                  The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
        
                  Example: ``05:00-09:00``  
        
                  If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.
        
                  .. note::
        
                    This parameter is only valid if the ``Engine`` parameter is ``redis`` .
        
                - **ClusterEnabled** *(boolean) --* 
        
                  A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).
        
                  Valid values: ``true`` | ``false``  
        
                - **CacheNodeType** *(string) --* 
        
                  The name of the compute and memory capacity node type for each node in the replication group.
        
                - **AuthTokenEnabled** *(boolean) --* 
        
                  A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.
        
                  Default: ``false``  
        
                - **TransitEncryptionEnabled** *(boolean) --* 
        
                  A flag that enables in-transit encryption when set to ``true`` .
        
                  You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster.
        
                   **Required:** Only available when creating a replication group in an Amazon VPC using redis version ``3.2.6`` or ``4.x`` .
        
                  Default: ``false``  
        
                - **AtRestEncryptionEnabled** *(boolean) --* 
        
                  A flag that enables encryption at-rest when set to ``true`` .
        
                  You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true`` when you create a cluster.
        
                   **Required:** Only available when creating a replication group in an Amazon VPC using redis version ``3.2.6`` or ``4.x`` .
        
                  Default: ``false``  
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeReservedCacheNodes(Paginator):
    def paginate(self, ReservedCacheNodeId: str = None, ReservedCacheNodesOfferingId: str = None, CacheNodeType: str = None, Duration: str = None, ProductDescription: str = None, OfferingType: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeReservedCacheNodes>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ReservedCacheNodeId=\'string\',
              ReservedCacheNodesOfferingId=\'string\',
              CacheNodeType=\'string\',
              Duration=\'string\',
              ProductDescription=\'string\',
              OfferingType=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ReservedCacheNodeId: string
        :param ReservedCacheNodeId: 
        
          The reserved cache node identifier filter value. Use this parameter to show only the reservation that matches the specified reservation ID.
        
        :type ReservedCacheNodesOfferingId: string
        :param ReservedCacheNodesOfferingId: 
        
          The offering identifier filter value. Use this parameter to show only purchased reservations matching the specified offering identifier.
        
        :type CacheNodeType: string
        :param CacheNodeType: 
        
          The cache node type filter value. Use this parameter to show only those reservations matching the specified cache node type.
        
          The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.
        
          * General purpose: 
        
            * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
             
            * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
             
          * Compute optimized: 
        
            * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
             
          * Memory optimized: 
        
            * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``    **R4 node types;**  ``cache.r4.large`` , ``cache.r4.xlarge`` , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``   
             
            * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
             
           **Notes:**  
        
          * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
           
          * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
           
          * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
           
          * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
           
          For a complete listing of node types and specifications, see:
        
          * `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__   
           
          * `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/ParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__   
           
          * `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/ParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__   
           
        :type Duration: string
        :param Duration: 
        
          The duration filter value, specified in years or seconds. Use this parameter to show only reservations for this duration.
        
          Valid Values: ``1 | 3 | 31536000 | 94608000``  
        
        :type ProductDescription: string
        :param ProductDescription: 
        
          The product description filter value. Use this parameter to show only those reservations matching the specified product description.
        
        :type OfferingType: string
        :param OfferingType: 
        
          The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type.
        
          Valid values: ``\"Light Utilization\"|\"Medium Utilization\"|\"Heavy Utilization\"``  
        
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
                \'ReservedCacheNodes\': [
                    {
                        \'ReservedCacheNodeId\': \'string\',
                        \'ReservedCacheNodesOfferingId\': \'string\',
                        \'CacheNodeType\': \'string\',
                        \'StartTime\': datetime(2015, 1, 1),
                        \'Duration\': 123,
                        \'FixedPrice\': 123.0,
                        \'UsagePrice\': 123.0,
                        \'CacheNodeCount\': 123,
                        \'ProductDescription\': \'string\',
                        \'OfferingType\': \'string\',
                        \'State\': \'string\',
                        \'RecurringCharges\': [
                            {
                                \'RecurringChargeAmount\': 123.0,
                                \'RecurringChargeFrequency\': \'string\'
                            },
                        ],
                        \'ReservationARN\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ``DescribeReservedCacheNodes`` operation.
        
            - **ReservedCacheNodes** *(list) --* 
        
              A list of reserved cache nodes. Each element in the list contains detailed information about one node.
        
              - *(dict) --* 
        
                Represents the output of a ``PurchaseReservedCacheNodesOffering`` operation.
        
                - **ReservedCacheNodeId** *(string) --* 
        
                  The unique identifier for the reservation.
        
                - **ReservedCacheNodesOfferingId** *(string) --* 
        
                  The offering identifier.
        
                - **CacheNodeType** *(string) --* 
        
                  The cache node type for the reserved cache nodes.
        
                  The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.
        
                  * General purpose: 
        
                    * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                     
                    * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                     
                  * Compute optimized: 
        
                    * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                     
                  * Memory optimized: 
        
                    * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``    **R4 node types;**  ``cache.r4.large`` , ``cache.r4.xlarge`` , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``   
                     
                    * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                     
                   **Notes:**  
        
                  * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
                   
                  * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
                   
                  * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
                   
                  * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
                   
                  For a complete listing of node types and specifications, see:
        
                  * `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__   
                   
                  * `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/ParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__   
                   
                  * `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/ParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__   
                   
                - **StartTime** *(datetime) --* 
        
                  The time the reservation started.
        
                - **Duration** *(integer) --* 
        
                  The duration of the reservation in seconds.
        
                - **FixedPrice** *(float) --* 
        
                  The fixed price charged for this reserved cache node.
        
                - **UsagePrice** *(float) --* 
        
                  The hourly price charged for this reserved cache node.
        
                - **CacheNodeCount** *(integer) --* 
        
                  The number of cache nodes that have been reserved.
        
                - **ProductDescription** *(string) --* 
        
                  The description of the reserved cache node.
        
                - **OfferingType** *(string) --* 
        
                  The offering type of this reserved cache node.
        
                - **State** *(string) --* 
        
                  The state of the reserved cache node.
        
                - **RecurringCharges** *(list) --* 
        
                  The recurring price charged to run this reserved cache node.
        
                  - *(dict) --* 
        
                    Contains the specific price and frequency of a recurring charges for a reserved cache node, or for a reserved cache node offering.
        
                    - **RecurringChargeAmount** *(float) --* 
        
                      The monetary amount of the recurring charge.
        
                    - **RecurringChargeFrequency** *(string) --* 
        
                      The frequency of the recurring charge.
        
                - **ReservationARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the reserved cache node.
        
                  Example: ``arn:aws:elasticache:us-east-1:123456789012:reserved-instance:ri-2017-03-27-08-33-25-582``  
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeReservedCacheNodesOfferings(Paginator):
    def paginate(self, ReservedCacheNodesOfferingId: str = None, CacheNodeType: str = None, Duration: str = None, ProductDescription: str = None, OfferingType: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeReservedCacheNodesOfferings>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ReservedCacheNodesOfferingId=\'string\',
              CacheNodeType=\'string\',
              Duration=\'string\',
              ProductDescription=\'string\',
              OfferingType=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ReservedCacheNodesOfferingId: string
        :param ReservedCacheNodesOfferingId: 
        
          The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.
        
          Example: ``438012d3-4052-4cc7-b2e3-8d3372e0e706``  
        
        :type CacheNodeType: string
        :param CacheNodeType: 
        
          The cache node type filter value. Use this parameter to show only the available offerings matching the specified cache node type.
        
          The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.
        
          * General purpose: 
        
            * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
             
            * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
             
          * Compute optimized: 
        
            * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
             
          * Memory optimized: 
        
            * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``    **R4 node types;**  ``cache.r4.large`` , ``cache.r4.xlarge`` , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``   
             
            * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
             
           **Notes:**  
        
          * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
           
          * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
           
          * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
           
          * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
           
          For a complete listing of node types and specifications, see:
        
          * `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__   
           
          * `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/ParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__   
           
          * `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/ParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__   
           
        :type Duration: string
        :param Duration: 
        
          Duration filter value, specified in years or seconds. Use this parameter to show only reservations for a given duration.
        
          Valid Values: ``1 | 3 | 31536000 | 94608000``  
        
        :type ProductDescription: string
        :param ProductDescription: 
        
          The product description filter value. Use this parameter to show only the available offerings matching the specified product description.
        
        :type OfferingType: string
        :param OfferingType: 
        
          The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type.
        
          Valid Values: ``\"Light Utilization\"|\"Medium Utilization\"|\"Heavy Utilization\"``  
        
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
                \'ReservedCacheNodesOfferings\': [
                    {
                        \'ReservedCacheNodesOfferingId\': \'string\',
                        \'CacheNodeType\': \'string\',
                        \'Duration\': 123,
                        \'FixedPrice\': 123.0,
                        \'UsagePrice\': 123.0,
                        \'ProductDescription\': \'string\',
                        \'OfferingType\': \'string\',
                        \'RecurringCharges\': [
                            {
                                \'RecurringChargeAmount\': 123.0,
                                \'RecurringChargeFrequency\': \'string\'
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ``DescribeReservedCacheNodesOfferings`` operation.
        
            - **ReservedCacheNodesOfferings** *(list) --* 
        
              A list of reserved cache node offerings. Each element in the list contains detailed information about one offering.
        
              - *(dict) --* 
        
                Describes all of the attributes of a reserved cache node offering.
        
                - **ReservedCacheNodesOfferingId** *(string) --* 
        
                  A unique identifier for the reserved cache node offering.
        
                - **CacheNodeType** *(string) --* 
        
                  The cache node type for the reserved cache node.
        
                  The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.
        
                  * General purpose: 
        
                    * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                     
                    * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                     
                  * Compute optimized: 
        
                    * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                     
                  * Memory optimized: 
        
                    * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``    **R4 node types;**  ``cache.r4.large`` , ``cache.r4.xlarge`` , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``   
                     
                    * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                     
                   **Notes:**  
        
                  * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
                   
                  * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
                   
                  * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
                   
                  * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
                   
                  For a complete listing of node types and specifications, see:
        
                  * `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__   
                   
                  * `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/ParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__   
                   
                  * `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/ParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__   
                   
                - **Duration** *(integer) --* 
        
                  The duration of the offering. in seconds.
        
                - **FixedPrice** *(float) --* 
        
                  The fixed price charged for this offering.
        
                - **UsagePrice** *(float) --* 
        
                  The hourly price charged for this offering.
        
                - **ProductDescription** *(string) --* 
        
                  The cache engine used by the offering.
        
                - **OfferingType** *(string) --* 
        
                  The offering type.
        
                - **RecurringCharges** *(list) --* 
        
                  The recurring price charged to run this reserved cache node.
        
                  - *(dict) --* 
        
                    Contains the specific price and frequency of a recurring charges for a reserved cache node, or for a reserved cache node offering.
        
                    - **RecurringChargeAmount** *(float) --* 
        
                      The monetary amount of the recurring charge.
        
                    - **RecurringChargeFrequency** *(string) --* 
        
                      The frequency of the recurring charge.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeSnapshots(Paginator):
    def paginate(self, ReplicationGroupId: str = None, CacheClusterId: str = None, SnapshotName: str = None, SnapshotSource: str = None, ShowNodeGroupConfig: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeSnapshots>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ReplicationGroupId=\'string\',
              CacheClusterId=\'string\',
              SnapshotName=\'string\',
              SnapshotSource=\'string\',
              ShowNodeGroupConfig=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ReplicationGroupId: string
        :param ReplicationGroupId: 
        
          A user-supplied replication group identifier. If this parameter is specified, only snapshots associated with that specific replication group are described.
        
        :type CacheClusterId: string
        :param CacheClusterId: 
        
          A user-supplied cluster identifier. If this parameter is specified, only snapshots associated with that specific cluster are described.
        
        :type SnapshotName: string
        :param SnapshotName: 
        
          A user-supplied name of the snapshot. If this parameter is specified, only this snapshot are described.
        
        :type SnapshotSource: string
        :param SnapshotSource: 
        
          If set to ``system`` , the output shows snapshots that were automatically created by ElastiCache. If set to ``user`` the output shows snapshots that were manually created. If omitted, the output shows both automatically and manually created snapshots.
        
        :type ShowNodeGroupConfig: boolean
        :param ShowNodeGroupConfig: 
        
          A Boolean value which if true, the node group (shard) configuration is included in the snapshot description.
        
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
                \'Snapshots\': [
                    {
                        \'SnapshotName\': \'string\',
                        \'ReplicationGroupId\': \'string\',
                        \'ReplicationGroupDescription\': \'string\',
                        \'CacheClusterId\': \'string\',
                        \'SnapshotStatus\': \'string\',
                        \'SnapshotSource\': \'string\',
                        \'CacheNodeType\': \'string\',
                        \'Engine\': \'string\',
                        \'EngineVersion\': \'string\',
                        \'NumCacheNodes\': 123,
                        \'PreferredAvailabilityZone\': \'string\',
                        \'CacheClusterCreateTime\': datetime(2015, 1, 1),
                        \'PreferredMaintenanceWindow\': \'string\',
                        \'TopicArn\': \'string\',
                        \'Port\': 123,
                        \'CacheParameterGroupName\': \'string\',
                        \'CacheSubnetGroupName\': \'string\',
                        \'VpcId\': \'string\',
                        \'AutoMinorVersionUpgrade\': True|False,
                        \'SnapshotRetentionLimit\': 123,
                        \'SnapshotWindow\': \'string\',
                        \'NumNodeGroups\': 123,
                        \'AutomaticFailover\': \'enabled\'|\'disabled\'|\'enabling\'|\'disabling\',
                        \'NodeSnapshots\': [
                            {
                                \'CacheClusterId\': \'string\',
                                \'NodeGroupId\': \'string\',
                                \'CacheNodeId\': \'string\',
                                \'NodeGroupConfiguration\': {
                                    \'NodeGroupId\': \'string\',
                                    \'Slots\': \'string\',
                                    \'ReplicaCount\': 123,
                                    \'PrimaryAvailabilityZone\': \'string\',
                                    \'ReplicaAvailabilityZones\': [
                                        \'string\',
                                    ]
                                },
                                \'CacheSize\': \'string\',
                                \'CacheNodeCreateTime\': datetime(2015, 1, 1),
                                \'SnapshotCreateTime\': datetime(2015, 1, 1)
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a ``DescribeSnapshots`` operation.
        
            - **Snapshots** *(list) --* 
        
              A list of snapshots. Each item in the list contains detailed information about one snapshot.
        
              - *(dict) --* 
        
                Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.
        
                - **SnapshotName** *(string) --* 
        
                  The name of a snapshot. For an automatic snapshot, the name is system-generated. For a manual snapshot, this is the user-provided name.
        
                - **ReplicationGroupId** *(string) --* 
        
                  The unique identifier of the source replication group.
        
                - **ReplicationGroupDescription** *(string) --* 
        
                  A description of the source replication group.
        
                - **CacheClusterId** *(string) --* 
        
                  The user-supplied identifier of the source cluster.
        
                - **SnapshotStatus** *(string) --* 
        
                  The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` | ``copying`` | ``deleting`` .
        
                - **SnapshotSource** *(string) --* 
        
                  Indicates whether the snapshot is from an automatic backup (``automated`` ) or was created manually (``manual`` ).
        
                - **CacheNodeType** *(string) --* 
        
                  The name of the compute and memory capacity node type for the source cluster.
        
                  The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.
        
                  * General purpose: 
        
                    * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                     
                    * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                     
                  * Compute optimized: 
        
                    * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                     
                  * Memory optimized: 
        
                    * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``    **R4 node types;**  ``cache.r4.large`` , ``cache.r4.xlarge`` , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``   
                     
                    * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                     
                   **Notes:**  
        
                  * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
                   
                  * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
                   
                  * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
                   
                  * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
                   
                  For a complete listing of node types and specifications, see:
        
                  * `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__   
                   
                  * `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/ParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__   
                   
                  * `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/ParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__   
                   
                - **Engine** *(string) --* 
        
                  The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.
        
                - **EngineVersion** *(string) --* 
        
                  The version of the cache engine version that is used by the source cluster.
        
                - **NumCacheNodes** *(integer) --* 
        
                  The number of cache nodes in the source cluster.
        
                  For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.
        
                - **PreferredAvailabilityZone** *(string) --* 
        
                  The name of the Availability Zone in which the source cluster is located.
        
                - **CacheClusterCreateTime** *(datetime) --* 
        
                  The date and time when the source cluster was created.
        
                - **PreferredMaintenanceWindow** *(string) --* 
        
                  Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
        
                  Valid values for ``ddd`` are:
        
                  * ``sun``   
                   
                  * ``mon``   
                   
                  * ``tue``   
                   
                  * ``wed``   
                   
                  * ``thu``   
                   
                  * ``fri``   
                   
                  * ``sat``   
                   
                  Example: ``sun:23:00-mon:01:30``  
        
                - **TopicArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing notifications.
        
                - **Port** *(integer) --* 
        
                  The port number used by each cache nodes in the source cluster.
        
                - **CacheParameterGroupName** *(string) --* 
        
                  The cache parameter group that is associated with the source cluster.
        
                - **CacheSubnetGroupName** *(string) --* 
        
                  The name of the cache subnet group associated with the source cluster.
        
                - **VpcId** *(string) --* 
        
                  The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the source cluster.
        
                - **AutoMinorVersionUpgrade** *(boolean) --* 
        
                  This parameter is currently disabled.
        
                - **SnapshotRetentionLimit** *(integer) --* 
        
                  For an automatic snapshot, the number of days for which ElastiCache retains the snapshot before deleting it.
        
                  For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do not expire, and can only be deleted using the ``DeleteSnapshot`` operation. 
        
                   **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
        
                - **SnapshotWindow** *(string) --* 
        
                  The daily time range during which ElastiCache takes daily snapshots of the source cluster.
        
                - **NumNodeGroups** *(integer) --* 
        
                  The number of node groups (shards) in this snapshot. When restoring from a snapshot, the number of node groups (shards) in the snapshot and in the restored replication group must be the same.
        
                - **AutomaticFailover** *(string) --* 
        
                  Indicates the status of Multi-AZ with automatic failover for the source Redis replication group.
        
                  Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:
        
                  * Redis versions earlier than 2.8.6. 
                   
                  * Redis (cluster mode disabled): T1 and T2 cache node types. 
                   
                  * Redis (cluster mode enabled): T1 node types. 
                   
                - **NodeSnapshots** *(list) --* 
        
                  A list of the cache nodes in the source cluster.
        
                  - *(dict) --* 
        
                    Represents an individual cache node in a snapshot of a cluster.
        
                    - **CacheClusterId** *(string) --* 
        
                      A unique identifier for the source cluster.
        
                    - **NodeGroupId** *(string) --* 
        
                      A unique identifier for the source node group (shard).
        
                    - **CacheNodeId** *(string) --* 
        
                      The cache node identifier for the node in the source cluster.
        
                    - **NodeGroupConfiguration** *(dict) --* 
        
                      The configuration for the source node group (shard).
        
                      - **NodeGroupId** *(string) --* 
        
                        The 4-digit id for the node group these configuration values apply to.
        
                      - **Slots** *(string) --* 
        
                        A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to 16,383. The string is in the format ``startkey-endkey`` .
        
                        Example: ``\"0-3999\"``  
        
                      - **ReplicaCount** *(integer) --* 
        
                        The number of read replica nodes in this node group (shard).
        
                      - **PrimaryAvailabilityZone** *(string) --* 
        
                        The Availability Zone where the primary node of this node group (shard) is launched.
        
                      - **ReplicaAvailabilityZones** *(list) --* 
        
                        A list of Availability Zones to be used for the read replicas. The number of Availability Zones in this list must match the value of ``ReplicaCount`` or ``ReplicasPerNodeGroup`` if not specified.
        
                        - *(string) --* 
                    
                    - **CacheSize** *(string) --* 
        
                      The size of the cache on the source cache node.
        
                    - **CacheNodeCreateTime** *(datetime) --* 
        
                      The date and time when the cache node was created in the source cluster.
        
                    - **SnapshotCreateTime** *(datetime) --* 
        
                      The date and time when the source node\'s metadata and cache data set was obtained for the snapshot.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
