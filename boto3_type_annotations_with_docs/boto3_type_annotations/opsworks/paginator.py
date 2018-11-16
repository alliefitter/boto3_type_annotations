from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeEcsClusters(Paginator):
    def paginate(self, EcsClusterArns: List = None, StackId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeEcsClusters>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              EcsClusterArns=[
                  \'string\',
              ],
              StackId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type EcsClusterArns: list
        :param EcsClusterArns: 
        
          A list of ARNs, one for each cluster to be described.
        
          - *(string) --* 
        
        :type StackId: string
        :param StackId: 
        
          A stack ID. ``DescribeEcsClusters`` returns a description of the cluster that is registered with the stack.
        
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
                \'EcsClusters\': [
                    {
                        \'EcsClusterArn\': \'string\',
                        \'EcsClusterName\': \'string\',
                        \'StackId\': \'string\',
                        \'RegisteredAt\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the response to a ``DescribeEcsClusters`` request.
        
            - **EcsClusters** *(list) --* 
        
              A list of ``EcsCluster`` objects containing the cluster descriptions.
        
              - *(dict) --* 
        
                Describes a registered Amazon ECS cluster.
        
                - **EcsClusterArn** *(string) --* 
        
                  The cluster\'s ARN.
        
                - **EcsClusterName** *(string) --* 
        
                  The cluster name.
        
                - **StackId** *(string) --* 
        
                  The stack ID.
        
                - **RegisteredAt** *(string) --* 
        
                  The time and date that the cluster was registered with the stack.
        
        """
        pass
