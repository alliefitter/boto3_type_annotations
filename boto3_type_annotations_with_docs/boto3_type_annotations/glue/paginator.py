from typing import List
from typing import Dict
from botocore.paginate import Paginator


class GetClassifiers(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetClassifiers>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'Classifiers\': [
                    {
                        \'GrokClassifier\': {
                            \'Name\': \'string\',
                            \'Classification\': \'string\',
                            \'CreationTime\': datetime(2015, 1, 1),
                            \'LastUpdated\': datetime(2015, 1, 1),
                            \'Version\': 123,
                            \'GrokPattern\': \'string\',
                            \'CustomPatterns\': \'string\'
                        },
                        \'XMLClassifier\': {
                            \'Name\': \'string\',
                            \'Classification\': \'string\',
                            \'CreationTime\': datetime(2015, 1, 1),
                            \'LastUpdated\': datetime(2015, 1, 1),
                            \'Version\': 123,
                            \'RowTag\': \'string\'
                        },
                        \'JsonClassifier\': {
                            \'Name\': \'string\',
                            \'CreationTime\': datetime(2015, 1, 1),
                            \'LastUpdated\': datetime(2015, 1, 1),
                            \'Version\': 123,
                            \'JsonPath\': \'string\'
                        }
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Classifiers** *(list) --* 
        
              The requested list of classifier objects.
        
              - *(dict) --* 
        
                Classifiers are triggered during a crawl task. A classifier checks whether a given file is in a format it can handle, and if it is, the classifier creates a schema in the form of a ``StructType`` object that matches that data format.
        
                You can use the standard classifiers that AWS Glue supplies, or you can write your own classifiers to best categorize your data sources and specify the appropriate schemas to use for them. A classifier can be a ``grok`` classifier, an ``XML`` classifier, or a ``JSON`` classifier, as specified in one of the fields in the ``Classifier`` object.
        
                - **GrokClassifier** *(dict) --* 
        
                  A ``GrokClassifier`` object.
        
                  - **Name** *(string) --* 
        
                    The name of the classifier.
        
                  - **Classification** *(string) --* 
        
                    An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, and so on.
        
                  - **CreationTime** *(datetime) --* 
        
                    The time this classifier was registered.
        
                  - **LastUpdated** *(datetime) --* 
        
                    The time this classifier was last updated.
        
                  - **Version** *(integer) --* 
        
                    The version of this classifier.
        
                  - **GrokPattern** *(string) --* 
        
                    The grok pattern applied to a data store by this classifier. For more information, see built-in patterns in `Writing Custom Classifers <http://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html>`__ .
        
                  - **CustomPatterns** *(string) --* 
        
                    Optional custom grok patterns defined by this classifier. For more information, see custom patterns in `Writing Custom Classifers <http://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html>`__ .
        
                - **XMLClassifier** *(dict) --* 
        
                  An ``XMLClassifier`` object.
        
                  - **Name** *(string) --* 
        
                    The name of the classifier.
        
                  - **Classification** *(string) --* 
        
                    An identifier of the data format that the classifier matches.
        
                  - **CreationTime** *(datetime) --* 
        
                    The time this classifier was registered.
        
                  - **LastUpdated** *(datetime) --* 
        
                    The time this classifier was last updated.
        
                  - **Version** *(integer) --* 
        
                    The version of this classifier.
        
                  - **RowTag** *(string) --* 
        
                    The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot identify a self-closing element (closed by ``/>`` ). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, ``<row item_a=\"A\" item_b=\"B\"></row>`` is okay, but ``<row item_a=\"A\" item_b=\"B\" />`` is not).
        
                - **JsonClassifier** *(dict) --* 
        
                  A ``JsonClassifier`` object.
        
                  - **Name** *(string) --* 
        
                    The name of the classifier.
        
                  - **CreationTime** *(datetime) --* 
        
                    The time this classifier was registered.
        
                  - **LastUpdated** *(datetime) --* 
        
                    The time this classifier was last updated.
        
                  - **Version** *(integer) --* 
        
                    The version of this classifier.
        
                  - **JsonPath** *(string) --* 
        
                    A ``JsonPath`` string defining the JSON data for the classifier to classify. AWS Glue supports a subset of JsonPath, as described in `Writing JsonPath Custom Classifiers <https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json>`__ .
        
        """
        pass


class GetConnections(Paginator):
    def paginate(self, CatalogId: str = None, Filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetConnections>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CatalogId=\'string\',
              Filter={
                  \'MatchCriteria\': [
                      \'string\',
                  ],
                  \'ConnectionType\': \'JDBC\'|\'SFTP\'
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CatalogId: string
        :param CatalogId: 
        
          The ID of the Data Catalog in which the connections reside. If none is supplied, the AWS account ID is used by default.
        
        :type Filter: dict
        :param Filter: 
        
          A filter that controls which connections will be returned.
        
          - **MatchCriteria** *(list) --* 
        
            A criteria string that must match the criteria recorded in the connection definition for that connection definition to be returned.
        
            - *(string) --* 
        
          - **ConnectionType** *(string) --* 
        
            The type of connections to return. Currently, only JDBC is supported; SFTP is not supported.
        
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
                \'ConnectionList\': [
                    {
                        \'Name\': \'string\',
                        \'Description\': \'string\',
                        \'ConnectionType\': \'JDBC\'|\'SFTP\',
                        \'MatchCriteria\': [
                            \'string\',
                        ],
                        \'ConnectionProperties\': {
                            \'string\': \'string\'
                        },
                        \'PhysicalConnectionRequirements\': {
                            \'SubnetId\': \'string\',
                            \'SecurityGroupIdList\': [
                                \'string\',
                            ],
                            \'AvailabilityZone\': \'string\'
                        },
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'LastUpdatedTime\': datetime(2015, 1, 1),
                        \'LastUpdatedBy\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ConnectionList** *(list) --* 
        
              A list of requested connection definitions.
        
              - *(dict) --* 
        
                Defines a connection to a data source.
        
                - **Name** *(string) --* 
        
                  The name of the connection definition.
        
                - **Description** *(string) --* 
        
                  Description of the connection.
        
                - **ConnectionType** *(string) --* 
        
                  The type of the connection. Currently, only JDBC is supported; SFTP is not supported.
        
                - **MatchCriteria** *(list) --* 
        
                  A list of criteria that can be used in selecting this connection.
        
                  - *(string) --* 
              
                - **ConnectionProperties** *(dict) --* 
        
                  These key-value pairs define parameters for the connection:
        
                  * ``HOST`` - The host URI: either the fully qualified domain name (FQDN) or the IPv4 address of the database host. 
                   
                  * ``PORT`` - The port number, between 1024 and 65535, of the port on which the database host is listening for database connections. 
                   
                  * ``USER_NAME`` - The name under which to log in to the database. The value string for ``USER_NAME`` is \"``USERNAME`` \". 
                   
                  * ``PASSWORD`` - A password, if one is used, for the user name. 
                   
                  * ``JDBC_DRIVER_JAR_URI`` - The S3 path of the a jar file that contains the JDBC driver to use. 
                   
                  * ``JDBC_DRIVER_CLASS_NAME`` - The class name of the JDBC driver to use. 
                   
                  * ``JDBC_ENGINE`` - The name of the JDBC engine to use. 
                   
                  * ``JDBC_ENGINE_VERSION`` - The version of the JDBC engine to use. 
                   
                  * ``CONFIG_FILES`` - (Reserved for future use). 
                   
                  * ``INSTANCE_ID`` - The instance ID to use. 
                   
                  * ``JDBC_CONNECTION_URL`` - The URL for the JDBC connection. 
                   
                  * ``JDBC_ENFORCE_SSL`` - A Boolean string (true, false) specifying whether SSL with hostname matching will be enforced for the JDBC connection on the client. The default is false. 
                   
                  - *(string) --* 
                    
                    - *(string) --* 
              
                - **PhysicalConnectionRequirements** *(dict) --* 
        
                  A map of physical connection requirements, such as VPC and SecurityGroup, needed for making this connection successfully.
        
                  - **SubnetId** *(string) --* 
        
                    The subnet ID used by the connection.
        
                  - **SecurityGroupIdList** *(list) --* 
        
                    The security group ID list used by the connection.
        
                    - *(string) --* 
                
                  - **AvailabilityZone** *(string) --* 
        
                    The connection\'s availability zone. This field is redundant, since the specified subnet implies the availability zone to be used. The field must be populated now, but will be deprecated in the future.
        
                - **CreationTime** *(datetime) --* 
        
                  The time this connection definition was created.
        
                - **LastUpdatedTime** *(datetime) --* 
        
                  The last time this connection definition was updated.
        
                - **LastUpdatedBy** *(string) --* 
        
                  The user, group or role that last updated this connection definition.
        
        """
        pass


