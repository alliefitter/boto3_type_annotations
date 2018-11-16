from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeCertificates(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeCertificates>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: list
        :param Filters: 
        
          Filters applied to the certificate described in the form of key-value pairs.
        
          - *(dict) --* 
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The filter value.
        
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
                \'Certificates\': [
                    {
                        \'CertificateIdentifier\': \'string\',
                        \'CertificateCreationDate\': datetime(2015, 1, 1),
                        \'CertificatePem\': \'string\',
                        \'CertificateWallet\': b\'bytes\',
                        \'CertificateArn\': \'string\',
                        \'CertificateOwner\': \'string\',
                        \'ValidFromDate\': datetime(2015, 1, 1),
                        \'ValidToDate\': datetime(2015, 1, 1),
                        \'SigningAlgorithm\': \'string\',
                        \'KeyLength\': 123
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Certificates** *(list) --* 
        
              The Secure Sockets Layer (SSL) certificates associated with the replication instance.
        
              - *(dict) --* 
        
                The SSL certificate that can be used to encrypt connections between the endpoints and the replication instance.
        
                - **CertificateIdentifier** *(string) --* 
        
                  The customer-assigned name of the certificate. Valid characters are A-z and 0-9.
        
                - **CertificateCreationDate** *(datetime) --* 
        
                  The date that the certificate was created.
        
                - **CertificatePem** *(string) --* 
        
                  The contents of the .pem X.509 certificate file for the certificate.
        
                - **CertificateWallet** *(bytes) --* 
        
                  The location of the imported Oracle Wallet certificate for use with SSL.
        
                - **CertificateArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) for the certificate.
        
                - **CertificateOwner** *(string) --* 
        
                  The owner of the certificate.
        
                - **ValidFromDate** *(datetime) --* 
        
                  The beginning date that the certificate is valid.
        
                - **ValidToDate** *(datetime) --* 
        
                  The final date that the certificate is valid.
        
                - **SigningAlgorithm** *(string) --* 
        
                  The signing algorithm for the certificate.
        
                - **KeyLength** *(integer) --* 
        
                  The key length of the cryptographic algorithm being used.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeConnections(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeConnections>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: list
        :param Filters: 
        
          The filters applied to the connection.
        
          Valid filter names: endpoint-arn | replication-instance-arn
        
          - *(dict) --* 
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The filter value.
        
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
                \'Connections\': [
                    {
                        \'ReplicationInstanceArn\': \'string\',
                        \'EndpointArn\': \'string\',
                        \'Status\': \'string\',
                        \'LastFailureMessage\': \'string\',
                        \'EndpointIdentifier\': \'string\',
                        \'ReplicationInstanceIdentifier\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Connections** *(list) --* 
        
              A description of the connections.
        
              - *(dict) --* 
        
                - **ReplicationInstanceArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the replication instance.
        
                - **EndpointArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
        
                - **Status** *(string) --* 
        
                  The connection status.
        
                - **LastFailureMessage** *(string) --* 
        
                  The error message when the connection last failed.
        
                - **EndpointIdentifier** *(string) --* 
        
                  The identifier of the endpoint. Identifiers must begin with a letter; must contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two consecutive hyphens.
        
                - **ReplicationInstanceIdentifier** *(string) --* 
        
                  The replication instance identifier. This parameter is stored as a lowercase string.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeEndpointTypes(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeEndpointTypes>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: list
        :param Filters: 
        
          Filters applied to the describe action.
        
          Valid filter names: engine-name | endpoint-type
        
          - *(dict) --* 
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The filter value.
        
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
                \'SupportedEndpointTypes\': [
                    {
                        \'EngineName\': \'string\',
                        \'SupportsCDC\': True|False,
                        \'EndpointType\': \'source\'|\'target\',
                        \'EngineDisplayName\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **SupportedEndpointTypes** *(list) --* 
        
              The type of endpoints that are supported.
        
              - *(dict) --* 
        
                - **EngineName** *(string) --* 
        
                  The database engine name. Valid values, depending on the EndPointType, include mysql, oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase, sybase, dynamodb, mongodb, and sqlserver.
        
                - **SupportsCDC** *(boolean) --* 
        
                  Indicates if Change Data Capture (CDC) is supported.
        
                - **EndpointType** *(string) --* 
        
                  The type of endpoint.
        
                - **EngineDisplayName** *(string) --* 
        
                  The expanded name for the engine name. For example, if the ``EngineName`` parameter is \"aurora,\" this value would be \"Amazon Aurora MySQL.\"
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeEndpoints(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeEndpoints>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: list
        :param Filters: 
        
          Filters applied to the describe action.
        
          Valid filter names: endpoint-arn | endpoint-type | endpoint-id | engine-name
        
          - *(dict) --* 
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The filter value.
        
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
                \'Endpoints\': [
                    {
                        \'EndpointIdentifier\': \'string\',
                        \'EndpointType\': \'source\'|\'target\',
                        \'EngineName\': \'string\',
                        \'EngineDisplayName\': \'string\',
                        \'Username\': \'string\',
                        \'ServerName\': \'string\',
                        \'Port\': 123,
                        \'DatabaseName\': \'string\',
                        \'ExtraConnectionAttributes\': \'string\',
                        \'Status\': \'string\',
                        \'KmsKeyId\': \'string\',
                        \'EndpointArn\': \'string\',
                        \'CertificateArn\': \'string\',
                        \'SslMode\': \'none\'|\'require\'|\'verify-ca\'|\'verify-full\',
                        \'ServiceAccessRoleArn\': \'string\',
                        \'ExternalTableDefinition\': \'string\',
                        \'ExternalId\': \'string\',
                        \'DynamoDbSettings\': {
                            \'ServiceAccessRoleArn\': \'string\'
                        },
                        \'S3Settings\': {
                            \'ServiceAccessRoleArn\': \'string\',
                            \'ExternalTableDefinition\': \'string\',
                            \'CsvRowDelimiter\': \'string\',
                            \'CsvDelimiter\': \'string\',
                            \'BucketFolder\': \'string\',
                            \'BucketName\': \'string\',
                            \'CompressionType\': \'none\'|\'gzip\'
                        },
                        \'DmsTransferSettings\': {
                            \'ServiceAccessRoleArn\': \'string\',
                            \'BucketName\': \'string\'
                        },
                        \'MongoDbSettings\': {
                            \'Username\': \'string\',
                            \'Password\': \'string\',
                            \'ServerName\': \'string\',
                            \'Port\': 123,
                            \'DatabaseName\': \'string\',
                            \'AuthType\': \'no\'|\'password\',
                            \'AuthMechanism\': \'default\'|\'mongodb_cr\'|\'scram_sha_1\',
                            \'NestingLevel\': \'none\'|\'one\',
                            \'ExtractDocId\': \'string\',
                            \'DocsToInvestigate\': \'string\',
                            \'AuthSource\': \'string\',
                            \'KmsKeyId\': \'string\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Endpoints** *(list) --* 
        
              Endpoint description.
        
              - *(dict) --* 
        
                - **EndpointIdentifier** *(string) --* 
        
                  The database endpoint identifier. Identifiers must begin with a letter; must contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two consecutive hyphens.
        
                - **EndpointType** *(string) --* 
        
                  The type of endpoint.
        
                - **EngineName** *(string) --* 
        
                  The database engine name. Valid values, depending on the EndPointType, include mysql, oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase, sybase, dynamodb, mongodb, and sqlserver.
        
                - **EngineDisplayName** *(string) --* 
        
                  The expanded name for the engine name. For example, if the ``EngineName`` parameter is \"aurora,\" this value would be \"Amazon Aurora MySQL.\"
        
                - **Username** *(string) --* 
        
                  The user name used to connect to the endpoint.
        
                - **ServerName** *(string) --* 
        
                  The name of the server at the endpoint.
        
                - **Port** *(integer) --* 
        
                  The port value used to access the endpoint.
        
                - **DatabaseName** *(string) --* 
        
                  The name of the database at the endpoint.
        
                - **ExtraConnectionAttributes** *(string) --* 
        
                  Additional connection attributes used to connect to the endpoint.
        
                - **Status** *(string) --* 
        
                  The status of the endpoint.
        
                - **KmsKeyId** *(string) --* 
        
                  The KMS key identifier that will be used to encrypt the connection parameters. If you do not specify a value for the KmsKeyId parameter, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
        
                - **EndpointArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
        
                - **CertificateArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) used for SSL connection to the endpoint.
        
                - **SslMode** *(string) --* 
        
                  The SSL mode used to connect to the endpoint.
        
                  SSL mode can be one of four values: none, require, verify-ca, verify-full. 
        
                  The default value is none.
        
                - **ServiceAccessRoleArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) used by the service access IAM role.
        
                - **ExternalTableDefinition** *(string) --* 
        
                  The external table definition.
        
                - **ExternalId** *(string) --* 
        
                  Value returned by a call to CreateEndpoint that can be used for cross-account validation. Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account. 
        
                - **DynamoDbSettings** *(dict) --* 
        
                  The settings for the target DynamoDB database. For more information, see the ``DynamoDBSettings`` structure.
        
                  - **ServiceAccessRoleArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) used by the service access IAM role. 
        
                - **S3Settings** *(dict) --* 
        
                  The settings for the S3 target endpoint. For more information, see the ``S3Settings`` structure.
        
                  - **ServiceAccessRoleArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) used by the service access IAM role. 
        
                  - **ExternalTableDefinition** *(string) --* 
        
                    The external table definition. 
        
                  - **CsvRowDelimiter** *(string) --* 
        
                    The delimiter used to separate rows in the source files. The default is a carriage return (\n). 
        
                  - **CsvDelimiter** *(string) --* 
        
                    The delimiter used to separate columns in the source files. The default is a comma. 
        
                  - **BucketFolder** *(string) --* 
        
                    An optional parameter to set a folder name in the S3 bucket. If provided, tables are created in the path <bucketFolder>/<schema_name>/<table_name>/. If this parameter is not specified, then the path used is <schema_name>/<table_name>/. 
        
                  - **BucketName** *(string) --* 
        
                    The name of the S3 bucket. 
        
                  - **CompressionType** *(string) --* 
        
                    An optional parameter to use GZIP to compress the target files. Set to GZIP to compress the target files. Set to NONE (the default) or do not use to leave the files uncompressed. 
        
                - **DmsTransferSettings** *(dict) --* 
        
                  The settings in JSON format for the DMS Transfer type source endpoint. 
        
                  Attributes include:
        
                  * serviceAccessRoleArn - The IAM role that has permission to access the Amazon S3 bucket. 
                   
                  * bucketName - The name of the S3 bucket to use. 
                   
                  * compressionType - An optional parameter to use GZIP to compress the target files. Set to NONE (the default) or do not use to leave the files uncompressed. 
                   
                  Shorthand syntax: ServiceAccessRoleArn=string ,BucketName=string,CompressionType=string
        
                  JSON syntax:
        
                  { \"ServiceAccessRoleArn\": \"string\", \"BucketName\": \"string\", \"CompressionType\": \"none\"|\"gzip\" } 
        
                  - **ServiceAccessRoleArn** *(string) --* 
        
                    The IAM role that has permission to access the Amazon S3 bucket. 
        
                  - **BucketName** *(string) --* 
        
                    The name of the S3 bucket to use. 
        
                - **MongoDbSettings** *(dict) --* 
        
                  The settings for the MongoDB source endpoint. For more information, see the ``MongoDbSettings`` structure.
        
                  - **Username** *(string) --* 
        
                    The user name you use to access the MongoDB source endpoint. 
        
                  - **Password** *(string) --* 
        
                    The password for the user account you use to access the MongoDB source endpoint. 
        
                  - **ServerName** *(string) --* 
        
                    The name of the server on the MongoDB source endpoint. 
        
                  - **Port** *(integer) --* 
        
                    The port value for the MongoDB source endpoint. 
        
                  - **DatabaseName** *(string) --* 
        
                    The database name on the MongoDB source endpoint. 
        
                  - **AuthType** *(string) --* 
        
                    The authentication type you use to access the MongoDB source endpoint.
        
                    Valid values: NO, PASSWORD 
        
                    When NO is selected, user name and password parameters are not used and can be empty. 
        
                  - **AuthMechanism** *(string) --* 
        
                    The authentication mechanism you use to access the MongoDB source endpoint.
        
                    Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1 
        
                    DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use SCRAM_SHA_1. This attribute is not used when authType=No.
        
                  - **NestingLevel** *(string) --* 
        
                    Specifies either document or table mode. 
        
                    Valid values: NONE, ONE
        
                    Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.
        
                  - **ExtractDocId** *(string) --* 
        
                    Specifies the document ID. Use this attribute when ``NestingLevel`` is set to NONE. 
        
                    Default value is false. 
        
                  - **DocsToInvestigate** *(string) --* 
        
                    Indicates the number of documents to preview to determine the document organization. Use this attribute when ``NestingLevel`` is set to ONE. 
        
                    Must be a positive value greater than 0. Default value is 1000.
        
                  - **AuthSource** *(string) --* 
        
                    The MongoDB database name. This attribute is not used when ``authType=NO`` . 
        
                    The default is admin.
        
                  - **KmsKeyId** *(string) --* 
        
                    The KMS key identifier that will be used to encrypt the connection parameters. If you do not specify a value for the KmsKeyId parameter, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region. 
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeEventSubscriptions(Paginator):
    def paginate(self, SubscriptionName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeEventSubscriptions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              SubscriptionName=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type SubscriptionName: string
        :param SubscriptionName: 
        
          The name of the AWS DMS event subscription to be described.
        
        :type Filters: list
        :param Filters: 
        
          Filters applied to the action.
        
          - *(dict) --* 
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The filter value.
        
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
                \'EventSubscriptionsList\': [
                    {
                        \'CustomerAwsId\': \'string\',
                        \'CustSubscriptionId\': \'string\',
                        \'SnsTopicArn\': \'string\',
                        \'Status\': \'string\',
                        \'SubscriptionCreationTime\': \'string\',
                        \'SourceType\': \'string\',
                        \'SourceIdsList\': [
                            \'string\',
                        ],
                        \'EventCategoriesList\': [
                            \'string\',
                        ],
                        \'Enabled\': True|False
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **EventSubscriptionsList** *(list) --* 
        
              A list of event subscriptions.
        
              - *(dict) --* 
        
                - **CustomerAwsId** *(string) --* 
        
                  The AWS customer account associated with the AWS DMS event notification subscription.
        
                - **CustSubscriptionId** *(string) --* 
        
                  The AWS DMS event notification subscription Id.
        
                - **SnsTopicArn** *(string) --* 
        
                  The topic ARN of the AWS DMS event notification subscription.
        
                - **Status** *(string) --* 
        
                  The status of the AWS DMS event notification subscription.
        
                  Constraints:
        
                  Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist
        
                  The status \"no-permission\" indicates that AWS DMS no longer has permission to post to the SNS topic. The status \"topic-not-exist\" indicates that the topic was deleted after the subscription was created.
        
                - **SubscriptionCreationTime** *(string) --* 
        
                  The time the RDS event notification subscription was created.
        
                - **SourceType** *(string) --* 
        
                  The type of AWS DMS resource that generates events. 
        
                  Valid values: replication-instance | replication-server | security-group | migration-task
        
                - **SourceIdsList** *(list) --* 
        
                  A list of source Ids for the event subscription.
        
                  - *(string) --* 
              
                - **EventCategoriesList** *(list) --* 
        
                  A lists of event categories.
        
                  - *(string) --* 
              
                - **Enabled** *(boolean) --* 
        
                  Boolean value that indicates if the event subscription is enabled.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeEvents(Paginator):
    def paginate(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, EventCategories: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeEvents>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              SourceIdentifier=\'string\',
              SourceType=\'replication-instance\',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Duration=123,
              EventCategories=[
                  \'string\',
              ],
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type SourceIdentifier: string
        :param SourceIdentifier: 
        
          The identifier of the event source. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens. It cannot end with a hyphen or contain two consecutive hyphens. 
        
        :type SourceType: string
        :param SourceType: 
        
          The type of AWS DMS resource that generates events.
        
          Valid values: replication-instance | migration-task
        
        :type StartTime: datetime
        :param StartTime: 
        
          The start time for the events to be listed.
        
        :type EndTime: datetime
        :param EndTime: 
        
          The end time for the events to be listed.
        
        :type Duration: integer
        :param Duration: 
        
          The duration of the events to be listed.
        
        :type EventCategories: list
        :param EventCategories: 
        
          A list of event categories for a source type that you want to subscribe to.
        
          - *(string) --* 
        
        :type Filters: list
        :param Filters: 
        
          Filters applied to the action.
        
          - *(dict) --* 
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The filter value.
        
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
                \'Events\': [
                    {
                        \'SourceIdentifier\': \'string\',
                        \'SourceType\': \'replication-instance\',
                        \'Message\': \'string\',
                        \'EventCategories\': [
                            \'string\',
                        ],
                        \'Date\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Events** *(list) --* 
        
              The events described.
        
              - *(dict) --* 
        
                - **SourceIdentifier** *(string) --* 
        
                  The identifier of the event source. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it cannot end with a hyphen or contain two consecutive hyphens. 
        
                  Constraints:replication instance, endpoint, migration task
        
                - **SourceType** *(string) --* 
        
                  The type of AWS DMS resource that generates events. 
        
                  Valid values: replication-instance | endpoint | migration-task
        
                - **Message** *(string) --* 
        
                  The event message.
        
                - **EventCategories** *(list) --* 
        
                  The event categories available for the specified source type.
        
                  - *(string) --* 
              
                - **Date** *(datetime) --* 
        
                  The date of the event.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeOrderableReplicationInstances(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeOrderableReplicationInstances>`_
        
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
                \'OrderableReplicationInstances\': [
                    {
                        \'EngineVersion\': \'string\',
                        \'ReplicationInstanceClass\': \'string\',
                        \'StorageType\': \'string\',
                        \'MinAllocatedStorage\': 123,
                        \'MaxAllocatedStorage\': 123,
                        \'DefaultAllocatedStorage\': 123,
                        \'IncludedAllocatedStorage\': 123
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **OrderableReplicationInstances** *(list) --* 
        
              The order-able replication instances available.
        
              - *(dict) --* 
        
                - **EngineVersion** *(string) --* 
        
                  The version of the replication engine.
        
                - **ReplicationInstanceClass** *(string) --* 
        
                  The compute and memory capacity of the replication instance.
        
                  Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``  
        
                - **StorageType** *(string) --* 
        
                  The type of storage used by the replication instance.
        
                - **MinAllocatedStorage** *(integer) --* 
        
                  The minimum amount of storage (in gigabytes) that can be allocated for the replication instance.
        
                - **MaxAllocatedStorage** *(integer) --* 
        
                  The minimum amount of storage (in gigabytes) that can be allocated for the replication instance.
        
                - **DefaultAllocatedStorage** *(integer) --* 
        
                  The default amount of storage (in gigabytes) that is allocated for the replication instance.
        
                - **IncludedAllocatedStorage** *(integer) --* 
        
                  The amount of storage (in gigabytes) that is allocated for the replication instance.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeReplicationInstances(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeReplicationInstances>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: list
        :param Filters: 
        
          Filters applied to the describe action.
        
          Valid filter names: replication-instance-arn | replication-instance-id | replication-instance-class | engine-version
        
          - *(dict) --* 
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The filter value.
        
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
                \'ReplicationInstances\': [
                    {
                        \'ReplicationInstanceIdentifier\': \'string\',
                        \'ReplicationInstanceClass\': \'string\',
                        \'ReplicationInstanceStatus\': \'string\',
                        \'AllocatedStorage\': 123,
                        \'InstanceCreateTime\': datetime(2015, 1, 1),
                        \'VpcSecurityGroups\': [
                            {
                                \'VpcSecurityGroupId\': \'string\',
                                \'Status\': \'string\'
                            },
                        ],
                        \'AvailabilityZone\': \'string\',
                        \'ReplicationSubnetGroup\': {
                            \'ReplicationSubnetGroupIdentifier\': \'string\',
                            \'ReplicationSubnetGroupDescription\': \'string\',
                            \'VpcId\': \'string\',
                            \'SubnetGroupStatus\': \'string\',
                            \'Subnets\': [
                                {
                                    \'SubnetIdentifier\': \'string\',
                                    \'SubnetAvailabilityZone\': {
                                        \'Name\': \'string\'
                                    },
                                    \'SubnetStatus\': \'string\'
                                },
                            ]
                        },
                        \'PreferredMaintenanceWindow\': \'string\',
                        \'PendingModifiedValues\': {
                            \'ReplicationInstanceClass\': \'string\',
                            \'AllocatedStorage\': 123,
                            \'MultiAZ\': True|False,
                            \'EngineVersion\': \'string\'
                        },
                        \'MultiAZ\': True|False,
                        \'EngineVersion\': \'string\',
                        \'AutoMinorVersionUpgrade\': True|False,
                        \'KmsKeyId\': \'string\',
                        \'ReplicationInstanceArn\': \'string\',
                        \'ReplicationInstancePublicIpAddress\': \'string\',
                        \'ReplicationInstancePrivateIpAddress\': \'string\',
                        \'ReplicationInstancePublicIpAddresses\': [
                            \'string\',
                        ],
                        \'ReplicationInstancePrivateIpAddresses\': [
                            \'string\',
                        ],
                        \'PubliclyAccessible\': True|False,
                        \'SecondaryAvailabilityZone\': \'string\',
                        \'FreeUntil\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ReplicationInstances** *(list) --* 
        
              The replication instances described.
        
              - *(dict) --* 
        
                - **ReplicationInstanceIdentifier** *(string) --* 
        
                  The replication instance identifier. This parameter is stored as a lowercase string.
        
                  Constraints:
        
                  * Must contain from 1 to 63 alphanumeric characters or hyphens. 
                   
                  * First character must be a letter. 
                   
                  * Cannot end with a hyphen or contain two consecutive hyphens. 
                   
                  Example: ``myrepinstance``  
        
                - **ReplicationInstanceClass** *(string) --* 
        
                  The compute and memory capacity of the replication instance.
        
                  Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``  
        
                - **ReplicationInstanceStatus** *(string) --* 
        
                  The status of the replication instance.
        
                - **AllocatedStorage** *(integer) --* 
        
                  The amount of storage (in gigabytes) that is allocated for the replication instance.
        
                - **InstanceCreateTime** *(datetime) --* 
        
                  The time the replication instance was created.
        
                - **VpcSecurityGroups** *(list) --* 
        
                  The VPC security group for the instance.
        
                  - *(dict) --* 
        
                    - **VpcSecurityGroupId** *(string) --* 
        
                      The VPC security group Id.
        
                    - **Status** *(string) --* 
        
                      The status of the VPC security group.
        
                - **AvailabilityZone** *(string) --* 
        
                  The Availability Zone for the instance.
        
                - **ReplicationSubnetGroup** *(dict) --* 
        
                  The subnet group for the replication instance.
        
                  - **ReplicationSubnetGroupIdentifier** *(string) --* 
        
                    The identifier of the replication instance subnet group.
        
                  - **ReplicationSubnetGroupDescription** *(string) --* 
        
                    The description of the replication subnet group.
        
                  - **VpcId** *(string) --* 
        
                    The ID of the VPC.
        
                  - **SubnetGroupStatus** *(string) --* 
        
                    The status of the subnet group.
        
                  - **Subnets** *(list) --* 
        
                    The subnets that are in the subnet group.
        
                    - *(dict) --* 
        
                      - **SubnetIdentifier** *(string) --* 
        
                        The subnet identifier.
        
                      - **SubnetAvailabilityZone** *(dict) --* 
        
                        The Availability Zone of the subnet.
        
                        - **Name** *(string) --* 
        
                          The name of the availability zone.
        
                      - **SubnetStatus** *(string) --* 
        
                        The status of the subnet.
        
                - **PreferredMaintenanceWindow** *(string) --* 
        
                  The maintenance window times for the replication instance.
        
                - **PendingModifiedValues** *(dict) --* 
        
                  The pending modification values.
        
                  - **ReplicationInstanceClass** *(string) --* 
        
                    The compute and memory capacity of the replication instance.
        
                    Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``  
        
                  - **AllocatedStorage** *(integer) --* 
        
                    The amount of storage (in gigabytes) that is allocated for the replication instance.
        
                  - **MultiAZ** *(boolean) --* 
        
                    Specifies if the replication instance is a Multi-AZ deployment. You cannot set the ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` . 
        
                  - **EngineVersion** *(string) --* 
        
                    The engine version number of the replication instance.
        
                - **MultiAZ** *(boolean) --* 
        
                  Specifies if the replication instance is a Multi-AZ deployment. You cannot set the ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` . 
        
                - **EngineVersion** *(string) --* 
        
                  The engine version number of the replication instance.
        
                - **AutoMinorVersionUpgrade** *(boolean) --* 
        
                  Boolean value indicating if minor version upgrades will be automatically applied to the instance.
        
                - **KmsKeyId** *(string) --* 
        
                  The KMS key identifier that is used to encrypt the content on the replication instance. If you do not specify a value for the KmsKeyId parameter, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
        
                - **ReplicationInstanceArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the replication instance.
        
                - **ReplicationInstancePublicIpAddress** *(string) --* 
        
                  The public IP address of the replication instance.
        
                - **ReplicationInstancePrivateIpAddress** *(string) --* 
        
                  The private IP address of the replication instance.
        
                - **ReplicationInstancePublicIpAddresses** *(list) --* 
        
                  The public IP address of the replication instance.
        
                  - *(string) --* 
              
                - **ReplicationInstancePrivateIpAddresses** *(list) --* 
        
                  The private IP address of the replication instance.
        
                  - *(string) --* 
              
                - **PubliclyAccessible** *(boolean) --* 
        
                  Specifies the accessibility options for the replication instance. A value of ``true`` represents an instance with a public IP address. A value of ``false`` represents an instance with a private IP address. The default value is ``true`` . 
        
                - **SecondaryAvailabilityZone** *(string) --* 
        
                  The availability zone of the standby replication instance in a Multi-AZ deployment.
        
                - **FreeUntil** *(datetime) --* 
        
                  The expiration date of the free replication instance that is part of the Free DMS program. 
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeReplicationSubnetGroups(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeReplicationSubnetGroups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: list
        :param Filters: 
        
          Filters applied to the describe action.
        
          - *(dict) --* 
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The filter value.
        
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
                \'ReplicationSubnetGroups\': [
                    {
                        \'ReplicationSubnetGroupIdentifier\': \'string\',
                        \'ReplicationSubnetGroupDescription\': \'string\',
                        \'VpcId\': \'string\',
                        \'SubnetGroupStatus\': \'string\',
                        \'Subnets\': [
                            {
                                \'SubnetIdentifier\': \'string\',
                                \'SubnetAvailabilityZone\': {
                                    \'Name\': \'string\'
                                },
                                \'SubnetStatus\': \'string\'
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ReplicationSubnetGroups** *(list) --* 
        
              A description of the replication subnet groups.
        
              - *(dict) --* 
        
                - **ReplicationSubnetGroupIdentifier** *(string) --* 
        
                  The identifier of the replication instance subnet group.
        
                - **ReplicationSubnetGroupDescription** *(string) --* 
        
                  The description of the replication subnet group.
        
                - **VpcId** *(string) --* 
        
                  The ID of the VPC.
        
                - **SubnetGroupStatus** *(string) --* 
        
                  The status of the subnet group.
        
                - **Subnets** *(list) --* 
        
                  The subnets that are in the subnet group.
        
                  - *(dict) --* 
        
                    - **SubnetIdentifier** *(string) --* 
        
                      The subnet identifier.
        
                    - **SubnetAvailabilityZone** *(dict) --* 
        
                      The Availability Zone of the subnet.
        
                      - **Name** *(string) --* 
        
                        The name of the availability zone.
        
                    - **SubnetStatus** *(string) --* 
        
                      The status of the subnet.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeReplicationTaskAssessmentResults(Paginator):
    def paginate(self, ReplicationTaskArn: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeReplicationTaskAssessmentResults>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ReplicationTaskArn=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn: 
        
          - The Amazon Resource Name (ARN) string that uniquely identifies the task. When this input parameter is specified the API will return only one result and ignore the values of the max-records and marker parameters. 
        
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
                \'BucketName\': \'string\',
                \'ReplicationTaskAssessmentResults\': [
                    {
                        \'ReplicationTaskIdentifier\': \'string\',
                        \'ReplicationTaskArn\': \'string\',
                        \'ReplicationTaskLastAssessmentDate\': datetime(2015, 1, 1),
                        \'AssessmentStatus\': \'string\',
                        \'AssessmentResultsFile\': \'string\',
                        \'AssessmentResults\': \'string\',
                        \'S3ObjectUrl\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **BucketName** *(string) --* 
        
              - The Amazon S3 bucket where the task assessment report is located. 
        
            - **ReplicationTaskAssessmentResults** *(list) --* 
        
              The task assessment report. 
        
              - *(dict) --* 
        
                The task assessment report in JSON format. 
        
                - **ReplicationTaskIdentifier** *(string) --* 
        
                  The replication task identifier of the task on which the task assessment was run. 
        
                - **ReplicationTaskArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the replication task. 
        
                - **ReplicationTaskLastAssessmentDate** *(datetime) --* 
        
                  The date the task assessment was completed. 
        
                - **AssessmentStatus** *(string) --* 
        
                  The status of the task assessment. 
        
                - **AssessmentResultsFile** *(string) --* 
        
                  The file containing the results of the task assessment. 
        
                - **AssessmentResults** *(string) --* 
        
                  The task assessment results in JSON format. 
        
                - **S3ObjectUrl** *(string) --* 
        
                  The URL of the S3 object containing the task assessment results. 
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeReplicationTasks(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeReplicationTasks>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: list
        :param Filters: 
        
          Filters applied to the describe action.
        
          Valid filter names: replication-task-arn | replication-task-id | migration-type | endpoint-arn | replication-instance-arn
        
          - *(dict) --* 
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The filter value.
        
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
                \'ReplicationTasks\': [
                    {
                        \'ReplicationTaskIdentifier\': \'string\',
                        \'SourceEndpointArn\': \'string\',
                        \'TargetEndpointArn\': \'string\',
                        \'ReplicationInstanceArn\': \'string\',
                        \'MigrationType\': \'full-load\'|\'cdc\'|\'full-load-and-cdc\',
                        \'TableMappings\': \'string\',
                        \'ReplicationTaskSettings\': \'string\',
                        \'Status\': \'string\',
                        \'LastFailureMessage\': \'string\',
                        \'StopReason\': \'string\',
                        \'ReplicationTaskCreationDate\': datetime(2015, 1, 1),
                        \'ReplicationTaskStartDate\': datetime(2015, 1, 1),
                        \'CdcStartPosition\': \'string\',
                        \'CdcStopPosition\': \'string\',
                        \'RecoveryCheckpoint\': \'string\',
                        \'ReplicationTaskArn\': \'string\',
                        \'ReplicationTaskStats\': {
                            \'FullLoadProgressPercent\': 123,
                            \'ElapsedTimeMillis\': 123,
                            \'TablesLoaded\': 123,
                            \'TablesLoading\': 123,
                            \'TablesQueued\': 123,
                            \'TablesErrored\': 123
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ReplicationTasks** *(list) --* 
        
              A description of the replication tasks.
        
              - *(dict) --* 
        
                - **ReplicationTaskIdentifier** *(string) --* 
        
                  The user-assigned replication task identifier or name.
        
                  Constraints:
        
                  * Must contain from 1 to 255 alphanumeric characters or hyphens. 
                   
                  * First character must be a letter. 
                   
                  * Cannot end with a hyphen or contain two consecutive hyphens. 
                   
                - **SourceEndpointArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
        
                - **TargetEndpointArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
        
                - **ReplicationInstanceArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the replication instance.
        
                - **MigrationType** *(string) --* 
        
                  The type of migration.
        
                - **TableMappings** *(string) --* 
        
                  Table mappings specified in the task.
        
                - **ReplicationTaskSettings** *(string) --* 
        
                  The settings for the replication task.
        
                - **Status** *(string) --* 
        
                  The status of the replication task.
        
                - **LastFailureMessage** *(string) --* 
        
                  The last error (failure) message generated for the replication instance.
        
                - **StopReason** *(string) --* 
        
                  The reason the replication task was stopped.
        
                - **ReplicationTaskCreationDate** *(datetime) --* 
        
                  The date the replication task was created.
        
                - **ReplicationTaskStartDate** *(datetime) --* 
        
                  The date the replication task is scheduled to start.
        
                - **CdcStartPosition** *(string) --* 
        
                  Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results in an error.
        
                  The value can be in date, checkpoint, or LSN/SCN format.
        
                  Date Example: --cdc-start-position “2018-03-08T12:12:12”
        
                  Checkpoint Example: --cdc-start-position \"checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93\"
        
                  LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”
        
                - **CdcStopPosition** *(string) --* 
        
                  Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
        
                  Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”
        
                  Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12 “
        
                - **RecoveryCheckpoint** *(string) --* 
        
                  Indicates the last checkpoint that occurred during a change data capture (CDC) operation. You can provide this value to the ``CdcStartPosition`` parameter to start a CDC operation that begins at that checkpoint.
        
                - **ReplicationTaskArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the replication task.
        
                - **ReplicationTaskStats** *(dict) --* 
        
                  The statistics for the task, including elapsed time, tables loaded, and table errors.
        
                  - **FullLoadProgressPercent** *(integer) --* 
        
                    The percent complete for the full load migration task.
        
                  - **ElapsedTimeMillis** *(integer) --* 
        
                    The elapsed time of the task, in milliseconds.
        
                  - **TablesLoaded** *(integer) --* 
        
                    The number of tables loaded for this task.
        
                  - **TablesLoading** *(integer) --* 
        
                    The number of tables currently loading for this task.
        
                  - **TablesQueued** *(integer) --* 
        
                    The number of tables queued for this task.
        
                  - **TablesErrored** *(integer) --* 
        
                    The number of errors that have occurred during this task.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeSchemas(Paginator):
    def paginate(self, EndpointArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeSchemas>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              EndpointArn=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
        
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
                \'Schemas\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Schemas** *(list) --* 
        
              The described schema.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeTableStatistics(Paginator):
    def paginate(self, ReplicationTaskArn: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeTableStatistics>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ReplicationTaskArn=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the replication task.
        
        :type Filters: list
        :param Filters: 
        
          Filters applied to the describe table statistics action.
        
          Valid filter names: schema-name | table-name | table-state
        
          A combination of filters creates an AND condition where each record matches all specified filters.
        
          - *(dict) --* 
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The filter value.
        
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
                \'ReplicationTaskArn\': \'string\',
                \'TableStatistics\': [
                    {
                        \'SchemaName\': \'string\',
                        \'TableName\': \'string\',
                        \'Inserts\': 123,
                        \'Deletes\': 123,
                        \'Updates\': 123,
                        \'Ddls\': 123,
                        \'FullLoadRows\': 123,
                        \'FullLoadCondtnlChkFailedRows\': 123,
                        \'FullLoadErrorRows\': 123,
                        \'LastUpdateTime\': datetime(2015, 1, 1),
                        \'TableState\': \'string\',
                        \'ValidationPendingRecords\': 123,
                        \'ValidationFailedRecords\': 123,
                        \'ValidationSuspendedRecords\': 123,
                        \'ValidationState\': \'string\',
                        \'ValidationStateDetails\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ReplicationTaskArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the replication task.
        
            - **TableStatistics** *(list) --* 
        
              The table statistics.
        
              - *(dict) --* 
        
                - **SchemaName** *(string) --* 
        
                  The schema name.
        
                - **TableName** *(string) --* 
        
                  The name of the table.
        
                - **Inserts** *(integer) --* 
        
                  The number of insert actions performed on a table.
        
                - **Deletes** *(integer) --* 
        
                  The number of delete actions performed on a table.
        
                - **Updates** *(integer) --* 
        
                  The number of update actions performed on a table.
        
                - **Ddls** *(integer) --* 
        
                  The Data Definition Language (DDL) used to build and modify the structure of your tables.
        
                - **FullLoadRows** *(integer) --* 
        
                  The number of rows added during the Full Load operation.
        
                - **FullLoadCondtnlChkFailedRows** *(integer) --* 
        
                  The number of rows that failed conditional checks during the Full Load operation (valid only for DynamoDB as a target migrations).
        
                - **FullLoadErrorRows** *(integer) --* 
        
                  The number of rows that failed to load during the Full Load operation (valid only for DynamoDB as a target migrations).
        
                - **LastUpdateTime** *(datetime) --* 
        
                  The last time the table was updated.
        
                - **TableState** *(string) --* 
        
                  The state of the tables described.
        
                  Valid states: Table does not exist | Before load | Full load | Table completed | Table cancelled | Table error | Table all | Table updates | Table is being reloaded
        
                - **ValidationPendingRecords** *(integer) --* 
        
                  The number of records that have yet to be validated.
        
                - **ValidationFailedRecords** *(integer) --* 
        
                  The number of records that failed validation.
        
                - **ValidationSuspendedRecords** *(integer) --* 
        
                  The number of records that could not be validated.
        
                - **ValidationState** *(string) --* 
        
                  The validation state of the table.
        
                  The parameter can have the following values
        
                  * Not enabled—Validation is not enabled for the table in the migration task. 
                   
                  * Pending records—Some records in the table are waiting for validation. 
                   
                  * Mismatched records—Some records in the table do not match between the source and target. 
                   
                  * Suspended records—Some records in the table could not be validated. 
                   
                  * No primary key—The table could not be validated because it had no primary key. 
                   
                  * Table error—The table was not validated because it was in an error state and some data was not migrated. 
                   
                  * Validated—All rows in the table were validated. If the table is updated, the status can change from Validated. 
                   
                  * Error—The table could not be validated because of an unexpected error. 
                   
                - **ValidationStateDetails** *(string) --* 
        
                  Additional details about the state of validation.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
