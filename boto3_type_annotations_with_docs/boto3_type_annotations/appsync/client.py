from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Union


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

    def create_api_key(self, apiId: str, description: str = None, expires: int = None) -> Dict:
        """
        Creates a unique key that you can distribute to clients who are executing your API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/CreateApiKey>`_
        
        **Request Syntax**
        ::
          response = client.create_api_key(
              apiId='string',
              description='string',
              expires=123
          )
        
        **Response Syntax**
        ::
            {
                'apiKey': {
                    'id': 'string',
                    'description': 'string',
                    'expires': 123
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **apiKey** *(dict) --* 
              The API key.
              - **id** *(string) --* 
                The API key ID.
              - **description** *(string) --* 
                A description of the purpose of the API key.
              - **expires** *(integer) --* 
                The time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The ID for your GraphQL API.
        :type description: string
        :param description:
          A description of the purpose of the API key.
        :type expires: integer
        :param expires:
          The time from creation time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour. The default value for this parameter is 7 days from creation time. For more information, see .
        :rtype: dict
        :returns:
        """
        pass

    def create_data_source(self, apiId: str, name: str, type: str, description: str = None, serviceRoleArn: str = None, dynamodbConfig: Dict = None, lambdaConfig: Dict = None, elasticsearchConfig: Dict = None, httpConfig: Dict = None, relationalDatabaseConfig: Dict = None) -> Dict:
        """
        Creates a ``DataSource`` object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/CreateDataSource>`_
        
        **Request Syntax**
        ::
          response = client.create_data_source(
              apiId='string',
              name='string',
              description='string',
              type='AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
              serviceRoleArn='string',
              dynamodbConfig={
                  'tableName': 'string',
                  'awsRegion': 'string',
                  'useCallerCredentials': True|False
              },
              lambdaConfig={
                  'lambdaFunctionArn': 'string'
              },
              elasticsearchConfig={
                  'endpoint': 'string',
                  'awsRegion': 'string'
              },
              httpConfig={
                  'endpoint': 'string',
                  'authorizationConfig': {
                      'authorizationType': 'AWS_IAM',
                      'awsIamConfig': {
                          'signingRegion': 'string',
                          'signingServiceName': 'string'
                      }
                  }
              },
              relationalDatabaseConfig={
                  'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
                  'rdsHttpEndpointConfig': {
                      'awsRegion': 'string',
                      'dbClusterIdentifier': 'string',
                      'databaseName': 'string',
                      'schema': 'string',
                      'awsSecretStoreArn': 'string'
                  }
              }
          )
        
        **Response Syntax**
        ::
            {
                'dataSource': {
                    'dataSourceArn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
                    'serviceRoleArn': 'string',
                    'dynamodbConfig': {
                        'tableName': 'string',
                        'awsRegion': 'string',
                        'useCallerCredentials': True|False
                    },
                    'lambdaConfig': {
                        'lambdaFunctionArn': 'string'
                    },
                    'elasticsearchConfig': {
                        'endpoint': 'string',
                        'awsRegion': 'string'
                    },
                    'httpConfig': {
                        'endpoint': 'string',
                        'authorizationConfig': {
                            'authorizationType': 'AWS_IAM',
                            'awsIamConfig': {
                                'signingRegion': 'string',
                                'signingServiceName': 'string'
                            }
                        }
                    },
                    'relationalDatabaseConfig': {
                        'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
                        'rdsHttpEndpointConfig': {
                            'awsRegion': 'string',
                            'dbClusterIdentifier': 'string',
                            'databaseName': 'string',
                            'schema': 'string',
                            'awsSecretStoreArn': 'string'
                        }
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **dataSource** *(dict) --* 
              The ``DataSource`` object.
              - **dataSourceArn** *(string) --* 
                The data source ARN.
              - **name** *(string) --* 
                The name of the data source.
              - **description** *(string) --* 
                The description of the data source.
              - **type** *(string) --* 
                The type of the data source.
                * **AMAZON_DYNAMODB** : The data source is an Amazon DynamoDB table. 
                * **AMAZON_ELASTICSEARCH** : The data source is an Amazon Elasticsearch Service domain. 
                * **AWS_LAMBDA** : The data source is an AWS Lambda function. 
                * **NONE** : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation. 
                * **HTTP** : The data source is an HTTP endpoint. 
                * **RELATIONAL_DATABASE** : The data source is a relational database. 
              - **serviceRoleArn** *(string) --* 
                The AWS IAM service role ARN for the data source. The system assumes this role when accessing the data source.
              - **dynamodbConfig** *(dict) --* 
                Amazon DynamoDB settings.
                - **tableName** *(string) --* 
                  The table name.
                - **awsRegion** *(string) --* 
                  The AWS Region.
                - **useCallerCredentials** *(boolean) --* 
                  Set to TRUE to use Amazon Cognito credentials with this data source.
              - **lambdaConfig** *(dict) --* 
                AWS Lambda settings.
                - **lambdaFunctionArn** *(string) --* 
                  The ARN for the Lambda function.
              - **elasticsearchConfig** *(dict) --* 
                Amazon Elasticsearch Service settings.
                - **endpoint** *(string) --* 
                  The endpoint.
                - **awsRegion** *(string) --* 
                  The AWS Region.
              - **httpConfig** *(dict) --* 
                HTTP endpoint settings.
                - **endpoint** *(string) --* 
                  The HTTP URL endpoint. You can either specify the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If the port is not specified, AWS AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.
                - **authorizationConfig** *(dict) --* 
                  The authorization config in case the HTTP endpoint requires authorization.
                  - **authorizationType** *(string) --* 
                    The authorization type required by the HTTP endpoint.
                    * **AWS_IAM** : The authorization type is Sigv4. 
                  - **awsIamConfig** *(dict) --* 
                    The AWS IAM settings.
                    - **signingRegion** *(string) --* 
                      The signing region for AWS IAM authorization.
                    - **signingServiceName** *(string) --* 
                      The signing service name for AWS IAM authorization.
              - **relationalDatabaseConfig** *(dict) --* 
                Relational database settings.
                - **relationalDatabaseSourceType** *(string) --* 
                  Source type for the relational database.
                  * **RDS_HTTP_ENDPOINT** : The relational database source type is an Amazon RDS HTTP endpoint. 
                - **rdsHttpEndpointConfig** *(dict) --* 
                  Amazon RDS HTTP endpoint settings.
                  - **awsRegion** *(string) --* 
                    AWS Region for RDS HTTP endpoint.
                  - **dbClusterIdentifier** *(string) --* 
                    Amazon RDS cluster identifier.
                  - **databaseName** *(string) --* 
                    Logical database name.
                  - **schema** *(string) --* 
                    Logical schema name.
                  - **awsSecretStoreArn** *(string) --* 
                    AWS secret store ARN for database credentials.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID for the GraphQL API for the ``DataSource`` .
        :type name: string
        :param name: **[REQUIRED]**
          A user-supplied name for the ``DataSource`` .
        :type description: string
        :param description:
          A description of the ``DataSource`` .
        :type type: string
        :param type: **[REQUIRED]**
          The type of the ``DataSource`` .
        :type serviceRoleArn: string
        :param serviceRoleArn:
          The AWS IAM service role ARN for the data source. The system assumes this role when accessing the data source.
        :type dynamodbConfig: dict
        :param dynamodbConfig:
          Amazon DynamoDB settings.
          - **tableName** *(string) --* **[REQUIRED]**
            The table name.
          - **awsRegion** *(string) --* **[REQUIRED]**
            The AWS Region.
          - **useCallerCredentials** *(boolean) --*
            Set to TRUE to use Amazon Cognito credentials with this data source.
        :type lambdaConfig: dict
        :param lambdaConfig:
          AWS Lambda settings.
          - **lambdaFunctionArn** *(string) --* **[REQUIRED]**
            The ARN for the Lambda function.
        :type elasticsearchConfig: dict
        :param elasticsearchConfig:
          Amazon Elasticsearch Service settings.
          - **endpoint** *(string) --* **[REQUIRED]**
            The endpoint.
          - **awsRegion** *(string) --* **[REQUIRED]**
            The AWS Region.
        :type httpConfig: dict
        :param httpConfig:
          HTTP endpoint settings.
          - **endpoint** *(string) --*
            The HTTP URL endpoint. You can either specify the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If the port is not specified, AWS AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.
          - **authorizationConfig** *(dict) --*
            The authorization config in case the HTTP endpoint requires authorization.
            - **authorizationType** *(string) --* **[REQUIRED]**
              The authorization type required by the HTTP endpoint.
              * **AWS_IAM** : The authorization type is Sigv4.
            - **awsIamConfig** *(dict) --*
              The AWS IAM settings.
              - **signingRegion** *(string) --*
                The signing region for AWS IAM authorization.
              - **signingServiceName** *(string) --*
                The signing service name for AWS IAM authorization.
        :type relationalDatabaseConfig: dict
        :param relationalDatabaseConfig:
          Relational database settings.
          - **relationalDatabaseSourceType** *(string) --*
            Source type for the relational database.
            * **RDS_HTTP_ENDPOINT** : The relational database source type is an Amazon RDS HTTP endpoint.
          - **rdsHttpEndpointConfig** *(dict) --*
            Amazon RDS HTTP endpoint settings.
            - **awsRegion** *(string) --*
              AWS Region for RDS HTTP endpoint.
            - **dbClusterIdentifier** *(string) --*
              Amazon RDS cluster identifier.
            - **databaseName** *(string) --*
              Logical database name.
            - **schema** *(string) --*
              Logical schema name.
            - **awsSecretStoreArn** *(string) --*
              AWS secret store ARN for database credentials.
        :rtype: dict
        :returns:
        """
        pass

    def create_function(self, apiId: str, name: str, dataSourceName: str, requestMappingTemplate: str, functionVersion: str, description: str = None, responseMappingTemplate: str = None) -> Dict:
        """
        Creates a ``Function`` object.
        A function is a reusable entity. Multiple functions can be used to compose the resolver logic.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/CreateFunction>`_
        
        **Request Syntax**
        ::
          response = client.create_function(
              apiId='string',
              name='string',
              description='string',
              dataSourceName='string',
              requestMappingTemplate='string',
              responseMappingTemplate='string',
              functionVersion='string'
          )
        
        **Response Syntax**
        ::
            {
                'functionConfiguration': {
                    'functionId': 'string',
                    'functionArn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'dataSourceName': 'string',
                    'requestMappingTemplate': 'string',
                    'responseMappingTemplate': 'string',
                    'functionVersion': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **functionConfiguration** *(dict) --* 
              The ``Function`` object.
              - **functionId** *(string) --* 
                A unique ID representing the ``Function`` object.
              - **functionArn** *(string) --* 
                The ARN of the ``Function`` object.
              - **name** *(string) --* 
                The name of the ``Function`` object.
              - **description** *(string) --* 
                The ``Function`` description.
              - **dataSourceName** *(string) --* 
                The name of the ``DataSource`` .
              - **requestMappingTemplate** *(string) --* 
                The ``Function`` request mapping template. Functions support only the 2018-05-29 version of the request mapping template.
              - **responseMappingTemplate** *(string) --* 
                The ``Function`` response mapping template.
              - **functionVersion** *(string) --* 
                The version of the request mapping template. Currently only the 2018-05-29 version of the template is supported.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The GraphQL API ID.
        :type name: string
        :param name: **[REQUIRED]**
          The ``Function`` name. The function name does not have to be unique.
        :type description: string
        :param description:
          The ``Function`` description.
        :type dataSourceName: string
        :param dataSourceName: **[REQUIRED]**
          The ``Function``  ``DataSource`` name.
        :type requestMappingTemplate: string
        :param requestMappingTemplate: **[REQUIRED]**
          The ``Function`` request mapping template. Functions support only the 2018-05-29 version of the request mapping template.
        :type responseMappingTemplate: string
        :param responseMappingTemplate:
          The ``Function`` response mapping template.
        :type functionVersion: string
        :param functionVersion: **[REQUIRED]**
          The ``version`` of the request mapping template. Currently the supported value is 2018-05-29.
        :rtype: dict
        :returns:
        """
        pass

    def create_graphql_api(self, name: str, authenticationType: str, logConfig: Dict = None, userPoolConfig: Dict = None, openIDConnectConfig: Dict = None) -> Dict:
        """
        Creates a ``GraphqlApi`` object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/CreateGraphqlApi>`_
        
        **Request Syntax**
        ::
          response = client.create_graphql_api(
              name='string',
              logConfig={
                  'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
                  'cloudWatchLogsRoleArn': 'string'
              },
              authenticationType='API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
              userPoolConfig={
                  'userPoolId': 'string',
                  'awsRegion': 'string',
                  'defaultAction': 'ALLOW'|'DENY',
                  'appIdClientRegex': 'string'
              },
              openIDConnectConfig={
                  'issuer': 'string',
                  'clientId': 'string',
                  'iatTTL': 123,
                  'authTTL': 123
              }
          )
        
        **Response Syntax**
        ::
            {
                'graphqlApi': {
                    'name': 'string',
                    'apiId': 'string',
                    'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
                    'logConfig': {
                        'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
                        'cloudWatchLogsRoleArn': 'string'
                    },
                    'userPoolConfig': {
                        'userPoolId': 'string',
                        'awsRegion': 'string',
                        'defaultAction': 'ALLOW'|'DENY',
                        'appIdClientRegex': 'string'
                    },
                    'openIDConnectConfig': {
                        'issuer': 'string',
                        'clientId': 'string',
                        'iatTTL': 123,
                        'authTTL': 123
                    },
                    'arn': 'string',
                    'uris': {
                        'string': 'string'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **graphqlApi** *(dict) --* 
              The ``GraphqlApi`` .
              - **name** *(string) --* 
                The API name.
              - **apiId** *(string) --* 
                The API ID.
              - **authenticationType** *(string) --* 
                The authentication type.
              - **logConfig** *(dict) --* 
                The Amazon CloudWatch Logs configuration.
                - **fieldLogLevel** *(string) --* 
                  The field logging level. Values can be NONE, ERROR, or ALL. 
                  * **NONE** : No field-level logs are captured. 
                  * **ERROR** : Logs the following information only for the fields that are in error: 
                    * The error section in the server response. 
                    * Field-level errors. 
                    * The generated request/response functions that got resolved for error fields. 
                  * **ALL** : The following information is logged for all fields in the query: 
                    * Field-level tracing information. 
                    * The generated request/response functions that got resolved for each field. 
                - **cloudWatchLogsRoleArn** *(string) --* 
                  The service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account. 
              - **userPoolConfig** *(dict) --* 
                The Amazon Cognito user pool configuration.
                - **userPoolId** *(string) --* 
                  The user pool ID.
                - **awsRegion** *(string) --* 
                  The AWS Region in which the user pool was created.
                - **defaultAction** *(string) --* 
                  The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn't match the Amazon Cognito user pool configuration.
                - **appIdClientRegex** *(string) --* 
                  A regular expression for validating the incoming Amazon Cognito user pool app client ID.
              - **openIDConnectConfig** *(dict) --* 
                The OpenID Connect configuration.
                - **issuer** *(string) --* 
                  The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of ``iss`` in the ID token.
                - **clientId** *(string) --* 
                  The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.
                - **iatTTL** *(integer) --* 
                  The number of milliseconds a token is valid after being issued to a user.
                - **authTTL** *(integer) --* 
                  The number of milliseconds a token is valid after being authenticated.
              - **arn** *(string) --* 
                The ARN.
              - **uris** *(dict) --* 
                The URIs.
                - *(string) --* 
                  - *(string) --* 
        :type name: string
        :param name: **[REQUIRED]**
          A user-supplied name for the ``GraphqlApi`` .
        :type logConfig: dict
        :param logConfig:
          The Amazon CloudWatch Logs configuration.
          - **fieldLogLevel** *(string) --* **[REQUIRED]**
            The field logging level. Values can be NONE, ERROR, or ALL.
            * **NONE** : No field-level logs are captured.
            * **ERROR** : Logs the following information only for the fields that are in error:
              * The error section in the server response.
              * Field-level errors.
              * The generated request/response functions that got resolved for error fields.
            * **ALL** : The following information is logged for all fields in the query:
              * Field-level tracing information.
              * The generated request/response functions that got resolved for each field.
          - **cloudWatchLogsRoleArn** *(string) --* **[REQUIRED]**
            The service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account.
        :type authenticationType: string
        :param authenticationType: **[REQUIRED]**
          The authentication type: API key, AWS IAM, or Amazon Cognito user pools.
        :type userPoolConfig: dict
        :param userPoolConfig:
          The Amazon Cognito user pool configuration.
          - **userPoolId** *(string) --* **[REQUIRED]**
            The user pool ID.
          - **awsRegion** *(string) --* **[REQUIRED]**
            The AWS Region in which the user pool was created.
          - **defaultAction** *(string) --* **[REQUIRED]**
            The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn\'t match the Amazon Cognito user pool configuration.
          - **appIdClientRegex** *(string) --*
            A regular expression for validating the incoming Amazon Cognito user pool app client ID.
        :type openIDConnectConfig: dict
        :param openIDConnectConfig:
          The OpenID Connect configuration.
          - **issuer** *(string) --* **[REQUIRED]**
            The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of ``iss`` in the ID token.
          - **clientId** *(string) --*
            The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.
          - **iatTTL** *(integer) --*
            The number of milliseconds a token is valid after being issued to a user.
          - **authTTL** *(integer) --*
            The number of milliseconds a token is valid after being authenticated.
        :rtype: dict
        :returns:
        """
        pass

    def create_resolver(self, apiId: str, typeName: str, fieldName: str, requestMappingTemplate: str, dataSourceName: str = None, responseMappingTemplate: str = None, kind: str = None, pipelineConfig: Dict = None) -> Dict:
        """
        Creates a ``Resolver`` object.
        A resolver converts incoming requests into a format that a data source can understand and converts the data source's responses into GraphQL.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/CreateResolver>`_
        
        **Request Syntax**
        ::
          response = client.create_resolver(
              apiId='string',
              typeName='string',
              fieldName='string',
              dataSourceName='string',
              requestMappingTemplate='string',
              responseMappingTemplate='string',
              kind='UNIT'|'PIPELINE',
              pipelineConfig={
                  'functions': [
                      'string',
                  ]
              }
          )
        
        **Response Syntax**
        ::
            {
                'resolver': {
                    'typeName': 'string',
                    'fieldName': 'string',
                    'dataSourceName': 'string',
                    'resolverArn': 'string',
                    'requestMappingTemplate': 'string',
                    'responseMappingTemplate': 'string',
                    'kind': 'UNIT'|'PIPELINE',
                    'pipelineConfig': {
                        'functions': [
                            'string',
                        ]
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **resolver** *(dict) --* 
              The ``Resolver`` object.
              - **typeName** *(string) --* 
                The resolver type name.
              - **fieldName** *(string) --* 
                The resolver field name.
              - **dataSourceName** *(string) --* 
                The resolver data source name.
              - **resolverArn** *(string) --* 
                The resolver ARN.
              - **requestMappingTemplate** *(string) --* 
                The request mapping template.
              - **responseMappingTemplate** *(string) --* 
                The response mapping template.
              - **kind** *(string) --* 
                The resolver type.
                * **UNIT** : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source. 
                * **PIPELINE** : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of ``Function`` in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources. 
              - **pipelineConfig** *(dict) --* 
                The ``PipelineConfig`` .
                - **functions** *(list) --* 
                  A list of ``Function`` objects.
                  - *(string) --* 
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The ID for the GraphQL API for which the resolver is being created.
        :type typeName: string
        :param typeName: **[REQUIRED]**
          The name of the ``Type`` .
        :type fieldName: string
        :param fieldName: **[REQUIRED]**
          The name of the field to attach the resolver to.
        :type dataSourceName: string
        :param dataSourceName:
          The name of the data source for which the resolver is being created.
        :type requestMappingTemplate: string
        :param requestMappingTemplate: **[REQUIRED]**
          The mapping template to be used for requests.
          A resolver uses a request mapping template to convert a GraphQL expression into a format that a data source can understand. Mapping templates are written in Apache Velocity Template Language (VTL).
        :type responseMappingTemplate: string
        :param responseMappingTemplate:
          The mapping template to be used for responses from the data source.
        :type kind: string
        :param kind:
          The resolver type.
          * **UNIT** : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
          * **PIPELINE** : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of ``Function`` in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.
        :type pipelineConfig: dict
        :param pipelineConfig:
          The ``PipelineConfig`` .
          - **functions** *(list) --*
            A list of ``Function`` objects.
            - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def create_type(self, apiId: str, definition: str, format: str) -> Dict:
        """
        Creates a ``Type`` object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/CreateType>`_
        
        **Request Syntax**
        ::
          response = client.create_type(
              apiId='string',
              definition='string',
              format='SDL'|'JSON'
          )
        
        **Response Syntax**
        ::
            {
                'type': {
                    'name': 'string',
                    'description': 'string',
                    'arn': 'string',
                    'definition': 'string',
                    'format': 'SDL'|'JSON'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **type** *(dict) --* 
              The ``Type`` object.
              - **name** *(string) --* 
                The type name.
              - **description** *(string) --* 
                The type description.
              - **arn** *(string) --* 
                The type ARN.
              - **definition** *(string) --* 
                The type definition.
              - **format** *(string) --* 
                The type format: SDL or JSON.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type definition: string
        :param definition: **[REQUIRED]**
          The type definition, in GraphQL Schema Definition Language (SDL) format.
          For more information, see the `GraphQL SDL documentation <http://graphql.org/learn/schema/>`__ .
        :type format: string
        :param format: **[REQUIRED]**
          The type format: SDL or JSON.
        :rtype: dict
        :returns:
        """
        pass

    def delete_api_key(self, apiId: str, id: str) -> Dict:
        """
        Deletes an API key.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/DeleteApiKey>`_
        
        **Request Syntax**
        ::
          response = client.delete_api_key(
              apiId='string',
              id='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type id: string
        :param id: **[REQUIRED]**
          The ID for the API key.
        :rtype: dict
        :returns:
        """
        pass

    def delete_data_source(self, apiId: str, name: str) -> Dict:
        """
        Deletes a ``DataSource`` object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/DeleteDataSource>`_
        
        **Request Syntax**
        ::
          response = client.delete_data_source(
              apiId='string',
              name='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type name: string
        :param name: **[REQUIRED]**
          The name of the data source.
        :rtype: dict
        :returns:
        """
        pass

    def delete_function(self, apiId: str, functionId: str) -> Dict:
        """
        Deletes a ``Function`` .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/DeleteFunction>`_
        
        **Request Syntax**
        ::
          response = client.delete_function(
              apiId='string',
              functionId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The GraphQL API ID.
        :type functionId: string
        :param functionId: **[REQUIRED]**
          The ``Function`` ID.
        :rtype: dict
        :returns:
        """
        pass

    def delete_graphql_api(self, apiId: str) -> Dict:
        """
        Deletes a ``GraphqlApi`` object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/DeleteGraphqlApi>`_
        
        **Request Syntax**
        ::
          response = client.delete_graphql_api(
              apiId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :rtype: dict
        :returns:
        """
        pass

    def delete_resolver(self, apiId: str, typeName: str, fieldName: str) -> Dict:
        """
        Deletes a ``Resolver`` object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/DeleteResolver>`_
        
        **Request Syntax**
        ::
          response = client.delete_resolver(
              apiId='string',
              typeName='string',
              fieldName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type typeName: string
        :param typeName: **[REQUIRED]**
          The name of the resolver type.
        :type fieldName: string
        :param fieldName: **[REQUIRED]**
          The resolver field name.
        :rtype: dict
        :returns:
        """
        pass

    def delete_type(self, apiId: str, typeName: str) -> Dict:
        """
        Deletes a ``Type`` object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/DeleteType>`_
        
        **Request Syntax**
        ::
          response = client.delete_type(
              apiId='string',
              typeName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type typeName: string
        :param typeName: **[REQUIRED]**
          The type name.
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

    def get_data_source(self, apiId: str, name: str) -> Dict:
        """
        Retrieves a ``DataSource`` object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/GetDataSource>`_
        
        **Request Syntax**
        ::
          response = client.get_data_source(
              apiId='string',
              name='string'
          )
        
        **Response Syntax**
        ::
            {
                'dataSource': {
                    'dataSourceArn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
                    'serviceRoleArn': 'string',
                    'dynamodbConfig': {
                        'tableName': 'string',
                        'awsRegion': 'string',
                        'useCallerCredentials': True|False
                    },
                    'lambdaConfig': {
                        'lambdaFunctionArn': 'string'
                    },
                    'elasticsearchConfig': {
                        'endpoint': 'string',
                        'awsRegion': 'string'
                    },
                    'httpConfig': {
                        'endpoint': 'string',
                        'authorizationConfig': {
                            'authorizationType': 'AWS_IAM',
                            'awsIamConfig': {
                                'signingRegion': 'string',
                                'signingServiceName': 'string'
                            }
                        }
                    },
                    'relationalDatabaseConfig': {
                        'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
                        'rdsHttpEndpointConfig': {
                            'awsRegion': 'string',
                            'dbClusterIdentifier': 'string',
                            'databaseName': 'string',
                            'schema': 'string',
                            'awsSecretStoreArn': 'string'
                        }
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **dataSource** *(dict) --* 
              The ``DataSource`` object.
              - **dataSourceArn** *(string) --* 
                The data source ARN.
              - **name** *(string) --* 
                The name of the data source.
              - **description** *(string) --* 
                The description of the data source.
              - **type** *(string) --* 
                The type of the data source.
                * **AMAZON_DYNAMODB** : The data source is an Amazon DynamoDB table. 
                * **AMAZON_ELASTICSEARCH** : The data source is an Amazon Elasticsearch Service domain. 
                * **AWS_LAMBDA** : The data source is an AWS Lambda function. 
                * **NONE** : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation. 
                * **HTTP** : The data source is an HTTP endpoint. 
                * **RELATIONAL_DATABASE** : The data source is a relational database. 
              - **serviceRoleArn** *(string) --* 
                The AWS IAM service role ARN for the data source. The system assumes this role when accessing the data source.
              - **dynamodbConfig** *(dict) --* 
                Amazon DynamoDB settings.
                - **tableName** *(string) --* 
                  The table name.
                - **awsRegion** *(string) --* 
                  The AWS Region.
                - **useCallerCredentials** *(boolean) --* 
                  Set to TRUE to use Amazon Cognito credentials with this data source.
              - **lambdaConfig** *(dict) --* 
                AWS Lambda settings.
                - **lambdaFunctionArn** *(string) --* 
                  The ARN for the Lambda function.
              - **elasticsearchConfig** *(dict) --* 
                Amazon Elasticsearch Service settings.
                - **endpoint** *(string) --* 
                  The endpoint.
                - **awsRegion** *(string) --* 
                  The AWS Region.
              - **httpConfig** *(dict) --* 
                HTTP endpoint settings.
                - **endpoint** *(string) --* 
                  The HTTP URL endpoint. You can either specify the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If the port is not specified, AWS AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.
                - **authorizationConfig** *(dict) --* 
                  The authorization config in case the HTTP endpoint requires authorization.
                  - **authorizationType** *(string) --* 
                    The authorization type required by the HTTP endpoint.
                    * **AWS_IAM** : The authorization type is Sigv4. 
                  - **awsIamConfig** *(dict) --* 
                    The AWS IAM settings.
                    - **signingRegion** *(string) --* 
                      The signing region for AWS IAM authorization.
                    - **signingServiceName** *(string) --* 
                      The signing service name for AWS IAM authorization.
              - **relationalDatabaseConfig** *(dict) --* 
                Relational database settings.
                - **relationalDatabaseSourceType** *(string) --* 
                  Source type for the relational database.
                  * **RDS_HTTP_ENDPOINT** : The relational database source type is an Amazon RDS HTTP endpoint. 
                - **rdsHttpEndpointConfig** *(dict) --* 
                  Amazon RDS HTTP endpoint settings.
                  - **awsRegion** *(string) --* 
                    AWS Region for RDS HTTP endpoint.
                  - **dbClusterIdentifier** *(string) --* 
                    Amazon RDS cluster identifier.
                  - **databaseName** *(string) --* 
                    Logical database name.
                  - **schema** *(string) --* 
                    Logical schema name.
                  - **awsSecretStoreArn** *(string) --* 
                    AWS secret store ARN for database credentials.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type name: string
        :param name: **[REQUIRED]**
          The name of the data source.
        :rtype: dict
        :returns:
        """
        pass

    def get_function(self, apiId: str, functionId: str) -> Dict:
        """
        Get a ``Function`` .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/GetFunction>`_
        
        **Request Syntax**
        ::
          response = client.get_function(
              apiId='string',
              functionId='string'
          )
        
        **Response Syntax**
        ::
            {
                'functionConfiguration': {
                    'functionId': 'string',
                    'functionArn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'dataSourceName': 'string',
                    'requestMappingTemplate': 'string',
                    'responseMappingTemplate': 'string',
                    'functionVersion': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **functionConfiguration** *(dict) --* 
              The ``Function`` object.
              - **functionId** *(string) --* 
                A unique ID representing the ``Function`` object.
              - **functionArn** *(string) --* 
                The ARN of the ``Function`` object.
              - **name** *(string) --* 
                The name of the ``Function`` object.
              - **description** *(string) --* 
                The ``Function`` description.
              - **dataSourceName** *(string) --* 
                The name of the ``DataSource`` .
              - **requestMappingTemplate** *(string) --* 
                The ``Function`` request mapping template. Functions support only the 2018-05-29 version of the request mapping template.
              - **responseMappingTemplate** *(string) --* 
                The ``Function`` response mapping template.
              - **functionVersion** *(string) --* 
                The version of the request mapping template. Currently only the 2018-05-29 version of the template is supported.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The GraphQL API ID.
        :type functionId: string
        :param functionId: **[REQUIRED]**
          The ``Function`` ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_graphql_api(self, apiId: str) -> Dict:
        """
        Retrieves a ``GraphqlApi`` object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/GetGraphqlApi>`_
        
        **Request Syntax**
        ::
          response = client.get_graphql_api(
              apiId='string'
          )
        
        **Response Syntax**
        ::
            {
                'graphqlApi': {
                    'name': 'string',
                    'apiId': 'string',
                    'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
                    'logConfig': {
                        'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
                        'cloudWatchLogsRoleArn': 'string'
                    },
                    'userPoolConfig': {
                        'userPoolId': 'string',
                        'awsRegion': 'string',
                        'defaultAction': 'ALLOW'|'DENY',
                        'appIdClientRegex': 'string'
                    },
                    'openIDConnectConfig': {
                        'issuer': 'string',
                        'clientId': 'string',
                        'iatTTL': 123,
                        'authTTL': 123
                    },
                    'arn': 'string',
                    'uris': {
                        'string': 'string'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **graphqlApi** *(dict) --* 
              The ``GraphqlApi`` object.
              - **name** *(string) --* 
                The API name.
              - **apiId** *(string) --* 
                The API ID.
              - **authenticationType** *(string) --* 
                The authentication type.
              - **logConfig** *(dict) --* 
                The Amazon CloudWatch Logs configuration.
                - **fieldLogLevel** *(string) --* 
                  The field logging level. Values can be NONE, ERROR, or ALL. 
                  * **NONE** : No field-level logs are captured. 
                  * **ERROR** : Logs the following information only for the fields that are in error: 
                    * The error section in the server response. 
                    * Field-level errors. 
                    * The generated request/response functions that got resolved for error fields. 
                  * **ALL** : The following information is logged for all fields in the query: 
                    * Field-level tracing information. 
                    * The generated request/response functions that got resolved for each field. 
                - **cloudWatchLogsRoleArn** *(string) --* 
                  The service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account. 
              - **userPoolConfig** *(dict) --* 
                The Amazon Cognito user pool configuration.
                - **userPoolId** *(string) --* 
                  The user pool ID.
                - **awsRegion** *(string) --* 
                  The AWS Region in which the user pool was created.
                - **defaultAction** *(string) --* 
                  The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn't match the Amazon Cognito user pool configuration.
                - **appIdClientRegex** *(string) --* 
                  A regular expression for validating the incoming Amazon Cognito user pool app client ID.
              - **openIDConnectConfig** *(dict) --* 
                The OpenID Connect configuration.
                - **issuer** *(string) --* 
                  The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of ``iss`` in the ID token.
                - **clientId** *(string) --* 
                  The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.
                - **iatTTL** *(integer) --* 
                  The number of milliseconds a token is valid after being issued to a user.
                - **authTTL** *(integer) --* 
                  The number of milliseconds a token is valid after being authenticated.
              - **arn** *(string) --* 
                The ARN.
              - **uris** *(dict) --* 
                The URIs.
                - *(string) --* 
                  - *(string) --* 
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID for the GraphQL API.
        :rtype: dict
        :returns:
        """
        pass

    def get_introspection_schema(self, apiId: str, format: str) -> Dict:
        """
        Retrieves the introspection schema for a GraphQL API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/GetIntrospectionSchema>`_
        
        **Request Syntax**
        ::
          response = client.get_introspection_schema(
              apiId='string',
              format='SDL'|'JSON'
          )
        
        **Response Syntax**
        ::
            {
                'schema': StreamingBody()
            }
        
        **Response Structure**
          - *(dict) --* 
            - **schema** (:class:`.StreamingBody`) -- 
              The schema, in GraphQL Schema Definition Language (SDL) format.
              For more information, see the `GraphQL SDL documentation <http://graphql.org/learn/schema/>`__ .
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type format: string
        :param format: **[REQUIRED]**
          The schema format: SDL or JSON.
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

    def get_resolver(self, apiId: str, typeName: str, fieldName: str) -> Dict:
        """
        Retrieves a ``Resolver`` object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/GetResolver>`_
        
        **Request Syntax**
        ::
          response = client.get_resolver(
              apiId='string',
              typeName='string',
              fieldName='string'
          )
        
        **Response Syntax**
        ::
            {
                'resolver': {
                    'typeName': 'string',
                    'fieldName': 'string',
                    'dataSourceName': 'string',
                    'resolverArn': 'string',
                    'requestMappingTemplate': 'string',
                    'responseMappingTemplate': 'string',
                    'kind': 'UNIT'|'PIPELINE',
                    'pipelineConfig': {
                        'functions': [
                            'string',
                        ]
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **resolver** *(dict) --* 
              The ``Resolver`` object.
              - **typeName** *(string) --* 
                The resolver type name.
              - **fieldName** *(string) --* 
                The resolver field name.
              - **dataSourceName** *(string) --* 
                The resolver data source name.
              - **resolverArn** *(string) --* 
                The resolver ARN.
              - **requestMappingTemplate** *(string) --* 
                The request mapping template.
              - **responseMappingTemplate** *(string) --* 
                The response mapping template.
              - **kind** *(string) --* 
                The resolver type.
                * **UNIT** : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source. 
                * **PIPELINE** : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of ``Function`` in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources. 
              - **pipelineConfig** *(dict) --* 
                The ``PipelineConfig`` .
                - **functions** *(list) --* 
                  A list of ``Function`` objects.
                  - *(string) --* 
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type typeName: string
        :param typeName: **[REQUIRED]**
          The resolver type name.
        :type fieldName: string
        :param fieldName: **[REQUIRED]**
          The resolver field name.
        :rtype: dict
        :returns:
        """
        pass

    def get_schema_creation_status(self, apiId: str) -> Dict:
        """
        Retrieves the current status of a schema creation operation.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/GetSchemaCreationStatus>`_
        
        **Request Syntax**
        ::
          response = client.get_schema_creation_status(
              apiId='string'
          )
        
        **Response Syntax**
        ::
            {
                'status': 'PROCESSING'|'ACTIVE'|'DELETING',
                'details': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **status** *(string) --* 
              The current state of the schema (PROCESSING, ACTIVE, or DELETING). Once the schema is in the ACTIVE state, you can add data.
            - **details** *(string) --* 
              Detailed information about the status of the schema creation operation.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_type(self, apiId: str, typeName: str, format: str) -> Dict:
        """
        Retrieves a ``Type`` object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/GetType>`_
        
        **Request Syntax**
        ::
          response = client.get_type(
              apiId='string',
              typeName='string',
              format='SDL'|'JSON'
          )
        
        **Response Syntax**
        ::
            {
                'type': {
                    'name': 'string',
                    'description': 'string',
                    'arn': 'string',
                    'definition': 'string',
                    'format': 'SDL'|'JSON'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **type** *(dict) --* 
              The ``Type`` object.
              - **name** *(string) --* 
                The type name.
              - **description** *(string) --* 
                The type description.
              - **arn** *(string) --* 
                The type ARN.
              - **definition** *(string) --* 
                The type definition.
              - **format** *(string) --* 
                The type format: SDL or JSON.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type typeName: string
        :param typeName: **[REQUIRED]**
          The type name.
        :type format: string
        :param format: **[REQUIRED]**
          The type format: SDL or JSON.
        :rtype: dict
        :returns:
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

    def list_api_keys(self, apiId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists the API keys for a given API.
        .. note::
          API keys are deleted automatically sometime after they expire. However, they may still be included in the response until they have actually been deleted. You can safely call ``DeleteApiKey`` to manually delete a key before it's automatically deleted.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListApiKeys>`_
        
        **Request Syntax**
        ::
          response = client.list_api_keys(
              apiId='string',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'apiKeys': [
                    {
                        'id': 'string',
                        'description': 'string',
                        'expires': 123
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **apiKeys** *(list) --* 
              The ``ApiKey`` objects.
              - *(dict) --* 
                Describes an API key.
                Customers invoke AWS AppSync GraphQL API operations with API keys as an identity mechanism. There are two key versions:
                 **da1** : This version was introduced at launch in November 2017. These keys always expire after 7 days. Key expiration is managed by Amazon DynamoDB TTL. The keys ceased to be valid after February 21, 2018 and should not be used after that date.
                * ``ListApiKeys`` returns the expiration time in milliseconds. 
                * ``CreateApiKey`` returns the expiration time in milliseconds. 
                * ``UpdateApiKey`` is not available for this key version. 
                * ``DeleteApiKey`` deletes the item from the table. 
                * Expiration is stored in Amazon DynamoDB as milliseconds. This results in a bug where keys are not automatically deleted because DynamoDB expects the TTL to be stored in seconds. As a one-time action, we will delete these keys from the table after February 21, 2018. 
                 **da2** : This version was introduced in February 2018 when AppSync added support to extend key expiration.
                * ``ListApiKeys`` returns the expiration time in seconds. 
                * ``CreateApiKey`` returns the expiration time in seconds and accepts a user-provided expiration time in seconds. 
                * ``UpdateApiKey`` returns the expiration time in seconds and accepts a user-provided expiration time in seconds. Key expiration can only be updated while the key has not expired. 
                * ``DeleteApiKey`` deletes the item from the table. 
                * Expiration is stored in Amazon DynamoDB as seconds. 
                - **id** *(string) --* 
                  The API key ID.
                - **description** *(string) --* 
                  A description of the purpose of the API key.
                - **expires** *(integer) --* 
                  The time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour.
            - **nextToken** *(string) --* 
              An identifier to be passed in the next request to this operation to return the next set of items in the list.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results you want the request to return.
        :rtype: dict
        :returns:
        """
        pass

    def list_data_sources(self, apiId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists the data sources for a given API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListDataSources>`_
        
        **Request Syntax**
        ::
          response = client.list_data_sources(
              apiId='string',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'dataSources': [
                    {
                        'dataSourceArn': 'string',
                        'name': 'string',
                        'description': 'string',
                        'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
                        'serviceRoleArn': 'string',
                        'dynamodbConfig': {
                            'tableName': 'string',
                            'awsRegion': 'string',
                            'useCallerCredentials': True|False
                        },
                        'lambdaConfig': {
                            'lambdaFunctionArn': 'string'
                        },
                        'elasticsearchConfig': {
                            'endpoint': 'string',
                            'awsRegion': 'string'
                        },
                        'httpConfig': {
                            'endpoint': 'string',
                            'authorizationConfig': {
                                'authorizationType': 'AWS_IAM',
                                'awsIamConfig': {
                                    'signingRegion': 'string',
                                    'signingServiceName': 'string'
                                }
                            }
                        },
                        'relationalDatabaseConfig': {
                            'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
                            'rdsHttpEndpointConfig': {
                                'awsRegion': 'string',
                                'dbClusterIdentifier': 'string',
                                'databaseName': 'string',
                                'schema': 'string',
                                'awsSecretStoreArn': 'string'
                            }
                        }
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **dataSources** *(list) --* 
              The ``DataSource`` objects.
              - *(dict) --* 
                Describes a data source.
                - **dataSourceArn** *(string) --* 
                  The data source ARN.
                - **name** *(string) --* 
                  The name of the data source.
                - **description** *(string) --* 
                  The description of the data source.
                - **type** *(string) --* 
                  The type of the data source.
                  * **AMAZON_DYNAMODB** : The data source is an Amazon DynamoDB table. 
                  * **AMAZON_ELASTICSEARCH** : The data source is an Amazon Elasticsearch Service domain. 
                  * **AWS_LAMBDA** : The data source is an AWS Lambda function. 
                  * **NONE** : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation. 
                  * **HTTP** : The data source is an HTTP endpoint. 
                  * **RELATIONAL_DATABASE** : The data source is a relational database. 
                - **serviceRoleArn** *(string) --* 
                  The AWS IAM service role ARN for the data source. The system assumes this role when accessing the data source.
                - **dynamodbConfig** *(dict) --* 
                  Amazon DynamoDB settings.
                  - **tableName** *(string) --* 
                    The table name.
                  - **awsRegion** *(string) --* 
                    The AWS Region.
                  - **useCallerCredentials** *(boolean) --* 
                    Set to TRUE to use Amazon Cognito credentials with this data source.
                - **lambdaConfig** *(dict) --* 
                  AWS Lambda settings.
                  - **lambdaFunctionArn** *(string) --* 
                    The ARN for the Lambda function.
                - **elasticsearchConfig** *(dict) --* 
                  Amazon Elasticsearch Service settings.
                  - **endpoint** *(string) --* 
                    The endpoint.
                  - **awsRegion** *(string) --* 
                    The AWS Region.
                - **httpConfig** *(dict) --* 
                  HTTP endpoint settings.
                  - **endpoint** *(string) --* 
                    The HTTP URL endpoint. You can either specify the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If the port is not specified, AWS AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.
                  - **authorizationConfig** *(dict) --* 
                    The authorization config in case the HTTP endpoint requires authorization.
                    - **authorizationType** *(string) --* 
                      The authorization type required by the HTTP endpoint.
                      * **AWS_IAM** : The authorization type is Sigv4. 
                    - **awsIamConfig** *(dict) --* 
                      The AWS IAM settings.
                      - **signingRegion** *(string) --* 
                        The signing region for AWS IAM authorization.
                      - **signingServiceName** *(string) --* 
                        The signing service name for AWS IAM authorization.
                - **relationalDatabaseConfig** *(dict) --* 
                  Relational database settings.
                  - **relationalDatabaseSourceType** *(string) --* 
                    Source type for the relational database.
                    * **RDS_HTTP_ENDPOINT** : The relational database source type is an Amazon RDS HTTP endpoint. 
                  - **rdsHttpEndpointConfig** *(dict) --* 
                    Amazon RDS HTTP endpoint settings.
                    - **awsRegion** *(string) --* 
                      AWS Region for RDS HTTP endpoint.
                    - **dbClusterIdentifier** *(string) --* 
                      Amazon RDS cluster identifier.
                    - **databaseName** *(string) --* 
                      Logical database name.
                    - **schema** *(string) --* 
                      Logical schema name.
                    - **awsSecretStoreArn** *(string) --* 
                      AWS secret store ARN for database credentials.
            - **nextToken** *(string) --* 
              An identifier to be passed in the next request to this operation to return the next set of items in the list.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results you want the request to return.
        :rtype: dict
        :returns:
        """
        pass

    def list_functions(self, apiId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        List multiple functions.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListFunctions>`_
        
        **Request Syntax**
        ::
          response = client.list_functions(
              apiId='string',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'functions': [
                    {
                        'functionId': 'string',
                        'functionArn': 'string',
                        'name': 'string',
                        'description': 'string',
                        'dataSourceName': 'string',
                        'requestMappingTemplate': 'string',
                        'responseMappingTemplate': 'string',
                        'functionVersion': 'string'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **functions** *(list) --* 
              A list of ``Function`` objects.
              - *(dict) --* 
                A function is a reusable entity. Multiple functions can be used to compose the resolver logic.
                - **functionId** *(string) --* 
                  A unique ID representing the ``Function`` object.
                - **functionArn** *(string) --* 
                  The ARN of the ``Function`` object.
                - **name** *(string) --* 
                  The name of the ``Function`` object.
                - **description** *(string) --* 
                  The ``Function`` description.
                - **dataSourceName** *(string) --* 
                  The name of the ``DataSource`` .
                - **requestMappingTemplate** *(string) --* 
                  The ``Function`` request mapping template. Functions support only the 2018-05-29 version of the request mapping template.
                - **responseMappingTemplate** *(string) --* 
                  The ``Function`` response mapping template.
                - **functionVersion** *(string) --* 
                  The version of the request mapping template. Currently only the 2018-05-29 version of the template is supported.
            - **nextToken** *(string) --* 
              An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The GraphQL API ID.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results you want the request to return.
        :rtype: dict
        :returns:
        """
        pass

    def list_graphql_apis(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists your GraphQL APIs.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListGraphqlApis>`_
        
        **Request Syntax**
        ::
          response = client.list_graphql_apis(
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'graphqlApis': [
                    {
                        'name': 'string',
                        'apiId': 'string',
                        'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
                        'logConfig': {
                            'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
                            'cloudWatchLogsRoleArn': 'string'
                        },
                        'userPoolConfig': {
                            'userPoolId': 'string',
                            'awsRegion': 'string',
                            'defaultAction': 'ALLOW'|'DENY',
                            'appIdClientRegex': 'string'
                        },
                        'openIDConnectConfig': {
                            'issuer': 'string',
                            'clientId': 'string',
                            'iatTTL': 123,
                            'authTTL': 123
                        },
                        'arn': 'string',
                        'uris': {
                            'string': 'string'
                        }
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **graphqlApis** *(list) --* 
              The ``GraphqlApi`` objects.
              - *(dict) --* 
                Describes a GraphQL API.
                - **name** *(string) --* 
                  The API name.
                - **apiId** *(string) --* 
                  The API ID.
                - **authenticationType** *(string) --* 
                  The authentication type.
                - **logConfig** *(dict) --* 
                  The Amazon CloudWatch Logs configuration.
                  - **fieldLogLevel** *(string) --* 
                    The field logging level. Values can be NONE, ERROR, or ALL. 
                    * **NONE** : No field-level logs are captured. 
                    * **ERROR** : Logs the following information only for the fields that are in error: 
                      * The error section in the server response. 
                      * Field-level errors. 
                      * The generated request/response functions that got resolved for error fields. 
                    * **ALL** : The following information is logged for all fields in the query: 
                      * Field-level tracing information. 
                      * The generated request/response functions that got resolved for each field. 
                  - **cloudWatchLogsRoleArn** *(string) --* 
                    The service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account. 
                - **userPoolConfig** *(dict) --* 
                  The Amazon Cognito user pool configuration.
                  - **userPoolId** *(string) --* 
                    The user pool ID.
                  - **awsRegion** *(string) --* 
                    The AWS Region in which the user pool was created.
                  - **defaultAction** *(string) --* 
                    The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn't match the Amazon Cognito user pool configuration.
                  - **appIdClientRegex** *(string) --* 
                    A regular expression for validating the incoming Amazon Cognito user pool app client ID.
                - **openIDConnectConfig** *(dict) --* 
                  The OpenID Connect configuration.
                  - **issuer** *(string) --* 
                    The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of ``iss`` in the ID token.
                  - **clientId** *(string) --* 
                    The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.
                  - **iatTTL** *(integer) --* 
                    The number of milliseconds a token is valid after being issued to a user.
                  - **authTTL** *(integer) --* 
                    The number of milliseconds a token is valid after being authenticated.
                - **arn** *(string) --* 
                  The ARN.
                - **uris** *(dict) --* 
                  The URIs.
                  - *(string) --* 
                    - *(string) --* 
            - **nextToken** *(string) --* 
              An identifier to be passed in the next request to this operation to return the next set of items in the list.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results you want the request to return.
        :rtype: dict
        :returns:
        """
        pass

    def list_resolvers(self, apiId: str, typeName: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists the resolvers for a given API and type.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListResolvers>`_
        
        **Request Syntax**
        ::
          response = client.list_resolvers(
              apiId='string',
              typeName='string',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'resolvers': [
                    {
                        'typeName': 'string',
                        'fieldName': 'string',
                        'dataSourceName': 'string',
                        'resolverArn': 'string',
                        'requestMappingTemplate': 'string',
                        'responseMappingTemplate': 'string',
                        'kind': 'UNIT'|'PIPELINE',
                        'pipelineConfig': {
                            'functions': [
                                'string',
                            ]
                        }
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **resolvers** *(list) --* 
              The ``Resolver`` objects.
              - *(dict) --* 
                Describes a resolver.
                - **typeName** *(string) --* 
                  The resolver type name.
                - **fieldName** *(string) --* 
                  The resolver field name.
                - **dataSourceName** *(string) --* 
                  The resolver data source name.
                - **resolverArn** *(string) --* 
                  The resolver ARN.
                - **requestMappingTemplate** *(string) --* 
                  The request mapping template.
                - **responseMappingTemplate** *(string) --* 
                  The response mapping template.
                - **kind** *(string) --* 
                  The resolver type.
                  * **UNIT** : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source. 
                  * **PIPELINE** : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of ``Function`` in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources. 
                - **pipelineConfig** *(dict) --* 
                  The ``PipelineConfig`` .
                  - **functions** *(list) --* 
                    A list of ``Function`` objects.
                    - *(string) --* 
            - **nextToken** *(string) --* 
              An identifier to be passed in the next request to this operation to return the next set of items in the list.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type typeName: string
        :param typeName: **[REQUIRED]**
          The type name.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results you want the request to return.
        :rtype: dict
        :returns:
        """
        pass

    def list_resolvers_by_function(self, apiId: str, functionId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        List the resolvers that are associated with a specific function.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListResolversByFunction>`_
        
        **Request Syntax**
        ::
          response = client.list_resolvers_by_function(
              apiId='string',
              functionId='string',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'resolvers': [
                    {
                        'typeName': 'string',
                        'fieldName': 'string',
                        'dataSourceName': 'string',
                        'resolverArn': 'string',
                        'requestMappingTemplate': 'string',
                        'responseMappingTemplate': 'string',
                        'kind': 'UNIT'|'PIPELINE',
                        'pipelineConfig': {
                            'functions': [
                                'string',
                            ]
                        }
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **resolvers** *(list) --* 
              The list of resolvers.
              - *(dict) --* 
                Describes a resolver.
                - **typeName** *(string) --* 
                  The resolver type name.
                - **fieldName** *(string) --* 
                  The resolver field name.
                - **dataSourceName** *(string) --* 
                  The resolver data source name.
                - **resolverArn** *(string) --* 
                  The resolver ARN.
                - **requestMappingTemplate** *(string) --* 
                  The request mapping template.
                - **responseMappingTemplate** *(string) --* 
                  The response mapping template.
                - **kind** *(string) --* 
                  The resolver type.
                  * **UNIT** : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source. 
                  * **PIPELINE** : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of ``Function`` in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources. 
                - **pipelineConfig** *(dict) --* 
                  The ``PipelineConfig`` .
                  - **functions** *(list) --* 
                    A list of ``Function`` objects.
                    - *(string) --* 
            - **nextToken** *(string) --* 
              An identifier that can be used to return the next set of items in the list.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type functionId: string
        :param functionId: **[REQUIRED]**
          The Function ID.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results you want the request to return.
        :rtype: dict
        :returns:
        """
        pass

    def list_types(self, apiId: str, format: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists the types for a given API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListTypes>`_
        
        **Request Syntax**
        ::
          response = client.list_types(
              apiId='string',
              format='SDL'|'JSON',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'types': [
                    {
                        'name': 'string',
                        'description': 'string',
                        'arn': 'string',
                        'definition': 'string',
                        'format': 'SDL'|'JSON'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **types** *(list) --* 
              The ``Type`` objects.
              - *(dict) --* 
                Describes a type.
                - **name** *(string) --* 
                  The type name.
                - **description** *(string) --* 
                  The type description.
                - **arn** *(string) --* 
                  The type ARN.
                - **definition** *(string) --* 
                  The type definition.
                - **format** *(string) --* 
                  The type format: SDL or JSON.
            - **nextToken** *(string) --* 
              An identifier to be passed in the next request to this operation to return the next set of items in the list.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type format: string
        :param format: **[REQUIRED]**
          The type format: SDL or JSON.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type maxResults: integer
        :param maxResults:
          The maximum number of results you want the request to return.
        :rtype: dict
        :returns:
        """
        pass

    def start_schema_creation(self, apiId: str, definition: bytes) -> Dict:
        """
        Adds a new schema to your GraphQL API.
        This operation is asynchronous. Use to determine when it has completed.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/StartSchemaCreation>`_
        
        **Request Syntax**
        ::
          response = client.start_schema_creation(
              apiId='string',
              definition=b'bytes'
          )
        
        **Response Syntax**
        ::
            {
                'status': 'PROCESSING'|'ACTIVE'|'DELETING'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **status** *(string) --* 
              The current state of the schema (PROCESSING, ACTIVE, or DELETING). When the schema is in the ACTIVE state, you can add data.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type definition: bytes
        :param definition: **[REQUIRED]**
          The schema definition, in GraphQL schema language format.
        :rtype: dict
        :returns:
        """
        pass

    def update_api_key(self, apiId: str, id: str, description: str = None, expires: int = None) -> Dict:
        """
        Updates an API key.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/UpdateApiKey>`_
        
        **Request Syntax**
        ::
          response = client.update_api_key(
              apiId='string',
              id='string',
              description='string',
              expires=123
          )
        
        **Response Syntax**
        ::
            {
                'apiKey': {
                    'id': 'string',
                    'description': 'string',
                    'expires': 123
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **apiKey** *(dict) --* 
              The API key.
              - **id** *(string) --* 
                The API key ID.
              - **description** *(string) --* 
                A description of the purpose of the API key.
              - **expires** *(integer) --* 
                The time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The ID for the GraphQL API.
        :type id: string
        :param id: **[REQUIRED]**
          The API key ID.
        :type description: string
        :param description:
          A description of the purpose of the API key.
        :type expires: integer
        :param expires:
          The time from update time after which the API key expires. The date is represented as seconds since the epoch. For more information, see .
        :rtype: dict
        :returns:
        """
        pass

    def update_data_source(self, apiId: str, name: str, type: str, description: str = None, serviceRoleArn: str = None, dynamodbConfig: Dict = None, lambdaConfig: Dict = None, elasticsearchConfig: Dict = None, httpConfig: Dict = None, relationalDatabaseConfig: Dict = None) -> Dict:
        """
        Updates a ``DataSource`` object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/UpdateDataSource>`_
        
        **Request Syntax**
        ::
          response = client.update_data_source(
              apiId='string',
              name='string',
              description='string',
              type='AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
              serviceRoleArn='string',
              dynamodbConfig={
                  'tableName': 'string',
                  'awsRegion': 'string',
                  'useCallerCredentials': True|False
              },
              lambdaConfig={
                  'lambdaFunctionArn': 'string'
              },
              elasticsearchConfig={
                  'endpoint': 'string',
                  'awsRegion': 'string'
              },
              httpConfig={
                  'endpoint': 'string',
                  'authorizationConfig': {
                      'authorizationType': 'AWS_IAM',
                      'awsIamConfig': {
                          'signingRegion': 'string',
                          'signingServiceName': 'string'
                      }
                  }
              },
              relationalDatabaseConfig={
                  'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
                  'rdsHttpEndpointConfig': {
                      'awsRegion': 'string',
                      'dbClusterIdentifier': 'string',
                      'databaseName': 'string',
                      'schema': 'string',
                      'awsSecretStoreArn': 'string'
                  }
              }
          )
        
        **Response Syntax**
        ::
            {
                'dataSource': {
                    'dataSourceArn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
                    'serviceRoleArn': 'string',
                    'dynamodbConfig': {
                        'tableName': 'string',
                        'awsRegion': 'string',
                        'useCallerCredentials': True|False
                    },
                    'lambdaConfig': {
                        'lambdaFunctionArn': 'string'
                    },
                    'elasticsearchConfig': {
                        'endpoint': 'string',
                        'awsRegion': 'string'
                    },
                    'httpConfig': {
                        'endpoint': 'string',
                        'authorizationConfig': {
                            'authorizationType': 'AWS_IAM',
                            'awsIamConfig': {
                                'signingRegion': 'string',
                                'signingServiceName': 'string'
                            }
                        }
                    },
                    'relationalDatabaseConfig': {
                        'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
                        'rdsHttpEndpointConfig': {
                            'awsRegion': 'string',
                            'dbClusterIdentifier': 'string',
                            'databaseName': 'string',
                            'schema': 'string',
                            'awsSecretStoreArn': 'string'
                        }
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **dataSource** *(dict) --* 
              The updated ``DataSource`` object.
              - **dataSourceArn** *(string) --* 
                The data source ARN.
              - **name** *(string) --* 
                The name of the data source.
              - **description** *(string) --* 
                The description of the data source.
              - **type** *(string) --* 
                The type of the data source.
                * **AMAZON_DYNAMODB** : The data source is an Amazon DynamoDB table. 
                * **AMAZON_ELASTICSEARCH** : The data source is an Amazon Elasticsearch Service domain. 
                * **AWS_LAMBDA** : The data source is an AWS Lambda function. 
                * **NONE** : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation. 
                * **HTTP** : The data source is an HTTP endpoint. 
                * **RELATIONAL_DATABASE** : The data source is a relational database. 
              - **serviceRoleArn** *(string) --* 
                The AWS IAM service role ARN for the data source. The system assumes this role when accessing the data source.
              - **dynamodbConfig** *(dict) --* 
                Amazon DynamoDB settings.
                - **tableName** *(string) --* 
                  The table name.
                - **awsRegion** *(string) --* 
                  The AWS Region.
                - **useCallerCredentials** *(boolean) --* 
                  Set to TRUE to use Amazon Cognito credentials with this data source.
              - **lambdaConfig** *(dict) --* 
                AWS Lambda settings.
                - **lambdaFunctionArn** *(string) --* 
                  The ARN for the Lambda function.
              - **elasticsearchConfig** *(dict) --* 
                Amazon Elasticsearch Service settings.
                - **endpoint** *(string) --* 
                  The endpoint.
                - **awsRegion** *(string) --* 
                  The AWS Region.
              - **httpConfig** *(dict) --* 
                HTTP endpoint settings.
                - **endpoint** *(string) --* 
                  The HTTP URL endpoint. You can either specify the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If the port is not specified, AWS AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.
                - **authorizationConfig** *(dict) --* 
                  The authorization config in case the HTTP endpoint requires authorization.
                  - **authorizationType** *(string) --* 
                    The authorization type required by the HTTP endpoint.
                    * **AWS_IAM** : The authorization type is Sigv4. 
                  - **awsIamConfig** *(dict) --* 
                    The AWS IAM settings.
                    - **signingRegion** *(string) --* 
                      The signing region for AWS IAM authorization.
                    - **signingServiceName** *(string) --* 
                      The signing service name for AWS IAM authorization.
              - **relationalDatabaseConfig** *(dict) --* 
                Relational database settings.
                - **relationalDatabaseSourceType** *(string) --* 
                  Source type for the relational database.
                  * **RDS_HTTP_ENDPOINT** : The relational database source type is an Amazon RDS HTTP endpoint. 
                - **rdsHttpEndpointConfig** *(dict) --* 
                  Amazon RDS HTTP endpoint settings.
                  - **awsRegion** *(string) --* 
                    AWS Region for RDS HTTP endpoint.
                  - **dbClusterIdentifier** *(string) --* 
                    Amazon RDS cluster identifier.
                  - **databaseName** *(string) --* 
                    Logical database name.
                  - **schema** *(string) --* 
                    Logical schema name.
                  - **awsSecretStoreArn** *(string) --* 
                    AWS secret store ARN for database credentials.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type name: string
        :param name: **[REQUIRED]**
          The new name for the data source.
        :type description: string
        :param description:
          The new description for the data source.
        :type type: string
        :param type: **[REQUIRED]**
          The new data source type.
        :type serviceRoleArn: string
        :param serviceRoleArn:
          The new service role ARN for the data source.
        :type dynamodbConfig: dict
        :param dynamodbConfig:
          The new Amazon DynamoDB configuration.
          - **tableName** *(string) --* **[REQUIRED]**
            The table name.
          - **awsRegion** *(string) --* **[REQUIRED]**
            The AWS Region.
          - **useCallerCredentials** *(boolean) --*
            Set to TRUE to use Amazon Cognito credentials with this data source.
        :type lambdaConfig: dict
        :param lambdaConfig:
          The new AWS Lambda configuration.
          - **lambdaFunctionArn** *(string) --* **[REQUIRED]**
            The ARN for the Lambda function.
        :type elasticsearchConfig: dict
        :param elasticsearchConfig:
          The new Elasticsearch Service configuration.
          - **endpoint** *(string) --* **[REQUIRED]**
            The endpoint.
          - **awsRegion** *(string) --* **[REQUIRED]**
            The AWS Region.
        :type httpConfig: dict
        :param httpConfig:
          The new HTTP endpoint configuration.
          - **endpoint** *(string) --*
            The HTTP URL endpoint. You can either specify the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If the port is not specified, AWS AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.
          - **authorizationConfig** *(dict) --*
            The authorization config in case the HTTP endpoint requires authorization.
            - **authorizationType** *(string) --* **[REQUIRED]**
              The authorization type required by the HTTP endpoint.
              * **AWS_IAM** : The authorization type is Sigv4.
            - **awsIamConfig** *(dict) --*
              The AWS IAM settings.
              - **signingRegion** *(string) --*
                The signing region for AWS IAM authorization.
              - **signingServiceName** *(string) --*
                The signing service name for AWS IAM authorization.
        :type relationalDatabaseConfig: dict
        :param relationalDatabaseConfig:
          The new relational database configuration.
          - **relationalDatabaseSourceType** *(string) --*
            Source type for the relational database.
            * **RDS_HTTP_ENDPOINT** : The relational database source type is an Amazon RDS HTTP endpoint.
          - **rdsHttpEndpointConfig** *(dict) --*
            Amazon RDS HTTP endpoint settings.
            - **awsRegion** *(string) --*
              AWS Region for RDS HTTP endpoint.
            - **dbClusterIdentifier** *(string) --*
              Amazon RDS cluster identifier.
            - **databaseName** *(string) --*
              Logical database name.
            - **schema** *(string) --*
              Logical schema name.
            - **awsSecretStoreArn** *(string) --*
              AWS secret store ARN for database credentials.
        :rtype: dict
        :returns:
        """
        pass

    def update_function(self, apiId: str, name: str, functionId: str, dataSourceName: str, requestMappingTemplate: str, functionVersion: str, description: str = None, responseMappingTemplate: str = None) -> Dict:
        """
        Updates a ``Function`` object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/UpdateFunction>`_
        
        **Request Syntax**
        ::
          response = client.update_function(
              apiId='string',
              name='string',
              description='string',
              functionId='string',
              dataSourceName='string',
              requestMappingTemplate='string',
              responseMappingTemplate='string',
              functionVersion='string'
          )
        
        **Response Syntax**
        ::
            {
                'functionConfiguration': {
                    'functionId': 'string',
                    'functionArn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'dataSourceName': 'string',
                    'requestMappingTemplate': 'string',
                    'responseMappingTemplate': 'string',
                    'functionVersion': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **functionConfiguration** *(dict) --* 
              The ``Function`` object.
              - **functionId** *(string) --* 
                A unique ID representing the ``Function`` object.
              - **functionArn** *(string) --* 
                The ARN of the ``Function`` object.
              - **name** *(string) --* 
                The name of the ``Function`` object.
              - **description** *(string) --* 
                The ``Function`` description.
              - **dataSourceName** *(string) --* 
                The name of the ``DataSource`` .
              - **requestMappingTemplate** *(string) --* 
                The ``Function`` request mapping template. Functions support only the 2018-05-29 version of the request mapping template.
              - **responseMappingTemplate** *(string) --* 
                The ``Function`` response mapping template.
              - **functionVersion** *(string) --* 
                The version of the request mapping template. Currently only the 2018-05-29 version of the template is supported.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The GraphQL API ID.
        :type name: string
        :param name: **[REQUIRED]**
          The ``Function`` name.
        :type description: string
        :param description:
          The ``Function`` description.
        :type functionId: string
        :param functionId: **[REQUIRED]**
          The function ID.
        :type dataSourceName: string
        :param dataSourceName: **[REQUIRED]**
          The ``Function``  ``DataSource`` name.
        :type requestMappingTemplate: string
        :param requestMappingTemplate: **[REQUIRED]**
          The ``Function`` request mapping template. Functions support only the 2018-05-29 version of the request mapping template.
        :type responseMappingTemplate: string
        :param responseMappingTemplate:
          The ``Function`` request mapping template.
        :type functionVersion: string
        :param functionVersion: **[REQUIRED]**
          The ``version`` of the request mapping template. Currently the supported value is 2018-05-29.
        :rtype: dict
        :returns:
        """
        pass

    def update_graphql_api(self, apiId: str, name: str, logConfig: Dict = None, authenticationType: str = None, userPoolConfig: Dict = None, openIDConnectConfig: Dict = None) -> Dict:
        """
        Updates a ``GraphqlApi`` object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/UpdateGraphqlApi>`_
        
        **Request Syntax**
        ::
          response = client.update_graphql_api(
              apiId='string',
              name='string',
              logConfig={
                  'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
                  'cloudWatchLogsRoleArn': 'string'
              },
              authenticationType='API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
              userPoolConfig={
                  'userPoolId': 'string',
                  'awsRegion': 'string',
                  'defaultAction': 'ALLOW'|'DENY',
                  'appIdClientRegex': 'string'
              },
              openIDConnectConfig={
                  'issuer': 'string',
                  'clientId': 'string',
                  'iatTTL': 123,
                  'authTTL': 123
              }
          )
        
        **Response Syntax**
        ::
            {
                'graphqlApi': {
                    'name': 'string',
                    'apiId': 'string',
                    'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
                    'logConfig': {
                        'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
                        'cloudWatchLogsRoleArn': 'string'
                    },
                    'userPoolConfig': {
                        'userPoolId': 'string',
                        'awsRegion': 'string',
                        'defaultAction': 'ALLOW'|'DENY',
                        'appIdClientRegex': 'string'
                    },
                    'openIDConnectConfig': {
                        'issuer': 'string',
                        'clientId': 'string',
                        'iatTTL': 123,
                        'authTTL': 123
                    },
                    'arn': 'string',
                    'uris': {
                        'string': 'string'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **graphqlApi** *(dict) --* 
              The updated ``GraphqlApi`` object.
              - **name** *(string) --* 
                The API name.
              - **apiId** *(string) --* 
                The API ID.
              - **authenticationType** *(string) --* 
                The authentication type.
              - **logConfig** *(dict) --* 
                The Amazon CloudWatch Logs configuration.
                - **fieldLogLevel** *(string) --* 
                  The field logging level. Values can be NONE, ERROR, or ALL. 
                  * **NONE** : No field-level logs are captured. 
                  * **ERROR** : Logs the following information only for the fields that are in error: 
                    * The error section in the server response. 
                    * Field-level errors. 
                    * The generated request/response functions that got resolved for error fields. 
                  * **ALL** : The following information is logged for all fields in the query: 
                    * Field-level tracing information. 
                    * The generated request/response functions that got resolved for each field. 
                - **cloudWatchLogsRoleArn** *(string) --* 
                  The service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account. 
              - **userPoolConfig** *(dict) --* 
                The Amazon Cognito user pool configuration.
                - **userPoolId** *(string) --* 
                  The user pool ID.
                - **awsRegion** *(string) --* 
                  The AWS Region in which the user pool was created.
                - **defaultAction** *(string) --* 
                  The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn't match the Amazon Cognito user pool configuration.
                - **appIdClientRegex** *(string) --* 
                  A regular expression for validating the incoming Amazon Cognito user pool app client ID.
              - **openIDConnectConfig** *(dict) --* 
                The OpenID Connect configuration.
                - **issuer** *(string) --* 
                  The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of ``iss`` in the ID token.
                - **clientId** *(string) --* 
                  The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.
                - **iatTTL** *(integer) --* 
                  The number of milliseconds a token is valid after being issued to a user.
                - **authTTL** *(integer) --* 
                  The number of milliseconds a token is valid after being authenticated.
              - **arn** *(string) --* 
                The ARN.
              - **uris** *(dict) --* 
                The URIs.
                - *(string) --* 
                  - *(string) --* 
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type name: string
        :param name: **[REQUIRED]**
          The new name for the ``GraphqlApi`` object.
        :type logConfig: dict
        :param logConfig:
          The Amazon CloudWatch Logs configuration for the ``GraphqlApi`` object.
          - **fieldLogLevel** *(string) --* **[REQUIRED]**
            The field logging level. Values can be NONE, ERROR, or ALL.
            * **NONE** : No field-level logs are captured.
            * **ERROR** : Logs the following information only for the fields that are in error:
              * The error section in the server response.
              * Field-level errors.
              * The generated request/response functions that got resolved for error fields.
            * **ALL** : The following information is logged for all fields in the query:
              * Field-level tracing information.
              * The generated request/response functions that got resolved for each field.
          - **cloudWatchLogsRoleArn** *(string) --* **[REQUIRED]**
            The service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account.
        :type authenticationType: string
        :param authenticationType:
          The new authentication type for the ``GraphqlApi`` object.
        :type userPoolConfig: dict
        :param userPoolConfig:
          The new Amazon Cognito user pool configuration for the ``GraphqlApi`` object.
          - **userPoolId** *(string) --* **[REQUIRED]**
            The user pool ID.
          - **awsRegion** *(string) --* **[REQUIRED]**
            The AWS Region in which the user pool was created.
          - **defaultAction** *(string) --* **[REQUIRED]**
            The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn\'t match the Amazon Cognito user pool configuration.
          - **appIdClientRegex** *(string) --*
            A regular expression for validating the incoming Amazon Cognito user pool app client ID.
        :type openIDConnectConfig: dict
        :param openIDConnectConfig:
          The OpenID Connect configuration for the ``GraphqlApi`` object.
          - **issuer** *(string) --* **[REQUIRED]**
            The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of ``iss`` in the ID token.
          - **clientId** *(string) --*
            The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.
          - **iatTTL** *(integer) --*
            The number of milliseconds a token is valid after being issued to a user.
          - **authTTL** *(integer) --*
            The number of milliseconds a token is valid after being authenticated.
        :rtype: dict
        :returns:
        """
        pass

    def update_resolver(self, apiId: str, typeName: str, fieldName: str, requestMappingTemplate: str, dataSourceName: str = None, responseMappingTemplate: str = None, kind: str = None, pipelineConfig: Dict = None) -> Dict:
        """
        Updates a ``Resolver`` object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/UpdateResolver>`_
        
        **Request Syntax**
        ::
          response = client.update_resolver(
              apiId='string',
              typeName='string',
              fieldName='string',
              dataSourceName='string',
              requestMappingTemplate='string',
              responseMappingTemplate='string',
              kind='UNIT'|'PIPELINE',
              pipelineConfig={
                  'functions': [
                      'string',
                  ]
              }
          )
        
        **Response Syntax**
        ::
            {
                'resolver': {
                    'typeName': 'string',
                    'fieldName': 'string',
                    'dataSourceName': 'string',
                    'resolverArn': 'string',
                    'requestMappingTemplate': 'string',
                    'responseMappingTemplate': 'string',
                    'kind': 'UNIT'|'PIPELINE',
                    'pipelineConfig': {
                        'functions': [
                            'string',
                        ]
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **resolver** *(dict) --* 
              The updated ``Resolver`` object.
              - **typeName** *(string) --* 
                The resolver type name.
              - **fieldName** *(string) --* 
                The resolver field name.
              - **dataSourceName** *(string) --* 
                The resolver data source name.
              - **resolverArn** *(string) --* 
                The resolver ARN.
              - **requestMappingTemplate** *(string) --* 
                The request mapping template.
              - **responseMappingTemplate** *(string) --* 
                The response mapping template.
              - **kind** *(string) --* 
                The resolver type.
                * **UNIT** : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source. 
                * **PIPELINE** : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of ``Function`` in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources. 
              - **pipelineConfig** *(dict) --* 
                The ``PipelineConfig`` .
                - **functions** *(list) --* 
                  A list of ``Function`` objects.
                  - *(string) --* 
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type typeName: string
        :param typeName: **[REQUIRED]**
          The new type name.
        :type fieldName: string
        :param fieldName: **[REQUIRED]**
          The new field name.
        :type dataSourceName: string
        :param dataSourceName:
          The new data source name.
        :type requestMappingTemplate: string
        :param requestMappingTemplate: **[REQUIRED]**
          The new request mapping template.
        :type responseMappingTemplate: string
        :param responseMappingTemplate:
          The new response mapping template.
        :type kind: string
        :param kind:
          The resolver type.
          * **UNIT** : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
          * **PIPELINE** : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of ``Function`` in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.
        :type pipelineConfig: dict
        :param pipelineConfig:
          The ``PipelineConfig`` .
          - **functions** *(list) --*
            A list of ``Function`` objects.
            - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def update_type(self, apiId: str, typeName: str, format: str, definition: str = None) -> Dict:
        """
        Updates a ``Type`` object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/UpdateType>`_
        
        **Request Syntax**
        ::
          response = client.update_type(
              apiId='string',
              typeName='string',
              definition='string',
              format='SDL'|'JSON'
          )
        
        **Response Syntax**
        ::
            {
                'type': {
                    'name': 'string',
                    'description': 'string',
                    'arn': 'string',
                    'definition': 'string',
                    'format': 'SDL'|'JSON'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **type** *(dict) --* 
              The updated ``Type`` object.
              - **name** *(string) --* 
                The type name.
              - **description** *(string) --* 
                The type description.
              - **arn** *(string) --* 
                The type ARN.
              - **definition** *(string) --* 
                The type definition.
              - **format** *(string) --* 
                The type format: SDL or JSON.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type typeName: string
        :param typeName: **[REQUIRED]**
          The new type name.
        :type definition: string
        :param definition:
          The new definition.
        :type format: string
        :param format: **[REQUIRED]**
          The new type format: SDL or JSON.
        :rtype: dict
        :returns:
        """
        pass
