from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeServices(Paginator):
    def paginate(self, ServiceCode: str = None, FormatVersion: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pricing-2017-10-15/DescribeServices>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ServiceCode=\'string\',
              FormatVersion=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ServiceCode: string
        :param ServiceCode: 
        
          The code for the service whose information you want to retrieve, such as ``AmazonEC2`` . You can use the ``ServiceCode`` to filter the results in a ``GetProducts`` call. To retrieve a list of all services, leave this blank.
        
        :type FormatVersion: string
        :param FormatVersion: 
        
          The format version that you want the response to be in.
        
          Valid values are: ``aws_v1``  
        
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
                \'Services\': [
                    {
                        \'ServiceCode\': \'string\',
                        \'AttributeNames\': [
                            \'string\',
                        ]
                    },
                ],
                \'FormatVersion\': \'string\',
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Services** *(list) --* 
        
              The service metadata for the service or services in the response.
        
              - *(dict) --* 
        
                The metadata for a service, such as the service code and available attribute names.
        
                - **ServiceCode** *(string) --* 
        
                  The code for the AWS service.
        
                - **AttributeNames** *(list) --* 
        
                  The attributes that are available for this service.
        
                  - *(string) --* 
              
            - **FormatVersion** *(string) --* 
        
              The format version of the response. For example, ``aws_v1`` .
        
        """
        pass


class GetAttributeValues(Paginator):
    def paginate(self, ServiceCode: str, AttributeName: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pricing-2017-10-15/GetAttributeValues>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ServiceCode=\'string\',
              AttributeName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ServiceCode: string
        :param ServiceCode: **[REQUIRED]** 
        
          The service code for the service whose attributes you want to retrieve. For example, if you want the retrieve an EC2 attribute, use ``AmazonEC2`` .
        
        :type AttributeName: string
        :param AttributeName: **[REQUIRED]** 
        
          The name of the attribute that you want to retrieve the values for, such as ``volumeType`` .
        
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
                \'AttributeValues\': [
                    {
                        \'Value\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AttributeValues** *(list) --* 
        
              The list of values for an attribute. For example, ``Throughput Optimized HDD`` and ``Provisioned IOPS`` are two available values for the ``AmazonEC2``  ``volumeType`` .
        
              - *(dict) --* 
        
                The values of a given attribute, such as ``Throughput Optimized HDD`` or ``Provisioned IOPS`` for the ``Amazon EC2``  ``volumeType`` attribute.
        
                - **Value** *(string) --* 
        
                  The specific value of an ``attributeName`` .
        
        """
        pass


class GetProducts(Paginator):
    def paginate(self, ServiceCode: str = None, Filters: List = None, FormatVersion: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pricing-2017-10-15/GetProducts>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ServiceCode=\'string\',
              Filters=[
                  {
                      \'Type\': \'TERM_MATCH\',
                      \'Field\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              FormatVersion=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ServiceCode: string
        :param ServiceCode: 
        
          The code for the service whose products you want to retrieve. 
        
        :type Filters: list
        :param Filters: 
        
          The list of filters that limit the returned products. only products that match all filters are returned.
        
          - *(dict) --* 
        
            The constraints that you want all returned products to match.
        
            - **Type** *(string) --* **[REQUIRED]** 
        
              The type of filter that you want to use.
        
              Valid values are: ``TERM_MATCH`` . ``TERM_MATCH`` returns only products that match both the given filter field and the given value.
        
            - **Field** *(string) --* **[REQUIRED]** 
        
              The product metadata field that you want to filter on. You can filter by just the service code to see all products for a specific service, filter by just the attribute name to see a specific attribute for multiple services, or use both a service code and an attribute name to retrieve only products that match both fields.
        
              Valid values include: ``ServiceCode`` , and all attribute names
        
              For example, you can filter by the ``AmazonEC2`` service code and the ``volumeType`` attribute name to get the prices for only Amazon EC2 volumes.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The service code or attribute value that you want to filter by. If you are filtering by service code this is the actual service code, such as ``AmazonEC2`` . If you are filtering by attribute name, this is the attribute value that you want the returned products to match, such as a ``Provisioned IOPS`` volume.
        
        :type FormatVersion: string
        :param FormatVersion: 
        
          The format version that you want the response to be in.
        
          Valid values are: ``aws_v1``  
        
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
                \'FormatVersion\': \'string\',
                \'PriceList\': [
                    \'string\',
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **FormatVersion** *(string) --* 
        
              The format version of the response. For example, aws_v1.
        
            - **PriceList** *(list) --* 
        
              The list of products that match your filters. The list contains both the product metadata and the price information.
        
              - *(string) --* 
          
        """
        pass
