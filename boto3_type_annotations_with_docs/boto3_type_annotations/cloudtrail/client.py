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
    def add_tags(self, ResourceId: str, TagsList: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/AddTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.add_tags(
              ResourceId=\'string\',
              TagsList=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          Specifies the ARN of the trail to which one or more tags will be added. The format of a trail ARN is:
        
           ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``  
        
        :type TagsList: list
        :param TagsList: 
        
          Contains a list of CloudTrail tags, up to a limit of 50
        
          - *(dict) --* 
        
            A custom key-value pair associated with a resource such as a CloudTrail trail.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The key in a key-value pair. The key must be must be no longer than 128 Unicode characters. The key must be unique for the resource to which it applies.
        
            - **Value** *(string) --* 
        
              The value in a key-value pair of a tag. The value must be no longer than 256 Unicode characters.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Returns the objects or data listed below if successful. Otherwise, returns an error.
        
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

    def create_trail(self, Name: str, S3BucketName: str, S3KeyPrefix: str = None, SnsTopicName: str = None, IncludeGlobalServiceEvents: bool = None, IsMultiRegionTrail: bool = None, EnableLogFileValidation: bool = None, CloudWatchLogsLogGroupArn: str = None, CloudWatchLogsRoleArn: str = None, KmsKeyId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/CreateTrail>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_trail(
              Name=\'string\',
              S3BucketName=\'string\',
              S3KeyPrefix=\'string\',
              SnsTopicName=\'string\',
              IncludeGlobalServiceEvents=True|False,
              IsMultiRegionTrail=True|False,
              EnableLogFileValidation=True|False,
              CloudWatchLogsLogGroupArn=\'string\',
              CloudWatchLogsRoleArn=\'string\',
              KmsKeyId=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Specifies the name of the trail. The name must meet the following requirements:
        
          * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-) 
           
          * Start with a letter or number, and end with a letter or number 
           
          * Be between 3 and 128 characters 
           
          * Have no adjacent periods, underscores or dashes. Names like ``my-_namespace`` and ``my--namespace`` are invalid. 
           
          * Not be in IP address format (for example, 192.168.5.4) 
           
        :type S3BucketName: string
        :param S3BucketName: **[REQUIRED]** 
        
          Specifies the name of the Amazon S3 bucket designated for publishing log files. See `Amazon S3 Bucket Naming Requirements <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/create_trail_naming_policy.html>`__ .
        
        :type S3KeyPrefix: string
        :param S3KeyPrefix: 
        
          Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see `Finding Your CloudTrail Log Files <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-find-log-files.html>`__ . The maximum length is 200 characters.
        
        :type SnsTopicName: string
        :param SnsTopicName: 
        
          Specifies the name of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.
        
        :type IncludeGlobalServiceEvents: boolean
        :param IncludeGlobalServiceEvents: 
        
          Specifies whether the trail is publishing events from global services such as IAM to the log files.
        
        :type IsMultiRegionTrail: boolean
        :param IsMultiRegionTrail: 
        
          Specifies whether the trail is created in the current region or in all regions. The default is false.
        
        :type EnableLogFileValidation: boolean
        :param EnableLogFileValidation: 
        
          Specifies whether log file integrity validation is enabled. The default is false.
        
          .. note::
        
            When you disable log file integrity validation, the chain of digest files is broken after one hour. CloudTrail will not create digest files for log files that were delivered during a period in which log file integrity validation was disabled. For example, if you enable log file integrity validation at noon on January 1, disable it at noon on January 2, and re-enable it at noon on January 10, digest files will not be created for the log files delivered from noon on January 2 to noon on January 10. The same applies whenever you stop CloudTrail logging or delete a trail.
        
        :type CloudWatchLogsLogGroupArn: string
        :param CloudWatchLogsLogGroupArn: 
        
          Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered. Not required unless you specify CloudWatchLogsRoleArn.
        
        :type CloudWatchLogsRoleArn: string
        :param CloudWatchLogsRoleArn: 
        
          Specifies the role for the CloudWatch Logs endpoint to assume to write to a user\'s log group.
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          Specifies the KMS key ID to use to encrypt the logs delivered by CloudTrail. The value can be an alias name prefixed by \"alias/\", a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
        
          Examples:
        
          * alias/MyAliasName 
           
          * arn:aws:kms:us-east-2:123456789012:alias/MyAliasName 
           
          * arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012 
           
          * 12345678-1234-1234-1234-123456789012 
           
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Name\': \'string\',
                \'S3BucketName\': \'string\',
                \'S3KeyPrefix\': \'string\',
                \'SnsTopicName\': \'string\',
                \'SnsTopicARN\': \'string\',
                \'IncludeGlobalServiceEvents\': True|False,
                \'IsMultiRegionTrail\': True|False,
                \'TrailARN\': \'string\',
                \'LogFileValidationEnabled\': True|False,
                \'CloudWatchLogsLogGroupArn\': \'string\',
                \'CloudWatchLogsRoleArn\': \'string\',
                \'KmsKeyId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Returns the objects or data listed below if successful. Otherwise, returns an error.
        
            - **Name** *(string) --* 
        
              Specifies the name of the trail.
        
            - **S3BucketName** *(string) --* 
        
              Specifies the name of the Amazon S3 bucket designated for publishing log files.
        
            - **S3KeyPrefix** *(string) --* 
        
              Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see `Finding Your CloudTrail Log Files <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-find-log-files.html>`__ .
        
            - **SnsTopicName** *(string) --* 
        
              This field is deprecated. Use SnsTopicARN.
        
            - **SnsTopicARN** *(string) --* 
        
              Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The format of a topic ARN is:
        
               ``arn:aws:sns:us-east-2:123456789012:MyTopic``  
        
            - **IncludeGlobalServiceEvents** *(boolean) --* 
        
              Specifies whether the trail is publishing events from global services such as IAM to the log files.
        
            - **IsMultiRegionTrail** *(boolean) --* 
        
              Specifies whether the trail exists in one region or in all regions.
        
            - **TrailARN** *(string) --* 
        
              Specifies the ARN of the trail that was created. The format of a trail ARN is:
        
               ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``  
        
            - **LogFileValidationEnabled** *(boolean) --* 
        
              Specifies whether log file integrity validation is enabled.
        
            - **CloudWatchLogsLogGroupArn** *(string) --* 
        
              Specifies the Amazon Resource Name (ARN) of the log group to which CloudTrail logs will be delivered.
        
            - **CloudWatchLogsRoleArn** *(string) --* 
        
              Specifies the role for the CloudWatch Logs endpoint to assume to write to a user\'s log group.
        
            - **KmsKeyId** *(string) --* 
        
              Specifies the KMS key ID that encrypts the logs delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the format:
        
               ``arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012``  
        
        """
        pass

    def delete_trail(self, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/DeleteTrail>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_trail(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Specifies the name or the CloudTrail ARN of the trail to be deleted. The format of a trail ARN is: ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Returns the objects or data listed below if successful. Otherwise, returns an error.
        
        """
        pass

    def describe_trails(self, trailNameList: List = None, includeShadowTrails: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/DescribeTrails>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_trails(
              trailNameList=[
                  \'string\',
              ],
              includeShadowTrails=True|False
          )
        :type trailNameList: list
        :param trailNameList: 
        
          Specifies a list of trail names, trail ARNs, or both, of the trails to describe. The format of a trail ARN is:
        
           ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``  
        
          If an empty list is specified, information for the trail in the current region is returned.
        
          * If an empty list is specified and ``IncludeShadowTrails`` is false, then information for all trails in the current region is returned. 
           
          * If an empty list is specified and IncludeShadowTrails is null or true, then information for all trails in the current region and any associated shadow trails in other regions is returned. 
           
          .. note::
        
            If one or more trail names are specified, information is returned only if the names match the names of trails belonging only to the current region. To return information about a trail in another region, you must specify its trail ARN.
        
          - *(string) --* 
        
        :type includeShadowTrails: boolean
        :param includeShadowTrails: 
        
          Specifies whether to include shadow trails in the response. A shadow trail is the replication in a region of a trail that was created in a different region. The default is true.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'trailList\': [
                    {
                        \'Name\': \'string\',
                        \'S3BucketName\': \'string\',
                        \'S3KeyPrefix\': \'string\',
                        \'SnsTopicName\': \'string\',
                        \'SnsTopicARN\': \'string\',
                        \'IncludeGlobalServiceEvents\': True|False,
                        \'IsMultiRegionTrail\': True|False,
                        \'HomeRegion\': \'string\',
                        \'TrailARN\': \'string\',
                        \'LogFileValidationEnabled\': True|False,
                        \'CloudWatchLogsLogGroupArn\': \'string\',
                        \'CloudWatchLogsRoleArn\': \'string\',
                        \'KmsKeyId\': \'string\',
                        \'HasCustomEventSelectors\': True|False
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Returns the objects or data listed below if successful. Otherwise, returns an error.
        
            - **trailList** *(list) --* 
        
              The list of trail objects.
        
              - *(dict) --* 
        
                The settings for a trail.
        
                - **Name** *(string) --* 
        
                  Name of the trail set by calling  CreateTrail . The maximum length is 128 characters.
        
                - **S3BucketName** *(string) --* 
        
                  Name of the Amazon S3 bucket into which CloudTrail delivers your trail files. See `Amazon S3 Bucket Naming Requirements <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/create_trail_naming_policy.html>`__ .
        
                - **S3KeyPrefix** *(string) --* 
        
                  Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see `Finding Your CloudTrail Log Files <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-find-log-files.html>`__ .The maximum length is 200 characters.
        
                - **SnsTopicName** *(string) --* 
        
                  This field is deprecated. Use SnsTopicARN.
        
                - **SnsTopicARN** *(string) --* 
        
                  Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The format of a topic ARN is:
        
                   ``arn:aws:sns:us-east-2:123456789012:MyTopic``  
        
                - **IncludeGlobalServiceEvents** *(boolean) --* 
        
                  Set to **True** to include AWS API calls from AWS global services such as IAM. Otherwise, **False** .
        
                - **IsMultiRegionTrail** *(boolean) --* 
        
                  Specifies whether the trail belongs only to one region or exists in all regions.
        
                - **HomeRegion** *(string) --* 
        
                  The region in which the trail was created.
        
                - **TrailARN** *(string) --* 
        
                  Specifies the ARN of the trail. The format of a trail ARN is:
        
                   ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``  
        
                - **LogFileValidationEnabled** *(boolean) --* 
        
                  Specifies whether log file validation is enabled.
        
                - **CloudWatchLogsLogGroupArn** *(string) --* 
        
                  Specifies an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered.
        
                - **CloudWatchLogsRoleArn** *(string) --* 
        
                  Specifies the role for the CloudWatch Logs endpoint to assume to write to a user\'s log group.
        
                - **KmsKeyId** *(string) --* 
        
                  Specifies the KMS key ID that encrypts the logs delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the format:
        
                   ``arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012``  
        
                - **HasCustomEventSelectors** *(boolean) --* 
        
                  Specifies if the trail has custom event selectors.
        
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

    def get_event_selectors(self, TrailName: str) -> Dict:
        """
        Describes the settings for the event selectors that you configured for your trail. The information returned for your event selectors includes the following:
        
        * If your event selector includes read-only events, write-only events, or all events. This applies to both management events and data events. 
         
        * If your event selector includes management events. 
         
        * If your event selector includes data events, the Amazon S3 objects or AWS Lambda functions that you are logging for data events. 
         
        For more information, see `Logging Data and Management Events for Trails <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html>`__ in the *AWS CloudTrail User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/GetEventSelectors>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_event_selectors(
              TrailName=\'string\'
          )
        :type TrailName: string
        :param TrailName: **[REQUIRED]** 
        
          Specifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:
        
          * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-) 
           
          * Start with a letter or number, and end with a letter or number 
           
          * Be between 3 and 128 characters 
           
          * Have no adjacent periods, underscores or dashes. Names like ``my-_namespace`` and ``my--namespace`` are not valid. 
           
          * Not be in IP address format (for example, 192.168.5.4) 
           
          If you specify a trail ARN, it must be in the format:
        
           ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TrailARN\': \'string\',
                \'EventSelectors\': [
                    {
                        \'ReadWriteType\': \'ReadOnly\'|\'WriteOnly\'|\'All\',
                        \'IncludeManagementEvents\': True|False,
                        \'DataResources\': [
                            {
                                \'Type\': \'string\',
                                \'Values\': [
                                    \'string\',
                                ]
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TrailARN** *(string) --* 
        
              The specified trail ARN that has the event selectors.
        
            - **EventSelectors** *(list) --* 
        
              The event selectors that are configured for the trail.
        
              - *(dict) --* 
        
                Use event selectors to further specify the management and data event settings for your trail. By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn\'t match any event selector, the trail doesn\'t log the event.
        
                You can configure up to five event selectors for a trail.
        
                - **ReadWriteType** *(string) --* 
        
                  Specify if you want your trail to log read-only events, write-only events, or all. For example, the EC2 ``GetConsoleOutput`` is a read-only API operation and ``RunInstances`` is a write-only API operation.
        
                  By default, the value is ``All`` .
        
                - **IncludeManagementEvents** *(boolean) --* 
        
                  Specify if you want your event selector to include management events for your trail.
        
                  For more information, see `Management Events <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-management-events>`__ in the *AWS CloudTrail User Guide* .
        
                  By default, the value is ``true`` .
        
                - **DataResources** *(list) --* 
        
                  CloudTrail supports data event logging for Amazon S3 objects and AWS Lambda functions. You can specify up to 250 resources for an individual event selector, but the total number of data resources cannot exceed 250 across all event selectors in a trail. This limit does not apply if you configure resource logging for all data events. 
        
                  For more information, see `Data Events <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-data-events>`__ and `Limits in AWS CloudTrail <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html>`__ in the *AWS CloudTrail User Guide* .
        
                  - *(dict) --* 
        
                    The Amazon S3 buckets or AWS Lambda functions that you specify in your event selectors for your trail to log data events. Data events provide insight into the resource operations performed on or within a resource itself. These are also known as data plane operations. You can specify up to 250 data resources for a trail.
        
                    .. note::
        
                      The total number of allowed data resources is 250. This number can be distributed between 1 and 5 event selectors, but the total cannot exceed 250 across all selectors.
        
                    The following example demonstrates how logging works when you configure logging of all data events for an S3 bucket named ``bucket-1`` . In this example, the CloudTrail user spcified an empty prefix, and the option to log both ``Read`` and ``Write`` data events.
        
                    * A user uploads an image file to ``bucket-1`` . 
                     
                    * The ``PutObject`` API operation is an Amazon S3 object-level API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an empty prefix, events that occur on any object in that bucket are logged. The trail processes and logs the event. 
                     
                    * A user uploads an object to an Amazon S3 bucket named ``arn:aws:s3:::bucket-2`` . 
                     
                    * The ``PutObject`` API operation occurred for an object in an S3 bucket that the CloudTrail user didn\'t specify for the trail. The trail doesn’t log the event. 
                     
                    The following example demonstrates how logging works when you configure logging of AWS Lambda data events for a Lambda function named *MyLambdaFunction* , but not for all AWS Lambda functions.
        
                    * A user runs a script that includes a call to the *MyLambdaFunction* function and the *MyOtherLambdaFunction* function. 
                     
                    * The ``Invoke`` API operation on *MyLambdaFunction* is an AWS Lambda API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified logging data events for *MyLambdaFunction* , any invocations of that function are logged. The trail processes and logs the event.  
                     
                    * The ``Invoke`` API operation on *MyOtherLambdaFunction* is an AWS Lambda API. Because the CloudTrail user did not specify logging data events for all Lambda functions, the ``Invoke`` operation for *MyOtherLambdaFunction* does not match the function specified for the trail. The trail doesn’t log the event.  
                     
                    - **Type** *(string) --* 
        
                      The resource type in which you want to log data events. You can specify ``AWS::S3::Object`` or ``AWS::Lambda::Function`` resources.
        
                    - **Values** *(list) --* 
        
                      An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified objects.
        
                      * To log data events for all objects in all S3 buckets in your AWS account, specify the prefix as ``arn:aws:s3:::`` .  
        
                      .. note::
        
                         This will also enable logging of data event activity performed by any user or role in your AWS account, even if that activity is performed on a bucket that belongs to another AWS account.  
        
                      * To log data events for all objects in all S3 buckets that include *my-bucket* in their names, specify the prefix as ``aws:s3:::my-bucket`` . The trail logs data events for all objects in all buckets whose name contains a match for *my-bucket* .  
                       
                      * To log data events for all objects in an S3 bucket, specify the bucket and an empty object prefix such as ``arn:aws:s3:::bucket-1/`` . The trail logs data events for all objects in this S3 bucket. 
                       
                      * To log data events for specific objects, specify the S3 bucket and object prefix such as ``arn:aws:s3:::bucket-1/example-images`` . The trail logs data events for objects in this S3 bucket that match the prefix. 
                       
                      * To log data events for all functions in your AWS account, specify the prefix as ``arn:aws:lambda`` . 
        
                      .. note::
        
                         This will also enable logging of ``Invoke`` activity performed by any user or role in your AWS account, even if that activity is performed on a function that belongs to another AWS account.  
        
                      * To log data eents for a specific Lambda function, specify the function ARN. 
        
                      .. note::
        
                         Lambda function ARNs are exact. Unlike S3, you cannot use matching. For example, if you specify a function ARN *arn:aws:lambda:us-west-2:111111111111:function:helloworld* , data events will only be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld* . They will not be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld2* . 
        
                      - *(string) --* 
                  
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

    def get_trail_status(self, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/GetTrailStatus>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_trail_status(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Specifies the name or the CloudTrail ARN of the trail for which you are requesting status. To get the status of a shadow trail (a replication of the trail in another region), you must specify its ARN. The format of a trail ARN is:
        
           ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IsLogging\': True|False,
                \'LatestDeliveryError\': \'string\',
                \'LatestNotificationError\': \'string\',
                \'LatestDeliveryTime\': datetime(2015, 1, 1),
                \'LatestNotificationTime\': datetime(2015, 1, 1),
                \'StartLoggingTime\': datetime(2015, 1, 1),
                \'StopLoggingTime\': datetime(2015, 1, 1),
                \'LatestCloudWatchLogsDeliveryError\': \'string\',
                \'LatestCloudWatchLogsDeliveryTime\': datetime(2015, 1, 1),
                \'LatestDigestDeliveryTime\': datetime(2015, 1, 1),
                \'LatestDigestDeliveryError\': \'string\',
                \'LatestDeliveryAttemptTime\': \'string\',
                \'LatestNotificationAttemptTime\': \'string\',
                \'LatestNotificationAttemptSucceeded\': \'string\',
                \'LatestDeliveryAttemptSucceeded\': \'string\',
                \'TimeLoggingStarted\': \'string\',
                \'TimeLoggingStopped\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Returns the objects or data listed below if successful. Otherwise, returns an error.
        
            - **IsLogging** *(boolean) --* 
        
              Whether the CloudTrail is currently logging AWS API calls.
        
            - **LatestDeliveryError** *(string) --* 
        
              Displays any Amazon S3 error that CloudTrail encountered when attempting to deliver log files to the designated bucket. For more information see the topic `Error Responses <http://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html>`__ in the Amazon S3 API Reference. 
        
              .. note::
        
                This error occurs only when there is a problem with the destination S3 bucket and will not occur for timeouts. To resolve the issue, create a new bucket and call ``UpdateTrail`` to specify the new bucket, or fix the existing objects so that CloudTrail can again write to the bucket.
        
            - **LatestNotificationError** *(string) --* 
        
              Displays any Amazon SNS error that CloudTrail encountered when attempting to send a notification. For more information about Amazon SNS errors, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/welcome.html>`__ . 
        
            - **LatestDeliveryTime** *(datetime) --* 
        
              Specifies the date and time that CloudTrail last delivered log files to an account\'s Amazon S3 bucket.
        
            - **LatestNotificationTime** *(datetime) --* 
        
              Specifies the date and time of the most recent Amazon SNS notification that CloudTrail has written a new log file to an account\'s Amazon S3 bucket.
        
            - **StartLoggingTime** *(datetime) --* 
        
              Specifies the most recent date and time when CloudTrail started recording API calls for an AWS account.
        
            - **StopLoggingTime** *(datetime) --* 
        
              Specifies the most recent date and time when CloudTrail stopped recording API calls for an AWS account.
        
            - **LatestCloudWatchLogsDeliveryError** *(string) --* 
        
              Displays any CloudWatch Logs error that CloudTrail encountered when attempting to deliver logs to CloudWatch Logs.
        
            - **LatestCloudWatchLogsDeliveryTime** *(datetime) --* 
        
              Displays the most recent date and time when CloudTrail delivered logs to CloudWatch Logs.
        
            - **LatestDigestDeliveryTime** *(datetime) --* 
        
              Specifies the date and time that CloudTrail last delivered a digest file to an account\'s Amazon S3 bucket.
        
            - **LatestDigestDeliveryError** *(string) --* 
        
              Displays any Amazon S3 error that CloudTrail encountered when attempting to deliver a digest file to the designated bucket. For more information see the topic `Error Responses <http://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html>`__ in the Amazon S3 API Reference. 
        
              .. note::
        
                This error occurs only when there is a problem with the destination S3 bucket and will not occur for timeouts. To resolve the issue, create a new bucket and call ``UpdateTrail`` to specify the new bucket, or fix the existing objects so that CloudTrail can again write to the bucket.
        
            - **LatestDeliveryAttemptTime** *(string) --* 
        
              This field is deprecated.
        
            - **LatestNotificationAttemptTime** *(string) --* 
        
              This field is deprecated.
        
            - **LatestNotificationAttemptSucceeded** *(string) --* 
        
              This field is deprecated.
        
            - **LatestDeliveryAttemptSucceeded** *(string) --* 
        
              This field is deprecated.
        
            - **TimeLoggingStarted** *(string) --* 
        
              This field is deprecated.
        
            - **TimeLoggingStopped** *(string) --* 
        
              This field is deprecated.
        
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

    def list_public_keys(self, StartTime: datetime = None, EndTime: datetime = None, NextToken: str = None) -> Dict:
        """
        
        .. note::
        
          CloudTrail uses different private/public key pairs per region. Each digest file is signed with a private key unique to its region. Therefore, when you validate a digest file from a particular region, you must look in the same region for its corresponding public key.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/ListPublicKeys>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_public_keys(
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              NextToken=\'string\'
          )
        :type StartTime: datetime
        :param StartTime: 
        
          Optionally specifies, in UTC, the start of the time range to look up public keys for CloudTrail digest files. If not specified, the current time is used, and the current public key is returned.
        
        :type EndTime: datetime
        :param EndTime: 
        
          Optionally specifies, in UTC, the end of the time range to look up public keys for CloudTrail digest files. If not specified, the current time is used.
        
        :type NextToken: string
        :param NextToken: 
        
          Reserved for future use.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'PublicKeyList\': [
                    {
                        \'Value\': b\'bytes\',
                        \'ValidityStartTime\': datetime(2015, 1, 1),
                        \'ValidityEndTime\': datetime(2015, 1, 1),
                        \'Fingerprint\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Returns the objects or data listed below if successful. Otherwise, returns an error.
        
            - **PublicKeyList** *(list) --* 
        
              Contains an array of PublicKey objects.
        
              .. note::
        
                The returned public keys may have validity time ranges that overlap.
        
              - *(dict) --* 
        
                Contains information about a returned public key.
        
                - **Value** *(bytes) --* 
        
                  The DER encoded public key value in PKCS#1 format.
        
                - **ValidityStartTime** *(datetime) --* 
        
                  The starting time of validity of the public key.
        
                - **ValidityEndTime** *(datetime) --* 
        
                  The ending time of validity of the public key.
        
                - **Fingerprint** *(string) --* 
        
                  The fingerprint of the public key.
        
            - **NextToken** *(string) --* 
        
              Reserved for future use.
        
        """
        pass

    def list_tags(self, ResourceIdList: List, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/ListTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags(
              ResourceIdList=[
                  \'string\',
              ],
              NextToken=\'string\'
          )
        :type ResourceIdList: list
        :param ResourceIdList: **[REQUIRED]** 
        
          Specifies a list of trail ARNs whose tags will be listed. The list has a limit of 20 ARNs. The format of a trail ARN is:
        
           ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``  
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          Reserved for future use.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ResourceTagList\': [
                    {
                        \'ResourceId\': \'string\',
                        \'TagsList\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Returns the objects or data listed below if successful. Otherwise, returns an error.
        
            - **ResourceTagList** *(list) --* 
        
              A list of resource tags.
        
              - *(dict) --* 
        
                A resource tag.
        
                - **ResourceId** *(string) --* 
        
                  Specifies the ARN of the resource.
        
                - **TagsList** *(list) --* 
        
                  A list of tags.
        
                  - *(dict) --* 
        
                    A custom key-value pair associated with a resource such as a CloudTrail trail.
        
                    - **Key** *(string) --* 
        
                      The key in a key-value pair. The key must be must be no longer than 128 Unicode characters. The key must be unique for the resource to which it applies.
        
                    - **Value** *(string) --* 
        
                      The value in a key-value pair of a tag. The value must be no longer than 256 Unicode characters.
        
            - **NextToken** *(string) --* 
        
              Reserved for future use.
        
        """
        pass

    def lookup_events(self, LookupAttributes: List = None, StartTime: datetime = None, EndTime: datetime = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Looks up `management events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-management-events>`__ captured by CloudTrail. Events for a region can be looked up in that region during the last 90 days. Lookup supports the following attributes:
        
        * AWS access key 
         
        * Event ID 
         
        * Event name 
         
        * Event source 
         
        * Read only 
         
        * Resource name 
         
        * Resource type 
         
        * User name 
         
        All attributes are optional. The default number of results returned is 50, with a maximum of 50 possible. The response includes a token that you can use to get the next page of results.
        
        .. warning::
        
          The rate of lookup requests is limited to one per second per account. If this limit is exceeded, a throttling error occurs.
        
        .. warning::
        
          Events that occurred during the selected time range will not be available for lookup if CloudTrail logging was not enabled when the events occurred.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/LookupEvents>`_
        
        **Request Syntax** 
        ::
        
          response = client.lookup_events(
              LookupAttributes=[
                  {
                      \'AttributeKey\': \'EventId\'|\'EventName\'|\'ReadOnly\'|\'Username\'|\'ResourceType\'|\'ResourceName\'|\'EventSource\'|\'AccessKeyId\',
                      \'AttributeValue\': \'string\'
                  },
              ],
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              MaxResults=123,
              NextToken=\'string\'
          )
        :type LookupAttributes: list
        :param LookupAttributes: 
        
          Contains a list of lookup attributes. Currently the list can contain only one item.
        
          - *(dict) --* 
        
            Specifies an attribute and value that filter the events returned.
        
            - **AttributeKey** *(string) --* **[REQUIRED]** 
        
              Specifies an attribute on which to filter the events returned.
        
            - **AttributeValue** *(string) --* **[REQUIRED]** 
        
              Specifies a value for the specified AttributeKey.
        
        :type StartTime: datetime
        :param StartTime: 
        
          Specifies that only events that occur after or at the specified time are returned. If the specified start time is after the specified end time, an error is returned.
        
        :type EndTime: datetime
        :param EndTime: 
        
          Specifies that only events that occur before or at the specified time are returned. If the specified end time is before the specified start time, an error is returned.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The number of events to return. Possible values are 1 through 50. The default is 50.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to use to get the next page of results after a previous API call. This token must be passed in with the same parameters that were specified in the the original call. For example, if the original call specified an AttributeKey of \'Username\' with a value of \'root\', the call with NextToken should include those same parameters.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Events\': [
                    {
                        \'EventId\': \'string\',
                        \'EventName\': \'string\',
                        \'ReadOnly\': \'string\',
                        \'AccessKeyId\': \'string\',
                        \'EventTime\': datetime(2015, 1, 1),
                        \'EventSource\': \'string\',
                        \'Username\': \'string\',
                        \'Resources\': [
                            {
                                \'ResourceType\': \'string\',
                                \'ResourceName\': \'string\'
                            },
                        ],
                        \'CloudTrailEvent\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains a response to a LookupEvents action.
        
            - **Events** *(list) --* 
        
              A list of events returned based on the lookup attributes specified and the CloudTrail event. The events list is sorted by time. The most recent event is listed first.
        
              - *(dict) --* 
        
                Contains information about an event that was returned by a lookup request. The result includes a representation of a CloudTrail event.
        
                - **EventId** *(string) --* 
        
                  The CloudTrail ID of the event returned.
        
                - **EventName** *(string) --* 
        
                  The name of the event returned.
        
                - **ReadOnly** *(string) --* 
        
                  Information about whether the event is a write event or a read event. 
        
                - **AccessKeyId** *(string) --* 
        
                  The AWS access key ID that was used to sign the request. If the request was made with temporary security credentials, this is the access key ID of the temporary credentials.
        
                - **EventTime** *(datetime) --* 
        
                  The date and time of the event returned.
        
                - **EventSource** *(string) --* 
        
                  The AWS service that the request was made to.
        
                - **Username** *(string) --* 
        
                  A user name or role name of the requester that called the API in the event returned.
        
                - **Resources** *(list) --* 
        
                  A list of resources referenced by the event returned.
        
                  - *(dict) --* 
        
                    Specifies the type and name of a resource referenced by an event.
        
                    - **ResourceType** *(string) --* 
        
                      The type of a resource referenced by the event returned. When the resource type cannot be determined, null is returned. Some examples of resource types are: **Instance** for EC2, **Trail** for CloudTrail, **DBInstance** for RDS, and **AccessKey** for IAM. For a list of resource types supported for event lookup, see `Resource Types Supported for Event Lookup <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/lookup_supported_resourcetypes.html>`__ .
        
                    - **ResourceName** *(string) --* 
        
                      The name of the resource referenced by the event returned. These are user-created names whose values will depend on the environment. For example, the resource name might be \"auto-scaling-test-group\" for an Auto Scaling Group or \"i-1234567\" for an EC2 Instance.
        
                - **CloudTrailEvent** *(string) --* 
        
                  A JSON string that contains a representation of the event returned.
        
            - **NextToken** *(string) --* 
        
              The token to use to get the next page of results after a previous API call. If the token does not appear, there are no more results to return. The token must be passed in with the same parameters as the previous call. For example, if the original call specified an AttributeKey of \'Username\' with a value of \'root\', the call with NextToken should include those same parameters.
        
        """
        pass

    def put_event_selectors(self, TrailName: str, EventSelectors: List) -> Dict:
        """
        
        When an event occurs in your account, CloudTrail evaluates the event selectors in all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn\'t match any event selector, the trail doesn\'t log the event. 
        
        Example
        
        * You create an event selector for a trail and specify that you want write-only events. 
         
        * The EC2 ``GetConsoleOutput`` and ``RunInstances`` API operations occur in your account. 
         
        * CloudTrail evaluates whether the events match your event selectors. 
         
        * The ``RunInstances`` is a write-only event and it matches your event selector. The trail logs the event. 
         
        * The ``GetConsoleOutput`` is a read-only event but it doesn\'t match your event selector. The trail doesn\'t log the event.  
         
        The ``PutEventSelectors`` operation must be called from the region in which the trail was created; otherwise, an ``InvalidHomeRegionException`` is thrown.
        
        You can configure up to five event selectors for each trail. For more information, see `Logging Data and Management Events for Trails <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html>`__ and `Limits in AWS CloudTrail <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html>`__ in the *AWS CloudTrail User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/PutEventSelectors>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_event_selectors(
              TrailName=\'string\',
              EventSelectors=[
                  {
                      \'ReadWriteType\': \'ReadOnly\'|\'WriteOnly\'|\'All\',
                      \'IncludeManagementEvents\': True|False,
                      \'DataResources\': [
                          {
                              \'Type\': \'string\',
                              \'Values\': [
                                  \'string\',
                              ]
                          },
                      ]
                  },
              ]
          )
        :type TrailName: string
        :param TrailName: **[REQUIRED]** 
        
          Specifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:
        
          * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-) 
           
          * Start with a letter or number, and end with a letter or number 
           
          * Be between 3 and 128 characters 
           
          * Have no adjacent periods, underscores or dashes. Names like ``my-_namespace`` and ``my--namespace`` are invalid. 
           
          * Not be in IP address format (for example, 192.168.5.4) 
           
          If you specify a trail ARN, it must be in the format:
        
           ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``  
        
        :type EventSelectors: list
        :param EventSelectors: **[REQUIRED]** 
        
          Specifies the settings for your event selectors. You can configure up to five event selectors for a trail.
        
          - *(dict) --* 
        
            Use event selectors to further specify the management and data event settings for your trail. By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn\'t match any event selector, the trail doesn\'t log the event.
        
            You can configure up to five event selectors for a trail.
        
            - **ReadWriteType** *(string) --* 
        
              Specify if you want your trail to log read-only events, write-only events, or all. For example, the EC2 ``GetConsoleOutput`` is a read-only API operation and ``RunInstances`` is a write-only API operation.
        
              By default, the value is ``All`` .
        
            - **IncludeManagementEvents** *(boolean) --* 
        
              Specify if you want your event selector to include management events for your trail.
        
              For more information, see `Management Events <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-management-events>`__ in the *AWS CloudTrail User Guide* .
        
              By default, the value is ``true`` .
        
            - **DataResources** *(list) --* 
        
              CloudTrail supports data event logging for Amazon S3 objects and AWS Lambda functions. You can specify up to 250 resources for an individual event selector, but the total number of data resources cannot exceed 250 across all event selectors in a trail. This limit does not apply if you configure resource logging for all data events. 
        
              For more information, see `Data Events <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-data-events>`__ and `Limits in AWS CloudTrail <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html>`__ in the *AWS CloudTrail User Guide* .
        
              - *(dict) --* 
        
                The Amazon S3 buckets or AWS Lambda functions that you specify in your event selectors for your trail to log data events. Data events provide insight into the resource operations performed on or within a resource itself. These are also known as data plane operations. You can specify up to 250 data resources for a trail.
        
                .. note::
        
                  The total number of allowed data resources is 250. This number can be distributed between 1 and 5 event selectors, but the total cannot exceed 250 across all selectors.
        
                The following example demonstrates how logging works when you configure logging of all data events for an S3 bucket named ``bucket-1`` . In this example, the CloudTrail user spcified an empty prefix, and the option to log both ``Read`` and ``Write`` data events.
        
                * A user uploads an image file to ``bucket-1`` . 
                 
                * The ``PutObject`` API operation is an Amazon S3 object-level API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an empty prefix, events that occur on any object in that bucket are logged. The trail processes and logs the event. 
                 
                * A user uploads an object to an Amazon S3 bucket named ``arn:aws:s3:::bucket-2`` . 
                 
                * The ``PutObject`` API operation occurred for an object in an S3 bucket that the CloudTrail user didn\'t specify for the trail. The trail doesn’t log the event. 
                 
                The following example demonstrates how logging works when you configure logging of AWS Lambda data events for a Lambda function named *MyLambdaFunction* , but not for all AWS Lambda functions.
        
                * A user runs a script that includes a call to the *MyLambdaFunction* function and the *MyOtherLambdaFunction* function. 
                 
                * The ``Invoke`` API operation on *MyLambdaFunction* is an AWS Lambda API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified logging data events for *MyLambdaFunction* , any invocations of that function are logged. The trail processes and logs the event.  
                 
                * The ``Invoke`` API operation on *MyOtherLambdaFunction* is an AWS Lambda API. Because the CloudTrail user did not specify logging data events for all Lambda functions, the ``Invoke`` operation for *MyOtherLambdaFunction* does not match the function specified for the trail. The trail doesn’t log the event.  
                 
                - **Type** *(string) --* 
        
                  The resource type in which you want to log data events. You can specify ``AWS::S3::Object`` or ``AWS::Lambda::Function`` resources.
        
                - **Values** *(list) --* 
        
                  An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified objects.
        
                  * To log data events for all objects in all S3 buckets in your AWS account, specify the prefix as ``arn:aws:s3:::`` .  
        
                  .. note::
        
                     This will also enable logging of data event activity performed by any user or role in your AWS account, even if that activity is performed on a bucket that belongs to another AWS account.  
        
                  * To log data events for all objects in all S3 buckets that include *my-bucket* in their names, specify the prefix as ``aws:s3:::my-bucket`` . The trail logs data events for all objects in all buckets whose name contains a match for *my-bucket* .  
                   
                  * To log data events for all objects in an S3 bucket, specify the bucket and an empty object prefix such as ``arn:aws:s3:::bucket-1/`` . The trail logs data events for all objects in this S3 bucket. 
                   
                  * To log data events for specific objects, specify the S3 bucket and object prefix such as ``arn:aws:s3:::bucket-1/example-images`` . The trail logs data events for objects in this S3 bucket that match the prefix. 
                   
                  * To log data events for all functions in your AWS account, specify the prefix as ``arn:aws:lambda`` . 
        
                  .. note::
        
                     This will also enable logging of ``Invoke`` activity performed by any user or role in your AWS account, even if that activity is performed on a function that belongs to another AWS account.  
        
                  * To log data eents for a specific Lambda function, specify the function ARN. 
        
                  .. note::
        
                     Lambda function ARNs are exact. Unlike S3, you cannot use matching. For example, if you specify a function ARN *arn:aws:lambda:us-west-2:111111111111:function:helloworld* , data events will only be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld* . They will not be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld2* . 
        
                  - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TrailARN\': \'string\',
                \'EventSelectors\': [
                    {
                        \'ReadWriteType\': \'ReadOnly\'|\'WriteOnly\'|\'All\',
                        \'IncludeManagementEvents\': True|False,
                        \'DataResources\': [
                            {
                                \'Type\': \'string\',
                                \'Values\': [
                                    \'string\',
                                ]
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TrailARN** *(string) --* 
        
              Specifies the ARN of the trail that was updated with event selectors. The format of a trail ARN is:
        
               ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``  
        
            - **EventSelectors** *(list) --* 
        
              Specifies the event selectors configured for your trail.
        
              - *(dict) --* 
        
                Use event selectors to further specify the management and data event settings for your trail. By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn\'t match any event selector, the trail doesn\'t log the event.
        
                You can configure up to five event selectors for a trail.
        
                - **ReadWriteType** *(string) --* 
        
                  Specify if you want your trail to log read-only events, write-only events, or all. For example, the EC2 ``GetConsoleOutput`` is a read-only API operation and ``RunInstances`` is a write-only API operation.
        
                  By default, the value is ``All`` .
        
                - **IncludeManagementEvents** *(boolean) --* 
        
                  Specify if you want your event selector to include management events for your trail.
        
                  For more information, see `Management Events <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-management-events>`__ in the *AWS CloudTrail User Guide* .
        
                  By default, the value is ``true`` .
        
                - **DataResources** *(list) --* 
        
                  CloudTrail supports data event logging for Amazon S3 objects and AWS Lambda functions. You can specify up to 250 resources for an individual event selector, but the total number of data resources cannot exceed 250 across all event selectors in a trail. This limit does not apply if you configure resource logging for all data events. 
        
                  For more information, see `Data Events <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-data-events>`__ and `Limits in AWS CloudTrail <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html>`__ in the *AWS CloudTrail User Guide* .
        
                  - *(dict) --* 
        
                    The Amazon S3 buckets or AWS Lambda functions that you specify in your event selectors for your trail to log data events. Data events provide insight into the resource operations performed on or within a resource itself. These are also known as data plane operations. You can specify up to 250 data resources for a trail.
        
                    .. note::
        
                      The total number of allowed data resources is 250. This number can be distributed between 1 and 5 event selectors, but the total cannot exceed 250 across all selectors.
        
                    The following example demonstrates how logging works when you configure logging of all data events for an S3 bucket named ``bucket-1`` . In this example, the CloudTrail user spcified an empty prefix, and the option to log both ``Read`` and ``Write`` data events.
        
                    * A user uploads an image file to ``bucket-1`` . 
                     
                    * The ``PutObject`` API operation is an Amazon S3 object-level API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an empty prefix, events that occur on any object in that bucket are logged. The trail processes and logs the event. 
                     
                    * A user uploads an object to an Amazon S3 bucket named ``arn:aws:s3:::bucket-2`` . 
                     
                    * The ``PutObject`` API operation occurred for an object in an S3 bucket that the CloudTrail user didn\'t specify for the trail. The trail doesn’t log the event. 
                     
                    The following example demonstrates how logging works when you configure logging of AWS Lambda data events for a Lambda function named *MyLambdaFunction* , but not for all AWS Lambda functions.
        
                    * A user runs a script that includes a call to the *MyLambdaFunction* function and the *MyOtherLambdaFunction* function. 
                     
                    * The ``Invoke`` API operation on *MyLambdaFunction* is an AWS Lambda API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified logging data events for *MyLambdaFunction* , any invocations of that function are logged. The trail processes and logs the event.  
                     
                    * The ``Invoke`` API operation on *MyOtherLambdaFunction* is an AWS Lambda API. Because the CloudTrail user did not specify logging data events for all Lambda functions, the ``Invoke`` operation for *MyOtherLambdaFunction* does not match the function specified for the trail. The trail doesn’t log the event.  
                     
                    - **Type** *(string) --* 
        
                      The resource type in which you want to log data events. You can specify ``AWS::S3::Object`` or ``AWS::Lambda::Function`` resources.
        
                    - **Values** *(list) --* 
        
                      An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified objects.
        
                      * To log data events for all objects in all S3 buckets in your AWS account, specify the prefix as ``arn:aws:s3:::`` .  
        
                      .. note::
        
                         This will also enable logging of data event activity performed by any user or role in your AWS account, even if that activity is performed on a bucket that belongs to another AWS account.  
        
                      * To log data events for all objects in all S3 buckets that include *my-bucket* in their names, specify the prefix as ``aws:s3:::my-bucket`` . The trail logs data events for all objects in all buckets whose name contains a match for *my-bucket* .  
                       
                      * To log data events for all objects in an S3 bucket, specify the bucket and an empty object prefix such as ``arn:aws:s3:::bucket-1/`` . The trail logs data events for all objects in this S3 bucket. 
                       
                      * To log data events for specific objects, specify the S3 bucket and object prefix such as ``arn:aws:s3:::bucket-1/example-images`` . The trail logs data events for objects in this S3 bucket that match the prefix. 
                       
                      * To log data events for all functions in your AWS account, specify the prefix as ``arn:aws:lambda`` . 
        
                      .. note::
        
                         This will also enable logging of ``Invoke`` activity performed by any user or role in your AWS account, even if that activity is performed on a function that belongs to another AWS account.  
        
                      * To log data eents for a specific Lambda function, specify the function ARN. 
        
                      .. note::
        
                         Lambda function ARNs are exact. Unlike S3, you cannot use matching. For example, if you specify a function ARN *arn:aws:lambda:us-west-2:111111111111:function:helloworld* , data events will only be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld* . They will not be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld2* . 
        
                      - *(string) --* 
                  
        """
        pass

    def remove_tags(self, ResourceId: str, TagsList: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/RemoveTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.remove_tags(
              ResourceId=\'string\',
              TagsList=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          Specifies the ARN of the trail from which tags should be removed. The format of a trail ARN is:
        
           ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``  
        
        :type TagsList: list
        :param TagsList: 
        
          Specifies a list of tags to be removed.
        
          - *(dict) --* 
        
            A custom key-value pair associated with a resource such as a CloudTrail trail.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The key in a key-value pair. The key must be must be no longer than 128 Unicode characters. The key must be unique for the resource to which it applies.
        
            - **Value** *(string) --* 
        
              The value in a key-value pair of a tag. The value must be no longer than 256 Unicode characters.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Returns the objects or data listed below if successful. Otherwise, returns an error.
        
        """
        pass

    def start_logging(self, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/StartLogging>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_logging(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Specifies the name or the CloudTrail ARN of the trail for which CloudTrail logs AWS API calls. The format of a trail ARN is:
        
           ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Returns the objects or data listed below if successful. Otherwise, returns an error.
        
        """
        pass

    def stop_logging(self, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/StopLogging>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_logging(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Specifies the name or the CloudTrail ARN of the trail for which CloudTrail will stop logging AWS API calls. The format of a trail ARN is:
        
           ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Returns the objects or data listed below if successful. Otherwise, returns an error.
        
        """
        pass

    def update_trail(self, Name: str, S3BucketName: str = None, S3KeyPrefix: str = None, SnsTopicName: str = None, IncludeGlobalServiceEvents: bool = None, IsMultiRegionTrail: bool = None, EnableLogFileValidation: bool = None, CloudWatchLogsLogGroupArn: str = None, CloudWatchLogsRoleArn: str = None, KmsKeyId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/UpdateTrail>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_trail(
              Name=\'string\',
              S3BucketName=\'string\',
              S3KeyPrefix=\'string\',
              SnsTopicName=\'string\',
              IncludeGlobalServiceEvents=True|False,
              IsMultiRegionTrail=True|False,
              EnableLogFileValidation=True|False,
              CloudWatchLogsLogGroupArn=\'string\',
              CloudWatchLogsRoleArn=\'string\',
              KmsKeyId=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Specifies the name of the trail or trail ARN. If ``Name`` is a trail name, the string must meet the following requirements:
        
          * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-) 
           
          * Start with a letter or number, and end with a letter or number 
           
          * Be between 3 and 128 characters 
           
          * Have no adjacent periods, underscores or dashes. Names like ``my-_namespace`` and ``my--namespace`` are invalid. 
           
          * Not be in IP address format (for example, 192.168.5.4) 
           
          If ``Name`` is a trail ARN, it must be in the format:
        
           ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``  
        
        :type S3BucketName: string
        :param S3BucketName: 
        
          Specifies the name of the Amazon S3 bucket designated for publishing log files. See `Amazon S3 Bucket Naming Requirements <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/create_trail_naming_policy.html>`__ .
        
        :type S3KeyPrefix: string
        :param S3KeyPrefix: 
        
          Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see `Finding Your CloudTrail Log Files <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-find-log-files.html>`__ . The maximum length is 200 characters.
        
        :type SnsTopicName: string
        :param SnsTopicName: 
        
          Specifies the name of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.
        
        :type IncludeGlobalServiceEvents: boolean
        :param IncludeGlobalServiceEvents: 
        
          Specifies whether the trail is publishing events from global services such as IAM to the log files.
        
        :type IsMultiRegionTrail: boolean
        :param IsMultiRegionTrail: 
        
          Specifies whether the trail applies only to the current region or to all regions. The default is false. If the trail exists only in the current region and this value is set to true, shadow trails (replications of the trail) will be created in the other regions. If the trail exists in all regions and this value is set to false, the trail will remain in the region where it was created, and its shadow trails in other regions will be deleted.
        
        :type EnableLogFileValidation: boolean
        :param EnableLogFileValidation: 
        
          Specifies whether log file validation is enabled. The default is false.
        
          .. note::
        
            When you disable log file integrity validation, the chain of digest files is broken after one hour. CloudTrail will not create digest files for log files that were delivered during a period in which log file integrity validation was disabled. For example, if you enable log file integrity validation at noon on January 1, disable it at noon on January 2, and re-enable it at noon on January 10, digest files will not be created for the log files delivered from noon on January 2 to noon on January 10. The same applies whenever you stop CloudTrail logging or delete a trail.
        
        :type CloudWatchLogsLogGroupArn: string
        :param CloudWatchLogsLogGroupArn: 
        
          Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered. Not required unless you specify CloudWatchLogsRoleArn.
        
        :type CloudWatchLogsRoleArn: string
        :param CloudWatchLogsRoleArn: 
        
          Specifies the role for the CloudWatch Logs endpoint to assume to write to a user\'s log group.
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          Specifies the KMS key ID to use to encrypt the logs delivered by CloudTrail. The value can be an alias name prefixed by \"alias/\", a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
        
          Examples:
        
          * alias/MyAliasName 
           
          * arn:aws:kms:us-east-2:123456789012:alias/MyAliasName 
           
          * arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012 
           
          * 12345678-1234-1234-1234-123456789012 
           
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Name\': \'string\',
                \'S3BucketName\': \'string\',
                \'S3KeyPrefix\': \'string\',
                \'SnsTopicName\': \'string\',
                \'SnsTopicARN\': \'string\',
                \'IncludeGlobalServiceEvents\': True|False,
                \'IsMultiRegionTrail\': True|False,
                \'TrailARN\': \'string\',
                \'LogFileValidationEnabled\': True|False,
                \'CloudWatchLogsLogGroupArn\': \'string\',
                \'CloudWatchLogsRoleArn\': \'string\',
                \'KmsKeyId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Returns the objects or data listed below if successful. Otherwise, returns an error.
        
            - **Name** *(string) --* 
        
              Specifies the name of the trail.
        
            - **S3BucketName** *(string) --* 
        
              Specifies the name of the Amazon S3 bucket designated for publishing log files.
        
            - **S3KeyPrefix** *(string) --* 
        
              Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see `Finding Your CloudTrail Log Files <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-find-log-files.html>`__ .
        
            - **SnsTopicName** *(string) --* 
        
              This field is deprecated. Use SnsTopicARN.
        
            - **SnsTopicARN** *(string) --* 
        
              Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The format of a topic ARN is:
        
               ``arn:aws:sns:us-east-2:123456789012:MyTopic``  
        
            - **IncludeGlobalServiceEvents** *(boolean) --* 
        
              Specifies whether the trail is publishing events from global services such as IAM to the log files.
        
            - **IsMultiRegionTrail** *(boolean) --* 
        
              Specifies whether the trail exists in one region or in all regions.
        
            - **TrailARN** *(string) --* 
        
              Specifies the ARN of the trail that was updated. The format of a trail ARN is:
        
               ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``  
        
            - **LogFileValidationEnabled** *(boolean) --* 
        
              Specifies whether log file integrity validation is enabled.
        
            - **CloudWatchLogsLogGroupArn** *(string) --* 
        
              Specifies the Amazon Resource Name (ARN) of the log group to which CloudTrail logs will be delivered.
        
            - **CloudWatchLogsRoleArn** *(string) --* 
        
              Specifies the role for the CloudWatch Logs endpoint to assume to write to a user\'s log group.
        
            - **KmsKeyId** *(string) --* 
        
              Specifies the KMS key ID that encrypts the logs delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the format:
        
               ``arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012``  
        
        """
        pass
