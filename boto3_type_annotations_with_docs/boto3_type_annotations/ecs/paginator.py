from typing import Dict
from botocore.paginate import Paginator


class ListClusters(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListClusters>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'clusterArns\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **clusterArns** *(list) --* 
        
              The list of full Amazon Resource Name (ARN) entries for each cluster associated with your account.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListContainerInstances(Paginator):
    def paginate(self, cluster: str = None, filter: str = None, status: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListContainerInstances>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              cluster=\'string\',
              filter=\'string\',
              status=\'ACTIVE\'|\'DRAINING\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type cluster: string
        :param cluster: 
        
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to list. If you do not specify a cluster, the default cluster is assumed.
        
        :type filter: string
        :param filter: 
        
          You can filter the results of a ``ListContainerInstances`` operation with cluster query language statements. For more information, see `Cluster Query Language <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        
        :type status: string
        :param status: 
        
          Filters the container instances by status. For example, if you specify the ``DRAINING`` status, the results include only container instances that have been set to ``DRAINING`` using  UpdateContainerInstancesState . If you do not specify this parameter, the default is to include container instances set to ``ACTIVE`` and ``DRAINING`` .
        
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
                \'containerInstanceArns\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **containerInstanceArns** *(list) --* 
        
              The list of container instances with full ARN entries for each container instance associated with the specified cluster.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListServices(Paginator):
    def paginate(self, cluster: str = None, launchType: str = None, schedulingStrategy: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListServices>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              cluster=\'string\',
              launchType=\'EC2\'|\'FARGATE\',
              schedulingStrategy=\'REPLICA\'|\'DAEMON\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type cluster: string
        :param cluster: 
        
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the services to list. If you do not specify a cluster, the default cluster is assumed.
        
        :type launchType: string
        :param launchType: 
        
          The launch type for the services to list.
        
        :type schedulingStrategy: string
        :param schedulingStrategy: 
        
          The scheduling strategy for services to list.
        
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
                \'serviceArns\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **serviceArns** *(list) --* 
        
              The list of full ARN entries for each service associated with the specified cluster.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListTaskDefinitionFamilies(Paginator):
    def paginate(self, familyPrefix: str = None, status: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListTaskDefinitionFamilies>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              familyPrefix=\'string\',
              status=\'ACTIVE\'|\'INACTIVE\'|\'ALL\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type familyPrefix: string
        :param familyPrefix: 
        
          The ``familyPrefix`` is a string that is used to filter the results of ``ListTaskDefinitionFamilies`` . If you specify a ``familyPrefix`` , only task definition family names that begin with the ``familyPrefix`` string are returned.
        
        :type status: string
        :param status: 
        
          The task definition family status with which to filter the ``ListTaskDefinitionFamilies`` results. By default, both ``ACTIVE`` and ``INACTIVE`` task definition families are listed. If this parameter is set to ``ACTIVE`` , only task definition families that have an ``ACTIVE`` task definition revision are returned. If this parameter is set to ``INACTIVE`` , only task definition families that do not have any ``ACTIVE`` task definition revisions are returned. If you paginate the resulting output, be sure to keep the ``status`` value constant in each subsequent request.
        
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
                \'families\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **families** *(list) --* 
        
              The list of task definition family names that match the ``ListTaskDefinitionFamilies`` request.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListTaskDefinitions(Paginator):
    def paginate(self, familyPrefix: str = None, status: str = None, sort: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListTaskDefinitions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              familyPrefix=\'string\',
              status=\'ACTIVE\'|\'INACTIVE\',
              sort=\'ASC\'|\'DESC\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type familyPrefix: string
        :param familyPrefix: 
        
          The full family name with which to filter the ``ListTaskDefinitions`` results. Specifying a ``familyPrefix`` limits the listed task definitions to task definition revisions that belong to that family.
        
        :type status: string
        :param status: 
        
          The task definition status with which to filter the ``ListTaskDefinitions`` results. By default, only ``ACTIVE`` task definitions are listed. By setting this parameter to ``INACTIVE`` , you can view task definitions that are ``INACTIVE`` as long as an active task or service still references them. If you paginate the resulting output, be sure to keep the ``status`` value constant in each subsequent request.
        
        :type sort: string
        :param sort: 
        
          The order in which to sort the results. Valid values are ``ASC`` and ``DESC`` . By default (``ASC`` ), task definitions are listed lexicographically by family name and in ascending numerical order by revision so that the newest task definitions in a family are listed last. Setting this parameter to ``DESC`` reverses the sort order on family name and revision so that the newest task definitions in a family are listed first.
        
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
                \'taskDefinitionArns\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **taskDefinitionArns** *(list) --* 
        
              The list of task definition Amazon Resource Name (ARN) entries for the ``ListTaskDefinitions`` request.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListTasks(Paginator):
    def paginate(self, cluster: str = None, containerInstance: str = None, family: str = None, startedBy: str = None, serviceName: str = None, desiredStatus: str = None, launchType: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListTasks>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              cluster=\'string\',
              containerInstance=\'string\',
              family=\'string\',
              startedBy=\'string\',
              serviceName=\'string\',
              desiredStatus=\'RUNNING\'|\'PENDING\'|\'STOPPED\',
              launchType=\'EC2\'|\'FARGATE\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type cluster: string
        :param cluster: 
        
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the tasks to list. If you do not specify a cluster, the default cluster is assumed.
        
        :type containerInstance: string
        :param containerInstance: 
        
          The container instance ID or full ARN of the container instance with which to filter the ``ListTasks`` results. Specifying a ``containerInstance`` limits the results to tasks that belong to that container instance.
        
        :type family: string
        :param family: 
        
          The name of the family with which to filter the ``ListTasks`` results. Specifying a ``family`` limits the results to tasks that belong to that family.
        
        :type startedBy: string
        :param startedBy: 
        
          The ``startedBy`` value with which to filter the task results. Specifying a ``startedBy`` value limits the results to tasks that were started with that value.
        
        :type serviceName: string
        :param serviceName: 
        
          The name of the service with which to filter the ``ListTasks`` results. Specifying a ``serviceName`` limits the results to tasks that belong to that service.
        
        :type desiredStatus: string
        :param desiredStatus: 
        
          The task desired status with which to filter the ``ListTasks`` results. Specifying a ``desiredStatus`` of ``STOPPED`` limits the results to tasks that Amazon ECS has set the desired status to ``STOPPED`` , which can be useful for debugging tasks that are not starting properly or have died or finished. The default status filter is ``RUNNING`` , which shows tasks that Amazon ECS has set the desired status to ``RUNNING`` .
        
          .. note::
        
            Although you can filter results based on a desired status of ``PENDING`` , this does not return any results because Amazon ECS never sets the desired status of a task to that value (only a task\'s ``lastStatus`` may have a value of ``PENDING`` ).
        
        :type launchType: string
        :param launchType: 
        
          The launch type for services to list.
        
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
                \'taskArns\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **taskArns** *(list) --* 
        
              The list of task ARN entries for the ``ListTasks`` request.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
