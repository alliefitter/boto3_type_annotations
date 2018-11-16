from datetime import datetime
from typing import Union
from botocore.paginate import Paginator
from typing import IO
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def add_permission(self, FunctionName: str, StatementId: str, Action: str, Principal: str, SourceArn: str = None, SourceAccount: str = None, EventSourceToken: str = None, Qualifier: str = None, RevisionId: str = None) -> Dict:
        """
        
        Permissions apply to the Amazon Resource Name (ARN) used to invoke the function, which can be unqualified (the unpublished version of the function), or include a version or alias. If a client uses a version or alias to invoke a function, use the ``Qualifier`` parameter to apply permissions to that ARN. For more information about versioning, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 
        
        This operation requires permission for the ``lambda:AddPermission`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/AddPermission>`_
        
        **Request Syntax** 
        ::
        
          response = client.add_permission(
              FunctionName=\'string\',
              StatementId=\'string\',
              Action=\'string\',
              Principal=\'string\',
              SourceArn=\'string\',
              SourceAccount=\'string\',
              EventSourceToken=\'string\',
              Qualifier=\'string\',
              RevisionId=\'string\'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type StatementId: string
        :param StatementId: **[REQUIRED]** 
        
          A unique statement identifier.
        
        :type Action: string
        :param Action: **[REQUIRED]** 
        
          The AWS Lambda action you want to allow in this statement. Each Lambda action is a string starting with ``lambda:`` followed by the API name . For example, ``lambda:CreateFunction`` . You can use wildcard (``lambda:*`` ) to grant permission for all AWS Lambda actions. 
        
        :type Principal: string
        :param Principal: **[REQUIRED]** 
        
          The principal who is getting this permission. The principal can be an AWS service (e.g. ``s3.amazonaws.com`` or ``sns.amazonaws.com`` ) for service triggers, or an account ID for cross-account access. If you specify a service as a principal, use the ``SourceArn`` parameter to limit who can invoke the function through that service.
        
        :type SourceArn: string
        :param SourceArn: 
        
          The Amazon Resource Name of the invoker. 
        
          .. warning::
        
            If you add a permission to a service principal without providing the source ARN, any AWS account that creates a mapping to your function ARN can invoke your Lambda function.
        
        :type SourceAccount: string
        :param SourceAccount: 
        
          This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner. For example, if the ``SourceArn`` identifies a bucket, then this is the bucket owner\'s account ID. You can use this additional condition to ensure the bucket you specify is owned by a specific account (it is possible the bucket owner deleted the bucket and some other AWS account created the bucket). You can also use this condition to specify all sources (that is, you don\'t specify the ``SourceArn`` ) owned by a specific account. 
        
        :type EventSourceToken: string
        :param EventSourceToken: 
        
          A unique token that must be supplied by the principal invoking the function. This is currently only used for Alexa Smart Home functions.
        
        :type Qualifier: string
        :param Qualifier: 
        
          Specify a version or alias to add permissions to a published version of the function.
        
        :type RevisionId: string
        :param RevisionId: 
        
          An optional value you can use to ensure you are updating the latest update of the function version or alias. If the ``RevisionID`` you pass doesn\'t match the latest ``RevisionId`` of the function or alias, it will fail with an error message, advising you to retrieve the latest function version or alias ``RevisionID`` using either  GetFunction or  GetAlias  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Statement\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Statement** *(string) --* 
        
              The permission statement you specified in the request. The response returns the same as a string using a backslash (\"\\") as an escape character in the JSON.
        
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

    def create_alias(self, FunctionName: str, Name: str, FunctionVersion: str, Description: str = None, RoutingConfig: Dict = None) -> Dict:
        """
        
        Alias names are unique for a given function. This requires permission for the lambda:CreateAlias action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/CreateAlias>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_alias(
              FunctionName=\'string\',
              Name=\'string\',
              FunctionVersion=\'string\',
              Description=\'string\',
              RoutingConfig={
                  \'AdditionalVersionWeights\': {
                      \'string\': 123.0
                  }
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
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Name for the alias you are creating.
        
        :type FunctionVersion: string
        :param FunctionVersion: **[REQUIRED]** 
        
          Lambda function version for which you are creating the alias.
        
        :type Description: string
        :param Description: 
        
          Description of the alias.
        
        :type RoutingConfig: dict
        :param RoutingConfig: 
        
          Specifies an additional version your alias can point to, allowing you to dictate what percentage of traffic will invoke each version. For more information, see `Traffic Shifting Using Aliases <http://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__ .
        
          - **AdditionalVersionWeights** *(dict) --* 
        
            The name of the second alias, and the percentage of traffic that is routed to it.
        
            - *(string) --* 
        
              - *(float) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
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
            }
          **Response Structure** 
        
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
        
        """
        pass

    def create_event_source_mapping(self, EventSourceArn: str, FunctionName: str, Enabled: bool = None, BatchSize: int = None, StartingPosition: str = None, StartingPositionTimestamp: datetime = None) -> Dict:
        """
        
        This association between a poll-based source and a Lambda function is called the event source mapping.
        
        You provide mapping information (for example, which stream or SQS queue to read from and which Lambda function to invoke) in the request body.
        
        Amazon Kinesis or DynamoDB stream event sources can be associated with multiple AWS Lambda functions and a given Lambda function can be associated with multiple AWS event sources. For Amazon SQS, you can configure multiple queues as event sources for a single Lambda function, but an SQS queue can be mapped only to a single Lambda function.
        
        You can configure an SQS queue in an account separate from your Lambda function\'s account. Also the queue needs to reside in the same AWS region as your function. 
        
        If you are using versioning, you can specify a specific function version or an alias via the function name parameter. For more information about versioning, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 
        
        This operation requires permission for the ``lambda:CreateEventSourceMapping`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/CreateEventSourceMapping>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_event_source_mapping(
              EventSourceArn=\'string\',
              FunctionName=\'string\',
              Enabled=True|False,
              BatchSize=123,
              StartingPosition=\'TRIM_HORIZON\'|\'LATEST\'|\'AT_TIMESTAMP\',
              StartingPositionTimestamp=datetime(2015, 1, 1)
          )
        :type EventSourceArn: string
        :param EventSourceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the event source.
        
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Version or Alias ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type Enabled: boolean
        :param Enabled: 
        
          Set to false to disable the event source upon creation. 
        
        :type BatchSize: integer
        :param BatchSize: 
        
          The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. The default for Amazon Kinesis and Amazon DynamoDB is 100 records. Both the default and maximum for Amazon SQS are 10 messages.
        
        :type StartingPosition: string
        :param StartingPosition: 
        
          The position in the DynamoDB or Kinesis stream where AWS Lambda should start reading. For more information, see `GetShardIterator <http://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html#Kinesis-GetShardIterator-request-ShardIteratorType>`__ in the *Amazon Kinesis API Reference Guide* or `GetShardIterator <http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetShardIterator.html>`__ in the *Amazon DynamoDB API Reference Guide* . The ``AT_TIMESTAMP`` value is supported only for `Kinesis streams <http://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-streams.html>`__ . 
        
        :type StartingPositionTimestamp: datetime
        :param StartingPositionTimestamp: 
        
          The timestamp of the data record from which to start reading. Used with `shard iterator type <http://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html#Kinesis-GetShardIterator-request-ShardIteratorType>`__ AT_TIMESTAMP. If a record with this exact timestamp does not exist, the iterator returned is for the next (later) record. If the timestamp is older than the current trim horizon, the iterator returned is for the oldest untrimmed data record (TRIM_HORIZON). Valid only for `Kinesis streams <http://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-streams.html>`__ . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UUID\': \'string\',
                \'BatchSize\': 123,
                \'EventSourceArn\': \'string\',
                \'FunctionArn\': \'string\',
                \'LastModified\': datetime(2015, 1, 1),
                \'LastProcessingResult\': \'string\',
                \'State\': \'string\',
                \'StateTransitionReason\': \'string\'
            }
          **Response Structure** 
        
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
        
        """
        pass

    def create_function(self, FunctionName: str, Runtime: str, Role: str, Handler: str, Code: Dict, Description: str = None, Timeout: int = None, MemorySize: int = None, Publish: bool = None, VpcConfig: Dict = None, DeadLetterConfig: Dict = None, Environment: Dict = None, KMSKeyArn: str = None, TracingConfig: Dict = None, Tags: Dict = None) -> Dict:
        """
        
        This operation requires permission for the ``lambda:CreateFunction`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/CreateFunction>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_function(
              FunctionName=\'string\',
              Runtime=\'nodejs\'|\'nodejs4.3\'|\'nodejs6.10\'|\'nodejs8.10\'|\'java8\'|\'python2.7\'|\'python3.6\'|\'dotnetcore1.0\'|\'dotnetcore2.0\'|\'dotnetcore2.1\'|\'nodejs4.3-edge\'|\'go1.x\',
              Role=\'string\',
              Handler=\'string\',
              Code={
                  \'ZipFile\': b\'bytes\',
                  \'S3Bucket\': \'string\',
                  \'S3Key\': \'string\',
                  \'S3ObjectVersion\': \'string\'
              },
              Description=\'string\',
              Timeout=123,
              MemorySize=123,
              Publish=True|False,
              VpcConfig={
                  \'SubnetIds\': [
                      \'string\',
                  ],
                  \'SecurityGroupIds\': [
                      \'string\',
                  ]
              },
              DeadLetterConfig={
                  \'TargetArn\': \'string\'
              },
              Environment={
                  \'Variables\': {
                      \'string\': \'string\'
                  }
              },
              KMSKeyArn=\'string\',
              TracingConfig={
                  \'Mode\': \'Active\'|\'PassThrough\'
              },
              Tags={
                  \'string\': \'string\'
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
        
        :type Runtime: string
        :param Runtime: **[REQUIRED]** 
        
          The runtime version for the function.
        
        :type Role: string
        :param Role: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the function\'s `execution role <http://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html#lambda-intro-execution-role>`__ .
        
        :type Handler: string
        :param Handler: **[REQUIRED]** 
        
          The name of the method within your code that Lambda calls to execute your function. For more information, see `Programming Model <http://docs.aws.amazon.com/lambda/latest/dg/programming-model-v2.html>`__ .
        
        :type Code: dict
        :param Code: **[REQUIRED]** 
        
          The code for the function.
        
          - **ZipFile** *(bytes) --* 
        
            The base64-encoded contents of your zip file containing your deployment package. AWS SDK and AWS CLI clients handle the encoding for you.
        
          - **S3Bucket** *(string) --* 
        
            An Amazon S3 bucket in the same region as your function.
        
          - **S3Key** *(string) --* 
        
            The Amazon S3 key of the deployment package.
        
          - **S3ObjectVersion** *(string) --* 
        
            For versioned objects, the version of the deployment package object to use.
        
        :type Description: string
        :param Description: 
        
          A description of the function.
        
        :type Timeout: integer
        :param Timeout: 
        
          The amount of time that Lambda allows a function to run before terminating it. The default is 3 seconds. The maximum allowed value is 900 seconds.
        
        :type MemorySize: integer
        :param MemorySize: 
        
          The amount of memory that your function has access to. Increasing the function\'s memory also increases it\'s CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.
        
        :type Publish: boolean
        :param Publish: 
        
          Set to true to publish the first version of the function during creation.
        
        :type VpcConfig: dict
        :param VpcConfig: 
        
          If your Lambda function accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and one subnet ID.
        
          - **SubnetIds** *(list) --* 
        
            A list of VPC subnet IDs.
        
            - *(string) --* 
        
          - **SecurityGroupIds** *(list) --* 
        
            A list of VPC security groups IDs.
        
            - *(string) --* 
        
        :type DeadLetterConfig: dict
        :param DeadLetterConfig: 
        
          A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see `Dead Letter Queues <http://docs.aws.amazon.com/lambda/latest/dg/dlq.html>`__ . 
        
          - **TargetArn** *(string) --* 
        
            The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
        
        :type Environment: dict
        :param Environment: 
        
          Environment variables that are accessible from function code during execution.
        
          - **Variables** *(dict) --* 
        
            Environment variable key-value pairs.
        
            - *(string) --* 
        
              - *(string) --* 
        
        :type KMSKeyArn: string
        :param KMSKeyArn: 
        
          The ARN of the KMS key used to encrypt your function\'s environment variables. If not provided, AWS Lambda will use a default service key.
        
        :type TracingConfig: dict
        :param TracingConfig: 
        
          Set ``Mode`` to ``Active`` to sample and trace a subset of incoming requests with AWS X-Ray.
        
          - **Mode** *(string) --* 
        
            The tracing mode.
        
        :type Tags: dict
        :param Tags: 
        
          The list of tags (key-value pairs) assigned to the new function. For more information, see `Tagging Lambda Functions <http://docs.aws.amazon.com/lambda/latest/dg/tagging.html>`__ in the **AWS Lambda Developer Guide** .
        
          - *(string) --* 
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
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
            }
          **Response Structure** 
        
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
        
        """
        pass

    def delete_alias(self, FunctionName: str, Name: str) -> NoReturn:
        """
        
        This requires permission for the lambda:DeleteAlias action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/DeleteAlias>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_alias(
              FunctionName=\'string\',
              Name=\'string\'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Name of the alias to delete.
        
        :returns: None
        """
        pass

    def delete_event_source_mapping(self, UUID: str) -> Dict:
        """
        
        This operation requires permission for the ``lambda:DeleteEventSourceMapping`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/DeleteEventSourceMapping>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_event_source_mapping(
              UUID=\'string\'
          )
        :type UUID: string
        :param UUID: **[REQUIRED]** 
        
          The event source mapping ID.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UUID\': \'string\',
                \'BatchSize\': 123,
                \'EventSourceArn\': \'string\',
                \'FunctionArn\': \'string\',
                \'LastModified\': datetime(2015, 1, 1),
                \'LastProcessingResult\': \'string\',
                \'State\': \'string\',
                \'StateTransitionReason\': \'string\'
            }
          **Response Structure** 
        
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
        
        """
        pass

    def delete_function(self, FunctionName: str, Qualifier: str = None) -> NoReturn:
        """
        
        This operation requires permission for the ``lambda:DeleteFunction`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/DeleteFunction>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_function(
              FunctionName=\'string\',
              Qualifier=\'string\'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type Qualifier: string
        :param Qualifier: 
        
          Specify a version to delete. You cannot delete a version that is referenced by an alias.
        
        :returns: None
        """
        pass

    def delete_function_concurrency(self, FunctionName: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/DeleteFunctionConcurrency>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_function_concurrency(
              FunctionName=\'string\'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :returns: None
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

    def get_account_settings(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetAccountSettings>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_account_settings()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AccountLimit\': {
                    \'TotalCodeSize\': 123,
                    \'CodeSizeUnzipped\': 123,
                    \'CodeSizeZipped\': 123,
                    \'ConcurrentExecutions\': 123,
                    \'UnreservedConcurrentExecutions\': 123
                },
                \'AccountUsage\': {
                    \'TotalCodeSize\': 123,
                    \'FunctionCount\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AccountLimit** *(dict) --* 
        
              Limits related to concurrency and code storage.
        
              - **TotalCodeSize** *(integer) --* 
        
                Maximum size, in bytes, of a code package you can upload per region. The default size is 75 GB. 
        
              - **CodeSizeUnzipped** *(integer) --* 
        
                Size, in bytes, of code/dependencies that you can zip into a deployment package (uncompressed zip/jar size) for uploading. The default limit is 250 MB.
        
              - **CodeSizeZipped** *(integer) --* 
        
                Size, in bytes, of a single zipped code/dependencies package you can upload for your Lambda function(.zip/.jar file). Try using Amazon S3 for uploading larger files. Default limit is 50 MB.
        
              - **ConcurrentExecutions** *(integer) --* 
        
                Number of simultaneous executions of your function per region. The default limit is 1000.
        
              - **UnreservedConcurrentExecutions** *(integer) --* 
        
                The number of concurrent executions available to functions that do not have concurrency limits set. For more information, see `Managing Concurrency <http://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html>`__ .
        
            - **AccountUsage** *(dict) --* 
        
              The number of functions and amount of storage in use.
        
              - **TotalCodeSize** *(integer) --* 
        
                Total size, in bytes, of the account\'s deployment packages per region.
        
              - **FunctionCount** *(integer) --* 
        
                The number of your account\'s existing functions per region.
        
        """
        pass

    def get_alias(self, FunctionName: str, Name: str) -> Dict:
        """
        
        This requires permission for the ``lambda:GetAlias`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetAlias>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_alias(
              FunctionName=\'string\',
              Name=\'string\'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Name of the alias for which you want to retrieve information.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
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
            }
          **Response Structure** 
        
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
        
        """
        pass

    def get_event_source_mapping(self, UUID: str) -> Dict:
        """
        
        This operation requires permission for the ``lambda:GetEventSourceMapping`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetEventSourceMapping>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_event_source_mapping(
              UUID=\'string\'
          )
        :type UUID: string
        :param UUID: **[REQUIRED]** 
        
          The AWS Lambda assigned ID of the event source mapping.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UUID\': \'string\',
                \'BatchSize\': 123,
                \'EventSourceArn\': \'string\',
                \'FunctionArn\': \'string\',
                \'LastModified\': datetime(2015, 1, 1),
                \'LastProcessingResult\': \'string\',
                \'State\': \'string\',
                \'StateTransitionReason\': \'string\'
            }
          **Response Structure** 
        
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
        
        """
        pass

    def get_function(self, FunctionName: str, Qualifier: str = None) -> Dict:
        """
        
        Use the ``Qualifier`` parameter to retrieve a published version of the function. Otherwise, returns the unpublished version (``$LATEST`` ). For more information, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .
        
        This operation requires permission for the ``lambda:GetFunction`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetFunction>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_function(
              FunctionName=\'string\',
              Qualifier=\'string\'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type Qualifier: string
        :param Qualifier: 
        
          Specify a version or alias to get details about a published version of the function.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Configuration\': {
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
                \'Code\': {
                    \'RepositoryType\': \'string\',
                    \'Location\': \'string\'
                },
                \'Tags\': {
                    \'string\': \'string\'
                },
                \'Concurrency\': {
                    \'ReservedConcurrentExecutions\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            This response contains the object for the Lambda function location (see  FunctionCodeLocation .
        
            - **Configuration** *(dict) --* 
        
              The function\'s configuration.
        
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
        
            - **Code** *(dict) --* 
        
              The function\'s code.
        
              - **RepositoryType** *(string) --* 
        
                The repository from which you can download the function.
        
              - **Location** *(string) --* 
        
                The presigned URL you can use to download the function\'s .zip file that you previously uploaded. The URL is valid for up to 10 minutes.
        
            - **Tags** *(dict) --* 
        
              Returns the list of tags associated with the function. For more information, see `Tagging Lambda Functions <http://docs.aws.amazon.com/lambda/latest/dg/tagging.html>`__ in the **AWS Lambda Developer Guide** .
        
              - *(string) --* 
                
                - *(string) --* 
          
            - **Concurrency** *(dict) --* 
        
              The concurrent execution limit set for this function. For more information, see `Managing Concurrency <http://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html>`__ .
        
              - **ReservedConcurrentExecutions** *(integer) --* 
        
                The number of concurrent executions reserved for this function. For more information, see `Managing Concurrency <http://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html>`__ .
        
        """
        pass

    def get_function_configuration(self, FunctionName: str, Qualifier: str = None) -> Dict:
        """
        
        If you are using the versioning feature, you can retrieve this information for a specific function version by using the optional ``Qualifier`` parameter and specifying the function version or alias that points to it. If you don\'t provide it, the API returns information about the $LATEST version of the function. For more information about versioning, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .
        
        This operation requires permission for the ``lambda:GetFunctionConfiguration`` operation.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetFunctionConfiguration>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_function_configuration(
              FunctionName=\'string\',
              Qualifier=\'string\'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type Qualifier: string
        :param Qualifier: 
        
          Specify a version or alias to get details about a published version of the function.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
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
            }
          **Response Structure** 
        
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

    def get_policy(self, FunctionName: str, Qualifier: str = None) -> Dict:
        """
        
        This action requires permission for the ``lambda:GetPolicy action.``  
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_policy(
              FunctionName=\'string\',
              Qualifier=\'string\'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type Qualifier: string
        :param Qualifier: 
        
          You can specify this optional query parameter to specify a function version or an alias name in which case this API will return all permissions associated with the specific qualified ARN. If you don\'t provide this parameter, the API will return permissions that apply to the unqualified function ARN.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Policy\': \'string\',
                \'RevisionId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Policy** *(string) --* 
        
              The resource policy associated with the specified function. The response returns the same as a string using a backslash (\"\\") as an escape character in the JSON.
        
            - **RevisionId** *(string) --* 
        
              Represents the latest updated revision of the function or alias.
        
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

    def invoke(self, FunctionName: str, InvocationType: str = None, LogType: str = None, ClientContext: str = None, Payload: Union[bytes, IO] = None, Qualifier: str = None) -> Dict:
        """
        
        Specify just a function name to invoke the latest version of the function. To invoke a published version, use the ``Qualifier`` parameter to specify a `version or alias <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .
        
        If you use the ``RequestResponse`` (synchronous) invocation option, the function will be invoked only once. If you use the ``Event`` (asynchronous) invocation option, the function will be invoked at least once in response to an event and the function must be idempotent to handle this.
        
        For functions with a long timeout, your client may be disconnected during synchronous invocation while it waits for a response. Configure your HTTP client, SDK, firewall, proxy, or operating system to allow for long connections with timeout or keep-alive settings.
        
        This operation requires permission for the ``lambda:InvokeFunction`` action.
        
        The ``TooManyRequestsException`` noted below will return the following: ``ConcurrentInvocationLimitExceeded`` will be returned if you have no functions with reserved concurrency and have exceeded your account concurrent limit or if a function without reserved concurrency exceeds the account\'s unreserved concurrency limit. ``ReservedFunctionConcurrentInvocationLimitExceeded`` will be returned when a function with reserved concurrency exceeds its configured concurrency limit. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/Invoke>`_
        
        **Request Syntax** 
        ::
        
          response = client.invoke(
              FunctionName=\'string\',
              InvocationType=\'Event\'|\'RequestResponse\'|\'DryRun\',
              LogType=\'None\'|\'Tail\',
              ClientContext=\'string\',
              Payload=b\'bytes\'|file,
              Qualifier=\'string\'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type InvocationType: string
        :param InvocationType: 
        
          Choose from the following options.
        
          * ``RequestResponse`` (default) - Invoke the function synchronously. Keep the connection open until the function returns a response or times out. 
           
          * ``Event`` - Invoke the function asynchronously. Send events that fail multiple times to the function\'s dead-letter queue (if configured). 
           
          * ``DryRun`` - Validate parameter values and verify that the user or role has permission to invoke the function. 
           
        :type LogType: string
        :param LogType: 
        
          You can set this optional parameter to ``Tail`` in the request only if you specify the ``InvocationType`` parameter with value ``RequestResponse`` . In this case, AWS Lambda returns the base64-encoded last 4 KB of log data produced by your Lambda function in the ``x-amz-log-result`` header. 
        
        :type ClientContext: string
        :param ClientContext: 
        
          Using the ``ClientContext`` you can pass client-specific information to the Lambda function you are invoking. You can then process the client information in your Lambda function as you choose through the context variable. For an example of a ``ClientContext`` JSON, see `PutEvents <http://docs.aws.amazon.com/mobileanalytics/latest/ug/PutEvents.html>`__ in the *Amazon Mobile Analytics API Reference and User Guide* .
        
          The ClientContext JSON must be base64-encoded and has a maximum size of 3583 bytes.
        
          .. note::
        
             ``ClientContext`` information is returned only if you use the synchronous (``RequestResponse`` ) invocation type.
        
        :type Payload: bytes or seekable file-like object
        :param Payload: 
        
          JSON that you want to provide to your Lambda function as input.
        
        :type Qualifier: string
        :param Qualifier: 
        
          Specify a version or alias to invoke a published version of the function.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StatusCode\': 123,
                \'FunctionError\': \'string\',
                \'LogResult\': \'string\',
                \'Payload\': StreamingBody(),
                \'ExecutedVersion\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Upon success, returns an empty response. Otherwise, throws an exception.
        
            - **StatusCode** *(integer) --* 
        
              The HTTP status code will be in the 200 range for successful request. For the ``RequestResponse`` invocation type this status code will be 200. For the ``Event`` invocation type this status code will be 202. For the ``DryRun`` invocation type the status code will be 204. 
        
            - **FunctionError** *(string) --* 
        
              Indicates whether an error occurred while executing the Lambda function. If an error occurred this field will have one of two values; ``Handled`` or ``Unhandled`` . ``Handled`` errors are errors that are reported by the function while the ``Unhandled`` errors are those detected and reported by AWS Lambda. Unhandled errors include out of memory errors and function timeouts. For information about how to report an ``Handled`` error, see `Programming Model <http://docs.aws.amazon.com/lambda/latest/dg/programming-model.html>`__ . 
        
            - **LogResult** *(string) --* 
        
              It is the base64-encoded logs for the Lambda function invocation. This is present only if the invocation type is ``RequestResponse`` and the logs were requested. 
        
            - **Payload** (:class:`.StreamingBody`) -- 
        
              It is the JSON representation of the object returned by the Lambda function. This is present only if the invocation type is ``RequestResponse`` . 
        
              In the event of a function error this field contains a message describing the error. For the ``Handled`` errors the Lambda function will report this message. For ``Unhandled`` errors AWS Lambda reports the message. 
        
            - **ExecutedVersion** *(string) --* 
        
              The function version that has been executed. This value is returned only if the invocation type is ``RequestResponse`` . For more information, see `Traffic Shifting Using Aliases <http://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__ .
        
        """
        pass

    def invoke_async(self, FunctionName: str, InvokeArgs: Union[bytes, IO]) -> Dict:
        """
        .. warning::
        
          For asynchronous function invocation, use  Invoke .
        
        Submits an invocation request to AWS Lambda. Upon receiving the request, Lambda executes the specified function asynchronously. To see the logs generated by the Lambda function execution, see the CloudWatch Logs console.
        
        This operation requires permission for the ``lambda:InvokeFunction`` action.
        
        .. danger::
        
            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/InvokeAsync>`_
        
        **Request Syntax** 
        ::
        
          response = client.invoke_async(
              FunctionName=\'string\',
              InvokeArgs=b\'bytes\'|file
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type InvokeArgs: bytes or seekable file-like object
        :param InvokeArgs: **[REQUIRED]** 
        
          JSON that you want to provide to your Lambda function as input.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Status\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Upon success, it returns empty response. Otherwise, throws an exception.
        
            - **Status** *(integer) --* 
        
              It will be 202 upon success.
        
        """
        pass

    def list_aliases(self, FunctionName: str, FunctionVersion: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        """
        
        This requires permission for the lambda:ListAliases action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListAliases>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_aliases(
              FunctionName=\'string\',
              FunctionVersion=\'string\',
              Marker=\'string\',
              MaxItems=123
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
        
        :type Marker: string
        :param Marker: 
        
          Optional string. An opaque pagination token returned from a previous ``ListAliases`` operation. If present, indicates where to continue the listing.
        
        :type MaxItems: integer
        :param MaxItems: 
        
          Optional integer. Specifies the maximum number of aliases to return in response. This parameter value must be greater than 0.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextMarker\': \'string\',
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextMarker** *(string) --* 
        
              A string, present if there are more aliases.
        
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
        
        """
        pass

    def list_event_source_mappings(self, EventSourceArn: str = None, FunctionName: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        """
        
        For each mapping, the API returns configuration information. You can optionally specify filters to retrieve specific event source mappings.
        
        This operation requires permission for the ``lambda:ListEventSourceMappings`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListEventSourceMappings>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_event_source_mappings(
              EventSourceArn=\'string\',
              FunctionName=\'string\',
              Marker=\'string\',
              MaxItems=123
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
        
        :type Marker: string
        :param Marker: 
        
          Optional string. An opaque pagination token returned from a previous ``ListEventSourceMappings`` operation. If present, specifies to continue the list from where the returning call left off. 
        
        :type MaxItems: integer
        :param MaxItems: 
        
          Optional integer. Specifies the maximum number of event sources to return in response. This value must be greater than 0.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextMarker\': \'string\',
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains a list of event sources (see  EventSourceMappingConfiguration )
        
            - **NextMarker** *(string) --* 
        
              A string, present if there are more event source mappings.
        
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
        
        """
        pass

    def list_functions(self, MasterRegion: str = None, FunctionVersion: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        """
        
        This operation requires permission for the ``lambda:ListFunctions`` action.
        
        If you are using the versioning feature, you can list all of your functions or only ``$LATEST`` versions. For information about the versioning feature, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListFunctions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_functions(
              MasterRegion=\'string\',
              FunctionVersion=\'ALL\',
              Marker=\'string\',
              MaxItems=123
          )
        :type MasterRegion: string
        :param MasterRegion: 
        
          Specify a region (e.g. ``us-east-2`` ) to only list functions that were created in that region, or ``ALL`` to include functions replicated from any region. If specified, you also must specify the ``FunctionVersion`` .
        
        :type FunctionVersion: string
        :param FunctionVersion: 
        
          Set to ``ALL`` to list all published versions. If not specified, only the latest unpublished version ARN is returned.
        
        :type Marker: string
        :param Marker: 
        
          Optional string. An opaque pagination token returned from a previous ``ListFunctions`` operation. If present, indicates where to continue the listing. 
        
        :type MaxItems: integer
        :param MaxItems: 
        
          Optional integer. Specifies the maximum number of AWS Lambda functions to return in response. This parameter value must be greater than 0. The absolute maximum of AWS Lambda functions that can be returned is 50.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextMarker\': \'string\',
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            A list of Lambda functions.
        
            - **NextMarker** *(string) --* 
        
              A string, present if there are more functions.
        
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
        
        """
        pass

    def list_tags(self, Resource: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags(
              Resource=\'string\'
          )
        :type Resource: string
        :param Resource: **[REQUIRED]** 
        
          The ARN (Amazon Resource Name) of the function. For more information, see `Tagging Lambda Functions <http://docs.aws.amazon.com/lambda/latest/dg/tagging.html>`__ in the **AWS Lambda Developer Guide** .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Tags\': {
                    \'string\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Tags** *(dict) --* 
        
              The list of tags assigned to the function. For more information, see `Tagging Lambda Functions <http://docs.aws.amazon.com/lambda/latest/dg/tagging.html>`__ in the **AWS Lambda Developer Guide** .
        
              - *(string) --* 
                
                - *(string) --* 
          
        """
        pass

    def list_versions_by_function(self, FunctionName: str, Marker: str = None, MaxItems: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListVersionsByFunction>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_versions_by_function(
              FunctionName=\'string\',
              Marker=\'string\',
              MaxItems=123
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type Marker: string
        :param Marker: 
        
          Optional string. An opaque pagination token returned from a previous ``ListVersionsByFunction`` operation. If present, indicates where to continue the listing. 
        
        :type MaxItems: integer
        :param MaxItems: 
        
          Optional integer. Specifies the maximum number of AWS Lambda function versions to return in response. This parameter value must be greater than 0.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextMarker\': \'string\',
                \'Versions\': [
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextMarker** *(string) --* 
        
              A string, present if there are more function versions.
        
            - **Versions** *(list) --* 
        
              A list of Lambda function versions.
        
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
        
        """
        pass

    def publish_version(self, FunctionName: str, CodeSha256: str = None, Description: str = None, RevisionId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/PublishVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.publish_version(
              FunctionName=\'string\',
              CodeSha256=\'string\',
              Description=\'string\',
              RevisionId=\'string\'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type CodeSha256: string
        :param CodeSha256: 
        
          The SHA256 hash of the deployment package you want to publish. This provides validation on the code you are publishing. If you provide this parameter, the value must match the SHA256 of the $LATEST version for the publication to succeed. You can use the **DryRun** parameter of  UpdateFunctionCode to verify the hash value that will be returned before publishing your new version.
        
        :type Description: string
        :param Description: 
        
          The description for the version you are publishing. If not provided, AWS Lambda copies the description from the $LATEST version.
        
        :type RevisionId: string
        :param RevisionId: 
        
          An optional value you can use to ensure you are updating the latest update of the function version or alias. If the ``RevisionID`` you pass doesn\'t match the latest ``RevisionId`` of the function or alias, it will fail with an error message, advising you retrieve the latest function version or alias ``RevisionID`` using either  GetFunction or  GetAlias .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
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
            }
          **Response Structure** 
        
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
        
        """
        pass

    def put_function_concurrency(self, FunctionName: str, ReservedConcurrentExecutions: int) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/PutFunctionConcurrency>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_function_concurrency(
              FunctionName=\'string\',
              ReservedConcurrentExecutions=123
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type ReservedConcurrentExecutions: integer
        :param ReservedConcurrentExecutions: **[REQUIRED]** 
        
          The concurrent execution limit reserved for this function.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ReservedConcurrentExecutions\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ReservedConcurrentExecutions** *(integer) --* 
        
              The number of concurrent executions reserved for this function. For more information, see `Managing Concurrency <http://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html>`__ .
        
        """
        pass

    def remove_permission(self, FunctionName: str, StatementId: str, Qualifier: str = None, RevisionId: str = None) -> NoReturn:
        """
        
        Permissions apply to the Amazon Resource Name (ARN) used to invoke the function, which can be unqualified (the unpublished version of the function), or include a version or alias. If a client uses a version or alias to invoke a function, use the ``Qualifier`` parameter to apply permissions to that ARN. For more information about versioning, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 
        
        You need permission for the ``lambda:RemovePermission`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/RemovePermission>`_
        
        **Request Syntax** 
        ::
        
          response = client.remove_permission(
              FunctionName=\'string\',
              StatementId=\'string\',
              Qualifier=\'string\',
              RevisionId=\'string\'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type StatementId: string
        :param StatementId: **[REQUIRED]** 
        
          Statement ID of the permission to remove.
        
        :type Qualifier: string
        :param Qualifier: 
        
          Specify a version or alias to remove permissions from a published version of the function.
        
        :type RevisionId: string
        :param RevisionId: 
        
          An optional value you can use to ensure you are updating the latest update of the function version or alias. If the ``RevisionID`` you pass doesn\'t match the latest ``RevisionId`` of the function or alias, it will fail with an error message, advising you to retrieve the latest function version or alias ``RevisionID`` using either  GetFunction or  GetAlias .
        
        :returns: None
        """
        pass

    def tag_resource(self, Resource: str, Tags: Dict) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/TagResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.tag_resource(
              Resource=\'string\',
              Tags={
                  \'string\': \'string\'
              }
          )
        :type Resource: string
        :param Resource: **[REQUIRED]** 
        
          The ARN (Amazon Resource Name) of the Lambda function. For more information, see `Tagging Lambda Functions <http://docs.aws.amazon.com/lambda/latest/dg/tagging.html>`__ in the **AWS Lambda Developer Guide** .
        
        :type Tags: dict
        :param Tags: **[REQUIRED]** 
        
          The list of tags (key-value pairs) you are assigning to the Lambda function. For more information, see `Tagging Lambda Functions <http://docs.aws.amazon.com/lambda/latest/dg/tagging.html>`__ in the **AWS Lambda Developer Guide** .
        
          - *(string) --* 
        
            - *(string) --* 
        
        :returns: None
        """
        pass

    def untag_resource(self, Resource: str, TagKeys: List) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/UntagResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.untag_resource(
              Resource=\'string\',
              TagKeys=[
                  \'string\',
              ]
          )
        :type Resource: string
        :param Resource: **[REQUIRED]** 
        
          The ARN (Amazon Resource Name) of the function. For more information, see `Tagging Lambda Functions <http://docs.aws.amazon.com/lambda/latest/dg/tagging.html>`__ in the **AWS Lambda Developer Guide** .
        
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** 
        
          The list of tag keys to be deleted from the function. For more information, see `Tagging Lambda Functions <http://docs.aws.amazon.com/lambda/latest/dg/tagging.html>`__ in the **AWS Lambda Developer Guide** .
        
          - *(string) --* 
        
        :returns: None
        """
        pass

    def update_alias(self, FunctionName: str, Name: str, FunctionVersion: str = None, Description: str = None, RoutingConfig: Dict = None, RevisionId: str = None) -> Dict:
        """
        
        This requires permission for the lambda:UpdateAlias action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/UpdateAlias>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_alias(
              FunctionName=\'string\',
              Name=\'string\',
              FunctionVersion=\'string\',
              Description=\'string\',
              RoutingConfig={
                  \'AdditionalVersionWeights\': {
                      \'string\': 123.0
                  }
              },
              RevisionId=\'string\'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The alias name.
        
        :type FunctionVersion: string
        :param FunctionVersion: 
        
          Using this parameter you can change the Lambda function version to which the alias points.
        
        :type Description: string
        :param Description: 
        
          You can change the description of the alias using this parameter.
        
        :type RoutingConfig: dict
        :param RoutingConfig: 
        
          Specifies an additional version your alias can point to, allowing you to dictate what percentage of traffic will invoke each version. For more information, see `Traffic Shifting Using Aliases <http://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__ .
        
          - **AdditionalVersionWeights** *(dict) --* 
        
            The name of the second alias, and the percentage of traffic that is routed to it.
        
            - *(string) --* 
        
              - *(float) --* 
        
        :type RevisionId: string
        :param RevisionId: 
        
          An optional value you can use to ensure you are updating the latest update of the function version or alias. If the ``RevisionID`` you pass doesn\'t match the latest ``RevisionId`` of the function or alias, it will fail with an error message, advising you retrieve the latest function version or alias ``RevisionID`` using either  GetFunction or  GetAlias .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
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
            }
          **Response Structure** 
        
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
        
        """
        pass

    def update_event_source_mapping(self, UUID: str, FunctionName: str = None, Enabled: bool = None, BatchSize: int = None) -> Dict:
        """
        
        If you disable the event source mapping, AWS Lambda stops polling. If you enable again, it will resume polling from the time it had stopped polling, so you don\'t lose processing of any records. However, if you delete event source mapping and create it again, it will reset.
        
        This operation requires permission for the ``lambda:UpdateEventSourceMapping`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/UpdateEventSourceMapping>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_event_source_mapping(
              UUID=\'string\',
              FunctionName=\'string\',
              Enabled=True|False,
              BatchSize=123
          )
        :type UUID: string
        :param UUID: **[REQUIRED]** 
        
          The event source mapping identifier.
        
        :type FunctionName: string
        :param FunctionName: 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Version or Alias ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type Enabled: boolean
        :param Enabled: 
        
          Specifies whether AWS Lambda should actively poll the stream or not. If disabled, AWS Lambda will not poll the stream.
        
        :type BatchSize: integer
        :param BatchSize: 
        
          The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UUID\': \'string\',
                \'BatchSize\': 123,
                \'EventSourceArn\': \'string\',
                \'FunctionArn\': \'string\',
                \'LastModified\': datetime(2015, 1, 1),
                \'LastProcessingResult\': \'string\',
                \'State\': \'string\',
                \'StateTransitionReason\': \'string\'
            }
          **Response Structure** 
        
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
        
        """
        pass

    def update_function_code(self, FunctionName: str, ZipFile: bytes = None, S3Bucket: str = None, S3Key: str = None, S3ObjectVersion: str = None, Publish: bool = None, DryRun: bool = None, RevisionId: str = None) -> Dict:
        """
        
        If you are using the versioning feature, note this API will always update the $LATEST version of your Lambda function. For information about the versioning feature, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 
        
        This operation requires permission for the ``lambda:UpdateFunctionCode`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/UpdateFunctionCode>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_function_code(
              FunctionName=\'string\',
              ZipFile=b\'bytes\',
              S3Bucket=\'string\',
              S3Key=\'string\',
              S3ObjectVersion=\'string\',
              Publish=True|False,
              DryRun=True|False,
              RevisionId=\'string\'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type ZipFile: bytes
        :param ZipFile: 
        
          The contents of your zip file containing your deployment package. If you are using the web API directly, the contents of the zip file must be base64-encoded. If you are using the AWS SDKs or the AWS CLI, the SDKs or CLI will do the encoding for you. For more information about creating a .zip file, see `Execution Permissions <http://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html#lambda-intro-execution-role.html>`__ . 
        
            **This value will be base64 encoded automatically. Do not base64 encode this value prior to performing the operation.**
        
        :type S3Bucket: string
        :param S3Bucket: 
        
          Amazon S3 bucket name where the .zip file containing your deployment package is stored. This bucket must reside in the same AWS Region where you are creating the Lambda function.
        
        :type S3Key: string
        :param S3Key: 
        
          The Amazon S3 object (the deployment package) key name you want to upload.
        
        :type S3ObjectVersion: string
        :param S3ObjectVersion: 
        
          The Amazon S3 object (the deployment package) version you want to upload.
        
        :type Publish: boolean
        :param Publish: 
        
          This boolean parameter can be used to request AWS Lambda to update the Lambda function and publish a version as an atomic operation.
        
        :type DryRun: boolean
        :param DryRun: 
        
          This boolean parameter can be used to test your request to AWS Lambda to update the Lambda function and publish a version as an atomic operation. It will do all necessary computation and validation of your code but will not upload it or a publish a version. Each time this operation is invoked, the ``CodeSha256`` hash value of the provided code will also be computed and returned in the response.
        
        :type RevisionId: string
        :param RevisionId: 
        
          An optional value you can use to ensure you are updating the latest update of the function version or alias. If the ``RevisionID`` you pass doesn\'t match the latest ``RevisionId`` of the function or alias, it will fail with an error message, advising you to retrieve the latest function version or alias ``RevisionID`` using either using using either  GetFunction or  GetAlias .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
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
            }
          **Response Structure** 
        
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
        
        """
        pass

    def update_function_configuration(self, FunctionName: str, Role: str = None, Handler: str = None, Description: str = None, Timeout: int = None, MemorySize: int = None, VpcConfig: Dict = None, Environment: Dict = None, Runtime: str = None, DeadLetterConfig: Dict = None, KMSKeyArn: str = None, TracingConfig: Dict = None, RevisionId: str = None) -> Dict:
        """
        
        If you are using the versioning feature, note this API will always update the $LATEST version of your Lambda function. For information about the versioning feature, see `AWS Lambda Function Versioning and Aliases <http://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ . 
        
        This operation requires permission for the ``lambda:UpdateFunctionConfiguration`` action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/UpdateFunctionConfiguration>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_function_configuration(
              FunctionName=\'string\',
              Role=\'string\',
              Handler=\'string\',
              Description=\'string\',
              Timeout=123,
              MemorySize=123,
              VpcConfig={
                  \'SubnetIds\': [
                      \'string\',
                  ],
                  \'SecurityGroupIds\': [
                      \'string\',
                  ]
              },
              Environment={
                  \'Variables\': {
                      \'string\': \'string\'
                  }
              },
              Runtime=\'nodejs\'|\'nodejs4.3\'|\'nodejs6.10\'|\'nodejs8.10\'|\'java8\'|\'python2.7\'|\'python3.6\'|\'dotnetcore1.0\'|\'dotnetcore2.0\'|\'dotnetcore2.1\'|\'nodejs4.3-edge\'|\'go1.x\',
              DeadLetterConfig={
                  \'TargetArn\': \'string\'
              },
              KMSKeyArn=\'string\',
              TracingConfig={
                  \'Mode\': \'Active\'|\'PassThrough\'
              },
              RevisionId=\'string\'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]** 
        
          The name of the lambda function.
        
           **Name formats**  
        
          * **Function name** - ``MyFunction`` . 
           
          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` . 
           
          * **Partial ARN** - ``123456789012:function:MyFunction`` . 
           
          The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
        
        :type Role: string
        :param Role: 
        
          The Amazon Resource Name (ARN) of the IAM role that Lambda will assume when it executes your function.
        
        :type Handler: string
        :param Handler: 
        
          The function that Lambda calls to begin executing your function. For Node.js, it is the ``module-name.export`` value in your function. 
        
        :type Description: string
        :param Description: 
        
          A short user-defined function description. AWS Lambda does not use this value. Assign a meaningful description as you see fit.
        
        :type Timeout: integer
        :param Timeout: 
        
          The amount of time that Lambda allows a function to run before terminating it. The default is 3 seconds. The maximum allowed value is 900 seconds.
        
        :type MemorySize: integer
        :param MemorySize: 
        
          The amount of memory, in MB, your Lambda function is given. AWS Lambda uses this memory size to infer the amount of CPU allocated to your function. Your function use-case determines your CPU and memory requirements. For example, a database operation might need less memory compared to an image processing function. The default value is 128 MB. The value must be a multiple of 64 MB.
        
        :type VpcConfig: dict
        :param VpcConfig: 
        
          Specify security groups and subnets in a VPC to which your Lambda function needs access.
        
          - **SubnetIds** *(list) --* 
        
            A list of VPC subnet IDs.
        
            - *(string) --* 
        
          - **SecurityGroupIds** *(list) --* 
        
            A list of VPC security groups IDs.
        
            - *(string) --* 
        
        :type Environment: dict
        :param Environment: 
        
          The parent object that contains your environment\'s configuration settings.
        
          - **Variables** *(dict) --* 
        
            Environment variable key-value pairs.
        
            - *(string) --* 
        
              - *(string) --* 
        
        :type Runtime: string
        :param Runtime: 
        
          The runtime version for the function.
        
        :type DeadLetterConfig: dict
        :param DeadLetterConfig: 
        
          A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see `Dead Letter Queues <http://docs.aws.amazon.com/lambda/latest/dg/dlq.html>`__ .
        
          - **TargetArn** *(string) --* 
        
            The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
        
        :type KMSKeyArn: string
        :param KMSKeyArn: 
        
          The Amazon Resource Name (ARN) of the KMS key used to encrypt your function\'s environment variables. If you elect to use the AWS Lambda default service key, pass in an empty string (\"\") for this parameter.
        
        :type TracingConfig: dict
        :param TracingConfig: 
        
          Set ``Mode`` to ``Active`` to sample and trace a subset of incoming requests with AWS X-Ray.
        
          - **Mode** *(string) --* 
        
            The tracing mode.
        
        :type RevisionId: string
        :param RevisionId: 
        
          An optional value you can use to ensure you are updating the latest update of the function version or alias. If the ``RevisionID`` you pass doesn\'t match the latest ``RevisionId`` of the function or alias, it will fail with an error message, advising you to retrieve the latest function version or alias ``RevisionID`` using either  GetFunction or  GetAlias .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
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
            }
          **Response Structure** 
        
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
        
        """
        pass
