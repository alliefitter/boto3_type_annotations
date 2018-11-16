from typing import Dict
from botocore.paginate import Paginator


class ListAliases(Paginator):
    def paginate(self, FunctionName: str, FunctionVersion: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListAliases>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              FunctionName=\'string\',
              FunctionVersion=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type FunctionVersion: string
        :param FunctionVersion: 
        
          If you specify this optional parameter, the API returns only the aliases that are pointing to the specific Lambda function version, otherwise the API returns all of the aliases created for the Lambda function.
        
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
                \'Aliases\': [
                    {
                        \'AliasArn\': \'string\',
                        \'Name\': \'string\',
                        \'FunctionVersion\': \'string\',
                        \'Description\': \'string\',
                        \'RoutingConfig\': {
                            \'AdditionalVersionWeights\': {
                                \'string\': 123.0
                            }
                        },
                        \'RevisionId\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Aliases** *(list) --* 
        
              A list of aliases.
        
              - *(dict) --* 
        
                Provides configuration information about a Lambda function version alias.
        
                - **AliasArn** *(string) --* 
        
                  Lambda function ARN that is qualified using the alias name as the suffix. For example, if you create an alias called ``BETA`` that points to a helloworld function version, the ARN is ``arn:aws:lambda:aws-regions:acct-id:function:helloworld:BETA`` .
        
                - **Name** *(string) --* 
        
                  Alias name.
        
                - **FunctionVersion** *(string) --* 
        
                  Function version to which the alias points.
        
                - **Description** *(string) --* 
        
                  Alias description.
        
                - **RoutingConfig** *(dict) --* 
        
                  Specifies an additional function versions the alias points to, allowing you to dictate what percentage of traffic will invoke each version.
        
                  - **AdditionalVersionWeights** *(dict) --* 
        
                    The name of the second alias, and the percentage of traffic that is routed to it.
        
                    - *(string) --* 
                      
                      - *(float) --* 
                
                - **RevisionId** *(string) --* 
        
                  Represents the latest updated revision of the function or alias.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListEventSourceMappings(Paginator):
    def paginate(self, EventSourceArn: str = None, FunctionName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListEventSourceMappings>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              EventSourceArn=\'string\',
              FunctionName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type EventSourceArn: string
        :param EventSourceArn: 
        
          The Amazon Resource Name (ARN) of the Amazon Kinesis or DynamoDB stream. (This parameter is optional.)
        
        :type FunctionName: string
        :param FunctionName: 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Version or Alias ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD`` . 
           
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'EventSourceMappings\': [
                    {
                        \'UUID\': \'string\',
                        \'BatchSize\': 123,
                        \'EventSourceArn\': \'string\',
                        \'FunctionArn\': \'string\',
                        \'LastModified\': datetime(2015, 1, 1),
                        \'LastProcessingResult\': \'string\',
                        \'State\': \'string\',
                        \'StateTransitionReason\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains a list of event sources (see  EventSourceMappingConfiguration )
        
            - **EventSourceMappings** *(list) --* 
        
              An array of ``EventSourceMappingConfiguration`` objects.
        
              - *(dict) --* 
        
                Describes mapping between an Amazon Kinesis or DynamoDB stream and a Lambda function.
        
                - **UUID** *(string) --* 
        
                  The AWS Lambda assigned opaque identifier for the mapping.
        
                - **BatchSize** *(integer) --* 
        
                  The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records.
        
                - **EventSourceArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the Amazon Kinesis or DynamoDB stream that is the source of events.
        
                - **FunctionArn** *(string) --* 
        
                  The Lambda function to invoke when AWS Lambda detects an event on the poll-based source.
        
                - **LastModified** *(datetime) --* 
        
                  The UTC time string indicating the last time the event mapping was updated.
        
                - **LastProcessingResult** *(string) --* 
        
                  The result of the last AWS Lambda invocation of your Lambda function. This value will be null if an SQS queue is the event source.
        
                - **State** *(string) --* 
        
                  The state of the event source mapping. It can be ``Creating`` , ``Enabled`` , ``Disabled`` , ``Enabling`` , ``Disabling`` , ``Updating`` , or ``Deleting`` .
        
                - **StateTransitionReason** *(string) --* 
        
                  The reason the event source mapping is in its current state. It is either user-requested or an AWS Lambda-initiated state transition.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListFunctions(Paginator):
    def paginate(self, MasterRegion: str = None, FunctionVersion: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListFunctions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              MasterRegion=\'string\',
              FunctionVersion=\'ALL\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type MasterRegion: string
        :param MasterRegion: 
        
          Specify a region (e.g. ``us-east-2`` ) to only list functions that were created in that region, or ``ALL`` to include functions replicated from any region. If specified, you also must specify the ``FunctionVersion`` .
        
        :type FunctionVersion: string
        :param FunctionVersion: 
        
          Set to ``ALL`` to list all published versions. If not specified, only the latest unpublished version ARN is returned.
        
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
                \'Functions\': [
                    {
                        \'FunctionName\': \'string\',
                        \'FunctionArn\': \'string\',
                        \'Runtime\': \'nodejs\'|\'nodejs4.3\'|\'nodejs6.10\'|\'nodejs8.10\'|\'java8\'|\'python2.7\'|\'python3.6\'|\'dotnetcore1.0\'|\'dotnetcore2.0\'|\'dotnetcore2.1\'|\'nodejs4.3-edge\'|\'go1.x\',
                        \'Role\': \'string\',
                        \'Handler\': \'string\',
                        \'CodeSize\': 123,
                        \'Description\': \'string\',
                        \'Timeout\': 123,
                        \'MemorySize\': 123,
                        \'LastModified\': \'string\',
                        \'CodeSha256\': \'string\',
                        \'Version\': \'string\',
                        \'VpcConfig\': {
                            \'SubnetIds\': [
                                \'string\',
                            ],
                            \'SecurityGroupIds\': [
                                \'string\',
                            ],
                            \'VpcId\': \'string\'
                        },
                        \'DeadLetterConfig\': {
                            \'TargetArn\': \'string\'
                        },
                        \'Environment\': {
                            \'Variables\': {
                                \'string\': \'string\'
                            },
                            \'Error\': {
                                \'ErrorCode\': \'string\',
                                \'Message\': \'string\'
                            }
                        },
                        \'KMSKeyArn\': \'string\',
                        \'TracingConfig\': {
                            \'Mode\': \'Active\'|\'PassThrough\'
                        },
                        \'MasterArn\': \'string\',
                        \'RevisionId\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            A list of Lambda functions.
        
            - **Functions** *(list) --* 
        
              A list of Lambda functions.
        
              - *(dict) --* 
        
                A Lambda function\'s configuration settings.
        
                - **FunctionName** *(string) --* 
        
                  The name of the function.
        
                - **FunctionArn** *(string) --* 
        
                  The function\'s Amazon Resource Name.
        
                - **Runtime** *(string) --* 
        
                  The runtime environment for the Lambda function.
        
                - **Role** *(string) --* 
        
                  The function\'s execution role.
        
                - **Handler** *(string) --* 
        
                  The function Lambda calls to begin executing your function.
        
                - **CodeSize** *(integer) --* 
        
                  The size of the function\'s deployment package in bytes.
        
                - **Description** *(string) --* 
        
                  The function\'s description.
        
                - **Timeout** *(integer) --* 
        
                  The amount of time that Lambda allows a function to run before terminating it.
        
                - **MemorySize** *(integer) --* 
        
                  The memory allocated to the function
        
                - **LastModified** *(string) --* 
        
                  The date and time that the function was last updated, in `ISO-8601 format <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ssTZD).
        
                - **CodeSha256** *(string) --* 
        
                  The SHA256 hash of the function\'s deployment package.
        
                - **Version** *(string) --* 
        
                  The version of the Lambda function.
        
                - **VpcConfig** *(dict) --* 
        
                  The function\'s networking configuration.
        
                  - **SubnetIds** *(list) --* 
        
                    A list of VPC subnet IDs.
        
                    - *(string) --* 
                
                  - **SecurityGroupIds** *(list) --* 
        
                    A list of VPC security groups IDs.
        
                    - *(string) --* 
                
                  - **VpcId** *(string) --* 
        
                    The ID of the VPC.
        
                - **DeadLetterConfig** *(dict) --* 
        
                  The function\'s dead letter queue.
        
                  - **TargetArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
        
                - **Environment** *(dict) --* 
        
                  The function\'s environment variables.
        
                  - **Variables** *(dict) --* 
        
                    Environment variable key-value pairs.
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
                  - **Error** *(dict) --* 
        
                    Error messages for environment variables that could not be applied.
        
                    - **ErrorCode** *(string) --* 
        
                      The error code.
        
                    - **Message** *(string) --* 
        
                      The error message.
        
                - **KMSKeyArn** *(string) --* 
        
                  The KMS key used to encrypt the function\'s environment variables. Only returned if you\'ve configured a customer managed CMK.
        
                - **TracingConfig** *(dict) --* 
        
                  The function\'s AWS X-Ray tracing configuration.
        
                  - **Mode** *(string) --* 
        
                    The tracing mode.
        
                - **MasterArn** *(string) --* 
        
                  The ARN of the master function.
        
                - **RevisionId** *(string) --* 
        
                  Represents the latest updated revision of the function or alias.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
