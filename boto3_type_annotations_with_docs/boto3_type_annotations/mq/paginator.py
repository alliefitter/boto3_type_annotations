from typing import Dict
from botocore.paginate import Paginator


class ListBrokers(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`MQ.Client.list_brokers`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/ListBrokers>`_
        
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
                'BrokerSummaries': [
                    {
                        'BrokerArn': 'string',
                        'BrokerId': 'string',
                        'BrokerName': 'string',
                        'BrokerState': 'CREATION_IN_PROGRESS'|'CREATION_FAILED'|'DELETION_IN_PROGRESS'|'RUNNING'|'REBOOT_IN_PROGRESS',
                        'Created': datetime(2015, 1, 1),
                        'DeploymentMode': 'SINGLE_INSTANCE'|'ACTIVE_STANDBY_MULTI_AZ',
                        'HostInstanceType': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* HTTP Status Code 200: OK.
            - **BrokerSummaries** *(list) --* A list of information about all brokers.
              - *(dict) --* The Amazon Resource Name (ARN) of the broker.
                - **BrokerArn** *(string) --* The Amazon Resource Name (ARN) of the broker.
                - **BrokerId** *(string) --* The unique ID that Amazon MQ generates for the broker.
                - **BrokerName** *(string) --* The name of the broker. This value must be unique in your AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain whitespaces, brackets, wildcard characters, or special characters.
                - **BrokerState** *(string) --* The status of the broker.
                - **Created** *(datetime) --* The time when the broker was created.
                - **DeploymentMode** *(string) --* Required. The deployment mode of the broker.
                - **HostInstanceType** *(string) --* The broker's instance type.
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
