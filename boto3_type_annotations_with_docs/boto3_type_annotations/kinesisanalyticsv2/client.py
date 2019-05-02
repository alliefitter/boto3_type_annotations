from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from datetime import datetime
from botocore.waiter import Waiter
from typing import Union
from typing import List


class Client(BaseClient):
    def add_application_cloud_watch_logging_option(self, ApplicationName: str, CurrentApplicationVersionId: int, CloudWatchLoggingOption: Dict) -> Dict:
        """
        Adds an Amazon CloudWatch log stream to monitor application configuration errors.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/AddApplicationCloudWatchLoggingOption>`_
        
        **Request Syntax**
        ::
          response = client.add_application_cloud_watch_logging_option(
              ApplicationName='string',
              CurrentApplicationVersionId=123,
              CloudWatchLoggingOption={
                  'LogStreamARN': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ApplicationARN': 'string',
                'ApplicationVersionId': 123,
                'CloudWatchLoggingOptionDescriptions': [
                    {
                        'CloudWatchLoggingOptionId': 'string',
                        'LogStreamARN': 'string',
                        'RoleARN': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ApplicationARN** *(string) --* 
              The application's ARN.
            - **ApplicationVersionId** *(integer) --* 
              The new version ID of the Kinesis Data Analytics application. Kinesis Data Analytics updates the ``ApplicationVersionId`` each time you change the CloudWatch logging options. 
            - **CloudWatchLoggingOptionDescriptions** *(list) --* 
              The descriptions of the current CloudWatch logging options for the Kinesis Data Analytics application.
              - *(dict) --* 
                Describes the Amazon CloudWatch logging option.
                - **CloudWatchLoggingOptionId** *(string) --* 
                  The ID of the CloudWatch logging option description.
                - **LogStreamARN** *(string) --* 
                  The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.
                - **RoleARN** *(string) --* 
                  The IAM ARN of the role to use to send application messages. 
                  .. note::
                    Provided for backward compatibility. Applications created with the current API version have an application-level service execution role rather than a resource-level role.
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The Kinesis Data Analytics application name.
        :type CurrentApplicationVersionId: integer
        :param CurrentApplicationVersionId: **[REQUIRED]**
          The version ID of the Kinesis Data Analytics application. You can retrieve the application version ID using  DescribeApplication .
        :type CloudWatchLoggingOption: dict
        :param CloudWatchLoggingOption: **[REQUIRED]**
          Provides the Amazon CloudWatch log stream Amazon Resource Name (ARN).
          - **LogStreamARN** *(string) --* **[REQUIRED]**
            The ARN of the CloudWatch log to receive application messages.
        :rtype: dict
        :returns:
        """
        pass

    def add_application_input(self, ApplicationName: str, CurrentApplicationVersionId: int, Input: Dict) -> Dict:
        """
        Adds a streaming source to your SQL-based Amazon Kinesis Data Analytics application. 
        You can add a streaming source when you create an application, or you can use this operation to add a streaming source after you create an application. For more information, see  CreateApplication .
        Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the  DescribeApplication operation to find the current application version. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/AddApplicationInput>`_
        
        **Request Syntax**
        ::
          response = client.add_application_input(
              ApplicationName='string',
              CurrentApplicationVersionId=123,
              Input={
                  'NamePrefix': 'string',
                  'InputProcessingConfiguration': {
                      'InputLambdaProcessor': {
                          'ResourceARN': 'string'
                      }
                  },
                  'KinesisStreamsInput': {
                      'ResourceARN': 'string'
                  },
                  'KinesisFirehoseInput': {
                      'ResourceARN': 'string'
                  },
                  'InputParallelism': {
                      'Count': 123
                  },
                  'InputSchema': {
                      'RecordFormat': {
                          'RecordFormatType': 'JSON'|'CSV',
                          'MappingParameters': {
                              'JSONMappingParameters': {
                                  'RecordRowPath': 'string'
                              },
                              'CSVMappingParameters': {
                                  'RecordRowDelimiter': 'string',
                                  'RecordColumnDelimiter': 'string'
                              }
                          }
                      },
                      'RecordEncoding': 'string',
                      'RecordColumns': [
                          {
                              'Name': 'string',
                              'Mapping': 'string',
                              'SqlType': 'string'
                          },
                      ]
                  }
              }
          )
        
        **Response Syntax**
        ::
            {
                'ApplicationARN': 'string',
                'ApplicationVersionId': 123,
                'InputDescriptions': [
                    {
                        'InputId': 'string',
                        'NamePrefix': 'string',
                        'InAppStreamNames': [
                            'string',
                        ],
                        'InputProcessingConfigurationDescription': {
                            'InputLambdaProcessorDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            }
                        },
                        'KinesisStreamsInputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'KinesisFirehoseInputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'InputSchema': {
                            'RecordFormat': {
                                'RecordFormatType': 'JSON'|'CSV',
                                'MappingParameters': {
                                    'JSONMappingParameters': {
                                        'RecordRowPath': 'string'
                                    },
                                    'CSVMappingParameters': {
                                        'RecordRowDelimiter': 'string',
                                        'RecordColumnDelimiter': 'string'
                                    }
                                }
                            },
                            'RecordEncoding': 'string',
                            'RecordColumns': [
                                {
                                    'Name': 'string',
                                    'Mapping': 'string',
                                    'SqlType': 'string'
                                },
                            ]
                        },
                        'InputParallelism': {
                            'Count': 123
                        },
                        'InputStartingPositionConfiguration': {
                            'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ApplicationARN** *(string) --* 
              The Amazon Resource Name (ARN) of the application.
            - **ApplicationVersionId** *(integer) --* 
              Provides the current application version.
            - **InputDescriptions** *(list) --* 
              Describes the application input configuration. 
              - *(dict) --* 
                Describes the application input configuration for an SQL-based Amazon Kinesis Data Analytics application. 
                - **InputId** *(string) --* 
                  The input ID that is associated with the application input. This is the ID that Kinesis Data Analytics assigns to each input configuration that you add to your application. 
                - **NamePrefix** *(string) --* 
                  The in-application name prefix.
                - **InAppStreamNames** *(list) --* 
                  Returns the in-application stream names that are mapped to the stream source. 
                  - *(string) --* 
                - **InputProcessingConfigurationDescription** *(dict) --* 
                  The description of the preprocessor that executes on records in this input before the application's code is run. 
                  - **InputLambdaProcessorDescription** *(dict) --* 
                    Provides configuration information about the associated  InputLambdaProcessorDescription  
                    - **ResourceARN** *(string) --* 
                      The ARN of the AWS Lambda function that is used to preprocess the records in the stream.
                    - **RoleARN** *(string) --* 
                      The ARN of the IAM role that is used to access the AWS Lambda function.
                      .. note::
                        Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                - **KinesisStreamsInputDescription** *(dict) --* 
                  If a Kinesis data stream is configured as a streaming source, provides the Kinesis data stream's Amazon Resource Name (ARN). 
                  - **ResourceARN** *(string) --* 
                    The Amazon Resource Name (ARN) of the Kinesis data stream.
                  - **RoleARN** *(string) --* 
                    The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.
                    .. note::
                      Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                - **KinesisFirehoseInputDescription** *(dict) --* 
                  If a Kinesis Data Firehose delivery stream is configured as a streaming source, provides the delivery stream's ARN. 
                  - **ResourceARN** *(string) --* 
                    The Amazon Resource Name (ARN) of the delivery stream.
                  - **RoleARN** *(string) --* 
                    The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.
                    .. note::
                      Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                - **InputSchema** *(dict) --* 
                  Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created. 
                  - **RecordFormat** *(dict) --* 
                    Specifies the format of the records on the streaming source.
                    - **RecordFormatType** *(string) --* 
                      The type of record format.
                    - **MappingParameters** *(dict) --* 
                      When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
                      - **JSONMappingParameters** *(dict) --* 
                        Provides additional mapping information when JSON is the record format on the streaming source.
                        - **RecordRowPath** *(string) --* 
                          The path to the top-level parent that contains the records.
                      - **CSVMappingParameters** *(dict) --* 
                        Provides additional mapping information when the record format uses delimiters (for example, CSV).
                        - **RecordRowDelimiter** *(string) --* 
                          The row delimiter. For example, in a CSV format, *'\n'* is the typical row delimiter.
                        - **RecordColumnDelimiter** *(string) --* 
                          The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
                  - **RecordEncoding** *(string) --* 
                    Specifies the encoding of the records in the streaming source. For example, UTF-8.
                  - **RecordColumns** *(list) --* 
                    A list of ``RecordColumn`` objects. 
                    - *(dict) --* 
                      For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
                      Also used to describe the format of the reference data source.
                      - **Name** *(string) --* 
                        The name of the column that is created in the in-application input stream or reference table.
                      - **Mapping** *(string) --* 
                        A reference to the data element in the streaming input of the reference data source.
                      - **SqlType** *(string) --* 
                        The type of column created in the in-application input stream or reference table.
                - **InputParallelism** *(dict) --* 
                  Describes the configured parallelism (number of in-application streams mapped to the streaming source). 
                  - **Count** *(integer) --* 
                    The number of in-application streams to create.
                - **InputStartingPositionConfiguration** *(dict) --* 
                  The point at which the application is configured to read from the input stream.
                  - **InputStartingPosition** *(string) --* 
                    The starting position on the stream.
                    * ``NOW`` - Start reading just after the most recent record in the stream, and start at the request timestamp that the customer issued. 
                    * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Data Firehose delivery stream. 
                    * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped reading. 
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The name of your existing application to which you want to add the streaming source.
        :type CurrentApplicationVersionId: integer
        :param CurrentApplicationVersionId: **[REQUIRED]**
          The current version of your application. You can use the  DescribeApplication operation to find the current application version.
        :type Input: dict
        :param Input: **[REQUIRED]**
          The  Input to add.
          - **NamePrefix** *(string) --* **[REQUIRED]**
            The name prefix to use when creating an in-application stream. Suppose that you specify a prefix \"``MyInApplicationStream`` .\" Kinesis Data Analytics then creates one or more (as per the ``InputParallelism`` count you specified) in-application streams with the names \"``MyInApplicationStream_001`` ,\" \"``MyInApplicationStream_002`` ,\" and so on.
          - **InputProcessingConfiguration** *(dict) --*
            The  InputProcessingConfiguration for the input. An input processor transforms records as they are received from the stream, before the application\'s SQL code executes. Currently, the only input processing configuration available is  InputLambdaProcessor .
            - **InputLambdaProcessor** *(dict) --* **[REQUIRED]**
              The  InputLambdaProcessor that is used to preprocess the records in the stream before being processed by your application code.
              - **ResourceARN** *(string) --* **[REQUIRED]**
                The ARN of the AWS Lambda function that operates on records in the stream.
          - **KinesisStreamsInput** *(dict) --*
            If the streaming source is an Amazon Kinesis data stream, identifies the stream\'s Amazon Resource Name (ARN).
            - **ResourceARN** *(string) --* **[REQUIRED]**
              The ARN of the input Kinesis data stream to read.
          - **KinesisFirehoseInput** *(dict) --*
            If the streaming source is an Amazon Kinesis Data Firehose delivery stream, identifies the delivery stream\'s ARN.
            - **ResourceARN** *(string) --* **[REQUIRED]**
              The Amazon Resource Name (ARN) of the delivery stream.
          - **InputParallelism** *(dict) --*
            Describes the number of in-application streams to create.
            - **Count** *(integer) --*
              The number of in-application streams to create.
          - **InputSchema** *(dict) --* **[REQUIRED]**
            Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.
            Also used to describe the format of the reference data source.
            - **RecordFormat** *(dict) --* **[REQUIRED]**
              Specifies the format of the records on the streaming source.
              - **RecordFormatType** *(string) --* **[REQUIRED]**
                The type of record format.
              - **MappingParameters** *(dict) --*
                When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
                - **JSONMappingParameters** *(dict) --*
                  Provides additional mapping information when JSON is the record format on the streaming source.
                  - **RecordRowPath** *(string) --* **[REQUIRED]**
                    The path to the top-level parent that contains the records.
                - **CSVMappingParameters** *(dict) --*
                  Provides additional mapping information when the record format uses delimiters (for example, CSV).
                  - **RecordRowDelimiter** *(string) --* **[REQUIRED]**
                    The row delimiter. For example, in a CSV format, *\'\n\'* is the typical row delimiter.
                  - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**
                    The column delimiter. For example, in a CSV format, a comma (\",\") is the typical column delimiter.
            - **RecordEncoding** *(string) --*
              Specifies the encoding of the records in the streaming source. For example, UTF-8.
            - **RecordColumns** *(list) --* **[REQUIRED]**
              A list of ``RecordColumn`` objects.
              - *(dict) --*
                For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
                Also used to describe the format of the reference data source.
                - **Name** *(string) --* **[REQUIRED]**
                  The name of the column that is created in the in-application input stream or reference table.
                - **Mapping** *(string) --*
                  A reference to the data element in the streaming input of the reference data source.
                - **SqlType** *(string) --* **[REQUIRED]**
                  The type of column created in the in-application input stream or reference table.
        :rtype: dict
        :returns:
        """
        pass

    def add_application_input_processing_configuration(self, ApplicationName: str, CurrentApplicationVersionId: int, InputId: str, InputProcessingConfiguration: Dict) -> Dict:
        """
        Adds an  InputProcessingConfiguration to an SQL-based Kinesis Data Analytics application. An input processor pre-processes records on the input stream before the application's SQL code executes. Currently, the only input processor available is `AWS Lambda <https://aws.amazon.com/documentation/lambda/>`__ .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/AddApplicationInputProcessingConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.add_application_input_processing_configuration(
              ApplicationName='string',
              CurrentApplicationVersionId=123,
              InputId='string',
              InputProcessingConfiguration={
                  'InputLambdaProcessor': {
                      'ResourceARN': 'string'
                  }
              }
          )
        
        **Response Syntax**
        ::
            {
                'ApplicationARN': 'string',
                'ApplicationVersionId': 123,
                'InputId': 'string',
                'InputProcessingConfigurationDescription': {
                    'InputLambdaProcessorDescription': {
                        'ResourceARN': 'string',
                        'RoleARN': 'string'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ApplicationARN** *(string) --* 
              The Amazon Resource Name (ARN) of the application.
            - **ApplicationVersionId** *(integer) --* 
              Provides the current application version.
            - **InputId** *(string) --* 
              The input ID that is associated with the application input. This is the ID that Amazon Kinesis Data Analytics assigns to each input configuration that you add to your application.
            - **InputProcessingConfigurationDescription** *(dict) --* 
              The description of the preprocessor that executes on records in this input before the application's code is run.
              - **InputLambdaProcessorDescription** *(dict) --* 
                Provides configuration information about the associated  InputLambdaProcessorDescription  
                - **ResourceARN** *(string) --* 
                  The ARN of the AWS Lambda function that is used to preprocess the records in the stream.
                - **RoleARN** *(string) --* 
                  The ARN of the IAM role that is used to access the AWS Lambda function.
                  .. note::
                    Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The name of the application to which you want to add the input processing configuration.
        :type CurrentApplicationVersionId: integer
        :param CurrentApplicationVersionId: **[REQUIRED]**
          The version of the application to which you want to add the input processing configuration. You can use the  DescribeApplication operation to get the current application version. If the version specified is not the current version, the ``ConcurrentModificationException`` is returned.
        :type InputId: string
        :param InputId: **[REQUIRED]**
          The ID of the input configuration to add the input processing configuration to. You can get a list of the input IDs for an application using the  DescribeApplication operation.
        :type InputProcessingConfiguration: dict
        :param InputProcessingConfiguration: **[REQUIRED]**
          The  InputProcessingConfiguration to add to the application.
          - **InputLambdaProcessor** *(dict) --* **[REQUIRED]**
            The  InputLambdaProcessor that is used to preprocess the records in the stream before being processed by your application code.
            - **ResourceARN** *(string) --* **[REQUIRED]**
              The ARN of the AWS Lambda function that operates on records in the stream.
        :rtype: dict
        :returns:
        """
        pass

    def add_application_output(self, ApplicationName: str, CurrentApplicationVersionId: int, Output: Dict) -> Dict:
        """
        Adds an external destination to your SQL-based Amazon Kinesis Data Analytics application.
        If you want Kinesis Data Analytics to deliver data from an in-application stream within your application to an external destination (such as an Kinesis data stream, a Kinesis Data Firehose delivery stream, or an AWS Lambda function), you add the relevant configuration to your application using this operation. You can configure one or more outputs for your application. Each output configuration maps an in-application stream and an external destination.
        You can use one of the output configurations to deliver data from your in-application error stream to an external destination so that you can analyze the errors. 
        Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the  DescribeApplication operation to find the current application version.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/AddApplicationOutput>`_
        
        **Request Syntax**
        ::
          response = client.add_application_output(
              ApplicationName='string',
              CurrentApplicationVersionId=123,
              Output={
                  'Name': 'string',
                  'KinesisStreamsOutput': {
                      'ResourceARN': 'string'
                  },
                  'KinesisFirehoseOutput': {
                      'ResourceARN': 'string'
                  },
                  'LambdaOutput': {
                      'ResourceARN': 'string'
                  },
                  'DestinationSchema': {
                      'RecordFormatType': 'JSON'|'CSV'
                  }
              }
          )
        
        **Response Syntax**
        ::
            {
                'ApplicationARN': 'string',
                'ApplicationVersionId': 123,
                'OutputDescriptions': [
                    {
                        'OutputId': 'string',
                        'Name': 'string',
                        'KinesisStreamsOutputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'KinesisFirehoseOutputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'LambdaOutputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'DestinationSchema': {
                            'RecordFormatType': 'JSON'|'CSV'
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ApplicationARN** *(string) --* 
              The application Amazon Resource Name (ARN).
            - **ApplicationVersionId** *(integer) --* 
              The updated application version ID. Kinesis Data Analytics increments this ID when the application is updated.
            - **OutputDescriptions** *(list) --* 
              Describes the application output configuration. For more information, see `Configuring Application Output <http://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`__ . 
              - *(dict) --* 
                For an SQL-based Amazon Kinesis Data Analytics application, describes the application output configuration, which includes the in-application stream name and the destination where the stream data is written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream. 
                - **OutputId** *(string) --* 
                  A unique identifier for the output configuration.
                - **Name** *(string) --* 
                  The name of the in-application stream that is configured as output.
                - **KinesisStreamsOutputDescription** *(dict) --* 
                  Describes the Kinesis data stream that is configured as the destination where output is written.
                  - **ResourceARN** *(string) --* 
                    The Amazon Resource Name (ARN) of the Kinesis data stream.
                  - **RoleARN** *(string) --* 
                    The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.
                    .. note::
                      Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                - **KinesisFirehoseOutputDescription** *(dict) --* 
                  Describes the Kinesis Data Firehose delivery stream that is configured as the destination where output is written.
                  - **ResourceARN** *(string) --* 
                    The Amazon Resource Name (ARN) of the delivery stream.
                  - **RoleARN** *(string) --* 
                    The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.
                    .. note::
                      Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                - **LambdaOutputDescription** *(dict) --* 
                  Describes the Lambda function that is configured as the destination where output is written.
                  - **ResourceARN** *(string) --* 
                    The Amazon Resource Name (ARN) of the destination Lambda function.
                  - **RoleARN** *(string) --* 
                    The ARN of the IAM role that Kinesis Data Analytics can assume to write to the destination function.
                    .. note::
                      Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                - **DestinationSchema** *(dict) --* 
                  The data format used for writing data to the destination.
                  - **RecordFormatType** *(string) --* 
                    Specifies the format of the records on the output stream.
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The name of the application to which you want to add the output configuration.
        :type CurrentApplicationVersionId: integer
        :param CurrentApplicationVersionId: **[REQUIRED]**
          The version of the application to which you want to add the output configuration. You can use the  DescribeApplication operation to get the current application version. If the version specified is not the current version, the ``ConcurrentModificationException`` is returned.
        :type Output: dict
        :param Output: **[REQUIRED]**
          An array of objects, each describing one output configuration. In the output configuration, you specify the name of an in-application stream, a destination (that is, a Kinesis data stream, a Kinesis Data Firehose delivery stream, or an AWS Lambda function), and record the formation to use when writing to the destination.
          - **Name** *(string) --* **[REQUIRED]**
            The name of the in-application stream.
          - **KinesisStreamsOutput** *(dict) --*
            Identifies an Amazon Kinesis data stream as the destination.
            - **ResourceARN** *(string) --* **[REQUIRED]**
              The ARN of the destination Kinesis data stream to write to.
          - **KinesisFirehoseOutput** *(dict) --*
            Identifies an Amazon Kinesis Data Firehose delivery stream as the destination.
            - **ResourceARN** *(string) --* **[REQUIRED]**
              The ARN of the destination delivery stream to write to.
          - **LambdaOutput** *(dict) --*
            Identifies an AWS Lambda function as the destination.
            - **ResourceARN** *(string) --* **[REQUIRED]**
              The Amazon Resource Name (ARN) of the destination Lambda function to write to.
          - **DestinationSchema** *(dict) --* **[REQUIRED]**
            Describes the data format when records are written to the destination.
            - **RecordFormatType** *(string) --* **[REQUIRED]**
              Specifies the format of the records on the output stream.
        :rtype: dict
        :returns:
        """
        pass

    def add_application_reference_data_source(self, ApplicationName: str, CurrentApplicationVersionId: int, ReferenceDataSource: Dict) -> Dict:
        """
        Adds a reference data source to an existing SQL-based Amazon Kinesis Data Analytics application.
        Kinesis Data Analytics reads reference data (that is, an Amazon S3 object) and creates an in-application table within your application. In the request, you provide the source (S3 bucket name and object key name), name of the in-application table to create, and the necessary mapping information that describes how data in an Amazon S3 object maps to columns in the resulting in-application table.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/AddApplicationReferenceDataSource>`_
        
        **Request Syntax**
        ::
          response = client.add_application_reference_data_source(
              ApplicationName='string',
              CurrentApplicationVersionId=123,
              ReferenceDataSource={
                  'TableName': 'string',
                  'S3ReferenceDataSource': {
                      'BucketARN': 'string',
                      'FileKey': 'string'
                  },
                  'ReferenceSchema': {
                      'RecordFormat': {
                          'RecordFormatType': 'JSON'|'CSV',
                          'MappingParameters': {
                              'JSONMappingParameters': {
                                  'RecordRowPath': 'string'
                              },
                              'CSVMappingParameters': {
                                  'RecordRowDelimiter': 'string',
                                  'RecordColumnDelimiter': 'string'
                              }
                          }
                      },
                      'RecordEncoding': 'string',
                      'RecordColumns': [
                          {
                              'Name': 'string',
                              'Mapping': 'string',
                              'SqlType': 'string'
                          },
                      ]
                  }
              }
          )
        
        **Response Syntax**
        ::
            {
                'ApplicationARN': 'string',
                'ApplicationVersionId': 123,
                'ReferenceDataSourceDescriptions': [
                    {
                        'ReferenceId': 'string',
                        'TableName': 'string',
                        'S3ReferenceDataSourceDescription': {
                            'BucketARN': 'string',
                            'FileKey': 'string',
                            'ReferenceRoleARN': 'string'
                        },
                        'ReferenceSchema': {
                            'RecordFormat': {
                                'RecordFormatType': 'JSON'|'CSV',
                                'MappingParameters': {
                                    'JSONMappingParameters': {
                                        'RecordRowPath': 'string'
                                    },
                                    'CSVMappingParameters': {
                                        'RecordRowDelimiter': 'string',
                                        'RecordColumnDelimiter': 'string'
                                    }
                                }
                            },
                            'RecordEncoding': 'string',
                            'RecordColumns': [
                                {
                                    'Name': 'string',
                                    'Mapping': 'string',
                                    'SqlType': 'string'
                                },
                            ]
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ApplicationARN** *(string) --* 
              The application Amazon Resource Name (ARN).
            - **ApplicationVersionId** *(integer) --* 
              The updated application version ID. Amazon Kinesis Data Analytics increments this ID when the application is updated.
            - **ReferenceDataSourceDescriptions** *(list) --* 
              Describes reference data sources configured for the application. 
              - *(dict) --* 
                For an SQL-based Amazon Kinesis Data Analytics application, describes the reference data source configured for an application.
                - **ReferenceId** *(string) --* 
                  The ID of the reference data source. This is the ID that Kinesis Data Analytics assigns when you add the reference data source to your application using the  CreateApplication or  UpdateApplication operation.
                - **TableName** *(string) --* 
                  The in-application table name created by the specific reference data source configuration.
                - **S3ReferenceDataSourceDescription** *(dict) --* 
                  Provides the Amazon S3 bucket name, the object key name that contains the reference data. 
                  - **BucketARN** *(string) --* 
                    The Amazon Resource Name (ARN) of the S3 bucket.
                  - **FileKey** *(string) --* 
                    Amazon S3 object key name.
                  - **ReferenceRoleARN** *(string) --* 
                    The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon S3 object on your behalf to populate the in-application reference table. 
                    .. note::
                      Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                - **ReferenceSchema** *(dict) --* 
                  Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.
                  - **RecordFormat** *(dict) --* 
                    Specifies the format of the records on the streaming source.
                    - **RecordFormatType** *(string) --* 
                      The type of record format.
                    - **MappingParameters** *(dict) --* 
                      When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
                      - **JSONMappingParameters** *(dict) --* 
                        Provides additional mapping information when JSON is the record format on the streaming source.
                        - **RecordRowPath** *(string) --* 
                          The path to the top-level parent that contains the records.
                      - **CSVMappingParameters** *(dict) --* 
                        Provides additional mapping information when the record format uses delimiters (for example, CSV).
                        - **RecordRowDelimiter** *(string) --* 
                          The row delimiter. For example, in a CSV format, *'\n'* is the typical row delimiter.
                        - **RecordColumnDelimiter** *(string) --* 
                          The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
                  - **RecordEncoding** *(string) --* 
                    Specifies the encoding of the records in the streaming source. For example, UTF-8.
                  - **RecordColumns** *(list) --* 
                    A list of ``RecordColumn`` objects. 
                    - *(dict) --* 
                      For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
                      Also used to describe the format of the reference data source.
                      - **Name** *(string) --* 
                        The name of the column that is created in the in-application input stream or reference table.
                      - **Mapping** *(string) --* 
                        A reference to the data element in the streaming input of the reference data source.
                      - **SqlType** *(string) --* 
                        The type of column created in the in-application input stream or reference table.
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The name of an existing application.
        :type CurrentApplicationVersionId: integer
        :param CurrentApplicationVersionId: **[REQUIRED]**
          The version of the application for which you are adding the reference data source. You can use the  DescribeApplication operation to get the current application version. If the version specified is not the current version, the ``ConcurrentModificationException`` is returned.
        :type ReferenceDataSource: dict
        :param ReferenceDataSource: **[REQUIRED]**
          The reference data source can be an object in your Amazon S3 bucket. Kinesis Data Analytics reads the object and copies the data into the in-application table that is created. You provide an S3 bucket, object key name, and the resulting in-application table that is created.
          - **TableName** *(string) --* **[REQUIRED]**
            The name of the in-application table to create.
          - **S3ReferenceDataSource** *(dict) --*
            Identifies the S3 bucket and object that contains the reference data. A Kinesis Data Analytics application loads reference data only once. If the data changes, you call the  UpdateApplication operation to trigger reloading of data into your application.
            - **BucketARN** *(string) --*
              The Amazon Resource Name (ARN) of the S3 bucket.
            - **FileKey** *(string) --*
              The object key name containing the reference data.
          - **ReferenceSchema** *(dict) --* **[REQUIRED]**
            Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.
            - **RecordFormat** *(dict) --* **[REQUIRED]**
              Specifies the format of the records on the streaming source.
              - **RecordFormatType** *(string) --* **[REQUIRED]**
                The type of record format.
              - **MappingParameters** *(dict) --*
                When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
                - **JSONMappingParameters** *(dict) --*
                  Provides additional mapping information when JSON is the record format on the streaming source.
                  - **RecordRowPath** *(string) --* **[REQUIRED]**
                    The path to the top-level parent that contains the records.
                - **CSVMappingParameters** *(dict) --*
                  Provides additional mapping information when the record format uses delimiters (for example, CSV).
                  - **RecordRowDelimiter** *(string) --* **[REQUIRED]**
                    The row delimiter. For example, in a CSV format, *\'\n\'* is the typical row delimiter.
                  - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**
                    The column delimiter. For example, in a CSV format, a comma (\",\") is the typical column delimiter.
            - **RecordEncoding** *(string) --*
              Specifies the encoding of the records in the streaming source. For example, UTF-8.
            - **RecordColumns** *(list) --* **[REQUIRED]**
              A list of ``RecordColumn`` objects.
              - *(dict) --*
                For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
                Also used to describe the format of the reference data source.
                - **Name** *(string) --* **[REQUIRED]**
                  The name of the column that is created in the in-application input stream or reference table.
                - **Mapping** *(string) --*
                  A reference to the data element in the streaming input of the reference data source.
                - **SqlType** *(string) --* **[REQUIRED]**
                  The type of column created in the in-application input stream or reference table.
        :rtype: dict
        :returns:
        """
        pass

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

    def create_application(self, ApplicationName: str, RuntimeEnvironment: str, ServiceExecutionRole: str, ApplicationDescription: str = None, ApplicationConfiguration: Dict = None, CloudWatchLoggingOptions: List = None) -> Dict:
        """
        Creates an Amazon Kinesis Data Analytics application. For information about creating a Kinesis Data Analytics application, see `Creating an Application <https://docs.aws.amazon.com/kinesisanalytics/latest/Java/creating-app.html>`__ . 
        .. note::
          SQL is not enabled for this private beta release. Using SQL parameters (such as  SqlApplicationConfiguration ) will result in an error.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/CreateApplication>`_
        
        **Request Syntax**
        ::
          response = client.create_application(
              ApplicationName='string',
              ApplicationDescription='string',
              RuntimeEnvironment='SQL-1_0'|'FLINK-1_6',
              ServiceExecutionRole='string',
              ApplicationConfiguration={
                  'SqlApplicationConfiguration': {
                      'Inputs': [
                          {
                              'NamePrefix': 'string',
                              'InputProcessingConfiguration': {
                                  'InputLambdaProcessor': {
                                      'ResourceARN': 'string'
                                  }
                              },
                              'KinesisStreamsInput': {
                                  'ResourceARN': 'string'
                              },
                              'KinesisFirehoseInput': {
                                  'ResourceARN': 'string'
                              },
                              'InputParallelism': {
                                  'Count': 123
                              },
                              'InputSchema': {
                                  'RecordFormat': {
                                      'RecordFormatType': 'JSON'|'CSV',
                                      'MappingParameters': {
                                          'JSONMappingParameters': {
                                              'RecordRowPath': 'string'
                                          },
                                          'CSVMappingParameters': {
                                              'RecordRowDelimiter': 'string',
                                              'RecordColumnDelimiter': 'string'
                                          }
                                      }
                                  },
                                  'RecordEncoding': 'string',
                                  'RecordColumns': [
                                      {
                                          'Name': 'string',
                                          'Mapping': 'string',
                                          'SqlType': 'string'
                                      },
                                  ]
                              }
                          },
                      ],
                      'Outputs': [
                          {
                              'Name': 'string',
                              'KinesisStreamsOutput': {
                                  'ResourceARN': 'string'
                              },
                              'KinesisFirehoseOutput': {
                                  'ResourceARN': 'string'
                              },
                              'LambdaOutput': {
                                  'ResourceARN': 'string'
                              },
                              'DestinationSchema': {
                                  'RecordFormatType': 'JSON'|'CSV'
                              }
                          },
                      ],
                      'ReferenceDataSources': [
                          {
                              'TableName': 'string',
                              'S3ReferenceDataSource': {
                                  'BucketARN': 'string',
                                  'FileKey': 'string'
                              },
                              'ReferenceSchema': {
                                  'RecordFormat': {
                                      'RecordFormatType': 'JSON'|'CSV',
                                      'MappingParameters': {
                                          'JSONMappingParameters': {
                                              'RecordRowPath': 'string'
                                          },
                                          'CSVMappingParameters': {
                                              'RecordRowDelimiter': 'string',
                                              'RecordColumnDelimiter': 'string'
                                          }
                                      }
                                  },
                                  'RecordEncoding': 'string',
                                  'RecordColumns': [
                                      {
                                          'Name': 'string',
                                          'Mapping': 'string',
                                          'SqlType': 'string'
                                      },
                                  ]
                              }
                          },
                      ]
                  },
                  'FlinkApplicationConfiguration': {
                      'CheckpointConfiguration': {
                          'ConfigurationType': 'DEFAULT'|'CUSTOM',
                          'CheckpointingEnabled': True|False,
                          'CheckpointInterval': 123,
                          'MinPauseBetweenCheckpoints': 123
                      },
                      'MonitoringConfiguration': {
                          'ConfigurationType': 'DEFAULT'|'CUSTOM',
                          'MetricsLevel': 'APPLICATION'|'TASK'|'OPERATOR'|'PARALLELISM',
                          'LogLevel': 'INFO'|'WARN'|'ERROR'|'DEBUG'
                      },
                      'ParallelismConfiguration': {
                          'ConfigurationType': 'DEFAULT'|'CUSTOM',
                          'Parallelism': 123,
                          'ParallelismPerKPU': 123,
                          'AutoScalingEnabled': True|False
                      }
                  },
                  'EnvironmentProperties': {
                      'PropertyGroups': [
                          {
                              'PropertyGroupId': 'string',
                              'PropertyMap': {
                                  'string': 'string'
                              }
                          },
                      ]
                  },
                  'ApplicationCodeConfiguration': {
                      'CodeContent': {
                          'TextContent': 'string',
                          'ZipFileContent': b'bytes',
                          'S3ContentLocation': {
                              'BucketARN': 'string',
                              'FileKey': 'string',
                              'ObjectVersion': 'string'
                          }
                      },
                      'CodeContentType': 'PLAINTEXT'|'ZIPFILE'
                  },
                  'ApplicationSnapshotConfiguration': {
                      'SnapshotsEnabled': True|False
                  }
              },
              CloudWatchLoggingOptions=[
                  {
                      'LogStreamARN': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'ApplicationDetail': {
                    'ApplicationARN': 'string',
                    'ApplicationDescription': 'string',
                    'ApplicationName': 'string',
                    'RuntimeEnvironment': 'SQL-1_0'|'FLINK-1_6',
                    'ServiceExecutionRole': 'string',
                    'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING',
                    'ApplicationVersionId': 123,
                    'CreateTimestamp': datetime(2015, 1, 1),
                    'LastUpdateTimestamp': datetime(2015, 1, 1),
                    'ApplicationConfigurationDescription': {
                        'SqlApplicationConfigurationDescription': {
                            'InputDescriptions': [
                                {
                                    'InputId': 'string',
                                    'NamePrefix': 'string',
                                    'InAppStreamNames': [
                                        'string',
                                    ],
                                    'InputProcessingConfigurationDescription': {
                                        'InputLambdaProcessorDescription': {
                                            'ResourceARN': 'string',
                                            'RoleARN': 'string'
                                        }
                                    },
                                    'KinesisStreamsInputDescription': {
                                        'ResourceARN': 'string',
                                        'RoleARN': 'string'
                                    },
                                    'KinesisFirehoseInputDescription': {
                                        'ResourceARN': 'string',
                                        'RoleARN': 'string'
                                    },
                                    'InputSchema': {
                                        'RecordFormat': {
                                            'RecordFormatType': 'JSON'|'CSV',
                                            'MappingParameters': {
                                                'JSONMappingParameters': {
                                                    'RecordRowPath': 'string'
                                                },
                                                'CSVMappingParameters': {
                                                    'RecordRowDelimiter': 'string',
                                                    'RecordColumnDelimiter': 'string'
                                                }
                                            }
                                        },
                                        'RecordEncoding': 'string',
                                        'RecordColumns': [
                                            {
                                                'Name': 'string',
                                                'Mapping': 'string',
                                                'SqlType': 'string'
                                            },
                                        ]
                                    },
                                    'InputParallelism': {
                                        'Count': 123
                                    },
                                    'InputStartingPositionConfiguration': {
                                        'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
                                    }
                                },
                            ],
                            'OutputDescriptions': [
                                {
                                    'OutputId': 'string',
                                    'Name': 'string',
                                    'KinesisStreamsOutputDescription': {
                                        'ResourceARN': 'string',
                                        'RoleARN': 'string'
                                    },
                                    'KinesisFirehoseOutputDescription': {
                                        'ResourceARN': 'string',
                                        'RoleARN': 'string'
                                    },
                                    'LambdaOutputDescription': {
                                        'ResourceARN': 'string',
                                        'RoleARN': 'string'
                                    },
                                    'DestinationSchema': {
                                        'RecordFormatType': 'JSON'|'CSV'
                                    }
                                },
                            ],
                            'ReferenceDataSourceDescriptions': [
                                {
                                    'ReferenceId': 'string',
                                    'TableName': 'string',
                                    'S3ReferenceDataSourceDescription': {
                                        'BucketARN': 'string',
                                        'FileKey': 'string',
                                        'ReferenceRoleARN': 'string'
                                    },
                                    'ReferenceSchema': {
                                        'RecordFormat': {
                                            'RecordFormatType': 'JSON'|'CSV',
                                            'MappingParameters': {
                                                'JSONMappingParameters': {
                                                    'RecordRowPath': 'string'
                                                },
                                                'CSVMappingParameters': {
                                                    'RecordRowDelimiter': 'string',
                                                    'RecordColumnDelimiter': 'string'
                                                }
                                            }
                                        },
                                        'RecordEncoding': 'string',
                                        'RecordColumns': [
                                            {
                                                'Name': 'string',
                                                'Mapping': 'string',
                                                'SqlType': 'string'
                                            },
                                        ]
                                    }
                                },
                            ]
                        },
                        'ApplicationCodeConfigurationDescription': {
                            'CodeContentType': 'PLAINTEXT'|'ZIPFILE',
                            'CodeContentDescription': {
                                'TextContent': 'string',
                                'CodeMD5': 'string',
                                'CodeSize': 123,
                                'S3ApplicationCodeLocationDescription': {
                                    'BucketARN': 'string',
                                    'FileKey': 'string',
                                    'ObjectVersion': 'string'
                                }
                            }
                        },
                        'RunConfigurationDescription': {
                            'ApplicationRestoreConfigurationDescription': {
                                'ApplicationRestoreType': 'SKIP_RESTORE_FROM_SNAPSHOT'|'RESTORE_FROM_LATEST_SNAPSHOT'|'RESTORE_FROM_CUSTOM_SNAPSHOT',
                                'SnapshotName': 'string'
                            }
                        },
                        'FlinkApplicationConfigurationDescription': {
                            'CheckpointConfigurationDescription': {
                                'ConfigurationType': 'DEFAULT'|'CUSTOM',
                                'CheckpointingEnabled': True|False,
                                'CheckpointInterval': 123,
                                'MinPauseBetweenCheckpoints': 123
                            },
                            'MonitoringConfigurationDescription': {
                                'ConfigurationType': 'DEFAULT'|'CUSTOM',
                                'MetricsLevel': 'APPLICATION'|'TASK'|'OPERATOR'|'PARALLELISM',
                                'LogLevel': 'INFO'|'WARN'|'ERROR'|'DEBUG'
                            },
                            'ParallelismConfigurationDescription': {
                                'ConfigurationType': 'DEFAULT'|'CUSTOM',
                                'Parallelism': 123,
                                'ParallelismPerKPU': 123,
                                'CurrentParallelism': 123,
                                'AutoScalingEnabled': True|False
                            },
                            'JobPlanDescription': 'string'
                        },
                        'EnvironmentPropertyDescriptions': {
                            'PropertyGroupDescriptions': [
                                {
                                    'PropertyGroupId': 'string',
                                    'PropertyMap': {
                                        'string': 'string'
                                    }
                                },
                            ]
                        },
                        'ApplicationSnapshotConfigurationDescription': {
                            'SnapshotsEnabled': True|False
                        }
                    },
                    'CloudWatchLoggingOptionDescriptions': [
                        {
                            'CloudWatchLoggingOptionId': 'string',
                            'LogStreamARN': 'string',
                            'RoleARN': 'string'
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ApplicationDetail** *(dict) --* 
              In response to your ``CreateApplication`` request, Kinesis Data Analytics returns a response with details of the application it created.
              - **ApplicationARN** *(string) --* 
                The ARN of the application.
              - **ApplicationDescription** *(string) --* 
                The description of the application.
              - **ApplicationName** *(string) --* 
                The name of the application.
              - **RuntimeEnvironment** *(string) --* 
                The runtime environment for the application (``SQL-1.0`` or ``JAVA-8-FLINK-1.5`` ).
              - **ServiceExecutionRole** *(string) --* 
                Specifies the IAM role that the application uses to access external resources.
              - **ApplicationStatus** *(string) --* 
                The status of the application.
              - **ApplicationVersionId** *(integer) --* 
                Provides the current application version. Kinesis Data Analytics updates the ``ApplicationVersionId`` each time you update the application.
              - **CreateTimestamp** *(datetime) --* 
                The current timestamp when the application was created.
              - **LastUpdateTimestamp** *(datetime) --* 
                The current timestamp when the application was last updated.
              - **ApplicationConfigurationDescription** *(dict) --* 
                Provides details about the application's SQL or Java code and starting parameters.
                - **SqlApplicationConfigurationDescription** *(dict) --* 
                  The details about inputs, outputs, and reference data sources for an SQL-based Kinesis Data Analytics application.
                  - **InputDescriptions** *(list) --* 
                    The array of  InputDescription objects describing the input streams used by the application.
                    - *(dict) --* 
                      Describes the application input configuration for an SQL-based Amazon Kinesis Data Analytics application. 
                      - **InputId** *(string) --* 
                        The input ID that is associated with the application input. This is the ID that Kinesis Data Analytics assigns to each input configuration that you add to your application. 
                      - **NamePrefix** *(string) --* 
                        The in-application name prefix.
                      - **InAppStreamNames** *(list) --* 
                        Returns the in-application stream names that are mapped to the stream source. 
                        - *(string) --* 
                      - **InputProcessingConfigurationDescription** *(dict) --* 
                        The description of the preprocessor that executes on records in this input before the application's code is run. 
                        - **InputLambdaProcessorDescription** *(dict) --* 
                          Provides configuration information about the associated  InputLambdaProcessorDescription  
                          - **ResourceARN** *(string) --* 
                            The ARN of the AWS Lambda function that is used to preprocess the records in the stream.
                          - **RoleARN** *(string) --* 
                            The ARN of the IAM role that is used to access the AWS Lambda function.
                            .. note::
                              Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **KinesisStreamsInputDescription** *(dict) --* 
                        If a Kinesis data stream is configured as a streaming source, provides the Kinesis data stream's Amazon Resource Name (ARN). 
                        - **ResourceARN** *(string) --* 
                          The Amazon Resource Name (ARN) of the Kinesis data stream.
                        - **RoleARN** *(string) --* 
                          The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.
                          .. note::
                            Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **KinesisFirehoseInputDescription** *(dict) --* 
                        If a Kinesis Data Firehose delivery stream is configured as a streaming source, provides the delivery stream's ARN. 
                        - **ResourceARN** *(string) --* 
                          The Amazon Resource Name (ARN) of the delivery stream.
                        - **RoleARN** *(string) --* 
                          The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.
                          .. note::
                            Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **InputSchema** *(dict) --* 
                        Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created. 
                        - **RecordFormat** *(dict) --* 
                          Specifies the format of the records on the streaming source.
                          - **RecordFormatType** *(string) --* 
                            The type of record format.
                          - **MappingParameters** *(dict) --* 
                            When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
                            - **JSONMappingParameters** *(dict) --* 
                              Provides additional mapping information when JSON is the record format on the streaming source.
                              - **RecordRowPath** *(string) --* 
                                The path to the top-level parent that contains the records.
                            - **CSVMappingParameters** *(dict) --* 
                              Provides additional mapping information when the record format uses delimiters (for example, CSV).
                              - **RecordRowDelimiter** *(string) --* 
                                The row delimiter. For example, in a CSV format, *'\n'* is the typical row delimiter.
                              - **RecordColumnDelimiter** *(string) --* 
                                The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
                        - **RecordEncoding** *(string) --* 
                          Specifies the encoding of the records in the streaming source. For example, UTF-8.
                        - **RecordColumns** *(list) --* 
                          A list of ``RecordColumn`` objects. 
                          - *(dict) --* 
                            For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
                            Also used to describe the format of the reference data source.
                            - **Name** *(string) --* 
                              The name of the column that is created in the in-application input stream or reference table.
                            - **Mapping** *(string) --* 
                              A reference to the data element in the streaming input of the reference data source.
                            - **SqlType** *(string) --* 
                              The type of column created in the in-application input stream or reference table.
                      - **InputParallelism** *(dict) --* 
                        Describes the configured parallelism (number of in-application streams mapped to the streaming source). 
                        - **Count** *(integer) --* 
                          The number of in-application streams to create.
                      - **InputStartingPositionConfiguration** *(dict) --* 
                        The point at which the application is configured to read from the input stream.
                        - **InputStartingPosition** *(string) --* 
                          The starting position on the stream.
                          * ``NOW`` - Start reading just after the most recent record in the stream, and start at the request timestamp that the customer issued. 
                          * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Data Firehose delivery stream. 
                          * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped reading. 
                  - **OutputDescriptions** *(list) --* 
                    The array of  OutputDescription objects describing the destination streams used by the application.
                    - *(dict) --* 
                      For an SQL-based Amazon Kinesis Data Analytics application, describes the application output configuration, which includes the in-application stream name and the destination where the stream data is written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream. 
                      - **OutputId** *(string) --* 
                        A unique identifier for the output configuration.
                      - **Name** *(string) --* 
                        The name of the in-application stream that is configured as output.
                      - **KinesisStreamsOutputDescription** *(dict) --* 
                        Describes the Kinesis data stream that is configured as the destination where output is written.
                        - **ResourceARN** *(string) --* 
                          The Amazon Resource Name (ARN) of the Kinesis data stream.
                        - **RoleARN** *(string) --* 
                          The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.
                          .. note::
                            Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **KinesisFirehoseOutputDescription** *(dict) --* 
                        Describes the Kinesis Data Firehose delivery stream that is configured as the destination where output is written.
                        - **ResourceARN** *(string) --* 
                          The Amazon Resource Name (ARN) of the delivery stream.
                        - **RoleARN** *(string) --* 
                          The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.
                          .. note::
                            Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **LambdaOutputDescription** *(dict) --* 
                        Describes the Lambda function that is configured as the destination where output is written.
                        - **ResourceARN** *(string) --* 
                          The Amazon Resource Name (ARN) of the destination Lambda function.
                        - **RoleARN** *(string) --* 
                          The ARN of the IAM role that Kinesis Data Analytics can assume to write to the destination function.
                          .. note::
                            Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **DestinationSchema** *(dict) --* 
                        The data format used for writing data to the destination.
                        - **RecordFormatType** *(string) --* 
                          Specifies the format of the records on the output stream.
                  - **ReferenceDataSourceDescriptions** *(list) --* 
                    The array of  ReferenceDataSourceDescription objects describing the reference data sources used by the application.
                    - *(dict) --* 
                      For an SQL-based Amazon Kinesis Data Analytics application, describes the reference data source configured for an application.
                      - **ReferenceId** *(string) --* 
                        The ID of the reference data source. This is the ID that Kinesis Data Analytics assigns when you add the reference data source to your application using the  CreateApplication or  UpdateApplication operation.
                      - **TableName** *(string) --* 
                        The in-application table name created by the specific reference data source configuration.
                      - **S3ReferenceDataSourceDescription** *(dict) --* 
                        Provides the Amazon S3 bucket name, the object key name that contains the reference data. 
                        - **BucketARN** *(string) --* 
                          The Amazon Resource Name (ARN) of the S3 bucket.
                        - **FileKey** *(string) --* 
                          Amazon S3 object key name.
                        - **ReferenceRoleARN** *(string) --* 
                          The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon S3 object on your behalf to populate the in-application reference table. 
                          .. note::
                            Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **ReferenceSchema** *(dict) --* 
                        Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.
                        - **RecordFormat** *(dict) --* 
                          Specifies the format of the records on the streaming source.
                          - **RecordFormatType** *(string) --* 
                            The type of record format.
                          - **MappingParameters** *(dict) --* 
                            When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
                            - **JSONMappingParameters** *(dict) --* 
                              Provides additional mapping information when JSON is the record format on the streaming source.
                              - **RecordRowPath** *(string) --* 
                                The path to the top-level parent that contains the records.
                            - **CSVMappingParameters** *(dict) --* 
                              Provides additional mapping information when the record format uses delimiters (for example, CSV).
                              - **RecordRowDelimiter** *(string) --* 
                                The row delimiter. For example, in a CSV format, *'\n'* is the typical row delimiter.
                              - **RecordColumnDelimiter** *(string) --* 
                                The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
                        - **RecordEncoding** *(string) --* 
                          Specifies the encoding of the records in the streaming source. For example, UTF-8.
                        - **RecordColumns** *(list) --* 
                          A list of ``RecordColumn`` objects. 
                          - *(dict) --* 
                            For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
                            Also used to describe the format of the reference data source.
                            - **Name** *(string) --* 
                              The name of the column that is created in the in-application input stream or reference table.
                            - **Mapping** *(string) --* 
                              A reference to the data element in the streaming input of the reference data source.
                            - **SqlType** *(string) --* 
                              The type of column created in the in-application input stream or reference table.
                - **ApplicationCodeConfigurationDescription** *(dict) --* 
                  The details about the application code for a Java-based Kinesis Data Analytics application.
                  - **CodeContentType** *(string) --* 
                    Specifies whether the code content is in text or zip format.
                  - **CodeContentDescription** *(dict) --* 
                    Describes details about the location and format of the application code.
                    - **TextContent** *(string) --* 
                      The text-format code
                    - **CodeMD5** *(string) --* 
                      The checksum that can be used to validate zip-format code.
                    - **CodeSize** *(integer) --* 
                      The size in bytes of the application code. Can be used to validate zip-format code.
                    - **S3ApplicationCodeLocationDescription** *(dict) --* 
                      The S3 bucket Amazon Resource Name (ARN), file key, and object version of the application code stored in Amazon S3.
                      - **BucketARN** *(string) --* 
                        The Amazon Resource Name (ARN) for the S3 bucket containing the application code.
                      - **FileKey** *(string) --* 
                        The file key for the object containing the application code.
                      - **ObjectVersion** *(string) --* 
                        The version of the object containing the application code.
                - **RunConfigurationDescription** *(dict) --* 
                  The details about the starting properties for a Kinesis Data Analytics application.
                  - **ApplicationRestoreConfigurationDescription** *(dict) --* 
                    Describes the restore behavior of a restarting application.
                    - **ApplicationRestoreType** *(string) --* 
                      Specifies how the application should be restored.
                    - **SnapshotName** *(string) --* 
                      The identifier of an existing snapshot of application state to use to restart an application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is specified for the ``ApplicationRestoreType`` .
                - **FlinkApplicationConfigurationDescription** *(dict) --* 
                  The details about a Java-based Kinesis Data Analytics application.
                  - **CheckpointConfigurationDescription** *(dict) --* 
                    Describes an application's checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance.
                    - **ConfigurationType** *(string) --* 
                      Describes whether the application uses the default checkpointing behavior in Kinesis Data Analytics.
                    - **CheckpointingEnabled** *(boolean) --* 
                      Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics application.
                    - **CheckpointInterval** *(integer) --* 
                      Describes the interval in milliseconds between checkpoint operations.
                    - **MinPauseBetweenCheckpoints** *(integer) --* 
                      Describes the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start.
                  - **MonitoringConfigurationDescription** *(dict) --* 
                    Describes configuration parameters for Amazon CloudWatch logging for an application.
                    - **ConfigurationType** *(string) --* 
                      Describes whether to use the default CloudWatch logging configuration for an application.
                    - **MetricsLevel** *(string) --* 
                      Describes the granularity of the CloudWatch Logs for an application.
                    - **LogLevel** *(string) --* 
                      Describes the verbosity of the CloudWatch Logs for an application.
                  - **ParallelismConfigurationDescription** *(dict) --* 
                    Describes parameters for how an application executes multiple tasks simultaneously.
                    - **ConfigurationType** *(string) --* 
                      Describes whether the application uses the default parallelism for the Kinesis Data Analytics service. 
                    - **Parallelism** *(integer) --* 
                      Describes the initial number of parallel tasks that a Java-based Kinesis Data Analytics application can perform. 
                    - **ParallelismPerKPU** *(integer) --* 
                      Describes the number of parallel tasks that a Java-based Kinesis Data Analytics application can perform per Kinesis Processing Unit (KPU) used by the application.
                    - **CurrentParallelism** *(integer) --* 
                      Describes the current number of parallel tasks that a Java-based Kinesis Data Analytics application can perform.
                    - **AutoScalingEnabled** *(boolean) --* 
                      Describes whether the Kinesis Data Analytics service can increase the parallelism of the application in response to increased throughput.
                  - **JobPlanDescription** *(string) --* 
                    The job plan for an application. For more information about the job plan, see `Jobs and Scheduling <https://ci.apache.org/projects/flink/flink-docs-stable/internals/job_scheduling.html>`__ in the `Apache Flink Documentation <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ . To retrieve the job plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails parameter of the  DescribeApplication operation.
                - **EnvironmentPropertyDescriptions** *(dict) --* 
                  Describes execution properties for a Java-based Kinesis Data Analytics application.
                  - **PropertyGroupDescriptions** *(list) --* 
                    Describes the execution property groups.
                    - *(dict) --* 
                      Property key-value pairs passed into a Java-based Kinesis Data Analytics application.
                      - **PropertyGroupId** *(string) --* 
                        Describes the key of an application execution property key-value pair.
                      - **PropertyMap** *(dict) --* 
                        Describes the value of an application execution property key-value pair.
                        - *(string) --* 
                          - *(string) --* 
                - **ApplicationSnapshotConfigurationDescription** *(dict) --* 
                  Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.
                  - **SnapshotsEnabled** *(boolean) --* 
                    Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.
              - **CloudWatchLoggingOptionDescriptions** *(list) --* 
                Describes the application Amazon CloudWatch logging options.
                - *(dict) --* 
                  Describes the Amazon CloudWatch logging option.
                  - **CloudWatchLoggingOptionId** *(string) --* 
                    The ID of the CloudWatch logging option description.
                  - **LogStreamARN** *(string) --* 
                    The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.
                  - **RoleARN** *(string) --* 
                    The IAM ARN of the role to use to send application messages. 
                    .. note::
                      Provided for backward compatibility. Applications created with the current API version have an application-level service execution role rather than a resource-level role.
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The name of your application (for example, ``sample-app`` ).
        :type ApplicationDescription: string
        :param ApplicationDescription:
          A summary description of the application.
        :type RuntimeEnvironment: string
        :param RuntimeEnvironment: **[REQUIRED]**
          The runtime environment for the application (``SQL-1.0`` or ``JAVA-8-FLINK-1.5`` ).
        :type ServiceExecutionRole: string
        :param ServiceExecutionRole: **[REQUIRED]**
          The IAM role used by the application to access Kinesis data streams, Kinesis Data Firehose delivery streams, Amazon S3 objects, and other external resources.
        :type ApplicationConfiguration: dict
        :param ApplicationConfiguration:
          Use this parameter to configure the application.
          - **SqlApplicationConfiguration** *(dict) --*
            The creation and update parameters for an SQL-based Kinesis Data Analytics application.
            - **Inputs** *(list) --*
              The array of  Input objects describing the input streams used by the application.
              - *(dict) --*
                When you configure the application input for an SQL-based Amazon Kinesis Data Analytics application, you specify the streaming source, the in-application stream name that is created, and the mapping between the two.
                - **NamePrefix** *(string) --* **[REQUIRED]**
                  The name prefix to use when creating an in-application stream. Suppose that you specify a prefix \"``MyInApplicationStream`` .\" Kinesis Data Analytics then creates one or more (as per the ``InputParallelism`` count you specified) in-application streams with the names \"``MyInApplicationStream_001`` ,\" \"``MyInApplicationStream_002`` ,\" and so on.
                - **InputProcessingConfiguration** *(dict) --*
                  The  InputProcessingConfiguration for the input. An input processor transforms records as they are received from the stream, before the application\'s SQL code executes. Currently, the only input processing configuration available is  InputLambdaProcessor .
                  - **InputLambdaProcessor** *(dict) --* **[REQUIRED]**
                    The  InputLambdaProcessor that is used to preprocess the records in the stream before being processed by your application code.
                    - **ResourceARN** *(string) --* **[REQUIRED]**
                      The ARN of the AWS Lambda function that operates on records in the stream.
                - **KinesisStreamsInput** *(dict) --*
                  If the streaming source is an Amazon Kinesis data stream, identifies the stream\'s Amazon Resource Name (ARN).
                  - **ResourceARN** *(string) --* **[REQUIRED]**
                    The ARN of the input Kinesis data stream to read.
                - **KinesisFirehoseInput** *(dict) --*
                  If the streaming source is an Amazon Kinesis Data Firehose delivery stream, identifies the delivery stream\'s ARN.
                  - **ResourceARN** *(string) --* **[REQUIRED]**
                    The Amazon Resource Name (ARN) of the delivery stream.
                - **InputParallelism** *(dict) --*
                  Describes the number of in-application streams to create.
                  - **Count** *(integer) --*
                    The number of in-application streams to create.
                - **InputSchema** *(dict) --* **[REQUIRED]**
                  Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.
                  Also used to describe the format of the reference data source.
                  - **RecordFormat** *(dict) --* **[REQUIRED]**
                    Specifies the format of the records on the streaming source.
                    - **RecordFormatType** *(string) --* **[REQUIRED]**
                      The type of record format.
                    - **MappingParameters** *(dict) --*
                      When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
                      - **JSONMappingParameters** *(dict) --*
                        Provides additional mapping information when JSON is the record format on the streaming source.
                        - **RecordRowPath** *(string) --* **[REQUIRED]**
                          The path to the top-level parent that contains the records.
                      - **CSVMappingParameters** *(dict) --*
                        Provides additional mapping information when the record format uses delimiters (for example, CSV).
                        - **RecordRowDelimiter** *(string) --* **[REQUIRED]**
                          The row delimiter. For example, in a CSV format, *\'\n\'* is the typical row delimiter.
                        - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**
                          The column delimiter. For example, in a CSV format, a comma (\",\") is the typical column delimiter.
                  - **RecordEncoding** *(string) --*
                    Specifies the encoding of the records in the streaming source. For example, UTF-8.
                  - **RecordColumns** *(list) --* **[REQUIRED]**
                    A list of ``RecordColumn`` objects.
                    - *(dict) --*
                      For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
                      Also used to describe the format of the reference data source.
                      - **Name** *(string) --* **[REQUIRED]**
                        The name of the column that is created in the in-application input stream or reference table.
                      - **Mapping** *(string) --*
                        A reference to the data element in the streaming input of the reference data source.
                      - **SqlType** *(string) --* **[REQUIRED]**
                        The type of column created in the in-application input stream or reference table.
            - **Outputs** *(list) --*
              The array of  Output objects describing the destination streams used by the application.
              - *(dict) --*
                Describes an SQL-based Amazon Kinesis Data Analytics application\'s output configuration, in which you identify an in-application stream and a destination where you want the in-application stream data to be written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.
                - **Name** *(string) --* **[REQUIRED]**
                  The name of the in-application stream.
                - **KinesisStreamsOutput** *(dict) --*
                  Identifies an Amazon Kinesis data stream as the destination.
                  - **ResourceARN** *(string) --* **[REQUIRED]**
                    The ARN of the destination Kinesis data stream to write to.
                - **KinesisFirehoseOutput** *(dict) --*
                  Identifies an Amazon Kinesis Data Firehose delivery stream as the destination.
                  - **ResourceARN** *(string) --* **[REQUIRED]**
                    The ARN of the destination delivery stream to write to.
                - **LambdaOutput** *(dict) --*
                  Identifies an AWS Lambda function as the destination.
                  - **ResourceARN** *(string) --* **[REQUIRED]**
                    The Amazon Resource Name (ARN) of the destination Lambda function to write to.
                - **DestinationSchema** *(dict) --* **[REQUIRED]**
                  Describes the data format when records are written to the destination.
                  - **RecordFormatType** *(string) --* **[REQUIRED]**
                    Specifies the format of the records on the output stream.
            - **ReferenceDataSources** *(list) --*
              The array of  ReferenceDataSource objects describing the reference data sources used by the application.
              - *(dict) --*
                For an SQL-based Amazon Kinesis Data Analytics application, describes the reference data source by providing the source information (Amazon S3 bucket name and object key name), the resulting in-application table name that is created, and the necessary schema to map the data elements in the Amazon S3 object to the in-application table.
                - **TableName** *(string) --* **[REQUIRED]**
                  The name of the in-application table to create.
                - **S3ReferenceDataSource** *(dict) --*
                  Identifies the S3 bucket and object that contains the reference data. A Kinesis Data Analytics application loads reference data only once. If the data changes, you call the  UpdateApplication operation to trigger reloading of data into your application.
                  - **BucketARN** *(string) --*
                    The Amazon Resource Name (ARN) of the S3 bucket.
                  - **FileKey** *(string) --*
                    The object key name containing the reference data.
                - **ReferenceSchema** *(dict) --* **[REQUIRED]**
                  Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.
                  - **RecordFormat** *(dict) --* **[REQUIRED]**
                    Specifies the format of the records on the streaming source.
                    - **RecordFormatType** *(string) --* **[REQUIRED]**
                      The type of record format.
                    - **MappingParameters** *(dict) --*
                      When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
                      - **JSONMappingParameters** *(dict) --*
                        Provides additional mapping information when JSON is the record format on the streaming source.
                        - **RecordRowPath** *(string) --* **[REQUIRED]**
                          The path to the top-level parent that contains the records.
                      - **CSVMappingParameters** *(dict) --*
                        Provides additional mapping information when the record format uses delimiters (for example, CSV).
                        - **RecordRowDelimiter** *(string) --* **[REQUIRED]**
                          The row delimiter. For example, in a CSV format, *\'\n\'* is the typical row delimiter.
                        - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**
                          The column delimiter. For example, in a CSV format, a comma (\",\") is the typical column delimiter.
                  - **RecordEncoding** *(string) --*
                    Specifies the encoding of the records in the streaming source. For example, UTF-8.
                  - **RecordColumns** *(list) --* **[REQUIRED]**
                    A list of ``RecordColumn`` objects.
                    - *(dict) --*
                      For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
                      Also used to describe the format of the reference data source.
                      - **Name** *(string) --* **[REQUIRED]**
                        The name of the column that is created in the in-application input stream or reference table.
                      - **Mapping** *(string) --*
                        A reference to the data element in the streaming input of the reference data source.
                      - **SqlType** *(string) --* **[REQUIRED]**
                        The type of column created in the in-application input stream or reference table.
          - **FlinkApplicationConfiguration** *(dict) --*
            The creation and update parameters for a Java-based Kinesis Data Analytics application.
            - **CheckpointConfiguration** *(dict) --*
              Describes an application\'s checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance. For more information, see `Checkpoints for Fault Tolerance <https://ci.apache.org/projects/flink/flink-docs-release-1.6/concepts/programming-model.html#checkpoints-for-fault-tolerance>`__ in the `Apache Flink Documentation <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ .
              - **ConfigurationType** *(string) --* **[REQUIRED]**
                Describes whether the application uses Amazon Kinesis Data Analytics\' default checkpointing behavior.
              - **CheckpointingEnabled** *(boolean) --*
                Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics application.
              - **CheckpointInterval** *(integer) --*
                Describes the interval in milliseconds between checkpoint operations.
              - **MinPauseBetweenCheckpoints** *(integer) --*
                Describes the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start. If a checkpoint operation takes longer than the ``CheckpointInterval`` , the application otherwise performs continual checkpoint operations. For more information, see `Tuning Checkpointing <https://ci.apache.org/projects/flink/flink-docs-stable/ops/state/large_state_tuning.html#tuning-checkpointing>`__ in the `Apache Flink Documentation <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ .
            - **MonitoringConfiguration** *(dict) --*
              Describes configuration parameters for Amazon CloudWatch logging for an application.
              - **ConfigurationType** *(string) --* **[REQUIRED]**
                Describes whether to use the default CloudWatch logging configuration for an application.
              - **MetricsLevel** *(string) --*
                Describes the granularity of the CloudWatch Logs for an application.
              - **LogLevel** *(string) --*
                Describes the verbosity of the CloudWatch Logs for an application.
            - **ParallelismConfiguration** *(dict) --*
              Describes parameters for how an application executes multiple tasks simultaneously.
              - **ConfigurationType** *(string) --* **[REQUIRED]**
                Describes whether the application uses the default parallelism for the Kinesis Data Analytics service.
              - **Parallelism** *(integer) --*
                Describes the initial number of parallel tasks that a Java-based Kinesis Data Analytics application can perform. The Kinesis Data Analytics service can increase this number automatically if  ParallelismConfiguration$AutoScalingEnabled is set to ``true`` .
              - **ParallelismPerKPU** *(integer) --*
                Describes the number of parallel tasks that a Java-based Kinesis Data Analytics application can perform per Kinesis Processing Unit (KPU) used by the application. For more information about KPUs, see `Amazon Kinesis Data Analytics Pricing <http://aws.amazon.com/kinesis/data-analytics/pricing/>`__ .
              - **AutoScalingEnabled** *(boolean) --*
                Describes whether the Kinesis Data Analytics service can increase the parallelism of the application in response to increased throughput.
          - **EnvironmentProperties** *(dict) --*
            Describes execution properties for a Java-based Kinesis Data Analytics application.
            - **PropertyGroups** *(list) --* **[REQUIRED]**
              Describes the execution property groups.
              - *(dict) --*
                Property key-value pairs passed into a Java-based Kinesis Data Analytics application.
                - **PropertyGroupId** *(string) --* **[REQUIRED]**
                  Describes the key of an application execution property key-value pair.
                - **PropertyMap** *(dict) --* **[REQUIRED]**
                  Describes the value of an application execution property key-value pair.
                  - *(string) --*
                    - *(string) --*
          - **ApplicationCodeConfiguration** *(dict) --* **[REQUIRED]**
            The code location and type parameters for a Java-based Kinesis Data Analytics application.
            - **CodeContent** *(dict) --*
              The location and type of the application code.
              - **TextContent** *(string) --*
                The text-format code for a Java-based Kinesis Data Analytics application.
              - **ZipFileContent** *(bytes) --*
                The zip-format code for a Java-based Kinesis Data Analytics application.
              - **S3ContentLocation** *(dict) --*
                Information about the Amazon S3 bucket containing the application code.
                - **BucketARN** *(string) --* **[REQUIRED]**
                  The Amazon Resource Name (ARN) for the S3 bucket containing the application code.
                - **FileKey** *(string) --* **[REQUIRED]**
                  The file key for the object containing the application code.
                - **ObjectVersion** *(string) --*
                  The version of the object containing the application code.
            - **CodeContentType** *(string) --* **[REQUIRED]**
              Specifies whether the code content is in text or zip format.
          - **ApplicationSnapshotConfiguration** *(dict) --*
            Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.
            - **SnapshotsEnabled** *(boolean) --* **[REQUIRED]**
              Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.
        :type CloudWatchLoggingOptions: list
        :param CloudWatchLoggingOptions:
          Use this parameter to configure an Amazon CloudWatch log stream to monitor application configuration errors.
          - *(dict) --*
            Provides a description of Amazon CloudWatch logging options, including the log stream Amazon Resource Name (ARN).
            - **LogStreamARN** *(string) --* **[REQUIRED]**
              The ARN of the CloudWatch log to receive application messages.
        :rtype: dict
        :returns:
        """
        pass

    def create_application_snapshot(self, ApplicationName: str, SnapshotName: str) -> Dict:
        """
        Creates a snapshot of the application's state data.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/CreateApplicationSnapshot>`_
        
        **Request Syntax**
        ::
          response = client.create_application_snapshot(
              ApplicationName='string',
              SnapshotName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The name of an existing application
        :type SnapshotName: string
        :param SnapshotName: **[REQUIRED]**
          An identifier for the application snapshot.
        :rtype: dict
        :returns:
        """
        pass

    def delete_application(self, ApplicationName: str, CreateTimestamp: datetime) -> Dict:
        """
        Deletes the specified application. Kinesis Data Analytics halts application execution and deletes the application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/DeleteApplication>`_
        
        **Request Syntax**
        ::
          response = client.delete_application(
              ApplicationName='string',
              CreateTimestamp=datetime(2015, 1, 1)
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The name of the application to delete.
        :type CreateTimestamp: datetime
        :param CreateTimestamp: **[REQUIRED]**
          Use the ``DescribeApplication`` operation to get this value.
        :rtype: dict
        :returns:
        """
        pass

    def delete_application_cloud_watch_logging_option(self, ApplicationName: str, CurrentApplicationVersionId: int, CloudWatchLoggingOptionId: str) -> Dict:
        """
        Deletes an Amazon CloudWatch log stream from an Amazon Kinesis Data Analytics application. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/DeleteApplicationCloudWatchLoggingOption>`_
        
        **Request Syntax**
        ::
          response = client.delete_application_cloud_watch_logging_option(
              ApplicationName='string',
              CurrentApplicationVersionId=123,
              CloudWatchLoggingOptionId='string'
          )
        
        **Response Syntax**
        ::
            {
                'ApplicationARN': 'string',
                'ApplicationVersionId': 123,
                'CloudWatchLoggingOptionDescriptions': [
                    {
                        'CloudWatchLoggingOptionId': 'string',
                        'LogStreamARN': 'string',
                        'RoleARN': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ApplicationARN** *(string) --* 
              The application's Amazon Resource Name (ARN).
            - **ApplicationVersionId** *(integer) --* 
              The version ID of the application. Kinesis Data Analytics updates the ``ApplicationVersionId`` each time you change the CloudWatch logging options.
            - **CloudWatchLoggingOptionDescriptions** *(list) --* 
              The descriptions of the remaining CloudWatch logging options for the application.
              - *(dict) --* 
                Describes the Amazon CloudWatch logging option.
                - **CloudWatchLoggingOptionId** *(string) --* 
                  The ID of the CloudWatch logging option description.
                - **LogStreamARN** *(string) --* 
                  The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.
                - **RoleARN** *(string) --* 
                  The IAM ARN of the role to use to send application messages. 
                  .. note::
                    Provided for backward compatibility. Applications created with the current API version have an application-level service execution role rather than a resource-level role.
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The application name.
        :type CurrentApplicationVersionId: integer
        :param CurrentApplicationVersionId: **[REQUIRED]**
          The version ID of the application. You can retrieve the application version ID using  DescribeApplication .
        :type CloudWatchLoggingOptionId: string
        :param CloudWatchLoggingOptionId: **[REQUIRED]**
          The ``CloudWatchLoggingOptionId`` of the Amazon CloudWatch logging option to delete. You can get the ``CloudWatchLoggingOptionId`` by using the  DescribeApplication operation.
        :rtype: dict
        :returns:
        """
        pass

    def delete_application_input_processing_configuration(self, ApplicationName: str, CurrentApplicationVersionId: int, InputId: str) -> Dict:
        """
        Deletes an  InputProcessingConfiguration from an input.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/DeleteApplicationInputProcessingConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.delete_application_input_processing_configuration(
              ApplicationName='string',
              CurrentApplicationVersionId=123,
              InputId='string'
          )
        
        **Response Syntax**
        ::
            {
                'ApplicationARN': 'string',
                'ApplicationVersionId': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ApplicationARN** *(string) --* 
              The Amazon Resource Name (ARN) of the application.
            - **ApplicationVersionId** *(integer) --* 
              The current application version ID.
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The name of the application.
        :type CurrentApplicationVersionId: integer
        :param CurrentApplicationVersionId: **[REQUIRED]**
          The application version. You can use the  DescribeApplication operation to get the current application version. If the version specified is not the current version, the ``ConcurrentModificationException`` is returned.
        :type InputId: string
        :param InputId: **[REQUIRED]**
          The ID of the input configuration from which to delete the input processing configuration. You can get a list of the input IDs for an application by using the  DescribeApplication operation.
        :rtype: dict
        :returns:
        """
        pass

    def delete_application_output(self, ApplicationName: str, CurrentApplicationVersionId: int, OutputId: str) -> Dict:
        """
        Deletes the output destination configuration from your SQL-based Amazon Kinesis Data Analytics application's configuration. Kinesis Data Analytics will no longer write data from the corresponding in-application stream to the external output destination.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/DeleteApplicationOutput>`_
        
        **Request Syntax**
        ::
          response = client.delete_application_output(
              ApplicationName='string',
              CurrentApplicationVersionId=123,
              OutputId='string'
          )
        
        **Response Syntax**
        ::
            {
                'ApplicationARN': 'string',
                'ApplicationVersionId': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ApplicationARN** *(string) --* 
              The application Amazon Resource Name (ARN).
            - **ApplicationVersionId** *(integer) --* 
              The current application version ID.
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The application name.
        :type CurrentApplicationVersionId: integer
        :param CurrentApplicationVersionId: **[REQUIRED]**
          The application version. You can use the  DescribeApplication operation to get the current application version. If the version specified is not the current version, the ``ConcurrentModificationException`` is returned.
        :type OutputId: string
        :param OutputId: **[REQUIRED]**
          The ID of the configuration to delete. Each output configuration that is added to the application (either when the application is created or later) using the  AddApplicationOutput operation has a unique ID. You need to provide the ID to uniquely identify the output configuration that you want to delete from the application configuration. You can use the  DescribeApplication operation to get the specific ``OutputId`` .
        :rtype: dict
        :returns:
        """
        pass

    def delete_application_reference_data_source(self, ApplicationName: str, CurrentApplicationVersionId: int, ReferenceId: str) -> Dict:
        """
        Deletes a reference data source configuration from the specified SQL-based Amazon Kinesis Data Analytics application's configuration.
        If the application is running, Kinesis Data Analytics immediately removes the in-application table that you created using the  AddApplicationReferenceDataSource operation. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/DeleteApplicationReferenceDataSource>`_
        
        **Request Syntax**
        ::
          response = client.delete_application_reference_data_source(
              ApplicationName='string',
              CurrentApplicationVersionId=123,
              ReferenceId='string'
          )
        
        **Response Syntax**
        ::
            {
                'ApplicationARN': 'string',
                'ApplicationVersionId': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ApplicationARN** *(string) --* 
              The application Amazon Resource Name (ARN).
            - **ApplicationVersionId** *(integer) --* 
              The updated version ID of the application.
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The name of an existing application.
        :type CurrentApplicationVersionId: integer
        :param CurrentApplicationVersionId: **[REQUIRED]**
          The current application version. You can use the  DescribeApplication operation to get the current application version. If the version specified is not the current version, the ``ConcurrentModificationException`` is returned.
        :type ReferenceId: string
        :param ReferenceId: **[REQUIRED]**
          The ID of the reference data source. When you add a reference data source to your application using the  AddApplicationReferenceDataSource , Kinesis Data Analytics assigns an ID. You can use the  DescribeApplication operation to get the reference ID.
        :rtype: dict
        :returns:
        """
        pass

    def delete_application_snapshot(self, ApplicationName: str, SnapshotName: str, SnapshotCreationTimestamp: datetime) -> Dict:
        """
        Deletes a snapshot of application state.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/DeleteApplicationSnapshot>`_
        
        **Request Syntax**
        ::
          response = client.delete_application_snapshot(
              ApplicationName='string',
              SnapshotName='string',
              SnapshotCreationTimestamp=datetime(2015, 1, 1)
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The name of an existing application.
        :type SnapshotName: string
        :param SnapshotName: **[REQUIRED]**
          The identifier for the snapshot delete.
        :type SnapshotCreationTimestamp: datetime
        :param SnapshotCreationTimestamp: **[REQUIRED]**
          The creation timestamp of the application snapshot to delete. You can retrieve this value using or .
        :rtype: dict
        :returns:
        """
        pass

    def describe_application(self, ApplicationName: str, IncludeAdditionalDetails: bool = None) -> Dict:
        """
        Returns information about a specific Amazon Kinesis Data Analytics application.
        If you want to retrieve a list of all applications in your account, use the  ListApplications operation.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/DescribeApplication>`_
        
        **Request Syntax**
        ::
          response = client.describe_application(
              ApplicationName='string',
              IncludeAdditionalDetails=True|False
          )
        
        **Response Syntax**
        ::
            {
                'ApplicationDetail': {
                    'ApplicationARN': 'string',
                    'ApplicationDescription': 'string',
                    'ApplicationName': 'string',
                    'RuntimeEnvironment': 'SQL-1_0'|'FLINK-1_6',
                    'ServiceExecutionRole': 'string',
                    'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING',
                    'ApplicationVersionId': 123,
                    'CreateTimestamp': datetime(2015, 1, 1),
                    'LastUpdateTimestamp': datetime(2015, 1, 1),
                    'ApplicationConfigurationDescription': {
                        'SqlApplicationConfigurationDescription': {
                            'InputDescriptions': [
                                {
                                    'InputId': 'string',
                                    'NamePrefix': 'string',
                                    'InAppStreamNames': [
                                        'string',
                                    ],
                                    'InputProcessingConfigurationDescription': {
                                        'InputLambdaProcessorDescription': {
                                            'ResourceARN': 'string',
                                            'RoleARN': 'string'
                                        }
                                    },
                                    'KinesisStreamsInputDescription': {
                                        'ResourceARN': 'string',
                                        'RoleARN': 'string'
                                    },
                                    'KinesisFirehoseInputDescription': {
                                        'ResourceARN': 'string',
                                        'RoleARN': 'string'
                                    },
                                    'InputSchema': {
                                        'RecordFormat': {
                                            'RecordFormatType': 'JSON'|'CSV',
                                            'MappingParameters': {
                                                'JSONMappingParameters': {
                                                    'RecordRowPath': 'string'
                                                },
                                                'CSVMappingParameters': {
                                                    'RecordRowDelimiter': 'string',
                                                    'RecordColumnDelimiter': 'string'
                                                }
                                            }
                                        },
                                        'RecordEncoding': 'string',
                                        'RecordColumns': [
                                            {
                                                'Name': 'string',
                                                'Mapping': 'string',
                                                'SqlType': 'string'
                                            },
                                        ]
                                    },
                                    'InputParallelism': {
                                        'Count': 123
                                    },
                                    'InputStartingPositionConfiguration': {
                                        'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
                                    }
                                },
                            ],
                            'OutputDescriptions': [
                                {
                                    'OutputId': 'string',
                                    'Name': 'string',
                                    'KinesisStreamsOutputDescription': {
                                        'ResourceARN': 'string',
                                        'RoleARN': 'string'
                                    },
                                    'KinesisFirehoseOutputDescription': {
                                        'ResourceARN': 'string',
                                        'RoleARN': 'string'
                                    },
                                    'LambdaOutputDescription': {
                                        'ResourceARN': 'string',
                                        'RoleARN': 'string'
                                    },
                                    'DestinationSchema': {
                                        'RecordFormatType': 'JSON'|'CSV'
                                    }
                                },
                            ],
                            'ReferenceDataSourceDescriptions': [
                                {
                                    'ReferenceId': 'string',
                                    'TableName': 'string',
                                    'S3ReferenceDataSourceDescription': {
                                        'BucketARN': 'string',
                                        'FileKey': 'string',
                                        'ReferenceRoleARN': 'string'
                                    },
                                    'ReferenceSchema': {
                                        'RecordFormat': {
                                            'RecordFormatType': 'JSON'|'CSV',
                                            'MappingParameters': {
                                                'JSONMappingParameters': {
                                                    'RecordRowPath': 'string'
                                                },
                                                'CSVMappingParameters': {
                                                    'RecordRowDelimiter': 'string',
                                                    'RecordColumnDelimiter': 'string'
                                                }
                                            }
                                        },
                                        'RecordEncoding': 'string',
                                        'RecordColumns': [
                                            {
                                                'Name': 'string',
                                                'Mapping': 'string',
                                                'SqlType': 'string'
                                            },
                                        ]
                                    }
                                },
                            ]
                        },
                        'ApplicationCodeConfigurationDescription': {
                            'CodeContentType': 'PLAINTEXT'|'ZIPFILE',
                            'CodeContentDescription': {
                                'TextContent': 'string',
                                'CodeMD5': 'string',
                                'CodeSize': 123,
                                'S3ApplicationCodeLocationDescription': {
                                    'BucketARN': 'string',
                                    'FileKey': 'string',
                                    'ObjectVersion': 'string'
                                }
                            }
                        },
                        'RunConfigurationDescription': {
                            'ApplicationRestoreConfigurationDescription': {
                                'ApplicationRestoreType': 'SKIP_RESTORE_FROM_SNAPSHOT'|'RESTORE_FROM_LATEST_SNAPSHOT'|'RESTORE_FROM_CUSTOM_SNAPSHOT',
                                'SnapshotName': 'string'
                            }
                        },
                        'FlinkApplicationConfigurationDescription': {
                            'CheckpointConfigurationDescription': {
                                'ConfigurationType': 'DEFAULT'|'CUSTOM',
                                'CheckpointingEnabled': True|False,
                                'CheckpointInterval': 123,
                                'MinPauseBetweenCheckpoints': 123
                            },
                            'MonitoringConfigurationDescription': {
                                'ConfigurationType': 'DEFAULT'|'CUSTOM',
                                'MetricsLevel': 'APPLICATION'|'TASK'|'OPERATOR'|'PARALLELISM',
                                'LogLevel': 'INFO'|'WARN'|'ERROR'|'DEBUG'
                            },
                            'ParallelismConfigurationDescription': {
                                'ConfigurationType': 'DEFAULT'|'CUSTOM',
                                'Parallelism': 123,
                                'ParallelismPerKPU': 123,
                                'CurrentParallelism': 123,
                                'AutoScalingEnabled': True|False
                            },
                            'JobPlanDescription': 'string'
                        },
                        'EnvironmentPropertyDescriptions': {
                            'PropertyGroupDescriptions': [
                                {
                                    'PropertyGroupId': 'string',
                                    'PropertyMap': {
                                        'string': 'string'
                                    }
                                },
                            ]
                        },
                        'ApplicationSnapshotConfigurationDescription': {
                            'SnapshotsEnabled': True|False
                        }
                    },
                    'CloudWatchLoggingOptionDescriptions': [
                        {
                            'CloudWatchLoggingOptionId': 'string',
                            'LogStreamARN': 'string',
                            'RoleARN': 'string'
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ApplicationDetail** *(dict) --* 
              Provides a description of the application, such as the application's Amazon Resource Name (ARN), status, and latest version.
              - **ApplicationARN** *(string) --* 
                The ARN of the application.
              - **ApplicationDescription** *(string) --* 
                The description of the application.
              - **ApplicationName** *(string) --* 
                The name of the application.
              - **RuntimeEnvironment** *(string) --* 
                The runtime environment for the application (``SQL-1.0`` or ``JAVA-8-FLINK-1.5`` ).
              - **ServiceExecutionRole** *(string) --* 
                Specifies the IAM role that the application uses to access external resources.
              - **ApplicationStatus** *(string) --* 
                The status of the application.
              - **ApplicationVersionId** *(integer) --* 
                Provides the current application version. Kinesis Data Analytics updates the ``ApplicationVersionId`` each time you update the application.
              - **CreateTimestamp** *(datetime) --* 
                The current timestamp when the application was created.
              - **LastUpdateTimestamp** *(datetime) --* 
                The current timestamp when the application was last updated.
              - **ApplicationConfigurationDescription** *(dict) --* 
                Provides details about the application's SQL or Java code and starting parameters.
                - **SqlApplicationConfigurationDescription** *(dict) --* 
                  The details about inputs, outputs, and reference data sources for an SQL-based Kinesis Data Analytics application.
                  - **InputDescriptions** *(list) --* 
                    The array of  InputDescription objects describing the input streams used by the application.
                    - *(dict) --* 
                      Describes the application input configuration for an SQL-based Amazon Kinesis Data Analytics application. 
                      - **InputId** *(string) --* 
                        The input ID that is associated with the application input. This is the ID that Kinesis Data Analytics assigns to each input configuration that you add to your application. 
                      - **NamePrefix** *(string) --* 
                        The in-application name prefix.
                      - **InAppStreamNames** *(list) --* 
                        Returns the in-application stream names that are mapped to the stream source. 
                        - *(string) --* 
                      - **InputProcessingConfigurationDescription** *(dict) --* 
                        The description of the preprocessor that executes on records in this input before the application's code is run. 
                        - **InputLambdaProcessorDescription** *(dict) --* 
                          Provides configuration information about the associated  InputLambdaProcessorDescription  
                          - **ResourceARN** *(string) --* 
                            The ARN of the AWS Lambda function that is used to preprocess the records in the stream.
                          - **RoleARN** *(string) --* 
                            The ARN of the IAM role that is used to access the AWS Lambda function.
                            .. note::
                              Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **KinesisStreamsInputDescription** *(dict) --* 
                        If a Kinesis data stream is configured as a streaming source, provides the Kinesis data stream's Amazon Resource Name (ARN). 
                        - **ResourceARN** *(string) --* 
                          The Amazon Resource Name (ARN) of the Kinesis data stream.
                        - **RoleARN** *(string) --* 
                          The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.
                          .. note::
                            Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **KinesisFirehoseInputDescription** *(dict) --* 
                        If a Kinesis Data Firehose delivery stream is configured as a streaming source, provides the delivery stream's ARN. 
                        - **ResourceARN** *(string) --* 
                          The Amazon Resource Name (ARN) of the delivery stream.
                        - **RoleARN** *(string) --* 
                          The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.
                          .. note::
                            Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **InputSchema** *(dict) --* 
                        Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created. 
                        - **RecordFormat** *(dict) --* 
                          Specifies the format of the records on the streaming source.
                          - **RecordFormatType** *(string) --* 
                            The type of record format.
                          - **MappingParameters** *(dict) --* 
                            When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
                            - **JSONMappingParameters** *(dict) --* 
                              Provides additional mapping information when JSON is the record format on the streaming source.
                              - **RecordRowPath** *(string) --* 
                                The path to the top-level parent that contains the records.
                            - **CSVMappingParameters** *(dict) --* 
                              Provides additional mapping information when the record format uses delimiters (for example, CSV).
                              - **RecordRowDelimiter** *(string) --* 
                                The row delimiter. For example, in a CSV format, *'\n'* is the typical row delimiter.
                              - **RecordColumnDelimiter** *(string) --* 
                                The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
                        - **RecordEncoding** *(string) --* 
                          Specifies the encoding of the records in the streaming source. For example, UTF-8.
                        - **RecordColumns** *(list) --* 
                          A list of ``RecordColumn`` objects. 
                          - *(dict) --* 
                            For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
                            Also used to describe the format of the reference data source.
                            - **Name** *(string) --* 
                              The name of the column that is created in the in-application input stream or reference table.
                            - **Mapping** *(string) --* 
                              A reference to the data element in the streaming input of the reference data source.
                            - **SqlType** *(string) --* 
                              The type of column created in the in-application input stream or reference table.
                      - **InputParallelism** *(dict) --* 
                        Describes the configured parallelism (number of in-application streams mapped to the streaming source). 
                        - **Count** *(integer) --* 
                          The number of in-application streams to create.
                      - **InputStartingPositionConfiguration** *(dict) --* 
                        The point at which the application is configured to read from the input stream.
                        - **InputStartingPosition** *(string) --* 
                          The starting position on the stream.
                          * ``NOW`` - Start reading just after the most recent record in the stream, and start at the request timestamp that the customer issued. 
                          * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Data Firehose delivery stream. 
                          * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped reading. 
                  - **OutputDescriptions** *(list) --* 
                    The array of  OutputDescription objects describing the destination streams used by the application.
                    - *(dict) --* 
                      For an SQL-based Amazon Kinesis Data Analytics application, describes the application output configuration, which includes the in-application stream name and the destination where the stream data is written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream. 
                      - **OutputId** *(string) --* 
                        A unique identifier for the output configuration.
                      - **Name** *(string) --* 
                        The name of the in-application stream that is configured as output.
                      - **KinesisStreamsOutputDescription** *(dict) --* 
                        Describes the Kinesis data stream that is configured as the destination where output is written.
                        - **ResourceARN** *(string) --* 
                          The Amazon Resource Name (ARN) of the Kinesis data stream.
                        - **RoleARN** *(string) --* 
                          The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.
                          .. note::
                            Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **KinesisFirehoseOutputDescription** *(dict) --* 
                        Describes the Kinesis Data Firehose delivery stream that is configured as the destination where output is written.
                        - **ResourceARN** *(string) --* 
                          The Amazon Resource Name (ARN) of the delivery stream.
                        - **RoleARN** *(string) --* 
                          The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.
                          .. note::
                            Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **LambdaOutputDescription** *(dict) --* 
                        Describes the Lambda function that is configured as the destination where output is written.
                        - **ResourceARN** *(string) --* 
                          The Amazon Resource Name (ARN) of the destination Lambda function.
                        - **RoleARN** *(string) --* 
                          The ARN of the IAM role that Kinesis Data Analytics can assume to write to the destination function.
                          .. note::
                            Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **DestinationSchema** *(dict) --* 
                        The data format used for writing data to the destination.
                        - **RecordFormatType** *(string) --* 
                          Specifies the format of the records on the output stream.
                  - **ReferenceDataSourceDescriptions** *(list) --* 
                    The array of  ReferenceDataSourceDescription objects describing the reference data sources used by the application.
                    - *(dict) --* 
                      For an SQL-based Amazon Kinesis Data Analytics application, describes the reference data source configured for an application.
                      - **ReferenceId** *(string) --* 
                        The ID of the reference data source. This is the ID that Kinesis Data Analytics assigns when you add the reference data source to your application using the  CreateApplication or  UpdateApplication operation.
                      - **TableName** *(string) --* 
                        The in-application table name created by the specific reference data source configuration.
                      - **S3ReferenceDataSourceDescription** *(dict) --* 
                        Provides the Amazon S3 bucket name, the object key name that contains the reference data. 
                        - **BucketARN** *(string) --* 
                          The Amazon Resource Name (ARN) of the S3 bucket.
                        - **FileKey** *(string) --* 
                          Amazon S3 object key name.
                        - **ReferenceRoleARN** *(string) --* 
                          The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon S3 object on your behalf to populate the in-application reference table. 
                          .. note::
                            Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **ReferenceSchema** *(dict) --* 
                        Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.
                        - **RecordFormat** *(dict) --* 
                          Specifies the format of the records on the streaming source.
                          - **RecordFormatType** *(string) --* 
                            The type of record format.
                          - **MappingParameters** *(dict) --* 
                            When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
                            - **JSONMappingParameters** *(dict) --* 
                              Provides additional mapping information when JSON is the record format on the streaming source.
                              - **RecordRowPath** *(string) --* 
                                The path to the top-level parent that contains the records.
                            - **CSVMappingParameters** *(dict) --* 
                              Provides additional mapping information when the record format uses delimiters (for example, CSV).
                              - **RecordRowDelimiter** *(string) --* 
                                The row delimiter. For example, in a CSV format, *'\n'* is the typical row delimiter.
                              - **RecordColumnDelimiter** *(string) --* 
                                The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
                        - **RecordEncoding** *(string) --* 
                          Specifies the encoding of the records in the streaming source. For example, UTF-8.
                        - **RecordColumns** *(list) --* 
                          A list of ``RecordColumn`` objects. 
                          - *(dict) --* 
                            For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
                            Also used to describe the format of the reference data source.
                            - **Name** *(string) --* 
                              The name of the column that is created in the in-application input stream or reference table.
                            - **Mapping** *(string) --* 
                              A reference to the data element in the streaming input of the reference data source.
                            - **SqlType** *(string) --* 
                              The type of column created in the in-application input stream or reference table.
                - **ApplicationCodeConfigurationDescription** *(dict) --* 
                  The details about the application code for a Java-based Kinesis Data Analytics application.
                  - **CodeContentType** *(string) --* 
                    Specifies whether the code content is in text or zip format.
                  - **CodeContentDescription** *(dict) --* 
                    Describes details about the location and format of the application code.
                    - **TextContent** *(string) --* 
                      The text-format code
                    - **CodeMD5** *(string) --* 
                      The checksum that can be used to validate zip-format code.
                    - **CodeSize** *(integer) --* 
                      The size in bytes of the application code. Can be used to validate zip-format code.
                    - **S3ApplicationCodeLocationDescription** *(dict) --* 
                      The S3 bucket Amazon Resource Name (ARN), file key, and object version of the application code stored in Amazon S3.
                      - **BucketARN** *(string) --* 
                        The Amazon Resource Name (ARN) for the S3 bucket containing the application code.
                      - **FileKey** *(string) --* 
                        The file key for the object containing the application code.
                      - **ObjectVersion** *(string) --* 
                        The version of the object containing the application code.
                - **RunConfigurationDescription** *(dict) --* 
                  The details about the starting properties for a Kinesis Data Analytics application.
                  - **ApplicationRestoreConfigurationDescription** *(dict) --* 
                    Describes the restore behavior of a restarting application.
                    - **ApplicationRestoreType** *(string) --* 
                      Specifies how the application should be restored.
                    - **SnapshotName** *(string) --* 
                      The identifier of an existing snapshot of application state to use to restart an application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is specified for the ``ApplicationRestoreType`` .
                - **FlinkApplicationConfigurationDescription** *(dict) --* 
                  The details about a Java-based Kinesis Data Analytics application.
                  - **CheckpointConfigurationDescription** *(dict) --* 
                    Describes an application's checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance.
                    - **ConfigurationType** *(string) --* 
                      Describes whether the application uses the default checkpointing behavior in Kinesis Data Analytics.
                    - **CheckpointingEnabled** *(boolean) --* 
                      Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics application.
                    - **CheckpointInterval** *(integer) --* 
                      Describes the interval in milliseconds between checkpoint operations.
                    - **MinPauseBetweenCheckpoints** *(integer) --* 
                      Describes the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start.
                  - **MonitoringConfigurationDescription** *(dict) --* 
                    Describes configuration parameters for Amazon CloudWatch logging for an application.
                    - **ConfigurationType** *(string) --* 
                      Describes whether to use the default CloudWatch logging configuration for an application.
                    - **MetricsLevel** *(string) --* 
                      Describes the granularity of the CloudWatch Logs for an application.
                    - **LogLevel** *(string) --* 
                      Describes the verbosity of the CloudWatch Logs for an application.
                  - **ParallelismConfigurationDescription** *(dict) --* 
                    Describes parameters for how an application executes multiple tasks simultaneously.
                    - **ConfigurationType** *(string) --* 
                      Describes whether the application uses the default parallelism for the Kinesis Data Analytics service. 
                    - **Parallelism** *(integer) --* 
                      Describes the initial number of parallel tasks that a Java-based Kinesis Data Analytics application can perform. 
                    - **ParallelismPerKPU** *(integer) --* 
                      Describes the number of parallel tasks that a Java-based Kinesis Data Analytics application can perform per Kinesis Processing Unit (KPU) used by the application.
                    - **CurrentParallelism** *(integer) --* 
                      Describes the current number of parallel tasks that a Java-based Kinesis Data Analytics application can perform.
                    - **AutoScalingEnabled** *(boolean) --* 
                      Describes whether the Kinesis Data Analytics service can increase the parallelism of the application in response to increased throughput.
                  - **JobPlanDescription** *(string) --* 
                    The job plan for an application. For more information about the job plan, see `Jobs and Scheduling <https://ci.apache.org/projects/flink/flink-docs-stable/internals/job_scheduling.html>`__ in the `Apache Flink Documentation <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ . To retrieve the job plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails parameter of the  DescribeApplication operation.
                - **EnvironmentPropertyDescriptions** *(dict) --* 
                  Describes execution properties for a Java-based Kinesis Data Analytics application.
                  - **PropertyGroupDescriptions** *(list) --* 
                    Describes the execution property groups.
                    - *(dict) --* 
                      Property key-value pairs passed into a Java-based Kinesis Data Analytics application.
                      - **PropertyGroupId** *(string) --* 
                        Describes the key of an application execution property key-value pair.
                      - **PropertyMap** *(dict) --* 
                        Describes the value of an application execution property key-value pair.
                        - *(string) --* 
                          - *(string) --* 
                - **ApplicationSnapshotConfigurationDescription** *(dict) --* 
                  Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.
                  - **SnapshotsEnabled** *(boolean) --* 
                    Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.
              - **CloudWatchLoggingOptionDescriptions** *(list) --* 
                Describes the application Amazon CloudWatch logging options.
                - *(dict) --* 
                  Describes the Amazon CloudWatch logging option.
                  - **CloudWatchLoggingOptionId** *(string) --* 
                    The ID of the CloudWatch logging option description.
                  - **LogStreamARN** *(string) --* 
                    The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.
                  - **RoleARN** *(string) --* 
                    The IAM ARN of the role to use to send application messages. 
                    .. note::
                      Provided for backward compatibility. Applications created with the current API version have an application-level service execution role rather than a resource-level role.
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The name of the application.
        :type IncludeAdditionalDetails: boolean
        :param IncludeAdditionalDetails:
          Displays verbose information about a Kinesis Data Analytics application, including the application\'s job plan.
        :rtype: dict
        :returns:
        """
        pass

    def describe_application_snapshot(self, ApplicationName: str, SnapshotName: str) -> Dict:
        """
        Returns information about a snapshot of application state data.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/DescribeApplicationSnapshot>`_
        
        **Request Syntax**
        ::
          response = client.describe_application_snapshot(
              ApplicationName='string',
              SnapshotName='string'
          )
        
        **Response Syntax**
        ::
            {
                'SnapshotDetails': {
                    'SnapshotName': 'string',
                    'SnapshotStatus': 'CREATING'|'READY'|'DELETING'|'FAILED',
                    'ApplicationVersionId': 123,
                    'SnapshotCreationTimestamp': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **SnapshotDetails** *(dict) --* 
              An object containing information about the application snapshot.
              - **SnapshotName** *(string) --* 
                The identifier for the application snapshot.
              - **SnapshotStatus** *(string) --* 
                The status of the application snapshot.
              - **ApplicationVersionId** *(integer) --* 
                The current application version ID when the snapshot was created.
              - **SnapshotCreationTimestamp** *(datetime) --* 
                The timestamp of the application snapshot.
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The name of an existing application.
        :type SnapshotName: string
        :param SnapshotName: **[REQUIRED]**
          The identifier of an application snapshot. You can retrieve this value using .
        :rtype: dict
        :returns:
        """
        pass

    def discover_input_schema(self, ServiceExecutionRole: str, ResourceARN: str = None, InputStartingPositionConfiguration: Dict = None, S3Configuration: Dict = None, InputProcessingConfiguration: Dict = None) -> Dict:
        """
        Infers a schema for an SQL-based Amazon Kinesis Data Analytics application by evaluating sample records on the specified streaming source (Kinesis data stream or Kinesis Data Firehose delivery stream) or Amazon S3 object. In the response, the operation returns the inferred schema and also the sample records that the operation used to infer the schema.
        You can use the inferred schema when configuring a streaming source for your application. When you create an application using the Kinesis Data Analytics console, the console uses this operation to infer a schema and show it in the console user interface. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/DiscoverInputSchema>`_
        
        **Request Syntax**
        ::
          response = client.discover_input_schema(
              ResourceARN='string',
              ServiceExecutionRole='string',
              InputStartingPositionConfiguration={
                  'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
              },
              S3Configuration={
                  'BucketARN': 'string',
                  'FileKey': 'string'
              },
              InputProcessingConfiguration={
                  'InputLambdaProcessor': {
                      'ResourceARN': 'string'
                  }
              }
          )
        
        **Response Syntax**
        ::
            {
                'InputSchema': {
                    'RecordFormat': {
                        'RecordFormatType': 'JSON'|'CSV',
                        'MappingParameters': {
                            'JSONMappingParameters': {
                                'RecordRowPath': 'string'
                            },
                            'CSVMappingParameters': {
                                'RecordRowDelimiter': 'string',
                                'RecordColumnDelimiter': 'string'
                            }
                        }
                    },
                    'RecordEncoding': 'string',
                    'RecordColumns': [
                        {
                            'Name': 'string',
                            'Mapping': 'string',
                            'SqlType': 'string'
                        },
                    ]
                },
                'ParsedInputRecords': [
                    [
                        'string',
                    ],
                ],
                'ProcessedInputRecords': [
                    'string',
                ],
                'RawInputRecords': [
                    'string',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **InputSchema** *(dict) --* 
              The schema inferred from the streaming source. It identifies the format of the data in the streaming source and how each data element maps to corresponding columns in the in-application stream that you can create.
              - **RecordFormat** *(dict) --* 
                Specifies the format of the records on the streaming source.
                - **RecordFormatType** *(string) --* 
                  The type of record format.
                - **MappingParameters** *(dict) --* 
                  When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
                  - **JSONMappingParameters** *(dict) --* 
                    Provides additional mapping information when JSON is the record format on the streaming source.
                    - **RecordRowPath** *(string) --* 
                      The path to the top-level parent that contains the records.
                  - **CSVMappingParameters** *(dict) --* 
                    Provides additional mapping information when the record format uses delimiters (for example, CSV).
                    - **RecordRowDelimiter** *(string) --* 
                      The row delimiter. For example, in a CSV format, *'\n'* is the typical row delimiter.
                    - **RecordColumnDelimiter** *(string) --* 
                      The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
              - **RecordEncoding** *(string) --* 
                Specifies the encoding of the records in the streaming source. For example, UTF-8.
              - **RecordColumns** *(list) --* 
                A list of ``RecordColumn`` objects. 
                - *(dict) --* 
                  For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
                  Also used to describe the format of the reference data source.
                  - **Name** *(string) --* 
                    The name of the column that is created in the in-application input stream or reference table.
                  - **Mapping** *(string) --* 
                    A reference to the data element in the streaming input of the reference data source.
                  - **SqlType** *(string) --* 
                    The type of column created in the in-application input stream or reference table.
            - **ParsedInputRecords** *(list) --* 
              An array of elements, where each element corresponds to a row in a stream record (a stream record can have more than one row).
              - *(list) --* 
                - *(string) --* 
            - **ProcessedInputRecords** *(list) --* 
              The stream data that was modified by the processor specified in the ``InputProcessingConfiguration`` parameter.
              - *(string) --* 
            - **RawInputRecords** *(list) --* 
              The raw stream data that was sampled to infer the schema.
              - *(string) --* 
        :type ResourceARN: string
        :param ResourceARN:
          The Amazon Resource Name (ARN) of the streaming source.
        :type ServiceExecutionRole: string
        :param ServiceExecutionRole: **[REQUIRED]**
          The ARN of the role that is used to access the streaming source.
        :type InputStartingPositionConfiguration: dict
        :param InputStartingPositionConfiguration:
          The point at which you want Kinesis Data Analytics to start reading records from the specified streaming source discovery purposes.
          - **InputStartingPosition** *(string) --*
            The starting position on the stream.
            * ``NOW`` - Start reading just after the most recent record in the stream, and start at the request timestamp that the customer issued.
            * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Data Firehose delivery stream.
            * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped reading.
        :type S3Configuration: dict
        :param S3Configuration:
          Specify this parameter to discover a schema from data in an Amazon S3 object.
          - **BucketARN** *(string) --* **[REQUIRED]**
            The ARN of the S3 bucket that contains the data.
          - **FileKey** *(string) --* **[REQUIRED]**
            The name of the object that contains the data.
        :type InputProcessingConfiguration: dict
        :param InputProcessingConfiguration:
          The  InputProcessingConfiguration to use to preprocess the records before discovering the schema of the records.
          - **InputLambdaProcessor** *(dict) --* **[REQUIRED]**
            The  InputLambdaProcessor that is used to preprocess the records in the stream before being processed by your application code.
            - **ResourceARN** *(string) --* **[REQUIRED]**
              The ARN of the AWS Lambda function that operates on records in the stream.
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

    def list_application_snapshots(self, ApplicationName: str, Limit: int = None, NextToken: str = None) -> Dict:
        """
        Lists information about the current application snapshots.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/ListApplicationSnapshots>`_
        
        **Request Syntax**
        ::
          response = client.list_application_snapshots(
              ApplicationName='string',
              Limit=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'SnapshotSummaries': [
                    {
                        'SnapshotName': 'string',
                        'SnapshotStatus': 'CREATING'|'READY'|'DELETING'|'FAILED',
                        'ApplicationVersionId': 123,
                        'SnapshotCreationTimestamp': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **SnapshotSummaries** *(list) --* 
              A collection of objects containing information about the application snapshots.
              - *(dict) --* 
                Provides details about a snapshot of application state.
                - **SnapshotName** *(string) --* 
                  The identifier for the application snapshot.
                - **SnapshotStatus** *(string) --* 
                  The status of the application snapshot.
                - **ApplicationVersionId** *(integer) --* 
                  The current application version ID when the snapshot was created.
                - **SnapshotCreationTimestamp** *(datetime) --* 
                  The timestamp of the application snapshot.
            - **NextToken** *(string) --* 
              The token for the next set of results, or ``null`` if there are no additional results.
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The name of an existing application.
        :type Limit: integer
        :param Limit:
          The maximum number of application snapshots to list.
        :type NextToken: string
        :param NextToken:
          Use this parameter if you receive a ``NextToken`` response in a previous request that indicates that there is more output available. Set it to the value of the previous call\'s ``NextToken`` response to indicate where the output should continue from.
        :rtype: dict
        :returns:
        """
        pass

    def list_applications(self, Limit: int = None, NextToken: str = None) -> Dict:
        """
        Returns a list of Amazon Kinesis Data Analytics applications in your account. For each application, the response includes the application name, Amazon Resource Name (ARN), and status. 
        If you want detailed information about a specific application, use  DescribeApplication .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/ListApplications>`_
        
        **Request Syntax**
        ::
          response = client.list_applications(
              Limit=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'ApplicationSummaries': [
                    {
                        'ApplicationName': 'string',
                        'ApplicationARN': 'string',
                        'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING',
                        'ApplicationVersionId': 123,
                        'RuntimeEnvironment': 'SQL-1_0'|'FLINK-1_6'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ApplicationSummaries** *(list) --* 
              A list of ``ApplicationSummary`` objects.
              - *(dict) --* 
                Provides application summary information, including the application Amazon Resource Name (ARN), name, and status.
                - **ApplicationName** *(string) --* 
                  The name of the application.
                - **ApplicationARN** *(string) --* 
                  The ARN of the application.
                - **ApplicationStatus** *(string) --* 
                  The status of the application.
                - **ApplicationVersionId** *(integer) --* 
                  Provides the current application version.
                - **RuntimeEnvironment** *(string) --* 
                  The runtime environment for the application (``SQL-1.0`` or ``JAVA-8-FLINK-1.5`` ).
            - **NextToken** *(string) --* 
              The pagination token for the next set of results, or ``null`` if there are no additional results. Pass this token into a subsequent command to retrieve the next set of items For more information about pagination, see `Using the AWS Command Line Interface's Pagination Options <https://docs.aws.amazon.com/cli/latest/userguide/pagination.html>`__ .
        :type Limit: integer
        :param Limit:
          The maximum number of applications to list.
        :type NextToken: string
        :param NextToken:
          If a previous command returned a pagination token, pass it into this value to retrieve the next set of results. For more information about pagination, see `Using the AWS Command Line Interface\'s Pagination Options <https://docs.aws.amazon.com/cli/latest/userguide/pagination.html>`__ .
        :rtype: dict
        :returns:
        """
        pass

    def start_application(self, ApplicationName: str, RunConfiguration: Dict) -> Dict:
        """
        Starts the specified Amazon Kinesis Data Analytics application. After creating an application, you must exclusively call this operation to start your application.
        .. note::
          SQL is not enabled for this private beta. Using SQL parameters (such as  RunConfiguration$SqlRunConfigurations ) will result in an error.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/StartApplication>`_
        
        **Request Syntax**
        ::
          response = client.start_application(
              ApplicationName='string',
              RunConfiguration={
                  'SqlRunConfigurations': [
                      {
                          'InputId': 'string',
                          'InputStartingPositionConfiguration': {
                              'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
                          }
                      },
                  ],
                  'ApplicationRestoreConfiguration': {
                      'ApplicationRestoreType': 'SKIP_RESTORE_FROM_SNAPSHOT'|'RESTORE_FROM_LATEST_SNAPSHOT'|'RESTORE_FROM_CUSTOM_SNAPSHOT',
                      'SnapshotName': 'string'
                  }
              }
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The name of the application.
        :type RunConfiguration: dict
        :param RunConfiguration: **[REQUIRED]**
          Identifies the run configuration (start parameters) of a Kinesis Data Analytics application.
          - **SqlRunConfigurations** *(list) --*
            Describes the starting parameters for an SQL-based Kinesis Data Analytics application.
            - *(dict) --*
              Describes the starting parameters for an SQL-based Kinesis Data Analytics application.
              - **InputId** *(string) --* **[REQUIRED]**
                The input source ID. You can get this ID by calling the  DescribeApplication operation.
              - **InputStartingPositionConfiguration** *(dict) --* **[REQUIRED]**
                The point at which you want the application to start processing records from the streaming source.
                - **InputStartingPosition** *(string) --*
                  The starting position on the stream.
                  * ``NOW`` - Start reading just after the most recent record in the stream, and start at the request timestamp that the customer issued.
                  * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Data Firehose delivery stream.
                  * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped reading.
          - **ApplicationRestoreConfiguration** *(dict) --*
            Describes the restore behavior of a restarting application.
            - **ApplicationRestoreType** *(string) --* **[REQUIRED]**
              Specifies how the application should be restored.
            - **SnapshotName** *(string) --*
              The identifier of an existing snapshot of application state to use to restart an application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is specified for the ``ApplicationRestoreType`` .
        :rtype: dict
        :returns:
        """
        pass

    def stop_application(self, ApplicationName: str) -> Dict:
        """
        Stops the application from processing data. You can stop an application only if it is in the running state. You can use the  DescribeApplication operation to find the application state. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/StopApplication>`_
        
        **Request Syntax**
        ::
          response = client.stop_application(
              ApplicationName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The name of the running application to stop.
        :rtype: dict
        :returns:
        """
        pass

    def update_application(self, ApplicationName: str, CurrentApplicationVersionId: int, ApplicationConfigurationUpdate: Dict = None, ServiceExecutionRoleUpdate: str = None, RunConfigurationUpdate: Dict = None, CloudWatchLoggingOptionUpdates: List = None) -> Dict:
        """
        Updates an existing Amazon Kinesis Data Analytics application. Using this operation, you can update application code, input configuration, and output configuration. 
        Kinesis Data Analytics updates the ``ApplicationVersionId`` each time you update your application. 
        .. note::
          SQL is not enabled for this private beta. Using SQL parameters (such as  SqlApplicationConfigurationUpdate ) will result in an error.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/UpdateApplication>`_
        
        **Request Syntax**
        ::
          response = client.update_application(
              ApplicationName='string',
              CurrentApplicationVersionId=123,
              ApplicationConfigurationUpdate={
                  'SqlApplicationConfigurationUpdate': {
                      'InputUpdates': [
                          {
                              'InputId': 'string',
                              'NamePrefixUpdate': 'string',
                              'InputProcessingConfigurationUpdate': {
                                  'InputLambdaProcessorUpdate': {
                                      'ResourceARNUpdate': 'string'
                                  }
                              },
                              'KinesisStreamsInputUpdate': {
                                  'ResourceARNUpdate': 'string'
                              },
                              'KinesisFirehoseInputUpdate': {
                                  'ResourceARNUpdate': 'string'
                              },
                              'InputSchemaUpdate': {
                                  'RecordFormatUpdate': {
                                      'RecordFormatType': 'JSON'|'CSV',
                                      'MappingParameters': {
                                          'JSONMappingParameters': {
                                              'RecordRowPath': 'string'
                                          },
                                          'CSVMappingParameters': {
                                              'RecordRowDelimiter': 'string',
                                              'RecordColumnDelimiter': 'string'
                                          }
                                      }
                                  },
                                  'RecordEncodingUpdate': 'string',
                                  'RecordColumnUpdates': [
                                      {
                                          'Name': 'string',
                                          'Mapping': 'string',
                                          'SqlType': 'string'
                                      },
                                  ]
                              },
                              'InputParallelismUpdate': {
                                  'CountUpdate': 123
                              }
                          },
                      ],
                      'OutputUpdates': [
                          {
                              'OutputId': 'string',
                              'NameUpdate': 'string',
                              'KinesisStreamsOutputUpdate': {
                                  'ResourceARNUpdate': 'string'
                              },
                              'KinesisFirehoseOutputUpdate': {
                                  'ResourceARNUpdate': 'string'
                              },
                              'LambdaOutputUpdate': {
                                  'ResourceARNUpdate': 'string'
                              },
                              'DestinationSchemaUpdate': {
                                  'RecordFormatType': 'JSON'|'CSV'
                              }
                          },
                      ],
                      'ReferenceDataSourceUpdates': [
                          {
                              'ReferenceId': 'string',
                              'TableNameUpdate': 'string',
                              'S3ReferenceDataSourceUpdate': {
                                  'BucketARNUpdate': 'string',
                                  'FileKeyUpdate': 'string'
                              },
                              'ReferenceSchemaUpdate': {
                                  'RecordFormat': {
                                      'RecordFormatType': 'JSON'|'CSV',
                                      'MappingParameters': {
                                          'JSONMappingParameters': {
                                              'RecordRowPath': 'string'
                                          },
                                          'CSVMappingParameters': {
                                              'RecordRowDelimiter': 'string',
                                              'RecordColumnDelimiter': 'string'
                                          }
                                      }
                                  },
                                  'RecordEncoding': 'string',
                                  'RecordColumns': [
                                      {
                                          'Name': 'string',
                                          'Mapping': 'string',
                                          'SqlType': 'string'
                                      },
                                  ]
                              }
                          },
                      ]
                  },
                  'ApplicationCodeConfigurationUpdate': {
                      'CodeContentTypeUpdate': 'PLAINTEXT'|'ZIPFILE',
                      'CodeContentUpdate': {
                          'TextContentUpdate': 'string',
                          'ZipFileContentUpdate': b'bytes',
                          'S3ContentLocationUpdate': {
                              'BucketARNUpdate': 'string',
                              'FileKeyUpdate': 'string',
                              'ObjectVersionUpdate': 'string'
                          }
                      }
                  },
                  'FlinkApplicationConfigurationUpdate': {
                      'CheckpointConfigurationUpdate': {
                          'ConfigurationTypeUpdate': 'DEFAULT'|'CUSTOM',
                          'CheckpointingEnabledUpdate': True|False,
                          'CheckpointIntervalUpdate': 123,
                          'MinPauseBetweenCheckpointsUpdate': 123
                      },
                      'MonitoringConfigurationUpdate': {
                          'ConfigurationTypeUpdate': 'DEFAULT'|'CUSTOM',
                          'MetricsLevelUpdate': 'APPLICATION'|'TASK'|'OPERATOR'|'PARALLELISM',
                          'LogLevelUpdate': 'INFO'|'WARN'|'ERROR'|'DEBUG'
                      },
                      'ParallelismConfigurationUpdate': {
                          'ConfigurationTypeUpdate': 'DEFAULT'|'CUSTOM',
                          'ParallelismUpdate': 123,
                          'ParallelismPerKPUUpdate': 123,
                          'AutoScalingEnabledUpdate': True|False
                      }
                  },
                  'EnvironmentPropertyUpdates': {
                      'PropertyGroups': [
                          {
                              'PropertyGroupId': 'string',
                              'PropertyMap': {
                                  'string': 'string'
                              }
                          },
                      ]
                  },
                  'ApplicationSnapshotConfigurationUpdate': {
                      'SnapshotsEnabledUpdate': True|False
                  }
              },
              ServiceExecutionRoleUpdate='string',
              RunConfigurationUpdate={
                  'ApplicationRestoreConfiguration': {
                      'ApplicationRestoreType': 'SKIP_RESTORE_FROM_SNAPSHOT'|'RESTORE_FROM_LATEST_SNAPSHOT'|'RESTORE_FROM_CUSTOM_SNAPSHOT',
                      'SnapshotName': 'string'
                  }
              },
              CloudWatchLoggingOptionUpdates=[
                  {
                      'CloudWatchLoggingOptionId': 'string',
                      'LogStreamARNUpdate': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'ApplicationDetail': {
                    'ApplicationARN': 'string',
                    'ApplicationDescription': 'string',
                    'ApplicationName': 'string',
                    'RuntimeEnvironment': 'SQL-1_0'|'FLINK-1_6',
                    'ServiceExecutionRole': 'string',
                    'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING',
                    'ApplicationVersionId': 123,
                    'CreateTimestamp': datetime(2015, 1, 1),
                    'LastUpdateTimestamp': datetime(2015, 1, 1),
                    'ApplicationConfigurationDescription': {
                        'SqlApplicationConfigurationDescription': {
                            'InputDescriptions': [
                                {
                                    'InputId': 'string',
                                    'NamePrefix': 'string',
                                    'InAppStreamNames': [
                                        'string',
                                    ],
                                    'InputProcessingConfigurationDescription': {
                                        'InputLambdaProcessorDescription': {
                                            'ResourceARN': 'string',
                                            'RoleARN': 'string'
                                        }
                                    },
                                    'KinesisStreamsInputDescription': {
                                        'ResourceARN': 'string',
                                        'RoleARN': 'string'
                                    },
                                    'KinesisFirehoseInputDescription': {
                                        'ResourceARN': 'string',
                                        'RoleARN': 'string'
                                    },
                                    'InputSchema': {
                                        'RecordFormat': {
                                            'RecordFormatType': 'JSON'|'CSV',
                                            'MappingParameters': {
                                                'JSONMappingParameters': {
                                                    'RecordRowPath': 'string'
                                                },
                                                'CSVMappingParameters': {
                                                    'RecordRowDelimiter': 'string',
                                                    'RecordColumnDelimiter': 'string'
                                                }
                                            }
                                        },
                                        'RecordEncoding': 'string',
                                        'RecordColumns': [
                                            {
                                                'Name': 'string',
                                                'Mapping': 'string',
                                                'SqlType': 'string'
                                            },
                                        ]
                                    },
                                    'InputParallelism': {
                                        'Count': 123
                                    },
                                    'InputStartingPositionConfiguration': {
                                        'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
                                    }
                                },
                            ],
                            'OutputDescriptions': [
                                {
                                    'OutputId': 'string',
                                    'Name': 'string',
                                    'KinesisStreamsOutputDescription': {
                                        'ResourceARN': 'string',
                                        'RoleARN': 'string'
                                    },
                                    'KinesisFirehoseOutputDescription': {
                                        'ResourceARN': 'string',
                                        'RoleARN': 'string'
                                    },
                                    'LambdaOutputDescription': {
                                        'ResourceARN': 'string',
                                        'RoleARN': 'string'
                                    },
                                    'DestinationSchema': {
                                        'RecordFormatType': 'JSON'|'CSV'
                                    }
                                },
                            ],
                            'ReferenceDataSourceDescriptions': [
                                {
                                    'ReferenceId': 'string',
                                    'TableName': 'string',
                                    'S3ReferenceDataSourceDescription': {
                                        'BucketARN': 'string',
                                        'FileKey': 'string',
                                        'ReferenceRoleARN': 'string'
                                    },
                                    'ReferenceSchema': {
                                        'RecordFormat': {
                                            'RecordFormatType': 'JSON'|'CSV',
                                            'MappingParameters': {
                                                'JSONMappingParameters': {
                                                    'RecordRowPath': 'string'
                                                },
                                                'CSVMappingParameters': {
                                                    'RecordRowDelimiter': 'string',
                                                    'RecordColumnDelimiter': 'string'
                                                }
                                            }
                                        },
                                        'RecordEncoding': 'string',
                                        'RecordColumns': [
                                            {
                                                'Name': 'string',
                                                'Mapping': 'string',
                                                'SqlType': 'string'
                                            },
                                        ]
                                    }
                                },
                            ]
                        },
                        'ApplicationCodeConfigurationDescription': {
                            'CodeContentType': 'PLAINTEXT'|'ZIPFILE',
                            'CodeContentDescription': {
                                'TextContent': 'string',
                                'CodeMD5': 'string',
                                'CodeSize': 123,
                                'S3ApplicationCodeLocationDescription': {
                                    'BucketARN': 'string',
                                    'FileKey': 'string',
                                    'ObjectVersion': 'string'
                                }
                            }
                        },
                        'RunConfigurationDescription': {
                            'ApplicationRestoreConfigurationDescription': {
                                'ApplicationRestoreType': 'SKIP_RESTORE_FROM_SNAPSHOT'|'RESTORE_FROM_LATEST_SNAPSHOT'|'RESTORE_FROM_CUSTOM_SNAPSHOT',
                                'SnapshotName': 'string'
                            }
                        },
                        'FlinkApplicationConfigurationDescription': {
                            'CheckpointConfigurationDescription': {
                                'ConfigurationType': 'DEFAULT'|'CUSTOM',
                                'CheckpointingEnabled': True|False,
                                'CheckpointInterval': 123,
                                'MinPauseBetweenCheckpoints': 123
                            },
                            'MonitoringConfigurationDescription': {
                                'ConfigurationType': 'DEFAULT'|'CUSTOM',
                                'MetricsLevel': 'APPLICATION'|'TASK'|'OPERATOR'|'PARALLELISM',
                                'LogLevel': 'INFO'|'WARN'|'ERROR'|'DEBUG'
                            },
                            'ParallelismConfigurationDescription': {
                                'ConfigurationType': 'DEFAULT'|'CUSTOM',
                                'Parallelism': 123,
                                'ParallelismPerKPU': 123,
                                'CurrentParallelism': 123,
                                'AutoScalingEnabled': True|False
                            },
                            'JobPlanDescription': 'string'
                        },
                        'EnvironmentPropertyDescriptions': {
                            'PropertyGroupDescriptions': [
                                {
                                    'PropertyGroupId': 'string',
                                    'PropertyMap': {
                                        'string': 'string'
                                    }
                                },
                            ]
                        },
                        'ApplicationSnapshotConfigurationDescription': {
                            'SnapshotsEnabled': True|False
                        }
                    },
                    'CloudWatchLoggingOptionDescriptions': [
                        {
                            'CloudWatchLoggingOptionId': 'string',
                            'LogStreamARN': 'string',
                            'RoleARN': 'string'
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ApplicationDetail** *(dict) --* 
              Describes application updates.
              - **ApplicationARN** *(string) --* 
                The ARN of the application.
              - **ApplicationDescription** *(string) --* 
                The description of the application.
              - **ApplicationName** *(string) --* 
                The name of the application.
              - **RuntimeEnvironment** *(string) --* 
                The runtime environment for the application (``SQL-1.0`` or ``JAVA-8-FLINK-1.5`` ).
              - **ServiceExecutionRole** *(string) --* 
                Specifies the IAM role that the application uses to access external resources.
              - **ApplicationStatus** *(string) --* 
                The status of the application.
              - **ApplicationVersionId** *(integer) --* 
                Provides the current application version. Kinesis Data Analytics updates the ``ApplicationVersionId`` each time you update the application.
              - **CreateTimestamp** *(datetime) --* 
                The current timestamp when the application was created.
              - **LastUpdateTimestamp** *(datetime) --* 
                The current timestamp when the application was last updated.
              - **ApplicationConfigurationDescription** *(dict) --* 
                Provides details about the application's SQL or Java code and starting parameters.
                - **SqlApplicationConfigurationDescription** *(dict) --* 
                  The details about inputs, outputs, and reference data sources for an SQL-based Kinesis Data Analytics application.
                  - **InputDescriptions** *(list) --* 
                    The array of  InputDescription objects describing the input streams used by the application.
                    - *(dict) --* 
                      Describes the application input configuration for an SQL-based Amazon Kinesis Data Analytics application. 
                      - **InputId** *(string) --* 
                        The input ID that is associated with the application input. This is the ID that Kinesis Data Analytics assigns to each input configuration that you add to your application. 
                      - **NamePrefix** *(string) --* 
                        The in-application name prefix.
                      - **InAppStreamNames** *(list) --* 
                        Returns the in-application stream names that are mapped to the stream source. 
                        - *(string) --* 
                      - **InputProcessingConfigurationDescription** *(dict) --* 
                        The description of the preprocessor that executes on records in this input before the application's code is run. 
                        - **InputLambdaProcessorDescription** *(dict) --* 
                          Provides configuration information about the associated  InputLambdaProcessorDescription  
                          - **ResourceARN** *(string) --* 
                            The ARN of the AWS Lambda function that is used to preprocess the records in the stream.
                          - **RoleARN** *(string) --* 
                            The ARN of the IAM role that is used to access the AWS Lambda function.
                            .. note::
                              Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **KinesisStreamsInputDescription** *(dict) --* 
                        If a Kinesis data stream is configured as a streaming source, provides the Kinesis data stream's Amazon Resource Name (ARN). 
                        - **ResourceARN** *(string) --* 
                          The Amazon Resource Name (ARN) of the Kinesis data stream.
                        - **RoleARN** *(string) --* 
                          The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.
                          .. note::
                            Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **KinesisFirehoseInputDescription** *(dict) --* 
                        If a Kinesis Data Firehose delivery stream is configured as a streaming source, provides the delivery stream's ARN. 
                        - **ResourceARN** *(string) --* 
                          The Amazon Resource Name (ARN) of the delivery stream.
                        - **RoleARN** *(string) --* 
                          The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.
                          .. note::
                            Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **InputSchema** *(dict) --* 
                        Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created. 
                        - **RecordFormat** *(dict) --* 
                          Specifies the format of the records on the streaming source.
                          - **RecordFormatType** *(string) --* 
                            The type of record format.
                          - **MappingParameters** *(dict) --* 
                            When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
                            - **JSONMappingParameters** *(dict) --* 
                              Provides additional mapping information when JSON is the record format on the streaming source.
                              - **RecordRowPath** *(string) --* 
                                The path to the top-level parent that contains the records.
                            - **CSVMappingParameters** *(dict) --* 
                              Provides additional mapping information when the record format uses delimiters (for example, CSV).
                              - **RecordRowDelimiter** *(string) --* 
                                The row delimiter. For example, in a CSV format, *'\n'* is the typical row delimiter.
                              - **RecordColumnDelimiter** *(string) --* 
                                The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
                        - **RecordEncoding** *(string) --* 
                          Specifies the encoding of the records in the streaming source. For example, UTF-8.
                        - **RecordColumns** *(list) --* 
                          A list of ``RecordColumn`` objects. 
                          - *(dict) --* 
                            For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
                            Also used to describe the format of the reference data source.
                            - **Name** *(string) --* 
                              The name of the column that is created in the in-application input stream or reference table.
                            - **Mapping** *(string) --* 
                              A reference to the data element in the streaming input of the reference data source.
                            - **SqlType** *(string) --* 
                              The type of column created in the in-application input stream or reference table.
                      - **InputParallelism** *(dict) --* 
                        Describes the configured parallelism (number of in-application streams mapped to the streaming source). 
                        - **Count** *(integer) --* 
                          The number of in-application streams to create.
                      - **InputStartingPositionConfiguration** *(dict) --* 
                        The point at which the application is configured to read from the input stream.
                        - **InputStartingPosition** *(string) --* 
                          The starting position on the stream.
                          * ``NOW`` - Start reading just after the most recent record in the stream, and start at the request timestamp that the customer issued. 
                          * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Data Firehose delivery stream. 
                          * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped reading. 
                  - **OutputDescriptions** *(list) --* 
                    The array of  OutputDescription objects describing the destination streams used by the application.
                    - *(dict) --* 
                      For an SQL-based Amazon Kinesis Data Analytics application, describes the application output configuration, which includes the in-application stream name and the destination where the stream data is written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream. 
                      - **OutputId** *(string) --* 
                        A unique identifier for the output configuration.
                      - **Name** *(string) --* 
                        The name of the in-application stream that is configured as output.
                      - **KinesisStreamsOutputDescription** *(dict) --* 
                        Describes the Kinesis data stream that is configured as the destination where output is written.
                        - **ResourceARN** *(string) --* 
                          The Amazon Resource Name (ARN) of the Kinesis data stream.
                        - **RoleARN** *(string) --* 
                          The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.
                          .. note::
                            Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **KinesisFirehoseOutputDescription** *(dict) --* 
                        Describes the Kinesis Data Firehose delivery stream that is configured as the destination where output is written.
                        - **ResourceARN** *(string) --* 
                          The Amazon Resource Name (ARN) of the delivery stream.
                        - **RoleARN** *(string) --* 
                          The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.
                          .. note::
                            Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **LambdaOutputDescription** *(dict) --* 
                        Describes the Lambda function that is configured as the destination where output is written.
                        - **ResourceARN** *(string) --* 
                          The Amazon Resource Name (ARN) of the destination Lambda function.
                        - **RoleARN** *(string) --* 
                          The ARN of the IAM role that Kinesis Data Analytics can assume to write to the destination function.
                          .. note::
                            Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **DestinationSchema** *(dict) --* 
                        The data format used for writing data to the destination.
                        - **RecordFormatType** *(string) --* 
                          Specifies the format of the records on the output stream.
                  - **ReferenceDataSourceDescriptions** *(list) --* 
                    The array of  ReferenceDataSourceDescription objects describing the reference data sources used by the application.
                    - *(dict) --* 
                      For an SQL-based Amazon Kinesis Data Analytics application, describes the reference data source configured for an application.
                      - **ReferenceId** *(string) --* 
                        The ID of the reference data source. This is the ID that Kinesis Data Analytics assigns when you add the reference data source to your application using the  CreateApplication or  UpdateApplication operation.
                      - **TableName** *(string) --* 
                        The in-application table name created by the specific reference data source configuration.
                      - **S3ReferenceDataSourceDescription** *(dict) --* 
                        Provides the Amazon S3 bucket name, the object key name that contains the reference data. 
                        - **BucketARN** *(string) --* 
                          The Amazon Resource Name (ARN) of the S3 bucket.
                        - **FileKey** *(string) --* 
                          Amazon S3 object key name.
                        - **ReferenceRoleARN** *(string) --* 
                          The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon S3 object on your behalf to populate the in-application reference table. 
                          .. note::
                            Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
                      - **ReferenceSchema** *(dict) --* 
                        Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.
                        - **RecordFormat** *(dict) --* 
                          Specifies the format of the records on the streaming source.
                          - **RecordFormatType** *(string) --* 
                            The type of record format.
                          - **MappingParameters** *(dict) --* 
                            When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
                            - **JSONMappingParameters** *(dict) --* 
                              Provides additional mapping information when JSON is the record format on the streaming source.
                              - **RecordRowPath** *(string) --* 
                                The path to the top-level parent that contains the records.
                            - **CSVMappingParameters** *(dict) --* 
                              Provides additional mapping information when the record format uses delimiters (for example, CSV).
                              - **RecordRowDelimiter** *(string) --* 
                                The row delimiter. For example, in a CSV format, *'\n'* is the typical row delimiter.
                              - **RecordColumnDelimiter** *(string) --* 
                                The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
                        - **RecordEncoding** *(string) --* 
                          Specifies the encoding of the records in the streaming source. For example, UTF-8.
                        - **RecordColumns** *(list) --* 
                          A list of ``RecordColumn`` objects. 
                          - *(dict) --* 
                            For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
                            Also used to describe the format of the reference data source.
                            - **Name** *(string) --* 
                              The name of the column that is created in the in-application input stream or reference table.
                            - **Mapping** *(string) --* 
                              A reference to the data element in the streaming input of the reference data source.
                            - **SqlType** *(string) --* 
                              The type of column created in the in-application input stream or reference table.
                - **ApplicationCodeConfigurationDescription** *(dict) --* 
                  The details about the application code for a Java-based Kinesis Data Analytics application.
                  - **CodeContentType** *(string) --* 
                    Specifies whether the code content is in text or zip format.
                  - **CodeContentDescription** *(dict) --* 
                    Describes details about the location and format of the application code.
                    - **TextContent** *(string) --* 
                      The text-format code
                    - **CodeMD5** *(string) --* 
                      The checksum that can be used to validate zip-format code.
                    - **CodeSize** *(integer) --* 
                      The size in bytes of the application code. Can be used to validate zip-format code.
                    - **S3ApplicationCodeLocationDescription** *(dict) --* 
                      The S3 bucket Amazon Resource Name (ARN), file key, and object version of the application code stored in Amazon S3.
                      - **BucketARN** *(string) --* 
                        The Amazon Resource Name (ARN) for the S3 bucket containing the application code.
                      - **FileKey** *(string) --* 
                        The file key for the object containing the application code.
                      - **ObjectVersion** *(string) --* 
                        The version of the object containing the application code.
                - **RunConfigurationDescription** *(dict) --* 
                  The details about the starting properties for a Kinesis Data Analytics application.
                  - **ApplicationRestoreConfigurationDescription** *(dict) --* 
                    Describes the restore behavior of a restarting application.
                    - **ApplicationRestoreType** *(string) --* 
                      Specifies how the application should be restored.
                    - **SnapshotName** *(string) --* 
                      The identifier of an existing snapshot of application state to use to restart an application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is specified for the ``ApplicationRestoreType`` .
                - **FlinkApplicationConfigurationDescription** *(dict) --* 
                  The details about a Java-based Kinesis Data Analytics application.
                  - **CheckpointConfigurationDescription** *(dict) --* 
                    Describes an application's checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance.
                    - **ConfigurationType** *(string) --* 
                      Describes whether the application uses the default checkpointing behavior in Kinesis Data Analytics.
                    - **CheckpointingEnabled** *(boolean) --* 
                      Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics application.
                    - **CheckpointInterval** *(integer) --* 
                      Describes the interval in milliseconds between checkpoint operations.
                    - **MinPauseBetweenCheckpoints** *(integer) --* 
                      Describes the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start.
                  - **MonitoringConfigurationDescription** *(dict) --* 
                    Describes configuration parameters for Amazon CloudWatch logging for an application.
                    - **ConfigurationType** *(string) --* 
                      Describes whether to use the default CloudWatch logging configuration for an application.
                    - **MetricsLevel** *(string) --* 
                      Describes the granularity of the CloudWatch Logs for an application.
                    - **LogLevel** *(string) --* 
                      Describes the verbosity of the CloudWatch Logs for an application.
                  - **ParallelismConfigurationDescription** *(dict) --* 
                    Describes parameters for how an application executes multiple tasks simultaneously.
                    - **ConfigurationType** *(string) --* 
                      Describes whether the application uses the default parallelism for the Kinesis Data Analytics service. 
                    - **Parallelism** *(integer) --* 
                      Describes the initial number of parallel tasks that a Java-based Kinesis Data Analytics application can perform. 
                    - **ParallelismPerKPU** *(integer) --* 
                      Describes the number of parallel tasks that a Java-based Kinesis Data Analytics application can perform per Kinesis Processing Unit (KPU) used by the application.
                    - **CurrentParallelism** *(integer) --* 
                      Describes the current number of parallel tasks that a Java-based Kinesis Data Analytics application can perform.
                    - **AutoScalingEnabled** *(boolean) --* 
                      Describes whether the Kinesis Data Analytics service can increase the parallelism of the application in response to increased throughput.
                  - **JobPlanDescription** *(string) --* 
                    The job plan for an application. For more information about the job plan, see `Jobs and Scheduling <https://ci.apache.org/projects/flink/flink-docs-stable/internals/job_scheduling.html>`__ in the `Apache Flink Documentation <https://ci.apache.org/projects/flink/flink-docs-release-1.6/>`__ . To retrieve the job plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails parameter of the  DescribeApplication operation.
                - **EnvironmentPropertyDescriptions** *(dict) --* 
                  Describes execution properties for a Java-based Kinesis Data Analytics application.
                  - **PropertyGroupDescriptions** *(list) --* 
                    Describes the execution property groups.
                    - *(dict) --* 
                      Property key-value pairs passed into a Java-based Kinesis Data Analytics application.
                      - **PropertyGroupId** *(string) --* 
                        Describes the key of an application execution property key-value pair.
                      - **PropertyMap** *(dict) --* 
                        Describes the value of an application execution property key-value pair.
                        - *(string) --* 
                          - *(string) --* 
                - **ApplicationSnapshotConfigurationDescription** *(dict) --* 
                  Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.
                  - **SnapshotsEnabled** *(boolean) --* 
                    Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.
              - **CloudWatchLoggingOptionDescriptions** *(list) --* 
                Describes the application Amazon CloudWatch logging options.
                - *(dict) --* 
                  Describes the Amazon CloudWatch logging option.
                  - **CloudWatchLoggingOptionId** *(string) --* 
                    The ID of the CloudWatch logging option description.
                  - **LogStreamARN** *(string) --* 
                    The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.
                  - **RoleARN** *(string) --* 
                    The IAM ARN of the role to use to send application messages. 
                    .. note::
                      Provided for backward compatibility. Applications created with the current API version have an application-level service execution role rather than a resource-level role.
        :type ApplicationName: string
        :param ApplicationName: **[REQUIRED]**
          The name of the application to update.
        :type CurrentApplicationVersionId: integer
        :param CurrentApplicationVersionId: **[REQUIRED]**
          The current application version ID. You can retrieve the application version ID using  DescribeApplication .
        :type ApplicationConfigurationUpdate: dict
        :param ApplicationConfigurationUpdate:
          Describes application configuration updates.
          - **SqlApplicationConfigurationUpdate** *(dict) --*
            Describes updates to an SQL-based Kinesis Data Analytics application\'s configuration.
            - **InputUpdates** *(list) --*
              The array of  InputUpdate objects describing the new input streams used by the application.
              - *(dict) --*
                For an SQL-based Amazon Kinesis Data Analytics application, describes updates to a specific input configuration (identified by the ``InputId`` of an application).
                - **InputId** *(string) --* **[REQUIRED]**
                  The input ID of the application input to be updated.
                - **NamePrefixUpdate** *(string) --*
                  The name prefix for in-application streams that Kinesis Data Analytics creates for the specific streaming source.
                - **InputProcessingConfigurationUpdate** *(dict) --*
                  Describes updates to an  InputProcessingConfiguration .
                  - **InputLambdaProcessorUpdate** *(dict) --* **[REQUIRED]**
                    Provides update information for an  InputLambdaProcessor .
                    - **ResourceARNUpdate** *(string) --* **[REQUIRED]**
                      The Amazon Resource Name (ARN) of the new AWS Lambda function that is used to preprocess the records in the stream.
                - **KinesisStreamsInputUpdate** *(dict) --*
                  If a Kinesis data stream is the streaming source to be updated, provides an updated stream Amazon Resource Name (ARN).
                  - **ResourceARNUpdate** *(string) --* **[REQUIRED]**
                    The Amazon Resource Name (ARN) of the input Kinesis data stream to read.
                - **KinesisFirehoseInputUpdate** *(dict) --*
                  If a Kinesis Data Firehose delivery stream is the streaming source to be updated, provides an updated stream ARN.
                  - **ResourceARNUpdate** *(string) --* **[REQUIRED]**
                    The Amazon Resource Name (ARN) of the input delivery stream to read.
                - **InputSchemaUpdate** *(dict) --*
                  Describes the data format on the streaming source, and how record elements on the streaming source map to columns of the in-application stream that is created.
                  - **RecordFormatUpdate** *(dict) --*
                    Specifies the format of the records on the streaming source.
                    - **RecordFormatType** *(string) --* **[REQUIRED]**
                      The type of record format.
                    - **MappingParameters** *(dict) --*
                      When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
                      - **JSONMappingParameters** *(dict) --*
                        Provides additional mapping information when JSON is the record format on the streaming source.
                        - **RecordRowPath** *(string) --* **[REQUIRED]**
                          The path to the top-level parent that contains the records.
                      - **CSVMappingParameters** *(dict) --*
                        Provides additional mapping information when the record format uses delimiters (for example, CSV).
                        - **RecordRowDelimiter** *(string) --* **[REQUIRED]**
                          The row delimiter. For example, in a CSV format, *\'\n\'* is the typical row delimiter.
                        - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**
                          The column delimiter. For example, in a CSV format, a comma (\",\") is the typical column delimiter.
                  - **RecordEncodingUpdate** *(string) --*
                    Specifies the encoding of the records in the streaming source; for example, UTF-8.
                  - **RecordColumnUpdates** *(list) --*
                    A list of ``RecordColumn`` objects. Each object describes the mapping of the streaming source element to the corresponding column in the in-application stream.
                    - *(dict) --*
                      For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
                      Also used to describe the format of the reference data source.
                      - **Name** *(string) --* **[REQUIRED]**
                        The name of the column that is created in the in-application input stream or reference table.
                      - **Mapping** *(string) --*
                        A reference to the data element in the streaming input of the reference data source.
                      - **SqlType** *(string) --* **[REQUIRED]**
                        The type of column created in the in-application input stream or reference table.
                - **InputParallelismUpdate** *(dict) --*
                  Describes the parallelism updates (the number of in-application streams Kinesis Data Analytics creates for the specific streaming source).
                  - **CountUpdate** *(integer) --* **[REQUIRED]**
                    The number of in-application streams to create for the specified streaming source.
            - **OutputUpdates** *(list) --*
              The array of  OutputUpdate objects describing the new destination streams used by the application.
              - *(dict) --*
                For an SQL-based Amazon Kinesis Data Analytics application, describes updates to the output configuration identified by the ``OutputId`` .
                - **OutputId** *(string) --* **[REQUIRED]**
                  Identifies the specific output configuration that you want to update.
                - **NameUpdate** *(string) --*
                  If you want to specify a different in-application stream for this output configuration, use this field to specify the new in-application stream name.
                - **KinesisStreamsOutputUpdate** *(dict) --*
                  Describes a Kinesis data stream as the destination for the output.
                  - **ResourceARNUpdate** *(string) --* **[REQUIRED]**
                    The Amazon Resource Name (ARN) of the Kinesis data stream where you want to write the output.
                - **KinesisFirehoseOutputUpdate** *(dict) --*
                  Describes a Kinesis Data Firehose delivery stream as the destination for the output.
                  - **ResourceARNUpdate** *(string) --* **[REQUIRED]**
                    The Amazon Resource Name (ARN) of the delivery stream to write to.
                - **LambdaOutputUpdate** *(dict) --*
                  Describes an AWS Lambda function as the destination for the output.
                  - **ResourceARNUpdate** *(string) --* **[REQUIRED]**
                    The Amazon Resource Name (ARN) of the destination AWS Lambda function.
                - **DestinationSchemaUpdate** *(dict) --*
                  Describes the data format when records are written to the destination.
                  - **RecordFormatType** *(string) --* **[REQUIRED]**
                    Specifies the format of the records on the output stream.
            - **ReferenceDataSourceUpdates** *(list) --*
              The array of  ReferenceDataSourceUpdate objects describing the new reference data sources used by the application.
              - *(dict) --*
                When you update a reference data source configuration for a SQL-based Amazon Kinesis Data Analytics application, this object provides all the updated values (such as the source bucket name and object key name), the in-application table name that is created, and updated mapping information that maps the data in the Amazon S3 object to the in-application reference table that is created.
                - **ReferenceId** *(string) --* **[REQUIRED]**
                  The ID of the reference data source that is being updated. You can use the  DescribeApplication operation to get this value.
                - **TableNameUpdate** *(string) --*
                  The in-application table name that is created by this update.
                - **S3ReferenceDataSourceUpdate** *(dict) --*
                  Describes the S3 bucket name, object key name, and IAM role that Kinesis Data Analytics can assume to read the Amazon S3 object on your behalf and populate the in-application reference table.
                  - **BucketARNUpdate** *(string) --*
                    The Amazon Resource Name (ARN) of the S3 bucket.
                  - **FileKeyUpdate** *(string) --*
                    The object key name.
                - **ReferenceSchemaUpdate** *(dict) --*
                  Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.
                  - **RecordFormat** *(dict) --* **[REQUIRED]**
                    Specifies the format of the records on the streaming source.
                    - **RecordFormatType** *(string) --* **[REQUIRED]**
                      The type of record format.
                    - **MappingParameters** *(dict) --*
                      When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
                      - **JSONMappingParameters** *(dict) --*
                        Provides additional mapping information when JSON is the record format on the streaming source.
                        - **RecordRowPath** *(string) --* **[REQUIRED]**
                          The path to the top-level parent that contains the records.
                      - **CSVMappingParameters** *(dict) --*
                        Provides additional mapping information when the record format uses delimiters (for example, CSV).
                        - **RecordRowDelimiter** *(string) --* **[REQUIRED]**
                          The row delimiter. For example, in a CSV format, *\'\n\'* is the typical row delimiter.
                        - **RecordColumnDelimiter** *(string) --* **[REQUIRED]**
                          The column delimiter. For example, in a CSV format, a comma (\",\") is the typical column delimiter.
                  - **RecordEncoding** *(string) --*
                    Specifies the encoding of the records in the streaming source. For example, UTF-8.
                  - **RecordColumns** *(list) --* **[REQUIRED]**
                    A list of ``RecordColumn`` objects.
                    - *(dict) --*
                      For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
                      Also used to describe the format of the reference data source.
                      - **Name** *(string) --* **[REQUIRED]**
                        The name of the column that is created in the in-application input stream or reference table.
                      - **Mapping** *(string) --*
                        A reference to the data element in the streaming input of the reference data source.
                      - **SqlType** *(string) --* **[REQUIRED]**
                        The type of column created in the in-application input stream or reference table.
          - **ApplicationCodeConfigurationUpdate** *(dict) --*
            Describes updates to a Java-based Kinesis Data Analytics application\'s code configuration.
            - **CodeContentTypeUpdate** *(string) --*
              Describes updates to the code content type.
            - **CodeContentUpdate** *(dict) --*
              Describes updates to the code content of an application.
              - **TextContentUpdate** *(string) --*
                Describes an update to the text code for an application.
              - **ZipFileContentUpdate** *(bytes) --*
                Describes an update to the zipped code for an application.
              - **S3ContentLocationUpdate** *(dict) --*
                Describes an update to the location of code for an application.
                - **BucketARNUpdate** *(string) --*
                  The new Amazon Resource Name (ARN) for the S3 bucket containing the application code.
                - **FileKeyUpdate** *(string) --*
                  The new file key for the object containing the application code.
                - **ObjectVersionUpdate** *(string) --*
                  The new version of the object containing the application code.
          - **FlinkApplicationConfigurationUpdate** *(dict) --*
            Describes updates to a Java-based Kinesis Data Analytics application\'s configuration.
            - **CheckpointConfigurationUpdate** *(dict) --*
              Describes updates to an application\'s checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance.
              - **ConfigurationTypeUpdate** *(string) --*
                Describes updates to whether the application uses the default checkpointing behavior of Kinesis Data Analytics.
              - **CheckpointingEnabledUpdate** *(boolean) --*
                Describes updates to whether checkpointing is enabled for an application.
              - **CheckpointIntervalUpdate** *(integer) --*
                Describes updates to the interval in milliseconds between checkpoint operations.
              - **MinPauseBetweenCheckpointsUpdate** *(integer) --*
                Describes updates to the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start.
            - **MonitoringConfigurationUpdate** *(dict) --*
              Describes updates to the configuration parameters for Amazon CloudWatch logging for an application.
              - **ConfigurationTypeUpdate** *(string) --*
                Describes updates to whether to use the default CloudWatch logging configuration for an application.
              - **MetricsLevelUpdate** *(string) --*
                Describes updates to the granularity of the CloudWatch Logs for an application.
              - **LogLevelUpdate** *(string) --*
                Describes updates to the verbosity of the CloudWatch Logs for an application.
            - **ParallelismConfigurationUpdate** *(dict) --*
              Describes updates to the parameters for how an application executes multiple tasks simultaneously.
              - **ConfigurationTypeUpdate** *(string) --*
                Describes updates to whether the application uses the default parallelism for the Kinesis Data Analytics service, or if a custom parallelism is used.
              - **ParallelismUpdate** *(integer) --*
                Describes updates to the initial number of parallel tasks an application can perform.
              - **ParallelismPerKPUUpdate** *(integer) --*
                Describes updates to the number of parallel tasks an application can perform per Kinesis Processing Unit (KPU) used by the application.
              - **AutoScalingEnabledUpdate** *(boolean) --*
                Describes updates to whether the Kinesis Data Analytics service can increase the parallelism of the application in response to increased throughput.
          - **EnvironmentPropertyUpdates** *(dict) --*
            Describes updates to the environment properties for a Java-based Kinesis Data Analytics application.
            - **PropertyGroups** *(list) --* **[REQUIRED]**
              Describes updates to the execution property groups.
              - *(dict) --*
                Property key-value pairs passed into a Java-based Kinesis Data Analytics application.
                - **PropertyGroupId** *(string) --* **[REQUIRED]**
                  Describes the key of an application execution property key-value pair.
                - **PropertyMap** *(dict) --* **[REQUIRED]**
                  Describes the value of an application execution property key-value pair.
                  - *(string) --*
                    - *(string) --*
          - **ApplicationSnapshotConfigurationUpdate** *(dict) --*
            Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.
            - **SnapshotsEnabledUpdate** *(boolean) --* **[REQUIRED]**
              Describes updates to whether snapshots are enabled for a Java-based Kinesis Data Analytics application.
        :type ServiceExecutionRoleUpdate: string
        :param ServiceExecutionRoleUpdate:
          Describes updates to the service execution role.
        :type RunConfigurationUpdate: dict
        :param RunConfigurationUpdate:
          Describes updates to the application\'s starting parameters.
          - **ApplicationRestoreConfiguration** *(dict) --*
            Describes updates to the restore behavior of a restarting application.
            - **ApplicationRestoreType** *(string) --* **[REQUIRED]**
              Specifies how the application should be restored.
            - **SnapshotName** *(string) --*
              The identifier of an existing snapshot of application state to use to restart an application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is specified for the ``ApplicationRestoreType`` .
        :type CloudWatchLoggingOptionUpdates: list
        :param CloudWatchLoggingOptionUpdates:
          Describes application Amazon CloudWatch logging option updates. You can only update existing CloudWatch logging options with this action. To add a new CloudWatch logging option, use  AddApplicationCloudWatchLoggingOption .
          - *(dict) --*
            Describes the Amazon CloudWatch logging option updates.
            - **CloudWatchLoggingOptionId** *(string) --* **[REQUIRED]**
              The ID of the CloudWatch logging option to update
            - **LogStreamARNUpdate** *(string) --*
              The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.
        :rtype: dict
        :returns:
        """
        pass
