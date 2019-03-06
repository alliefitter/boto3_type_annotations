from typing import Dict
from botocore.paginate import Paginator


class ListCreatedArtifacts(Paginator):
    def paginate(self, ProgressUpdateStream: str, MigrationTaskName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`MigrationHub.Client.list_created_artifacts`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/ListCreatedArtifacts>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ProgressUpdateStream='string',
              MigrationTaskName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'CreatedArtifactList': [
                    {
                        'Name': 'string',
                        'Description': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CreatedArtifactList** *(list) --* 
              List of created artifacts up to the maximum number of results specified in the request.
              - *(dict) --* 
                An ARN of the AWS cloud resource target receiving the migration (e.g., AMI, EC2 instance, RDS instance, etc.).
                - **Name** *(string) --* 
                  An ARN that uniquely identifies the result of a migration task.
                - **Description** *(string) --* 
                  A description that can be free-form text to record additional detail about the artifact for clarity or for later reference.
        :type ProgressUpdateStream: string
        :param ProgressUpdateStream: **[REQUIRED]**
          The name of the ProgressUpdateStream.
        :type MigrationTaskName: string
        :param MigrationTaskName: **[REQUIRED]**
          Unique identifier that references the migration task.
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


class ListDiscoveredResources(Paginator):
    def paginate(self, ProgressUpdateStream: str, MigrationTaskName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`MigrationHub.Client.list_discovered_resources`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/ListDiscoveredResources>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ProgressUpdateStream='string',
              MigrationTaskName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'DiscoveredResourceList': [
                    {
                        'ConfigurationId': 'string',
                        'Description': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DiscoveredResourceList** *(list) --* 
              Returned list of discovered resources associated with the given MigrationTask.
              - *(dict) --* 
                Object representing the on-premises resource being migrated.
                - **ConfigurationId** *(string) --* 
                  The configurationId in ADS that uniquely identifies the on-premise resource.
                - **Description** *(string) --* 
                  A description that can be free-form text to record additional detail about the discovered resource for clarity or later reference.
        :type ProgressUpdateStream: string
        :param ProgressUpdateStream: **[REQUIRED]**
          The name of the ProgressUpdateStream.
        :type MigrationTaskName: string
        :param MigrationTaskName: **[REQUIRED]**
          The name of the MigrationTask.
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


class ListMigrationTasks(Paginator):
    def paginate(self, ResourceName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`MigrationHub.Client.list_migration_tasks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/ListMigrationTasks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ResourceName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'MigrationTaskSummaryList': [
                    {
                        'ProgressUpdateStream': 'string',
                        'MigrationTaskName': 'string',
                        'Status': 'NOT_STARTED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
                        'ProgressPercent': 123,
                        'StatusDetail': 'string',
                        'UpdateDateTime': datetime(2015, 1, 1)
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **MigrationTaskSummaryList** *(list) --* 
              Lists the migration task's summary which includes: ``MigrationTaskName`` , ``ProgressPercent`` , ``ProgressUpdateStream`` , ``Status`` , and the ``UpdateDateTime`` for each task.
              - *(dict) --* 
                MigrationTaskSummary includes ``MigrationTaskName`` , ``ProgressPercent`` , ``ProgressUpdateStream`` , ``Status`` , and ``UpdateDateTime`` for each task.
                - **ProgressUpdateStream** *(string) --* 
                  An AWS resource used for access control. It should uniquely identify the migration tool as it is used for all updates made by the tool.
                - **MigrationTaskName** *(string) --* 
                  Unique identifier that references the migration task.
                - **Status** *(string) --* 
                  Status of the task.
                - **ProgressPercent** *(integer) --* 
                - **StatusDetail** *(string) --* 
                  Detail information of what is being done within the overall status state.
                - **UpdateDateTime** *(datetime) --* 
                  The timestamp when the task was gathered.
        :type ResourceName: string
        :param ResourceName:
          Filter migration tasks by discovered resource name.
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


class ListProgressUpdateStreams(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`MigrationHub.Client.list_progress_update_streams`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams>`_
        
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
                'ProgressUpdateStreamSummaryList': [
                    {
                        'ProgressUpdateStreamName': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProgressUpdateStreamSummaryList** *(list) --* 
              List of progress update streams up to the max number of results passed in the input.
              - *(dict) --* 
                Summary of the AWS resource used for access control that is implicitly linked to your AWS account.
                - **ProgressUpdateStreamName** *(string) --* 
                  The name of the ProgressUpdateStream. 
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
