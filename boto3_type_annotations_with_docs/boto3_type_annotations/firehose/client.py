from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
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

    def create_delivery_stream(self, DeliveryStreamName: str, DeliveryStreamType: str = None, KinesisStreamSourceConfiguration: Dict = None, S3DestinationConfiguration: Dict = None, ExtendedS3DestinationConfiguration: Dict = None, RedshiftDestinationConfiguration: Dict = None, ElasticsearchDestinationConfiguration: Dict = None, SplunkDestinationConfiguration: Dict = None, Tags: List = None) -> Dict:
        """
        
        By default, you can create up to 50 delivery streams per AWS Region.
        
        This is an asynchronous operation that immediately returns. The initial status of the delivery stream is ``CREATING`` . After the delivery stream is created, its status is ``ACTIVE`` and it now accepts data. Attempts to send data to a delivery stream that is not in the ``ACTIVE`` state cause an exception. To check the state of a delivery stream, use  DescribeDeliveryStream .
        
        A Kinesis Data Firehose delivery stream can be configured to receive records directly from providers using  PutRecord or  PutRecordBatch , or it can be configured to use an existing Kinesis stream as its source. To specify a Kinesis data stream as input, set the ``DeliveryStreamType`` parameter to ``KinesisStreamAsSource`` , and provide the Kinesis stream Amazon Resource Name (ARN) and role ARN in the ``KinesisStreamSourceConfiguration`` parameter.
        
        A delivery stream is configured with a single destination: Amazon S3, Amazon ES, Amazon Redshift, or Splunk. You must specify only one of the following destination configuration parameters: **ExtendedS3DestinationConfiguration** , **S3DestinationConfiguration** , **ElasticsearchDestinationConfiguration** , **RedshiftDestinationConfiguration** , or **SplunkDestinationConfiguration** .
        
        When you specify **S3DestinationConfiguration** , you can also provide the following optional values: **BufferingHints** , **EncryptionConfiguration** , and **CompressionFormat** . By default, if no **BufferingHints** value is provided, Kinesis Data Firehose buffers data up to 5 MB or for 5 minutes, whichever condition is satisfied first. **BufferingHints** is a hint, so there are some cases where the service cannot adhere to these conditions strictly. For example, record boundaries might be such that the size is a little over or under the configured buffering size. By default, no encryption is performed. We strongly recommend that you enable encryption to ensure secure data storage in Amazon S3.
        
        A few notes about Amazon Redshift as a destination:
        
        * An Amazon Redshift destination requires an S3 bucket as intermediate location. Kinesis Data Firehose first delivers data to Amazon S3 and then uses ``COPY`` syntax to load data into an Amazon Redshift table. This is specified in the **RedshiftDestinationConfiguration.S3Configuration** parameter. 
         
        * The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified in ``RedshiftDestinationConfiguration.S3Configuration`` because the Amazon Redshift ``COPY`` operation that reads from the S3 bucket doesn\'t support these compression formats. 
         
        * We strongly recommend that you use the user name and password you provide exclusively with Kinesis Data Firehose, and that the permissions for the account are restricted for Amazon Redshift ``INSERT`` permissions. 
         
        Kinesis Data Firehose assumes the IAM role that is configured as part of the destination. The role should allow the Kinesis Data Firehose principal to assume the role, and the role should have permissions that allow the service to deliver the data. For more information, see `Grant Kinesis Data Firehose Access to an Amazon S3 Destination <http://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-s3>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/firehose-2015-08-04/CreateDeliveryStream>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_delivery_stream(
              DeliveryStreamName=\'string\',
              DeliveryStreamType=\'DirectPut\'|\'KinesisStreamAsSource\',
              KinesisStreamSourceConfiguration={
                  \'KinesisStreamARN\': \'string\',
                  \'RoleARN\': \'string\'
              },
              S3DestinationConfiguration={
                  \'RoleARN\': \'string\',
                  \'BucketARN\': \'string\',
                  \'Prefix\': \'string\',
                  \'BufferingHints\': {
                      \'SizeInMBs\': 123,
                      \'IntervalInSeconds\': 123
                  },
                  \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                  \'EncryptionConfiguration\': {
                      \'NoEncryptionConfig\': \'NoEncryption\',
                      \'KMSEncryptionConfig\': {
                          \'AWSKMSKeyARN\': \'string\'
                      }
                  },
                  \'CloudWatchLoggingOptions\': {
                      \'Enabled\': True|False,
                      \'LogGroupName\': \'string\',
                      \'LogStreamName\': \'string\'
                  }
              },
              ExtendedS3DestinationConfiguration={
                  \'RoleARN\': \'string\',
                  \'BucketARN\': \'string\',
                  \'Prefix\': \'string\',
                  \'BufferingHints\': {
                      \'SizeInMBs\': 123,
                      \'IntervalInSeconds\': 123
                  },
                  \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                  \'EncryptionConfiguration\': {
                      \'NoEncryptionConfig\': \'NoEncryption\',
                      \'KMSEncryptionConfig\': {
                          \'AWSKMSKeyARN\': \'string\'
                      }
                  },
                  \'CloudWatchLoggingOptions\': {
                      \'Enabled\': True|False,
                      \'LogGroupName\': \'string\',
                      \'LogStreamName\': \'string\'
                  },
                  \'ProcessingConfiguration\': {
                      \'Enabled\': True|False,
                      \'Processors\': [
                          {
                              \'Type\': \'Lambda\',
                              \'Parameters\': [
                                  {
                                      \'ParameterName\': \'LambdaArn\'|\'NumberOfRetries\'|\'RoleArn\'|\'BufferSizeInMBs\'|\'BufferIntervalInSeconds\',
                                      \'ParameterValue\': \'string\'
                                  },
                              ]
                          },
                      ]
                  },
                  \'S3BackupMode\': \'Disabled\'|\'Enabled\',
                  \'S3BackupConfiguration\': {
                      \'RoleARN\': \'string\',
                      \'BucketARN\': \'string\',
                      \'Prefix\': \'string\',
                      \'BufferingHints\': {
                          \'SizeInMBs\': 123,
                          \'IntervalInSeconds\': 123
                      },
                      \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                      \'EncryptionConfiguration\': {
                          \'NoEncryptionConfig\': \'NoEncryption\',
                          \'KMSEncryptionConfig\': {
                              \'AWSKMSKeyARN\': \'string\'
                          }
                      },
                      \'CloudWatchLoggingOptions\': {
                          \'Enabled\': True|False,
                          \'LogGroupName\': \'string\',
                          \'LogStreamName\': \'string\'
                      }
                  },
                  \'DataFormatConversionConfiguration\': {
                      \'SchemaConfiguration\': {
                          \'RoleARN\': \'string\',
                          \'CatalogId\': \'string\',
                          \'DatabaseName\': \'string\',
                          \'TableName\': \'string\',
                          \'Region\': \'string\',
                          \'VersionId\': \'string\'
                      },
                      \'InputFormatConfiguration\': {
                          \'Deserializer\': {
                              \'OpenXJsonSerDe\': {
                                  \'ConvertDotsInJsonKeysToUnderscores\': True|False,
                                  \'CaseInsensitive\': True|False,
                                  \'ColumnToJsonKeyMappings\': {
                                      \'string\': \'string\'
                                  }
                              },
                              \'HiveJsonSerDe\': {
                                  \'TimestampFormats\': [
                                      \'string\',
                                  ]
                              }
                          }
                      },
                      \'OutputFormatConfiguration\': {
                          \'Serializer\': {
                              \'ParquetSerDe\': {
                                  \'BlockSizeBytes\': 123,
                                  \'PageSizeBytes\': 123,
                                  \'Compression\': \'UNCOMPRESSED\'|\'GZIP\'|\'SNAPPY\',
                                  \'EnableDictionaryCompression\': True|False,
                                  \'MaxPaddingBytes\': 123,
                                  \'WriterVersion\': \'V1\'|\'V2\'
                              },
                              \'OrcSerDe\': {
                                  \'StripeSizeBytes\': 123,
                                  \'BlockSizeBytes\': 123,
                                  \'RowIndexStride\': 123,
                                  \'EnablePadding\': True|False,
                                  \'PaddingTolerance\': 123.0,
                                  \'Compression\': \'NONE\'|\'ZLIB\'|\'SNAPPY\',
                                  \'BloomFilterColumns\': [
                                      \'string\',
                                  ],
                                  \'BloomFilterFalsePositiveProbability\': 123.0,
                                  \'DictionaryKeyThreshold\': 123.0,
                                  \'FormatVersion\': \'V0_11\'|\'V0_12\'
                              }
                          }
                      },
                      \'Enabled\': True|False
                  }
              },
              RedshiftDestinationConfiguration={
                  \'RoleARN\': \'string\',
                  \'ClusterJDBCURL\': \'string\',
                  \'CopyCommand\': {
                      \'DataTableName\': \'string\',
                      \'DataTableColumns\': \'string\',
                      \'CopyOptions\': \'string\'
                  },
                  \'Username\': \'string\',
                  \'Password\': \'string\',
                  \'RetryOptions\': {
                      \'DurationInSeconds\': 123
                  },
                  \'S3Configuration\': {
                      \'RoleARN\': \'string\',
                      \'BucketARN\': \'string\',
                      \'Prefix\': \'string\',
                      \'BufferingHints\': {
                          \'SizeInMBs\': 123,
                          \'IntervalInSeconds\': 123
                      },
                      \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                      \'EncryptionConfiguration\': {
                          \'NoEncryptionConfig\': \'NoEncryption\',
                          \'KMSEncryptionConfig\': {
                              \'AWSKMSKeyARN\': \'string\'
                          }
                      },
                      \'CloudWatchLoggingOptions\': {
                          \'Enabled\': True|False,
                          \'LogGroupName\': \'string\',
                          \'LogStreamName\': \'string\'
                      }
                  },
                  \'ProcessingConfiguration\': {
                      \'Enabled\': True|False,
                      \'Processors\': [
                          {
                              \'Type\': \'Lambda\',
                              \'Parameters\': [
                                  {
                                      \'ParameterName\': \'LambdaArn\'|\'NumberOfRetries\'|\'RoleArn\'|\'BufferSizeInMBs\'|\'BufferIntervalInSeconds\',
                                      \'ParameterValue\': \'string\'
                                  },
                              ]
                          },
                      ]
                  },
                  \'S3BackupMode\': \'Disabled\'|\'Enabled\',
                  \'S3BackupConfiguration\': {
                      \'RoleARN\': \'string\',
                      \'BucketARN\': \'string\',
                      \'Prefix\': \'string\',
                      \'BufferingHints\': {
                          \'SizeInMBs\': 123,
                          \'IntervalInSeconds\': 123
                      },
                      \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                      \'EncryptionConfiguration\': {
                          \'NoEncryptionConfig\': \'NoEncryption\',
                          \'KMSEncryptionConfig\': {
                              \'AWSKMSKeyARN\': \'string\'
                          }
                      },
                      \'CloudWatchLoggingOptions\': {
                          \'Enabled\': True|False,
                          \'LogGroupName\': \'string\',
                          \'LogStreamName\': \'string\'
                      }
                  },
                  \'CloudWatchLoggingOptions\': {
                      \'Enabled\': True|False,
                      \'LogGroupName\': \'string\',
                      \'LogStreamName\': \'string\'
                  }
              },
              ElasticsearchDestinationConfiguration={
                  \'RoleARN\': \'string\',
                  \'DomainARN\': \'string\',
                  \'IndexName\': \'string\',
                  \'TypeName\': \'string\',
                  \'IndexRotationPeriod\': \'NoRotation\'|\'OneHour\'|\'OneDay\'|\'OneWeek\'|\'OneMonth\',
                  \'BufferingHints\': {
                      \'IntervalInSeconds\': 123,
                      \'SizeInMBs\': 123
                  },
                  \'RetryOptions\': {
                      \'DurationInSeconds\': 123
                  },
                  \'S3BackupMode\': \'FailedDocumentsOnly\'|\'AllDocuments\',
                  \'S3Configuration\': {
                      \'RoleARN\': \'string\',
                      \'BucketARN\': \'string\',
                      \'Prefix\': \'string\',
                      \'BufferingHints\': {
                          \'SizeInMBs\': 123,
                          \'IntervalInSeconds\': 123
                      },
                      \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                      \'EncryptionConfiguration\': {
                          \'NoEncryptionConfig\': \'NoEncryption\',
                          \'KMSEncryptionConfig\': {
                              \'AWSKMSKeyARN\': \'string\'
                          }
                      },
                      \'CloudWatchLoggingOptions\': {
                          \'Enabled\': True|False,
                          \'LogGroupName\': \'string\',
                          \'LogStreamName\': \'string\'
                      }
                  },
                  \'ProcessingConfiguration\': {
                      \'Enabled\': True|False,
                      \'Processors\': [
                          {
                              \'Type\': \'Lambda\',
                              \'Parameters\': [
                                  {
                                      \'ParameterName\': \'LambdaArn\'|\'NumberOfRetries\'|\'RoleArn\'|\'BufferSizeInMBs\'|\'BufferIntervalInSeconds\',
                                      \'ParameterValue\': \'string\'
                                  },
                              ]
                          },
                      ]
                  },
                  \'CloudWatchLoggingOptions\': {
                      \'Enabled\': True|False,
                      \'LogGroupName\': \'string\',
                      \'LogStreamName\': \'string\'
                  }
              },
              SplunkDestinationConfiguration={
                  \'HECEndpoint\': \'string\',
                  \'HECEndpointType\': \'Raw\'|\'Event\',
                  \'HECToken\': \'string\',
                  \'HECAcknowledgmentTimeoutInSeconds\': 123,
                  \'RetryOptions\': {
                      \'DurationInSeconds\': 123
                  },
                  \'S3BackupMode\': \'FailedEventsOnly\'|\'AllEvents\',
                  \'S3Configuration\': {
                      \'RoleARN\': \'string\',
                      \'BucketARN\': \'string\',
                      \'Prefix\': \'string\',
                      \'BufferingHints\': {
                          \'SizeInMBs\': 123,
                          \'IntervalInSeconds\': 123
                      },
                      \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                      \'EncryptionConfiguration\': {
                          \'NoEncryptionConfig\': \'NoEncryption\',
                          \'KMSEncryptionConfig\': {
                              \'AWSKMSKeyARN\': \'string\'
                          }
                      },
                      \'CloudWatchLoggingOptions\': {
                          \'Enabled\': True|False,
                          \'LogGroupName\': \'string\',
                          \'LogStreamName\': \'string\'
                      }
                  },
                  \'ProcessingConfiguration\': {
                      \'Enabled\': True|False,
                      \'Processors\': [
                          {
                              \'Type\': \'Lambda\',
                              \'Parameters\': [
                                  {
                                      \'ParameterName\': \'LambdaArn\'|\'NumberOfRetries\'|\'RoleArn\'|\'BufferSizeInMBs\'|\'BufferIntervalInSeconds\',
                                      \'ParameterValue\': \'string\'
                                  },
                              ]
                          },
                      ]
                  },
                  \'CloudWatchLoggingOptions\': {
                      \'Enabled\': True|False,
                      \'LogGroupName\': \'string\',
                      \'LogStreamName\': \'string\'
                  }
              },
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DeliveryStreamName: string
        :param DeliveryStreamName: **[REQUIRED]** 
        
          The name of the delivery stream. This name must be unique per AWS account in the same AWS Region. If the delivery streams are in different accounts or different Regions, you can have multiple delivery streams with the same name.
        
        :type DeliveryStreamType: string
        :param DeliveryStreamType: 
        
          The delivery stream type. This parameter can be one of the following values:
        
          * ``DirectPut`` : Provider applications access the delivery stream directly. 
           
          * ``KinesisStreamAsSource`` : The delivery stream uses a Kinesis data stream as a source. 
           
        :type KinesisStreamSourceConfiguration: dict
        :param KinesisStreamSourceConfiguration: 
        
          When a Kinesis data stream is used as the source for the delivery stream, a  KinesisStreamSourceConfiguration containing the Kinesis data stream Amazon Resource Name (ARN) and the role ARN for the source stream.
        
          - **KinesisStreamARN** *(string) --* **[REQUIRED]** 
        
            The ARN of the source Kinesis data stream. For more information, see `Amazon Kinesis Data Streams ARN Format <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams>`__ .
        
          - **RoleARN** *(string) --* **[REQUIRED]** 
        
            The ARN of the role that provides access to the source Kinesis data stream. For more information, see `AWS Identity and Access Management (IAM) ARN Format <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam>`__ .
        
        :type S3DestinationConfiguration: dict
        :param S3DestinationConfiguration: 
        
          [Deprecated] The destination in Amazon S3. You can specify only one destination.
        
          - **RoleARN** *(string) --* **[REQUIRED]** 
        
            The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
          - **BucketARN** *(string) --* **[REQUIRED]** 
        
            The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
          - **Prefix** *(string) --* 
        
            The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
          - **BufferingHints** *(dict) --* 
        
            The buffering option. If no value is specified, ``BufferingHints`` object default values are used.
        
            - **SizeInMBs** *(integer) --* 
        
              Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
              We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
            - **IntervalInSeconds** *(integer) --* 
        
              Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
          - **CompressionFormat** *(string) --* 
        
            The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
            The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift ``COPY`` operation that reads from the S3 bucket.
        
          - **EncryptionConfiguration** *(dict) --* 
        
            The encryption configuration. If no value is specified, the default is no encryption.
        
            - **NoEncryptionConfig** *(string) --* 
        
              Specifically override existing encryption information to ensure that no encryption is used.
        
            - **KMSEncryptionConfig** *(dict) --* 
        
              The encryption key.
        
              - **AWSKMSKeyARN** *(string) --* **[REQUIRED]** 
        
                The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
          - **CloudWatchLoggingOptions** *(dict) --* 
        
            The CloudWatch logging options for your delivery stream.
        
            - **Enabled** *(boolean) --* 
        
              Enables or disables CloudWatch logging.
        
            - **LogGroupName** *(string) --* 
        
              The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
            - **LogStreamName** *(string) --* 
        
              The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
        :type ExtendedS3DestinationConfiguration: dict
        :param ExtendedS3DestinationConfiguration: 
        
          The destination in Amazon S3. You can specify only one destination.
        
          - **RoleARN** *(string) --* **[REQUIRED]** 
        
            The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
          - **BucketARN** *(string) --* **[REQUIRED]** 
        
            The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
          - **Prefix** *(string) --* 
        
            The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
          - **BufferingHints** *(dict) --* 
        
            The buffering option.
        
            - **SizeInMBs** *(integer) --* 
        
              Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
              We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
            - **IntervalInSeconds** *(integer) --* 
        
              Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
          - **CompressionFormat** *(string) --* 
        
            The compression format. If no value is specified, the default is UNCOMPRESSED.
        
          - **EncryptionConfiguration** *(dict) --* 
        
            The encryption configuration. If no value is specified, the default is no encryption.
        
            - **NoEncryptionConfig** *(string) --* 
        
              Specifically override existing encryption information to ensure that no encryption is used.
        
            - **KMSEncryptionConfig** *(dict) --* 
        
              The encryption key.
        
              - **AWSKMSKeyARN** *(string) --* **[REQUIRED]** 
        
                The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
          - **CloudWatchLoggingOptions** *(dict) --* 
        
            The Amazon CloudWatch logging options for your delivery stream.
        
            - **Enabled** *(boolean) --* 
        
              Enables or disables CloudWatch logging.
        
            - **LogGroupName** *(string) --* 
        
              The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
            - **LogStreamName** *(string) --* 
        
              The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
          - **ProcessingConfiguration** *(dict) --* 
        
            The data processing configuration.
        
            - **Enabled** *(boolean) --* 
        
              Enables or disables data processing.
        
            - **Processors** *(list) --* 
        
              The data processors.
        
              - *(dict) --* 
        
                Describes a data processor.
        
                - **Type** *(string) --* **[REQUIRED]** 
        
                  The type of processor.
        
                - **Parameters** *(list) --* 
        
                  The processor parameters.
        
                  - *(dict) --* 
        
                    Describes the processor parameter.
        
                    - **ParameterName** *(string) --* **[REQUIRED]** 
        
                      The name of the parameter.
        
                    - **ParameterValue** *(string) --* **[REQUIRED]** 
        
                      The parameter value.
        
          - **S3BackupMode** *(string) --* 
        
            The Amazon S3 backup mode.
        
          - **S3BackupConfiguration** *(dict) --* 
        
            The configuration for backup in Amazon S3.
        
            - **RoleARN** *(string) --* **[REQUIRED]** 
        
              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **BucketARN** *(string) --* **[REQUIRED]** 
        
              The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **Prefix** *(string) --* 
        
              The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
            - **BufferingHints** *(dict) --* 
        
              The buffering option. If no value is specified, ``BufferingHints`` object default values are used.
        
              - **SizeInMBs** *(integer) --* 
        
                Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
                We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
              - **IntervalInSeconds** *(integer) --* 
        
                Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
            - **CompressionFormat** *(string) --* 
        
              The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
              The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift ``COPY`` operation that reads from the S3 bucket.
        
            - **EncryptionConfiguration** *(dict) --* 
        
              The encryption configuration. If no value is specified, the default is no encryption.
        
              - **NoEncryptionConfig** *(string) --* 
        
                Specifically override existing encryption information to ensure that no encryption is used.
        
              - **KMSEncryptionConfig** *(dict) --* 
        
                The encryption key.
        
                - **AWSKMSKeyARN** *(string) --* **[REQUIRED]** 
        
                  The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **CloudWatchLoggingOptions** *(dict) --* 
        
              The CloudWatch logging options for your delivery stream.
        
              - **Enabled** *(boolean) --* 
        
                Enables or disables CloudWatch logging.
        
              - **LogGroupName** *(string) --* 
        
                The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
              - **LogStreamName** *(string) --* 
        
                The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
          - **DataFormatConversionConfiguration** *(dict) --* 
        
            The serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3.
        
            - **SchemaConfiguration** *(dict) --* 
        
              Specifies the AWS Glue Data Catalog table that contains the column information.
        
              - **RoleARN** *(string) --* 
        
                The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren\'t allowed.
        
              - **CatalogId** *(string) --* 
        
                The ID of the AWS Glue Data Catalog. If you don\'t supply this, the AWS account ID is used by default.
        
              - **DatabaseName** *(string) --* 
        
                Specifies the name of the AWS Glue database that contains the schema for the output data.
        
              - **TableName** *(string) --* 
        
                Specifies the AWS Glue table that contains the column information that constitutes your data schema.
        
              - **Region** *(string) --* 
        
                If you don\'t specify an AWS Region, the default is the current Region.
        
              - **VersionId** *(string) --* 
        
                Specifies the table version for the output data schema. If you don\'t specify this version ID, or if you set it to ``LATEST`` , Kinesis Data Firehose uses the most recent version. This means that any updates to the table are automatically picked up.
        
            - **InputFormatConfiguration** *(dict) --* 
        
              Specifies the deserializer that you want Kinesis Data Firehose to use to convert the format of your data from JSON.
        
              - **Deserializer** *(dict) --* 
        
                Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the request.
        
                - **OpenXJsonSerDe** *(dict) --* 
        
                  The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.
        
                  - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --* 
        
                    When set to ``true`` , specifies that the names of the keys include dots and that you want Kinesis Data Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is \"a.b\", you can define the column name to be \"a_b\" when using this option.
        
                    The default is ``false`` .
        
                  - **CaseInsensitive** *(boolean) --* 
        
                    When set to ``true`` , which is the default, Kinesis Data Firehose converts JSON keys to lowercase before deserializing them.
        
                  - **ColumnToJsonKeyMappings** *(dict) --* 
        
                    Maps column names to JSON keys that aren\'t identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, ``timestamp`` is a Hive keyword. If you have a JSON key named ``timestamp`` , set this parameter to ``{\"ts\": \"timestamp\"}`` to map this key to a column named ``ts`` .
        
                    - *(string) --* 
        
                      - *(string) --* 
        
                - **HiveJsonSerDe** *(dict) --* 
        
                  The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.
        
                  - **TimestampFormats** *(list) --* 
        
                    Indicates how you want Kinesis Data Firehose to parse the date and time stamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime\'s DateTimeFormat format strings. For more information, see `Class DateTimeFormat <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__ . You can also use the special value ``millis`` to parse time stamps in epoch milliseconds. If you don\'t specify a format, Kinesis Data Firehose uses ``java.sql.Timestamp::valueOf`` by default.
        
                    - *(string) --* 
        
            - **OutputFormatConfiguration** *(dict) --* 
        
              Specifies the serializer that you want Kinesis Data Firehose to use to convert the format of your data to the Parquet or ORC format.
        
              - **Serializer** *(dict) --* 
        
                Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. If both are non-null, the server rejects the request.
        
                - **ParquetSerDe** *(dict) --* 
        
                  A serializer to use for converting data to the Parquet format before storing it in Amazon S3. For more information, see `Apache Parquet <https://parquet.apache.org/documentation/latest/>`__ .
        
                  - **BlockSizeBytes** *(integer) --* 
        
                    The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.
        
                  - **PageSizeBytes** *(integer) --* 
        
                    The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.
        
                  - **Compression** *(string) --* 
        
                    The compression code to use over data blocks. The possible values are ``UNCOMPRESSED`` , ``SNAPPY`` , and ``GZIP`` , with the default being ``SNAPPY`` . Use ``SNAPPY`` for higher decompression speed. Use ``GZIP`` if the compression ration is more important than speed.
        
                  - **EnableDictionaryCompression** *(boolean) --* 
        
                    Indicates whether to enable dictionary compression.
        
                  - **MaxPaddingBytes** *(integer) --* 
        
                    The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 0.
        
                  - **WriterVersion** *(string) --* 
        
                    Indicates the version of row format to output. The possible values are ``V1`` and ``V2`` . The default is ``V1`` .
        
                - **OrcSerDe** *(dict) --* 
        
                  A serializer to use for converting data to the ORC format before storing it in Amazon S3. For more information, see `Apache ORC <https://orc.apache.org/docs/>`__ .
        
                  - **StripeSizeBytes** *(integer) --* 
        
                    The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.
        
                  - **BlockSizeBytes** *(integer) --* 
        
                    The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.
        
                  - **RowIndexStride** *(integer) --* 
        
                    The number of rows between index entries. The default is 10,000 and the minimum is 1,000.
        
                  - **EnablePadding** *(boolean) --* 
        
                    Set this to ``true`` to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is ``false`` .
        
                  - **PaddingTolerance** *(float) --* 
        
                    A number between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is 0.05, which means 5 percent of stripe size.
        
                    For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task.
        
                    Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is ``false`` .
        
                  - **Compression** *(string) --* 
        
                    The compression code to use over data blocks. The default is ``SNAPPY`` .
        
                  - **BloomFilterColumns** *(list) --* 
        
                    The column names for which you want Kinesis Data Firehose to create bloom filters. The default is ``null`` .
        
                    - *(string) --* 
        
                  - **BloomFilterFalsePositiveProbability** *(float) --* 
        
                    The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.
        
                  - **DictionaryKeyThreshold** *(float) --* 
        
                    Represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to 1.
        
                  - **FormatVersion** *(string) --* 
        
                    The version of the file to write. The possible values are ``V0_11`` and ``V0_12`` . The default is ``V0_12`` .
        
            - **Enabled** *(boolean) --* 
        
              Defaults to ``true`` . Set it to ``false`` if you want to disable format conversion while preserving the configuration details.
        
        :type RedshiftDestinationConfiguration: dict
        :param RedshiftDestinationConfiguration: 
        
          The destination in Amazon Redshift. You can specify only one destination.
        
          - **RoleARN** *(string) --* **[REQUIRED]** 
        
            The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
          - **ClusterJDBCURL** *(string) --* **[REQUIRED]** 
        
            The database connection string.
        
          - **CopyCommand** *(dict) --* **[REQUIRED]** 
        
            The ``COPY`` command.
        
            - **DataTableName** *(string) --* **[REQUIRED]** 
        
              The name of the target table. The table must already exist in the database.
        
            - **DataTableColumns** *(string) --* 
        
              A comma-separated list of column names.
        
            - **CopyOptions** *(string) --* 
        
              Optional parameters to use with the Amazon Redshift ``COPY`` command. For more information, see the \"Optional Parameters\" section of `Amazon Redshift COPY command <http://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html>`__ . Some possible examples that would apply to Kinesis Data Firehose are as follows:
        
               ``delimiter \'\t\' lzop;`` - fields are delimited with \"\t\" (TAB character) and compressed using lzop.
        
               ``delimiter \'|\'`` - fields are delimited with \"|\" (this is the default delimiter).
        
               ``delimiter \'|\' escape`` - the delimiter should be escaped.
        
               ``fixedwidth \'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6\'`` - fields are fixed width in the source, with each width specified after every column in the table.
        
               ``JSON \'s3://mybucket/jsonpaths.txt\'`` - data is in JSON format, and the path specified is the format of the data.
        
              For more examples, see `Amazon Redshift COPY command examples <http://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html>`__ .
        
          - **Username** *(string) --* **[REQUIRED]** 
        
            The name of the user.
        
          - **Password** *(string) --* **[REQUIRED]** 
        
            The user password.
        
          - **RetryOptions** *(dict) --* 
        
            The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).
        
            - **DurationInSeconds** *(integer) --* 
        
              The length of time during which Kinesis Data Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Kinesis Data Firehose does not retry if the value of ``DurationInSeconds`` is 0 (zero) or if the first delivery attempt takes longer than the current value.
        
          - **S3Configuration** *(dict) --* **[REQUIRED]** 
        
            The configuration for the intermediate Amazon S3 location from which Amazon Redshift obtains data. Restrictions are described in the topic for  CreateDeliveryStream .
        
            The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified in ``RedshiftDestinationConfiguration.S3Configuration`` because the Amazon Redshift ``COPY`` operation that reads from the S3 bucket doesn\'t support these compression formats.
        
            - **RoleARN** *(string) --* **[REQUIRED]** 
        
              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **BucketARN** *(string) --* **[REQUIRED]** 
        
              The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **Prefix** *(string) --* 
        
              The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
            - **BufferingHints** *(dict) --* 
        
              The buffering option. If no value is specified, ``BufferingHints`` object default values are used.
        
              - **SizeInMBs** *(integer) --* 
        
                Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
                We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
              - **IntervalInSeconds** *(integer) --* 
        
                Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
            - **CompressionFormat** *(string) --* 
        
              The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
              The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift ``COPY`` operation that reads from the S3 bucket.
        
            - **EncryptionConfiguration** *(dict) --* 
        
              The encryption configuration. If no value is specified, the default is no encryption.
        
              - **NoEncryptionConfig** *(string) --* 
        
                Specifically override existing encryption information to ensure that no encryption is used.
        
              - **KMSEncryptionConfig** *(dict) --* 
        
                The encryption key.
        
                - **AWSKMSKeyARN** *(string) --* **[REQUIRED]** 
        
                  The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **CloudWatchLoggingOptions** *(dict) --* 
        
              The CloudWatch logging options for your delivery stream.
        
              - **Enabled** *(boolean) --* 
        
                Enables or disables CloudWatch logging.
        
              - **LogGroupName** *(string) --* 
        
                The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
              - **LogStreamName** *(string) --* 
        
                The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
          - **ProcessingConfiguration** *(dict) --* 
        
            The data processing configuration.
        
            - **Enabled** *(boolean) --* 
        
              Enables or disables data processing.
        
            - **Processors** *(list) --* 
        
              The data processors.
        
              - *(dict) --* 
        
                Describes a data processor.
        
                - **Type** *(string) --* **[REQUIRED]** 
        
                  The type of processor.
        
                - **Parameters** *(list) --* 
        
                  The processor parameters.
        
                  - *(dict) --* 
        
                    Describes the processor parameter.
        
                    - **ParameterName** *(string) --* **[REQUIRED]** 
        
                      The name of the parameter.
        
                    - **ParameterValue** *(string) --* **[REQUIRED]** 
        
                      The parameter value.
        
          - **S3BackupMode** *(string) --* 
        
            The Amazon S3 backup mode.
        
          - **S3BackupConfiguration** *(dict) --* 
        
            The configuration for backup in Amazon S3.
        
            - **RoleARN** *(string) --* **[REQUIRED]** 
        
              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **BucketARN** *(string) --* **[REQUIRED]** 
        
              The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **Prefix** *(string) --* 
        
              The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
            - **BufferingHints** *(dict) --* 
        
              The buffering option. If no value is specified, ``BufferingHints`` object default values are used.
        
              - **SizeInMBs** *(integer) --* 
        
                Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
                We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
              - **IntervalInSeconds** *(integer) --* 
        
                Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
            - **CompressionFormat** *(string) --* 
        
              The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
              The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift ``COPY`` operation that reads from the S3 bucket.
        
            - **EncryptionConfiguration** *(dict) --* 
        
              The encryption configuration. If no value is specified, the default is no encryption.
        
              - **NoEncryptionConfig** *(string) --* 
        
                Specifically override existing encryption information to ensure that no encryption is used.
        
              - **KMSEncryptionConfig** *(dict) --* 
        
                The encryption key.
        
                - **AWSKMSKeyARN** *(string) --* **[REQUIRED]** 
        
                  The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **CloudWatchLoggingOptions** *(dict) --* 
        
              The CloudWatch logging options for your delivery stream.
        
              - **Enabled** *(boolean) --* 
        
                Enables or disables CloudWatch logging.
        
              - **LogGroupName** *(string) --* 
        
                The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
              - **LogStreamName** *(string) --* 
        
                The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
          - **CloudWatchLoggingOptions** *(dict) --* 
        
            The CloudWatch logging options for your delivery stream.
        
            - **Enabled** *(boolean) --* 
        
              Enables or disables CloudWatch logging.
        
            - **LogGroupName** *(string) --* 
        
              The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
            - **LogStreamName** *(string) --* 
        
              The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
        :type ElasticsearchDestinationConfiguration: dict
        :param ElasticsearchDestinationConfiguration: 
        
          The destination in Amazon ES. You can specify only one destination.
        
          - **RoleARN** *(string) --* **[REQUIRED]** 
        
            The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis Data Firehose for calling the Amazon ES Configuration API and for indexing documents. For more information, see `Grant Kinesis Data Firehose Access to an Amazon S3 Destination <http://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-s3>`__ and `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
          - **DomainARN** *(string) --* **[REQUIRED]** 
        
            The ARN of the Amazon ES domain. The IAM role must have permissions for ``DescribeElasticsearchDomain`` , ``DescribeElasticsearchDomains`` , and ``DescribeElasticsearchDomainConfig`` after assuming the role specified in **RoleARN** . For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
          - **IndexName** *(string) --* **[REQUIRED]** 
        
            The Elasticsearch index name.
        
          - **TypeName** *(string) --* **[REQUIRED]** 
        
            The Elasticsearch type name. For Elasticsearch 6.x, there can be only one type per index. If you try to specify a new type for an existing index that already has another type, Kinesis Data Firehose returns an error during run time.
        
          - **IndexRotationPeriod** *(string) --* 
        
            The Elasticsearch index rotation period. Index rotation appends a time stamp to the ``IndexName`` to facilitate the expiration of old data. For more information, see `Index Rotation for the Amazon ES Destination <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#es-index-rotation>`__ . The default value is ``OneDay`` .
        
          - **BufferingHints** *(dict) --* 
        
            The buffering options. If no value is specified, the default values for ``ElasticsearchBufferingHints`` are used.
        
            - **IntervalInSeconds** *(integer) --* 
        
              Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).
        
            - **SizeInMBs** *(integer) --* 
        
              Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
              We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
          - **RetryOptions** *(dict) --* 
        
            The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon ES. The default value is 300 (5 minutes).
        
            - **DurationInSeconds** *(integer) --* 
        
              After an initial failure to deliver to Amazon ES, the total amount of time during which Kinesis Data Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.
        
          - **S3BackupMode** *(string) --* 
        
            Defines how documents should be delivered to Amazon S3. When it is set to ``FailedDocumentsOnly`` , Kinesis Data Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with ``elasticsearch-failed/`` appended to the key prefix. When set to ``AllDocuments`` , Kinesis Data Firehose delivers all incoming records to Amazon S3, and also writes failed documents with ``elasticsearch-failed/`` appended to the prefix. For more information, see `Amazon S3 Backup for the Amazon ES Destination <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#es-s3-backup>`__ . Default value is ``FailedDocumentsOnly`` .
        
          - **S3Configuration** *(dict) --* **[REQUIRED]** 
        
            The configuration for the backup Amazon S3 location.
        
            - **RoleARN** *(string) --* **[REQUIRED]** 
        
              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **BucketARN** *(string) --* **[REQUIRED]** 
        
              The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **Prefix** *(string) --* 
        
              The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
            - **BufferingHints** *(dict) --* 
        
              The buffering option. If no value is specified, ``BufferingHints`` object default values are used.
        
              - **SizeInMBs** *(integer) --* 
        
                Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
                We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
              - **IntervalInSeconds** *(integer) --* 
        
                Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
            - **CompressionFormat** *(string) --* 
        
              The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
              The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift ``COPY`` operation that reads from the S3 bucket.
        
            - **EncryptionConfiguration** *(dict) --* 
        
              The encryption configuration. If no value is specified, the default is no encryption.
        
              - **NoEncryptionConfig** *(string) --* 
        
                Specifically override existing encryption information to ensure that no encryption is used.
        
              - **KMSEncryptionConfig** *(dict) --* 
        
                The encryption key.
        
                - **AWSKMSKeyARN** *(string) --* **[REQUIRED]** 
        
                  The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **CloudWatchLoggingOptions** *(dict) --* 
        
              The CloudWatch logging options for your delivery stream.
        
              - **Enabled** *(boolean) --* 
        
                Enables or disables CloudWatch logging.
        
              - **LogGroupName** *(string) --* 
        
                The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
              - **LogStreamName** *(string) --* 
        
                The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
          - **ProcessingConfiguration** *(dict) --* 
        
            The data processing configuration.
        
            - **Enabled** *(boolean) --* 
        
              Enables or disables data processing.
        
            - **Processors** *(list) --* 
        
              The data processors.
        
              - *(dict) --* 
        
                Describes a data processor.
        
                - **Type** *(string) --* **[REQUIRED]** 
        
                  The type of processor.
        
                - **Parameters** *(list) --* 
        
                  The processor parameters.
        
                  - *(dict) --* 
        
                    Describes the processor parameter.
        
                    - **ParameterName** *(string) --* **[REQUIRED]** 
        
                      The name of the parameter.
        
                    - **ParameterValue** *(string) --* **[REQUIRED]** 
        
                      The parameter value.
        
          - **CloudWatchLoggingOptions** *(dict) --* 
        
            The Amazon CloudWatch logging options for your delivery stream.
        
            - **Enabled** *(boolean) --* 
        
              Enables or disables CloudWatch logging.
        
            - **LogGroupName** *(string) --* 
        
              The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
            - **LogStreamName** *(string) --* 
        
              The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
        :type SplunkDestinationConfiguration: dict
        :param SplunkDestinationConfiguration: 
        
          The destination in Splunk. You can specify only one destination.
        
          - **HECEndpoint** *(string) --* **[REQUIRED]** 
        
            The HTTP Event Collector (HEC) endpoint to which Kinesis Data Firehose sends your data.
        
          - **HECEndpointType** *(string) --* **[REQUIRED]** 
        
            This type can be either \"Raw\" or \"Event.\"
        
          - **HECToken** *(string) --* **[REQUIRED]** 
        
            This is a GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.
        
          - **HECAcknowledgmentTimeoutInSeconds** *(integer) --* 
        
            The amount of time that Kinesis Data Firehose waits to receive an acknowledgment from Splunk after it sends it data. At the end of the timeout period, Kinesis Data Firehose either tries to send the data again or considers it an error, based on your retry settings.
        
          - **RetryOptions** *(dict) --* 
        
            The retry behavior in case Kinesis Data Firehose is unable to deliver data to Splunk, or if it doesn\'t receive an acknowledgment of receipt from Splunk.
        
            - **DurationInSeconds** *(integer) --* 
        
              The total amount of time that Kinesis Data Firehose spends on retries. This duration starts after the initial attempt to send data to Splunk fails. It doesn\'t include the periods during which Kinesis Data Firehose waits for acknowledgment from Splunk after each attempt.
        
          - **S3BackupMode** *(string) --* 
        
            Defines how documents should be delivered to Amazon S3. When set to ``FailedDocumentsOnly`` , Kinesis Data Firehose writes any data that could not be indexed to the configured Amazon S3 destination. When set to ``AllDocuments`` , Kinesis Data Firehose delivers all incoming records to Amazon S3, and also writes failed documents to Amazon S3. Default value is ``FailedDocumentsOnly`` . 
        
          - **S3Configuration** *(dict) --* **[REQUIRED]** 
        
            The configuration for the backup Amazon S3 location.
        
            - **RoleARN** *(string) --* **[REQUIRED]** 
        
              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **BucketARN** *(string) --* **[REQUIRED]** 
        
              The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **Prefix** *(string) --* 
        
              The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
            - **BufferingHints** *(dict) --* 
        
              The buffering option. If no value is specified, ``BufferingHints`` object default values are used.
        
              - **SizeInMBs** *(integer) --* 
        
                Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
                We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
              - **IntervalInSeconds** *(integer) --* 
        
                Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
            - **CompressionFormat** *(string) --* 
        
              The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
              The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift ``COPY`` operation that reads from the S3 bucket.
        
            - **EncryptionConfiguration** *(dict) --* 
        
              The encryption configuration. If no value is specified, the default is no encryption.
        
              - **NoEncryptionConfig** *(string) --* 
        
                Specifically override existing encryption information to ensure that no encryption is used.
        
              - **KMSEncryptionConfig** *(dict) --* 
        
                The encryption key.
        
                - **AWSKMSKeyARN** *(string) --* **[REQUIRED]** 
        
                  The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **CloudWatchLoggingOptions** *(dict) --* 
        
              The CloudWatch logging options for your delivery stream.
        
              - **Enabled** *(boolean) --* 
        
                Enables or disables CloudWatch logging.
        
              - **LogGroupName** *(string) --* 
        
                The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
              - **LogStreamName** *(string) --* 
        
                The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
          - **ProcessingConfiguration** *(dict) --* 
        
            The data processing configuration.
        
            - **Enabled** *(boolean) --* 
        
              Enables or disables data processing.
        
            - **Processors** *(list) --* 
        
              The data processors.
        
              - *(dict) --* 
        
                Describes a data processor.
        
                - **Type** *(string) --* **[REQUIRED]** 
        
                  The type of processor.
        
                - **Parameters** *(list) --* 
        
                  The processor parameters.
        
                  - *(dict) --* 
        
                    Describes the processor parameter.
        
                    - **ParameterName** *(string) --* **[REQUIRED]** 
        
                      The name of the parameter.
        
                    - **ParameterValue** *(string) --* **[REQUIRED]** 
        
                      The parameter value.
        
          - **CloudWatchLoggingOptions** *(dict) --* 
        
            The Amazon CloudWatch logging options for your delivery stream.
        
            - **Enabled** *(boolean) --* 
        
              Enables or disables CloudWatch logging.
        
            - **LogGroupName** *(string) --* 
        
              The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
            - **LogStreamName** *(string) --* 
        
              The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
        :type Tags: list
        :param Tags: 
        
          A set of tags to assign to the delivery stream. A tag is a key-value pair that you can define and assign to AWS resources. Tags are metadata. For example, you can add friendly names and descriptions or other types of information that can help you distinguish the delivery stream. For more information about tags, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in the AWS Billing and Cost Management User Guide.
        
          You can specify up to 50 tags when creating a delivery stream.
        
          - *(dict) --* 
        
            Metadata that you can assign to a delivery stream, consisting of a key-value pair.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @
        
            - **Value** *(string) --* 
        
              An optional string, which you can use to describe or define the tag. Maximum length: 256 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeliveryStreamARN\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DeliveryStreamARN** *(string) --* 
        
              The ARN of the delivery stream.
        
        """
        pass

    def delete_delivery_stream(self, DeliveryStreamName: str) -> Dict:
        """
        
        You can delete a delivery stream only if it is in ``ACTIVE`` or ``DELETING`` state, and not in the ``CREATING`` state. While the deletion request is in process, the delivery stream is in the ``DELETING`` state.
        
        To check the state of a delivery stream, use  DescribeDeliveryStream .
        
        While the delivery stream is ``DELETING`` state, the service might continue to accept the records, but it doesn\'t make any guarantees with respect to delivering the data. Therefore, as a best practice, you should first stop any applications that are sending records before deleting a delivery stream.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/firehose-2015-08-04/DeleteDeliveryStream>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_delivery_stream(
              DeliveryStreamName=\'string\'
          )
        :type DeliveryStreamName: string
        :param DeliveryStreamName: **[REQUIRED]** 
        
          The name of the delivery stream.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def describe_delivery_stream(self, DeliveryStreamName: str, Limit: int = None, ExclusiveStartDestinationId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/firehose-2015-08-04/DescribeDeliveryStream>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_delivery_stream(
              DeliveryStreamName=\'string\',
              Limit=123,
              ExclusiveStartDestinationId=\'string\'
          )
        :type DeliveryStreamName: string
        :param DeliveryStreamName: **[REQUIRED]** 
        
          The name of the delivery stream.
        
        :type Limit: integer
        :param Limit: 
        
          The limit on the number of destinations to return. You can have one destination per delivery stream.
        
        :type ExclusiveStartDestinationId: string
        :param ExclusiveStartDestinationId: 
        
          The ID of the destination to start returning the destination information. Kinesis Data Firehose supports one destination per delivery stream.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeliveryStreamDescription\': {
                    \'DeliveryStreamName\': \'string\',
                    \'DeliveryStreamARN\': \'string\',
                    \'DeliveryStreamStatus\': \'CREATING\'|\'DELETING\'|\'ACTIVE\',
                    \'DeliveryStreamEncryptionConfiguration\': {
                        \'Status\': \'ENABLED\'|\'ENABLING\'|\'DISABLED\'|\'DISABLING\'
                    },
                    \'DeliveryStreamType\': \'DirectPut\'|\'KinesisStreamAsSource\',
                    \'VersionId\': \'string\',
                    \'CreateTimestamp\': datetime(2015, 1, 1),
                    \'LastUpdateTimestamp\': datetime(2015, 1, 1),
                    \'Source\': {
                        \'KinesisStreamSourceDescription\': {
                            \'KinesisStreamARN\': \'string\',
                            \'RoleARN\': \'string\',
                            \'DeliveryStartTimestamp\': datetime(2015, 1, 1)
                        }
                    },
                    \'Destinations\': [
                        {
                            \'DestinationId\': \'string\',
                            \'S3DestinationDescription\': {
                                \'RoleARN\': \'string\',
                                \'BucketARN\': \'string\',
                                \'Prefix\': \'string\',
                                \'BufferingHints\': {
                                    \'SizeInMBs\': 123,
                                    \'IntervalInSeconds\': 123
                                },
                                \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                                \'EncryptionConfiguration\': {
                                    \'NoEncryptionConfig\': \'NoEncryption\',
                                    \'KMSEncryptionConfig\': {
                                        \'AWSKMSKeyARN\': \'string\'
                                    }
                                },
                                \'CloudWatchLoggingOptions\': {
                                    \'Enabled\': True|False,
                                    \'LogGroupName\': \'string\',
                                    \'LogStreamName\': \'string\'
                                }
                            },
                            \'ExtendedS3DestinationDescription\': {
                                \'RoleARN\': \'string\',
                                \'BucketARN\': \'string\',
                                \'Prefix\': \'string\',
                                \'BufferingHints\': {
                                    \'SizeInMBs\': 123,
                                    \'IntervalInSeconds\': 123
                                },
                                \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                                \'EncryptionConfiguration\': {
                                    \'NoEncryptionConfig\': \'NoEncryption\',
                                    \'KMSEncryptionConfig\': {
                                        \'AWSKMSKeyARN\': \'string\'
                                    }
                                },
                                \'CloudWatchLoggingOptions\': {
                                    \'Enabled\': True|False,
                                    \'LogGroupName\': \'string\',
                                    \'LogStreamName\': \'string\'
                                },
                                \'ProcessingConfiguration\': {
                                    \'Enabled\': True|False,
                                    \'Processors\': [
                                        {
                                            \'Type\': \'Lambda\',
                                            \'Parameters\': [
                                                {
                                                    \'ParameterName\': \'LambdaArn\'|\'NumberOfRetries\'|\'RoleArn\'|\'BufferSizeInMBs\'|\'BufferIntervalInSeconds\',
                                                    \'ParameterValue\': \'string\'
                                                },
                                            ]
                                        },
                                    ]
                                },
                                \'S3BackupMode\': \'Disabled\'|\'Enabled\',
                                \'S3BackupDescription\': {
                                    \'RoleARN\': \'string\',
                                    \'BucketARN\': \'string\',
                                    \'Prefix\': \'string\',
                                    \'BufferingHints\': {
                                        \'SizeInMBs\': 123,
                                        \'IntervalInSeconds\': 123
                                    },
                                    \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                                    \'EncryptionConfiguration\': {
                                        \'NoEncryptionConfig\': \'NoEncryption\',
                                        \'KMSEncryptionConfig\': {
                                            \'AWSKMSKeyARN\': \'string\'
                                        }
                                    },
                                    \'CloudWatchLoggingOptions\': {
                                        \'Enabled\': True|False,
                                        \'LogGroupName\': \'string\',
                                        \'LogStreamName\': \'string\'
                                    }
                                },
                                \'DataFormatConversionConfiguration\': {
                                    \'SchemaConfiguration\': {
                                        \'RoleARN\': \'string\',
                                        \'CatalogId\': \'string\',
                                        \'DatabaseName\': \'string\',
                                        \'TableName\': \'string\',
                                        \'Region\': \'string\',
                                        \'VersionId\': \'string\'
                                    },
                                    \'InputFormatConfiguration\': {
                                        \'Deserializer\': {
                                            \'OpenXJsonSerDe\': {
                                                \'ConvertDotsInJsonKeysToUnderscores\': True|False,
                                                \'CaseInsensitive\': True|False,
                                                \'ColumnToJsonKeyMappings\': {
                                                    \'string\': \'string\'
                                                }
                                            },
                                            \'HiveJsonSerDe\': {
                                                \'TimestampFormats\': [
                                                    \'string\',
                                                ]
                                            }
                                        }
                                    },
                                    \'OutputFormatConfiguration\': {
                                        \'Serializer\': {
                                            \'ParquetSerDe\': {
                                                \'BlockSizeBytes\': 123,
                                                \'PageSizeBytes\': 123,
                                                \'Compression\': \'UNCOMPRESSED\'|\'GZIP\'|\'SNAPPY\',
                                                \'EnableDictionaryCompression\': True|False,
                                                \'MaxPaddingBytes\': 123,
                                                \'WriterVersion\': \'V1\'|\'V2\'
                                            },
                                            \'OrcSerDe\': {
                                                \'StripeSizeBytes\': 123,
                                                \'BlockSizeBytes\': 123,
                                                \'RowIndexStride\': 123,
                                                \'EnablePadding\': True|False,
                                                \'PaddingTolerance\': 123.0,
                                                \'Compression\': \'NONE\'|\'ZLIB\'|\'SNAPPY\',
                                                \'BloomFilterColumns\': [
                                                    \'string\',
                                                ],
                                                \'BloomFilterFalsePositiveProbability\': 123.0,
                                                \'DictionaryKeyThreshold\': 123.0,
                                                \'FormatVersion\': \'V0_11\'|\'V0_12\'
                                            }
                                        }
                                    },
                                    \'Enabled\': True|False
                                }
                            },
                            \'RedshiftDestinationDescription\': {
                                \'RoleARN\': \'string\',
                                \'ClusterJDBCURL\': \'string\',
                                \'CopyCommand\': {
                                    \'DataTableName\': \'string\',
                                    \'DataTableColumns\': \'string\',
                                    \'CopyOptions\': \'string\'
                                },
                                \'Username\': \'string\',
                                \'RetryOptions\': {
                                    \'DurationInSeconds\': 123
                                },
                                \'S3DestinationDescription\': {
                                    \'RoleARN\': \'string\',
                                    \'BucketARN\': \'string\',
                                    \'Prefix\': \'string\',
                                    \'BufferingHints\': {
                                        \'SizeInMBs\': 123,
                                        \'IntervalInSeconds\': 123
                                    },
                                    \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                                    \'EncryptionConfiguration\': {
                                        \'NoEncryptionConfig\': \'NoEncryption\',
                                        \'KMSEncryptionConfig\': {
                                            \'AWSKMSKeyARN\': \'string\'
                                        }
                                    },
                                    \'CloudWatchLoggingOptions\': {
                                        \'Enabled\': True|False,
                                        \'LogGroupName\': \'string\',
                                        \'LogStreamName\': \'string\'
                                    }
                                },
                                \'ProcessingConfiguration\': {
                                    \'Enabled\': True|False,
                                    \'Processors\': [
                                        {
                                            \'Type\': \'Lambda\',
                                            \'Parameters\': [
                                                {
                                                    \'ParameterName\': \'LambdaArn\'|\'NumberOfRetries\'|\'RoleArn\'|\'BufferSizeInMBs\'|\'BufferIntervalInSeconds\',
                                                    \'ParameterValue\': \'string\'
                                                },
                                            ]
                                        },
                                    ]
                                },
                                \'S3BackupMode\': \'Disabled\'|\'Enabled\',
                                \'S3BackupDescription\': {
                                    \'RoleARN\': \'string\',
                                    \'BucketARN\': \'string\',
                                    \'Prefix\': \'string\',
                                    \'BufferingHints\': {
                                        \'SizeInMBs\': 123,
                                        \'IntervalInSeconds\': 123
                                    },
                                    \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                                    \'EncryptionConfiguration\': {
                                        \'NoEncryptionConfig\': \'NoEncryption\',
                                        \'KMSEncryptionConfig\': {
                                            \'AWSKMSKeyARN\': \'string\'
                                        }
                                    },
                                    \'CloudWatchLoggingOptions\': {
                                        \'Enabled\': True|False,
                                        \'LogGroupName\': \'string\',
                                        \'LogStreamName\': \'string\'
                                    }
                                },
                                \'CloudWatchLoggingOptions\': {
                                    \'Enabled\': True|False,
                                    \'LogGroupName\': \'string\',
                                    \'LogStreamName\': \'string\'
                                }
                            },
                            \'ElasticsearchDestinationDescription\': {
                                \'RoleARN\': \'string\',
                                \'DomainARN\': \'string\',
                                \'IndexName\': \'string\',
                                \'TypeName\': \'string\',
                                \'IndexRotationPeriod\': \'NoRotation\'|\'OneHour\'|\'OneDay\'|\'OneWeek\'|\'OneMonth\',
                                \'BufferingHints\': {
                                    \'IntervalInSeconds\': 123,
                                    \'SizeInMBs\': 123
                                },
                                \'RetryOptions\': {
                                    \'DurationInSeconds\': 123
                                },
                                \'S3BackupMode\': \'FailedDocumentsOnly\'|\'AllDocuments\',
                                \'S3DestinationDescription\': {
                                    \'RoleARN\': \'string\',
                                    \'BucketARN\': \'string\',
                                    \'Prefix\': \'string\',
                                    \'BufferingHints\': {
                                        \'SizeInMBs\': 123,
                                        \'IntervalInSeconds\': 123
                                    },
                                    \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                                    \'EncryptionConfiguration\': {
                                        \'NoEncryptionConfig\': \'NoEncryption\',
                                        \'KMSEncryptionConfig\': {
                                            \'AWSKMSKeyARN\': \'string\'
                                        }
                                    },
                                    \'CloudWatchLoggingOptions\': {
                                        \'Enabled\': True|False,
                                        \'LogGroupName\': \'string\',
                                        \'LogStreamName\': \'string\'
                                    }
                                },
                                \'ProcessingConfiguration\': {
                                    \'Enabled\': True|False,
                                    \'Processors\': [
                                        {
                                            \'Type\': \'Lambda\',
                                            \'Parameters\': [
                                                {
                                                    \'ParameterName\': \'LambdaArn\'|\'NumberOfRetries\'|\'RoleArn\'|\'BufferSizeInMBs\'|\'BufferIntervalInSeconds\',
                                                    \'ParameterValue\': \'string\'
                                                },
                                            ]
                                        },
                                    ]
                                },
                                \'CloudWatchLoggingOptions\': {
                                    \'Enabled\': True|False,
                                    \'LogGroupName\': \'string\',
                                    \'LogStreamName\': \'string\'
                                }
                            },
                            \'SplunkDestinationDescription\': {
                                \'HECEndpoint\': \'string\',
                                \'HECEndpointType\': \'Raw\'|\'Event\',
                                \'HECToken\': \'string\',
                                \'HECAcknowledgmentTimeoutInSeconds\': 123,
                                \'RetryOptions\': {
                                    \'DurationInSeconds\': 123
                                },
                                \'S3BackupMode\': \'FailedEventsOnly\'|\'AllEvents\',
                                \'S3DestinationDescription\': {
                                    \'RoleARN\': \'string\',
                                    \'BucketARN\': \'string\',
                                    \'Prefix\': \'string\',
                                    \'BufferingHints\': {
                                        \'SizeInMBs\': 123,
                                        \'IntervalInSeconds\': 123
                                    },
                                    \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                                    \'EncryptionConfiguration\': {
                                        \'NoEncryptionConfig\': \'NoEncryption\',
                                        \'KMSEncryptionConfig\': {
                                            \'AWSKMSKeyARN\': \'string\'
                                        }
                                    },
                                    \'CloudWatchLoggingOptions\': {
                                        \'Enabled\': True|False,
                                        \'LogGroupName\': \'string\',
                                        \'LogStreamName\': \'string\'
                                    }
                                },
                                \'ProcessingConfiguration\': {
                                    \'Enabled\': True|False,
                                    \'Processors\': [
                                        {
                                            \'Type\': \'Lambda\',
                                            \'Parameters\': [
                                                {
                                                    \'ParameterName\': \'LambdaArn\'|\'NumberOfRetries\'|\'RoleArn\'|\'BufferSizeInMBs\'|\'BufferIntervalInSeconds\',
                                                    \'ParameterValue\': \'string\'
                                                },
                                            ]
                                        },
                                    ]
                                },
                                \'CloudWatchLoggingOptions\': {
                                    \'Enabled\': True|False,
                                    \'LogGroupName\': \'string\',
                                    \'LogStreamName\': \'string\'
                                }
                            }
                        },
                    ],
                    \'HasMoreDestinations\': True|False
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DeliveryStreamDescription** *(dict) --* 
        
              Information about the delivery stream.
        
              - **DeliveryStreamName** *(string) --* 
        
                The name of the delivery stream.
        
              - **DeliveryStreamARN** *(string) --* 
        
                The Amazon Resource Name (ARN) of the delivery stream. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
              - **DeliveryStreamStatus** *(string) --* 
        
                The status of the delivery stream.
        
              - **DeliveryStreamEncryptionConfiguration** *(dict) --* 
        
                Indicates the server-side encryption (SSE) status for the delivery stream.
        
                - **Status** *(string) --* 
        
                  For a full description of the different values of this status, see  StartDeliveryStreamEncryption and  StopDeliveryStreamEncryption .
        
              - **DeliveryStreamType** *(string) --* 
        
                The delivery stream type. This can be one of the following values:
        
                * ``DirectPut`` : Provider applications access the delivery stream directly. 
                 
                * ``KinesisStreamAsSource`` : The delivery stream uses a Kinesis data stream as a source. 
                 
              - **VersionId** *(string) --* 
        
                Each time the destination is updated for a delivery stream, the version ID is changed, and the current version ID is required when updating the destination. This is so that the service knows it is applying the changes to the correct version of the delivery stream.
        
              - **CreateTimestamp** *(datetime) --* 
        
                The date and time that the delivery stream was created.
        
              - **LastUpdateTimestamp** *(datetime) --* 
        
                The date and time that the delivery stream was last updated.
        
              - **Source** *(dict) --* 
        
                If the ``DeliveryStreamType`` parameter is ``KinesisStreamAsSource`` , a  SourceDescription object describing the source Kinesis data stream.
        
                - **KinesisStreamSourceDescription** *(dict) --* 
        
                  The  KinesisStreamSourceDescription value for the source Kinesis data stream.
        
                  - **KinesisStreamARN** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the source Kinesis data stream. For more information, see `Amazon Kinesis Data Streams ARN Format <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams>`__ .
        
                  - **RoleARN** *(string) --* 
        
                    The ARN of the role used by the source Kinesis data stream. For more information, see `AWS Identity and Access Management (IAM) ARN Format <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam>`__ .
        
                  - **DeliveryStartTimestamp** *(datetime) --* 
        
                    Kinesis Data Firehose starts retrieving records from the Kinesis data stream starting with this time stamp.
        
              - **Destinations** *(list) --* 
        
                The destinations.
        
                - *(dict) --* 
        
                  Describes the destination for a delivery stream.
        
                  - **DestinationId** *(string) --* 
        
                    The ID of the destination.
        
                  - **S3DestinationDescription** *(dict) --* 
        
                    [Deprecated] The destination in Amazon S3.
        
                    - **RoleARN** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                    - **BucketARN** *(string) --* 
        
                      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                    - **Prefix** *(string) --* 
        
                      The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
                    - **BufferingHints** *(dict) --* 
        
                      The buffering option. If no value is specified, ``BufferingHints`` object default values are used.
        
                      - **SizeInMBs** *(integer) --* 
        
                        Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
                        We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
                      - **IntervalInSeconds** *(integer) --* 
        
                        Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
                    - **CompressionFormat** *(string) --* 
        
                      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
                    - **EncryptionConfiguration** *(dict) --* 
        
                      The encryption configuration. If no value is specified, the default is no encryption.
        
                      - **NoEncryptionConfig** *(string) --* 
        
                        Specifically override existing encryption information to ensure that no encryption is used.
        
                      - **KMSEncryptionConfig** *(dict) --* 
        
                        The encryption key.
        
                        - **AWSKMSKeyARN** *(string) --* 
        
                          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                    - **CloudWatchLoggingOptions** *(dict) --* 
        
                      The Amazon CloudWatch logging options for your delivery stream.
        
                      - **Enabled** *(boolean) --* 
        
                        Enables or disables CloudWatch logging.
        
                      - **LogGroupName** *(string) --* 
        
                        The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
                      - **LogStreamName** *(string) --* 
        
                        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
                  - **ExtendedS3DestinationDescription** *(dict) --* 
        
                    The destination in Amazon S3.
        
                    - **RoleARN** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                    - **BucketARN** *(string) --* 
        
                      The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                    - **Prefix** *(string) --* 
        
                      The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
                    - **BufferingHints** *(dict) --* 
        
                      The buffering option.
        
                      - **SizeInMBs** *(integer) --* 
        
                        Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
                        We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
                      - **IntervalInSeconds** *(integer) --* 
        
                        Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
                    - **CompressionFormat** *(string) --* 
        
                      The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
                    - **EncryptionConfiguration** *(dict) --* 
        
                      The encryption configuration. If no value is specified, the default is no encryption.
        
                      - **NoEncryptionConfig** *(string) --* 
        
                        Specifically override existing encryption information to ensure that no encryption is used.
        
                      - **KMSEncryptionConfig** *(dict) --* 
        
                        The encryption key.
        
                        - **AWSKMSKeyARN** *(string) --* 
        
                          The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                    - **CloudWatchLoggingOptions** *(dict) --* 
        
                      The Amazon CloudWatch logging options for your delivery stream.
        
                      - **Enabled** *(boolean) --* 
        
                        Enables or disables CloudWatch logging.
        
                      - **LogGroupName** *(string) --* 
        
                        The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
                      - **LogStreamName** *(string) --* 
        
                        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
                    - **ProcessingConfiguration** *(dict) --* 
        
                      The data processing configuration.
        
                      - **Enabled** *(boolean) --* 
        
                        Enables or disables data processing.
        
                      - **Processors** *(list) --* 
        
                        The data processors.
        
                        - *(dict) --* 
        
                          Describes a data processor.
        
                          - **Type** *(string) --* 
        
                            The type of processor.
        
                          - **Parameters** *(list) --* 
        
                            The processor parameters.
        
                            - *(dict) --* 
        
                              Describes the processor parameter.
        
                              - **ParameterName** *(string) --* 
        
                                The name of the parameter.
        
                              - **ParameterValue** *(string) --* 
        
                                The parameter value.
        
                    - **S3BackupMode** *(string) --* 
        
                      The Amazon S3 backup mode.
        
                    - **S3BackupDescription** *(dict) --* 
        
                      The configuration for backup in Amazon S3.
        
                      - **RoleARN** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                      - **BucketARN** *(string) --* 
        
                        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                      - **Prefix** *(string) --* 
        
                        The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
                      - **BufferingHints** *(dict) --* 
        
                        The buffering option. If no value is specified, ``BufferingHints`` object default values are used.
        
                        - **SizeInMBs** *(integer) --* 
        
                          Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
                          We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
                        - **IntervalInSeconds** *(integer) --* 
        
                          Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
                      - **CompressionFormat** *(string) --* 
        
                        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
                      - **EncryptionConfiguration** *(dict) --* 
        
                        The encryption configuration. If no value is specified, the default is no encryption.
        
                        - **NoEncryptionConfig** *(string) --* 
        
                          Specifically override existing encryption information to ensure that no encryption is used.
        
                        - **KMSEncryptionConfig** *(dict) --* 
        
                          The encryption key.
        
                          - **AWSKMSKeyARN** *(string) --* 
        
                            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                      - **CloudWatchLoggingOptions** *(dict) --* 
        
                        The Amazon CloudWatch logging options for your delivery stream.
        
                        - **Enabled** *(boolean) --* 
        
                          Enables or disables CloudWatch logging.
        
                        - **LogGroupName** *(string) --* 
        
                          The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
                        - **LogStreamName** *(string) --* 
        
                          The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
                    - **DataFormatConversionConfiguration** *(dict) --* 
        
                      The serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3.
        
                      - **SchemaConfiguration** *(dict) --* 
        
                        Specifies the AWS Glue Data Catalog table that contains the column information.
        
                        - **RoleARN** *(string) --* 
        
                          The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren\'t allowed.
        
                        - **CatalogId** *(string) --* 
        
                          The ID of the AWS Glue Data Catalog. If you don\'t supply this, the AWS account ID is used by default.
        
                        - **DatabaseName** *(string) --* 
        
                          Specifies the name of the AWS Glue database that contains the schema for the output data.
        
                        - **TableName** *(string) --* 
        
                          Specifies the AWS Glue table that contains the column information that constitutes your data schema.
        
                        - **Region** *(string) --* 
        
                          If you don\'t specify an AWS Region, the default is the current Region.
        
                        - **VersionId** *(string) --* 
        
                          Specifies the table version for the output data schema. If you don\'t specify this version ID, or if you set it to ``LATEST`` , Kinesis Data Firehose uses the most recent version. This means that any updates to the table are automatically picked up.
        
                      - **InputFormatConfiguration** *(dict) --* 
        
                        Specifies the deserializer that you want Kinesis Data Firehose to use to convert the format of your data from JSON.
        
                        - **Deserializer** *(dict) --* 
        
                          Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the request.
        
                          - **OpenXJsonSerDe** *(dict) --* 
        
                            The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.
        
                            - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --* 
        
                              When set to ``true`` , specifies that the names of the keys include dots and that you want Kinesis Data Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is \"a.b\", you can define the column name to be \"a_b\" when using this option.
        
                              The default is ``false`` .
        
                            - **CaseInsensitive** *(boolean) --* 
        
                              When set to ``true`` , which is the default, Kinesis Data Firehose converts JSON keys to lowercase before deserializing them.
        
                            - **ColumnToJsonKeyMappings** *(dict) --* 
        
                              Maps column names to JSON keys that aren\'t identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, ``timestamp`` is a Hive keyword. If you have a JSON key named ``timestamp`` , set this parameter to ``{\"ts\": \"timestamp\"}`` to map this key to a column named ``ts`` .
        
                              - *(string) --* 
                                
                                - *(string) --* 
                          
                          - **HiveJsonSerDe** *(dict) --* 
        
                            The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.
        
                            - **TimestampFormats** *(list) --* 
        
                              Indicates how you want Kinesis Data Firehose to parse the date and time stamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime\'s DateTimeFormat format strings. For more information, see `Class DateTimeFormat <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__ . You can also use the special value ``millis`` to parse time stamps in epoch milliseconds. If you don\'t specify a format, Kinesis Data Firehose uses ``java.sql.Timestamp::valueOf`` by default.
        
                              - *(string) --* 
                          
                      - **OutputFormatConfiguration** *(dict) --* 
        
                        Specifies the serializer that you want Kinesis Data Firehose to use to convert the format of your data to the Parquet or ORC format.
        
                        - **Serializer** *(dict) --* 
        
                          Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. If both are non-null, the server rejects the request.
        
                          - **ParquetSerDe** *(dict) --* 
        
                            A serializer to use for converting data to the Parquet format before storing it in Amazon S3. For more information, see `Apache Parquet <https://parquet.apache.org/documentation/latest/>`__ .
        
                            - **BlockSizeBytes** *(integer) --* 
        
                              The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.
        
                            - **PageSizeBytes** *(integer) --* 
        
                              The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.
        
                            - **Compression** *(string) --* 
        
                              The compression code to use over data blocks. The possible values are ``UNCOMPRESSED`` , ``SNAPPY`` , and ``GZIP`` , with the default being ``SNAPPY`` . Use ``SNAPPY`` for higher decompression speed. Use ``GZIP`` if the compression ration is more important than speed.
        
                            - **EnableDictionaryCompression** *(boolean) --* 
        
                              Indicates whether to enable dictionary compression.
        
                            - **MaxPaddingBytes** *(integer) --* 
        
                              The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 0.
        
                            - **WriterVersion** *(string) --* 
        
                              Indicates the version of row format to output. The possible values are ``V1`` and ``V2`` . The default is ``V1`` .
        
                          - **OrcSerDe** *(dict) --* 
        
                            A serializer to use for converting data to the ORC format before storing it in Amazon S3. For more information, see `Apache ORC <https://orc.apache.org/docs/>`__ .
        
                            - **StripeSizeBytes** *(integer) --* 
        
                              The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.
        
                            - **BlockSizeBytes** *(integer) --* 
        
                              The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.
        
                            - **RowIndexStride** *(integer) --* 
        
                              The number of rows between index entries. The default is 10,000 and the minimum is 1,000.
        
                            - **EnablePadding** *(boolean) --* 
        
                              Set this to ``true`` to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is ``false`` .
        
                            - **PaddingTolerance** *(float) --* 
        
                              A number between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is 0.05, which means 5 percent of stripe size.
        
                              For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task.
        
                              Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is ``false`` .
        
                            - **Compression** *(string) --* 
        
                              The compression code to use over data blocks. The default is ``SNAPPY`` .
        
                            - **BloomFilterColumns** *(list) --* 
        
                              The column names for which you want Kinesis Data Firehose to create bloom filters. The default is ``null`` .
        
                              - *(string) --* 
                          
                            - **BloomFilterFalsePositiveProbability** *(float) --* 
        
                              The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.
        
                            - **DictionaryKeyThreshold** *(float) --* 
        
                              Represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to 1.
        
                            - **FormatVersion** *(string) --* 
        
                              The version of the file to write. The possible values are ``V0_11`` and ``V0_12`` . The default is ``V0_12`` .
        
                      - **Enabled** *(boolean) --* 
        
                        Defaults to ``true`` . Set it to ``false`` if you want to disable format conversion while preserving the configuration details.
        
                  - **RedshiftDestinationDescription** *(dict) --* 
        
                    The destination in Amazon Redshift.
        
                    - **RoleARN** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                    - **ClusterJDBCURL** *(string) --* 
        
                      The database connection string.
        
                    - **CopyCommand** *(dict) --* 
        
                      The ``COPY`` command.
        
                      - **DataTableName** *(string) --* 
        
                        The name of the target table. The table must already exist in the database.
        
                      - **DataTableColumns** *(string) --* 
        
                        A comma-separated list of column names.
        
                      - **CopyOptions** *(string) --* 
        
                        Optional parameters to use with the Amazon Redshift ``COPY`` command. For more information, see the \"Optional Parameters\" section of `Amazon Redshift COPY command <http://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html>`__ . Some possible examples that would apply to Kinesis Data Firehose are as follows:
        
                         ``delimiter \'\t\' lzop;`` - fields are delimited with \"\t\" (TAB character) and compressed using lzop.
        
                         ``delimiter \'|\'`` - fields are delimited with \"|\" (this is the default delimiter).
        
                         ``delimiter \'|\' escape`` - the delimiter should be escaped.
        
                         ``fixedwidth \'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6\'`` - fields are fixed width in the source, with each width specified after every column in the table.
        
                         ``JSON \'s3://mybucket/jsonpaths.txt\'`` - data is in JSON format, and the path specified is the format of the data.
        
                        For more examples, see `Amazon Redshift COPY command examples <http://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html>`__ .
        
                    - **Username** *(string) --* 
        
                      The name of the user.
        
                    - **RetryOptions** *(dict) --* 
        
                      The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).
        
                      - **DurationInSeconds** *(integer) --* 
        
                        The length of time during which Kinesis Data Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Kinesis Data Firehose does not retry if the value of ``DurationInSeconds`` is 0 (zero) or if the first delivery attempt takes longer than the current value.
        
                    - **S3DestinationDescription** *(dict) --* 
        
                      The Amazon S3 destination.
        
                      - **RoleARN** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                      - **BucketARN** *(string) --* 
        
                        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                      - **Prefix** *(string) --* 
        
                        The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
                      - **BufferingHints** *(dict) --* 
        
                        The buffering option. If no value is specified, ``BufferingHints`` object default values are used.
        
                        - **SizeInMBs** *(integer) --* 
        
                          Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
                          We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
                        - **IntervalInSeconds** *(integer) --* 
        
                          Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
                      - **CompressionFormat** *(string) --* 
        
                        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
                      - **EncryptionConfiguration** *(dict) --* 
        
                        The encryption configuration. If no value is specified, the default is no encryption.
        
                        - **NoEncryptionConfig** *(string) --* 
        
                          Specifically override existing encryption information to ensure that no encryption is used.
        
                        - **KMSEncryptionConfig** *(dict) --* 
        
                          The encryption key.
        
                          - **AWSKMSKeyARN** *(string) --* 
        
                            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                      - **CloudWatchLoggingOptions** *(dict) --* 
        
                        The Amazon CloudWatch logging options for your delivery stream.
        
                        - **Enabled** *(boolean) --* 
        
                          Enables or disables CloudWatch logging.
        
                        - **LogGroupName** *(string) --* 
        
                          The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
                        - **LogStreamName** *(string) --* 
        
                          The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
                    - **ProcessingConfiguration** *(dict) --* 
        
                      The data processing configuration.
        
                      - **Enabled** *(boolean) --* 
        
                        Enables or disables data processing.
        
                      - **Processors** *(list) --* 
        
                        The data processors.
        
                        - *(dict) --* 
        
                          Describes a data processor.
        
                          - **Type** *(string) --* 
        
                            The type of processor.
        
                          - **Parameters** *(list) --* 
        
                            The processor parameters.
        
                            - *(dict) --* 
        
                              Describes the processor parameter.
        
                              - **ParameterName** *(string) --* 
        
                                The name of the parameter.
        
                              - **ParameterValue** *(string) --* 
        
                                The parameter value.
        
                    - **S3BackupMode** *(string) --* 
        
                      The Amazon S3 backup mode.
        
                    - **S3BackupDescription** *(dict) --* 
        
                      The configuration for backup in Amazon S3.
        
                      - **RoleARN** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                      - **BucketARN** *(string) --* 
        
                        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                      - **Prefix** *(string) --* 
        
                        The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
                      - **BufferingHints** *(dict) --* 
        
                        The buffering option. If no value is specified, ``BufferingHints`` object default values are used.
        
                        - **SizeInMBs** *(integer) --* 
        
                          Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
                          We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
                        - **IntervalInSeconds** *(integer) --* 
        
                          Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
                      - **CompressionFormat** *(string) --* 
        
                        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
                      - **EncryptionConfiguration** *(dict) --* 
        
                        The encryption configuration. If no value is specified, the default is no encryption.
        
                        - **NoEncryptionConfig** *(string) --* 
        
                          Specifically override existing encryption information to ensure that no encryption is used.
        
                        - **KMSEncryptionConfig** *(dict) --* 
        
                          The encryption key.
        
                          - **AWSKMSKeyARN** *(string) --* 
        
                            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                      - **CloudWatchLoggingOptions** *(dict) --* 
        
                        The Amazon CloudWatch logging options for your delivery stream.
        
                        - **Enabled** *(boolean) --* 
        
                          Enables or disables CloudWatch logging.
        
                        - **LogGroupName** *(string) --* 
        
                          The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
                        - **LogStreamName** *(string) --* 
        
                          The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
                    - **CloudWatchLoggingOptions** *(dict) --* 
        
                      The Amazon CloudWatch logging options for your delivery stream.
        
                      - **Enabled** *(boolean) --* 
        
                        Enables or disables CloudWatch logging.
        
                      - **LogGroupName** *(string) --* 
        
                        The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
                      - **LogStreamName** *(string) --* 
        
                        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
                  - **ElasticsearchDestinationDescription** *(dict) --* 
        
                    The destination in Amazon ES.
        
                    - **RoleARN** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                    - **DomainARN** *(string) --* 
        
                      The ARN of the Amazon ES domain. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                    - **IndexName** *(string) --* 
        
                      The Elasticsearch index name.
        
                    - **TypeName** *(string) --* 
        
                      The Elasticsearch type name.
        
                    - **IndexRotationPeriod** *(string) --* 
        
                      The Elasticsearch index rotation period
        
                    - **BufferingHints** *(dict) --* 
        
                      The buffering options.
        
                      - **IntervalInSeconds** *(integer) --* 
        
                        Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).
        
                      - **SizeInMBs** *(integer) --* 
        
                        Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
                        We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
                    - **RetryOptions** *(dict) --* 
        
                      The Amazon ES retry options.
        
                      - **DurationInSeconds** *(integer) --* 
        
                        After an initial failure to deliver to Amazon ES, the total amount of time during which Kinesis Data Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.
        
                    - **S3BackupMode** *(string) --* 
        
                      The Amazon S3 backup mode.
        
                    - **S3DestinationDescription** *(dict) --* 
        
                      The Amazon S3 destination.
        
                      - **RoleARN** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                      - **BucketARN** *(string) --* 
        
                        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                      - **Prefix** *(string) --* 
        
                        The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
                      - **BufferingHints** *(dict) --* 
        
                        The buffering option. If no value is specified, ``BufferingHints`` object default values are used.
        
                        - **SizeInMBs** *(integer) --* 
        
                          Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
                          We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
                        - **IntervalInSeconds** *(integer) --* 
        
                          Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
                      - **CompressionFormat** *(string) --* 
        
                        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
                      - **EncryptionConfiguration** *(dict) --* 
        
                        The encryption configuration. If no value is specified, the default is no encryption.
        
                        - **NoEncryptionConfig** *(string) --* 
        
                          Specifically override existing encryption information to ensure that no encryption is used.
        
                        - **KMSEncryptionConfig** *(dict) --* 
        
                          The encryption key.
        
                          - **AWSKMSKeyARN** *(string) --* 
        
                            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                      - **CloudWatchLoggingOptions** *(dict) --* 
        
                        The Amazon CloudWatch logging options for your delivery stream.
        
                        - **Enabled** *(boolean) --* 
        
                          Enables or disables CloudWatch logging.
        
                        - **LogGroupName** *(string) --* 
        
                          The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
                        - **LogStreamName** *(string) --* 
        
                          The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
                    - **ProcessingConfiguration** *(dict) --* 
        
                      The data processing configuration.
        
                      - **Enabled** *(boolean) --* 
        
                        Enables or disables data processing.
        
                      - **Processors** *(list) --* 
        
                        The data processors.
        
                        - *(dict) --* 
        
                          Describes a data processor.
        
                          - **Type** *(string) --* 
        
                            The type of processor.
        
                          - **Parameters** *(list) --* 
        
                            The processor parameters.
        
                            - *(dict) --* 
        
                              Describes the processor parameter.
        
                              - **ParameterName** *(string) --* 
        
                                The name of the parameter.
        
                              - **ParameterValue** *(string) --* 
        
                                The parameter value.
        
                    - **CloudWatchLoggingOptions** *(dict) --* 
        
                      The Amazon CloudWatch logging options.
        
                      - **Enabled** *(boolean) --* 
        
                        Enables or disables CloudWatch logging.
        
                      - **LogGroupName** *(string) --* 
        
                        The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
                      - **LogStreamName** *(string) --* 
        
                        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
                  - **SplunkDestinationDescription** *(dict) --* 
        
                    The destination in Splunk.
        
                    - **HECEndpoint** *(string) --* 
        
                      The HTTP Event Collector (HEC) endpoint to which Kinesis Data Firehose sends your data.
        
                    - **HECEndpointType** *(string) --* 
        
                      This type can be either \"Raw\" or \"Event.\"
        
                    - **HECToken** *(string) --* 
        
                      A GUID you obtain from your Splunk cluster when you create a new HEC endpoint.
        
                    - **HECAcknowledgmentTimeoutInSeconds** *(integer) --* 
        
                      The amount of time that Kinesis Data Firehose waits to receive an acknowledgment from Splunk after it sends it data. At the end of the timeout period, Kinesis Data Firehose either tries to send the data again or considers it an error, based on your retry settings.
        
                    - **RetryOptions** *(dict) --* 
        
                      The retry behavior in case Kinesis Data Firehose is unable to deliver data to Splunk or if it doesn\'t receive an acknowledgment of receipt from Splunk.
        
                      - **DurationInSeconds** *(integer) --* 
        
                        The total amount of time that Kinesis Data Firehose spends on retries. This duration starts after the initial attempt to send data to Splunk fails. It doesn\'t include the periods during which Kinesis Data Firehose waits for acknowledgment from Splunk after each attempt.
        
                    - **S3BackupMode** *(string) --* 
        
                      Defines how documents should be delivered to Amazon S3. When set to ``FailedDocumentsOnly`` , Kinesis Data Firehose writes any data that could not be indexed to the configured Amazon S3 destination. When set to ``AllDocuments`` , Kinesis Data Firehose delivers all incoming records to Amazon S3, and also writes failed documents to Amazon S3. Default value is ``FailedDocumentsOnly`` . 
        
                    - **S3DestinationDescription** *(dict) --* 
        
                      The Amazon S3 destination.>
        
                      - **RoleARN** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                      - **BucketARN** *(string) --* 
        
                        The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                      - **Prefix** *(string) --* 
        
                        The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
                      - **BufferingHints** *(dict) --* 
        
                        The buffering option. If no value is specified, ``BufferingHints`` object default values are used.
        
                        - **SizeInMBs** *(integer) --* 
        
                          Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
                          We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
                        - **IntervalInSeconds** *(integer) --* 
        
                          Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
                      - **CompressionFormat** *(string) --* 
        
                        The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
                      - **EncryptionConfiguration** *(dict) --* 
        
                        The encryption configuration. If no value is specified, the default is no encryption.
        
                        - **NoEncryptionConfig** *(string) --* 
        
                          Specifically override existing encryption information to ensure that no encryption is used.
        
                        - **KMSEncryptionConfig** *(dict) --* 
        
                          The encryption key.
        
                          - **AWSKMSKeyARN** *(string) --* 
        
                            The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
                      - **CloudWatchLoggingOptions** *(dict) --* 
        
                        The Amazon CloudWatch logging options for your delivery stream.
        
                        - **Enabled** *(boolean) --* 
        
                          Enables or disables CloudWatch logging.
        
                        - **LogGroupName** *(string) --* 
        
                          The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
                        - **LogStreamName** *(string) --* 
        
                          The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
                    - **ProcessingConfiguration** *(dict) --* 
        
                      The data processing configuration.
        
                      - **Enabled** *(boolean) --* 
        
                        Enables or disables data processing.
        
                      - **Processors** *(list) --* 
        
                        The data processors.
        
                        - *(dict) --* 
        
                          Describes a data processor.
        
                          - **Type** *(string) --* 
        
                            The type of processor.
        
                          - **Parameters** *(list) --* 
        
                            The processor parameters.
        
                            - *(dict) --* 
        
                              Describes the processor parameter.
        
                              - **ParameterName** *(string) --* 
        
                                The name of the parameter.
        
                              - **ParameterValue** *(string) --* 
        
                                The parameter value.
        
                    - **CloudWatchLoggingOptions** *(dict) --* 
        
                      The Amazon CloudWatch logging options for your delivery stream.
        
                      - **Enabled** *(boolean) --* 
        
                        Enables or disables CloudWatch logging.
        
                      - **LogGroupName** *(string) --* 
        
                        The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
                      - **LogStreamName** *(string) --* 
        
                        The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
              - **HasMoreDestinations** *(boolean) --* 
        
                Indicates whether there are more destinations available to list.
        
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
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

    def list_delivery_streams(self, Limit: int = None, DeliveryStreamType: str = None, ExclusiveStartDeliveryStreamName: str = None) -> Dict:
        """
        
        The number of delivery streams might be too large to return using a single call to ``ListDeliveryStreams`` . You can limit the number of delivery streams returned, using the **Limit** parameter. To determine whether there are more delivery streams to list, check the value of ``HasMoreDeliveryStreams`` in the output. If there are more delivery streams to list, you can request them by calling this operation again and setting the ``ExclusiveStartDeliveryStreamName`` parameter to the name of the last delivery stream returned in the last call.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/firehose-2015-08-04/ListDeliveryStreams>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_delivery_streams(
              Limit=123,
              DeliveryStreamType=\'DirectPut\'|\'KinesisStreamAsSource\',
              ExclusiveStartDeliveryStreamName=\'string\'
          )
        :type Limit: integer
        :param Limit: 
        
          The maximum number of delivery streams to list. The default value is 10.
        
        :type DeliveryStreamType: string
        :param DeliveryStreamType: 
        
          The delivery stream type. This can be one of the following values:
        
          * ``DirectPut`` : Provider applications access the delivery stream directly. 
           
          * ``KinesisStreamAsSource`` : The delivery stream uses a Kinesis data stream as a source. 
           
          This parameter is optional. If this parameter is omitted, delivery streams of all types are returned.
        
        :type ExclusiveStartDeliveryStreamName: string
        :param ExclusiveStartDeliveryStreamName: 
        
          The list of delivery streams returned by this call to ``ListDeliveryStreams`` will start with the delivery stream whose name comes alphabetically immediately after the name you specify in ``ExclusiveStartDeliveryStreamName`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeliveryStreamNames\': [
                    \'string\',
                ],
                \'HasMoreDeliveryStreams\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DeliveryStreamNames** *(list) --* 
        
              The names of the delivery streams.
        
              - *(string) --* 
          
            - **HasMoreDeliveryStreams** *(boolean) --* 
        
              Indicates whether there are more delivery streams available to list.
        
        """
        pass

    def list_tags_for_delivery_stream(self, DeliveryStreamName: str, ExclusiveStartTagKey: str = None, Limit: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/firehose-2015-08-04/ListTagsForDeliveryStream>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags_for_delivery_stream(
              DeliveryStreamName=\'string\',
              ExclusiveStartTagKey=\'string\',
              Limit=123
          )
        :type DeliveryStreamName: string
        :param DeliveryStreamName: **[REQUIRED]** 
        
          The name of the delivery stream whose tags you want to list.
        
        :type ExclusiveStartTagKey: string
        :param ExclusiveStartTagKey: 
        
          The key to use as the starting point for the list of tags. If you set this parameter, ``ListTagsForDeliveryStream`` gets all tags that occur after ``ExclusiveStartTagKey`` .
        
        :type Limit: integer
        :param Limit: 
        
          The number of tags to return. If this number is less than the total number of tags associated with the delivery stream, ``HasMoreTags`` is set to ``true`` in the response. To list additional tags, set ``ExclusiveStartTagKey`` to the last key in the response. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Tags\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ],
                \'HasMoreTags\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Tags** *(list) --* 
        
              A list of tags associated with ``DeliveryStreamName`` , starting with the first tag after ``ExclusiveStartTagKey`` and up to the specified ``Limit`` .
        
              - *(dict) --* 
        
                Metadata that you can assign to a delivery stream, consisting of a key-value pair.
        
                - **Key** *(string) --* 
        
                  A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @
        
                - **Value** *(string) --* 
        
                  An optional string, which you can use to describe or define the tag. Maximum length: 256 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @
        
            - **HasMoreTags** *(boolean) --* 
        
              If this is ``true`` in the response, more tags are available. To list the remaining tags, set ``ExclusiveStartTagKey`` to the key of the last tag returned and call ``ListTagsForDeliveryStream`` again.
        
        """
        pass

    def put_record(self, DeliveryStreamName: str, Record: Dict) -> Dict:
        """
        
        By default, each delivery stream can take in up to 2,000 transactions per second, 5,000 records per second, or 5 MB per second. If you use  PutRecord and  PutRecordBatch , the limits are an aggregate across these two operations for each delivery stream. For more information about limits and how to request an increase, see `Amazon Kinesis Data Firehose Limits <http://docs.aws.amazon.com/firehose/latest/dev/limits.html>`__ . 
        
        You must specify the name of the delivery stream and the data record when using  PutRecord . The data record consists of a data blob that can be up to 1,000 KB in size, and any kind of data. For example, it can be a segment from a log file, geographic location data, website clickstream data, and so on.
        
        Kinesis Data Firehose buffers records before delivering them to the destination. To disambiguate the data blobs at the destination, a common solution is to use delimiters in the data, such as a newline (``\n`` ) or some other character unique within the data. This allows the consumer application to parse individual data items when reading the data from the destination.
        
        The ``PutRecord`` operation returns a ``RecordId`` , which is a unique string assigned to each record. Producer applications can use this ID for purposes such as auditability and investigation.
        
        If the ``PutRecord`` operation throws a ``ServiceUnavailableException`` , back off and retry. If the exception persists, it is possible that the throughput limits have been exceeded for the delivery stream. 
        
        Data records sent to Kinesis Data Firehose are stored for 24 hours from the time they are added to a delivery stream as it tries to send the records to the destination. If the destination is unreachable for more than 24 hours, the data is no longer available.
        
        .. warning::
        
          Don\'t concatenate two or more base64 strings to form the data fields of your records. Instead, concatenate the raw data, then perform base64 encoding.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/firehose-2015-08-04/PutRecord>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_record(
              DeliveryStreamName=\'string\',
              Record={
                  \'Data\': b\'bytes\'
              }
          )
        :type DeliveryStreamName: string
        :param DeliveryStreamName: **[REQUIRED]** 
        
          The name of the delivery stream.
        
        :type Record: dict
        :param Record: **[REQUIRED]** 
        
          The record.
        
          - **Data** *(bytes) --* **[REQUIRED]** 
        
            The data blob, which is base64-encoded when the blob is serialized. The maximum size of the data blob, before base64-encoding, is 1,000 KiB.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RecordId\': \'string\',
                \'Encrypted\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **RecordId** *(string) --* 
        
              The ID of the record.
        
            - **Encrypted** *(boolean) --* 
        
              Indicates whether server-side encryption (SSE) was enabled during this operation.
        
        """
        pass

    def put_record_batch(self, DeliveryStreamName: str, Records: List) -> Dict:
        """
        
        By default, each delivery stream can take in up to 2,000 transactions per second, 5,000 records per second, or 5 MB per second. If you use  PutRecord and  PutRecordBatch , the limits are an aggregate across these two operations for each delivery stream. For more information about limits, see `Amazon Kinesis Data Firehose Limits <http://docs.aws.amazon.com/firehose/latest/dev/limits.html>`__ .
        
        Each  PutRecordBatch request supports up to 500 records. Each record in the request can be as large as 1,000 KB (before 64-bit encoding), up to a limit of 4 MB for the entire request. These limits cannot be changed.
        
        You must specify the name of the delivery stream and the data record when using  PutRecord . The data record consists of a data blob that can be up to 1,000 KB in size, and any kind of data. For example, it could be a segment from a log file, geographic location data, website clickstream data, and so on.
        
        Kinesis Data Firehose buffers records before delivering them to the destination. To disambiguate the data blobs at the destination, a common solution is to use delimiters in the data, such as a newline (``\n`` ) or some other character unique within the data. This allows the consumer application to parse individual data items when reading the data from the destination.
        
        The  PutRecordBatch response includes a count of failed records, **FailedPutCount** , and an array of responses, **RequestResponses** . Even if the  PutRecordBatch call succeeds, the value of **FailedPutCount** may be greater than 0, indicating that there are records for which the operation didn\'t succeed. Each entry in the **RequestResponses** array provides additional information about the processed record. It directly correlates with a record in the request array using the same ordering, from the top to the bottom. The response array always includes the same number of records as the request array. **RequestResponses** includes both successfully and unsuccessfully processed records. Kinesis Data Firehose tries to process all records in each  PutRecordBatch request. A single record failure does not stop the processing of subsequent records. 
        
        A successfully processed record includes a **RecordId** value, which is unique for the record. An unsuccessfully processed record includes **ErrorCode** and **ErrorMessage** values. **ErrorCode** reflects the type of error, and is one of the following values: ``ServiceUnavailableException`` or ``InternalFailure`` . **ErrorMessage** provides more detailed information about the error.
        
        If there is an internal server error or a timeout, the write might have completed or it might have failed. If **FailedPutCount** is greater than 0, retry the request, resending only those records that might have failed processing. This minimizes the possible duplicate records and also reduces the total bytes sent (and corresponding charges). We recommend that you handle any duplicates at the destination.
        
        If  PutRecordBatch throws **ServiceUnavailableException** , back off and retry. If the exception persists, it is possible that the throughput limits have been exceeded for the delivery stream.
        
        Data records sent to Kinesis Data Firehose are stored for 24 hours from the time they are added to a delivery stream as it attempts to send the records to the destination. If the destination is unreachable for more than 24 hours, the data is no longer available.
        
        .. warning::
        
          Don\'t concatenate two or more base64 strings to form the data fields of your records. Instead, concatenate the raw data, then perform base64 encoding.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/firehose-2015-08-04/PutRecordBatch>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_record_batch(
              DeliveryStreamName=\'string\',
              Records=[
                  {
                      \'Data\': b\'bytes\'
                  },
              ]
          )
        :type DeliveryStreamName: string
        :param DeliveryStreamName: **[REQUIRED]** 
        
          The name of the delivery stream.
        
        :type Records: list
        :param Records: **[REQUIRED]** 
        
          One or more records.
        
          - *(dict) --* 
        
            The unit of data in a delivery stream.
        
            - **Data** *(bytes) --* **[REQUIRED]** 
        
              The data blob, which is base64-encoded when the blob is serialized. The maximum size of the data blob, before base64-encoding, is 1,000 KiB.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FailedPutCount\': 123,
                \'Encrypted\': True|False,
                \'RequestResponses\': [
                    {
                        \'RecordId\': \'string\',
                        \'ErrorCode\': \'string\',
                        \'ErrorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **FailedPutCount** *(integer) --* 
        
              The number of records that might have failed processing. This number might be greater than 0 even if the  PutRecordBatch call succeeds. Check ``FailedPutCount`` to determine whether there are records that you need to resend.
        
            - **Encrypted** *(boolean) --* 
        
              Indicates whether server-side encryption (SSE) was enabled during this operation.
        
            - **RequestResponses** *(list) --* 
        
              The results array. For each record, the index of the response element is the same as the index used in the request array.
        
              - *(dict) --* 
        
                Contains the result for an individual record from a  PutRecordBatch request. If the record is successfully added to your delivery stream, it receives a record ID. If the record fails to be added to your delivery stream, the result includes an error code and an error message.
        
                - **RecordId** *(string) --* 
        
                  The ID of the record.
        
                - **ErrorCode** *(string) --* 
        
                  The error code for an individual record result.
        
                - **ErrorMessage** *(string) --* 
        
                  The error message for an individual record result.
        
        """
        pass

    def start_delivery_stream_encryption(self, DeliveryStreamName: str) -> Dict:
        """
        
        To check the encryption state of a delivery stream, use  DescribeDeliveryStream . 
        
        You can only enable SSE for a delivery stream that uses ``DirectPut`` as its source. 
        
        The ``StartDeliveryStreamEncryption`` and ``StopDeliveryStreamEncryption`` operations have a combined limit of 25 calls per delivery stream per 24 hours. For example, you reach the limit if you call ``StartDeliveryStreamEncryption`` thirteen times and ``StopDeliveryStreamEncryption`` twelve times for the same stream in a 24-hour period.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/firehose-2015-08-04/StartDeliveryStreamEncryption>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_delivery_stream_encryption(
              DeliveryStreamName=\'string\'
          )
        :type DeliveryStreamName: string
        :param DeliveryStreamName: **[REQUIRED]** 
        
          The name of the delivery stream for which you want to enable server-side encryption (SSE).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def stop_delivery_stream_encryption(self, DeliveryStreamName: str) -> Dict:
        """
        
        To check the encryption state of a delivery stream, use  DescribeDeliveryStream . 
        
        The ``StartDeliveryStreamEncryption`` and ``StopDeliveryStreamEncryption`` operations have a combined limit of 25 calls per delivery stream per 24 hours. For example, you reach the limit if you call ``StartDeliveryStreamEncryption`` thirteen times and ``StopDeliveryStreamEncryption`` twelve times for the same stream in a 24-hour period.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/firehose-2015-08-04/StopDeliveryStreamEncryption>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_delivery_stream_encryption(
              DeliveryStreamName=\'string\'
          )
        :type DeliveryStreamName: string
        :param DeliveryStreamName: **[REQUIRED]** 
        
          The name of the delivery stream for which you want to disable server-side encryption (SSE).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def tag_delivery_stream(self, DeliveryStreamName: str, Tags: List) -> Dict:
        """
        
        Each delivery stream can have up to 50 tags. 
        
        This operation has a limit of five transactions per second per account. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/firehose-2015-08-04/TagDeliveryStream>`_
        
        **Request Syntax** 
        ::
        
          response = client.tag_delivery_stream(
              DeliveryStreamName=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DeliveryStreamName: string
        :param DeliveryStreamName: **[REQUIRED]** 
        
          The name of the delivery stream to which you want to add the tags.
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          A set of key-value pairs to use to create the tags.
        
          - *(dict) --* 
        
            Metadata that you can assign to a delivery stream, consisting of a key-value pair.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @
        
            - **Value** *(string) --* 
        
              An optional string, which you can use to describe or define the tag. Maximum length: 256 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def untag_delivery_stream(self, DeliveryStreamName: str, TagKeys: List) -> Dict:
        """
        
        If you specify a tag that doesn\'t exist, the operation ignores it.
        
        This operation has a limit of five transactions per second per account. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/firehose-2015-08-04/UntagDeliveryStream>`_
        
        **Request Syntax** 
        ::
        
          response = client.untag_delivery_stream(
              DeliveryStreamName=\'string\',
              TagKeys=[
                  \'string\',
              ]
          )
        :type DeliveryStreamName: string
        :param DeliveryStreamName: **[REQUIRED]** 
        
          The name of the delivery stream.
        
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** 
        
          A list of tag keys. Each corresponding tag is removed from the delivery stream.
        
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

    def update_destination(self, DeliveryStreamName: str, CurrentDeliveryStreamVersionId: str, DestinationId: str, S3DestinationUpdate: Dict = None, ExtendedS3DestinationUpdate: Dict = None, RedshiftDestinationUpdate: Dict = None, ElasticsearchDestinationUpdate: Dict = None, SplunkDestinationUpdate: Dict = None) -> Dict:
        """
        
        Use this operation to change the destination type (for example, to replace the Amazon S3 destination with Amazon Redshift) or change the parameters associated with a destination (for example, to change the bucket name of the Amazon S3 destination). The update might not occur immediately. The target delivery stream remains active while the configurations are updated, so data writes to the delivery stream can continue during this process. The updated configurations are usually effective within a few minutes.
        
        Switching between Amazon ES and other services is not supported. For an Amazon ES destination, you can only update to another Amazon ES destination.
        
        If the destination type is the same, Kinesis Data Firehose merges the configuration parameters specified with the destination configuration that already exists on the delivery stream. If any of the parameters are not specified in the call, the existing values are retained. For example, in the Amazon S3 destination, if  EncryptionConfiguration is not specified, then the existing ``EncryptionConfiguration`` is maintained on the destination.
        
        If the destination type is not the same, for example, changing the destination from Amazon S3 to Amazon Redshift, Kinesis Data Firehose does not merge any parameters. In this case, all parameters must be specified.
        
        Kinesis Data Firehose uses **CurrentDeliveryStreamVersionId** to avoid race conditions and conflicting merges. This is a required field, and the service updates the configuration only if the existing configuration has a version ID that matches. After the update is applied successfully, the version ID is updated, and can be retrieved using  DescribeDeliveryStream . Use the new version ID to set **CurrentDeliveryStreamVersionId** in the next call.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/firehose-2015-08-04/UpdateDestination>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_destination(
              DeliveryStreamName=\'string\',
              CurrentDeliveryStreamVersionId=\'string\',
              DestinationId=\'string\',
              S3DestinationUpdate={
                  \'RoleARN\': \'string\',
                  \'BucketARN\': \'string\',
                  \'Prefix\': \'string\',
                  \'BufferingHints\': {
                      \'SizeInMBs\': 123,
                      \'IntervalInSeconds\': 123
                  },
                  \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                  \'EncryptionConfiguration\': {
                      \'NoEncryptionConfig\': \'NoEncryption\',
                      \'KMSEncryptionConfig\': {
                          \'AWSKMSKeyARN\': \'string\'
                      }
                  },
                  \'CloudWatchLoggingOptions\': {
                      \'Enabled\': True|False,
                      \'LogGroupName\': \'string\',
                      \'LogStreamName\': \'string\'
                  }
              },
              ExtendedS3DestinationUpdate={
                  \'RoleARN\': \'string\',
                  \'BucketARN\': \'string\',
                  \'Prefix\': \'string\',
                  \'BufferingHints\': {
                      \'SizeInMBs\': 123,
                      \'IntervalInSeconds\': 123
                  },
                  \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                  \'EncryptionConfiguration\': {
                      \'NoEncryptionConfig\': \'NoEncryption\',
                      \'KMSEncryptionConfig\': {
                          \'AWSKMSKeyARN\': \'string\'
                      }
                  },
                  \'CloudWatchLoggingOptions\': {
                      \'Enabled\': True|False,
                      \'LogGroupName\': \'string\',
                      \'LogStreamName\': \'string\'
                  },
                  \'ProcessingConfiguration\': {
                      \'Enabled\': True|False,
                      \'Processors\': [
                          {
                              \'Type\': \'Lambda\',
                              \'Parameters\': [
                                  {
                                      \'ParameterName\': \'LambdaArn\'|\'NumberOfRetries\'|\'RoleArn\'|\'BufferSizeInMBs\'|\'BufferIntervalInSeconds\',
                                      \'ParameterValue\': \'string\'
                                  },
                              ]
                          },
                      ]
                  },
                  \'S3BackupMode\': \'Disabled\'|\'Enabled\',
                  \'S3BackupUpdate\': {
                      \'RoleARN\': \'string\',
                      \'BucketARN\': \'string\',
                      \'Prefix\': \'string\',
                      \'BufferingHints\': {
                          \'SizeInMBs\': 123,
                          \'IntervalInSeconds\': 123
                      },
                      \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                      \'EncryptionConfiguration\': {
                          \'NoEncryptionConfig\': \'NoEncryption\',
                          \'KMSEncryptionConfig\': {
                              \'AWSKMSKeyARN\': \'string\'
                          }
                      },
                      \'CloudWatchLoggingOptions\': {
                          \'Enabled\': True|False,
                          \'LogGroupName\': \'string\',
                          \'LogStreamName\': \'string\'
                      }
                  },
                  \'DataFormatConversionConfiguration\': {
                      \'SchemaConfiguration\': {
                          \'RoleARN\': \'string\',
                          \'CatalogId\': \'string\',
                          \'DatabaseName\': \'string\',
                          \'TableName\': \'string\',
                          \'Region\': \'string\',
                          \'VersionId\': \'string\'
                      },
                      \'InputFormatConfiguration\': {
                          \'Deserializer\': {
                              \'OpenXJsonSerDe\': {
                                  \'ConvertDotsInJsonKeysToUnderscores\': True|False,
                                  \'CaseInsensitive\': True|False,
                                  \'ColumnToJsonKeyMappings\': {
                                      \'string\': \'string\'
                                  }
                              },
                              \'HiveJsonSerDe\': {
                                  \'TimestampFormats\': [
                                      \'string\',
                                  ]
                              }
                          }
                      },
                      \'OutputFormatConfiguration\': {
                          \'Serializer\': {
                              \'ParquetSerDe\': {
                                  \'BlockSizeBytes\': 123,
                                  \'PageSizeBytes\': 123,
                                  \'Compression\': \'UNCOMPRESSED\'|\'GZIP\'|\'SNAPPY\',
                                  \'EnableDictionaryCompression\': True|False,
                                  \'MaxPaddingBytes\': 123,
                                  \'WriterVersion\': \'V1\'|\'V2\'
                              },
                              \'OrcSerDe\': {
                                  \'StripeSizeBytes\': 123,
                                  \'BlockSizeBytes\': 123,
                                  \'RowIndexStride\': 123,
                                  \'EnablePadding\': True|False,
                                  \'PaddingTolerance\': 123.0,
                                  \'Compression\': \'NONE\'|\'ZLIB\'|\'SNAPPY\',
                                  \'BloomFilterColumns\': [
                                      \'string\',
                                  ],
                                  \'BloomFilterFalsePositiveProbability\': 123.0,
                                  \'DictionaryKeyThreshold\': 123.0,
                                  \'FormatVersion\': \'V0_11\'|\'V0_12\'
                              }
                          }
                      },
                      \'Enabled\': True|False
                  }
              },
              RedshiftDestinationUpdate={
                  \'RoleARN\': \'string\',
                  \'ClusterJDBCURL\': \'string\',
                  \'CopyCommand\': {
                      \'DataTableName\': \'string\',
                      \'DataTableColumns\': \'string\',
                      \'CopyOptions\': \'string\'
                  },
                  \'Username\': \'string\',
                  \'Password\': \'string\',
                  \'RetryOptions\': {
                      \'DurationInSeconds\': 123
                  },
                  \'S3Update\': {
                      \'RoleARN\': \'string\',
                      \'BucketARN\': \'string\',
                      \'Prefix\': \'string\',
                      \'BufferingHints\': {
                          \'SizeInMBs\': 123,
                          \'IntervalInSeconds\': 123
                      },
                      \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                      \'EncryptionConfiguration\': {
                          \'NoEncryptionConfig\': \'NoEncryption\',
                          \'KMSEncryptionConfig\': {
                              \'AWSKMSKeyARN\': \'string\'
                          }
                      },
                      \'CloudWatchLoggingOptions\': {
                          \'Enabled\': True|False,
                          \'LogGroupName\': \'string\',
                          \'LogStreamName\': \'string\'
                      }
                  },
                  \'ProcessingConfiguration\': {
                      \'Enabled\': True|False,
                      \'Processors\': [
                          {
                              \'Type\': \'Lambda\',
                              \'Parameters\': [
                                  {
                                      \'ParameterName\': \'LambdaArn\'|\'NumberOfRetries\'|\'RoleArn\'|\'BufferSizeInMBs\'|\'BufferIntervalInSeconds\',
                                      \'ParameterValue\': \'string\'
                                  },
                              ]
                          },
                      ]
                  },
                  \'S3BackupMode\': \'Disabled\'|\'Enabled\',
                  \'S3BackupUpdate\': {
                      \'RoleARN\': \'string\',
                      \'BucketARN\': \'string\',
                      \'Prefix\': \'string\',
                      \'BufferingHints\': {
                          \'SizeInMBs\': 123,
                          \'IntervalInSeconds\': 123
                      },
                      \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                      \'EncryptionConfiguration\': {
                          \'NoEncryptionConfig\': \'NoEncryption\',
                          \'KMSEncryptionConfig\': {
                              \'AWSKMSKeyARN\': \'string\'
                          }
                      },
                      \'CloudWatchLoggingOptions\': {
                          \'Enabled\': True|False,
                          \'LogGroupName\': \'string\',
                          \'LogStreamName\': \'string\'
                      }
                  },
                  \'CloudWatchLoggingOptions\': {
                      \'Enabled\': True|False,
                      \'LogGroupName\': \'string\',
                      \'LogStreamName\': \'string\'
                  }
              },
              ElasticsearchDestinationUpdate={
                  \'RoleARN\': \'string\',
                  \'DomainARN\': \'string\',
                  \'IndexName\': \'string\',
                  \'TypeName\': \'string\',
                  \'IndexRotationPeriod\': \'NoRotation\'|\'OneHour\'|\'OneDay\'|\'OneWeek\'|\'OneMonth\',
                  \'BufferingHints\': {
                      \'IntervalInSeconds\': 123,
                      \'SizeInMBs\': 123
                  },
                  \'RetryOptions\': {
                      \'DurationInSeconds\': 123
                  },
                  \'S3Update\': {
                      \'RoleARN\': \'string\',
                      \'BucketARN\': \'string\',
                      \'Prefix\': \'string\',
                      \'BufferingHints\': {
                          \'SizeInMBs\': 123,
                          \'IntervalInSeconds\': 123
                      },
                      \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                      \'EncryptionConfiguration\': {
                          \'NoEncryptionConfig\': \'NoEncryption\',
                          \'KMSEncryptionConfig\': {
                              \'AWSKMSKeyARN\': \'string\'
                          }
                      },
                      \'CloudWatchLoggingOptions\': {
                          \'Enabled\': True|False,
                          \'LogGroupName\': \'string\',
                          \'LogStreamName\': \'string\'
                      }
                  },
                  \'ProcessingConfiguration\': {
                      \'Enabled\': True|False,
                      \'Processors\': [
                          {
                              \'Type\': \'Lambda\',
                              \'Parameters\': [
                                  {
                                      \'ParameterName\': \'LambdaArn\'|\'NumberOfRetries\'|\'RoleArn\'|\'BufferSizeInMBs\'|\'BufferIntervalInSeconds\',
                                      \'ParameterValue\': \'string\'
                                  },
                              ]
                          },
                      ]
                  },
                  \'CloudWatchLoggingOptions\': {
                      \'Enabled\': True|False,
                      \'LogGroupName\': \'string\',
                      \'LogStreamName\': \'string\'
                  }
              },
              SplunkDestinationUpdate={
                  \'HECEndpoint\': \'string\',
                  \'HECEndpointType\': \'Raw\'|\'Event\',
                  \'HECToken\': \'string\',
                  \'HECAcknowledgmentTimeoutInSeconds\': 123,
                  \'RetryOptions\': {
                      \'DurationInSeconds\': 123
                  },
                  \'S3BackupMode\': \'FailedEventsOnly\'|\'AllEvents\',
                  \'S3Update\': {
                      \'RoleARN\': \'string\',
                      \'BucketARN\': \'string\',
                      \'Prefix\': \'string\',
                      \'BufferingHints\': {
                          \'SizeInMBs\': 123,
                          \'IntervalInSeconds\': 123
                      },
                      \'CompressionFormat\': \'UNCOMPRESSED\'|\'GZIP\'|\'ZIP\'|\'Snappy\',
                      \'EncryptionConfiguration\': {
                          \'NoEncryptionConfig\': \'NoEncryption\',
                          \'KMSEncryptionConfig\': {
                              \'AWSKMSKeyARN\': \'string\'
                          }
                      },
                      \'CloudWatchLoggingOptions\': {
                          \'Enabled\': True|False,
                          \'LogGroupName\': \'string\',
                          \'LogStreamName\': \'string\'
                      }
                  },
                  \'ProcessingConfiguration\': {
                      \'Enabled\': True|False,
                      \'Processors\': [
                          {
                              \'Type\': \'Lambda\',
                              \'Parameters\': [
                                  {
                                      \'ParameterName\': \'LambdaArn\'|\'NumberOfRetries\'|\'RoleArn\'|\'BufferSizeInMBs\'|\'BufferIntervalInSeconds\',
                                      \'ParameterValue\': \'string\'
                                  },
                              ]
                          },
                      ]
                  },
                  \'CloudWatchLoggingOptions\': {
                      \'Enabled\': True|False,
                      \'LogGroupName\': \'string\',
                      \'LogStreamName\': \'string\'
                  }
              }
          )
        :type DeliveryStreamName: string
        :param DeliveryStreamName: **[REQUIRED]** 
        
          The name of the delivery stream.
        
        :type CurrentDeliveryStreamVersionId: string
        :param CurrentDeliveryStreamVersionId: **[REQUIRED]** 
        
          Obtain this value from the **VersionId** result of  DeliveryStreamDescription . This value is required, and helps the service perform conditional operations. For example, if there is an interleaving update and this value is null, then the update destination fails. After the update is successful, the ``VersionId`` value is updated. The service then performs a merge of the old configuration with the new configuration.
        
        :type DestinationId: string
        :param DestinationId: **[REQUIRED]** 
        
          The ID of the destination.
        
        :type S3DestinationUpdate: dict
        :param S3DestinationUpdate: 
        
          [Deprecated] Describes an update for a destination in Amazon S3.
        
          - **RoleARN** *(string) --* 
        
            The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
          - **BucketARN** *(string) --* 
        
            The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
          - **Prefix** *(string) --* 
        
            The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
          - **BufferingHints** *(dict) --* 
        
            The buffering option. If no value is specified, ``BufferingHints`` object default values are used.
        
            - **SizeInMBs** *(integer) --* 
        
              Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
              We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
            - **IntervalInSeconds** *(integer) --* 
        
              Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
          - **CompressionFormat** *(string) --* 
        
            The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
            The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift ``COPY`` operation that reads from the S3 bucket.
        
          - **EncryptionConfiguration** *(dict) --* 
        
            The encryption configuration. If no value is specified, the default is no encryption.
        
            - **NoEncryptionConfig** *(string) --* 
        
              Specifically override existing encryption information to ensure that no encryption is used.
        
            - **KMSEncryptionConfig** *(dict) --* 
        
              The encryption key.
        
              - **AWSKMSKeyARN** *(string) --* **[REQUIRED]** 
        
                The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
          - **CloudWatchLoggingOptions** *(dict) --* 
        
            The CloudWatch logging options for your delivery stream.
        
            - **Enabled** *(boolean) --* 
        
              Enables or disables CloudWatch logging.
        
            - **LogGroupName** *(string) --* 
        
              The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
            - **LogStreamName** *(string) --* 
        
              The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
        :type ExtendedS3DestinationUpdate: dict
        :param ExtendedS3DestinationUpdate: 
        
          Describes an update for a destination in Amazon S3.
        
          - **RoleARN** *(string) --* 
        
            The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
          - **BucketARN** *(string) --* 
        
            The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
          - **Prefix** *(string) --* 
        
            The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
          - **BufferingHints** *(dict) --* 
        
            The buffering option.
        
            - **SizeInMBs** *(integer) --* 
        
              Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
              We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
            - **IntervalInSeconds** *(integer) --* 
        
              Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
          - **CompressionFormat** *(string) --* 
        
            The compression format. If no value is specified, the default is ``UNCOMPRESSED`` . 
        
          - **EncryptionConfiguration** *(dict) --* 
        
            The encryption configuration. If no value is specified, the default is no encryption.
        
            - **NoEncryptionConfig** *(string) --* 
        
              Specifically override existing encryption information to ensure that no encryption is used.
        
            - **KMSEncryptionConfig** *(dict) --* 
        
              The encryption key.
        
              - **AWSKMSKeyARN** *(string) --* **[REQUIRED]** 
        
                The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
          - **CloudWatchLoggingOptions** *(dict) --* 
        
            The Amazon CloudWatch logging options for your delivery stream.
        
            - **Enabled** *(boolean) --* 
        
              Enables or disables CloudWatch logging.
        
            - **LogGroupName** *(string) --* 
        
              The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
            - **LogStreamName** *(string) --* 
        
              The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
          - **ProcessingConfiguration** *(dict) --* 
        
            The data processing configuration.
        
            - **Enabled** *(boolean) --* 
        
              Enables or disables data processing.
        
            - **Processors** *(list) --* 
        
              The data processors.
        
              - *(dict) --* 
        
                Describes a data processor.
        
                - **Type** *(string) --* **[REQUIRED]** 
        
                  The type of processor.
        
                - **Parameters** *(list) --* 
        
                  The processor parameters.
        
                  - *(dict) --* 
        
                    Describes the processor parameter.
        
                    - **ParameterName** *(string) --* **[REQUIRED]** 
        
                      The name of the parameter.
        
                    - **ParameterValue** *(string) --* **[REQUIRED]** 
        
                      The parameter value.
        
          - **S3BackupMode** *(string) --* 
        
            Enables or disables Amazon S3 backup mode.
        
          - **S3BackupUpdate** *(dict) --* 
        
            The Amazon S3 destination for backup.
        
            - **RoleARN** *(string) --* 
        
              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **BucketARN** *(string) --* 
        
              The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **Prefix** *(string) --* 
        
              The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
            - **BufferingHints** *(dict) --* 
        
              The buffering option. If no value is specified, ``BufferingHints`` object default values are used.
        
              - **SizeInMBs** *(integer) --* 
        
                Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
                We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
              - **IntervalInSeconds** *(integer) --* 
        
                Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
            - **CompressionFormat** *(string) --* 
        
              The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
              The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift ``COPY`` operation that reads from the S3 bucket.
        
            - **EncryptionConfiguration** *(dict) --* 
        
              The encryption configuration. If no value is specified, the default is no encryption.
        
              - **NoEncryptionConfig** *(string) --* 
        
                Specifically override existing encryption information to ensure that no encryption is used.
        
              - **KMSEncryptionConfig** *(dict) --* 
        
                The encryption key.
        
                - **AWSKMSKeyARN** *(string) --* **[REQUIRED]** 
        
                  The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **CloudWatchLoggingOptions** *(dict) --* 
        
              The CloudWatch logging options for your delivery stream.
        
              - **Enabled** *(boolean) --* 
        
                Enables or disables CloudWatch logging.
        
              - **LogGroupName** *(string) --* 
        
                The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
              - **LogStreamName** *(string) --* 
        
                The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
          - **DataFormatConversionConfiguration** *(dict) --* 
        
            The serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3.
        
            - **SchemaConfiguration** *(dict) --* 
        
              Specifies the AWS Glue Data Catalog table that contains the column information.
        
              - **RoleARN** *(string) --* 
        
                The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren\'t allowed.
        
              - **CatalogId** *(string) --* 
        
                The ID of the AWS Glue Data Catalog. If you don\'t supply this, the AWS account ID is used by default.
        
              - **DatabaseName** *(string) --* 
        
                Specifies the name of the AWS Glue database that contains the schema for the output data.
        
              - **TableName** *(string) --* 
        
                Specifies the AWS Glue table that contains the column information that constitutes your data schema.
        
              - **Region** *(string) --* 
        
                If you don\'t specify an AWS Region, the default is the current Region.
        
              - **VersionId** *(string) --* 
        
                Specifies the table version for the output data schema. If you don\'t specify this version ID, or if you set it to ``LATEST`` , Kinesis Data Firehose uses the most recent version. This means that any updates to the table are automatically picked up.
        
            - **InputFormatConfiguration** *(dict) --* 
        
              Specifies the deserializer that you want Kinesis Data Firehose to use to convert the format of your data from JSON.
        
              - **Deserializer** *(dict) --* 
        
                Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the request.
        
                - **OpenXJsonSerDe** *(dict) --* 
        
                  The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.
        
                  - **ConvertDotsInJsonKeysToUnderscores** *(boolean) --* 
        
                    When set to ``true`` , specifies that the names of the keys include dots and that you want Kinesis Data Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is \"a.b\", you can define the column name to be \"a_b\" when using this option.
        
                    The default is ``false`` .
        
                  - **CaseInsensitive** *(boolean) --* 
        
                    When set to ``true`` , which is the default, Kinesis Data Firehose converts JSON keys to lowercase before deserializing them.
        
                  - **ColumnToJsonKeyMappings** *(dict) --* 
        
                    Maps column names to JSON keys that aren\'t identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, ``timestamp`` is a Hive keyword. If you have a JSON key named ``timestamp`` , set this parameter to ``{\"ts\": \"timestamp\"}`` to map this key to a column named ``ts`` .
        
                    - *(string) --* 
        
                      - *(string) --* 
        
                - **HiveJsonSerDe** *(dict) --* 
        
                  The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.
        
                  - **TimestampFormats** *(list) --* 
        
                    Indicates how you want Kinesis Data Firehose to parse the date and time stamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime\'s DateTimeFormat format strings. For more information, see `Class DateTimeFormat <https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`__ . You can also use the special value ``millis`` to parse time stamps in epoch milliseconds. If you don\'t specify a format, Kinesis Data Firehose uses ``java.sql.Timestamp::valueOf`` by default.
        
                    - *(string) --* 
        
            - **OutputFormatConfiguration** *(dict) --* 
        
              Specifies the serializer that you want Kinesis Data Firehose to use to convert the format of your data to the Parquet or ORC format.
        
              - **Serializer** *(dict) --* 
        
                Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. If both are non-null, the server rejects the request.
        
                - **ParquetSerDe** *(dict) --* 
        
                  A serializer to use for converting data to the Parquet format before storing it in Amazon S3. For more information, see `Apache Parquet <https://parquet.apache.org/documentation/latest/>`__ .
        
                  - **BlockSizeBytes** *(integer) --* 
        
                    The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.
        
                  - **PageSizeBytes** *(integer) --* 
        
                    The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.
        
                  - **Compression** *(string) --* 
        
                    The compression code to use over data blocks. The possible values are ``UNCOMPRESSED`` , ``SNAPPY`` , and ``GZIP`` , with the default being ``SNAPPY`` . Use ``SNAPPY`` for higher decompression speed. Use ``GZIP`` if the compression ration is more important than speed.
        
                  - **EnableDictionaryCompression** *(boolean) --* 
        
                    Indicates whether to enable dictionary compression.
        
                  - **MaxPaddingBytes** *(integer) --* 
        
                    The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 0.
        
                  - **WriterVersion** *(string) --* 
        
                    Indicates the version of row format to output. The possible values are ``V1`` and ``V2`` . The default is ``V1`` .
        
                - **OrcSerDe** *(dict) --* 
        
                  A serializer to use for converting data to the ORC format before storing it in Amazon S3. For more information, see `Apache ORC <https://orc.apache.org/docs/>`__ .
        
                  - **StripeSizeBytes** *(integer) --* 
        
                    The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.
        
                  - **BlockSizeBytes** *(integer) --* 
        
                    The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.
        
                  - **RowIndexStride** *(integer) --* 
        
                    The number of rows between index entries. The default is 10,000 and the minimum is 1,000.
        
                  - **EnablePadding** *(boolean) --* 
        
                    Set this to ``true`` to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is ``false`` .
        
                  - **PaddingTolerance** *(float) --* 
        
                    A number between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is 0.05, which means 5 percent of stripe size.
        
                    For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task.
        
                    Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is ``false`` .
        
                  - **Compression** *(string) --* 
        
                    The compression code to use over data blocks. The default is ``SNAPPY`` .
        
                  - **BloomFilterColumns** *(list) --* 
        
                    The column names for which you want Kinesis Data Firehose to create bloom filters. The default is ``null`` .
        
                    - *(string) --* 
        
                  - **BloomFilterFalsePositiveProbability** *(float) --* 
        
                    The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.
        
                  - **DictionaryKeyThreshold** *(float) --* 
        
                    Represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to 1.
        
                  - **FormatVersion** *(string) --* 
        
                    The version of the file to write. The possible values are ``V0_11`` and ``V0_12`` . The default is ``V0_12`` .
        
            - **Enabled** *(boolean) --* 
        
              Defaults to ``true`` . Set it to ``false`` if you want to disable format conversion while preserving the configuration details.
        
        :type RedshiftDestinationUpdate: dict
        :param RedshiftDestinationUpdate: 
        
          Describes an update for a destination in Amazon Redshift.
        
          - **RoleARN** *(string) --* 
        
            The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
          - **ClusterJDBCURL** *(string) --* 
        
            The database connection string.
        
          - **CopyCommand** *(dict) --* 
        
            The ``COPY`` command.
        
            - **DataTableName** *(string) --* **[REQUIRED]** 
        
              The name of the target table. The table must already exist in the database.
        
            - **DataTableColumns** *(string) --* 
        
              A comma-separated list of column names.
        
            - **CopyOptions** *(string) --* 
        
              Optional parameters to use with the Amazon Redshift ``COPY`` command. For more information, see the \"Optional Parameters\" section of `Amazon Redshift COPY command <http://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html>`__ . Some possible examples that would apply to Kinesis Data Firehose are as follows:
        
               ``delimiter \'\t\' lzop;`` - fields are delimited with \"\t\" (TAB character) and compressed using lzop.
        
               ``delimiter \'|\'`` - fields are delimited with \"|\" (this is the default delimiter).
        
               ``delimiter \'|\' escape`` - the delimiter should be escaped.
        
               ``fixedwidth \'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6\'`` - fields are fixed width in the source, with each width specified after every column in the table.
        
               ``JSON \'s3://mybucket/jsonpaths.txt\'`` - data is in JSON format, and the path specified is the format of the data.
        
              For more examples, see `Amazon Redshift COPY command examples <http://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html>`__ .
        
          - **Username** *(string) --* 
        
            The name of the user.
        
          - **Password** *(string) --* 
        
            The user password.
        
          - **RetryOptions** *(dict) --* 
        
            The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).
        
            - **DurationInSeconds** *(integer) --* 
        
              The length of time during which Kinesis Data Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Kinesis Data Firehose does not retry if the value of ``DurationInSeconds`` is 0 (zero) or if the first delivery attempt takes longer than the current value.
        
          - **S3Update** *(dict) --* 
        
            The Amazon S3 destination.
        
            The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified in ``RedshiftDestinationUpdate.S3Update`` because the Amazon Redshift ``COPY`` operation that reads from the S3 bucket doesn\'t support these compression formats.
        
            - **RoleARN** *(string) --* 
        
              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **BucketARN** *(string) --* 
        
              The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **Prefix** *(string) --* 
        
              The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
            - **BufferingHints** *(dict) --* 
        
              The buffering option. If no value is specified, ``BufferingHints`` object default values are used.
        
              - **SizeInMBs** *(integer) --* 
        
                Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
                We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
              - **IntervalInSeconds** *(integer) --* 
        
                Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
            - **CompressionFormat** *(string) --* 
        
              The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
              The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift ``COPY`` operation that reads from the S3 bucket.
        
            - **EncryptionConfiguration** *(dict) --* 
        
              The encryption configuration. If no value is specified, the default is no encryption.
        
              - **NoEncryptionConfig** *(string) --* 
        
                Specifically override existing encryption information to ensure that no encryption is used.
        
              - **KMSEncryptionConfig** *(dict) --* 
        
                The encryption key.
        
                - **AWSKMSKeyARN** *(string) --* **[REQUIRED]** 
        
                  The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **CloudWatchLoggingOptions** *(dict) --* 
        
              The CloudWatch logging options for your delivery stream.
        
              - **Enabled** *(boolean) --* 
        
                Enables or disables CloudWatch logging.
        
              - **LogGroupName** *(string) --* 
        
                The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
              - **LogStreamName** *(string) --* 
        
                The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
          - **ProcessingConfiguration** *(dict) --* 
        
            The data processing configuration.
        
            - **Enabled** *(boolean) --* 
        
              Enables or disables data processing.
        
            - **Processors** *(list) --* 
        
              The data processors.
        
              - *(dict) --* 
        
                Describes a data processor.
        
                - **Type** *(string) --* **[REQUIRED]** 
        
                  The type of processor.
        
                - **Parameters** *(list) --* 
        
                  The processor parameters.
        
                  - *(dict) --* 
        
                    Describes the processor parameter.
        
                    - **ParameterName** *(string) --* **[REQUIRED]** 
        
                      The name of the parameter.
        
                    - **ParameterValue** *(string) --* **[REQUIRED]** 
        
                      The parameter value.
        
          - **S3BackupMode** *(string) --* 
        
            The Amazon S3 backup mode.
        
          - **S3BackupUpdate** *(dict) --* 
        
            The Amazon S3 destination for backup.
        
            - **RoleARN** *(string) --* 
        
              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **BucketARN** *(string) --* 
        
              The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **Prefix** *(string) --* 
        
              The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
            - **BufferingHints** *(dict) --* 
        
              The buffering option. If no value is specified, ``BufferingHints`` object default values are used.
        
              - **SizeInMBs** *(integer) --* 
        
                Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
                We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
              - **IntervalInSeconds** *(integer) --* 
        
                Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
            - **CompressionFormat** *(string) --* 
        
              The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
              The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift ``COPY`` operation that reads from the S3 bucket.
        
            - **EncryptionConfiguration** *(dict) --* 
        
              The encryption configuration. If no value is specified, the default is no encryption.
        
              - **NoEncryptionConfig** *(string) --* 
        
                Specifically override existing encryption information to ensure that no encryption is used.
        
              - **KMSEncryptionConfig** *(dict) --* 
        
                The encryption key.
        
                - **AWSKMSKeyARN** *(string) --* **[REQUIRED]** 
        
                  The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **CloudWatchLoggingOptions** *(dict) --* 
        
              The CloudWatch logging options for your delivery stream.
        
              - **Enabled** *(boolean) --* 
        
                Enables or disables CloudWatch logging.
        
              - **LogGroupName** *(string) --* 
        
                The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
              - **LogStreamName** *(string) --* 
        
                The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
          - **CloudWatchLoggingOptions** *(dict) --* 
        
            The Amazon CloudWatch logging options for your delivery stream.
        
            - **Enabled** *(boolean) --* 
        
              Enables or disables CloudWatch logging.
        
            - **LogGroupName** *(string) --* 
        
              The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
            - **LogStreamName** *(string) --* 
        
              The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
        :type ElasticsearchDestinationUpdate: dict
        :param ElasticsearchDestinationUpdate: 
        
          Describes an update for a destination in Amazon ES.
        
          - **RoleARN** *(string) --* 
        
            The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis Data Firehose for calling the Amazon ES Configuration API and for indexing documents. For more information, see `Grant Kinesis Data Firehose Access to an Amazon S3 Destination <http://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-s3>`__ and `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
          - **DomainARN** *(string) --* 
        
            The ARN of the Amazon ES domain. The IAM role must have permissions for ``DescribeElasticsearchDomain`` , ``DescribeElasticsearchDomains`` , and ``DescribeElasticsearchDomainConfig`` after assuming the IAM role specified in **RoleARN** . For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
          - **IndexName** *(string) --* 
        
            The Elasticsearch index name.
        
          - **TypeName** *(string) --* 
        
            The Elasticsearch type name. For Elasticsearch 6.x, there can be only one type per index. If you try to specify a new type for an existing index that already has another type, Kinesis Data Firehose returns an error during runtime.
        
          - **IndexRotationPeriod** *(string) --* 
        
            The Elasticsearch index rotation period. Index rotation appends a time stamp to ``IndexName`` to facilitate the expiration of old data. For more information, see `Index Rotation for the Amazon ES Destination <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#es-index-rotation>`__ . Default value is ``OneDay`` .
        
          - **BufferingHints** *(dict) --* 
        
            The buffering options. If no value is specified, **ElasticsearchBufferingHints** object default values are used. 
        
            - **IntervalInSeconds** *(integer) --* 
        
              Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).
        
            - **SizeInMBs** *(integer) --* 
        
              Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
              We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
          - **RetryOptions** *(dict) --* 
        
            The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon ES. The default value is 300 (5 minutes).
        
            - **DurationInSeconds** *(integer) --* 
        
              After an initial failure to deliver to Amazon ES, the total amount of time during which Kinesis Data Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.
        
          - **S3Update** *(dict) --* 
        
            The Amazon S3 destination.
        
            - **RoleARN** *(string) --* 
        
              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **BucketARN** *(string) --* 
        
              The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **Prefix** *(string) --* 
        
              The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
            - **BufferingHints** *(dict) --* 
        
              The buffering option. If no value is specified, ``BufferingHints`` object default values are used.
        
              - **SizeInMBs** *(integer) --* 
        
                Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
                We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
              - **IntervalInSeconds** *(integer) --* 
        
                Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
            - **CompressionFormat** *(string) --* 
        
              The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
              The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift ``COPY`` operation that reads from the S3 bucket.
        
            - **EncryptionConfiguration** *(dict) --* 
        
              The encryption configuration. If no value is specified, the default is no encryption.
        
              - **NoEncryptionConfig** *(string) --* 
        
                Specifically override existing encryption information to ensure that no encryption is used.
        
              - **KMSEncryptionConfig** *(dict) --* 
        
                The encryption key.
        
                - **AWSKMSKeyARN** *(string) --* **[REQUIRED]** 
        
                  The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **CloudWatchLoggingOptions** *(dict) --* 
        
              The CloudWatch logging options for your delivery stream.
        
              - **Enabled** *(boolean) --* 
        
                Enables or disables CloudWatch logging.
        
              - **LogGroupName** *(string) --* 
        
                The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
              - **LogStreamName** *(string) --* 
        
                The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
          - **ProcessingConfiguration** *(dict) --* 
        
            The data processing configuration.
        
            - **Enabled** *(boolean) --* 
        
              Enables or disables data processing.
        
            - **Processors** *(list) --* 
        
              The data processors.
        
              - *(dict) --* 
        
                Describes a data processor.
        
                - **Type** *(string) --* **[REQUIRED]** 
        
                  The type of processor.
        
                - **Parameters** *(list) --* 
        
                  The processor parameters.
        
                  - *(dict) --* 
        
                    Describes the processor parameter.
        
                    - **ParameterName** *(string) --* **[REQUIRED]** 
        
                      The name of the parameter.
        
                    - **ParameterValue** *(string) --* **[REQUIRED]** 
        
                      The parameter value.
        
          - **CloudWatchLoggingOptions** *(dict) --* 
        
            The CloudWatch logging options for your delivery stream.
        
            - **Enabled** *(boolean) --* 
        
              Enables or disables CloudWatch logging.
        
            - **LogGroupName** *(string) --* 
        
              The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
            - **LogStreamName** *(string) --* 
        
              The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
        :type SplunkDestinationUpdate: dict
        :param SplunkDestinationUpdate: 
        
          Describes an update for a destination in Splunk.
        
          - **HECEndpoint** *(string) --* 
        
            The HTTP Event Collector (HEC) endpoint to which Kinesis Data Firehose sends your data.
        
          - **HECEndpointType** *(string) --* 
        
            This type can be either \"Raw\" or \"Event.\"
        
          - **HECToken** *(string) --* 
        
            A GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.
        
          - **HECAcknowledgmentTimeoutInSeconds** *(integer) --* 
        
            The amount of time that Kinesis Data Firehose waits to receive an acknowledgment from Splunk after it sends data. At the end of the timeout period, Kinesis Data Firehose either tries to send the data again or considers it an error, based on your retry settings.
        
          - **RetryOptions** *(dict) --* 
        
            The retry behavior in case Kinesis Data Firehose is unable to deliver data to Splunk or if it doesn\'t receive an acknowledgment of receipt from Splunk.
        
            - **DurationInSeconds** *(integer) --* 
        
              The total amount of time that Kinesis Data Firehose spends on retries. This duration starts after the initial attempt to send data to Splunk fails. It doesn\'t include the periods during which Kinesis Data Firehose waits for acknowledgment from Splunk after each attempt.
        
          - **S3BackupMode** *(string) --* 
        
            Defines how documents should be delivered to Amazon S3. When set to ``FailedDocumentsOnly`` , Kinesis Data Firehose writes any data that could not be indexed to the configured Amazon S3 destination. When set to ``AllDocuments`` , Kinesis Data Firehose delivers all incoming records to Amazon S3, and also writes failed documents to Amazon S3. Default value is ``FailedDocumentsOnly`` . 
        
          - **S3Update** *(dict) --* 
        
            Your update to the configuration of the backup Amazon S3 location.
        
            - **RoleARN** *(string) --* 
        
              The Amazon Resource Name (ARN) of the AWS credentials. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **BucketARN** *(string) --* 
        
              The ARN of the S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **Prefix** *(string) --* 
        
              The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see `Amazon S3 Object Name Format <http://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#s3-object-name>`__ in the *Amazon Kinesis Data Firehose Developer Guide* .
        
            - **BufferingHints** *(dict) --* 
        
              The buffering option. If no value is specified, ``BufferingHints`` object default values are used.
        
              - **SizeInMBs** *(integer) --* 
        
                Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
        
                We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
        
              - **IntervalInSeconds** *(integer) --* 
        
                Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
        
            - **CompressionFormat** *(string) --* 
        
              The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
        
              The compression formats ``SNAPPY`` or ``ZIP`` cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift ``COPY`` operation that reads from the S3 bucket.
        
            - **EncryptionConfiguration** *(dict) --* 
        
              The encryption configuration. If no value is specified, the default is no encryption.
        
              - **NoEncryptionConfig** *(string) --* 
        
                Specifically override existing encryption information to ensure that no encryption is used.
        
              - **KMSEncryptionConfig** *(dict) --* 
        
                The encryption key.
        
                - **AWSKMSKeyARN** *(string) --* **[REQUIRED]** 
        
                  The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
            - **CloudWatchLoggingOptions** *(dict) --* 
        
              The CloudWatch logging options for your delivery stream.
        
              - **Enabled** *(boolean) --* 
        
                Enables or disables CloudWatch logging.
        
              - **LogGroupName** *(string) --* 
        
                The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
              - **LogStreamName** *(string) --* 
        
                The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
          - **ProcessingConfiguration** *(dict) --* 
        
            The data processing configuration.
        
            - **Enabled** *(boolean) --* 
        
              Enables or disables data processing.
        
            - **Processors** *(list) --* 
        
              The data processors.
        
              - *(dict) --* 
        
                Describes a data processor.
        
                - **Type** *(string) --* **[REQUIRED]** 
        
                  The type of processor.
        
                - **Parameters** *(list) --* 
        
                  The processor parameters.
        
                  - *(dict) --* 
        
                    Describes the processor parameter.
        
                    - **ParameterName** *(string) --* **[REQUIRED]** 
        
                      The name of the parameter.
        
                    - **ParameterValue** *(string) --* **[REQUIRED]** 
        
                      The parameter value.
        
          - **CloudWatchLoggingOptions** *(dict) --* 
        
            The Amazon CloudWatch logging options for your delivery stream.
        
            - **Enabled** *(boolean) --* 
        
              Enables or disables CloudWatch logging.
        
            - **LogGroupName** *(string) --* 
        
              The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
        
            - **LogStreamName** *(string) --* 
        
              The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass
