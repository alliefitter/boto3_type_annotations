from datetime import datetime
from typing import Dict
from botocore.paginate import Paginator


class ListChannels(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoTAnalytics.Client.list_channels`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/ListChannels>`_
        
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
                'channelSummaries': [
                    {
                        'channelName': 'string',
                        'status': 'CREATING'|'ACTIVE'|'DELETING',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdateTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **channelSummaries** *(list) --* 
              A list of "ChannelSummary" objects.
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


class ListDatasetContents(Paginator):
    def paginate(self, datasetName: str, scheduledOnOrAfter: datetime = None, scheduledBefore: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoTAnalytics.Client.list_dataset_contents`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/ListDatasetContents>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              datasetName='string',
              scheduledOnOrAfter=datetime(2015, 1, 1),
              scheduledBefore=datetime(2015, 1, 1),
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'datasetContentSummaries': [
                    {
                        'version': 'string',
                        'status': {
                            'state': 'CREATING'|'SUCCEEDED'|'FAILED',
                            'reason': 'string'
                        },
                        'creationTime': datetime(2015, 1, 1),
                        'scheduleTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
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
                    The state of the data set contents. Can be one of "READY", "CREATING", "SUCCEEDED" or "FAILED".
                  - **reason** *(string) --* 
                    The reason the data set contents are in this state.
                - **creationTime** *(datetime) --* 
                  The actual time the creation of the data set contents was started.
                - **scheduleTime** *(datetime) --* 
                  The time the creation of the data set contents was scheduled to start.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type datasetName: string
        :param datasetName: **[REQUIRED]**
          The name of the data set whose contents information you want to list.
        :type scheduledOnOrAfter: datetime
        :param scheduledOnOrAfter:
          A filter to limit results to those data set contents whose creation is scheduled on or after the given time. See the field ``triggers.schedule`` in the CreateDataset request. (timestamp)
        :type scheduledBefore: datetime
        :param scheduledBefore:
          A filter to limit results to those data set contents whose creation is scheduled before the given time. See the field ``triggers.schedule`` in the CreateDataset request. (timestamp)
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


class ListDatasets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoTAnalytics.Client.list_datasets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/ListDatasets>`_
        
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
                'datasetSummaries': [
                    {
                        'datasetName': 'string',
                        'status': 'CREATING'|'ACTIVE'|'DELETING',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdateTime': datetime(2015, 1, 1),
                        'triggers': [
                            {
                                'schedule': {
                                    'expression': 'string'
                                },
                                'dataset': {
                                    'name': 'string'
                                }
                            },
                        ],
                        'actions': [
                            {
                                'actionName': 'string',
                                'actionType': 'QUERY'|'CONTAINER'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **datasetSummaries** *(list) --* 
              A list of "DatasetSummary" objects.
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
                    The "DatasetTrigger" that specifies when the data set is automatically updated.
                    - **schedule** *(dict) --* 
                      The "Schedule" when the trigger is initiated.
                      - **expression** *(string) --* 
                        The expression that defines when to trigger an update. For more information, see `Schedule Expressions for Rules <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__ in the Amazon CloudWatch Events User Guide.
                    - **dataset** *(dict) --* 
                      The data set whose content creation triggers the creation of this data set's contents.
                      - **name** *(string) --* 
                        The name of the data set whose content generation triggers the new data set content generation.
                - **actions** *(list) --* 
                  A list of "DataActionSummary" objects.
                  - *(dict) --* 
                    - **actionName** *(string) --* 
                      The name of the action which automatically creates the data set's contents.
                    - **actionType** *(string) --* 
                      The type of action by which the data set's contents are automatically created.
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


class ListDatastores(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoTAnalytics.Client.list_datastores`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/ListDatastores>`_
        
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
                'datastoreSummaries': [
                    {
                        'datastoreName': 'string',
                        'status': 'CREATING'|'ACTIVE'|'DELETING',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdateTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **datastoreSummaries** *(list) --* 
              A list of "DatastoreSummary" objects.
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


class ListPipelines(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoTAnalytics.Client.list_pipelines`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/ListPipelines>`_
        
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
                'pipelineSummaries': [
                    {
                        'pipelineName': 'string',
                        'reprocessingSummaries': [
                            {
                                'id': 'string',
                                'status': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED',
                                'creationTime': datetime(2015, 1, 1)
                            },
                        ],
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdateTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **pipelineSummaries** *(list) --* 
              A list of "PipelineSummary" objects.
              - *(dict) --* 
                A summary of information about a pipeline.
                - **pipelineName** *(string) --* 
                  The name of the pipeline.
                - **reprocessingSummaries** *(list) --* 
                  A summary of information about the pipeline reprocessing.
                  - *(dict) --* 
                    Information about pipeline reprocessing.
                    - **id** *(string) --* 
                      The 'reprocessingId' returned by "StartPipelineReprocessing".
                    - **status** *(string) --* 
                      The status of the pipeline reprocessing.
                    - **creationTime** *(datetime) --* 
                      The time the pipeline reprocessing was created.
                - **creationTime** *(datetime) --* 
                  When the pipeline was created.
                - **lastUpdateTime** *(datetime) --* 
                  When the pipeline was last updated.
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