class GetCrawlerMetrics(Paginator):
    def paginate(self, CrawlerNameList: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetCrawlerMetrics>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CrawlerNameList=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CrawlerNameList: list
        :param CrawlerNameList: 
        
          A list of the names of crawlers about which to retrieve metrics.
        
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
                \'CrawlerMetricsList\': [
                    {
                        \'CrawlerName\': \'string\',
                        \'TimeLeftSeconds\': 123.0,
                        \'StillEstimating\': True|False,
                        \'LastRuntimeSeconds\': 123.0,
                        \'MedianRuntimeSeconds\': 123.0,
                        \'TablesCreated\': 123,
                        \'TablesUpdated\': 123,
                        \'TablesDeleted\': 123
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CrawlerMetricsList** *(list) --* 
        
              A list of metrics for the specified crawler.
        
              - *(dict) --* 
        
                Metrics for a specified crawler.
        
                - **CrawlerName** *(string) --* 
        
                  The name of the crawler.
        
                - **TimeLeftSeconds** *(float) --* 
        
                  The estimated time left to complete a running crawl.
        
                - **StillEstimating** *(boolean) --* 
        
                  True if the crawler is still estimating how long it will take to complete this run.
        
                - **LastRuntimeSeconds** *(float) --* 
        
                  The duration of the crawler\'s most recent run, in seconds.
        
                - **MedianRuntimeSeconds** *(float) --* 
        
                  The median duration of this crawler\'s runs, in seconds.
        
                - **TablesCreated** *(integer) --* 
        
                  The number of tables created by this crawler.
        
                - **TablesUpdated** *(integer) --* 
        
                  The number of tables updated by this crawler.
        
                - **TablesDeleted** *(integer) --* 
        
                  The number of tables deleted by this crawler.
        
        """
        pass


class GetCrawlers(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetCrawlers>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'Crawlers\': [
                    {
                        \'Name\': \'string\',
                        \'Role\': \'string\',
                        \'Targets\': {
                            \'S3Targets\': [
                                {
                                    \'Path\': \'string\',
                                    \'Exclusions\': [
                                        \'string\',
                                    ]
                                },
                            ],
                            \'JdbcTargets\': [
                                {
                                    \'ConnectionName\': \'string\',
                                    \'Path\': \'string\',
                                    \'Exclusions\': [
                                        \'string\',
                                    ]
                                },
                            ],
                            \'DynamoDBTargets\': [
                                {
                                    \'Path\': \'string\'
                                },
                            ]
                        },
                        \'DatabaseName\': \'string\',
                        \'Description\': \'string\',
                        \'Classifiers\': [
                            \'string\',
                        ],
                        \'SchemaChangePolicy\': {
                            \'UpdateBehavior\': \'LOG\'|\'UPDATE_IN_DATABASE\',
                            \'DeleteBehavior\': \'LOG\'|\'DELETE_FROM_DATABASE\'|\'DEPRECATE_IN_DATABASE\'
                        },
                        \'State\': \'READY\'|\'RUNNING\'|\'STOPPING\',
                        \'TablePrefix\': \'string\',
                        \'Schedule\': {
                            \'ScheduleExpression\': \'string\',
                            \'State\': \'SCHEDULED\'|\'NOT_SCHEDULED\'|\'TRANSITIONING\'
                        },
                        \'CrawlElapsedTime\': 123,
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'LastUpdated\': datetime(2015, 1, 1),
                        \'LastCrawl\': {
                            \'Status\': \'SUCCEEDED\'|\'CANCELLED\'|\'FAILED\',
                            \'ErrorMessage\': \'string\',
                            \'LogGroup\': \'string\',
                            \'LogStream\': \'string\',
                            \'MessagePrefix\': \'string\',
                            \'StartTime\': datetime(2015, 1, 1)
                        },
                        \'Version\': 123,
                        \'Configuration\': \'string\',
                        \'CrawlerSecurityConfiguration\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Crawlers** *(list) --* 
        
              A list of crawler metadata.
        
              - *(dict) --* 
        
                Specifies a crawler program that examines a data source and uses classifiers to try to determine its schema. If successful, the crawler records metadata concerning the data source in the AWS Glue Data Catalog.
        
                - **Name** *(string) --* 
        
                  The crawler name.
        
                - **Role** *(string) --* 
        
                  The IAM role (or ARN of an IAM role) used to access customer resources, such as data in Amazon S3.
        
                - **Targets** *(dict) --* 
        
                  A collection of targets to crawl.
        
                  - **S3Targets** *(list) --* 
        
                    Specifies Amazon S3 targets.
        
                    - *(dict) --* 
        
                      Specifies a data store in Amazon S3.
        
                      - **Path** *(string) --* 
        
                        The path to the Amazon S3 target.
        
                      - **Exclusions** *(list) --* 
        
                        A list of glob patterns used to exclude from the crawl. For more information, see `Catalog Tables with a Crawler <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .
        
                        - *(string) --* 
                    
                  - **JdbcTargets** *(list) --* 
        
                    Specifies JDBC targets.
        
                    - *(dict) --* 
        
                      Specifies a JDBC data store to crawl.
        
                      - **ConnectionName** *(string) --* 
        
                        The name of the connection to use to connect to the JDBC target.
        
                      - **Path** *(string) --* 
        
                        The path of the JDBC target.
        
                      - **Exclusions** *(list) --* 
        
                        A list of glob patterns used to exclude from the crawl. For more information, see `Catalog Tables with a Crawler <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .
        
                        - *(string) --* 
                    
                  - **DynamoDBTargets** *(list) --* 
        
                    Specifies DynamoDB targets.
        
                    - *(dict) --* 
        
                      Specifies a DynamoDB table to crawl.
        
                      - **Path** *(string) --* 
        
                        The name of the DynamoDB table to crawl.
        
                - **DatabaseName** *(string) --* 
        
                  The database where metadata is written by this crawler.
        
                - **Description** *(string) --* 
        
                  A description of the crawler.
        
                - **Classifiers** *(list) --* 
        
                  A list of custom classifiers associated with the crawler.
        
                  - *(string) --* 
              
                - **SchemaChangePolicy** *(dict) --* 
        
                  Sets the behavior when the crawler finds a changed or deleted object.
        
                  - **UpdateBehavior** *(string) --* 
        
                    The update behavior when the crawler finds a changed schema.
        
                  - **DeleteBehavior** *(string) --* 
        
                    The deletion behavior when the crawler finds a deleted object.
        
                - **State** *(string) --* 
        
                  Indicates whether the crawler is running, or whether a run is pending.
        
                - **TablePrefix** *(string) --* 
        
                  The prefix added to the names of tables that are created.
        
                - **Schedule** *(dict) --* 
        
                  For scheduled crawlers, the schedule when the crawler runs.
        
                  - **ScheduleExpression** *(string) --* 
        
                    A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for Jobs and Crawlers <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ . For example, to run something every day at 12:15 UTC, you would specify: ``cron(15 12 * * ? *)`` .
        
                  - **State** *(string) --* 
        
                    The state of the schedule.
        
                - **CrawlElapsedTime** *(integer) --* 
        
                  If the crawler is running, contains the total time elapsed since the last crawl began.
        
                - **CreationTime** *(datetime) --* 
        
                  The time when the crawler was created.
        
                - **LastUpdated** *(datetime) --* 
        
                  The time the crawler was last updated.
        
                - **LastCrawl** *(dict) --* 
        
                  The status of the last crawl, and potentially error information if an error occurred.
        
                  - **Status** *(string) --* 
        
                    Status of the last crawl.
        
                  - **ErrorMessage** *(string) --* 
        
                    If an error occurred, the error information about the last crawl.
        
                  - **LogGroup** *(string) --* 
        
                    The log group for the last crawl.
        
                  - **LogStream** *(string) --* 
        
                    The log stream for the last crawl.
        
                  - **MessagePrefix** *(string) --* 
        
                    The prefix for a message about this crawl.
        
                  - **StartTime** *(datetime) --* 
        
                    The time at which the crawl started.
        
                - **Version** *(integer) --* 
        
                  The version of the crawler.
        
                - **Configuration** *(string) --* 
        
                  Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler\'s behavior. For more information, see `Configuring a Crawler <http://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html>`__ .
        
                - **CrawlerSecurityConfiguration** *(string) --* 
        
                  The name of the SecurityConfiguration structure to be used by this Crawler.
        
        """
        pass


class GetDatabases(Paginator):
    def paginate(self, CatalogId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetDatabases>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CatalogId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CatalogId: string
        :param CatalogId: 
        
          The ID of the Data Catalog from which to retrieve ``Databases`` . If none is supplied, the AWS account ID is used by default.
        
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
                \'DatabaseList\': [
                    {
                        \'Name\': \'string\',
                        \'Description\': \'string\',
                        \'LocationUri\': \'string\',
                        \'Parameters\': {
                            \'string\': \'string\'
                        },
                        \'CreateTime\': datetime(2015, 1, 1)
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DatabaseList** *(list) --* 
        
              A list of ``Database`` objects from the specified catalog.
        
              - *(dict) --* 
        
                The ``Database`` object represents a logical grouping of tables that may reside in a Hive metastore or an RDBMS.
        
                - **Name** *(string) --* 
        
                  Name of the database. For Hive compatibility, this is folded to lowercase when it is stored.
        
                - **Description** *(string) --* 
        
                  Description of the database.
        
                - **LocationUri** *(string) --* 
        
                  The location of the database (for example, an HDFS path).
        
                - **Parameters** *(dict) --* 
        
                  These key-value pairs define parameters and properties of the database.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
                - **CreateTime** *(datetime) --* 
        
                  The time at which the metadata database was created in the catalog.
        
        """
        pass


class GetDevEndpoints(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetDevEndpoints>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'DevEndpoints\': [
                    {
                        \'EndpointName\': \'string\',
                        \'RoleArn\': \'string\',
                        \'SecurityGroupIds\': [
                            \'string\',
                        ],
                        \'SubnetId\': \'string\',
                        \'YarnEndpointAddress\': \'string\',
                        \'PrivateAddress\': \'string\',
                        \'ZeppelinRemoteSparkInterpreterPort\': 123,
                        \'PublicAddress\': \'string\',
                        \'Status\': \'string\',
                        \'NumberOfNodes\': 123,
                        \'AvailabilityZone\': \'string\',
                        \'VpcId\': \'string\',
                        \'ExtraPythonLibsS3Path\': \'string\',
                        \'ExtraJarsS3Path\': \'string\',
                        \'FailureReason\': \'string\',
                        \'LastUpdateStatus\': \'string\',
                        \'CreatedTimestamp\': datetime(2015, 1, 1),
                        \'LastModifiedTimestamp\': datetime(2015, 1, 1),
                        \'PublicKey\': \'string\',
                        \'PublicKeys\': [
                            \'string\',
                        ],
                        \'SecurityConfiguration\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DevEndpoints** *(list) --* 
        
              A list of DevEndpoint definitions.
        
              - *(dict) --* 
        
                A development endpoint where a developer can remotely debug ETL scripts.
        
                - **EndpointName** *(string) --* 
        
                  The name of the DevEndpoint.
        
                - **RoleArn** *(string) --* 
        
                  The AWS ARN of the IAM role used in this DevEndpoint.
        
                - **SecurityGroupIds** *(list) --* 
        
                  A list of security group identifiers used in this DevEndpoint.
        
                  - *(string) --* 
              
                - **SubnetId** *(string) --* 
        
                  The subnet ID for this DevEndpoint.
        
                - **YarnEndpointAddress** *(string) --* 
        
                  The YARN endpoint address used by this DevEndpoint.
        
                - **PrivateAddress** *(string) --* 
        
                  A private IP address to access the DevEndpoint within a VPC, if the DevEndpoint is created within one. The PrivateAddress field is present only when you create the DevEndpoint within your virtual private cloud (VPC).
        
                - **ZeppelinRemoteSparkInterpreterPort** *(integer) --* 
        
                  The Apache Zeppelin port for the remote Apache Spark interpreter.
        
                - **PublicAddress** *(string) --* 
        
                  The public IP address used by this DevEndpoint. The PublicAddress field is present only when you create a non-VPC (virtual private cloud) DevEndpoint.
        
                - **Status** *(string) --* 
        
                  The current status of this DevEndpoint.
        
                - **NumberOfNodes** *(integer) --* 
        
                  The number of AWS Glue Data Processing Units (DPUs) allocated to this DevEndpoint.
        
                - **AvailabilityZone** *(string) --* 
        
                  The AWS availability zone where this DevEndpoint is located.
        
                - **VpcId** *(string) --* 
        
                  The ID of the virtual private cloud (VPC) used by this DevEndpoint.
        
                - **ExtraPythonLibsS3Path** *(string) --* 
        
                  Path(s) to one or more Python libraries in an S3 bucket that should be loaded in your DevEndpoint. Multiple values must be complete paths separated by a comma.
        
                  Please note that only pure Python libraries can currently be used on a DevEndpoint. Libraries that rely on C extensions, such as the `pandas <http://pandas.pydata.org/>`__ Python data analysis library, are not yet supported.
        
                - **ExtraJarsS3Path** *(string) --* 
        
                  Path to one or more Java Jars in an S3 bucket that should be loaded in your DevEndpoint.
        
                  Please note that only pure Java/Scala libraries can currently be used on a DevEndpoint.
        
                - **FailureReason** *(string) --* 
        
                  The reason for a current failure in this DevEndpoint.
        
                - **LastUpdateStatus** *(string) --* 
        
                  The status of the last update.
        
                - **CreatedTimestamp** *(datetime) --* 
        
                  The point in time at which this DevEndpoint was created.
        
                - **LastModifiedTimestamp** *(datetime) --* 
        
                  The point in time at which this DevEndpoint was last modified.
        
                - **PublicKey** *(string) --* 
        
                  The public key to be used by this DevEndpoint for authentication. This attribute is provided for backward compatibility, as the recommended attribute to use is public keys.
        
                - **PublicKeys** *(list) --* 
        
                  A list of public keys to be used by the DevEndpoints for authentication. The use of this attribute is preferred over a single public key because the public keys allow you to have a different private key per client.
        
                  .. note::
        
                    If you previously created an endpoint with a public key, you must remove that key to be able to set a list of public keys: call the ``UpdateDevEndpoint`` API with the public key content in the ``deletePublicKeys`` attribute, and the list of new keys in the ``addPublicKeys`` attribute.
        
                  - *(string) --* 
              
                - **SecurityConfiguration** *(string) --* 
        
                  The name of the SecurityConfiguration structure to be used with this DevEndpoint.
        
        """
        pass


class GetJobRuns(Paginator):
    def paginate(self, JobName: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetJobRuns>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              JobName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type JobName: string
        :param JobName: **[REQUIRED]** 
        
          The name of the job definition for which to retrieve all job runs.
        
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
                \'JobRuns\': [
                    {
                        \'Id\': \'string\',
                        \'Attempt\': 123,
                        \'PreviousRunId\': \'string\',
                        \'TriggerName\': \'string\',
                        \'JobName\': \'string\',
                        \'StartedOn\': datetime(2015, 1, 1),
                        \'LastModifiedOn\': datetime(2015, 1, 1),
                        \'CompletedOn\': datetime(2015, 1, 1),
                        \'JobRunState\': \'STARTING\'|\'RUNNING\'|\'STOPPING\'|\'STOPPED\'|\'SUCCEEDED\'|\'FAILED\'|\'TIMEOUT\',
                        \'Arguments\': {
                            \'string\': \'string\'
                        },
                        \'ErrorMessage\': \'string\',
                        \'PredecessorRuns\': [
                            {
                                \'JobName\': \'string\',
                                \'RunId\': \'string\'
                            },
                        ],
                        \'AllocatedCapacity\': 123,
                        \'ExecutionTime\': 123,
                        \'Timeout\': 123,
                        \'NotificationProperty\': {
                            \'NotifyDelayAfter\': 123
                        },
                        \'SecurityConfiguration\': \'string\',
                        \'LogGroupName\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **JobRuns** *(list) --* 
        
              A list of job-run metatdata objects.
        
              - *(dict) --* 
        
                Contains information about a job run.
        
                - **Id** *(string) --* 
        
                  The ID of this job run.
        
                - **Attempt** *(integer) --* 
        
                  The number of the attempt to run this job.
        
                - **PreviousRunId** *(string) --* 
        
                  The ID of the previous run of this job. For example, the JobRunId specified in the StartJobRun action.
        
                - **TriggerName** *(string) --* 
        
                  The name of the trigger that started this job run.
        
                - **JobName** *(string) --* 
        
                  The name of the job definition being used in this run.
        
                - **StartedOn** *(datetime) --* 
        
                  The date and time at which this job run was started.
        
                - **LastModifiedOn** *(datetime) --* 
        
                  The last time this job run was modified.
        
                - **CompletedOn** *(datetime) --* 
        
                  The date and time this job run completed.
        
                - **JobRunState** *(string) --* 
        
                  The current state of the job run.
        
                - **Arguments** *(dict) --* 
        
                  The job arguments associated with this run. These override equivalent default arguments set for the job.
        
                  You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
        
                  For information about how to specify and consume your own job arguments, see the `Calling AWS Glue APIs in Python <http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__ topic in the developer guide.
        
                  For information about the key-value pairs that AWS Glue consumes to set up your job, see the `Special Parameters Used by AWS Glue <http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__ topic in the developer guide.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
                - **ErrorMessage** *(string) --* 
        
                  An error message associated with this job run.
        
                - **PredecessorRuns** *(list) --* 
        
                  A list of predecessors to this job run.
        
                  - *(dict) --* 
        
                    A job run that was used in the predicate of a conditional trigger that triggered this job run.
        
                    - **JobName** *(string) --* 
        
                      The name of the job definition used by the predecessor job run.
        
                    - **RunId** *(string) --* 
        
                      The job-run ID of the predecessor job run.
        
                - **AllocatedCapacity** *(integer) --* 
        
                  The number of AWS Glue data processing units (DPUs) allocated to this JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the `AWS Glue pricing page <https://aws.amazon.com/glue/pricing/>`__ .
        
                - **ExecutionTime** *(integer) --* 
        
                  The amount of time (in seconds) that the job run consumed resources.
        
                - **Timeout** *(integer) --* 
        
                  The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters ``TIMEOUT`` status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.
        
                - **NotificationProperty** *(dict) --* 
        
                  Specifies configuration properties of a job run notification.
        
                  - **NotifyDelayAfter** *(integer) --* 
        
                    After a job run starts, the number of minutes to wait before sending a job run delay notification.
        
                - **SecurityConfiguration** *(string) --* 
        
                  The name of the SecurityConfiguration structure to be used with this job run.
        
                - **LogGroupName** *(string) --* 
        
                  The name of the log group for secure logging, that can be server-side encrypted in CloudWatch using KMS. This name can be ``/aws-glue/jobs/`` , in which case the default encryption is ``NONE`` . If you add a role name and SecurityConfiguration name (in other words, ``/aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/`` ), then that security configuration will be used to encrypt the log group.
        
        """
        pass


class GetJobs(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetJobs>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'Jobs\': [
                    {
                        \'Name\': \'string\',
                        \'Description\': \'string\',
                        \'LogUri\': \'string\',
                        \'Role\': \'string\',
                        \'CreatedOn\': datetime(2015, 1, 1),
                        \'LastModifiedOn\': datetime(2015, 1, 1),
                        \'ExecutionProperty\': {
                            \'MaxConcurrentRuns\': 123
                        },
                        \'Command\': {
                            \'Name\': \'string\',
                            \'ScriptLocation\': \'string\'
                        },
                        \'DefaultArguments\': {
                            \'string\': \'string\'
                        },
                        \'Connections\': {
                            \'Connections\': [
                                \'string\',
                            ]
                        },
                        \'MaxRetries\': 123,
                        \'AllocatedCapacity\': 123,
                        \'Timeout\': 123,
                        \'NotificationProperty\': {
                            \'NotifyDelayAfter\': 123
                        },
                        \'SecurityConfiguration\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Jobs** *(list) --* 
        
              A list of job definitions.
        
              - *(dict) --* 
        
                Specifies a job definition.
        
                - **Name** *(string) --* 
        
                  The name you assign to this job definition.
        
                - **Description** *(string) --* 
        
                  Description of the job being defined.
        
                - **LogUri** *(string) --* 
        
                  This field is reserved for future use.
        
                - **Role** *(string) --* 
        
                  The name or ARN of the IAM role associated with this job.
        
                - **CreatedOn** *(datetime) --* 
        
                  The time and date that this job definition was created.
        
                - **LastModifiedOn** *(datetime) --* 
        
                  The last point in time when this job definition was modified.
        
                - **ExecutionProperty** *(dict) --* 
        
                  An ExecutionProperty specifying the maximum number of concurrent runs allowed for this job.
        
                  - **MaxConcurrentRuns** *(integer) --* 
        
                    The maximum number of concurrent runs allowed for the job. The default is 1. An error is returned when this threshold is reached. The maximum value you can specify is controlled by a service limit.
        
                - **Command** *(dict) --* 
        
                  The JobCommand that executes this job.
        
                  - **Name** *(string) --* 
        
                    The name of the job command: this must be ``glueetl`` .
        
                  - **ScriptLocation** *(string) --* 
        
                    Specifies the S3 path to a script that executes a job (required).
        
                - **DefaultArguments** *(dict) --* 
        
                  The default arguments for this job, specified as name-value pairs.
        
                  You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
        
                  For information about how to specify and consume your own Job arguments, see the `Calling AWS Glue APIs in Python <http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__ topic in the developer guide.
        
                  For information about the key-value pairs that AWS Glue consumes to set up your job, see the `Special Parameters Used by AWS Glue <http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__ topic in the developer guide.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
                - **Connections** *(dict) --* 
        
                  The connections used for this job.
        
                  - **Connections** *(list) --* 
        
                    A list of connections used by the job.
        
                    - *(string) --* 
                
                - **MaxRetries** *(integer) --* 
        
                  The maximum number of times to retry this job after a JobRun fails.
        
                - **AllocatedCapacity** *(integer) --* 
        
                  The number of AWS Glue data processing units (DPUs) allocated to runs of this job. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the `AWS Glue pricing page <https://aws.amazon.com/glue/pricing/>`__ .
        
                - **Timeout** *(integer) --* 
        
                  The job timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters ``TIMEOUT`` status. The default is 2,880 minutes (48 hours).
        
                - **NotificationProperty** *(dict) --* 
        
                  Specifies configuration properties of a job notification.
        
                  - **NotifyDelayAfter** *(integer) --* 
        
                    After a job run starts, the number of minutes to wait before sending a job run delay notification.
        
                - **SecurityConfiguration** *(string) --* 
        
                  The name of the SecurityConfiguration structure to be used with this job.
        
        """
        pass


class GetPartitions(Paginator):
    def paginate(self, DatabaseName: str, TableName: str, CatalogId: str = None, Expression: str = None, Segment: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetPartitions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CatalogId=\'string\',
              DatabaseName=\'string\',
              TableName=\'string\',
              Expression=\'string\',
              Segment={
                  \'SegmentNumber\': 123,
                  \'TotalSegments\': 123
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CatalogId: string
        :param CatalogId: 
        
          The ID of the Data Catalog where the partitions in question reside. If none is supplied, the AWS account ID is used by default.
        
        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]** 
        
          The name of the catalog database where the partitions reside.
        
        :type TableName: string
        :param TableName: **[REQUIRED]** 
        
          The name of the partitions\' table.
        
        :type Expression: string
        :param Expression: 
        
          An expression filtering the partitions to be returned.
        
          The expression uses SQL syntax similar to the SQL ``WHERE`` filter clause. The SQL statement parser `JSQLParser <http://jsqlparser.sourceforge.net/home.php>`__ parses the expression. 
        
           *Operators* : The following are the operators that you can use in the ``Expression`` API call:
        
            =  
        
          Checks if the values of the two operands are equal or not; if yes, then the condition becomes true.
        
          Example: Assume \'variable a\' holds 10 and \'variable b\' holds 20. 
        
          (a = b) is not true.
        
            < >  
        
          Checks if the values of two operands are equal or not; if the values are not equal, then the condition becomes true.
        
          Example: (a < > b) is true.
        
            >  
        
          Checks if the value of the left operand is greater than the value of the right operand; if yes, then the condition becomes true.
        
          Example: (a > b) is not true.
        
            <  
        
          Checks if the value of the left operand is less than the value of the right operand; if yes, then the condition becomes true.
        
          Example: (a < b) is true.
        
            >=  
        
          Checks if the value of the left operand is greater than or equal to the value of the right operand; if yes, then the condition becomes true.
        
          Example: (a >= b) is not true.
        
            <=  
        
          Checks if the value of the left operand is less than or equal to the value of the right operand; if yes, then the condition becomes true.
        
          Example: (a <= b) is true.
        
            AND, OR, IN, BETWEEN, LIKE, NOT, IS NULL  
        
          Logical operators.
        
           *Supported Partition Key Types* : The following are the the supported partition keys.
        
          * ``string``   
           
          * ``date``   
           
          * ``timestamp``   
           
          * ``int``   
           
          * ``bigint``   
           
          * ``long``   
           
          * ``tinyint``   
           
          * ``smallint``   
           
          * ``decimal``   
           
          If an invalid type is encountered, an exception is thrown. 
        
          The following list shows the valid operators on each type. When you define a crawler, the ``partitionKey`` type is created as a ``STRING`` , to be compatible with the catalog partitions. 
        
           *Sample API Call* : 
        
        :type Segment: dict
        :param Segment: 
        
          The segment of the table\'s partitions to scan in this request.
        
          - **SegmentNumber** *(integer) --* **[REQUIRED]** 
        
            The zero-based index number of the this segment. For example, if the total number of segments is 4, SegmentNumber values will range from zero through three.
        
          - **TotalSegments** *(integer) --* **[REQUIRED]** 
        
            The total numer of segments.
        
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
                \'Partitions\': [
                    {
                        \'Values\': [
                            \'string\',
                        ],
                        \'DatabaseName\': \'string\',
                        \'TableName\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'LastAccessTime\': datetime(2015, 1, 1),
                        \'StorageDescriptor\': {
                            \'Columns\': [
                                {
                                    \'Name\': \'string\',
                                    \'Type\': \'string\',
                                    \'Comment\': \'string\'
                                },
                            ],
                            \'Location\': \'string\',
                            \'InputFormat\': \'string\',
                            \'OutputFormat\': \'string\',
                            \'Compressed\': True|False,
                            \'NumberOfBuckets\': 123,
                            \'SerdeInfo\': {
                                \'Name\': \'string\',
                                \'SerializationLibrary\': \'string\',
                                \'Parameters\': {
                                    \'string\': \'string\'
                                }
                            },
                            \'BucketColumns\': [
                                \'string\',
                            ],
                            \'SortColumns\': [
                                {
                                    \'Column\': \'string\',
                                    \'SortOrder\': 123
                                },
                            ],
                            \'Parameters\': {
                                \'string\': \'string\'
                            },
                            \'SkewedInfo\': {
                                \'SkewedColumnNames\': [
                                    \'string\',
                                ],
                                \'SkewedColumnValues\': [
                                    \'string\',
                                ],
                                \'SkewedColumnValueLocationMaps\': {
                                    \'string\': \'string\'
                                }
                            },
                            \'StoredAsSubDirectories\': True|False
                        },
                        \'Parameters\': {
                            \'string\': \'string\'
                        },
                        \'LastAnalyzedTime\': datetime(2015, 1, 1)
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Partitions** *(list) --* 
        
              A list of requested partitions.
        
              - *(dict) --* 
        
                Represents a slice of table data.
        
                - **Values** *(list) --* 
        
                  The values of the partition.
        
                  - *(string) --* 
              
                - **DatabaseName** *(string) --* 
        
                  The name of the catalog database where the table in question is located.
        
                - **TableName** *(string) --* 
        
                  The name of the table in question.
        
                - **CreationTime** *(datetime) --* 
        
                  The time at which the partition was created.
        
                - **LastAccessTime** *(datetime) --* 
        
                  The last time at which the partition was accessed.
        
                - **StorageDescriptor** *(dict) --* 
        
                  Provides information about the physical location where the partition is stored.
        
                  - **Columns** *(list) --* 
        
                    A list of the ``Columns`` in the table.
        
                    - *(dict) --* 
        
                      A column in a ``Table`` .
        
                      - **Name** *(string) --* 
        
                        The name of the ``Column`` .
        
                      - **Type** *(string) --* 
        
                        The datatype of data in the ``Column`` .
        
                      - **Comment** *(string) --* 
        
                        Free-form text comment.
        
                  - **Location** *(string) --* 
        
                    The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
        
                  - **InputFormat** *(string) --* 
        
                    The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom format.
        
                  - **OutputFormat** *(string) --* 
        
                    The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` , or a custom format.
        
                  - **Compressed** *(boolean) --* 
        
                    True if the data in the table is compressed, or False if not.
        
                  - **NumberOfBuckets** *(integer) --* 
        
                    Must be specified if the table contains any dimension columns.
        
                  - **SerdeInfo** *(dict) --* 
        
                    Serialization/deserialization (SerDe) information.
        
                    - **Name** *(string) --* 
        
                      Name of the SerDe.
        
                    - **SerializationLibrary** *(string) --* 
        
                      Usually the class that implements the SerDe. An example is: ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .
        
                    - **Parameters** *(dict) --* 
        
                      These key-value pairs define initialization parameters for the SerDe.
        
                      - *(string) --* 
                        
                        - *(string) --* 
                  
                  - **BucketColumns** *(list) --* 
        
                    A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
        
                    - *(string) --* 
                
                  - **SortColumns** *(list) --* 
        
                    A list specifying the sort order of each bucket in the table.
        
                    - *(dict) --* 
        
                      Specifies the sort order of a sorted column.
        
                      - **Column** *(string) --* 
        
                        The name of the column.
        
                      - **SortOrder** *(integer) --* 
        
                        Indicates that the column is sorted in ascending order (``== 1`` ), or in descending order (``==0`` ).
        
                  - **Parameters** *(dict) --* 
        
                    User-supplied properties in key-value form.
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
                  - **SkewedInfo** *(dict) --* 
        
                    Information about values that appear very frequently in a column (skewed values).
        
                    - **SkewedColumnNames** *(list) --* 
        
                      A list of names of columns that contain skewed values.
        
                      - *(string) --* 
                  
                    - **SkewedColumnValues** *(list) --* 
        
                      A list of values that appear so frequently as to be considered skewed.
        
                      - *(string) --* 
                  
                    - **SkewedColumnValueLocationMaps** *(dict) --* 
        
                      A mapping of skewed values to the columns that contain them.
        
                      - *(string) --* 
                        
                        - *(string) --* 
                  
                  - **StoredAsSubDirectories** *(boolean) --* 
        
                    True if the table data is stored in subdirectories, or False if not.
        
                - **Parameters** *(dict) --* 
        
                  These key-value pairs define partition parameters.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
                - **LastAnalyzedTime** *(datetime) --* 
        
                  The last time at which column statistics were computed for this partition.
        
        """
        pass


class GetTableVersions(Paginator):
    def paginate(self, DatabaseName: str, TableName: str, CatalogId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetTableVersions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CatalogId=\'string\',
              DatabaseName=\'string\',
              TableName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CatalogId: string
        :param CatalogId: 
        
          The ID of the Data Catalog where the tables reside. If none is supplied, the AWS account ID is used by default.
        
        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]** 
        
          The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.
        
        :type TableName: string
        :param TableName: **[REQUIRED]** 
        
          The name of the table. For Hive compatibility, this name is entirely lowercase.
        
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
                \'TableVersions\': [
                    {
                        \'Table\': {
                            \'Name\': \'string\',
                            \'DatabaseName\': \'string\',
                            \'Description\': \'string\',
                            \'Owner\': \'string\',
                            \'CreateTime\': datetime(2015, 1, 1),
                            \'UpdateTime\': datetime(2015, 1, 1),
                            \'LastAccessTime\': datetime(2015, 1, 1),
                            \'LastAnalyzedTime\': datetime(2015, 1, 1),
                            \'Retention\': 123,
                            \'StorageDescriptor\': {
                                \'Columns\': [
                                    {
                                        \'Name\': \'string\',
                                        \'Type\': \'string\',
                                        \'Comment\': \'string\'
                                    },
                                ],
                                \'Location\': \'string\',
                                \'InputFormat\': \'string\',
                                \'OutputFormat\': \'string\',
                                \'Compressed\': True|False,
                                \'NumberOfBuckets\': 123,
                                \'SerdeInfo\': {
                                    \'Name\': \'string\',
                                    \'SerializationLibrary\': \'string\',
                                    \'Parameters\': {
                                        \'string\': \'string\'
                                    }
                                },
                                \'BucketColumns\': [
                                    \'string\',
                                ],
                                \'SortColumns\': [
                                    {
                                        \'Column\': \'string\',
                                        \'SortOrder\': 123
                                    },
                                ],
                                \'Parameters\': {
                                    \'string\': \'string\'
                                },
                                \'SkewedInfo\': {
                                    \'SkewedColumnNames\': [
                                        \'string\',
                                    ],
                                    \'SkewedColumnValues\': [
                                        \'string\',
                                    ],
                                    \'SkewedColumnValueLocationMaps\': {
                                        \'string\': \'string\'
                                    }
                                },
                                \'StoredAsSubDirectories\': True|False
                            },
                            \'PartitionKeys\': [
                                {
                                    \'Name\': \'string\',
                                    \'Type\': \'string\',
                                    \'Comment\': \'string\'
                                },
                            ],
                            \'ViewOriginalText\': \'string\',
                            \'ViewExpandedText\': \'string\',
                            \'TableType\': \'string\',
                            \'Parameters\': {
                                \'string\': \'string\'
                            },
                            \'CreatedBy\': \'string\'
                        },
                        \'VersionId\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TableVersions** *(list) --* 
        
              A list of strings identifying available versions of the specified table.
        
              - *(dict) --* 
        
                Specifies a version of a table.
        
                - **Table** *(dict) --* 
        
                  The table in question
        
                  - **Name** *(string) --* 
        
                    Name of the table. For Hive compatibility, this must be entirely lowercase.
        
                  - **DatabaseName** *(string) --* 
        
                    Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
        
                  - **Description** *(string) --* 
        
                    Description of the table.
        
                  - **Owner** *(string) --* 
        
                    Owner of the table.
        
                  - **CreateTime** *(datetime) --* 
        
                    Time when the table definition was created in the Data Catalog.
        
                  - **UpdateTime** *(datetime) --* 
        
                    Last time the table was updated.
        
                  - **LastAccessTime** *(datetime) --* 
        
                    Last time the table was accessed. This is usually taken from HDFS, and may not be reliable.
        
                  - **LastAnalyzedTime** *(datetime) --* 
        
                    Last time column statistics were computed for this table.
        
                  - **Retention** *(integer) --* 
        
                    Retention time for this table.
        
                  - **StorageDescriptor** *(dict) --* 
        
                    A storage descriptor containing information about the physical storage of this table.
        
                    - **Columns** *(list) --* 
        
                      A list of the ``Columns`` in the table.
        
                      - *(dict) --* 
        
                        A column in a ``Table`` .
        
                        - **Name** *(string) --* 
        
                          The name of the ``Column`` .
        
                        - **Type** *(string) --* 
        
                          The datatype of data in the ``Column`` .
        
                        - **Comment** *(string) --* 
        
                          Free-form text comment.
        
                    - **Location** *(string) --* 
        
                      The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
        
                    - **InputFormat** *(string) --* 
        
                      The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom format.
        
                    - **OutputFormat** *(string) --* 
        
                      The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` , or a custom format.
        
                    - **Compressed** *(boolean) --* 
        
                      True if the data in the table is compressed, or False if not.
        
                    - **NumberOfBuckets** *(integer) --* 
        
                      Must be specified if the table contains any dimension columns.
        
                    - **SerdeInfo** *(dict) --* 
        
                      Serialization/deserialization (SerDe) information.
        
                      - **Name** *(string) --* 
        
                        Name of the SerDe.
        
                      - **SerializationLibrary** *(string) --* 
        
                        Usually the class that implements the SerDe. An example is: ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .
        
                      - **Parameters** *(dict) --* 
        
                        These key-value pairs define initialization parameters for the SerDe.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                    - **BucketColumns** *(list) --* 
        
                      A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
        
                      - *(string) --* 
                  
                    - **SortColumns** *(list) --* 
        
                      A list specifying the sort order of each bucket in the table.
        
                      - *(dict) --* 
        
                        Specifies the sort order of a sorted column.
        
                        - **Column** *(string) --* 
        
                          The name of the column.
        
                        - **SortOrder** *(integer) --* 
        
                          Indicates that the column is sorted in ascending order (``== 1`` ), or in descending order (``==0`` ).
        
                    - **Parameters** *(dict) --* 
        
                      User-supplied properties in key-value form.
        
                      - *(string) --* 
                        
                        - *(string) --* 
                  
                    - **SkewedInfo** *(dict) --* 
        
                      Information about values that appear very frequently in a column (skewed values).
        
                      - **SkewedColumnNames** *(list) --* 
        
                        A list of names of columns that contain skewed values.
        
                        - *(string) --* 
                    
                      - **SkewedColumnValues** *(list) --* 
        
                        A list of values that appear so frequently as to be considered skewed.
        
                        - *(string) --* 
                    
                      - **SkewedColumnValueLocationMaps** *(dict) --* 
        
                        A mapping of skewed values to the columns that contain them.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                    - **StoredAsSubDirectories** *(boolean) --* 
        
                      True if the table data is stored in subdirectories, or False if not.
        
                  - **PartitionKeys** *(list) --* 
        
                    A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
        
                    - *(dict) --* 
        
                      A column in a ``Table`` .
        
                      - **Name** *(string) --* 
        
                        The name of the ``Column`` .
        
                      - **Type** *(string) --* 
        
                        The datatype of data in the ``Column`` .
        
                      - **Comment** *(string) --* 
        
                        Free-form text comment.
        
                  - **ViewOriginalText** *(string) --* 
        
                    If the table is a view, the original text of the view; otherwise ``null`` .
        
                  - **ViewExpandedText** *(string) --* 
        
                    If the table is a view, the expanded text of the view; otherwise ``null`` .
        
                  - **TableType** *(string) --* 
        
                    The type of this table (``EXTERNAL_TABLE`` , ``VIRTUAL_VIEW`` , etc.).
        
                  - **Parameters** *(dict) --* 
        
                    These key-value pairs define properties associated with the table.
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
                  - **CreatedBy** *(string) --* 
        
                    Person or entity who created the table.
        
                - **VersionId** *(string) --* 
        
                  The ID value that identifies this table version. A ``VersionId`` is a string representation of an integer. Each version is incremented by 1.
        
        """
        pass


class GetTables(Paginator):
    def paginate(self, DatabaseName: str, CatalogId: str = None, Expression: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetTables>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CatalogId=\'string\',
              DatabaseName=\'string\',
              Expression=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CatalogId: string
        :param CatalogId: 
        
          The ID of the Data Catalog where the tables reside. If none is supplied, the AWS account ID is used by default.
        
        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]** 
        
          The database in the catalog whose tables to list. For Hive compatibility, this name is entirely lowercase.
        
        :type Expression: string
        :param Expression: 
        
          A regular expression pattern. If present, only those tables whose names match the pattern are returned.
        
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
                \'TableList\': [
                    {
                        \'Name\': \'string\',
                        \'DatabaseName\': \'string\',
                        \'Description\': \'string\',
                        \'Owner\': \'string\',
                        \'CreateTime\': datetime(2015, 1, 1),
                        \'UpdateTime\': datetime(2015, 1, 1),
                        \'LastAccessTime\': datetime(2015, 1, 1),
                        \'LastAnalyzedTime\': datetime(2015, 1, 1),
                        \'Retention\': 123,
                        \'StorageDescriptor\': {
                            \'Columns\': [
                                {
                                    \'Name\': \'string\',
                                    \'Type\': \'string\',
                                    \'Comment\': \'string\'
                                },
                            ],
                            \'Location\': \'string\',
                            \'InputFormat\': \'string\',
                            \'OutputFormat\': \'string\',
                            \'Compressed\': True|False,
                            \'NumberOfBuckets\': 123,
                            \'SerdeInfo\': {
                                \'Name\': \'string\',
                                \'SerializationLibrary\': \'string\',
                                \'Parameters\': {
                                    \'string\': \'string\'
                                }
                            },
                            \'BucketColumns\': [
                                \'string\',
                            ],
                            \'SortColumns\': [
                                {
                                    \'Column\': \'string\',
                                    \'SortOrder\': 123
                                },
                            ],
                            \'Parameters\': {
                                \'string\': \'string\'
                            },
                            \'SkewedInfo\': {
                                \'SkewedColumnNames\': [
                                    \'string\',
                                ],
                                \'SkewedColumnValues\': [
                                    \'string\',
                                ],
                                \'SkewedColumnValueLocationMaps\': {
                                    \'string\': \'string\'
                                }
                            },
                            \'StoredAsSubDirectories\': True|False
                        },
                        \'PartitionKeys\': [
                            {
                                \'Name\': \'string\',
                                \'Type\': \'string\',
                                \'Comment\': \'string\'
                            },
                        ],
                        \'ViewOriginalText\': \'string\',
                        \'ViewExpandedText\': \'string\',
                        \'TableType\': \'string\',
                        \'Parameters\': {
                            \'string\': \'string\'
                        },
                        \'CreatedBy\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TableList** *(list) --* 
        
              A list of the requested ``Table`` objects.
        
              - *(dict) --* 
        
                Represents a collection of related data organized in columns and rows.
        
                - **Name** *(string) --* 
        
                  Name of the table. For Hive compatibility, this must be entirely lowercase.
        
                - **DatabaseName** *(string) --* 
        
                  Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
        
                - **Description** *(string) --* 
        
                  Description of the table.
        
                - **Owner** *(string) --* 
        
                  Owner of the table.
        
                - **CreateTime** *(datetime) --* 
        
                  Time when the table definition was created in the Data Catalog.
        
                - **UpdateTime** *(datetime) --* 
        
                  Last time the table was updated.
        
                - **LastAccessTime** *(datetime) --* 
        
                  Last time the table was accessed. This is usually taken from HDFS, and may not be reliable.
        
                - **LastAnalyzedTime** *(datetime) --* 
        
                  Last time column statistics were computed for this table.
        
                - **Retention** *(integer) --* 
        
                  Retention time for this table.
        
                - **StorageDescriptor** *(dict) --* 
        
                  A storage descriptor containing information about the physical storage of this table.
        
                  - **Columns** *(list) --* 
        
                    A list of the ``Columns`` in the table.
        
                    - *(dict) --* 
        
                      A column in a ``Table`` .
        
                      - **Name** *(string) --* 
        
                        The name of the ``Column`` .
        
                      - **Type** *(string) --* 
        
                        The datatype of data in the ``Column`` .
        
                      - **Comment** *(string) --* 
        
                        Free-form text comment.
        
                  - **Location** *(string) --* 
        
                    The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
        
                  - **InputFormat** *(string) --* 
        
                    The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom format.
        
                  - **OutputFormat** *(string) --* 
        
                    The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` , or a custom format.
        
                  - **Compressed** *(boolean) --* 
        
                    True if the data in the table is compressed, or False if not.
        
                  - **NumberOfBuckets** *(integer) --* 
        
                    Must be specified if the table contains any dimension columns.
        
                  - **SerdeInfo** *(dict) --* 
        
                    Serialization/deserialization (SerDe) information.
        
                    - **Name** *(string) --* 
        
                      Name of the SerDe.
        
                    - **SerializationLibrary** *(string) --* 
        
                      Usually the class that implements the SerDe. An example is: ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .
        
                    - **Parameters** *(dict) --* 
        
                      These key-value pairs define initialization parameters for the SerDe.
        
                      - *(string) --* 
                        
                        - *(string) --* 
                  
                  - **BucketColumns** *(list) --* 
        
                    A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
        
                    - *(string) --* 
                
                  - **SortColumns** *(list) --* 
        
                    A list specifying the sort order of each bucket in the table.
        
                    - *(dict) --* 
        
                      Specifies the sort order of a sorted column.
        
                      - **Column** *(string) --* 
        
                        The name of the column.
        
                      - **SortOrder** *(integer) --* 
        
                        Indicates that the column is sorted in ascending order (``== 1`` ), or in descending order (``==0`` ).
        
                  - **Parameters** *(dict) --* 
        
                    User-supplied properties in key-value form.
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
                  - **SkewedInfo** *(dict) --* 
        
                    Information about values that appear very frequently in a column (skewed values).
        
                    - **SkewedColumnNames** *(list) --* 
        
                      A list of names of columns that contain skewed values.
        
                      - *(string) --* 
                  
                    - **SkewedColumnValues** *(list) --* 
        
                      A list of values that appear so frequently as to be considered skewed.
        
                      - *(string) --* 
                  
                    - **SkewedColumnValueLocationMaps** *(dict) --* 
        
                      A mapping of skewed values to the columns that contain them.
        
                      - *(string) --* 
                        
                        - *(string) --* 
                  
                  - **StoredAsSubDirectories** *(boolean) --* 
        
                    True if the table data is stored in subdirectories, or False if not.
        
                - **PartitionKeys** *(list) --* 
        
                  A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
        
                  - *(dict) --* 
        
                    A column in a ``Table`` .
        
                    - **Name** *(string) --* 
        
                      The name of the ``Column`` .
        
                    - **Type** *(string) --* 
        
                      The datatype of data in the ``Column`` .
        
                    - **Comment** *(string) --* 
        
                      Free-form text comment.
        
                - **ViewOriginalText** *(string) --* 
        
                  If the table is a view, the original text of the view; otherwise ``null`` .
        
                - **ViewExpandedText** *(string) --* 
        
                  If the table is a view, the expanded text of the view; otherwise ``null`` .
        
                - **TableType** *(string) --* 
        
                  The type of this table (``EXTERNAL_TABLE`` , ``VIRTUAL_VIEW`` , etc.).
        
                - **Parameters** *(dict) --* 
        
                  These key-value pairs define properties associated with the table.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
                - **CreatedBy** *(string) --* 
        
                  Person or entity who created the table.
        
        """
        pass


