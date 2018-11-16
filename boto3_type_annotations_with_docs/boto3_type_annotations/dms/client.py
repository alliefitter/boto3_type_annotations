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
    def add_tags_to_resource(self, ResourceArn: str, Tags: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/AddTagsToResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.add_tags_to_resource(
              ResourceArn=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the AWS DMS resource the tag is to be added to. AWS DMS resources include a replication instance, endpoint, and a replication task.
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          The tag to be assigned to the DMS resource.
        
          - *(dict) --* 
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with \"aws:\" or \"dms:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with \"aws:\" or \"dms:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
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

    def create_endpoint(self, EndpointIdentifier: str, EndpointType: str, EngineName: str, Username: str = None, Password: str = None, ServerName: str = None, Port: int = None, DatabaseName: str = None, ExtraConnectionAttributes: str = None, KmsKeyId: str = None, Tags: List = None, CertificateArn: str = None, SslMode: str = None, ServiceAccessRoleArn: str = None, ExternalTableDefinition: str = None, DynamoDbSettings: Dict = None, S3Settings: Dict = None, DmsTransferSettings: Dict = None, MongoDbSettings: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/CreateEndpoint>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_endpoint(
              EndpointIdentifier=\'string\',
              EndpointType=\'source\'|\'target\',
              EngineName=\'string\',
              Username=\'string\',
              Password=\'string\',
              ServerName=\'string\',
              Port=123,
              DatabaseName=\'string\',
              ExtraConnectionAttributes=\'string\',
              KmsKeyId=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              CertificateArn=\'string\',
              SslMode=\'none\'|\'require\'|\'verify-ca\'|\'verify-full\',
              ServiceAccessRoleArn=\'string\',
              ExternalTableDefinition=\'string\',
              DynamoDbSettings={
                  \'ServiceAccessRoleArn\': \'string\'
              },
              S3Settings={
                  \'ServiceAccessRoleArn\': \'string\',
                  \'ExternalTableDefinition\': \'string\',
                  \'CsvRowDelimiter\': \'string\',
                  \'CsvDelimiter\': \'string\',
                  \'BucketFolder\': \'string\',
                  \'BucketName\': \'string\',
                  \'CompressionType\': \'none\'|\'gzip\'
              },
              DmsTransferSettings={
                  \'ServiceAccessRoleArn\': \'string\',
                  \'BucketName\': \'string\'
              },
              MongoDbSettings={
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
          )
        :type EndpointIdentifier: string
        :param EndpointIdentifier: **[REQUIRED]** 
        
          The database endpoint identifier. Identifiers must begin with a letter; must contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two consecutive hyphens.
        
        :type EndpointType: string
        :param EndpointType: **[REQUIRED]** 
        
          The type of endpoint.
        
        :type EngineName: string
        :param EngineName: **[REQUIRED]** 
        
          The type of engine for the endpoint. Valid values, depending on the EndPointType, include mysql, oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase, dynamodb, mongodb, and sqlserver.
        
        :type Username: string
        :param Username: 
        
          The user name to be used to login to the endpoint database.
        
        :type Password: string
        :param Password: 
        
          The password to be used to login to the endpoint database.
        
        :type ServerName: string
        :param ServerName: 
        
          The name of the server where the endpoint database resides.
        
        :type Port: integer
        :param Port: 
        
          The port used by the endpoint database.
        
        :type DatabaseName: string
        :param DatabaseName: 
        
          The name of the endpoint database.
        
        :type ExtraConnectionAttributes: string
        :param ExtraConnectionAttributes: 
        
          Additional attributes associated with the connection.
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          The KMS key identifier that will be used to encrypt the connection parameters. If you do not specify a value for the KmsKeyId parameter, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
        
        :type Tags: list
        :param Tags: 
        
          Tags to be added to the endpoint.
        
          - *(dict) --* 
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with \"aws:\" or \"dms:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with \"aws:\" or \"dms:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :type CertificateArn: string
        :param CertificateArn: 
        
          The Amazon Resource Name (ARN) for the certificate.
        
        :type SslMode: string
        :param SslMode: 
        
          The SSL mode to use for the SSL connection.
        
          SSL mode can be one of four values: none, require, verify-ca, verify-full. 
        
          The default value is none.
        
        :type ServiceAccessRoleArn: string
        :param ServiceAccessRoleArn: 
        
          The Amazon Resource Name (ARN) for the service access role you want to use to create the endpoint. 
        
        :type ExternalTableDefinition: string
        :param ExternalTableDefinition: 
        
          The external table definition. 
        
        :type DynamoDbSettings: dict
        :param DynamoDbSettings: 
        
          Settings in JSON format for the target Amazon DynamoDB endpoint. For more information about the available settings, see the **Using Object Mapping to Migrate Data to DynamoDB** section at `Using an Amazon DynamoDB Database as a Target for AWS Database Migration Service <http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html>`__ . 
        
          - **ServiceAccessRoleArn** *(string) --* **[REQUIRED]** 
        
            The Amazon Resource Name (ARN) used by the service access IAM role. 
        
        :type S3Settings: dict
        :param S3Settings: 
        
          Settings in JSON format for the target Amazon S3 endpoint. For more information about the available settings, see the **Extra Connection Attributes** section at `Using Amazon S3 as a Target for AWS Database Migration Service <http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html>`__ . 
        
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
        
        :type DmsTransferSettings: dict
        :param DmsTransferSettings: 
        
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
        
        :type MongoDbSettings: dict
        :param MongoDbSettings: 
        
          Settings in JSON format for the source MongoDB endpoint. For more information about the available settings, see the **Configuration Properties When Using MongoDB as a Source for AWS Database Migration Service** section at `Using MongoDB as a Target for AWS Database Migration Service <http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html>`__ . 
        
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
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Endpoint\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Endpoint** *(dict) --* 
        
              The endpoint that was created.
        
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
        
        """
        pass

    def create_event_subscription(self, SubscriptionName: str, SnsTopicArn: str, SourceType: str = None, EventCategories: List = None, SourceIds: List = None, Enabled: bool = None, Tags: List = None) -> Dict:
        """
        
        You can specify the type of source (``SourceType`` ) you want to be notified of, provide a list of AWS DMS source IDs (``SourceIds`` ) that triggers the events, and provide a list of event categories (``EventCategories`` ) for events you want to be notified of. If you specify both the ``SourceType`` and ``SourceIds`` , such as ``SourceType = replication-instance`` and ``SourceIdentifier = my-replinstance`` , you will be notified of all the replication instance events for the specified source. If you specify a ``SourceType`` but don\'t specify a ``SourceIdentifier`` , you receive notice of the events for that source type for all your AWS DMS sources. If you don\'t specify either ``SourceType`` nor ``SourceIdentifier`` , you will be notified of events generated from all AWS DMS sources belonging to your customer account.
        
        For more information about AWS DMS events, see `Working with Events and Notifications <http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html>`__ in the AWS Database MIgration Service User Guide.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/CreateEventSubscription>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_event_subscription(
              SubscriptionName=\'string\',
              SnsTopicArn=\'string\',
              SourceType=\'string\',
              EventCategories=[
                  \'string\',
              ],
              SourceIds=[
                  \'string\',
              ],
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
        
          The name of the AWS DMS event notification subscription. 
        
          Constraints: The name must be less than 255 characters. 
        
        :type SnsTopicArn: string
        :param SnsTopicArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it. 
        
        :type SourceType: string
        :param SourceType: 
        
          The type of AWS DMS resource that generates the events. For example, if you want to be notified of events generated by a replication instance, you set this parameter to ``replication-instance`` . If this value is not specified, all events are returned. 
        
          Valid values: replication-instance | migration-task
        
        :type EventCategories: list
        :param EventCategories: 
        
          A list of event categories for a source type that you want to subscribe to. You can see a list of the categories for a given source type by calling the **DescribeEventCategories** action or in the topic `Working with Events and Notifications <http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html>`__ in the AWS Database Migration Service User Guide. 
        
          - *(string) --* 
        
        :type SourceIds: list
        :param SourceIds: 
        
          The list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it cannot end with a hyphen or contain two consecutive hyphens. 
        
          - *(string) --* 
        
        :type Enabled: boolean
        :param Enabled: 
        
          A Boolean value; set to **true** to activate the subscription, or set to **false** to create the subscription but not activate it. 
        
        :type Tags: list
        :param Tags: 
        
          A tag to be attached to the event subscription.
        
          - *(dict) --* 
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with \"aws:\" or \"dms:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with \"aws:\" or \"dms:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
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
                    \'SubscriptionCreationTime\': \'string\',
                    \'SourceType\': \'string\',
                    \'SourceIdsList\': [
                        \'string\',
                    ],
                    \'EventCategoriesList\': [
                        \'string\',
                    ],
                    \'Enabled\': True|False
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **EventSubscription** *(dict) --* 
        
              The event subscription that was created.
        
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
        
        """
        pass

    def create_replication_instance(self, ReplicationInstanceIdentifier: str, ReplicationInstanceClass: str, AllocatedStorage: int = None, VpcSecurityGroupIds: List = None, AvailabilityZone: str = None, ReplicationSubnetGroupIdentifier: str = None, PreferredMaintenanceWindow: str = None, MultiAZ: bool = None, EngineVersion: str = None, AutoMinorVersionUpgrade: bool = None, Tags: List = None, KmsKeyId: str = None, PubliclyAccessible: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/CreateReplicationInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_replication_instance(
              ReplicationInstanceIdentifier=\'string\',
              AllocatedStorage=123,
              ReplicationInstanceClass=\'string\',
              VpcSecurityGroupIds=[
                  \'string\',
              ],
              AvailabilityZone=\'string\',
              ReplicationSubnetGroupIdentifier=\'string\',
              PreferredMaintenanceWindow=\'string\',
              MultiAZ=True|False,
              EngineVersion=\'string\',
              AutoMinorVersionUpgrade=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              KmsKeyId=\'string\',
              PubliclyAccessible=True|False
          )
        :type ReplicationInstanceIdentifier: string
        :param ReplicationInstanceIdentifier: **[REQUIRED]** 
        
          The replication instance identifier. This parameter is stored as a lowercase string.
        
          Constraints:
        
          * Must contain from 1 to 63 alphanumeric characters or hyphens. 
           
          * First character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
          Example: ``myrepinstance``  
        
        :type AllocatedStorage: integer
        :param AllocatedStorage: 
        
          The amount of storage (in gigabytes) to be initially allocated for the replication instance.
        
        :type ReplicationInstanceClass: string
        :param ReplicationInstanceClass: **[REQUIRED]** 
        
          The compute and memory capacity of the replication instance as specified by the replication instance class.
        
          Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``  
        
        :type VpcSecurityGroupIds: list
        :param VpcSecurityGroupIds: 
        
          Specifies the VPC security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance. 
        
          - *(string) --* 
        
        :type AvailabilityZone: string
        :param AvailabilityZone: 
        
          The EC2 Availability Zone that the replication instance will be created in.
        
          Default: A random, system-chosen Availability Zone in the endpoint\'s region.
        
          Example: ``us-east-1d``  
        
        :type ReplicationSubnetGroupIdentifier: string
        :param ReplicationSubnetGroupIdentifier: 
        
          A subnet group to associate with the replication instance.
        
        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow: 
        
          The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
        
          Format: ``ddd:hh24:mi-ddd:hh24:mi``  
        
          Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week.
        
          Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun
        
          Constraints: Minimum 30-minute window.
        
        :type MultiAZ: boolean
        :param MultiAZ: 
        
          Specifies if the replication instance is a Multi-AZ deployment. You cannot set the ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` . 
        
        :type EngineVersion: string
        :param EngineVersion: 
        
          The engine version number of the replication instance.
        
        :type AutoMinorVersionUpgrade: boolean
        :param AutoMinorVersionUpgrade: 
        
          Indicates that minor engine upgrades will be applied automatically to the replication instance during the maintenance window.
        
          Default: ``true``  
        
        :type Tags: list
        :param Tags: 
        
          Tags to be associated with the replication instance.
        
          - *(dict) --* 
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with \"aws:\" or \"dms:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with \"aws:\" or \"dms:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          The KMS key identifier that will be used to encrypt the content on the replication instance. If you do not specify a value for the KmsKeyId parameter, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
        
        :type PubliclyAccessible: boolean
        :param PubliclyAccessible: 
        
          Specifies the accessibility options for the replication instance. A value of ``true`` represents an instance with a public IP address. A value of ``false`` represents an instance with a private IP address. The default value is ``true`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ReplicationInstance\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ReplicationInstance** *(dict) --* 
        
              The replication instance that was created.
        
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
        
        """
        pass

    def create_replication_subnet_group(self, ReplicationSubnetGroupIdentifier: str, ReplicationSubnetGroupDescription: str, SubnetIds: List, Tags: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/CreateReplicationSubnetGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_replication_subnet_group(
              ReplicationSubnetGroupIdentifier=\'string\',
              ReplicationSubnetGroupDescription=\'string\',
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
        :type ReplicationSubnetGroupIdentifier: string
        :param ReplicationSubnetGroupIdentifier: **[REQUIRED]** 
        
          The name for the replication subnet group. This value is stored as a lowercase string.
        
          Constraints: Must contain no more than 255 alphanumeric characters, periods, spaces, underscores, or hyphens. Must not be \"default\".
        
          Example: ``mySubnetgroup``  
        
        :type ReplicationSubnetGroupDescription: string
        :param ReplicationSubnetGroupDescription: **[REQUIRED]** 
        
          The description for the subnet group.
        
        :type SubnetIds: list
        :param SubnetIds: **[REQUIRED]** 
        
          The EC2 subnet IDs for the subnet group.
        
          - *(string) --* 
        
        :type Tags: list
        :param Tags: 
        
          The tag to be assigned to the subnet group.
        
          - *(dict) --* 
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with \"aws:\" or \"dms:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with \"aws:\" or \"dms:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ReplicationSubnetGroup** *(dict) --* 
        
              The replication subnet group that was created.
        
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
        
        """
        pass

    def create_replication_task(self, ReplicationTaskIdentifier: str, SourceEndpointArn: str, TargetEndpointArn: str, ReplicationInstanceArn: str, MigrationType: str, TableMappings: str, ReplicationTaskSettings: str = None, CdcStartTime: datetime = None, CdcStartPosition: str = None, CdcStopPosition: str = None, Tags: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/CreateReplicationTask>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_replication_task(
              ReplicationTaskIdentifier=\'string\',
              SourceEndpointArn=\'string\',
              TargetEndpointArn=\'string\',
              ReplicationInstanceArn=\'string\',
              MigrationType=\'full-load\'|\'cdc\'|\'full-load-and-cdc\',
              TableMappings=\'string\',
              ReplicationTaskSettings=\'string\',
              CdcStartTime=datetime(2015, 1, 1),
              CdcStartPosition=\'string\',
              CdcStopPosition=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type ReplicationTaskIdentifier: string
        :param ReplicationTaskIdentifier: **[REQUIRED]** 
        
          The replication task identifier.
        
          Constraints:
        
          * Must contain from 1 to 255 alphanumeric characters or hyphens. 
           
          * First character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
        :type SourceEndpointArn: string
        :param SourceEndpointArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
        
        :type TargetEndpointArn: string
        :param TargetEndpointArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
        
        :type ReplicationInstanceArn: string
        :param ReplicationInstanceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the replication instance.
        
        :type MigrationType: string
        :param MigrationType: **[REQUIRED]** 
        
          The migration type.
        
        :type TableMappings: string
        :param TableMappings: **[REQUIRED]** 
        
          When using the AWS CLI or boto3, provide the path of the JSON file that contains the table mappings. Precede the path with \"file://\". When working with the DMS API, provide the JSON as the parameter value.
        
          For example, --table-mappings file://mappingfile.json
        
        :type ReplicationTaskSettings: string
        :param ReplicationTaskSettings: 
        
          Settings for the task, such as target metadata settings. For a complete list of task settings, see `Task Settings for AWS Database Migration Service Tasks <http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html>`__ .
        
        :type CdcStartTime: datetime
        :param CdcStartTime: 
        
          Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or CdcStartPosition to specify when you want a CDC operation to start. Specifying both values results in an error.
        
          Timestamp Example: --cdc-start-time “2018-03-08T12:12:12”
        
        :type CdcStartPosition: string
        :param CdcStartPosition: 
        
          Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results in an error.
        
          The value can be in date, checkpoint, or LSN/SCN format.
        
          Date Example: --cdc-start-position “2018-03-08T12:12:12”
        
          Checkpoint Example: --cdc-start-position \"checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93\"
        
          LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”
        
        :type CdcStopPosition: string
        :param CdcStopPosition: 
        
          Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
        
          Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”
        
          Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12 “
        
        :type Tags: list
        :param Tags: 
        
          Tags to be added to the replication instance.
        
          - *(dict) --* 
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with \"aws:\" or \"dms:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with \"aws:\" or \"dms:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ReplicationTask\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ReplicationTask** *(dict) --* 
        
              The replication task that was created.
        
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
        
        """
        pass

    def delete_certificate(self, CertificateArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DeleteCertificate>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_certificate(
              CertificateArn=\'string\'
          )
        :type CertificateArn: string
        :param CertificateArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the deleted certificate.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Certificate\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Certificate** *(dict) --* 
        
              The Secure Sockets Layer (SSL) certificate.
        
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
        
        """
        pass

    def delete_endpoint(self, EndpointArn: str) -> Dict:
        """
        
        .. note::
        
          All tasks associated with the endpoint must be deleted before you can delete the endpoint.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DeleteEndpoint>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_endpoint(
              EndpointArn=\'string\'
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Endpoint\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Endpoint** *(dict) --* 
        
              The endpoint that was deleted.
        
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
        
        """
        pass

    def delete_event_subscription(self, SubscriptionName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DeleteEventSubscription>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_event_subscription(
              SubscriptionName=\'string\'
          )
        :type SubscriptionName: string
        :param SubscriptionName: **[REQUIRED]** 
        
          The name of the DMS event notification subscription to be deleted.
        
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
                    \'SubscriptionCreationTime\': \'string\',
                    \'SourceType\': \'string\',
                    \'SourceIdsList\': [
                        \'string\',
                    ],
                    \'EventCategoriesList\': [
                        \'string\',
                    ],
                    \'Enabled\': True|False
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **EventSubscription** *(dict) --* 
        
              The event subscription that was deleted.
        
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
        
        """
        pass

    def delete_replication_instance(self, ReplicationInstanceArn: str) -> Dict:
        """
        
        .. note::
        
          You must delete any migration tasks that are associated with the replication instance before you can delete it.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DeleteReplicationInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_replication_instance(
              ReplicationInstanceArn=\'string\'
          )
        :type ReplicationInstanceArn: string
        :param ReplicationInstanceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the replication instance to be deleted.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ReplicationInstance\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ReplicationInstance** *(dict) --* 
        
              The replication instance that was deleted.
        
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
        
        """
        pass

    def delete_replication_subnet_group(self, ReplicationSubnetGroupIdentifier: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DeleteReplicationSubnetGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_replication_subnet_group(
              ReplicationSubnetGroupIdentifier=\'string\'
          )
        :type ReplicationSubnetGroupIdentifier: string
        :param ReplicationSubnetGroupIdentifier: **[REQUIRED]** 
        
          The subnet group name of the replication instance.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
        """
        pass

    def delete_replication_task(self, ReplicationTaskArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DeleteReplicationTask>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_replication_task(
              ReplicationTaskArn=\'string\'
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the replication task to be deleted.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ReplicationTask\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ReplicationTask** *(dict) --* 
        
              The deleted replication task.
        
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
        
        """
        pass

    def describe_account_attributes(self) -> Dict:
        """
        
        This command does not take any parameters.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeAccountAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_account_attributes()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AccountQuotas\': [
                    {
                        \'AccountQuotaName\': \'string\',
                        \'Used\': 123,
                        \'Max\': 123
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **AccountQuotas** *(list) --* 
        
              Account quota information.
        
              - *(dict) --* 
        
                Describes a quota for an AWS account, for example, the number of replication instances allowed.
        
                - **AccountQuotaName** *(string) --* 
        
                  The name of the AWS DMS quota for this AWS account.
        
                - **Used** *(integer) --* 
        
                  The amount currently used toward the quota maximum.
        
                - **Max** *(integer) --* 
        
                  The maximum allowed value for the quota.
        
        """
        pass

    def describe_certificates(self, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeCertificates>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_certificates(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\'
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 10
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Marker** *(string) --* 
        
              The pagination token.
        
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
        
        """
        pass

    def describe_connections(self, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeConnections>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_connections(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\'
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'Connections\': [
                    {
                        \'ReplicationInstanceArn\': \'string\',
                        \'EndpointArn\': \'string\',
                        \'Status\': \'string\',
                        \'LastFailureMessage\': \'string\',
                        \'EndpointIdentifier\': \'string\',
                        \'ReplicationInstanceIdentifier\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
        
        """
        pass

    def describe_endpoint_types(self, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeEndpointTypes>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_endpoint_types(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\'
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'SupportedEndpointTypes\': [
                    {
                        \'EngineName\': \'string\',
                        \'SupportsCDC\': True|False,
                        \'EndpointType\': \'source\'|\'target\',
                        \'EngineDisplayName\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
        
        """
        pass

    def describe_endpoints(self, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeEndpoints>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_endpoints(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\'
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
        
        """
        pass

    def describe_event_categories(self, SourceType: str = None, Filters: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeEventCategories>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_event_categories(
              SourceType=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ]
          )
        :type SourceType: string
        :param SourceType: 
        
          The type of AWS DMS resource that generates events. 
        
          Valid values: replication-instance | migration-task
        
        :type Filters: list
        :param Filters: 
        
          Filters applied to the action.
        
          - *(dict) --* 
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              The filter value.
        
              - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EventCategoryGroupList\': [
                    {
                        \'SourceType\': \'string\',
                        \'EventCategories\': [
                            \'string\',
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **EventCategoryGroupList** *(list) --* 
        
              A list of event categories.
        
              - *(dict) --* 
        
                - **SourceType** *(string) --* 
        
                  The type of AWS DMS resource that generates events. 
        
                  Valid values: replication-instance | replication-server | security-group | migration-task
        
                - **EventCategories** *(list) --* 
        
                  A list of event categories for a ``SourceType`` that you want to subscribe to. 
        
                  - *(string) --* 
              
        """
        pass

    def describe_event_subscriptions(self, SubscriptionName: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        If you specify ``SubscriptionName`` , this action lists the description for that subscription.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeEventSubscriptions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_event_subscriptions(
              SubscriptionName=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\'
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
        
        """
        pass

    def describe_events(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, EventCategories: List = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeEvents>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_events(
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
              MaxRecords=123,
              Marker=\'string\'
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
        
        """
        pass

    def describe_orderable_replication_instances(self, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeOrderableReplicationInstances>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_orderable_replication_instances(
              MaxRecords=123,
              Marker=\'string\'
          )
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
                \'Marker\': \'string\'
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
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        """
        pass

    def describe_refresh_schemas_status(self, EndpointArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeRefreshSchemasStatus>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_refresh_schemas_status(
              EndpointArn=\'string\'
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RefreshSchemasStatus\': {
                    \'EndpointArn\': \'string\',
                    \'ReplicationInstanceArn\': \'string\',
                    \'Status\': \'successful\'|\'failed\'|\'refreshing\',
                    \'LastRefreshDate\': datetime(2015, 1, 1),
                    \'LastFailureMessage\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **RefreshSchemasStatus** *(dict) --* 
        
              The status of the schema.
        
              - **EndpointArn** *(string) --* 
        
                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
        
              - **ReplicationInstanceArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the replication instance.
        
              - **Status** *(string) --* 
        
                The status of the schema.
        
              - **LastRefreshDate** *(datetime) --* 
        
                The date the schema was last refreshed.
        
              - **LastFailureMessage** *(string) --* 
        
                The last failure message for the schema.
        
        """
        pass

    def describe_replication_instance_task_logs(self, ReplicationInstanceArn: str, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeReplicationInstanceTaskLogs>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_replication_instance_task_logs(
              ReplicationInstanceArn=\'string\',
              MaxRecords=123,
              Marker=\'string\'
          )
        :type ReplicationInstanceArn: string
        :param ReplicationInstanceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the replication instance.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ReplicationInstanceArn\': \'string\',
                \'ReplicationInstanceTaskLogs\': [
                    {
                        \'ReplicationTaskName\': \'string\',
                        \'ReplicationTaskArn\': \'string\',
                        \'ReplicationInstanceTaskLogSize\': 123
                    },
                ],
                \'Marker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ReplicationInstanceArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the replication instance.
        
            - **ReplicationInstanceTaskLogs** *(list) --* 
        
              An array of replication task log metadata. Each member of the array contains the replication task name, ARN, and task log size (in bytes). 
        
              - *(dict) --* 
        
                Contains metadata for a replication instance task log.
        
                - **ReplicationTaskName** *(string) --* 
        
                  The name of the replication task.
        
                - **ReplicationTaskArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the replication task.
        
                - **ReplicationInstanceTaskLogSize** *(integer) --* 
        
                  The size, in bytes, of the replication task log.
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
        
        """
        pass

    def describe_replication_instances(self, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeReplicationInstances>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_replication_instances(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\'
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
        
        """
        pass

    def describe_replication_subnet_groups(self, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeReplicationSubnetGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_replication_subnet_groups(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\'
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
        
        """
        pass

    def describe_replication_task_assessment_results(self, ReplicationTaskArn: str = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeReplicationTaskAssessmentResults>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_replication_task_assessment_results(
              ReplicationTaskArn=\'string\',
              MaxRecords=123,
              Marker=\'string\'
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn: 
        
          - The Amazon Resource Name (ARN) string that uniquely identifies the task. When this input parameter is specified the API will return only one result and ignore the values of the max-records and marker parameters. 
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
        
        """
        pass

    def describe_replication_tasks(self, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeReplicationTasks>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_replication_tasks(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\'
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
        
        """
        pass

    def describe_schemas(self, EndpointArn: str, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeSchemas>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_schemas(
              EndpointArn=\'string\',
              MaxRecords=123,
              Marker=\'string\'
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'Schemas\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
            - **Schemas** *(list) --* 
        
              The described schema.
        
              - *(string) --* 
          
        """
        pass

    def describe_table_statistics(self, ReplicationTaskArn: str, MaxRecords: int = None, Marker: str = None, Filters: List = None) -> Dict:
        """
        
        Note that the \"last updated\" column the DMS console only indicates the time that AWS DMS last updated the table statistics record for a table. It does not indicate the time of the last update to the table.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeTableStatistics>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_table_statistics(
              ReplicationTaskArn=\'string\',
              MaxRecords=123,
              Marker=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ]
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the replication task.
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 500.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
                \'Marker\': \'string\'
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
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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

    def import_certificate(self, CertificateIdentifier: str, CertificatePem: str = None, CertificateWallet: bytes = None, Tags: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ImportCertificate>`_
        
        **Request Syntax** 
        ::
        
          response = client.import_certificate(
              CertificateIdentifier=\'string\',
              CertificatePem=\'string\',
              CertificateWallet=b\'bytes\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type CertificateIdentifier: string
        :param CertificateIdentifier: **[REQUIRED]** 
        
          The customer-assigned name of the certificate. Valid characters are A-z and 0-9.
        
        :type CertificatePem: string
        :param CertificatePem: 
        
          The contents of the .pem X.509 certificate file for the certificate.
        
        :type CertificateWallet: bytes
        :param CertificateWallet: 
        
          The location of the imported Oracle Wallet certificate for use with SSL.
        
        :type Tags: list
        :param Tags: 
        
          The tags associated with the certificate.
        
          - *(dict) --* 
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with \"aws:\" or \"dms:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with \"aws:\" or \"dms:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Certificate\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Certificate** *(dict) --* 
        
              The certificate to be uploaded.
        
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
        
        """
        pass

    def list_tags_for_resource(self, ResourceArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ListTagsForResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags_for_resource(
              ResourceArn=\'string\'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) string that uniquely identifies the AWS DMS resource.
        
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **TagList** *(list) --* 
        
              A list of tags for the resource.
        
              - *(dict) --* 
        
                - **Key** *(string) --* 
        
                  A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with \"aws:\" or \"dms:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
                - **Value** *(string) --* 
        
                  A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with \"aws:\" or \"dms:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        """
        pass

    def modify_endpoint(self, EndpointArn: str, EndpointIdentifier: str = None, EndpointType: str = None, EngineName: str = None, Username: str = None, Password: str = None, ServerName: str = None, Port: int = None, DatabaseName: str = None, ExtraConnectionAttributes: str = None, CertificateArn: str = None, SslMode: str = None, ServiceAccessRoleArn: str = None, ExternalTableDefinition: str = None, DynamoDbSettings: Dict = None, S3Settings: Dict = None, DmsTransferSettings: Dict = None, MongoDbSettings: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ModifyEndpoint>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_endpoint(
              EndpointArn=\'string\',
              EndpointIdentifier=\'string\',
              EndpointType=\'source\'|\'target\',
              EngineName=\'string\',
              Username=\'string\',
              Password=\'string\',
              ServerName=\'string\',
              Port=123,
              DatabaseName=\'string\',
              ExtraConnectionAttributes=\'string\',
              CertificateArn=\'string\',
              SslMode=\'none\'|\'require\'|\'verify-ca\'|\'verify-full\',
              ServiceAccessRoleArn=\'string\',
              ExternalTableDefinition=\'string\',
              DynamoDbSettings={
                  \'ServiceAccessRoleArn\': \'string\'
              },
              S3Settings={
                  \'ServiceAccessRoleArn\': \'string\',
                  \'ExternalTableDefinition\': \'string\',
                  \'CsvRowDelimiter\': \'string\',
                  \'CsvDelimiter\': \'string\',
                  \'BucketFolder\': \'string\',
                  \'BucketName\': \'string\',
                  \'CompressionType\': \'none\'|\'gzip\'
              },
              DmsTransferSettings={
                  \'ServiceAccessRoleArn\': \'string\',
                  \'BucketName\': \'string\'
              },
              MongoDbSettings={
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
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
        
        :type EndpointIdentifier: string
        :param EndpointIdentifier: 
        
          The database endpoint identifier. Identifiers must begin with a letter; must contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two consecutive hyphens.
        
        :type EndpointType: string
        :param EndpointType: 
        
          The type of endpoint.
        
        :type EngineName: string
        :param EngineName: 
        
          The type of engine for the endpoint. Valid values, depending on the EndPointType, include mysql, oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase, sybase, dynamodb, mongodb, and sqlserver.
        
        :type Username: string
        :param Username: 
        
          The user name to be used to login to the endpoint database.
        
        :type Password: string
        :param Password: 
        
          The password to be used to login to the endpoint database.
        
        :type ServerName: string
        :param ServerName: 
        
          The name of the server where the endpoint database resides.
        
        :type Port: integer
        :param Port: 
        
          The port used by the endpoint database.
        
        :type DatabaseName: string
        :param DatabaseName: 
        
          The name of the endpoint database.
        
        :type ExtraConnectionAttributes: string
        :param ExtraConnectionAttributes: 
        
          Additional attributes associated with the connection. To reset this parameter, pass the empty string (\"\") as an argument.
        
        :type CertificateArn: string
        :param CertificateArn: 
        
          The Amazon Resource Name (ARN) of the certificate used for SSL connection.
        
        :type SslMode: string
        :param SslMode: 
        
          The SSL mode to be used.
        
          SSL mode can be one of four values: none, require, verify-ca, verify-full. 
        
          The default value is none.
        
        :type ServiceAccessRoleArn: string
        :param ServiceAccessRoleArn: 
        
          The Amazon Resource Name (ARN) for the service access role you want to use to modify the endpoint. 
        
        :type ExternalTableDefinition: string
        :param ExternalTableDefinition: 
        
          The external table definition.
        
        :type DynamoDbSettings: dict
        :param DynamoDbSettings: 
        
          Settings in JSON format for the target Amazon DynamoDB endpoint. For more information about the available settings, see the **Using Object Mapping to Migrate Data to DynamoDB** section at `Using an Amazon DynamoDB Database as a Target for AWS Database Migration Service <http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html>`__ . 
        
          - **ServiceAccessRoleArn** *(string) --* **[REQUIRED]** 
        
            The Amazon Resource Name (ARN) used by the service access IAM role. 
        
        :type S3Settings: dict
        :param S3Settings: 
        
          Settings in JSON format for the target S3 endpoint. For more information about the available settings, see the **Extra Connection Attributes** section at `Using Amazon S3 as a Target for AWS Database Migration Service <http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html>`__ . 
        
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
        
        :type DmsTransferSettings: dict
        :param DmsTransferSettings: 
        
          The settings in JSON format for the DMS Transfer type source endpoint. 
        
          Attributes include:
        
          * serviceAccessRoleArn - The IAM role that has permission to access the Amazon S3 bucket. 
           
          * BucketName - The name of the S3 bucket to use. 
           
          * compressionType - An optional parameter to use GZIP to compress the target files. Set to NONE (the default) or do not use to leave the files uncompressed. 
           
          Shorthand syntax: ServiceAccessRoleArn=string ,BucketName=string,CompressionType=string
        
          JSON syntax:
        
          { \"ServiceAccessRoleArn\": \"string\", \"BucketName\": \"string\", \"CompressionType\": \"none\"|\"gzip\" } 
        
          - **ServiceAccessRoleArn** *(string) --* 
        
            The IAM role that has permission to access the Amazon S3 bucket. 
        
          - **BucketName** *(string) --* 
        
            The name of the S3 bucket to use. 
        
        :type MongoDbSettings: dict
        :param MongoDbSettings: 
        
          Settings in JSON format for the source MongoDB endpoint. For more information about the available settings, see the **Configuration Properties When Using MongoDB as a Source for AWS Database Migration Service** section at `Using Amazon S3 as a Target for AWS Database Migration Service <http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html>`__ . 
        
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
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Endpoint\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Endpoint** *(dict) --* 
        
              The modified endpoint.
        
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
        
        """
        pass

    def modify_event_subscription(self, SubscriptionName: str, SnsTopicArn: str = None, SourceType: str = None, EventCategories: List = None, Enabled: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ModifyEventSubscription>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_event_subscription(
              SubscriptionName=\'string\',
              SnsTopicArn=\'string\',
              SourceType=\'string\',
              EventCategories=[
                  \'string\',
              ],
              Enabled=True|False
          )
        :type SubscriptionName: string
        :param SubscriptionName: **[REQUIRED]** 
        
          The name of the AWS DMS event notification subscription to be modified.
        
        :type SnsTopicArn: string
        :param SnsTopicArn: 
        
          The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
        
        :type SourceType: string
        :param SourceType: 
        
          The type of AWS DMS resource that generates the events you want to subscribe to. 
        
          Valid values: replication-instance | migration-task
        
        :type EventCategories: list
        :param EventCategories: 
        
          A list of event categories for a source type that you want to subscribe to. Use the ``DescribeEventCategories`` action to see a list of event categories. 
        
          - *(string) --* 
        
        :type Enabled: boolean
        :param Enabled: 
        
          A Boolean value; set to **true** to activate the subscription. 
        
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
                    \'SubscriptionCreationTime\': \'string\',
                    \'SourceType\': \'string\',
                    \'SourceIdsList\': [
                        \'string\',
                    ],
                    \'EventCategoriesList\': [
                        \'string\',
                    ],
                    \'Enabled\': True|False
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **EventSubscription** *(dict) --* 
        
              The modified event subscription.
        
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
        
        """
        pass

    def modify_replication_instance(self, ReplicationInstanceArn: str, AllocatedStorage: int = None, ApplyImmediately: bool = None, ReplicationInstanceClass: str = None, VpcSecurityGroupIds: List = None, PreferredMaintenanceWindow: str = None, MultiAZ: bool = None, EngineVersion: str = None, AllowMajorVersionUpgrade: bool = None, AutoMinorVersionUpgrade: bool = None, ReplicationInstanceIdentifier: str = None) -> Dict:
        """
        
        Some settings are applied during the maintenance window.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ModifyReplicationInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_replication_instance(
              ReplicationInstanceArn=\'string\',
              AllocatedStorage=123,
              ApplyImmediately=True|False,
              ReplicationInstanceClass=\'string\',
              VpcSecurityGroupIds=[
                  \'string\',
              ],
              PreferredMaintenanceWindow=\'string\',
              MultiAZ=True|False,
              EngineVersion=\'string\',
              AllowMajorVersionUpgrade=True|False,
              AutoMinorVersionUpgrade=True|False,
              ReplicationInstanceIdentifier=\'string\'
          )
        :type ReplicationInstanceArn: string
        :param ReplicationInstanceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the replication instance.
        
        :type AllocatedStorage: integer
        :param AllocatedStorage: 
        
          The amount of storage (in gigabytes) to be allocated for the replication instance.
        
        :type ApplyImmediately: boolean
        :param ApplyImmediately: 
        
          Indicates whether the changes should be applied immediately or during the next maintenance window.
        
        :type ReplicationInstanceClass: string
        :param ReplicationInstanceClass: 
        
          The compute and memory capacity of the replication instance.
        
          Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``  
        
        :type VpcSecurityGroupIds: list
        :param VpcSecurityGroupIds: 
        
          Specifies the VPC security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance. 
        
          - *(string) --* 
        
        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow: 
        
          The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter does not result in an outage, except in the following situation, and the change is asynchronously applied as soon as possible. If moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure pending changes are applied.
        
          Default: Uses existing setting
        
          Format: ddd:hh24:mi-ddd:hh24:mi
        
          Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun
        
          Constraints: Must be at least 30 minutes
        
        :type MultiAZ: boolean
        :param MultiAZ: 
        
          Specifies if the replication instance is a Multi-AZ deployment. You cannot set the ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` . 
        
        :type EngineVersion: string
        :param EngineVersion: 
        
          The engine version number of the replication instance.
        
        :type AllowMajorVersionUpgrade: boolean
        :param AllowMajorVersionUpgrade: 
        
          Indicates that major version upgrades are allowed. Changing this parameter does not result in an outage and the change is asynchronously applied as soon as possible.
        
          Constraints: This parameter must be set to true when specifying a value for the ``EngineVersion`` parameter that is a different major version than the replication instance\'s current version.
        
        :type AutoMinorVersionUpgrade: boolean
        :param AutoMinorVersionUpgrade: 
        
          Indicates that minor version upgrades will be applied automatically to the replication instance during the maintenance window. Changing this parameter does not result in an outage except in the following case and the change is asynchronously applied as soon as possible. An outage will result if this parameter is set to ``true`` during the maintenance window, and a newer minor version is available, and AWS DMS has enabled auto patching for that engine version. 
        
        :type ReplicationInstanceIdentifier: string
        :param ReplicationInstanceIdentifier: 
        
          The replication instance identifier. This parameter is stored as a lowercase string.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ReplicationInstance\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ReplicationInstance** *(dict) --* 
        
              The modified replication instance.
        
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
        
        """
        pass

    def modify_replication_subnet_group(self, ReplicationSubnetGroupIdentifier: str, SubnetIds: List, ReplicationSubnetGroupDescription: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ModifyReplicationSubnetGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_replication_subnet_group(
              ReplicationSubnetGroupIdentifier=\'string\',
              ReplicationSubnetGroupDescription=\'string\',
              SubnetIds=[
                  \'string\',
              ]
          )
        :type ReplicationSubnetGroupIdentifier: string
        :param ReplicationSubnetGroupIdentifier: **[REQUIRED]** 
        
          The name of the replication instance subnet group.
        
        :type ReplicationSubnetGroupDescription: string
        :param ReplicationSubnetGroupDescription: 
        
          The description of the replication instance subnet group.
        
        :type SubnetIds: list
        :param SubnetIds: **[REQUIRED]** 
        
          A list of subnet IDs.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ReplicationSubnetGroup** *(dict) --* 
        
              The modified replication subnet group.
        
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
        
        """
        pass

    def modify_replication_task(self, ReplicationTaskArn: str, ReplicationTaskIdentifier: str = None, MigrationType: str = None, TableMappings: str = None, ReplicationTaskSettings: str = None, CdcStartTime: datetime = None, CdcStartPosition: str = None, CdcStopPosition: str = None) -> Dict:
        """
        
        You can\'t modify the task endpoints. The task must be stopped before you can modify it. 
        
        For more information about AWS DMS tasks, see the AWS DMS user guide at `Working with Migration Tasks <http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html>`__  
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ModifyReplicationTask>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_replication_task(
              ReplicationTaskArn=\'string\',
              ReplicationTaskIdentifier=\'string\',
              MigrationType=\'full-load\'|\'cdc\'|\'full-load-and-cdc\',
              TableMappings=\'string\',
              ReplicationTaskSettings=\'string\',
              CdcStartTime=datetime(2015, 1, 1),
              CdcStartPosition=\'string\',
              CdcStopPosition=\'string\'
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the replication task.
        
        :type ReplicationTaskIdentifier: string
        :param ReplicationTaskIdentifier: 
        
          The replication task identifier.
        
          Constraints:
        
          * Must contain from 1 to 255 alphanumeric characters or hyphens. 
           
          * First character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
        :type MigrationType: string
        :param MigrationType: 
        
          The migration type.
        
          Valid values: full-load | cdc | full-load-and-cdc
        
        :type TableMappings: string
        :param TableMappings: 
        
          When using the AWS CLI or boto3, provide the path of the JSON file that contains the table mappings. Precede the path with \"file://\". When working with the DMS API, provide the JSON as the parameter value.
        
          For example, --table-mappings file://mappingfile.json
        
        :type ReplicationTaskSettings: string
        :param ReplicationTaskSettings: 
        
          JSON file that contains settings for the task, such as target metadata settings.
        
        :type CdcStartTime: datetime
        :param CdcStartTime: 
        
          Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or CdcStartPosition to specify when you want a CDC operation to start. Specifying both values results in an error.
        
          Timestamp Example: --cdc-start-time “2018-03-08T12:12:12”
        
        :type CdcStartPosition: string
        :param CdcStartPosition: 
        
          Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results in an error.
        
          The value can be in date, checkpoint, or LSN/SCN format.
        
          Date Example: --cdc-start-position “2018-03-08T12:12:12”
        
          Checkpoint Example: --cdc-start-position \"checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93\"
        
          LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”
        
        :type CdcStopPosition: string
        :param CdcStopPosition: 
        
          Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
        
          Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”
        
          Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12 “
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ReplicationTask\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ReplicationTask** *(dict) --* 
        
              The replication task that was modified.
        
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
        
        """
        pass

    def reboot_replication_instance(self, ReplicationInstanceArn: str, ForceFailover: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/RebootReplicationInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.reboot_replication_instance(
              ReplicationInstanceArn=\'string\',
              ForceFailover=True|False
          )
        :type ReplicationInstanceArn: string
        :param ReplicationInstanceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the replication instance.
        
        :type ForceFailover: boolean
        :param ForceFailover: 
        
          If this parameter is ``true`` , the reboot is conducted through a Multi-AZ failover. (If the instance isn\'t configured for Multi-AZ, then you can\'t specify ``true`` .)
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ReplicationInstance\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ReplicationInstance** *(dict) --* 
        
              The replication instance that is being rebooted. 
        
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
        
        """
        pass

    def refresh_schemas(self, EndpointArn: str, ReplicationInstanceArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/RefreshSchemas>`_
        
        **Request Syntax** 
        ::
        
          response = client.refresh_schemas(
              EndpointArn=\'string\',
              ReplicationInstanceArn=\'string\'
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
        
        :type ReplicationInstanceArn: string
        :param ReplicationInstanceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the replication instance.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RefreshSchemasStatus\': {
                    \'EndpointArn\': \'string\',
                    \'ReplicationInstanceArn\': \'string\',
                    \'Status\': \'successful\'|\'failed\'|\'refreshing\',
                    \'LastRefreshDate\': datetime(2015, 1, 1),
                    \'LastFailureMessage\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **RefreshSchemasStatus** *(dict) --* 
        
              The status of the refreshed schema.
        
              - **EndpointArn** *(string) --* 
        
                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
        
              - **ReplicationInstanceArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the replication instance.
        
              - **Status** *(string) --* 
        
                The status of the schema.
        
              - **LastRefreshDate** *(datetime) --* 
        
                The date the schema was last refreshed.
        
              - **LastFailureMessage** *(string) --* 
        
                The last failure message for the schema.
        
        """
        pass

    def reload_tables(self, ReplicationTaskArn: str, TablesToReload: List, ReloadOption: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ReloadTables>`_
        
        **Request Syntax** 
        ::
        
          response = client.reload_tables(
              ReplicationTaskArn=\'string\',
              TablesToReload=[
                  {
                      \'SchemaName\': \'string\',
                      \'TableName\': \'string\'
                  },
              ],
              ReloadOption=\'data-reload\'|\'validate-only\'
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the replication task. 
        
        :type TablesToReload: list
        :param TablesToReload: **[REQUIRED]** 
        
          The name and schema of the table to be reloaded. 
        
          - *(dict) --* 
        
            - **SchemaName** *(string) --* 
        
              The schema name of the table to be reloaded.
        
            - **TableName** *(string) --* 
        
              The table name of the table to be reloaded.
        
        :type ReloadOption: string
        :param ReloadOption: 
        
          Options for reload. Specify ``data-reload`` to reload the data and re-validate it if validation is enabled. Specify ``validate-only`` to re-validate the table. This option applies only when validation is enabled for the task. 
        
          Valid values: data-reload, validate-only
        
          Default value is data-reload.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ReplicationTaskArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ReplicationTaskArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the replication task. 
        
        """
        pass

    def remove_tags_from_resource(self, ResourceArn: str, TagKeys: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/RemoveTagsFromResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.remove_tags_from_resource(
              ResourceArn=\'string\',
              TagKeys=[
                  \'string\',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** 
        
          >The Amazon Resource Name (ARN) of the AWS DMS resource the tag is to be removed from.
        
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** 
        
          The tag key (name) of the tag to be removed.
        
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

    def start_replication_task(self, ReplicationTaskArn: str, StartReplicationTaskType: str, CdcStartTime: datetime = None, CdcStartPosition: str = None, CdcStopPosition: str = None) -> Dict:
        """
        
        For more information about AWS DMS tasks, see the AWS DMS user guide at `Working with Migration Tasks <http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html>`__  
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/StartReplicationTask>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_replication_task(
              ReplicationTaskArn=\'string\',
              StartReplicationTaskType=\'start-replication\'|\'resume-processing\'|\'reload-target\',
              CdcStartTime=datetime(2015, 1, 1),
              CdcStartPosition=\'string\',
              CdcStopPosition=\'string\'
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the replication task to be started.
        
        :type StartReplicationTaskType: string
        :param StartReplicationTaskType: **[REQUIRED]** 
        
          The type of replication task.
        
        :type CdcStartTime: datetime
        :param CdcStartTime: 
        
          Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or CdcStartPosition to specify when you want a CDC operation to start. Specifying both values results in an error.
        
          Timestamp Example: --cdc-start-time “2018-03-08T12:12:12”
        
        :type CdcStartPosition: string
        :param CdcStartPosition: 
        
          Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results in an error.
        
          The value can be in date, checkpoint, or LSN/SCN format.
        
          Date Example: --cdc-start-position “2018-03-08T12:12:12”
        
          Checkpoint Example: --cdc-start-position \"checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93\"
        
          LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”
        
        :type CdcStopPosition: string
        :param CdcStopPosition: 
        
          Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
        
          Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”
        
          Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12 “
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ReplicationTask\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ReplicationTask** *(dict) --* 
        
              The replication task started.
        
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
        
        """
        pass

    def start_replication_task_assessment(self, ReplicationTaskArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/StartReplicationTaskAssessment>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_replication_task_assessment(
              ReplicationTaskArn=\'string\'
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the replication task. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ReplicationTask\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ReplicationTask** *(dict) --* 
        
              The assessed replication task. 
        
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
        
        """
        pass

    def stop_replication_task(self, ReplicationTaskArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/StopReplicationTask>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_replication_task(
              ReplicationTaskArn=\'string\'
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn: **[REQUIRED]** 
        
          The Amazon Resource Name(ARN) of the replication task to be stopped.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ReplicationTask\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **ReplicationTask** *(dict) --* 
        
              The replication task stopped.
        
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
        
        """
        pass

    def test_connection(self, ReplicationInstanceArn: str, EndpointArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/TestConnection>`_
        
        **Request Syntax** 
        ::
        
          response = client.test_connection(
              ReplicationInstanceArn=\'string\',
              EndpointArn=\'string\'
          )
        :type ReplicationInstanceArn: string
        :param ReplicationInstanceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the replication instance.
        
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Connection\': {
                    \'ReplicationInstanceArn\': \'string\',
                    \'EndpointArn\': \'string\',
                    \'Status\': \'string\',
                    \'LastFailureMessage\': \'string\',
                    \'EndpointIdentifier\': \'string\',
                    \'ReplicationInstanceIdentifier\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Connection** *(dict) --* 
        
              The connection tested.
        
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
        
        """
        pass
