from typing import Dict
from botocore.paginate import Paginator


class GetEntitlements(Paginator):
    def paginate(self, ProductCode: str, Filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`MarketplaceEntitlementService.Client.get_entitlements`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/entitlement.marketplace-2017-01-11/GetEntitlements>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ProductCode='string',
              Filter={
                  'string': [
                      'string',
                  ]
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Entitlements': [
                    {
                        'ProductCode': 'string',
                        'Dimension': 'string',
                        'CustomerIdentifier': 'string',
                        'Value': {
                            'IntegerValue': 123,
                            'DoubleValue': 123.0,
                            'BooleanValue': True|False,
                            'StringValue': 'string'
                        },
                        'ExpirationDate': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            The GetEntitlementsRequest contains results from the GetEntitlements operation.
            - **Entitlements** *(list) --* 
              The set of entitlements found through the GetEntitlements operation. If the result contains an empty set of entitlements, NextToken might still be present and should be used.
              - *(dict) --* 
                An entitlement represents capacity in a product owned by the customer. For example, a customer might own some number of users or seats in an SaaS application or some amount of data capacity in a multi-tenant database.
                - **ProductCode** *(string) --* 
                  The product code for which the given entitlement applies. Product codes are provided by AWS Marketplace when the product listing is created.
                - **Dimension** *(string) --* 
                  The dimension for which the given entitlement applies. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace.
                - **CustomerIdentifier** *(string) --* 
                  The customer identifier is a handle to each unique customer in an application. Customer identifiers are obtained through the ResolveCustomer operation in AWS Marketplace Metering Service.
                - **Value** *(dict) --* 
                  The EntitlementValue represents the amount of capacity that the customer is entitled to for the product.
                  - **IntegerValue** *(integer) --* 
                    The IntegerValue field will be populated with an integer value when the entitlement is an integer type. Otherwise, the field will not be set.
                  - **DoubleValue** *(float) --* 
                    The DoubleValue field will be populated with a double value when the entitlement is a double type. Otherwise, the field will not be set.
                  - **BooleanValue** *(boolean) --* 
                    The BooleanValue field will be populated with a boolean value when the entitlement is a boolean type. Otherwise, the field will not be set.
                  - **StringValue** *(string) --* 
                    The StringValue field will be populated with a string value when the entitlement is a string type. Otherwise, the field will not be set.
                - **ExpirationDate** *(datetime) --* 
                  The expiration date represents the minimum date through which this entitlement is expected to remain valid. For contractual products listed on AWS Marketplace, the expiration date is the date at which the customer will renew or cancel their contract. Customers who are opting to renew their contract will still have entitlements with an expiration date.
        :type ProductCode: string
        :param ProductCode: **[REQUIRED]**
          Product code is used to uniquely identify a product in AWS Marketplace. The product code will be provided by AWS Marketplace when the product listing is created.
        :type Filter: dict
        :param Filter:
          Filter is used to return entitlements for a specific customer or for a specific dimension. Filters are described as keys mapped to a lists of values. Filtered requests are *unioned* for each value in the value list, and then *intersected* for each filter key.
          - *(string) --*
            - *(list) --*
              - *(string) --*
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
