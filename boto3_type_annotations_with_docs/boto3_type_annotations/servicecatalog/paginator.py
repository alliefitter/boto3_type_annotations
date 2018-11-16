from typing import Dict
from botocore.paginate import Paginator


class ListAcceptedPortfolioShares(Paginator):
    def paginate(self, AcceptLanguage: str = None, PortfolioShareType: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListAcceptedPortfolioShares>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AcceptLanguage=\'string\',
              PortfolioShareType=\'IMPORTED\'|\'AWS_SERVICECATALOG\'|\'AWS_ORGANIZATIONS\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type AcceptLanguage: string
        :param AcceptLanguage: 
        
          The language code.
        
          * ``en`` - English (default) 
           
          * ``jp`` - Japanese 
           
          * ``zh`` - Chinese 
           
        :type PortfolioShareType: string
        :param PortfolioShareType: 
        
          The type of shared portfolios to list. The default is to list imported portfolios.
        
          * ``AWS_ORGANIZATIONS`` - List portfolios shared by the master account of your organization 
           
          * ``AWS_SERVICECATALOG`` - List default portfolios 
           
          * ``IMPORTED`` - List imported portfolios 
           
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
                \'PortfolioDetails\': [
                    {
                        \'Id\': \'string\',
                        \'ARN\': \'string\',
                        \'DisplayName\': \'string\',
                        \'Description\': \'string\',
                        \'CreatedTime\': datetime(2015, 1, 1),
                        \'ProviderName\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **PortfolioDetails** *(list) --* 
        
              Information about the portfolios.
        
              - *(dict) --* 
        
                Information about a portfolio.
        
                - **Id** *(string) --* 
        
                  The portfolio identifier.
        
                - **ARN** *(string) --* 
        
                  The ARN assigned to the portfolio.
        
                - **DisplayName** *(string) --* 
        
                  The name to use for display purposes.
        
                - **Description** *(string) --* 
        
                  The description of the portfolio.
        
                - **CreatedTime** *(datetime) --* 
        
                  The UTC time stamp of the creation time.
        
                - **ProviderName** *(string) --* 
        
                  The name of the portfolio provider.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListConstraintsForPortfolio(Paginator):
    def paginate(self, PortfolioId: str, AcceptLanguage: str = None, ProductId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListConstraintsForPortfolio>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AcceptLanguage=\'string\',
              PortfolioId=\'string\',
              ProductId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type AcceptLanguage: string
        :param AcceptLanguage: 
        
          The language code.
        
          * ``en`` - English (default) 
           
          * ``jp`` - Japanese 
           
          * ``zh`` - Chinese 
           
        :type PortfolioId: string
        :param PortfolioId: **[REQUIRED]** 
        
          The portfolio identifier.
        
        :type ProductId: string
        :param ProductId: 
        
          The product identifier.
        
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
                \'ConstraintDetails\': [
                    {
                        \'ConstraintId\': \'string\',
                        \'Type\': \'string\',
                        \'Description\': \'string\',
                        \'Owner\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ConstraintDetails** *(list) --* 
        
              Information about the constraints.
        
              - *(dict) --* 
        
                Information about a constraint.
        
                - **ConstraintId** *(string) --* 
        
                  The identifier of the constraint.
        
                - **Type** *(string) --* 
        
                  The type of constraint.
        
                  * ``LAUNCH``   
                   
                  * ``NOTIFICATION``   
                   
                  * ``TEMPLATE``   
                   
                - **Description** *(string) --* 
        
                  The description of the constraint.
        
                - **Owner** *(string) --* 
        
                  The owner of the constraint.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListLaunchPaths(Paginator):
    def paginate(self, ProductId: str, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListLaunchPaths>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AcceptLanguage=\'string\',
              ProductId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type AcceptLanguage: string
        :param AcceptLanguage: 
        
          The language code.
        
          * ``en`` - English (default) 
           
          * ``jp`` - Japanese 
           
          * ``zh`` - Chinese 
           
        :type ProductId: string
        :param ProductId: **[REQUIRED]** 
        
          The product identifier.
        
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
                \'LaunchPathSummaries\': [
                    {
                        \'Id\': \'string\',
                        \'ConstraintSummaries\': [
                            {
                                \'Type\': \'string\',
                                \'Description\': \'string\'
                            },
                        ],
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **LaunchPathSummaries** *(list) --* 
        
              Information about the launch path.
        
              - *(dict) --* 
        
                Summary information about a product path for a user.
        
                - **Id** *(string) --* 
        
                  The identifier of the product path.
        
                - **ConstraintSummaries** *(list) --* 
        
                  The constraints on the portfolio-product relationship.
        
                  - *(dict) --* 
        
                    Summary information about a constraint.
        
                    - **Type** *(string) --* 
        
                      The type of constraint.
        
                      * ``LAUNCH``   
                       
                      * ``NOTIFICATION``   
                       
                      * ``TEMPLATE``   
                       
                    - **Description** *(string) --* 
        
                      The description of the constraint.
        
                - **Tags** *(list) --* 
        
                  The tags associated with this product path.
        
                  - *(dict) --* 
        
                    Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
        
                    - **Key** *(string) --* 
        
                      The tag key.
        
                    - **Value** *(string) --* 
        
                      The value for this key.
        
                - **Name** *(string) --* 
        
                  The name of the portfolio to which the user was assigned.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListPortfolios(Paginator):
    def paginate(self, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListPortfolios>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AcceptLanguage=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type AcceptLanguage: string
        :param AcceptLanguage: 
        
          The language code.
        
          * ``en`` - English (default) 
           
          * ``jp`` - Japanese 
           
          * ``zh`` - Chinese 
           
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
                \'PortfolioDetails\': [
                    {
                        \'Id\': \'string\',
                        \'ARN\': \'string\',
                        \'DisplayName\': \'string\',
                        \'Description\': \'string\',
                        \'CreatedTime\': datetime(2015, 1, 1),
                        \'ProviderName\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **PortfolioDetails** *(list) --* 
        
              Information about the portfolios.
        
              - *(dict) --* 
        
                Information about a portfolio.
        
                - **Id** *(string) --* 
        
                  The portfolio identifier.
        
                - **ARN** *(string) --* 
        
                  The ARN assigned to the portfolio.
        
                - **DisplayName** *(string) --* 
        
                  The name to use for display purposes.
        
                - **Description** *(string) --* 
        
                  The description of the portfolio.
        
                - **CreatedTime** *(datetime) --* 
        
                  The UTC time stamp of the creation time.
        
                - **ProviderName** *(string) --* 
        
                  The name of the portfolio provider.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListPortfoliosForProduct(Paginator):
    def paginate(self, ProductId: str, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListPortfoliosForProduct>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AcceptLanguage=\'string\',
              ProductId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type AcceptLanguage: string
        :param AcceptLanguage: 
        
          The language code.
        
          * ``en`` - English (default) 
           
          * ``jp`` - Japanese 
           
          * ``zh`` - Chinese 
           
        :type ProductId: string
        :param ProductId: **[REQUIRED]** 
        
          The product identifier.
        
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
                \'PortfolioDetails\': [
                    {
                        \'Id\': \'string\',
                        \'ARN\': \'string\',
                        \'DisplayName\': \'string\',
                        \'Description\': \'string\',
                        \'CreatedTime\': datetime(2015, 1, 1),
                        \'ProviderName\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **PortfolioDetails** *(list) --* 
        
              Information about the portfolios.
        
              - *(dict) --* 
        
                Information about a portfolio.
        
                - **Id** *(string) --* 
        
                  The portfolio identifier.
        
                - **ARN** *(string) --* 
        
                  The ARN assigned to the portfolio.
        
                - **DisplayName** *(string) --* 
        
                  The name to use for display purposes.
        
                - **Description** *(string) --* 
        
                  The description of the portfolio.
        
                - **CreatedTime** *(datetime) --* 
        
                  The UTC time stamp of the creation time.
        
                - **ProviderName** *(string) --* 
        
                  The name of the portfolio provider.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListPrincipalsForPortfolio(Paginator):
    def paginate(self, PortfolioId: str, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListPrincipalsForPortfolio>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AcceptLanguage=\'string\',
              PortfolioId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type AcceptLanguage: string
        :param AcceptLanguage: 
        
          The language code.
        
          * ``en`` - English (default) 
           
          * ``jp`` - Japanese 
           
          * ``zh`` - Chinese 
           
        :type PortfolioId: string
        :param PortfolioId: **[REQUIRED]** 
        
          The portfolio identifier.
        
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
                \'Principals\': [
                    {
                        \'PrincipalARN\': \'string\',
                        \'PrincipalType\': \'IAM\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Principals** *(list) --* 
        
              The IAM principals (users or roles) associated with the portfolio.
        
              - *(dict) --* 
        
                Information about a principal.
        
                - **PrincipalARN** *(string) --* 
        
                  The ARN of the principal (IAM user, role, or group).
        
                - **PrincipalType** *(string) --* 
        
                  The principal type. The supported value is ``IAM`` .
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListResourcesForTagOption(Paginator):
    def paginate(self, TagOptionId: str, ResourceType: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListResourcesForTagOption>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              TagOptionId=\'string\',
              ResourceType=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type TagOptionId: string
        :param TagOptionId: **[REQUIRED]** 
        
          The TagOption identifier.
        
        :type ResourceType: string
        :param ResourceType: 
        
          The resource type.
        
          * ``Portfolio``   
           
          * ``Product``   
           
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
                \'ResourceDetails\': [
                    {
                        \'Id\': \'string\',
                        \'ARN\': \'string\',
                        \'Name\': \'string\',
                        \'Description\': \'string\',
                        \'CreatedTime\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ResourceDetails** *(list) --* 
        
              Information about the resources.
        
              - *(dict) --* 
        
                Information about a resource.
        
                - **Id** *(string) --* 
        
                  The identifier of the resource.
        
                - **ARN** *(string) --* 
        
                  The ARN of the resource.
        
                - **Name** *(string) --* 
        
                  The name of the resource.
        
                - **Description** *(string) --* 
        
                  The description of the resource.
        
                - **CreatedTime** *(datetime) --* 
        
                  The creation time of the resource.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListTagOptions(Paginator):
    def paginate(self, Filters: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListTagOptions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters={
                  \'Key\': \'string\',
                  \'Value\': \'string\',
                  \'Active\': True|False
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: dict
        :param Filters: 
        
          The search filters. If no search filters are specified, the output includes all TagOptions.
        
          - **Key** *(string) --* 
        
            The TagOption key.
        
          - **Value** *(string) --* 
        
            The TagOption value.
        
          - **Active** *(boolean) --* 
        
            The active state.
        
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
                \'TagOptionDetails\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\',
                        \'Active\': True|False,
                        \'Id\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TagOptionDetails** *(list) --* 
        
              Information about the TagOptions.
        
              - *(dict) --* 
        
                Information about a TagOption.
        
                - **Key** *(string) --* 
        
                  The TagOption key.
        
                - **Value** *(string) --* 
        
                  The TagOption value.
        
                - **Active** *(boolean) --* 
        
                  The TagOption active state.
        
                - **Id** *(string) --* 
        
                  The TagOption identifier.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class SearchProductsAsAdmin(Paginator):
    def paginate(self, AcceptLanguage: str = None, PortfolioId: str = None, Filters: Dict = None, SortBy: str = None, SortOrder: str = None, ProductSource: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/SearchProductsAsAdmin>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AcceptLanguage=\'string\',
              PortfolioId=\'string\',
              Filters={
                  \'string\': [
                      \'string\',
                  ]
              },
              SortBy=\'Title\'|\'VersionCount\'|\'CreationDate\',
              SortOrder=\'ASCENDING\'|\'DESCENDING\',
              ProductSource=\'ACCOUNT\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type AcceptLanguage: string
        :param AcceptLanguage: 
        
          The language code.
        
          * ``en`` - English (default) 
           
          * ``jp`` - Japanese 
           
          * ``zh`` - Chinese 
           
        :type PortfolioId: string
        :param PortfolioId: 
        
          The portfolio identifier.
        
        :type Filters: dict
        :param Filters: 
        
          The search filters. If no search filters are specified, the output includes all products to which the administrator has access.
        
          - *(string) --* 
        
            - *(list) --* 
        
              - *(string) --* 
        
        :type SortBy: string
        :param SortBy: 
        
          The sort field. If no value is specified, the results are not sorted.
        
        :type SortOrder: string
        :param SortOrder: 
        
          The sort order. If no value is specified, the results are not sorted.
        
        :type ProductSource: string
        :param ProductSource: 
        
          Access level of the source of the product.
        
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
                \'ProductViewDetails\': [
                    {
                        \'ProductViewSummary\': {
                            \'Id\': \'string\',
                            \'ProductId\': \'string\',
                            \'Name\': \'string\',
                            \'Owner\': \'string\',
                            \'ShortDescription\': \'string\',
                            \'Type\': \'CLOUD_FORMATION_TEMPLATE\'|\'MARKETPLACE\',
                            \'Distributor\': \'string\',
                            \'HasDefaultPath\': True|False,
                            \'SupportEmail\': \'string\',
                            \'SupportDescription\': \'string\',
                            \'SupportUrl\': \'string\'
                        },
                        \'Status\': \'AVAILABLE\'|\'CREATING\'|\'FAILED\',
                        \'ProductARN\': \'string\',
                        \'CreatedTime\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ProductViewDetails** *(list) --* 
        
              Information about the product views.
        
              - *(dict) --* 
        
                Information about a product view.
        
                - **ProductViewSummary** *(dict) --* 
        
                  Summary information about the product view.
        
                  - **Id** *(string) --* 
        
                    The product view identifier.
        
                  - **ProductId** *(string) --* 
        
                    The product identifier.
        
                  - **Name** *(string) --* 
        
                    The name of the product.
        
                  - **Owner** *(string) --* 
        
                    The owner of the product. Contact the product administrator for the significance of this value.
        
                  - **ShortDescription** *(string) --* 
        
                    Short description of the product.
        
                  - **Type** *(string) --* 
        
                    The product type. Contact the product administrator for the significance of this value. If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.
        
                  - **Distributor** *(string) --* 
        
                    The distributor of the product. Contact the product administrator for the significance of this value.
        
                  - **HasDefaultPath** *(boolean) --* 
        
                    Indicates whether the product has a default path. If the product does not have a default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is not required, and the output of  ProductViewSummary can be used directly with  DescribeProvisioningParameters .
        
                  - **SupportEmail** *(string) --* 
        
                    The email contact information to obtain support for this Product.
        
                  - **SupportDescription** *(string) --* 
        
                    The description of the support for this Product.
        
                  - **SupportUrl** *(string) --* 
        
                    The URL information to obtain support for this Product.
        
                - **Status** *(string) --* 
        
                  The status of the product.
        
                  * ``AVAILABLE`` - The product is ready for use. 
                   
                  * ``CREATING`` - Product creation has started; the product is not ready for use. 
                   
                  * ``FAILED`` - An action failed. 
                   
                - **ProductARN** *(string) --* 
        
                  The ARN of the product.
        
                - **CreatedTime** *(datetime) --* 
        
                  The UTC time stamp of the creation time.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