class GetTriggers(Paginator):
    def paginate(self, DependentJobName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetTriggers>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DependentJobName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type DependentJobName: string
        :param DependentJobName: 
        
          The name of the job for which to retrieve triggers. The trigger that can start this job will be returned, and if there is no such trigger, all triggers will be returned.
        
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
                \'Triggers\': [
                    {
                        \'Name\': \'string\',
                        \'Id\': \'string\',
                        \'Type\': \'SCHEDULED\'|\'CONDITIONAL\'|\'ON_DEMAND\',
                        \'State\': \'CREATING\'|\'CREATED\'|\'ACTIVATING\'|\'ACTIVATED\'|\'DEACTIVATING\'|\'DEACTIVATED\'|\'DELETING\'|\'UPDATING\',
                        \'Description\': \'string\',
                        \'Schedule\': \'string\',
                        \'Actions\': [
                            {
                                \'JobName\': \'string\',
                                \'Arguments\': {
                                    \'string\': \'string\'
                                },
                                \'Timeout\': 123,
                                \'NotificationProperty\': {
                                    \'NotifyDelayAfter\': 123
                                },
                                \'SecurityConfiguration\': \'string\'
                            },
                        ],
                        \'Predicate\': {
                            \'Logical\': \'AND\'|\'ANY\',
                            \'Conditions\': [
                                {
                                    \'LogicalOperator\': \'EQUALS\',
                                    \'JobName\': \'string\',
                                    \'State\': \'STARTING\'|\'RUNNING\'|\'STOPPING\'|\'STOPPED\'|\'SUCCEEDED\'|\'FAILED\'|\'TIMEOUT\'
                                },
                            ]
                        }
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Triggers** *(list) --* 
        
              A list of triggers for the specified job.
        
              - *(dict) --* 
        
                Information about a specific trigger.
        
                - **Name** *(string) --* 
        
                  Name of the trigger.
        
                - **Id** *(string) --* 
        
                  Reserved for future use.
        
                - **Type** *(string) --* 
        
                  The type of trigger that this is.
        
                - **State** *(string) --* 
        
                  The current state of the trigger.
        
                - **Description** *(string) --* 
        
                  A description of this trigger.
        
                - **Schedule** *(string) --* 
        
                  A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for Jobs and Crawlers <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__ . For example, to run something every day at 12:15 UTC, you would specify: ``cron(15 12 * * ? *)`` .
        
                - **Actions** *(list) --* 
        
                  The actions initiated by this trigger.
        
                  - *(dict) --* 
        
                    Defines an action to be initiated by a trigger.
        
                    - **JobName** *(string) --* 
        
                      The name of a job to be executed.
        
                    - **Arguments** *(dict) --* 
        
                      Arguments to be passed to the job run.
        
                      You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
        
                      For information about how to specify and consume your own Job arguments, see the `Calling AWS Glue APIs in Python <http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__ topic in the developer guide.
        
                      For information about the key-value pairs that AWS Glue consumes to set up your job, see the `Special Parameters Used by AWS Glue <http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__ topic in the developer guide.
        
                      - *(string) --* 
                        
                        - *(string) --* 
                  
                    - **Timeout** *(integer) --* 
        
                      The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters ``TIMEOUT`` status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.
        
                    - **NotificationProperty** *(dict) --* 
        
                      Specifies configuration properties of a job run notification.
        
                      - **NotifyDelayAfter** *(integer) --* 
        
                        After a job run starts, the number of minutes to wait before sending a job run delay notification.
        
                    - **SecurityConfiguration** *(string) --* 
        
                      The name of the SecurityConfiguration structure to be used with this action.
        
                - **Predicate** *(dict) --* 
        
                  The predicate of this trigger, which defines when it will fire.
        
                  - **Logical** *(string) --* 
        
                    Optional field if only one condition is listed. If multiple conditions are listed, then this field is required.
        
                  - **Conditions** *(list) --* 
        
                    A list of the conditions that determine when the trigger will fire.
        
                    - *(dict) --* 
        
                      Defines a condition under which a trigger fires.
        
                      - **LogicalOperator** *(string) --* 
        
                        A logical operator.
        
                      - **JobName** *(string) --* 
        
                        The name of the Job to whose JobRuns this condition applies and on which this trigger waits.
        
                      - **State** *(string) --* 
        
                        The condition state. Currently, the values supported are SUCCEEDED, STOPPED, TIMEOUT and FAILED.
        
        """
        pass


class GetUserDefinedFunctions(Paginator):
    def paginate(self, DatabaseName: str, Pattern: str, CatalogId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetUserDefinedFunctions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CatalogId=\'string\',
              DatabaseName=\'string\',
              Pattern=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CatalogId: string
        :param CatalogId: 
        
          The ID of the Data Catalog where the functions to be retrieved are located. If none is supplied, the AWS account ID is used by default.
        
        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]** 
        
          The name of the catalog database where the functions are located.
        
        :type Pattern: string
        :param Pattern: **[REQUIRED]** 
        
          An optional function-name pattern string that filters the function definitions returned.
        
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
                \'UserDefinedFunctions\': [
                    {
                        \'FunctionName\': \'string\',
                        \'ClassName\': \'string\',
                        \'OwnerName\': \'string\',
                        \'OwnerType\': \'USER\'|\'ROLE\'|\'GROUP\',
                        \'CreateTime\': datetime(2015, 1, 1),
                        \'ResourceUris\': [
                            {
                                \'ResourceType\': \'JAR\'|\'FILE\'|\'ARCHIVE\',
                                \'Uri\': \'string\'
                            },
                        ]
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **UserDefinedFunctions** *(list) --* 
        
              A list of requested function definitions.
        
              - *(dict) --* 
        
                Represents the equivalent of a Hive user-defined function (``UDF`` ) definition.
        
                - **FunctionName** *(string) --* 
        
                  The name of the function.
        
                - **ClassName** *(string) --* 
        
                  The Java class that contains the function code.
        
                - **OwnerName** *(string) --* 
        
                  The owner of the function.
        
                - **OwnerType** *(string) --* 
        
                  The owner type.
        
                - **CreateTime** *(datetime) --* 
        
                  The time at which the function was created.
        
                - **ResourceUris** *(list) --* 
        
                  The resource URIs for the function.
        
                  - *(dict) --* 
        
                    URIs for function resources.
        
                    - **ResourceType** *(string) --* 
        
                      The type of the resource.
        
                    - **Uri** *(string) --* 
        
                      The URI for accessing the resource.
        
        """
        pass
