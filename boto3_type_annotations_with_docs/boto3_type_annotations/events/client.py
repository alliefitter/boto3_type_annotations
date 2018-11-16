from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
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

    def delete_rule(self, Name: str) -> NoReturn:
        """
        
        Before you can delete the rule, you must remove all targets, using  RemoveTargets .
        
        When you delete a rule, incoming events might continue to match to the deleted rule. Allow a short period of time for changes to take effect.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/DeleteRule>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_rule(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the rule.
        
        :returns: None
        """
        pass

    def describe_event_bus(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/DescribeEventBus>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_event_bus()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Name\': \'string\',
                \'Arn\': \'string\',
                \'Policy\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Name** *(string) --* 
        
              The name of the event bus. Currently, this is always ``default`` .
        
            - **Arn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the account permitted to write events to the current account.
        
            - **Policy** *(string) --* 
        
              The policy that enables the external account to send events to your account.
        
        """
        pass

    def describe_rule(self, Name: str) -> Dict:
        """
        
        DescribeRule does not list the targets of a rule. To see the targets associated with a rule, use  ListTargetsByRule .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/DescribeRule>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_rule(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the rule.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Name\': \'string\',
                \'Arn\': \'string\',
                \'EventPattern\': \'string\',
                \'ScheduleExpression\': \'string\',
                \'State\': \'ENABLED\'|\'DISABLED\',
                \'Description\': \'string\',
                \'RoleArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Name** *(string) --* 
        
              The name of the rule.
        
            - **Arn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the rule.
        
            - **EventPattern** *(string) --* 
        
              The event pattern. For more information, see `Events and Event Patterns <http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html>`__ in the *Amazon CloudWatch Events User Guide* .
        
            - **ScheduleExpression** *(string) --* 
        
              The scheduling expression. For example, \"cron(0 20 * * ? *)\", \"rate(5 minutes)\".
        
            - **State** *(string) --* 
        
              Specifies whether the rule is enabled or disabled.
        
            - **Description** *(string) --* 
        
              The description of the rule.
        
            - **RoleArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the IAM role associated with the rule.
        
        """
        pass

    def disable_rule(self, Name: str) -> NoReturn:
        """
        
        When you disable a rule, incoming events might continue to match to the disabled rule. Allow a short period of time for changes to take effect.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/DisableRule>`_
        
        **Request Syntax** 
        ::
        
          response = client.disable_rule(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the rule.
        
        :returns: None
        """
        pass

    def enable_rule(self, Name: str) -> NoReturn:
        """
        
        When you enable a rule, incoming events might not immediately start matching to a newly enabled rule. Allow a short period of time for changes to take effect.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/EnableRule>`_
        
        **Request Syntax** 
        ::
        
          response = client.enable_rule(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the rule.
        
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

    def list_rule_names_by_target(self, TargetArn: str, NextToken: str = None, Limit: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/ListRuleNamesByTarget>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_rule_names_by_target(
              TargetArn=\'string\',
              NextToken=\'string\',
              Limit=123
          )
        :type TargetArn: string
        :param TargetArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the target resource.
        
        :type NextToken: string
        :param NextToken: 
        
          The token returned by a previous call to retrieve the next set of results.
        
        :type Limit: integer
        :param Limit: 
        
          The maximum number of results to return.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RuleNames\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **RuleNames** *(list) --* 
        
              The names of the rules that can invoke the given target.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              Indicates whether there are additional results to retrieve. If there are no more results, the value is null.
        
        """
        pass

    def list_rules(self, NamePrefix: str = None, NextToken: str = None, Limit: int = None) -> Dict:
        """
        
        ListRules does not list the targets of a rule. To see the targets associated with a rule, use  ListTargetsByRule .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/ListRules>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_rules(
              NamePrefix=\'string\',
              NextToken=\'string\',
              Limit=123
          )
        :type NamePrefix: string
        :param NamePrefix: 
        
          The prefix matching the rule name.
        
        :type NextToken: string
        :param NextToken: 
        
          The token returned by a previous call to retrieve the next set of results.
        
        :type Limit: integer
        :param Limit: 
        
          The maximum number of results to return.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Rules\': [
                    {
                        \'Name\': \'string\',
                        \'Arn\': \'string\',
                        \'EventPattern\': \'string\',
                        \'State\': \'ENABLED\'|\'DISABLED\',
                        \'Description\': \'string\',
                        \'ScheduleExpression\': \'string\',
                        \'RoleArn\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Rules** *(list) --* 
        
              The rules that match the specified criteria.
        
              - *(dict) --* 
        
                Contains information about a rule in Amazon CloudWatch Events.
        
                - **Name** *(string) --* 
        
                  The name of the rule.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the rule.
        
                - **EventPattern** *(string) --* 
        
                  The event pattern of the rule. For more information, see `Events and Event Patterns <http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html>`__ in the *Amazon CloudWatch Events User Guide* .
        
                - **State** *(string) --* 
        
                  The state of the rule.
        
                - **Description** *(string) --* 
        
                  The description of the rule.
        
                - **ScheduleExpression** *(string) --* 
        
                  The scheduling expression. For example, \"cron(0 20 * * ? *)\", \"rate(5 minutes)\".
        
                - **RoleArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the role that is used for target invocation.
        
            - **NextToken** *(string) --* 
        
              Indicates whether there are additional results to retrieve. If there are no more results, the value is null.
        
        """
        pass

    def list_targets_by_rule(self, Rule: str, NextToken: str = None, Limit: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/ListTargetsByRule>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_targets_by_rule(
              Rule=\'string\',
              NextToken=\'string\',
              Limit=123
          )
        :type Rule: string
        :param Rule: **[REQUIRED]** 
        
          The name of the rule.
        
        :type NextToken: string
        :param NextToken: 
        
          The token returned by a previous call to retrieve the next set of results.
        
        :type Limit: integer
        :param Limit: 
        
          The maximum number of results to return.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Targets\': [
                    {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'RoleArn\': \'string\',
                        \'Input\': \'string\',
                        \'InputPath\': \'string\',
                        \'InputTransformer\': {
                            \'InputPathsMap\': {
                                \'string\': \'string\'
                            },
                            \'InputTemplate\': \'string\'
                        },
                        \'KinesisParameters\': {
                            \'PartitionKeyPath\': \'string\'
                        },
                        \'RunCommandParameters\': {
                            \'RunCommandTargets\': [
                                {
                                    \'Key\': \'string\',
                                    \'Values\': [
                                        \'string\',
                                    ]
                                },
                            ]
                        },
                        \'EcsParameters\': {
                            \'TaskDefinitionArn\': \'string\',
                            \'TaskCount\': 123,
                            \'LaunchType\': \'EC2\'|\'FARGATE\',
                            \'NetworkConfiguration\': {
                                \'awsvpcConfiguration\': {
                                    \'Subnets\': [
                                        \'string\',
                                    ],
                                    \'SecurityGroups\': [
                                        \'string\',
                                    ],
                                    \'AssignPublicIp\': \'ENABLED\'|\'DISABLED\'
                                }
                            },
                            \'PlatformVersion\': \'string\',
                            \'Group\': \'string\'
                        },
                        \'BatchParameters\': {
                            \'JobDefinition\': \'string\',
                            \'JobName\': \'string\',
                            \'ArrayProperties\': {
                                \'Size\': 123
                            },
                            \'RetryStrategy\': {
                                \'Attempts\': 123
                            }
                        },
                        \'SqsParameters\': {
                            \'MessageGroupId\': \'string\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Targets** *(list) --* 
        
              The targets assigned to the rule.
        
              - *(dict) --* 
        
                Targets are the resources to be invoked when a rule is triggered. For a complete list of services and resources that can be set as a target, see  PutTargets .
        
                If you are setting the event bus of another account as the target, and that account granted permission to your account through an organization instead of directly by the account ID, then you must specify a ``RoleArn`` with proper permissions in the ``Target`` structure. For more information, see `Sending and Receiving Events Between AWS Accounts <http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEvents-CrossAccountEventDelivery.html>`__ in the *Amazon CloudWatch Events User Guide* .
        
                - **Id** *(string) --* 
        
                  The ID of the target.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the target.
        
                - **RoleArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. If one rule triggers multiple targets, you can use a different IAM role for each target.
        
                - **Input** *(string) --* 
        
                  Valid JSON text passed to the target. In this case, nothing from the event itself is passed to the target. For more information, see `The JavaScript Object Notation (JSON) Data Interchange Format <http://www.rfc-editor.org/rfc/rfc7159.txt>`__ .
        
                - **InputPath** *(string) --* 
        
                  The value of the JSONPath that is used for extracting part of the matched event when passing it to the target. You must use JSON dot notation, not bracket notation. For more information about JSON paths, see `JSONPath <http://goessner.net/articles/JsonPath/>`__ .
        
                - **InputTransformer** *(dict) --* 
        
                  Settings to enable you to provide custom input to a target based on certain event data. You can extract one or more key-value pairs from the event and then use that data to send customized input to the target.
        
                  - **InputPathsMap** *(dict) --* 
        
                    Map of JSON paths to be extracted from the event. You can then insert these in the template in ``InputTemplate`` to produce the output you want to be sent to the target.
        
                     ``InputPathsMap`` is an array key-value pairs, where each value is a valid JSON path. You can have as many as 10 key-value pairs. You must use JSON dot notation, not bracket notation.
        
                    The keys cannot start with \"AWS.\" 
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
                  - **InputTemplate** *(string) --* 
        
                    Input template where you specify placeholders that will be filled with the values of the keys from ``InputPathsMap`` to customize the data sent to the target. Enclose each ``InputPathsMaps`` value in brackets: <*value* > The InputTemplate must be valid JSON.
        
                    If ``InputTemplate`` is a JSON object (surrounded by curly braces), the following restrictions apply:
        
                    * The placeholder cannot be used as an object key. 
                     
                    * Object values cannot include quote marks. 
                     
                    The following example shows the syntax for using ``InputPathsMap`` and ``InputTemplate`` .
        
                     ``\"InputTransformer\":``  
        
                     ``{``  
        
                     ``\"InputPathsMap\": {\"instance\": \"$.detail.instance\",\"status\": \"$.detail.status\"},``  
        
                     ``\"InputTemplate\": \"<instance> is in state <status>\"``  
        
                     ``}``  
        
                    To have the ``InputTemplate`` include quote marks within a JSON string, escape each quote marks with a slash, as in the following example:
        
                     ``\"InputTransformer\":``  
        
                     ``{``  
        
                     ``\"InputPathsMap\": {\"instance\": \"$.detail.instance\",\"status\": \"$.detail.status\"},``  
        
                     ``\"InputTemplate\": \"<instance> is in state \\"<status>\\"\"``  
        
                     ``}``  
        
                - **KinesisParameters** *(dict) --* 
        
                  The custom parameter you can use to control the shard assignment, when the target is a Kinesis data stream. If you do not include this parameter, the default is to use the ``eventId`` as the partition key.
        
                  - **PartitionKeyPath** *(string) --* 
        
                    The JSON path to be extracted from the event and used as the partition key. For more information, see `Amazon Kinesis Streams Key Concepts <http://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#partition-key>`__ in the *Amazon Kinesis Streams Developer Guide* .
        
                - **RunCommandParameters** *(dict) --* 
        
                  Parameters used when you are using the rule to invoke Amazon EC2 Run Command.
        
                  - **RunCommandTargets** *(list) --* 
        
                    Currently, we support including only one RunCommandTarget block, which specifies either an array of InstanceIds or a tag.
        
                    - *(dict) --* 
        
                      Information about the EC2 instances that are to be sent the command, specified as key-value pairs. Each ``RunCommandTarget`` block can include only one key, but this key may specify multiple values.
        
                      - **Key** *(string) --* 
        
                        Can be either ``tag:``  *tag-key* or ``InstanceIds`` .
        
                      - **Values** *(list) --* 
        
                        If ``Key`` is ``tag:``  *tag-key* , ``Values`` is a list of tag values. If ``Key`` is ``InstanceIds`` , ``Values`` is a list of Amazon EC2 instance IDs.
        
                        - *(string) --* 
                    
                - **EcsParameters** *(dict) --* 
        
                  Contains the Amazon ECS task definition and task count to be used, if the event target is an Amazon ECS task. For more information about Amazon ECS tasks, see `Task Definitions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in the *Amazon EC2 Container Service Developer Guide* .
        
                  - **TaskDefinitionArn** *(string) --* 
        
                    The ARN of the task definition to use if the event target is an Amazon ECS task. 
        
                  - **TaskCount** *(integer) --* 
        
                    The number of tasks to create based on ``TaskDefinition`` . The default is 1.
        
                  - **LaunchType** *(string) --* 
        
                    Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The ``FARGATE`` value is supported only in the Regions where AWS Fargate with Amazon ECS is supported. For more information, see `AWS Fargate on Amazon ECS <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-Fargate.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        
                  - **NetworkConfiguration** *(dict) --* 
        
                    Use this structure if the ECS task uses the ``awsvpc`` network mode. This structure specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. This structure is required if ``LaunchType`` is ``FARGATE`` because the ``awsvpc`` mode is required for Fargate tasks.
        
                    If you specify ``NetworkConfiguration`` when the target ECS task does not use the ``awsvpc`` network mode, the task fails.
        
                    - **awsvpcConfiguration** *(dict) --* 
        
                      Use this structure to specify the VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the ``awsvpc`` network mode.
        
                      - **Subnets** *(list) --* 
        
                        Specifies the subnets associated with the task. These subnets must all be in the same VPC. You can specify as many as 16 subnets.
        
                        - *(string) --* 
                    
                      - **SecurityGroups** *(list) --* 
        
                        Specifies the security groups associated with the task. These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.
        
                        - *(string) --* 
                    
                      - **AssignPublicIp** *(string) --* 
        
                        Specifies whether the task\'s elastic network interface receives a public IP address. You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters`` is set to ``FARGATE`` .
        
                  - **PlatformVersion** *(string) --* 
        
                    Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as ``1.1.0`` .
        
                    This structure is used only if ``LaunchType`` is ``FARGATE`` . For more information about valid platform versions, see `AWS Fargate Platform Versions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        
                  - **Group** *(string) --* 
        
                    Specifies an ECS task group for the task. The maximum length is 255 characters.
        
                - **BatchParameters** *(dict) --* 
        
                  If the event target is an AWS Batch job, this contains the job definition, job name, and other parameters. For more information, see `Jobs <http://docs.aws.amazon.com/batch/latest/userguide/jobs.html>`__ in the *AWS Batch User Guide* .
        
                  - **JobDefinition** *(string) --* 
        
                    The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.
        
                  - **JobName** *(string) --* 
        
                    The name to use for this execution of the job, if the target is an AWS Batch job.
        
                  - **ArrayProperties** *(dict) --* 
        
                    The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. This parameter is used only if the target is an AWS Batch job.
        
                    - **Size** *(integer) --* 
        
                      The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.
        
                  - **RetryStrategy** *(dict) --* 
        
                    The retry strategy to use for failed jobs, if the target is an AWS Batch job. The retry strategy is the number of times to retry the failed job execution. Valid values are 1–10. When you specify a retry strategy here, it overrides the retry strategy defined in the job definition.
        
                    - **Attempts** *(integer) --* 
        
                      The number of times to attempt to retry, if the job fails. Valid values are 1–10.
        
                - **SqsParameters** *(dict) --* 
        
                  Contains the message group ID to use when the target is a FIFO queue.
        
                  If you specify an SQS FIFO queue as a target, the queue must have content-based deduplication enabled.
        
                  - **MessageGroupId** *(string) --* 
        
                    The FIFO message group ID to use as the target.
        
            - **NextToken** *(string) --* 
        
              Indicates whether there are additional results to retrieve. If there are no more results, the value is null.
        
        """
        pass

    def put_events(self, Entries: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/PutEvents>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_events(
              Entries=[
                  {
                      \'Time\': datetime(2015, 1, 1),
                      \'Source\': \'string\',
                      \'Resources\': [
                          \'string\',
                      ],
                      \'DetailType\': \'string\',
                      \'Detail\': \'string\'
                  },
              ]
          )
        :type Entries: list
        :param Entries: **[REQUIRED]** 
        
          The entry that defines an event in your system. You can specify several parameters for the entry such as the source and type of the event, resources associated with the event, and so on.
        
          - *(dict) --* 
        
            Represents an event to be submitted.
        
            - **Time** *(datetime) --* 
        
              The time stamp of the event, per `RFC3339 <https://www.rfc-editor.org/rfc/rfc3339.txt>`__ . If no time stamp is provided, the time stamp of the  PutEvents call is used.
        
            - **Source** *(string) --* 
        
              The source of the event. This field is required.
        
            - **Resources** *(list) --* 
        
              AWS resources, identified by Amazon Resource Name (ARN), which the event primarily concerns. Any number, including zero, may be present.
        
              - *(string) --* 
        
            - **DetailType** *(string) --* 
        
              Free-form string used to decide what fields to expect in the event detail.
        
            - **Detail** *(string) --* 
        
              A valid JSON string. There is no other schema imposed. The JSON string may contain fields and nested subobjects.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FailedEntryCount\': 123,
                \'Entries\': [
                    {
                        \'EventId\': \'string\',
                        \'ErrorCode\': \'string\',
                        \'ErrorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **FailedEntryCount** *(integer) --* 
        
              The number of failed entries.
        
            - **Entries** *(list) --* 
        
              The successfully and unsuccessfully ingested events results. If the ingestion was successful, the entry has the event ID in it. Otherwise, you can use the error code and error message to identify the problem with the entry.
        
              - *(dict) --* 
        
                Represents an event that failed to be submitted.
        
                - **EventId** *(string) --* 
        
                  The ID of the event.
        
                - **ErrorCode** *(string) --* 
        
                  The error code that indicates why the event submission failed.
        
                - **ErrorMessage** *(string) --* 
        
                  The error message that explains why the event submission failed.
        
        """
        pass

    def put_permission(self, Action: str, Principal: str, StatementId: str, Condition: Dict = None) -> NoReturn:
        """
        
        For another account to send events to your account, that external account must have a CloudWatch Events rule with your account\'s default event bus as a target.
        
        To enable multiple AWS accounts to put events to your default event bus, run ``PutPermission`` once for each of these accounts. Or, if all the accounts are members of the same AWS organization, you can run ``PutPermission`` once specifying ``Principal`` as \"*\" and specifying the AWS organization ID in ``Condition`` , to grant permissions to all accounts in that organization.
        
        If you grant permissions using an organization, then accounts in that organization must specify a ``RoleArn`` with proper permissions when they use ``PutTarget`` to add your account\'s event bus as a target. For more information, see `Sending and Receiving Events Between AWS Accounts <http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEvents-CrossAccountEventDelivery.html>`__ in the *Amazon CloudWatch Events User Guide* .
        
        The permission policy on the default event bus cannot exceed 10 KB in size.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/PutPermission>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_permission(
              Action=\'string\',
              Principal=\'string\',
              StatementId=\'string\',
              Condition={
                  \'Type\': \'string\',
                  \'Key\': \'string\',
                  \'Value\': \'string\'
              }
          )
        :type Action: string
        :param Action: **[REQUIRED]** 
        
          The action that you are enabling the other account to perform. Currently, this must be ``events:PutEvents`` .
        
        :type Principal: string
        :param Principal: **[REQUIRED]** 
        
          The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify \"*\" to permit any account to put events to your default event bus.
        
          If you specify \"*\" without specifying ``Condition`` , avoid creating rules that may match undesirable events. To create more secure rules, make sure that the event pattern for each rule contains an ``account`` field with a specific account ID from which to receive events. Rules with an account field do not match any events sent from other accounts.
        
        :type StatementId: string
        :param StatementId: **[REQUIRED]** 
        
          An identifier string for the external account that you are granting permissions to. If you later want to revoke the permission for this external account, specify this ``StatementId`` when you run  RemovePermission .
        
        :type Condition: dict
        :param Condition: 
        
          This parameter enables you to limit the permission to accounts that fulfill a certain condition, such as being a member of a certain AWS organization. For more information about AWS Organizations, see `What Is AWS Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html>`__ in the *AWS Organizations User Guide* .
        
          If you specify ``Condition`` with an AWS organization ID, and specify \"*\" as the value for ``Principal`` , you grant permission to all the accounts in the named organization.
        
          The ``Condition`` is a JSON string which must contain ``Type`` , ``Key`` , and ``Value`` fields.
        
          - **Type** *(string) --* **[REQUIRED]** 
        
            Specifies the type of condition. Currently the only supported value is ``StringEquals`` .
        
          - **Key** *(string) --* **[REQUIRED]** 
        
            Specifies the key for the condition. Currently the only supported key is ``aws:PrincipalOrgID`` .
        
          - **Value** *(string) --* **[REQUIRED]** 
        
            Specifies the value for the key. Currently, this must be the ID of the organization.
        
        :returns: None
        """
        pass

    def put_rule(self, Name: str, ScheduleExpression: str = None, EventPattern: str = None, State: str = None, Description: str = None, RoleArn: str = None) -> Dict:
        """
        
        If you are updating an existing rule, the rule is replaced with what you specify in this ``PutRule`` command. If you omit arguments in ``PutRule`` , the old values for those arguments are not kept. Instead, they are replaced with null values.
        
        When you create or update a rule, incoming events might not immediately start matching to new or updated rules. Allow a short period of time for changes to take effect.
        
        A rule must contain at least an EventPattern or ScheduleExpression. Rules with EventPatterns are triggered when a matching event is observed. Rules with ScheduleExpressions self-trigger based on the given schedule. A rule can have both an EventPattern and a ScheduleExpression, in which case the rule triggers on matching events as well as on a schedule.
        
        Most services in AWS treat : or / as the same character in Amazon Resource Names (ARNs). However, CloudWatch Events uses an exact match in event patterns and rules. Be sure to use the correct ARN characters when creating event patterns so that they match the ARN syntax in the event you want to match.
        
        In CloudWatch Events, it is possible to create rules that lead to infinite loops, where a rule is fired repeatedly. For example, a rule might detect that ACLs have changed on an S3 bucket, and trigger software to change them to the desired state. If the rule is not written carefully, the subsequent change to the ACLs fires the rule again, creating an infinite loop.
        
        To prevent this, write the rules so that the triggered actions do not re-fire the same rule. For example, your rule could fire only if ACLs are found to be in a bad state, instead of after any change. 
        
        An infinite loop can quickly cause higher than expected charges. We recommend that you use budgeting, which alerts you when charges exceed your specified limit. For more information, see `Managing Your Costs with Budgets <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/PutRule>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_rule(
              Name=\'string\',
              ScheduleExpression=\'string\',
              EventPattern=\'string\',
              State=\'ENABLED\'|\'DISABLED\',
              Description=\'string\',
              RoleArn=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the rule that you are creating or updating.
        
        :type ScheduleExpression: string
        :param ScheduleExpression: 
        
          The scheduling expression. For example, \"cron(0 20 * * ? *)\" or \"rate(5 minutes)\".
        
        :type EventPattern: string
        :param EventPattern: 
        
          The event pattern. For more information, see `Events and Event Patterns <http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html>`__ in the *Amazon CloudWatch Events User Guide* .
        
        :type State: string
        :param State: 
        
          Indicates whether the rule is enabled or disabled.
        
        :type Description: string
        :param Description: 
        
          A description of the rule.
        
        :type RoleArn: string
        :param RoleArn: 
        
          The Amazon Resource Name (ARN) of the IAM role associated with the rule.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RuleArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **RuleArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the rule.
        
        """
        pass

    def put_targets(self, Rule: str, Targets: List) -> Dict:
        """
        
        Targets are the resources that are invoked when a rule is triggered.
        
        You can configure the following as targets for CloudWatch Events:
        
        * EC2 instances 
         
        * SSM Run Command 
         
        * SSM Automation 
         
        * AWS Lambda functions 
         
        * Data streams in Amazon Kinesis Data Streams 
         
        * Data delivery streams in Amazon Kinesis Data Firehose 
         
        * Amazon ECS tasks 
         
        * AWS Step Functions state machines 
         
        * AWS Batch jobs 
         
        * AWS CodeBuild projects 
         
        * Pipelines in AWS CodePipeline 
         
        * Amazon Inspector assessment templates 
         
        * Amazon SNS topics 
         
        * Amazon SQS queues, including FIFO queues 
         
        * The default event bus of another AWS account 
         
        Creating rules with built-in targets is supported only in the AWS Management Console. The built-in targets are ``EC2 CreateSnapshot API call`` , ``EC2 RebootInstances API call`` , ``EC2 StopInstances API call`` , and ``EC2 TerminateInstances API call`` . 
        
        For some target types, ``PutTargets`` provides target-specific parameters. If the target is a Kinesis data stream, you can optionally specify which shard the event goes to by using the ``KinesisParameters`` argument. To invoke a command on multiple EC2 instances with one rule, you can use the ``RunCommandParameters`` field.
        
        To be able to make API calls against the resources that you own, Amazon CloudWatch Events needs the appropriate permissions. For AWS Lambda and Amazon SNS resources, CloudWatch Events relies on resource-based policies. For EC2 instances, Kinesis data streams, and AWS Step Functions state machines, CloudWatch Events relies on IAM roles that you specify in the ``RoleARN`` argument in ``PutTargets`` . For more information, see `Authentication and Access Control <http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/auth-and-access-control-cwe.html>`__ in the *Amazon CloudWatch Events User Guide* .
        
        If another AWS account is in the same region and has granted you permission (using ``PutPermission`` ), you can send events to that account. Set that account\'s event bus as a target of the rules in your account. To send the matched events to the other account, specify that account\'s event bus as the ``Arn`` value when you run ``PutTargets`` . If your account sends events to another account, your account is charged for each sent event. Each event sent to another account is charged as a custom event. The account receiving the event is not charged. For more information, see `Amazon CloudWatch Pricing <https://aws.amazon.com/cloudwatch/pricing/>`__ .
        
        If you are setting the event bus of another account as the target, and that account granted permission to your account through an organization instead of directly by the account ID, then you must specify a ``RoleArn`` with proper permissions in the ``Target`` structure. For more information, see `Sending and Receiving Events Between AWS Accounts <http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEvents-CrossAccountEventDelivery.html>`__ in the *Amazon CloudWatch Events User Guide* .
        
        For more information about enabling cross-account events, see  PutPermission .
        
         **Input** , **InputPath** , and **InputTransformer** are mutually exclusive and optional parameters of a target. When a rule is triggered due to a matched event:
        
        * If none of the following arguments are specified for a target, then the entire event is passed to the target in JSON format (unless the target is Amazon EC2 Run Command or Amazon ECS task, in which case nothing from the event is passed to the target). 
         
        * If **Input** is specified in the form of valid JSON, then the matched event is overridden with this constant. 
         
        * If **InputPath** is specified in the form of JSONPath (for example, ``$.detail`` ), then only the part of the event specified in the path is passed to the target (for example, only the detail part of the event is passed). 
         
        * If **InputTransformer** is specified, then one or more specified JSONPaths are extracted from the event and used as values in a template that you specify as the input to the target. 
         
        When you specify ``InputPath`` or ``InputTransformer`` , you must use JSON dot notation, not bracket notation.
        
        When you add targets to a rule and the associated rule triggers soon after, new or updated targets might not be immediately invoked. Allow a short period of time for changes to take effect.
        
        This action can partially fail if too many requests are made at the same time. If that happens, ``FailedEntryCount`` is non-zero in the response and each entry in ``FailedEntries`` provides the ID of the failed target and the error code.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/PutTargets>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_targets(
              Rule=\'string\',
              Targets=[
                  {
                      \'Id\': \'string\',
                      \'Arn\': \'string\',
                      \'RoleArn\': \'string\',
                      \'Input\': \'string\',
                      \'InputPath\': \'string\',
                      \'InputTransformer\': {
                          \'InputPathsMap\': {
                              \'string\': \'string\'
                          },
                          \'InputTemplate\': \'string\'
                      },
                      \'KinesisParameters\': {
                          \'PartitionKeyPath\': \'string\'
                      },
                      \'RunCommandParameters\': {
                          \'RunCommandTargets\': [
                              {
                                  \'Key\': \'string\',
                                  \'Values\': [
                                      \'string\',
                                  ]
                              },
                          ]
                      },
                      \'EcsParameters\': {
                          \'TaskDefinitionArn\': \'string\',
                          \'TaskCount\': 123,
                          \'LaunchType\': \'EC2\'|\'FARGATE\',
                          \'NetworkConfiguration\': {
                              \'awsvpcConfiguration\': {
                                  \'Subnets\': [
                                      \'string\',
                                  ],
                                  \'SecurityGroups\': [
                                      \'string\',
                                  ],
                                  \'AssignPublicIp\': \'ENABLED\'|\'DISABLED\'
                              }
                          },
                          \'PlatformVersion\': \'string\',
                          \'Group\': \'string\'
                      },
                      \'BatchParameters\': {
                          \'JobDefinition\': \'string\',
                          \'JobName\': \'string\',
                          \'ArrayProperties\': {
                              \'Size\': 123
                          },
                          \'RetryStrategy\': {
                              \'Attempts\': 123
                          }
                      },
                      \'SqsParameters\': {
                          \'MessageGroupId\': \'string\'
                      }
                  },
              ]
          )
        :type Rule: string
        :param Rule: **[REQUIRED]** 
        
          The name of the rule.
        
        :type Targets: list
        :param Targets: **[REQUIRED]** 
        
          The targets to update or add to the rule.
        
          - *(dict) --* 
        
            Targets are the resources to be invoked when a rule is triggered. For a complete list of services and resources that can be set as a target, see  PutTargets .
        
            If you are setting the event bus of another account as the target, and that account granted permission to your account through an organization instead of directly by the account ID, then you must specify a ``RoleArn`` with proper permissions in the ``Target`` structure. For more information, see `Sending and Receiving Events Between AWS Accounts <http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEvents-CrossAccountEventDelivery.html>`__ in the *Amazon CloudWatch Events User Guide* .
        
            - **Id** *(string) --* **[REQUIRED]** 
        
              The ID of the target.
        
            - **Arn** *(string) --* **[REQUIRED]** 
        
              The Amazon Resource Name (ARN) of the target.
        
            - **RoleArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. If one rule triggers multiple targets, you can use a different IAM role for each target.
        
            - **Input** *(string) --* 
        
              Valid JSON text passed to the target. In this case, nothing from the event itself is passed to the target. For more information, see `The JavaScript Object Notation (JSON) Data Interchange Format <http://www.rfc-editor.org/rfc/rfc7159.txt>`__ .
        
            - **InputPath** *(string) --* 
        
              The value of the JSONPath that is used for extracting part of the matched event when passing it to the target. You must use JSON dot notation, not bracket notation. For more information about JSON paths, see `JSONPath <http://goessner.net/articles/JsonPath/>`__ .
        
            - **InputTransformer** *(dict) --* 
        
              Settings to enable you to provide custom input to a target based on certain event data. You can extract one or more key-value pairs from the event and then use that data to send customized input to the target.
        
              - **InputPathsMap** *(dict) --* 
        
                Map of JSON paths to be extracted from the event. You can then insert these in the template in ``InputTemplate`` to produce the output you want to be sent to the target.
        
                 ``InputPathsMap`` is an array key-value pairs, where each value is a valid JSON path. You can have as many as 10 key-value pairs. You must use JSON dot notation, not bracket notation.
        
                The keys cannot start with \"AWS.\" 
        
                - *(string) --* 
        
                  - *(string) --* 
        
              - **InputTemplate** *(string) --* **[REQUIRED]** 
        
                Input template where you specify placeholders that will be filled with the values of the keys from ``InputPathsMap`` to customize the data sent to the target. Enclose each ``InputPathsMaps`` value in brackets: <*value* > The InputTemplate must be valid JSON.
        
                If ``InputTemplate`` is a JSON object (surrounded by curly braces), the following restrictions apply:
        
                * The placeholder cannot be used as an object key. 
                 
                * Object values cannot include quote marks. 
                 
                The following example shows the syntax for using ``InputPathsMap`` and ``InputTemplate`` .
        
                 ``\"InputTransformer\":``  
        
                 ``{``  
        
                 ``\"InputPathsMap\": {\"instance\": \"$.detail.instance\",\"status\": \"$.detail.status\"},``  
        
                 ``\"InputTemplate\": \"<instance> is in state <status>\"``  
        
                 ``}``  
        
                To have the ``InputTemplate`` include quote marks within a JSON string, escape each quote marks with a slash, as in the following example:
        
                 ``\"InputTransformer\":``  
        
                 ``{``  
        
                 ``\"InputPathsMap\": {\"instance\": \"$.detail.instance\",\"status\": \"$.detail.status\"},``  
        
                 ``\"InputTemplate\": \"<instance> is in state \\"<status>\\"\"``  
        
                 ``}``  
        
            - **KinesisParameters** *(dict) --* 
        
              The custom parameter you can use to control the shard assignment, when the target is a Kinesis data stream. If you do not include this parameter, the default is to use the ``eventId`` as the partition key.
        
              - **PartitionKeyPath** *(string) --* **[REQUIRED]** 
        
                The JSON path to be extracted from the event and used as the partition key. For more information, see `Amazon Kinesis Streams Key Concepts <http://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#partition-key>`__ in the *Amazon Kinesis Streams Developer Guide* .
        
            - **RunCommandParameters** *(dict) --* 
        
              Parameters used when you are using the rule to invoke Amazon EC2 Run Command.
        
              - **RunCommandTargets** *(list) --* **[REQUIRED]** 
        
                Currently, we support including only one RunCommandTarget block, which specifies either an array of InstanceIds or a tag.
        
                - *(dict) --* 
        
                  Information about the EC2 instances that are to be sent the command, specified as key-value pairs. Each ``RunCommandTarget`` block can include only one key, but this key may specify multiple values.
        
                  - **Key** *(string) --* **[REQUIRED]** 
        
                    Can be either ``tag:``  *tag-key* or ``InstanceIds`` .
        
                  - **Values** *(list) --* **[REQUIRED]** 
        
                    If ``Key`` is ``tag:``  *tag-key* , ``Values`` is a list of tag values. If ``Key`` is ``InstanceIds`` , ``Values`` is a list of Amazon EC2 instance IDs.
        
                    - *(string) --* 
        
            - **EcsParameters** *(dict) --* 
        
              Contains the Amazon ECS task definition and task count to be used, if the event target is an Amazon ECS task. For more information about Amazon ECS tasks, see `Task Definitions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in the *Amazon EC2 Container Service Developer Guide* .
        
              - **TaskDefinitionArn** *(string) --* **[REQUIRED]** 
        
                The ARN of the task definition to use if the event target is an Amazon ECS task. 
        
              - **TaskCount** *(integer) --* 
        
                The number of tasks to create based on ``TaskDefinition`` . The default is 1.
        
              - **LaunchType** *(string) --* 
        
                Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The ``FARGATE`` value is supported only in the Regions where AWS Fargate with Amazon ECS is supported. For more information, see `AWS Fargate on Amazon ECS <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-Fargate.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        
              - **NetworkConfiguration** *(dict) --* 
        
                Use this structure if the ECS task uses the ``awsvpc`` network mode. This structure specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. This structure is required if ``LaunchType`` is ``FARGATE`` because the ``awsvpc`` mode is required for Fargate tasks.
        
                If you specify ``NetworkConfiguration`` when the target ECS task does not use the ``awsvpc`` network mode, the task fails.
        
                - **awsvpcConfiguration** *(dict) --* 
        
                  Use this structure to specify the VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the ``awsvpc`` network mode.
        
                  - **Subnets** *(list) --* **[REQUIRED]** 
        
                    Specifies the subnets associated with the task. These subnets must all be in the same VPC. You can specify as many as 16 subnets.
        
                    - *(string) --* 
        
                  - **SecurityGroups** *(list) --* 
        
                    Specifies the security groups associated with the task. These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.
        
                    - *(string) --* 
        
                  - **AssignPublicIp** *(string) --* 
        
                    Specifies whether the task\'s elastic network interface receives a public IP address. You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters`` is set to ``FARGATE`` .
        
              - **PlatformVersion** *(string) --* 
        
                Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as ``1.1.0`` .
        
                This structure is used only if ``LaunchType`` is ``FARGATE`` . For more information about valid platform versions, see `AWS Fargate Platform Versions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        
              - **Group** *(string) --* 
        
                Specifies an ECS task group for the task. The maximum length is 255 characters.
        
            - **BatchParameters** *(dict) --* 
        
              If the event target is an AWS Batch job, this contains the job definition, job name, and other parameters. For more information, see `Jobs <http://docs.aws.amazon.com/batch/latest/userguide/jobs.html>`__ in the *AWS Batch User Guide* .
        
              - **JobDefinition** *(string) --* **[REQUIRED]** 
        
                The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.
        
              - **JobName** *(string) --* **[REQUIRED]** 
        
                The name to use for this execution of the job, if the target is an AWS Batch job.
        
              - **ArrayProperties** *(dict) --* 
        
                The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. This parameter is used only if the target is an AWS Batch job.
        
                - **Size** *(integer) --* 
        
                  The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.
        
              - **RetryStrategy** *(dict) --* 
        
                The retry strategy to use for failed jobs, if the target is an AWS Batch job. The retry strategy is the number of times to retry the failed job execution. Valid values are 1–10. When you specify a retry strategy here, it overrides the retry strategy defined in the job definition.
        
                - **Attempts** *(integer) --* 
        
                  The number of times to attempt to retry, if the job fails. Valid values are 1–10.
        
            - **SqsParameters** *(dict) --* 
        
              Contains the message group ID to use when the target is a FIFO queue.
        
              If you specify an SQS FIFO queue as a target, the queue must have content-based deduplication enabled.
        
              - **MessageGroupId** *(string) --* 
        
                The FIFO message group ID to use as the target.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FailedEntryCount\': 123,
                \'FailedEntries\': [
                    {
                        \'TargetId\': \'string\',
                        \'ErrorCode\': \'string\',
                        \'ErrorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **FailedEntryCount** *(integer) --* 
        
              The number of failed entries.
        
            - **FailedEntries** *(list) --* 
        
              The failed target entries.
        
              - *(dict) --* 
        
                Represents a target that failed to be added to a rule.
        
                - **TargetId** *(string) --* 
        
                  The ID of the target.
        
                - **ErrorCode** *(string) --* 
        
                  The error code that indicates why the target addition failed. If the value is ``ConcurrentModificationException`` , too many requests were made at the same time.
        
                - **ErrorMessage** *(string) --* 
        
                  The error message that explains why the target addition failed.
        
        """
        pass

    def remove_permission(self, StatementId: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/RemovePermission>`_
        
        **Request Syntax** 
        ::
        
          response = client.remove_permission(
              StatementId=\'string\'
          )
        :type StatementId: string
        :param StatementId: **[REQUIRED]** 
        
          The statement ID corresponding to the account that is no longer allowed to put events to the default event bus.
        
        :returns: None
        """
        pass

    def remove_targets(self, Rule: str, Ids: List) -> Dict:
        """
        
        When you remove a target, when the associated rule triggers, removed targets might continue to be invoked. Allow a short period of time for changes to take effect.
        
        This action can partially fail if too many requests are made at the same time. If that happens, ``FailedEntryCount`` is non-zero in the response and each entry in ``FailedEntries`` provides the ID of the failed target and the error code.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/RemoveTargets>`_
        
        **Request Syntax** 
        ::
        
          response = client.remove_targets(
              Rule=\'string\',
              Ids=[
                  \'string\',
              ]
          )
        :type Rule: string
        :param Rule: **[REQUIRED]** 
        
          The name of the rule.
        
        :type Ids: list
        :param Ids: **[REQUIRED]** 
        
          The IDs of the targets to remove from the rule.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FailedEntryCount\': 123,
                \'FailedEntries\': [
                    {
                        \'TargetId\': \'string\',
                        \'ErrorCode\': \'string\',
                        \'ErrorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **FailedEntryCount** *(integer) --* 
        
              The number of failed entries.
        
            - **FailedEntries** *(list) --* 
        
              The failed target entries.
        
              - *(dict) --* 
        
                Represents a target that failed to be removed from a rule.
        
                - **TargetId** *(string) --* 
        
                  The ID of the target.
        
                - **ErrorCode** *(string) --* 
        
                  The error code that indicates why the target removal failed. If the value is ``ConcurrentModificationException`` , too many requests were made at the same time.
        
                - **ErrorMessage** *(string) --* 
        
                  The error message that explains why the target removal failed.
        
        """
        pass

    def test_event_pattern(self, EventPattern: str, Event: str) -> Dict:
        """
        
        Most services in AWS treat : or / as the same character in Amazon Resource Names (ARNs). However, CloudWatch Events uses an exact match in event patterns and rules. Be sure to use the correct ARN characters when creating event patterns so that they match the ARN syntax in the event you want to match.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/events-2015-10-07/TestEventPattern>`_
        
        **Request Syntax** 
        ::
        
          response = client.test_event_pattern(
              EventPattern=\'string\',
              Event=\'string\'
          )
        :type EventPattern: string
        :param EventPattern: **[REQUIRED]** 
        
          The event pattern. For more information, see `Events and Event Patterns <http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html>`__ in the *Amazon CloudWatch Events User Guide* .
        
        :type Event: string
        :param Event: **[REQUIRED]** 
        
          The event, in JSON format, to test against the event pattern.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Result\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Result** *(boolean) --* 
        
              Indicates whether the event matches the event pattern.
        
        """
        pass
