from typing import Dict
from botocore.paginate import Paginator


class ListElasticsearchInstanceTypes(Paginator):
    def paginate(self, ElasticsearchVersion: str, DomainName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/ListElasticsearchInstanceTypes>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ElasticsearchVersion=\'string\',
              DomainName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ElasticsearchVersion: string
        :param ElasticsearchVersion: **[REQUIRED]** 
        
          Version of Elasticsearch for which list of supported elasticsearch instance types are needed. 
        
        :type DomainName: string
        :param DomainName: 
        
          DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for list of available Elasticsearch instance types when modifying existing domain. 
        
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
                \'ElasticsearchInstanceTypes\': [
                    \'m3.medium.elasticsearch\'|\'m3.large.elasticsearch\'|\'m3.xlarge.elasticsearch\'|\'m3.2xlarge.elasticsearch\'|\'m4.large.elasticsearch\'|\'m4.xlarge.elasticsearch\'|\'m4.2xlarge.elasticsearch\'|\'m4.4xlarge.elasticsearch\'|\'m4.10xlarge.elasticsearch\'|\'t2.micro.elasticsearch\'|\'t2.small.elasticsearch\'|\'t2.medium.elasticsearch\'|\'r3.large.elasticsearch\'|\'r3.xlarge.elasticsearch\'|\'r3.2xlarge.elasticsearch\'|\'r3.4xlarge.elasticsearch\'|\'r3.8xlarge.elasticsearch\'|\'i2.xlarge.elasticsearch\'|\'i2.2xlarge.elasticsearch\'|\'d2.xlarge.elasticsearch\'|\'d2.2xlarge.elasticsearch\'|\'d2.4xlarge.elasticsearch\'|\'d2.8xlarge.elasticsearch\'|\'c4.large.elasticsearch\'|\'c4.xlarge.elasticsearch\'|\'c4.2xlarge.elasticsearch\'|\'c4.4xlarge.elasticsearch\'|\'c4.8xlarge.elasticsearch\'|\'r4.large.elasticsearch\'|\'r4.xlarge.elasticsearch\'|\'r4.2xlarge.elasticsearch\'|\'r4.4xlarge.elasticsearch\'|\'r4.8xlarge.elasticsearch\'|\'r4.16xlarge.elasticsearch\'|\'i3.large.elasticsearch\'|\'i3.xlarge.elasticsearch\'|\'i3.2xlarge.elasticsearch\'|\'i3.4xlarge.elasticsearch\'|\'i3.8xlarge.elasticsearch\'|\'i3.16xlarge.elasticsearch\',
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Container for the parameters returned by ``  ListElasticsearchInstanceTypes `` operation. 
        
            - **ElasticsearchInstanceTypes** *(list) --* 
        
              List of instance types supported by Amazon Elasticsearch service for given ``  ElasticsearchVersion ``  
        
              - *(string) --* 
          
        """
        pass


class ListElasticsearchVersions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/ListElasticsearchVersions>`_
        
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
                \'ElasticsearchVersions\': [
                    \'string\',
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Container for the parameters for response received from ``  ListElasticsearchVersions `` operation. 
        
            - **ElasticsearchVersions** *(list) --* 
        
              List of supported elastic search versions. 
        
              - *(string) --* 
          
        """
        pass
