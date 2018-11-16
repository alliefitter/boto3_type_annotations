from typing import Dict
from botocore.paginate import Paginator


class ListDomains(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sdb-2009-04-15/ListDomains>`_
        
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
                \'DomainNames\': [
                    \'string\',
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DomainNames** *(list) --* A list of domain names that match the expression.
              
              - *(string) --* 
          
        """
        pass


class Select(Paginator):
    def paginate(self, SelectExpression: str, ConsistentRead: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sdb-2009-04-15/Select>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              SelectExpression=\'string\',
              ConsistentRead=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type SelectExpression: string
        :param SelectExpression: **[REQUIRED]** The expression used to query the domain.
        
        :type ConsistentRead: boolean
        :param ConsistentRead: Determines whether or not strong consistency should be enforced when data is read from SimpleDB. If ``true`` , any data previously written to SimpleDB will be returned. Otherwise, results will be consistent eventually, and the client may not see data that was written immediately before your read.
        
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
                \'Items\': [
                    {
                        \'Name\': \'string\',
                        \'AlternateNameEncoding\': \'string\',
                        \'Attributes\': [
                            {
                                \'Name\': \'string\',
                                \'AlternateNameEncoding\': \'string\',
                                \'Value\': \'string\',
                                \'AlternateValueEncoding\': \'string\'
                            },
                        ]
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Items** *(list) --* A list of items that match the select expression.
              
              - *(dict) --* 
        
                - **Name** *(string) --* The name of the item.
                
                - **AlternateNameEncoding** *(string) --* 
        
                - **Attributes** *(list) --* A list of attributes.
                  
                  - *(dict) --* 
        
                    - **Name** *(string) --* The name of the attribute.
                    
                    - **AlternateNameEncoding** *(string) --* 
        
                    - **Value** *(string) --* The value of the attribute.
                    
                    - **AlternateValueEncoding** *(string) --* 
        
        """
        pass
