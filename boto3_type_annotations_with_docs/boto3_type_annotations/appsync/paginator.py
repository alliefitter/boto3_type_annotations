from typing import Dict
from botocore.paginate import Paginator


class ListApiKeys(Paginator):
    def paginate(self, apiId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppSync.Client.list_api_keys`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListApiKeys>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              apiId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
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


class ListDataSources(Paginator):
    def paginate(self, apiId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppSync.Client.list_data_sources`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListDataSources>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              apiId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
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


class ListFunctions(Paginator):
    def paginate(self, apiId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppSync.Client.list_functions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListFunctions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              apiId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The GraphQL API ID.
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


class ListGraphqlApis(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppSync.Client.list_graphql_apis`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListGraphqlApis>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListResolvers(Paginator):
    def paginate(self, apiId: str, typeName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppSync.Client.list_resolvers`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListResolvers>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              apiId='string',
              typeName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type typeName: string
        :param typeName: **[REQUIRED]**
          The type name.
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


class ListResolversByFunction(Paginator):
    def paginate(self, apiId: str, functionId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppSync.Client.list_resolvers_by_function`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListResolversByFunction>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              apiId='string',
              functionId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type functionId: string
        :param functionId: **[REQUIRED]**
          The Function ID.
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


class ListTypes(Paginator):
    def paginate(self, apiId: str, format: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AppSync.Client.list_types`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListTypes>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              apiId='string',
              format='SDL'|'JSON',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type apiId: string
        :param apiId: **[REQUIRED]**
          The API ID.
        :type format: string
        :param format: **[REQUIRED]**
          The type format: SDL or JSON.
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
