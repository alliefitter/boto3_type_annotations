from typing import Dict
from botocore.paginate import Paginator


class ListAgents(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DataSync.Client.list_agents`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/ListAgents>`_
        
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
                'Agents': [
                    {
                        'AgentArn': 'string',
                        'Name': 'string',
                        'Status': 'ONLINE'|'OFFLINE'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            ListAgentsResponse
            - **Agents** *(list) --* 
              A list of agents in your account.
              - *(dict) --* 
                Represents a single entry in a list of agents. ``AgentListEntry`` returns an array that contains a list of agents when the  ListAgents operation is called.
                - **AgentArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the agent.
                - **Name** *(string) --* 
                  The name of the agent.
                - **Status** *(string) --* 
                  The status of the agent.
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


class ListLocations(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DataSync.Client.list_locations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/ListLocations>`_
        
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
                'Locations': [
                    {
                        'LocationArn': 'string',
                        'LocationUri': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            ListLocationsResponse
            - **Locations** *(list) --* 
              An array that contains a list of locations.
              - *(dict) --* 
                Represents a single entry in a list of locations. ``LocationListEntry`` returns an array that contains a list of locations when the  ListLocations operation is called.
                - **LocationArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the location. For Network File System (NFS) or Amazon EFS, the location is the export path. For Amazon S3, the location is the prefix path that you want to mount and use as the root of the location.
                - **LocationUri** *(string) --* 
                  Represents a list of URLs of a location. ``LocationUri`` returns an array that contains a list of locations when the  ListLocations operation is called.
                  Format: ``TYPE://GLOBAL_ID/SUBDIR`` .
                  TYPE designates the type of location. Valid values: NFS | EFS | S3.
                  GLOBAL_ID is the globally unique identifier of the resource that backs the location. An example for EFS is ``us-east-2.fs-abcd1234`` . An example for Amazon S3 is the bucket name, such as ``myBucket`` . An example for NFS is a valid IPv4 address or a host name compliant with Domain Name Service (DNS).
                  SUBDIR is a valid file system path, delimited by forward slashes as is the *nix convention. For NFS and Amazon EFS, it's the export path to mount the location. For Amazon S3, it's the prefix path that you mount to and treat as the root of the location.
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


class ListTagsForResource(Paginator):
    def paginate(self, ResourceArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DataSync.Client.list_tags_for_resource`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/ListTagsForResource>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ResourceArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            ListTagsForResourceResponse
            - **Tags** *(list) --* 
              Array of resource tags.
              - *(dict) --* 
                Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array that contains a list of tasks when the  ListTagsForResource operation is called.
                - **Key** *(string) --* 
                  The key for an AWS resource tag.
                - **Value** *(string) --* 
                  The value for an AWS resource tag.
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the resource whose tags to list.
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


class ListTaskExecutions(Paginator):
    def paginate(self, TaskArn: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DataSync.Client.list_task_executions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/ListTaskExecutions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              TaskArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'TaskExecutions': [
                    {
                        'TaskExecutionArn': 'string',
                        'Status': 'LAUNCHING'|'PREPARING'|'TRANSFERRING'|'VERIFYING'|'SUCCESS'|'ERROR'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            ListTaskExecutionsResponse
            - **TaskExecutions** *(list) --* 
              A list of executed tasks.
              - *(dict) --* 
                Represents a single entry in a list of task executions. ``TaskExecutionListEntry`` returns an array that contains a list of specific invocations of a task when  ListTaskExecutions operation is called.
                - **TaskExecutionArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the task that was executed.
                - **Status** *(string) --* 
                  The status of a task execution.
        :type TaskArn: string
        :param TaskArn:
          The Amazon Resource Name (ARN) of the task whose tasks you want to list.
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


class ListTasks(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DataSync.Client.list_tasks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/ListTasks>`_
        
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
                'Tasks': [
                    {
                        'TaskArn': 'string',
                        'Status': 'AVAILABLE'|'CREATING'|'RUNNING'|'UNAVAILABLE',
                        'Name': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            ListTasksResponse
            - **Tasks** *(list) --* 
              A list of all the tasks that are returned.
              - *(dict) --* 
                Represents a single entry in a list of tasks. ``TaskListEntry`` returns an array that contains a list of tasks when the  ListTasks operation is called. A task includes the source and destination file systems to sync and the options to use for the tasks.
                - **TaskArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the task.
                - **Status** *(string) --* 
                  The status of the task.
                - **Name** *(string) --* 
                  The name of the task.
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
