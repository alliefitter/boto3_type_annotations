from typing import Dict
from botocore.paginate import Paginator


class ListProtections(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/ListProtections>`_
        
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
                \'Protections\': [
                    {
                        \'Id\': \'string\',
                        \'Name\': \'string\',
                        \'ResourceArn\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Protections** *(list) --* 
        
              The array of enabled  Protection objects.
        
              - *(dict) --* 
        
                An object that represents a resource that is under DDoS protection.
        
                - **Id** *(string) --* 
        
                  The unique identifier (ID) of the protection.
        
                - **Name** *(string) --* 
        
                  The friendly name of the protection. For example, ``My CloudFront distributions`` .
        
                - **ResourceArn** *(string) --* 
        
                  The ARN (Amazon Resource Name) of the AWS resource that is protected.
        
        """
        pass
