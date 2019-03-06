from typing import Dict
from botocore.paginate import Paginator


class ListContainers(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`MediaStore.Client.list_containers`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/ListContainers>`_
        
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
                'Containers': [
                    {
                        'Endpoint': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'ARN': 'string',
                        'Name': 'string',
                        'Status': 'ACTIVE'|'CREATING'|'DELETING',
                        'AccessLoggingEnabled': True|False
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Containers** *(list) --* 
              The names of the containers.
              - *(dict) --* 
                This section describes operations that you can perform on an AWS Elemental MediaStore container.
                - **Endpoint** *(string) --* 
                  The DNS endpoint of the container. Use the endpoint to identify the specific container when sending requests to the data plane. The service assigns this value when the container is created. Once the value has been assigned, it does not change.
                - **CreationTime** *(datetime) --* 
                  Unix timestamp.
                - **ARN** *(string) --* 
                  The Amazon Resource Name (ARN) of the container. The ARN has the following format:
                  arn:aws:<region>:<account that owns this container>:container/<name of container> 
                  For example: arn:aws:mediastore:us-west-2:111122223333:container/movies 
                - **Name** *(string) --* 
                  The name of the container.
                - **Status** *(string) --* 
                  The status of container creation or deletion. The status is one of the following: ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the container, the status is ``CREATING`` . When the endpoint is available, the status changes to ``ACTIVE`` .
                - **AccessLoggingEnabled** *(boolean) --* 
                  The state of access logging on the container. This value is ``false`` by default, indicating that AWS Elemental MediaStore does not send access logs to Amazon CloudWatch Logs. When you enable access logging on the container, MediaStore changes this value to ``true`` , indicating that the service delivers access logs for objects stored in that container to CloudWatch Logs.
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
