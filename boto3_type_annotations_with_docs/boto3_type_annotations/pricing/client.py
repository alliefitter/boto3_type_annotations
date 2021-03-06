from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Union
from typing import List


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        """
        Check if an operation can be paginated.
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """
        pass

    def describe_services(self, ServiceCode: str = None, FormatVersion: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Returns the metadata for one service or a list of the metadata for all services. Use this without a service code to get the service codes for all services. Use it with a service code, such as ``AmazonEC2`` , to get information specific to that service, such as the attribute names available for that service. For example, some of the attribute names available for EC2 are ``volumeType`` , ``maxIopsVolume`` , ``operation`` , ``locationType`` , and ``instanceCapacity10xlarge`` .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pricing-2017-10-15/DescribeServices>`_
        
        **Request Syntax**
        ::
          response = client.describe_services(
              ServiceCode='string',
              FormatVersion='string',
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'Services': [
                    {
                        'ServiceCode': 'string',
                        'AttributeNames': [
                            'string',
                        ]
                    },
                ],
                'FormatVersion': 'string',
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              The pagination token for the next set of retreivable results.
        :type ServiceCode: string
        :param ServiceCode:
          The code for the service whose information you want to retrieve, such as ``AmazonEC2`` . You can use the ``ServiceCode`` to filter the results in a ``GetProducts`` call. To retrieve a list of all services, leave this blank.
        :type FormatVersion: string
        :param FormatVersion:
          The format version that you want the response to be in.
          Valid values are: ``aws_v1``
        :type NextToken: string
        :param NextToken:
          The pagination token that indicates the next set of results that you want to retrieve.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results that you want returned in the response.
        :rtype: dict
        :returns:
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        """
        Generate a presigned url given a client, its method, and arguments
        :type ClientMethod: string
        :param ClientMethod: The client method to presign for
        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.
        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method\'s model.
        :returns: The presigned url
        """
        pass

    def get_attribute_values(self, ServiceCode: str, AttributeName: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Returns a list of attribute values. Attibutes are similar to the details in a Price List API offer file. For a list of available attributes, see `Offer File Definitions <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/reading-an-offer.html#pps-defs>`__ in the `AWS Billing and Cost Management User Guide <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html>`__ .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pricing-2017-10-15/GetAttributeValues>`_
        
        **Request Syntax**
        ::
          response = client.get_attribute_values(
              ServiceCode='string',
              AttributeName='string',
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'AttributeValues': [
                    {
                        'Value': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AttributeValues** *(list) --* 
              The list of values for an attribute. For example, ``Throughput Optimized HDD`` and ``Provisioned IOPS`` are two available values for the ``AmazonEC2``  ``volumeType`` .
              - *(dict) --* 
                The values of a given attribute, such as ``Throughput Optimized HDD`` or ``Provisioned IOPS`` for the ``Amazon EC2``  ``volumeType`` attribute.
                - **Value** *(string) --* 
                  The specific value of an ``attributeName`` .
            - **NextToken** *(string) --* 
              The pagination token that indicates the next set of results to retrieve.
        :type ServiceCode: string
        :param ServiceCode: **[REQUIRED]**
          The service code for the service whose attributes you want to retrieve. For example, if you want the retrieve an EC2 attribute, use ``AmazonEC2`` .
        :type AttributeName: string
        :param AttributeName: **[REQUIRED]**
          The name of the attribute that you want to retrieve the values for, such as ``volumeType`` .
        :type NextToken: string
        :param NextToken:
          The pagination token that indicates the next set of results that you want to retrieve.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to return in response.
        :rtype: dict
        :returns:
        """
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        """
        Create a paginator for an operation.
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.
        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """
        pass

    def get_products(self, ServiceCode: str = None, Filters: List = None, FormatVersion: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Returns a list of all products that match the filter criteria.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pricing-2017-10-15/GetProducts>`_
        
        **Request Syntax**
        ::
          response = client.get_products(
              ServiceCode='string',
              Filters=[
                  {
                      'Type': 'TERM_MATCH',
                      'Field': 'string',
                      'Value': 'string'
                  },
              ],
              FormatVersion='string',
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'FormatVersion': 'string',
                'PriceList': [
                    'string',
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FormatVersion** *(string) --* 
              The format version of the response. For example, aws_v1.
            - **PriceList** *(list) --* 
              The list of products that match your filters. The list contains both the product metadata and the price information.
              - *(string) --* 
            - **NextToken** *(string) --* 
              The pagination token that indicates the next set of results to retrieve.
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
        :type NextToken: string
        :param NextToken:
          The pagination token that indicates the next set of results that you want to retrieve.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to return in the response.
        :rtype: dict
        :returns:
        """
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        Returns an object that can wait for some condition.
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass
