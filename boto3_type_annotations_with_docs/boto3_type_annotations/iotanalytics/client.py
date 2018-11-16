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
    def batch_put_message(self, channelName: str, messages: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/BatchPutMessage>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_put_message(
              channelName=\'string\',
              messages=[
                  {
                      \'messageId\': \'string\',
                      \'payload\': b\'bytes\'
                  },
              ]
          )
        :type channelName: string
        :param channelName: **[REQUIRED]** 
        
          The name of the channel where the messages are sent.
        
        :type messages: list
        :param messages: **[REQUIRED]** 
        
          The list of messages to be sent. Each message has format: \'{ \"messageId\": \"string\", \"payload\": \"string\"}\'.
        
          - *(dict) --* 
        
            Information about a message.
        
            - **messageId** *(string) --* **[REQUIRED]** 
        
              The ID you wish to assign to the message. Each \"messageId\" must be unique within each batch sent.
        
            - **payload** *(bytes) --* **[REQUIRED]** 
        
              The payload of the message. This may be a JSON string or a Base64-encoded string representing binary data (in which case you must decode it by means of a pipeline activity).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'batchPutMessageErrorEntries\': [
                    {
                        \'messageId\': \'string\',
                        \'errorCode\': \'string\',
                        \'errorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **batchPutMessageErrorEntries** *(list) --* 
        
              A list of any errors encountered when sending the messages to the channel.
        
              - *(dict) --* 
        
                Contains informations about errors.
        
                - **messageId** *(string) --* 
        
                  The ID of the message that caused the error. (See the value corresponding to the \"messageId\" key in the message object.)
        
                - **errorCode** *(string) --* 
        
                  The code associated with the error.
        
                - **errorMessage** *(string) --* 
        
                  The message associated with the error.
        
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

    def cancel_pipeline_reprocessing(self, pipelineName: str, reprocessingId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/CancelPipelineReprocessing>`_
        
        **Request Syntax** 
        ::
        
          response = client.cancel_pipeline_reprocessing(
              pipelineName=\'string\',
              reprocessingId=\'string\'
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]** 
        
          The name of pipeline for which data reprocessing is canceled.
        
        :type reprocessingId: string
        :param reprocessingId: **[REQUIRED]** 
        
          The ID of the reprocessing task (returned by \"StartPipelineReprocessing\").
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def create_channel(self, channelName: str, retentionPeriod: Dict = None, tags: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/CreateChannel>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_channel(
              channelName=\'string\',
              retentionPeriod={
                  \'unlimited\': True|False,
                  \'numberOfDays\': 123
              },
              tags=[
                  {
                      \'key\': \'string\',
                      \'value\': \'string\'
                  },
              ]
          )
        :type channelName: string
        :param channelName: **[REQUIRED]** 
        
          The name of the channel.
        
        :type retentionPeriod: dict
        :param retentionPeriod: 
        
          How long, in days, message data is kept for the channel.
        
          - **unlimited** *(boolean) --* 
        
            If true, message data is kept indefinitely.
        
          - **numberOfDays** *(integer) --* 
        
            The number of days that message data is kept. The \"unlimited\" parameter must be false.
        
        :type tags: list
        :param tags: 
        
          Metadata which can be used to manage the channel.
        
          - *(dict) --* 
        
            A set of key/value pairs which are used to manage the resource.
        
            - **key** *(string) --* **[REQUIRED]** 
        
              The tag\'s key.
        
            - **value** *(string) --* **[REQUIRED]** 
        
              The tag\'s value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'channelName\': \'string\',
                \'channelArn\': \'string\',
                \'retentionPeriod\': {
                    \'unlimited\': True|False,
                    \'numberOfDays\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **channelName** *(string) --* 
        
              The name of the channel.
        
            - **channelArn** *(string) --* 
        
              The ARN of the channel.
        
            - **retentionPeriod** *(dict) --* 
        
              How long, in days, message data is kept for the channel.
        
              - **unlimited** *(boolean) --* 
        
                If true, message data is kept indefinitely.
        
              - **numberOfDays** *(integer) --* 
        
                The number of days that message data is kept. The \"unlimited\" parameter must be false.
        
        """
        pass

    def create_dataset(self, datasetName: str, actions: List, triggers: List = None, retentionPeriod: Dict = None, tags: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/CreateDataset>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_dataset(
              datasetName=\'string\',
              actions=[
                  {
                      \'actionName\': \'string\',
                      \'queryAction\': {
                          \'sqlQuery\': \'string\',
                          \'filters\': [
                              {
                                  \'deltaTime\': {
                                      \'offsetSeconds\': 123,
                                      \'timeExpression\': \'string\'
                                  }
                              },
                          ]
                      },
                      \'containerAction\': {
                          \'image\': \'string\',
                          \'executionRoleArn\': \'string\',
                          \'resourceConfiguration\': {
                              \'computeType\': \'ACU_1\'|\'ACU_2\',
                              \'volumeSizeInGB\': 123
                          },
                          \'variables\': [
                              {
                                  \'name\': \'string\',
                                  \'stringValue\': \'string\',
                                  \'doubleValue\': 123.0,
                                  \'datasetContentVersionValue\': {
                                      \'datasetName\': \'string\'
                                  },
                                  \'outputFileUriValue\': {
                                      \'fileName\': \'string\'
                                  }
                              },
                          ]
                      }
                  },
              ],
              triggers=[
                  {
                      \'schedule\': {
                          \'expression\': \'string\'
                      },
                      \'dataset\': {
                          \'name\': \'string\'
                      }
                  },
              ],
              retentionPeriod={
                  \'unlimited\': True|False,
                  \'numberOfDays\': 123
              },
              tags=[
                  {
                      \'key\': \'string\',
                      \'value\': \'string\'
                  },
              ]
          )
        :type datasetName: string
        :param datasetName: **[REQUIRED]** 
        
          The name of the data set.
        
        :type actions: list
        :param actions: **[REQUIRED]** 
        
          A list of actions that create the data set contents.
        
          - *(dict) --* 
        
            A \"DatasetAction\" object specifying the query that creates the data set content.
        
            - **actionName** *(string) --* 
        
              The name of the data set action by which data set contents are automatically created.
        
            - **queryAction** *(dict) --* 
        
              An \"SqlQueryDatasetAction\" object that contains the SQL query to modify the message.
        
              - **sqlQuery** *(string) --* **[REQUIRED]** 
        
                A SQL query string.
        
              - **filters** *(list) --* 
        
                Pre-filters applied to message data.
        
                - *(dict) --* 
        
                  Information which is used to filter message data, to segregate it according to the time frame in which it arrives.
        
                  - **deltaTime** *(dict) --* 
        
                    Used to limit data to that which has arrived since the last execution of the action. When you create data set contents using message data from a specified time frame, some message data may still be \"in flight\" when processing begins, and so will not arrive in time to be processed. Use this field to make allowances for the \"in flight\" time of you message data, so that data not processed from a previous time frame will be included with the next time frame. Without this, missed message data would be excluded from processing during the next time frame as well, because its timestamp places it within the previous time frame.
        
                    - **offsetSeconds** *(integer) --* **[REQUIRED]** 
        
                      The number of seconds of estimated \"in flight\" lag time of message data.
        
                    - **timeExpression** *(string) --* **[REQUIRED]** 
        
                      An expression by which the time of the message data may be determined. This may be the name of a timestamp field, or a SQL expression which is used to derive the time the message data was generated.
        
            - **containerAction** *(dict) --* 
        
              Information which allows the system to run a containerized application in order to create the data set contents. The application must be in a Docker container along with any needed support libraries.
        
              - **image** *(string) --* **[REQUIRED]** 
        
                The ARN of the Docker container stored in your account. The Docker container contains an application and needed support libraries and is used to generate data set contents.
        
              - **executionRoleArn** *(string) --* **[REQUIRED]** 
        
                The ARN of the role which gives permission to the system to access needed resources in order to run the \"containerAction\". This includes, at minimum, permission to retrieve the data set contents which are the input to the containerized application.
        
              - **resourceConfiguration** *(dict) --* **[REQUIRED]** 
        
                Configuration of the resource which executes the \"containerAction\".
        
                - **computeType** *(string) --* **[REQUIRED]** 
        
                  The type of the compute resource used to execute the \"containerAction\". Possible values are: ACU_1 (vCPU=4, memory=16GiB) or ACU_2 (vCPU=8, memory=32GiB).
        
                - **volumeSizeInGB** *(integer) --* **[REQUIRED]** 
        
                  The size (in GB) of the persistent storage available to the resource instance used to execute the \"containerAction\" (min: 1, max: 50).
        
              - **variables** *(list) --* 
        
                The values of variables used within the context of the execution of the containerized application (basically, parameters passed to the application). Each variable must have a name and a value given by one of \"stringValue\", \"datasetContentVersionValue\", or \"outputFileUriValue\".
        
                - *(dict) --* 
        
                  An instance of a variable to be passed to the \"containerAction\" execution. Each variable must have a name and a value given by one of \"stringValue\", \"datasetContentVersionValue\", or \"outputFileUriValue\".
        
                  - **name** *(string) --* **[REQUIRED]** 
        
                    The name of the variable.
        
                  - **stringValue** *(string) --* 
        
                    The value of the variable as a string.
        
                  - **doubleValue** *(float) --* 
        
                    The value of the variable as a double (numeric).
        
                  - **datasetContentVersionValue** *(dict) --* 
        
                    The value of the variable as a structure that specifies a data set content version.
        
                    - **datasetName** *(string) --* **[REQUIRED]** 
        
                      The name of the data set whose latest contents will be used as input to the notebook or application.
        
                  - **outputFileUriValue** *(dict) --* 
        
                    The value of the variable as a structure that specifies an output file URI.
        
                    - **fileName** *(string) --* **[REQUIRED]** 
        
                      The URI of the location where data set contents are stored, usually the URI of a file in an S3 bucket.
        
        :type triggers: list
        :param triggers: 
        
          A list of triggers. A trigger causes data set contents to be populated at a specified time interval or when another data set\'s contents are created. The list of triggers can be empty or contain up to five **DataSetTrigger** objects.
        
          - *(dict) --* 
        
            The \"DatasetTrigger\" that specifies when the data set is automatically updated.
        
            - **schedule** *(dict) --* 
        
              The \"Schedule\" when the trigger is initiated.
        
              - **expression** *(string) --* 
        
                The expression that defines when to trigger an update. For more information, see `Schedule Expressions for Rules <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__ in the Amazon CloudWatch documentation.
        
            - **dataset** *(dict) --* 
        
              The data set whose content creation will trigger the creation of this data set\'s contents.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the data set whose content generation will trigger the new data set content generation.
        
        :type retentionPeriod: dict
        :param retentionPeriod: 
        
          [Optional] How long, in days, message data is kept for the data set. If not given or set to null, the latest version of the dataset content plus the latest succeeded version (if they are different) are retained for at most 90 days.
        
          - **unlimited** *(boolean) --* 
        
            If true, message data is kept indefinitely.
        
          - **numberOfDays** *(integer) --* 
        
            The number of days that message data is kept. The \"unlimited\" parameter must be false.
        
        :type tags: list
        :param tags: 
        
          Metadata which can be used to manage the data set.
        
          - *(dict) --* 
        
            A set of key/value pairs which are used to manage the resource.
        
            - **key** *(string) --* **[REQUIRED]** 
        
              The tag\'s key.
        
            - **value** *(string) --* **[REQUIRED]** 
        
              The tag\'s value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'datasetName\': \'string\',
                \'datasetArn\': \'string\',
                \'retentionPeriod\': {
                    \'unlimited\': True|False,
                    \'numberOfDays\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **datasetName** *(string) --* 
        
              The name of the data set.
        
            - **datasetArn** *(string) --* 
        
              The ARN of the data set.
        
            - **retentionPeriod** *(dict) --* 
        
              How long, in days, message data is kept for the data set.
        
              - **unlimited** *(boolean) --* 
        
                If true, message data is kept indefinitely.
        
              - **numberOfDays** *(integer) --* 
        
                The number of days that message data is kept. The \"unlimited\" parameter must be false.
        
        """
        pass

    def create_dataset_content(self, datasetName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/CreateDatasetContent>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_dataset_content(
              datasetName=\'string\'
          )
        :type datasetName: string
        :param datasetName: **[REQUIRED]** 
        
          The name of the data set.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'versionId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **versionId** *(string) --* 
        
              The version ID of the data set contents which are being created.
        
        """
        pass

    def create_datastore(self, datastoreName: str, retentionPeriod: Dict = None, tags: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/CreateDatastore>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_datastore(
              datastoreName=\'string\',
              retentionPeriod={
                  \'unlimited\': True|False,
                  \'numberOfDays\': 123
              },
              tags=[
                  {
                      \'key\': \'string\',
                      \'value\': \'string\'
                  },
              ]
          )
        :type datastoreName: string
        :param datastoreName: **[REQUIRED]** 
        
          The name of the data store.
        
        :type retentionPeriod: dict
        :param retentionPeriod: 
        
          How long, in days, message data is kept for the data store.
        
          - **unlimited** *(boolean) --* 
        
            If true, message data is kept indefinitely.
        
          - **numberOfDays** *(integer) --* 
        
            The number of days that message data is kept. The \"unlimited\" parameter must be false.
        
        :type tags: list
        :param tags: 
        
          Metadata which can be used to manage the data store.
        
          - *(dict) --* 
        
            A set of key/value pairs which are used to manage the resource.
        
            - **key** *(string) --* **[REQUIRED]** 
        
              The tag\'s key.
        
            - **value** *(string) --* **[REQUIRED]** 
        
              The tag\'s value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'datastoreName\': \'string\',
                \'datastoreArn\': \'string\',
                \'retentionPeriod\': {
                    \'unlimited\': True|False,
                    \'numberOfDays\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **datastoreName** *(string) --* 
        
              The name of the data store.
        
            - **datastoreArn** *(string) --* 
        
              The ARN of the data store.
        
            - **retentionPeriod** *(dict) --* 
        
              How long, in days, message data is kept for the data store.
        
              - **unlimited** *(boolean) --* 
        
                If true, message data is kept indefinitely.
        
              - **numberOfDays** *(integer) --* 
        
                The number of days that message data is kept. The \"unlimited\" parameter must be false.
        
        """
        pass

    def create_pipeline(self, pipelineName: str, pipelineActivities: List, tags: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/CreatePipeline>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_pipeline(
              pipelineName=\'string\',
              pipelineActivities=[
                  {
                      \'channel\': {
                          \'name\': \'string\',
                          \'channelName\': \'string\',
                          \'next\': \'string\'
                      },
                      \'lambda\': {
                          \'name\': \'string\',
                          \'lambdaName\': \'string\',
                          \'batchSize\': 123,
                          \'next\': \'string\'
                      },
                      \'datastore\': {
                          \'name\': \'string\',
                          \'datastoreName\': \'string\'
                      },
                      \'addAttributes\': {
                          \'name\': \'string\',
                          \'attributes\': {
                              \'string\': \'string\'
                          },
                          \'next\': \'string\'
                      },
                      \'removeAttributes\': {
                          \'name\': \'string\',
                          \'attributes\': [
                              \'string\',
                          ],
                          \'next\': \'string\'
                      },
                      \'selectAttributes\': {
                          \'name\': \'string\',
                          \'attributes\': [
                              \'string\',
                          ],
                          \'next\': \'string\'
                      },
                      \'filter\': {
                          \'name\': \'string\',
                          \'filter\': \'string\',
                          \'next\': \'string\'
                      },
                      \'math\': {
                          \'name\': \'string\',
                          \'attribute\': \'string\',
                          \'math\': \'string\',
                          \'next\': \'string\'
                      },
                      \'deviceRegistryEnrich\': {
                          \'name\': \'string\',
                          \'attribute\': \'string\',
                          \'thingName\': \'string\',
                          \'roleArn\': \'string\',
                          \'next\': \'string\'
                      },
                      \'deviceShadowEnrich\': {
                          \'name\': \'string\',
                          \'attribute\': \'string\',
                          \'thingName\': \'string\',
                          \'roleArn\': \'string\',
                          \'next\': \'string\'
                      }
                  },
              ],
              tags=[
                  {
                      \'key\': \'string\',
                      \'value\': \'string\'
                  },
              ]
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]** 
        
          The name of the pipeline.
        
        :type pipelineActivities: list
        :param pipelineActivities: **[REQUIRED]** 
        
          A list of pipeline activities.
        
          The list can be 1-25 **PipelineActivity** objects. Activities perform transformations on your messages, such as removing, renaming, or adding message attributes; filtering messages based on attribute values; invoking your Lambda functions on messages for advanced processing; or performing mathematical transformations to normalize device data.
        
          - *(dict) --* 
        
            An activity that performs a transformation on a message.
        
            - **channel** *(dict) --* 
        
              Determines the source of the messages to be processed.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'channel\' activity.
        
              - **channelName** *(string) --* **[REQUIRED]** 
        
                The name of the channel from which the messages are processed.
        
              - **next** *(string) --* 
        
                The next activity in the pipeline.
        
            - **lambda** *(dict) --* 
        
              Runs a Lambda function to modify the message.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'lambda\' activity.
        
              - **lambdaName** *(string) --* **[REQUIRED]** 
        
                The name of the Lambda function that is run on the message.
        
              - **batchSize** *(integer) --* **[REQUIRED]** 
        
                The number of messages passed to the Lambda function for processing.
        
                The AWS Lambda function must be able to process all of these messages within five minutes, which is the maximum timeout duration for Lambda functions.
        
              - **next** *(string) --* 
        
                The next activity in the pipeline.
        
            - **datastore** *(dict) --* 
        
              Specifies where to store the processed message data.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'datastore\' activity.
        
              - **datastoreName** *(string) --* **[REQUIRED]** 
        
                The name of the data store where processed messages are stored.
        
            - **addAttributes** *(dict) --* 
        
              Adds other attributes based on existing attributes in the message.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'addAttributes\' activity.
        
              - **attributes** *(dict) --* **[REQUIRED]** 
        
                A list of 1-50 \"AttributeNameMapping\" objects that map an existing attribute to a new attribute.
        
                .. note::
        
                  The existing attributes remain in the message, so if you want to remove the originals, use \"RemoveAttributeActivity\".
        
                - *(string) --* 
        
                  - *(string) --* 
        
              - **next** *(string) --* 
        
                The next activity in the pipeline.
        
            - **removeAttributes** *(dict) --* 
        
              Removes attributes from a message.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'removeAttributes\' activity.
        
              - **attributes** *(list) --* **[REQUIRED]** 
        
                A list of 1-50 attributes to remove from the message.
        
                - *(string) --* 
        
              - **next** *(string) --* 
        
                The next activity in the pipeline.
        
            - **selectAttributes** *(dict) --* 
        
              Creates a new message using only the specified attributes from the original message. 
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'selectAttributes\' activity.
        
              - **attributes** *(list) --* **[REQUIRED]** 
        
                A list of the attributes to select from the message.
        
                - *(string) --* 
        
              - **next** *(string) --* 
        
                The next activity in the pipeline.
        
            - **filter** *(dict) --* 
        
              Filters a message based on its attributes.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'filter\' activity.
        
              - **filter** *(string) --* **[REQUIRED]** 
        
                An expression that looks like a SQL WHERE clause that must return a Boolean value.
        
              - **next** *(string) --* 
        
                The next activity in the pipeline.
        
            - **math** *(dict) --* 
        
              Computes an arithmetic expression using the message\'s attributes and adds it to the message.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'math\' activity.
        
              - **attribute** *(string) --* **[REQUIRED]** 
        
                The name of the attribute that will contain the result of the math operation.
        
              - **math** *(string) --* **[REQUIRED]** 
        
                An expression that uses one or more existing attributes and must return an integer value.
        
              - **next** *(string) --* 
        
                The next activity in the pipeline.
        
            - **deviceRegistryEnrich** *(dict) --* 
        
              Adds data from the AWS IoT device registry to your message.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'deviceRegistryEnrich\' activity.
        
              - **attribute** *(string) --* **[REQUIRED]** 
        
                The name of the attribute that is added to the message.
        
              - **thingName** *(string) --* **[REQUIRED]** 
        
                The name of the IoT device whose registry information is added to the message.
        
              - **roleArn** *(string) --* **[REQUIRED]** 
        
                The ARN of the role that allows access to the device\'s registry information.
        
              - **next** *(string) --* 
        
                The next activity in the pipeline.
        
            - **deviceShadowEnrich** *(dict) --* 
        
              Adds information from the AWS IoT Device Shadows service to a message.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'deviceShadowEnrich\' activity.
        
              - **attribute** *(string) --* **[REQUIRED]** 
        
                The name of the attribute that is added to the message.
        
              - **thingName** *(string) --* **[REQUIRED]** 
        
                The name of the IoT device whose shadow information is added to the message.
        
              - **roleArn** *(string) --* **[REQUIRED]** 
        
                The ARN of the role that allows access to the device\'s shadow.
        
              - **next** *(string) --* 
        
                The next activity in the pipeline.
        
        :type tags: list
        :param tags: 
        
          Metadata which can be used to manage the pipeline.
        
          - *(dict) --* 
        
            A set of key/value pairs which are used to manage the resource.
        
            - **key** *(string) --* **[REQUIRED]** 
        
              The tag\'s key.
        
            - **value** *(string) --* **[REQUIRED]** 
        
              The tag\'s value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pipelineName\': \'string\',
                \'pipelineArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **pipelineName** *(string) --* 
        
              The name of the pipeline.
        
            - **pipelineArn** *(string) --* 
        
              The ARN of the pipeline.
        
        """
        pass

    def delete_channel(self, channelName: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DeleteChannel>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_channel(
              channelName=\'string\'
          )
        :type channelName: string
        :param channelName: **[REQUIRED]** 
        
          The name of the channel to delete.
        
        :returns: None
        """
        pass

    def delete_dataset(self, datasetName: str) -> NoReturn:
        """
        
        You do not have to delete the content of the data set before you perform this operation.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DeleteDataset>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_dataset(
              datasetName=\'string\'
          )
        :type datasetName: string
        :param datasetName: **[REQUIRED]** 
        
          The name of the data set to delete.
        
        :returns: None
        """
        pass

    def delete_dataset_content(self, datasetName: str, versionId: str = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DeleteDatasetContent>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_dataset_content(
              datasetName=\'string\',
              versionId=\'string\'
          )
        :type datasetName: string
        :param datasetName: **[REQUIRED]** 
        
          The name of the data set whose content is deleted.
        
        :type versionId: string
        :param versionId: 
        
          The version of the data set whose content is deleted. You can also use the strings \"$LATEST\" or \"$LATEST_SUCCEEDED\" to delete the latest or latest successfully completed data set. If not specified, \"$LATEST_SUCCEEDED\" is the default.
        
        :returns: None
        """
        pass

    def delete_datastore(self, datastoreName: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DeleteDatastore>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_datastore(
              datastoreName=\'string\'
          )
        :type datastoreName: string
        :param datastoreName: **[REQUIRED]** 
        
          The name of the data store to delete.
        
        :returns: None
        """
        pass

    def delete_pipeline(self, pipelineName: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DeletePipeline>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_pipeline(
              pipelineName=\'string\'
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]** 
        
          The name of the pipeline to delete.
        
        :returns: None
        """
        pass

    def describe_channel(self, channelName: str, includeStatistics: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DescribeChannel>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_channel(
              channelName=\'string\',
              includeStatistics=True|False
          )
        :type channelName: string
        :param channelName: **[REQUIRED]** 
        
          The name of the channel whose information is retrieved.
        
        :type includeStatistics: boolean
        :param includeStatistics: 
        
          If true, additional statistical information about the channel is included in the response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'channel\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'status\': \'CREATING\'|\'ACTIVE\'|\'DELETING\',
                    \'retentionPeriod\': {
                        \'unlimited\': True|False,
                        \'numberOfDays\': 123
                    },
                    \'creationTime\': datetime(2015, 1, 1),
                    \'lastUpdateTime\': datetime(2015, 1, 1)
                },
                \'statistics\': {
                    \'size\': {
                        \'estimatedSizeInBytes\': 123.0,
                        \'estimatedOn\': datetime(2015, 1, 1)
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **channel** *(dict) --* 
        
              An object that contains information about the channel.
        
              - **name** *(string) --* 
        
                The name of the channel.
        
              - **arn** *(string) --* 
        
                The ARN of the channel.
        
              - **status** *(string) --* 
        
                The status of the channel.
        
              - **retentionPeriod** *(dict) --* 
        
                How long, in days, message data is kept for the channel.
        
                - **unlimited** *(boolean) --* 
        
                  If true, message data is kept indefinitely.
        
                - **numberOfDays** *(integer) --* 
        
                  The number of days that message data is kept. The \"unlimited\" parameter must be false.
        
              - **creationTime** *(datetime) --* 
        
                When the channel was created.
        
              - **lastUpdateTime** *(datetime) --* 
        
                When the channel was last updated.
        
            - **statistics** *(dict) --* 
        
              Statistics about the channel. Included if the \'includeStatistics\' parameter is set to true in the request.
        
              - **size** *(dict) --* 
        
                The estimated size of the channel.
        
                - **estimatedSizeInBytes** *(float) --* 
        
                  The estimated size of the resource in bytes.
        
                - **estimatedOn** *(datetime) --* 
        
                  The time when the estimate of the size of the resource was made.
        
        """
        pass

    def describe_dataset(self, datasetName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DescribeDataset>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_dataset(
              datasetName=\'string\'
          )
        :type datasetName: string
        :param datasetName: **[REQUIRED]** 
        
          The name of the data set whose information is retrieved.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'dataset\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'actions\': [
                        {
                            \'actionName\': \'string\',
                            \'queryAction\': {
                                \'sqlQuery\': \'string\',
                                \'filters\': [
                                    {
                                        \'deltaTime\': {
                                            \'offsetSeconds\': 123,
                                            \'timeExpression\': \'string\'
                                        }
                                    },
                                ]
                            },
                            \'containerAction\': {
                                \'image\': \'string\',
                                \'executionRoleArn\': \'string\',
                                \'resourceConfiguration\': {
                                    \'computeType\': \'ACU_1\'|\'ACU_2\',
                                    \'volumeSizeInGB\': 123
                                },
                                \'variables\': [
                                    {
                                        \'name\': \'string\',
                                        \'stringValue\': \'string\',
                                        \'doubleValue\': 123.0,
                                        \'datasetContentVersionValue\': {
                                            \'datasetName\': \'string\'
                                        },
                                        \'outputFileUriValue\': {
                                            \'fileName\': \'string\'
                                        }
                                    },
                                ]
                            }
                        },
                    ],
                    \'triggers\': [
                        {
                            \'schedule\': {
                                \'expression\': \'string\'
                            },
                            \'dataset\': {
                                \'name\': \'string\'
                            }
                        },
                    ],
                    \'status\': \'CREATING\'|\'ACTIVE\'|\'DELETING\',
                    \'creationTime\': datetime(2015, 1, 1),
                    \'lastUpdateTime\': datetime(2015, 1, 1),
                    \'retentionPeriod\': {
                        \'unlimited\': True|False,
                        \'numberOfDays\': 123
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **dataset** *(dict) --* 
        
              An object that contains information about the data set.
        
              - **name** *(string) --* 
        
                The name of the data set.
        
              - **arn** *(string) --* 
        
                The ARN of the data set.
        
              - **actions** *(list) --* 
        
                The \"DatasetAction\" objects that automatically create the data set contents.
        
                - *(dict) --* 
        
                  A \"DatasetAction\" object specifying the query that creates the data set content.
        
                  - **actionName** *(string) --* 
        
                    The name of the data set action by which data set contents are automatically created.
        
                  - **queryAction** *(dict) --* 
        
                    An \"SqlQueryDatasetAction\" object that contains the SQL query to modify the message.
        
                    - **sqlQuery** *(string) --* 
        
                      A SQL query string.
        
                    - **filters** *(list) --* 
        
                      Pre-filters applied to message data.
        
                      - *(dict) --* 
        
                        Information which is used to filter message data, to segregate it according to the time frame in which it arrives.
        
                        - **deltaTime** *(dict) --* 
        
                          Used to limit data to that which has arrived since the last execution of the action. When you create data set contents using message data from a specified time frame, some message data may still be \"in flight\" when processing begins, and so will not arrive in time to be processed. Use this field to make allowances for the \"in flight\" time of you message data, so that data not processed from a previous time frame will be included with the next time frame. Without this, missed message data would be excluded from processing during the next time frame as well, because its timestamp places it within the previous time frame.
        
                          - **offsetSeconds** *(integer) --* 
        
                            The number of seconds of estimated \"in flight\" lag time of message data.
        
                          - **timeExpression** *(string) --* 
        
                            An expression by which the time of the message data may be determined. This may be the name of a timestamp field, or a SQL expression which is used to derive the time the message data was generated.
        
                  - **containerAction** *(dict) --* 
        
                    Information which allows the system to run a containerized application in order to create the data set contents. The application must be in a Docker container along with any needed support libraries.
        
                    - **image** *(string) --* 
        
                      The ARN of the Docker container stored in your account. The Docker container contains an application and needed support libraries and is used to generate data set contents.
        
                    - **executionRoleArn** *(string) --* 
        
                      The ARN of the role which gives permission to the system to access needed resources in order to run the \"containerAction\". This includes, at minimum, permission to retrieve the data set contents which are the input to the containerized application.
        
                    - **resourceConfiguration** *(dict) --* 
        
                      Configuration of the resource which executes the \"containerAction\".
        
                      - **computeType** *(string) --* 
        
                        The type of the compute resource used to execute the \"containerAction\". Possible values are: ACU_1 (vCPU=4, memory=16GiB) or ACU_2 (vCPU=8, memory=32GiB).
        
                      - **volumeSizeInGB** *(integer) --* 
        
                        The size (in GB) of the persistent storage available to the resource instance used to execute the \"containerAction\" (min: 1, max: 50).
        
                    - **variables** *(list) --* 
        
                      The values of variables used within the context of the execution of the containerized application (basically, parameters passed to the application). Each variable must have a name and a value given by one of \"stringValue\", \"datasetContentVersionValue\", or \"outputFileUriValue\".
        
                      - *(dict) --* 
        
                        An instance of a variable to be passed to the \"containerAction\" execution. Each variable must have a name and a value given by one of \"stringValue\", \"datasetContentVersionValue\", or \"outputFileUriValue\".
        
                        - **name** *(string) --* 
        
                          The name of the variable.
        
                        - **stringValue** *(string) --* 
        
                          The value of the variable as a string.
        
                        - **doubleValue** *(float) --* 
        
                          The value of the variable as a double (numeric).
        
                        - **datasetContentVersionValue** *(dict) --* 
        
                          The value of the variable as a structure that specifies a data set content version.
        
                          - **datasetName** *(string) --* 
        
                            The name of the data set whose latest contents will be used as input to the notebook or application.
        
                        - **outputFileUriValue** *(dict) --* 
        
                          The value of the variable as a structure that specifies an output file URI.
        
                          - **fileName** *(string) --* 
        
                            The URI of the location where data set contents are stored, usually the URI of a file in an S3 bucket.
        
              - **triggers** *(list) --* 
        
                The \"DatasetTrigger\" objects that specify when the data set is automatically updated.
        
                - *(dict) --* 
        
                  The \"DatasetTrigger\" that specifies when the data set is automatically updated.
        
                  - **schedule** *(dict) --* 
        
                    The \"Schedule\" when the trigger is initiated.
        
                    - **expression** *(string) --* 
        
                      The expression that defines when to trigger an update. For more information, see `Schedule Expressions for Rules <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__ in the Amazon CloudWatch documentation.
        
                  - **dataset** *(dict) --* 
        
                    The data set whose content creation will trigger the creation of this data set\'s contents.
        
                    - **name** *(string) --* 
        
                      The name of the data set whose content generation will trigger the new data set content generation.
        
              - **status** *(string) --* 
        
                The status of the data set.
        
              - **creationTime** *(datetime) --* 
        
                When the data set was created.
        
              - **lastUpdateTime** *(datetime) --* 
        
                The last time the data set was updated.
        
              - **retentionPeriod** *(dict) --* 
        
                [Optional] How long, in days, message data is kept for the data set.
        
                - **unlimited** *(boolean) --* 
        
                  If true, message data is kept indefinitely.
        
                - **numberOfDays** *(integer) --* 
        
                  The number of days that message data is kept. The \"unlimited\" parameter must be false.
        
        """
        pass

    def describe_datastore(self, datastoreName: str, includeStatistics: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DescribeDatastore>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_datastore(
              datastoreName=\'string\',
              includeStatistics=True|False
          )
        :type datastoreName: string
        :param datastoreName: **[REQUIRED]** 
        
          The name of the data store
        
        :type includeStatistics: boolean
        :param includeStatistics: 
        
          If true, additional statistical information about the datastore is included in the response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'datastore\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'status\': \'CREATING\'|\'ACTIVE\'|\'DELETING\',
                    \'retentionPeriod\': {
                        \'unlimited\': True|False,
                        \'numberOfDays\': 123
                    },
                    \'creationTime\': datetime(2015, 1, 1),
                    \'lastUpdateTime\': datetime(2015, 1, 1)
                },
                \'statistics\': {
                    \'size\': {
                        \'estimatedSizeInBytes\': 123.0,
                        \'estimatedOn\': datetime(2015, 1, 1)
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **datastore** *(dict) --* 
        
              Information about the data store.
        
              - **name** *(string) --* 
        
                The name of the data store.
        
              - **arn** *(string) --* 
        
                The ARN of the data store.
        
              - **status** *(string) --* 
        
                The status of a data store:
        
                  CREATING  
        
                The data store is being created.
        
                  ACTIVE  
        
                The data store has been created and can be used.
        
                  DELETING  
        
                The data store is being deleted.
        
              - **retentionPeriod** *(dict) --* 
        
                How long, in days, message data is kept for the data store.
        
                - **unlimited** *(boolean) --* 
        
                  If true, message data is kept indefinitely.
        
                - **numberOfDays** *(integer) --* 
        
                  The number of days that message data is kept. The \"unlimited\" parameter must be false.
        
              - **creationTime** *(datetime) --* 
        
                When the data store was created.
        
              - **lastUpdateTime** *(datetime) --* 
        
                The last time the data store was updated.
        
            - **statistics** *(dict) --* 
        
              Additional statistical information about the data store. Included if the \'includeStatistics\' parameter is set to true in the request.
        
              - **size** *(dict) --* 
        
                The estimated size of the data store.
        
                - **estimatedSizeInBytes** *(float) --* 
        
                  The estimated size of the resource in bytes.
        
                - **estimatedOn** *(datetime) --* 
        
                  The time when the estimate of the size of the resource was made.
        
        """
        pass

    def describe_logging_options(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DescribeLoggingOptions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_logging_options()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'loggingOptions\': {
                    \'roleArn\': \'string\',
                    \'level\': \'ERROR\',
                    \'enabled\': True|False
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **loggingOptions** *(dict) --* 
        
              The current settings of the AWS IoT Analytics logging options.
        
              - **roleArn** *(string) --* 
        
                The ARN of the role that grants permission to AWS IoT Analytics to perform logging.
        
              - **level** *(string) --* 
        
                The logging level. Currently, only \"ERROR\" is supported.
        
              - **enabled** *(boolean) --* 
        
                If true, logging is enabled for AWS IoT Analytics.
        
        """
        pass

    def describe_pipeline(self, pipelineName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DescribePipeline>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_pipeline(
              pipelineName=\'string\'
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]** 
        
          The name of the pipeline whose information is retrieved.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pipeline\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'activities\': [
                        {
                            \'channel\': {
                                \'name\': \'string\',
                                \'channelName\': \'string\',
                                \'next\': \'string\'
                            },
                            \'lambda\': {
                                \'name\': \'string\',
                                \'lambdaName\': \'string\',
                                \'batchSize\': 123,
                                \'next\': \'string\'
                            },
                            \'datastore\': {
                                \'name\': \'string\',
                                \'datastoreName\': \'string\'
                            },
                            \'addAttributes\': {
                                \'name\': \'string\',
                                \'attributes\': {
                                    \'string\': \'string\'
                                },
                                \'next\': \'string\'
                            },
                            \'removeAttributes\': {
                                \'name\': \'string\',
                                \'attributes\': [
                                    \'string\',
                                ],
                                \'next\': \'string\'
                            },
                            \'selectAttributes\': {
                                \'name\': \'string\',
                                \'attributes\': [
                                    \'string\',
                                ],
                                \'next\': \'string\'
                            },
                            \'filter\': {
                                \'name\': \'string\',
                                \'filter\': \'string\',
                                \'next\': \'string\'
                            },
                            \'math\': {
                                \'name\': \'string\',
                                \'attribute\': \'string\',
                                \'math\': \'string\',
                                \'next\': \'string\'
                            },
                            \'deviceRegistryEnrich\': {
                                \'name\': \'string\',
                                \'attribute\': \'string\',
                                \'thingName\': \'string\',
                                \'roleArn\': \'string\',
                                \'next\': \'string\'
                            },
                            \'deviceShadowEnrich\': {
                                \'name\': \'string\',
                                \'attribute\': \'string\',
                                \'thingName\': \'string\',
                                \'roleArn\': \'string\',
                                \'next\': \'string\'
                            }
                        },
                    ],
                    \'reprocessingSummaries\': [
                        {
                            \'id\': \'string\',
                            \'status\': \'RUNNING\'|\'SUCCEEDED\'|\'CANCELLED\'|\'FAILED\',
                            \'creationTime\': datetime(2015, 1, 1)
                        },
                    ],
                    \'creationTime\': datetime(2015, 1, 1),
                    \'lastUpdateTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **pipeline** *(dict) --* 
        
              A \"Pipeline\" object that contains information about the pipeline.
        
              - **name** *(string) --* 
        
                The name of the pipeline.
        
              - **arn** *(string) --* 
        
                The ARN of the pipeline.
        
              - **activities** *(list) --* 
        
                The activities that perform transformations on the messages.
        
                - *(dict) --* 
        
                  An activity that performs a transformation on a message.
        
                  - **channel** *(dict) --* 
        
                    Determines the source of the messages to be processed.
        
                    - **name** *(string) --* 
        
                      The name of the \'channel\' activity.
        
                    - **channelName** *(string) --* 
        
                      The name of the channel from which the messages are processed.
        
                    - **next** *(string) --* 
        
                      The next activity in the pipeline.
        
                  - **lambda** *(dict) --* 
        
                    Runs a Lambda function to modify the message.
        
                    - **name** *(string) --* 
        
                      The name of the \'lambda\' activity.
        
                    - **lambdaName** *(string) --* 
        
                      The name of the Lambda function that is run on the message.
        
                    - **batchSize** *(integer) --* 
        
                      The number of messages passed to the Lambda function for processing.
        
                      The AWS Lambda function must be able to process all of these messages within five minutes, which is the maximum timeout duration for Lambda functions.
        
                    - **next** *(string) --* 
        
                      The next activity in the pipeline.
        
                  - **datastore** *(dict) --* 
        
                    Specifies where to store the processed message data.
        
                    - **name** *(string) --* 
        
                      The name of the \'datastore\' activity.
        
                    - **datastoreName** *(string) --* 
        
                      The name of the data store where processed messages are stored.
        
                  - **addAttributes** *(dict) --* 
        
                    Adds other attributes based on existing attributes in the message.
        
                    - **name** *(string) --* 
        
                      The name of the \'addAttributes\' activity.
        
                    - **attributes** *(dict) --* 
        
                      A list of 1-50 \"AttributeNameMapping\" objects that map an existing attribute to a new attribute.
        
                      .. note::
        
                        The existing attributes remain in the message, so if you want to remove the originals, use \"RemoveAttributeActivity\".
        
                      - *(string) --* 
                        
                        - *(string) --* 
                  
                    - **next** *(string) --* 
        
                      The next activity in the pipeline.
        
                  - **removeAttributes** *(dict) --* 
        
                    Removes attributes from a message.
        
                    - **name** *(string) --* 
        
                      The name of the \'removeAttributes\' activity.
        
                    - **attributes** *(list) --* 
        
                      A list of 1-50 attributes to remove from the message.
        
                      - *(string) --* 
                  
                    - **next** *(string) --* 
        
                      The next activity in the pipeline.
        
                  - **selectAttributes** *(dict) --* 
        
                    Creates a new message using only the specified attributes from the original message. 
        
                    - **name** *(string) --* 
        
                      The name of the \'selectAttributes\' activity.
        
                    - **attributes** *(list) --* 
        
                      A list of the attributes to select from the message.
        
                      - *(string) --* 
                  
                    - **next** *(string) --* 
        
                      The next activity in the pipeline.
        
                  - **filter** *(dict) --* 
        
                    Filters a message based on its attributes.
        
                    - **name** *(string) --* 
        
                      The name of the \'filter\' activity.
        
                    - **filter** *(string) --* 
        
                      An expression that looks like a SQL WHERE clause that must return a Boolean value.
        
                    - **next** *(string) --* 
        
                      The next activity in the pipeline.
        
                  - **math** *(dict) --* 
        
                    Computes an arithmetic expression using the message\'s attributes and adds it to the message.
        
                    - **name** *(string) --* 
        
                      The name of the \'math\' activity.
        
                    - **attribute** *(string) --* 
        
                      The name of the attribute that will contain the result of the math operation.
        
                    - **math** *(string) --* 
        
                      An expression that uses one or more existing attributes and must return an integer value.
        
                    - **next** *(string) --* 
        
                      The next activity in the pipeline.
        
                  - **deviceRegistryEnrich** *(dict) --* 
        
                    Adds data from the AWS IoT device registry to your message.
        
                    - **name** *(string) --* 
        
                      The name of the \'deviceRegistryEnrich\' activity.
        
                    - **attribute** *(string) --* 
        
                      The name of the attribute that is added to the message.
        
                    - **thingName** *(string) --* 
        
                      The name of the IoT device whose registry information is added to the message.
        
                    - **roleArn** *(string) --* 
        
                      The ARN of the role that allows access to the device\'s registry information.
        
                    - **next** *(string) --* 
        
                      The next activity in the pipeline.
        
                  - **deviceShadowEnrich** *(dict) --* 
        
                    Adds information from the AWS IoT Device Shadows service to a message.
        
                    - **name** *(string) --* 
        
                      The name of the \'deviceShadowEnrich\' activity.
        
                    - **attribute** *(string) --* 
        
                      The name of the attribute that is added to the message.
        
                    - **thingName** *(string) --* 
        
                      The name of the IoT device whose shadow information is added to the message.
        
                    - **roleArn** *(string) --* 
        
                      The ARN of the role that allows access to the device\'s shadow.
        
                    - **next** *(string) --* 
        
                      The next activity in the pipeline.
        
              - **reprocessingSummaries** *(list) --* 
        
                A summary of information about the pipeline reprocessing.
        
                - *(dict) --* 
        
                  Information about pipeline reprocessing.
        
                  - **id** *(string) --* 
        
                    The \'reprocessingId\' returned by \"StartPipelineReprocessing\".
        
                  - **status** *(string) --* 
        
                    The status of the pipeline reprocessing.
        
                  - **creationTime** *(datetime) --* 
        
                    The time the pipeline reprocessing was created.
        
              - **creationTime** *(datetime) --* 
        
                When the pipeline was created.
        
              - **lastUpdateTime** *(datetime) --* 
        
                The last time the pipeline was updated.
        
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

    def get_dataset_content(self, datasetName: str, versionId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/GetDatasetContent>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_dataset_content(
              datasetName=\'string\',
              versionId=\'string\'
          )
        :type datasetName: string
        :param datasetName: **[REQUIRED]** 
        
          The name of the data set whose contents are retrieved.
        
        :type versionId: string
        :param versionId: 
        
          The version of the data set whose contents are retrieved. You can also use the strings \"$LATEST\" or \"$LATEST_SUCCEEDED\" to retrieve the contents of the latest or latest successfully completed data set. If not specified, \"$LATEST_SUCCEEDED\" is the default.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'entries\': [
                    {
                        \'entryName\': \'string\',
                        \'dataURI\': \'string\'
                    },
                ],
                \'timestamp\': datetime(2015, 1, 1),
                \'status\': {
                    \'state\': \'CREATING\'|\'SUCCEEDED\'|\'FAILED\',
                    \'reason\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **entries** *(list) --* 
        
              A list of \"DatasetEntry\" objects.
        
              - *(dict) --* 
        
                The reference to a data set entry.
        
                - **entryName** *(string) --* 
        
                  The name of the data set item.
        
                - **dataURI** *(string) --* 
        
                  The pre-signed URI of the data set item.
        
            - **timestamp** *(datetime) --* 
        
              The time when the request was made.
        
            - **status** *(dict) --* 
        
              The status of the data set content.
        
              - **state** *(string) --* 
        
                The state of the data set contents. Can be one of \"READY\", \"CREATING\", \"SUCCEEDED\" or \"FAILED\".
        
              - **reason** *(string) --* 
        
                The reason the data set contents are in this state.
        
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

    def list_channels(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/ListChannels>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_channels(
              nextToken=\'string\',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken: 
        
          The token for the next set of results.
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of results to return in this request.
        
          The default value is 100.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'channelSummaries\': [
                    {
                        \'channelName\': \'string\',
                        \'status\': \'CREATING\'|\'ACTIVE\'|\'DELETING\',
                        \'creationTime\': datetime(2015, 1, 1),
                        \'lastUpdateTime\': datetime(2015, 1, 1)
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **channelSummaries** *(list) --* 
        
              A list of \"ChannelSummary\" objects.
        
              - *(dict) --* 
        
                A summary of information about a channel.
        
                - **channelName** *(string) --* 
        
                  The name of the channel.
        
                - **status** *(string) --* 
        
                  The status of the channel.
        
                - **creationTime** *(datetime) --* 
        
                  When the channel was created.
        
                - **lastUpdateTime** *(datetime) --* 
        
                  The last time the channel was updated.
        
            - **nextToken** *(string) --* 
        
              The token to retrieve the next set of results, or ``null`` if there are no more results.
        
        """
        pass

    def list_dataset_contents(self, datasetName: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/ListDatasetContents>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_dataset_contents(
              datasetName=\'string\',
              nextToken=\'string\',
              maxResults=123
          )
        :type datasetName: string
        :param datasetName: **[REQUIRED]** 
        
          The name of the data set whose contents information you want to list.
        
        :type nextToken: string
        :param nextToken: 
        
          The token for the next set of results.
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of results to return in this request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'datasetContentSummaries\': [
                    {
                        \'version\': \'string\',
                        \'status\': {
                            \'state\': \'CREATING\'|\'SUCCEEDED\'|\'FAILED\',
                            \'reason\': \'string\'
                        },
                        \'creationTime\': datetime(2015, 1, 1),
                        \'scheduleTime\': datetime(2015, 1, 1)
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **datasetContentSummaries** *(list) --* 
        
              Summary information about data set contents that have been created.
        
              - *(dict) --* 
        
                Summary information about data set contents.
        
                - **version** *(string) --* 
        
                  The version of the data set contents.
        
                - **status** *(dict) --* 
        
                  The status of the data set contents.
        
                  - **state** *(string) --* 
        
                    The state of the data set contents. Can be one of \"READY\", \"CREATING\", \"SUCCEEDED\" or \"FAILED\".
        
                  - **reason** *(string) --* 
        
                    The reason the data set contents are in this state.
        
                - **creationTime** *(datetime) --* 
        
                  The actual time the creation of the data set contents was started.
        
                - **scheduleTime** *(datetime) --* 
        
                  The time the creation of the data set contents was scheduled to start.
        
            - **nextToken** *(string) --* 
        
              The token to retrieve the next set of results, or ``null`` if there are no more results.
        
        """
        pass

    def list_datasets(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/ListDatasets>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_datasets(
              nextToken=\'string\',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken: 
        
          The token for the next set of results.
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of results to return in this request.
        
          The default value is 100.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'datasetSummaries\': [
                    {
                        \'datasetName\': \'string\',
                        \'status\': \'CREATING\'|\'ACTIVE\'|\'DELETING\',
                        \'creationTime\': datetime(2015, 1, 1),
                        \'lastUpdateTime\': datetime(2015, 1, 1),
                        \'triggers\': [
                            {
                                \'schedule\': {
                                    \'expression\': \'string\'
                                },
                                \'dataset\': {
                                    \'name\': \'string\'
                                }
                            },
                        ],
                        \'actions\': [
                            {
                                \'actionName\': \'string\',
                                \'actionType\': \'QUERY\'|\'CONTAINER\'
                            },
                        ]
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **datasetSummaries** *(list) --* 
        
              A list of \"DatasetSummary\" objects.
        
              - *(dict) --* 
        
                A summary of information about a data set.
        
                - **datasetName** *(string) --* 
        
                  The name of the data set.
        
                - **status** *(string) --* 
        
                  The status of the data set.
        
                - **creationTime** *(datetime) --* 
        
                  The time the data set was created.
        
                - **lastUpdateTime** *(datetime) --* 
        
                  The last time the data set was updated.
        
                - **triggers** *(list) --* 
        
                  A list of triggers. A trigger causes data set content to be populated at a specified time interval or when another data set is populated. The list of triggers can be empty or contain up to five DataSetTrigger objects
        
                  - *(dict) --* 
        
                    The \"DatasetTrigger\" that specifies when the data set is automatically updated.
        
                    - **schedule** *(dict) --* 
        
                      The \"Schedule\" when the trigger is initiated.
        
                      - **expression** *(string) --* 
        
                        The expression that defines when to trigger an update. For more information, see `Schedule Expressions for Rules <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__ in the Amazon CloudWatch documentation.
        
                    - **dataset** *(dict) --* 
        
                      The data set whose content creation will trigger the creation of this data set\'s contents.
        
                      - **name** *(string) --* 
        
                        The name of the data set whose content generation will trigger the new data set content generation.
        
                - **actions** *(list) --* 
        
                  A list of \"DataActionSummary\" objects.
        
                  - *(dict) --* 
        
                    - **actionName** *(string) --* 
        
                      The name of the action which automatically creates the data set\'s contents.
        
                    - **actionType** *(string) --* 
        
                      The type of action by which the data set\'s contents are automatically created.
        
            - **nextToken** *(string) --* 
        
              The token to retrieve the next set of results, or ``null`` if there are no more results.
        
        """
        pass

    def list_datastores(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/ListDatastores>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_datastores(
              nextToken=\'string\',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken: 
        
          The token for the next set of results.
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of results to return in this request.
        
          The default value is 100.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'datastoreSummaries\': [
                    {
                        \'datastoreName\': \'string\',
                        \'status\': \'CREATING\'|\'ACTIVE\'|\'DELETING\',
                        \'creationTime\': datetime(2015, 1, 1),
                        \'lastUpdateTime\': datetime(2015, 1, 1)
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **datastoreSummaries** *(list) --* 
        
              A list of \"DatastoreSummary\" objects.
        
              - *(dict) --* 
        
                A summary of information about a data store.
        
                - **datastoreName** *(string) --* 
        
                  The name of the data store.
        
                - **status** *(string) --* 
        
                  The status of the data store.
        
                - **creationTime** *(datetime) --* 
        
                  When the data store was created.
        
                - **lastUpdateTime** *(datetime) --* 
        
                  The last time the data store was updated.
        
            - **nextToken** *(string) --* 
        
              The token to retrieve the next set of results, or ``null`` if there are no more results.
        
        """
        pass

    def list_pipelines(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/ListPipelines>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_pipelines(
              nextToken=\'string\',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken: 
        
          The token for the next set of results.
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of results to return in this request.
        
          The default value is 100.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pipelineSummaries\': [
                    {
                        \'pipelineName\': \'string\',
                        \'reprocessingSummaries\': [
                            {
                                \'id\': \'string\',
                                \'status\': \'RUNNING\'|\'SUCCEEDED\'|\'CANCELLED\'|\'FAILED\',
                                \'creationTime\': datetime(2015, 1, 1)
                            },
                        ],
                        \'creationTime\': datetime(2015, 1, 1),
                        \'lastUpdateTime\': datetime(2015, 1, 1)
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **pipelineSummaries** *(list) --* 
        
              A list of \"PipelineSummary\" objects.
        
              - *(dict) --* 
        
                A summary of information about a pipeline.
        
                - **pipelineName** *(string) --* 
        
                  The name of the pipeline.
        
                - **reprocessingSummaries** *(list) --* 
        
                  A summary of information about the pipeline reprocessing.
        
                  - *(dict) --* 
        
                    Information about pipeline reprocessing.
        
                    - **id** *(string) --* 
        
                      The \'reprocessingId\' returned by \"StartPipelineReprocessing\".
        
                    - **status** *(string) --* 
        
                      The status of the pipeline reprocessing.
        
                    - **creationTime** *(datetime) --* 
        
                      The time the pipeline reprocessing was created.
        
                - **creationTime** *(datetime) --* 
        
                  When the pipeline was created.
        
                - **lastUpdateTime** *(datetime) --* 
        
                  When the pipeline was last updated.
        
            - **nextToken** *(string) --* 
        
              The token to retrieve the next set of results, or ``null`` if there are no more results.
        
        """
        pass

    def list_tags_for_resource(self, resourceArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/ListTagsForResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags_for_resource(
              resourceArn=\'string\'
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]** 
        
          The ARN of the resource whose tags you want to list.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'tags\': [
                    {
                        \'key\': \'string\',
                        \'value\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **tags** *(list) --* 
        
              The tags (metadata) which you have assigned to the resource.
        
              - *(dict) --* 
        
                A set of key/value pairs which are used to manage the resource.
        
                - **key** *(string) --* 
        
                  The tag\'s key.
        
                - **value** *(string) --* 
        
                  The tag\'s value.
        
        """
        pass

    def put_logging_options(self, loggingOptions: Dict) -> NoReturn:
        """
        
        Note that if you update the value of any ``loggingOptions`` field, it takes up to one minute for the change to take effect. Also, if you change the policy attached to the role you specified in the roleArn field (for example, to correct an invalid policy) it takes up to 5 minutes for that change to take effect. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/PutLoggingOptions>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_logging_options(
              loggingOptions={
                  \'roleArn\': \'string\',
                  \'level\': \'ERROR\',
                  \'enabled\': True|False
              }
          )
        :type loggingOptions: dict
        :param loggingOptions: **[REQUIRED]** 
        
          The new values of the AWS IoT Analytics logging options.
        
          - **roleArn** *(string) --* **[REQUIRED]** 
        
            The ARN of the role that grants permission to AWS IoT Analytics to perform logging.
        
          - **level** *(string) --* **[REQUIRED]** 
        
            The logging level. Currently, only \"ERROR\" is supported.
        
          - **enabled** *(boolean) --* **[REQUIRED]** 
        
            If true, logging is enabled for AWS IoT Analytics.
        
        :returns: None
        """
        pass

    def run_pipeline_activity(self, pipelineActivity: Dict, payloads: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/RunPipelineActivity>`_
        
        **Request Syntax** 
        ::
        
          response = client.run_pipeline_activity(
              pipelineActivity={
                  \'channel\': {
                      \'name\': \'string\',
                      \'channelName\': \'string\',
                      \'next\': \'string\'
                  },
                  \'lambda\': {
                      \'name\': \'string\',
                      \'lambdaName\': \'string\',
                      \'batchSize\': 123,
                      \'next\': \'string\'
                  },
                  \'datastore\': {
                      \'name\': \'string\',
                      \'datastoreName\': \'string\'
                  },
                  \'addAttributes\': {
                      \'name\': \'string\',
                      \'attributes\': {
                          \'string\': \'string\'
                      },
                      \'next\': \'string\'
                  },
                  \'removeAttributes\': {
                      \'name\': \'string\',
                      \'attributes\': [
                          \'string\',
                      ],
                      \'next\': \'string\'
                  },
                  \'selectAttributes\': {
                      \'name\': \'string\',
                      \'attributes\': [
                          \'string\',
                      ],
                      \'next\': \'string\'
                  },
                  \'filter\': {
                      \'name\': \'string\',
                      \'filter\': \'string\',
                      \'next\': \'string\'
                  },
                  \'math\': {
                      \'name\': \'string\',
                      \'attribute\': \'string\',
                      \'math\': \'string\',
                      \'next\': \'string\'
                  },
                  \'deviceRegistryEnrich\': {
                      \'name\': \'string\',
                      \'attribute\': \'string\',
                      \'thingName\': \'string\',
                      \'roleArn\': \'string\',
                      \'next\': \'string\'
                  },
                  \'deviceShadowEnrich\': {
                      \'name\': \'string\',
                      \'attribute\': \'string\',
                      \'thingName\': \'string\',
                      \'roleArn\': \'string\',
                      \'next\': \'string\'
                  }
              },
              payloads=[
                  b\'bytes\',
              ]
          )
        :type pipelineActivity: dict
        :param pipelineActivity: **[REQUIRED]** 
        
          The pipeline activity that is run. This must not be a \'channel\' activity or a \'datastore\' activity because these activities are used in a pipeline only to load the original message and to store the (possibly) transformed message. If a \'lambda\' activity is specified, only short-running Lambda functions (those with a timeout of less than 30 seconds or less) can be used.
        
          - **channel** *(dict) --* 
        
            Determines the source of the messages to be processed.
        
            - **name** *(string) --* **[REQUIRED]** 
        
              The name of the \'channel\' activity.
        
            - **channelName** *(string) --* **[REQUIRED]** 
        
              The name of the channel from which the messages are processed.
        
            - **next** *(string) --* 
        
              The next activity in the pipeline.
        
          - **lambda** *(dict) --* 
        
            Runs a Lambda function to modify the message.
        
            - **name** *(string) --* **[REQUIRED]** 
        
              The name of the \'lambda\' activity.
        
            - **lambdaName** *(string) --* **[REQUIRED]** 
        
              The name of the Lambda function that is run on the message.
        
            - **batchSize** *(integer) --* **[REQUIRED]** 
        
              The number of messages passed to the Lambda function for processing.
        
              The AWS Lambda function must be able to process all of these messages within five minutes, which is the maximum timeout duration for Lambda functions.
        
            - **next** *(string) --* 
        
              The next activity in the pipeline.
        
          - **datastore** *(dict) --* 
        
            Specifies where to store the processed message data.
        
            - **name** *(string) --* **[REQUIRED]** 
        
              The name of the \'datastore\' activity.
        
            - **datastoreName** *(string) --* **[REQUIRED]** 
        
              The name of the data store where processed messages are stored.
        
          - **addAttributes** *(dict) --* 
        
            Adds other attributes based on existing attributes in the message.
        
            - **name** *(string) --* **[REQUIRED]** 
        
              The name of the \'addAttributes\' activity.
        
            - **attributes** *(dict) --* **[REQUIRED]** 
        
              A list of 1-50 \"AttributeNameMapping\" objects that map an existing attribute to a new attribute.
        
              .. note::
        
                The existing attributes remain in the message, so if you want to remove the originals, use \"RemoveAttributeActivity\".
        
              - *(string) --* 
        
                - *(string) --* 
        
            - **next** *(string) --* 
        
              The next activity in the pipeline.
        
          - **removeAttributes** *(dict) --* 
        
            Removes attributes from a message.
        
            - **name** *(string) --* **[REQUIRED]** 
        
              The name of the \'removeAttributes\' activity.
        
            - **attributes** *(list) --* **[REQUIRED]** 
        
              A list of 1-50 attributes to remove from the message.
        
              - *(string) --* 
        
            - **next** *(string) --* 
        
              The next activity in the pipeline.
        
          - **selectAttributes** *(dict) --* 
        
            Creates a new message using only the specified attributes from the original message. 
        
            - **name** *(string) --* **[REQUIRED]** 
        
              The name of the \'selectAttributes\' activity.
        
            - **attributes** *(list) --* **[REQUIRED]** 
        
              A list of the attributes to select from the message.
        
              - *(string) --* 
        
            - **next** *(string) --* 
        
              The next activity in the pipeline.
        
          - **filter** *(dict) --* 
        
            Filters a message based on its attributes.
        
            - **name** *(string) --* **[REQUIRED]** 
        
              The name of the \'filter\' activity.
        
            - **filter** *(string) --* **[REQUIRED]** 
        
              An expression that looks like a SQL WHERE clause that must return a Boolean value.
        
            - **next** *(string) --* 
        
              The next activity in the pipeline.
        
          - **math** *(dict) --* 
        
            Computes an arithmetic expression using the message\'s attributes and adds it to the message.
        
            - **name** *(string) --* **[REQUIRED]** 
        
              The name of the \'math\' activity.
        
            - **attribute** *(string) --* **[REQUIRED]** 
        
              The name of the attribute that will contain the result of the math operation.
        
            - **math** *(string) --* **[REQUIRED]** 
        
              An expression that uses one or more existing attributes and must return an integer value.
        
            - **next** *(string) --* 
        
              The next activity in the pipeline.
        
          - **deviceRegistryEnrich** *(dict) --* 
        
            Adds data from the AWS IoT device registry to your message.
        
            - **name** *(string) --* **[REQUIRED]** 
        
              The name of the \'deviceRegistryEnrich\' activity.
        
            - **attribute** *(string) --* **[REQUIRED]** 
        
              The name of the attribute that is added to the message.
        
            - **thingName** *(string) --* **[REQUIRED]** 
        
              The name of the IoT device whose registry information is added to the message.
        
            - **roleArn** *(string) --* **[REQUIRED]** 
        
              The ARN of the role that allows access to the device\'s registry information.
        
            - **next** *(string) --* 
        
              The next activity in the pipeline.
        
          - **deviceShadowEnrich** *(dict) --* 
        
            Adds information from the AWS IoT Device Shadows service to a message.
        
            - **name** *(string) --* **[REQUIRED]** 
        
              The name of the \'deviceShadowEnrich\' activity.
        
            - **attribute** *(string) --* **[REQUIRED]** 
        
              The name of the attribute that is added to the message.
        
            - **thingName** *(string) --* **[REQUIRED]** 
        
              The name of the IoT device whose shadow information is added to the message.
        
            - **roleArn** *(string) --* **[REQUIRED]** 
        
              The ARN of the role that allows access to the device\'s shadow.
        
            - **next** *(string) --* 
        
              The next activity in the pipeline.
        
        :type payloads: list
        :param payloads: **[REQUIRED]** 
        
          The sample message payloads on which the pipeline activity is run.
        
          - *(bytes) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'payloads\': [
                    b\'bytes\',
                ],
                \'logResult\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **payloads** *(list) --* 
        
              The enriched or transformed sample message payloads as base64-encoded strings. (The results of running the pipeline activity on each input sample message payload, encoded in base64.)
        
              - *(bytes) --* 
          
            - **logResult** *(string) --* 
        
              In case the pipeline activity fails, the log message that is generated.
        
        """
        pass

    def sample_channel_data(self, channelName: str, maxMessages: int = None, startTime: datetime = None, endTime: datetime = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/SampleChannelData>`_
        
        **Request Syntax** 
        ::
        
          response = client.sample_channel_data(
              channelName=\'string\',
              maxMessages=123,
              startTime=datetime(2015, 1, 1),
              endTime=datetime(2015, 1, 1)
          )
        :type channelName: string
        :param channelName: **[REQUIRED]** 
        
          The name of the channel whose message samples are retrieved.
        
        :type maxMessages: integer
        :param maxMessages: 
        
          The number of sample messages to be retrieved. The limit is 10, the default is also 10.
        
        :type startTime: datetime
        :param startTime: 
        
          The start of the time window from which sample messages are retrieved.
        
        :type endTime: datetime
        :param endTime: 
        
          The end of the time window from which sample messages are retrieved.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'payloads\': [
                    b\'bytes\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **payloads** *(list) --* 
        
              The list of message samples. Each sample message is returned as a base64-encoded string.
        
              - *(bytes) --* 
          
        """
        pass

    def start_pipeline_reprocessing(self, pipelineName: str, startTime: datetime = None, endTime: datetime = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/StartPipelineReprocessing>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_pipeline_reprocessing(
              pipelineName=\'string\',
              startTime=datetime(2015, 1, 1),
              endTime=datetime(2015, 1, 1)
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]** 
        
          The name of the pipeline on which to start reprocessing.
        
        :type startTime: datetime
        :param startTime: 
        
          The start time (inclusive) of raw message data that is reprocessed.
        
        :type endTime: datetime
        :param endTime: 
        
          The end time (exclusive) of raw message data that is reprocessed.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'reprocessingId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **reprocessingId** *(string) --* 
        
              The ID of the pipeline reprocessing activity that was started.
        
        """
        pass

    def tag_resource(self, resourceArn: str, tags: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/TagResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.tag_resource(
              resourceArn=\'string\',
              tags=[
                  {
                      \'key\': \'string\',
                      \'value\': \'string\'
                  },
              ]
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]** 
        
          The ARN of the resource whose tags will be modified.
        
        :type tags: list
        :param tags: **[REQUIRED]** 
        
          The new or modified tags for the resource.
        
          - *(dict) --* 
        
            A set of key/value pairs which are used to manage the resource.
        
            - **key** *(string) --* **[REQUIRED]** 
        
              The tag\'s key.
        
            - **value** *(string) --* **[REQUIRED]** 
        
              The tag\'s value.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def untag_resource(self, resourceArn: str, tagKeys: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/UntagResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.untag_resource(
              resourceArn=\'string\',
              tagKeys=[
                  \'string\',
              ]
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]** 
        
          The ARN of the resource whose tags will be removed.
        
        :type tagKeys: list
        :param tagKeys: **[REQUIRED]** 
        
          The keys of those tags which will be removed.
        
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

    def update_channel(self, channelName: str, retentionPeriod: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/UpdateChannel>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_channel(
              channelName=\'string\',
              retentionPeriod={
                  \'unlimited\': True|False,
                  \'numberOfDays\': 123
              }
          )
        :type channelName: string
        :param channelName: **[REQUIRED]** 
        
          The name of the channel to be updated.
        
        :type retentionPeriod: dict
        :param retentionPeriod: 
        
          How long, in days, message data is kept for the channel.
        
          - **unlimited** *(boolean) --* 
        
            If true, message data is kept indefinitely.
        
          - **numberOfDays** *(integer) --* 
        
            The number of days that message data is kept. The \"unlimited\" parameter must be false.
        
        :returns: None
        """
        pass

    def update_dataset(self, datasetName: str, actions: List, triggers: List = None, retentionPeriod: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/UpdateDataset>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_dataset(
              datasetName=\'string\',
              actions=[
                  {
                      \'actionName\': \'string\',
                      \'queryAction\': {
                          \'sqlQuery\': \'string\',
                          \'filters\': [
                              {
                                  \'deltaTime\': {
                                      \'offsetSeconds\': 123,
                                      \'timeExpression\': \'string\'
                                  }
                              },
                          ]
                      },
                      \'containerAction\': {
                          \'image\': \'string\',
                          \'executionRoleArn\': \'string\',
                          \'resourceConfiguration\': {
                              \'computeType\': \'ACU_1\'|\'ACU_2\',
                              \'volumeSizeInGB\': 123
                          },
                          \'variables\': [
                              {
                                  \'name\': \'string\',
                                  \'stringValue\': \'string\',
                                  \'doubleValue\': 123.0,
                                  \'datasetContentVersionValue\': {
                                      \'datasetName\': \'string\'
                                  },
                                  \'outputFileUriValue\': {
                                      \'fileName\': \'string\'
                                  }
                              },
                          ]
                      }
                  },
              ],
              triggers=[
                  {
                      \'schedule\': {
                          \'expression\': \'string\'
                      },
                      \'dataset\': {
                          \'name\': \'string\'
                      }
                  },
              ],
              retentionPeriod={
                  \'unlimited\': True|False,
                  \'numberOfDays\': 123
              }
          )
        :type datasetName: string
        :param datasetName: **[REQUIRED]** 
        
          The name of the data set to update.
        
        :type actions: list
        :param actions: **[REQUIRED]** 
        
          A list of \"DatasetAction\" objects.
        
          - *(dict) --* 
        
            A \"DatasetAction\" object specifying the query that creates the data set content.
        
            - **actionName** *(string) --* 
        
              The name of the data set action by which data set contents are automatically created.
        
            - **queryAction** *(dict) --* 
        
              An \"SqlQueryDatasetAction\" object that contains the SQL query to modify the message.
        
              - **sqlQuery** *(string) --* **[REQUIRED]** 
        
                A SQL query string.
        
              - **filters** *(list) --* 
        
                Pre-filters applied to message data.
        
                - *(dict) --* 
        
                  Information which is used to filter message data, to segregate it according to the time frame in which it arrives.
        
                  - **deltaTime** *(dict) --* 
        
                    Used to limit data to that which has arrived since the last execution of the action. When you create data set contents using message data from a specified time frame, some message data may still be \"in flight\" when processing begins, and so will not arrive in time to be processed. Use this field to make allowances for the \"in flight\" time of you message data, so that data not processed from a previous time frame will be included with the next time frame. Without this, missed message data would be excluded from processing during the next time frame as well, because its timestamp places it within the previous time frame.
        
                    - **offsetSeconds** *(integer) --* **[REQUIRED]** 
        
                      The number of seconds of estimated \"in flight\" lag time of message data.
        
                    - **timeExpression** *(string) --* **[REQUIRED]** 
        
                      An expression by which the time of the message data may be determined. This may be the name of a timestamp field, or a SQL expression which is used to derive the time the message data was generated.
        
            - **containerAction** *(dict) --* 
        
              Information which allows the system to run a containerized application in order to create the data set contents. The application must be in a Docker container along with any needed support libraries.
        
              - **image** *(string) --* **[REQUIRED]** 
        
                The ARN of the Docker container stored in your account. The Docker container contains an application and needed support libraries and is used to generate data set contents.
        
              - **executionRoleArn** *(string) --* **[REQUIRED]** 
        
                The ARN of the role which gives permission to the system to access needed resources in order to run the \"containerAction\". This includes, at minimum, permission to retrieve the data set contents which are the input to the containerized application.
        
              - **resourceConfiguration** *(dict) --* **[REQUIRED]** 
        
                Configuration of the resource which executes the \"containerAction\".
        
                - **computeType** *(string) --* **[REQUIRED]** 
        
                  The type of the compute resource used to execute the \"containerAction\". Possible values are: ACU_1 (vCPU=4, memory=16GiB) or ACU_2 (vCPU=8, memory=32GiB).
        
                - **volumeSizeInGB** *(integer) --* **[REQUIRED]** 
        
                  The size (in GB) of the persistent storage available to the resource instance used to execute the \"containerAction\" (min: 1, max: 50).
        
              - **variables** *(list) --* 
        
                The values of variables used within the context of the execution of the containerized application (basically, parameters passed to the application). Each variable must have a name and a value given by one of \"stringValue\", \"datasetContentVersionValue\", or \"outputFileUriValue\".
        
                - *(dict) --* 
        
                  An instance of a variable to be passed to the \"containerAction\" execution. Each variable must have a name and a value given by one of \"stringValue\", \"datasetContentVersionValue\", or \"outputFileUriValue\".
        
                  - **name** *(string) --* **[REQUIRED]** 
        
                    The name of the variable.
        
                  - **stringValue** *(string) --* 
        
                    The value of the variable as a string.
        
                  - **doubleValue** *(float) --* 
        
                    The value of the variable as a double (numeric).
        
                  - **datasetContentVersionValue** *(dict) --* 
        
                    The value of the variable as a structure that specifies a data set content version.
        
                    - **datasetName** *(string) --* **[REQUIRED]** 
        
                      The name of the data set whose latest contents will be used as input to the notebook or application.
        
                  - **outputFileUriValue** *(dict) --* 
        
                    The value of the variable as a structure that specifies an output file URI.
        
                    - **fileName** *(string) --* **[REQUIRED]** 
        
                      The URI of the location where data set contents are stored, usually the URI of a file in an S3 bucket.
        
        :type triggers: list
        :param triggers: 
        
          A list of \"DatasetTrigger\" objects. The list can be empty or can contain up to five **DataSetTrigger** objects.
        
          - *(dict) --* 
        
            The \"DatasetTrigger\" that specifies when the data set is automatically updated.
        
            - **schedule** *(dict) --* 
        
              The \"Schedule\" when the trigger is initiated.
        
              - **expression** *(string) --* 
        
                The expression that defines when to trigger an update. For more information, see `Schedule Expressions for Rules <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__ in the Amazon CloudWatch documentation.
        
            - **dataset** *(dict) --* 
        
              The data set whose content creation will trigger the creation of this data set\'s contents.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the data set whose content generation will trigger the new data set content generation.
        
        :type retentionPeriod: dict
        :param retentionPeriod: 
        
          How long, in days, message data is kept for the data set.
        
          - **unlimited** *(boolean) --* 
        
            If true, message data is kept indefinitely.
        
          - **numberOfDays** *(integer) --* 
        
            The number of days that message data is kept. The \"unlimited\" parameter must be false.
        
        :returns: None
        """
        pass

    def update_datastore(self, datastoreName: str, retentionPeriod: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/UpdateDatastore>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_datastore(
              datastoreName=\'string\',
              retentionPeriod={
                  \'unlimited\': True|False,
                  \'numberOfDays\': 123
              }
          )
        :type datastoreName: string
        :param datastoreName: **[REQUIRED]** 
        
          The name of the data store to be updated.
        
        :type retentionPeriod: dict
        :param retentionPeriod: 
        
          How long, in days, message data is kept for the data store.
        
          - **unlimited** *(boolean) --* 
        
            If true, message data is kept indefinitely.
        
          - **numberOfDays** *(integer) --* 
        
            The number of days that message data is kept. The \"unlimited\" parameter must be false.
        
        :returns: None
        """
        pass

    def update_pipeline(self, pipelineName: str, pipelineActivities: List) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/UpdatePipeline>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_pipeline(
              pipelineName=\'string\',
              pipelineActivities=[
                  {
                      \'channel\': {
                          \'name\': \'string\',
                          \'channelName\': \'string\',
                          \'next\': \'string\'
                      },
                      \'lambda\': {
                          \'name\': \'string\',
                          \'lambdaName\': \'string\',
                          \'batchSize\': 123,
                          \'next\': \'string\'
                      },
                      \'datastore\': {
                          \'name\': \'string\',
                          \'datastoreName\': \'string\'
                      },
                      \'addAttributes\': {
                          \'name\': \'string\',
                          \'attributes\': {
                              \'string\': \'string\'
                          },
                          \'next\': \'string\'
                      },
                      \'removeAttributes\': {
                          \'name\': \'string\',
                          \'attributes\': [
                              \'string\',
                          ],
                          \'next\': \'string\'
                      },
                      \'selectAttributes\': {
                          \'name\': \'string\',
                          \'attributes\': [
                              \'string\',
                          ],
                          \'next\': \'string\'
                      },
                      \'filter\': {
                          \'name\': \'string\',
                          \'filter\': \'string\',
                          \'next\': \'string\'
                      },
                      \'math\': {
                          \'name\': \'string\',
                          \'attribute\': \'string\',
                          \'math\': \'string\',
                          \'next\': \'string\'
                      },
                      \'deviceRegistryEnrich\': {
                          \'name\': \'string\',
                          \'attribute\': \'string\',
                          \'thingName\': \'string\',
                          \'roleArn\': \'string\',
                          \'next\': \'string\'
                      },
                      \'deviceShadowEnrich\': {
                          \'name\': \'string\',
                          \'attribute\': \'string\',
                          \'thingName\': \'string\',
                          \'roleArn\': \'string\',
                          \'next\': \'string\'
                      }
                  },
              ]
          )
        :type pipelineName: string
        :param pipelineName: **[REQUIRED]** 
        
          The name of the pipeline to update.
        
        :type pipelineActivities: list
        :param pipelineActivities: **[REQUIRED]** 
        
          A list of \"PipelineActivity\" objects.
        
          The list can be 1-25 **PipelineActivity** objects. Activities perform transformations on your messages, such as removing, renaming or adding message attributes; filtering messages based on attribute values; invoking your Lambda functions on messages for advanced processing; or performing mathematical transformations to normalize device data.
        
          - *(dict) --* 
        
            An activity that performs a transformation on a message.
        
            - **channel** *(dict) --* 
        
              Determines the source of the messages to be processed.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'channel\' activity.
        
              - **channelName** *(string) --* **[REQUIRED]** 
        
                The name of the channel from which the messages are processed.
        
              - **next** *(string) --* 
        
                The next activity in the pipeline.
        
            - **lambda** *(dict) --* 
        
              Runs a Lambda function to modify the message.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'lambda\' activity.
        
              - **lambdaName** *(string) --* **[REQUIRED]** 
        
                The name of the Lambda function that is run on the message.
        
              - **batchSize** *(integer) --* **[REQUIRED]** 
        
                The number of messages passed to the Lambda function for processing.
        
                The AWS Lambda function must be able to process all of these messages within five minutes, which is the maximum timeout duration for Lambda functions.
        
              - **next** *(string) --* 
        
                The next activity in the pipeline.
        
            - **datastore** *(dict) --* 
        
              Specifies where to store the processed message data.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'datastore\' activity.
        
              - **datastoreName** *(string) --* **[REQUIRED]** 
        
                The name of the data store where processed messages are stored.
        
            - **addAttributes** *(dict) --* 
        
              Adds other attributes based on existing attributes in the message.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'addAttributes\' activity.
        
              - **attributes** *(dict) --* **[REQUIRED]** 
        
                A list of 1-50 \"AttributeNameMapping\" objects that map an existing attribute to a new attribute.
        
                .. note::
        
                  The existing attributes remain in the message, so if you want to remove the originals, use \"RemoveAttributeActivity\".
        
                - *(string) --* 
        
                  - *(string) --* 
        
              - **next** *(string) --* 
        
                The next activity in the pipeline.
        
            - **removeAttributes** *(dict) --* 
        
              Removes attributes from a message.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'removeAttributes\' activity.
        
              - **attributes** *(list) --* **[REQUIRED]** 
        
                A list of 1-50 attributes to remove from the message.
        
                - *(string) --* 
        
              - **next** *(string) --* 
        
                The next activity in the pipeline.
        
            - **selectAttributes** *(dict) --* 
        
              Creates a new message using only the specified attributes from the original message. 
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'selectAttributes\' activity.
        
              - **attributes** *(list) --* **[REQUIRED]** 
        
                A list of the attributes to select from the message.
        
                - *(string) --* 
        
              - **next** *(string) --* 
        
                The next activity in the pipeline.
        
            - **filter** *(dict) --* 
        
              Filters a message based on its attributes.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'filter\' activity.
        
              - **filter** *(string) --* **[REQUIRED]** 
        
                An expression that looks like a SQL WHERE clause that must return a Boolean value.
        
              - **next** *(string) --* 
        
                The next activity in the pipeline.
        
            - **math** *(dict) --* 
        
              Computes an arithmetic expression using the message\'s attributes and adds it to the message.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'math\' activity.
        
              - **attribute** *(string) --* **[REQUIRED]** 
        
                The name of the attribute that will contain the result of the math operation.
        
              - **math** *(string) --* **[REQUIRED]** 
        
                An expression that uses one or more existing attributes and must return an integer value.
        
              - **next** *(string) --* 
        
                The next activity in the pipeline.
        
            - **deviceRegistryEnrich** *(dict) --* 
        
              Adds data from the AWS IoT device registry to your message.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'deviceRegistryEnrich\' activity.
        
              - **attribute** *(string) --* **[REQUIRED]** 
        
                The name of the attribute that is added to the message.
        
              - **thingName** *(string) --* **[REQUIRED]** 
        
                The name of the IoT device whose registry information is added to the message.
        
              - **roleArn** *(string) --* **[REQUIRED]** 
        
                The ARN of the role that allows access to the device\'s registry information.
        
              - **next** *(string) --* 
        
                The next activity in the pipeline.
        
            - **deviceShadowEnrich** *(dict) --* 
        
              Adds information from the AWS IoT Device Shadows service to a message.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The name of the \'deviceShadowEnrich\' activity.
        
              - **attribute** *(string) --* **[REQUIRED]** 
        
                The name of the attribute that is added to the message.
        
              - **thingName** *(string) --* **[REQUIRED]** 
        
                The name of the IoT device whose shadow information is added to the message.
        
              - **roleArn** *(string) --* **[REQUIRED]** 
        
                The ARN of the role that allows access to the device\'s shadow.
        
              - **next** *(string) --* 
        
                The next activity in the pipeline.
        
        :returns: None
        """
        pass
