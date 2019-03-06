from typing import Dict
from botocore.paginate import Paginator


class ListAliases(Paginator):
    def paginate(self, FunctionName: str, FunctionVersion: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lambda.Client.list_aliases`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListAliases>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              FunctionName='string',
              FunctionVersion='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Aliases': [
                    {
                        'AliasArn': 'string',
                        'Name': 'string',
                        'FunctionVersion': 'string',
                        'Description': 'string',
                        'RoutingConfig': {
                            'AdditionalVersionWeights': {
                                'string': 123.0
                            }
                        },
                        'RevisionId': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Aliases** *(list) --* 
              A list of aliases.
              - *(dict) --* 
                Provides configuration information about a Lambda function `alias <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .
                - **AliasArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the alias.
                - **Name** *(string) --* 
                  The name of the alias.
                - **FunctionVersion** *(string) --* 
                  The function version that the alias invokes.
                - **Description** *(string) --* 
                  A description of the alias.
                - **RoutingConfig** *(dict) --* 
                  The `routing configuration <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__ of the alias.
                  - **AdditionalVersionWeights** *(dict) --* 
                    The name of the second alias, and the percentage of traffic that's routed to it.
                    - *(string) --* 
                      - *(float) --* 
                - **RevisionId** *(string) --* 
                  A unique identifier that changes when you update the alias.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**
          The name of the Lambda function.
           **Name formats**
          * **Function name** - ``MyFunction`` .
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` .
          * **Partial ARN** - ``123456789012:function:MyFunction`` .
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        :type FunctionVersion: string
        :param FunctionVersion:
          Specify a function version to only list aliases that invoke that version.
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


class ListEventSourceMappings(Paginator):
    def paginate(self, EventSourceArn: str = None, FunctionName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lambda.Client.list_event_source_mappings`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListEventSourceMappings>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              EventSourceArn='string',
              FunctionName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'EventSourceMappings': [
                    {
                        'UUID': 'string',
                        'BatchSize': 123,
                        'EventSourceArn': 'string',
                        'FunctionArn': 'string',
                        'LastModified': datetime(2015, 1, 1),
                        'LastProcessingResult': 'string',
                        'State': 'string',
                        'StateTransitionReason': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EventSourceMappings** *(list) --* 
              A list of event source mappings.
              - *(dict) --* 
                A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping for details.
                - **UUID** *(string) --* 
                  The identifier of the event source mapping.
                - **BatchSize** *(integer) --* 
                  The maximum number of items to retrieve in a single batch.
                - **EventSourceArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the event source.
                - **FunctionArn** *(string) --* 
                  The ARN of the Lambda function.
                - **LastModified** *(datetime) --* 
                  The date that the event source mapping was last updated.
                - **LastProcessingResult** *(string) --* 
                  The result of the last AWS Lambda invocation of your Lambda function.
                - **State** *(string) --* 
                  The state of the event source mapping. It can be one of the following: ``Creating`` , ``Enabling`` , ``Enabled`` , ``Disabling`` , ``Disabled`` , ``Updating`` , or ``Deleting`` .
                - **StateTransitionReason** *(string) --* 
                  The cause of the last state change, either ``User initiated`` or ``Lambda initiated`` .
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type EventSourceArn: string
        :param EventSourceArn:
          The Amazon Resource Name (ARN) of the event source.
          * **Amazon Kinesis** - The ARN of the data stream or a stream consumer.
          * **Amazon DynamoDB Streams** - The ARN of the stream.
          * **Amazon Simple Queue Service** - The ARN of the queue.
        :type FunctionName: string
        :param FunctionName:
          The name of the Lambda function.
           **Name formats**
          * **Function name** - ``MyFunction`` .
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` .
          * **Version or Alias ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD`` .
          * **Partial ARN** - ``123456789012:function:MyFunction`` .
          The length constraint applies only to the full ARN. If you specify only the function name, it\'s limited to 64 characters in length.
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
    def paginate(self, MasterRegion: str = None, FunctionVersion: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lambda.Client.list_functions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListFunctions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              MasterRegion='string',
              FunctionVersion='ALL',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Functions': [
                    {
                        'FunctionName': 'string',
                        'FunctionArn': 'string',
                        'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
                        'Role': 'string',
                        'Handler': 'string',
                        'CodeSize': 123,
                        'Description': 'string',
                        'Timeout': 123,
                        'MemorySize': 123,
                        'LastModified': 'string',
                        'CodeSha256': 'string',
                        'Version': 'string',
                        'VpcConfig': {
                            'SubnetIds': [
                                'string',
                            ],
                            'SecurityGroupIds': [
                                'string',
                            ],
                            'VpcId': 'string'
                        },
                        'DeadLetterConfig': {
                            'TargetArn': 'string'
                        },
                        'Environment': {
                            'Variables': {
                                'string': 'string'
                            },
                            'Error': {
                                'ErrorCode': 'string',
                                'Message': 'string'
                            }
                        },
                        'KMSKeyArn': 'string',
                        'TracingConfig': {
                            'Mode': 'Active'|'PassThrough'
                        },
                        'MasterArn': 'string',
                        'RevisionId': 'string',
                        'Layers': [
                            {
                                'Arn': 'string',
                                'CodeSize': 123
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            A list of Lambda functions.
            - **Functions** *(list) --* 
              A list of Lambda functions.
              - *(dict) --* 
                Details about a function's configuration.
                - **FunctionName** *(string) --* 
                  The name of the function.
                - **FunctionArn** *(string) --* 
                  The function's Amazon Resource Name (ARN).
                - **Runtime** *(string) --* 
                  The runtime environment for the Lambda function.
                - **Role** *(string) --* 
                  The function's execution role.
                - **Handler** *(string) --* 
                  The function that Lambda calls to begin executing your function.
                - **CodeSize** *(integer) --* 
                  The size of the function's deployment package, in bytes.
                - **Description** *(string) --* 
                  The function's description.
                - **Timeout** *(integer) --* 
                  The amount of time that Lambda allows a function to run before stopping it.
                - **MemorySize** *(integer) --* 
                  The memory that's allocated to the function.
                - **LastModified** *(string) --* 
                  The date and time that the function was last updated, in `ISO-8601 format <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).
                - **CodeSha256** *(string) --* 
                  The SHA256 hash of the function's deployment package.
                - **Version** *(string) --* 
                  The version of the Lambda function.
                - **VpcConfig** *(dict) --* 
                  The function's networking configuration.
                  - **SubnetIds** *(list) --* 
                    A list of VPC subnet IDs.
                    - *(string) --* 
                  - **SecurityGroupIds** *(list) --* 
                    A list of VPC security groups IDs.
                    - *(string) --* 
                  - **VpcId** *(string) --* 
                    The ID of the VPC.
                - **DeadLetterConfig** *(dict) --* 
                  The function's dead letter queue.
                  - **TargetArn** *(string) --* 
                    The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
                - **Environment** *(dict) --* 
                  The function's environment variables.
                  - **Variables** *(dict) --* 
                    Environment variable key-value pairs.
                    - *(string) --* 
                      - *(string) --* 
                  - **Error** *(dict) --* 
                    Error messages for environment variables that couldn't be applied.
                    - **ErrorCode** *(string) --* 
                      The error code.
                    - **Message** *(string) --* 
                      The error message.
                - **KMSKeyArn** *(string) --* 
                  The KMS key that's used to encrypt the function's environment variables. This key is only returned if you've configured a customer-managed CMK.
                - **TracingConfig** *(dict) --* 
                  The function's AWS X-Ray tracing configuration.
                  - **Mode** *(string) --* 
                    The tracing mode.
                - **MasterArn** *(string) --* 
                  For Lambda@Edge functions, the ARN of the master function.
                - **RevisionId** *(string) --* 
                  The latest updated revision of the function or alias.
                - **Layers** *(list) --* 
                  The function's `layers <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .
                  - *(dict) --* 
                    An `AWS Lambda layer <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .
                    - **Arn** *(string) --* 
                      The Amazon Resource Name (ARN) of the function layer.
                    - **CodeSize** *(integer) --* 
                      The size of the layer archive in bytes.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type MasterRegion: string
        :param MasterRegion:
          For Lambda@Edge functions, the AWS Region of the master function. For example, ``us-east-2`` or ``ALL`` . If specified, you must set ``FunctionVersion`` to ``ALL`` .
        :type FunctionVersion: string
        :param FunctionVersion:
          Set to ``ALL`` to include entries for all published versions of each function.
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


class ListLayerVersions(Paginator):
    def paginate(self, LayerName: str, CompatibleRuntime: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lambda.Client.list_layer_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListLayerVersions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              CompatibleRuntime='nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
              LayerName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'LayerVersions': [
                    {
                        'LayerVersionArn': 'string',
                        'Version': 123,
                        'Description': 'string',
                        'CreatedDate': 'string',
                        'CompatibleRuntimes': [
                            'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
                        ],
                        'LicenseInfo': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LayerVersions** *(list) --* 
              A list of versions.
              - *(dict) --* 
                Details about a version of an `AWS Lambda layer <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .
                - **LayerVersionArn** *(string) --* 
                  The ARN of the layer version.
                - **Version** *(integer) --* 
                  The version number.
                - **Description** *(string) --* 
                  The description of the version.
                - **CreatedDate** *(string) --* 
                  The date that the version was created, in ISO 8601 format. For example, ``2018-11-27T15:10:45.123+0000`` .
                - **CompatibleRuntimes** *(list) --* 
                  The layer's compatible runtimes.
                  - *(string) --* 
                - **LicenseInfo** *(string) --* 
                  The layer's open-source license.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type CompatibleRuntime: string
        :param CompatibleRuntime:
          A runtime identifier. For example, ``go1.x`` .
        :type LayerName: string
        :param LayerName: **[REQUIRED]**
          The name or Amazon Resource Name (ARN) of the layer.
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


class ListLayers(Paginator):
    def paginate(self, CompatibleRuntime: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lambda.Client.list_layers`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListLayers>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              CompatibleRuntime='nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Layers': [
                    {
                        'LayerName': 'string',
                        'LayerArn': 'string',
                        'LatestMatchingVersion': {
                            'LayerVersionArn': 'string',
                            'Version': 123,
                            'Description': 'string',
                            'CreatedDate': 'string',
                            'CompatibleRuntimes': [
                                'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
                            ],
                            'LicenseInfo': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Layers** *(list) --* 
              A list of function layers.
              - *(dict) --* 
                Details about an `AWS Lambda layer <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .
                - **LayerName** *(string) --* 
                  The name of the layer.
                - **LayerArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the function layer.
                - **LatestMatchingVersion** *(dict) --* 
                  The newest version of the layer.
                  - **LayerVersionArn** *(string) --* 
                    The ARN of the layer version.
                  - **Version** *(integer) --* 
                    The version number.
                  - **Description** *(string) --* 
                    The description of the version.
                  - **CreatedDate** *(string) --* 
                    The date that the version was created, in ISO 8601 format. For example, ``2018-11-27T15:10:45.123+0000`` .
                  - **CompatibleRuntimes** *(list) --* 
                    The layer's compatible runtimes.
                    - *(string) --* 
                  - **LicenseInfo** *(string) --* 
                    The layer's open-source license.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type CompatibleRuntime: string
        :param CompatibleRuntime:
          A runtime identifier. For example, ``go1.x`` .
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


class ListVersionsByFunction(Paginator):
    def paginate(self, FunctionName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Lambda.Client.list_versions_by_function`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListVersionsByFunction>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              FunctionName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Versions': [
                    {
                        'FunctionName': 'string',
                        'FunctionArn': 'string',
                        'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
                        'Role': 'string',
                        'Handler': 'string',
                        'CodeSize': 123,
                        'Description': 'string',
                        'Timeout': 123,
                        'MemorySize': 123,
                        'LastModified': 'string',
                        'CodeSha256': 'string',
                        'Version': 'string',
                        'VpcConfig': {
                            'SubnetIds': [
                                'string',
                            ],
                            'SecurityGroupIds': [
                                'string',
                            ],
                            'VpcId': 'string'
                        },
                        'DeadLetterConfig': {
                            'TargetArn': 'string'
                        },
                        'Environment': {
                            'Variables': {
                                'string': 'string'
                            },
                            'Error': {
                                'ErrorCode': 'string',
                                'Message': 'string'
                            }
                        },
                        'KMSKeyArn': 'string',
                        'TracingConfig': {
                            'Mode': 'Active'|'PassThrough'
                        },
                        'MasterArn': 'string',
                        'RevisionId': 'string',
                        'Layers': [
                            {
                                'Arn': 'string',
                                'CodeSize': 123
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Versions** *(list) --* 
              A list of Lambda function versions.
              - *(dict) --* 
                Details about a function's configuration.
                - **FunctionName** *(string) --* 
                  The name of the function.
                - **FunctionArn** *(string) --* 
                  The function's Amazon Resource Name (ARN).
                - **Runtime** *(string) --* 
                  The runtime environment for the Lambda function.
                - **Role** *(string) --* 
                  The function's execution role.
                - **Handler** *(string) --* 
                  The function that Lambda calls to begin executing your function.
                - **CodeSize** *(integer) --* 
                  The size of the function's deployment package, in bytes.
                - **Description** *(string) --* 
                  The function's description.
                - **Timeout** *(integer) --* 
                  The amount of time that Lambda allows a function to run before stopping it.
                - **MemorySize** *(integer) --* 
                  The memory that's allocated to the function.
                - **LastModified** *(string) --* 
                  The date and time that the function was last updated, in `ISO-8601 format <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).
                - **CodeSha256** *(string) --* 
                  The SHA256 hash of the function's deployment package.
                - **Version** *(string) --* 
                  The version of the Lambda function.
                - **VpcConfig** *(dict) --* 
                  The function's networking configuration.
                  - **SubnetIds** *(list) --* 
                    A list of VPC subnet IDs.
                    - *(string) --* 
                  - **SecurityGroupIds** *(list) --* 
                    A list of VPC security groups IDs.
                    - *(string) --* 
                  - **VpcId** *(string) --* 
                    The ID of the VPC.
                - **DeadLetterConfig** *(dict) --* 
                  The function's dead letter queue.
                  - **TargetArn** *(string) --* 
                    The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
                - **Environment** *(dict) --* 
                  The function's environment variables.
                  - **Variables** *(dict) --* 
                    Environment variable key-value pairs.
                    - *(string) --* 
                      - *(string) --* 
                  - **Error** *(dict) --* 
                    Error messages for environment variables that couldn't be applied.
                    - **ErrorCode** *(string) --* 
                      The error code.
                    - **Message** *(string) --* 
                      The error message.
                - **KMSKeyArn** *(string) --* 
                  The KMS key that's used to encrypt the function's environment variables. This key is only returned if you've configured a customer-managed CMK.
                - **TracingConfig** *(dict) --* 
                  The function's AWS X-Ray tracing configuration.
                  - **Mode** *(string) --* 
                    The tracing mode.
                - **MasterArn** *(string) --* 
                  For Lambda@Edge functions, the ARN of the master function.
                - **RevisionId** *(string) --* 
                  The latest updated revision of the function or alias.
                - **Layers** *(list) --* 
                  The function's `layers <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .
                  - *(dict) --* 
                    An `AWS Lambda layer <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .
                    - **Arn** *(string) --* 
                      The Amazon Resource Name (ARN) of the function layer.
                    - **CodeSize** *(integer) --* 
                      The size of the layer archive in bytes.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**
          The name of the Lambda function.
           **Name formats**
          * **Function name** - ``MyFunction`` .
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` .
          * **Partial ARN** - ``123456789012:function:MyFunction`` .
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
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
