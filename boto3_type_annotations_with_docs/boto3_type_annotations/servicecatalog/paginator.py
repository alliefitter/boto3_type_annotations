from typing import Dict
from botocore.paginate import Paginator


class ListAcceptedPortfolioShares(Paginator):
    def paginate(self, AcceptLanguage: str = None, PortfolioShareType: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceCatalog.Client.list_accepted_portfolio_shares`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListAcceptedPortfolioShares>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AcceptLanguage='string',
              PortfolioShareType='IMPORTED'|'AWS_SERVICECATALOG'|'AWS_ORGANIZATIONS',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'PortfolioDetails': [
                    {
                        'Id': 'string',
                        'ARN': 'string',
                        'DisplayName': 'string',
                        'Description': 'string',
                        'CreatedTime': datetime(2015, 1, 1),
                        'ProviderName': 'string'
                    },
                ],
                'NextToken': 'string'
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
        """
        pass


class ListConstraintsForPortfolio(Paginator):
    def paginate(self, PortfolioId: str, AcceptLanguage: str = None, ProductId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceCatalog.Client.list_constraints_for_portfolio`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListConstraintsForPortfolio>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AcceptLanguage='string',
              PortfolioId='string',
              ProductId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ConstraintDetails': [
                    {
                        'ConstraintId': 'string',
                        'Type': 'string',
                        'Description': 'string',
                        'Owner': 'string'
                    },
                ],
                'NextToken': 'string'
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
                  * STACKSET 
                  * ``TEMPLATE``   
                - **Description** *(string) --* 
                  The description of the constraint.
                - **Owner** *(string) --* 
                  The owner of the constraint.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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
        """
        pass


class ListLaunchPaths(Paginator):
    def paginate(self, ProductId: str, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceCatalog.Client.list_launch_paths`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListLaunchPaths>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AcceptLanguage='string',
              ProductId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'LaunchPathSummaries': [
                    {
                        'Id': 'string',
                        'ConstraintSummaries': [
                            {
                                'Type': 'string',
                                'Description': 'string'
                            },
                        ],
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
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
                      * STACKSET 
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
        """
        pass


class ListOrganizationPortfolioAccess(Paginator):
    def paginate(self, PortfolioId: str, OrganizationNodeType: str, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceCatalog.Client.list_organization_portfolio_access`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AcceptLanguage='string',
              PortfolioId='string',
              OrganizationNodeType='ORGANIZATION'|'ORGANIZATIONAL_UNIT'|'ACCOUNT',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'OrganizationNodes': [
                    {
                        'Type': 'ORGANIZATION'|'ORGANIZATIONAL_UNIT'|'ACCOUNT',
                        'Value': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **OrganizationNodes** *(list) --* 
              Displays information about the organization nodes.
              - *(dict) --* 
                Information about the organization node.
                - **Type** *(string) --* 
                  The organization node type.
                - **Value** *(string) --* 
                  The identifier of the organization node.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type PortfolioId: string
        :param PortfolioId: **[REQUIRED]**
          The portfolio identifier. For example, ``port-2abcdext3y5fk`` .
        :type OrganizationNodeType: string
        :param OrganizationNodeType: **[REQUIRED]**
          The organization node type that will be returned in the output.
          * ``ORGANIZATION`` - Organization that has access to the portfolio.
          * ``ORGANIZATIONAL_UNIT`` - Organizational unit that has access to the portfolio within your organization.
          * ``ACCOUNT`` - Account that has access to the portfolio within your organization.
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


class ListPortfolios(Paginator):
    def paginate(self, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceCatalog.Client.list_portfolios`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListPortfolios>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AcceptLanguage='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'PortfolioDetails': [
                    {
                        'Id': 'string',
                        'ARN': 'string',
                        'DisplayName': 'string',
                        'Description': 'string',
                        'CreatedTime': datetime(2015, 1, 1),
                        'ProviderName': 'string'
                    },
                ],
                'NextToken': 'string'
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
        """
        pass


class ListPortfoliosForProduct(Paginator):
    def paginate(self, ProductId: str, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceCatalog.Client.list_portfolios_for_product`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListPortfoliosForProduct>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AcceptLanguage='string',
              ProductId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'PortfolioDetails': [
                    {
                        'Id': 'string',
                        'ARN': 'string',
                        'DisplayName': 'string',
                        'Description': 'string',
                        'CreatedTime': datetime(2015, 1, 1),
                        'ProviderName': 'string'
                    },
                ],
                'NextToken': 'string'
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
        """
        pass


class ListPrincipalsForPortfolio(Paginator):
    def paginate(self, PortfolioId: str, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceCatalog.Client.list_principals_for_portfolio`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListPrincipalsForPortfolio>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AcceptLanguage='string',
              PortfolioId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Principals': [
                    {
                        'PrincipalARN': 'string',
                        'PrincipalType': 'IAM'
                    },
                ],
                'NextToken': 'string'
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
        """
        pass


class ListProvisionedProductPlans(Paginator):
    def paginate(self, AcceptLanguage: str = None, ProvisionProductId: str = None, AccessLevelFilter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceCatalog.Client.list_provisioned_product_plans`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListProvisionedProductPlans>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AcceptLanguage='string',
              ProvisionProductId='string',
              AccessLevelFilter={
                  'Key': 'Account'|'Role'|'User',
                  'Value': 'string'
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
                'ProvisionedProductPlans': [
                    {
                        'PlanName': 'string',
                        'PlanId': 'string',
                        'ProvisionProductId': 'string',
                        'ProvisionProductName': 'string',
                        'PlanType': 'CLOUDFORMATION',
                        'ProvisioningArtifactId': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProvisionedProductPlans** *(list) --* 
              Information about the plans.
              - *(dict) --* 
                Summary information about a plan.
                - **PlanName** *(string) --* 
                  The name of the plan.
                - **PlanId** *(string) --* 
                  The plan identifier.
                - **ProvisionProductId** *(string) --* 
                  The product identifier.
                - **ProvisionProductName** *(string) --* 
                  The user-friendly name of the provisioned product.
                - **PlanType** *(string) --* 
                  The plan type.
                - **ProvisioningArtifactId** *(string) --* 
                  The identifier of the provisioning artifact.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type ProvisionProductId: string
        :param ProvisionProductId:
          The product identifier.
        :type AccessLevelFilter: dict
        :param AccessLevelFilter:
          The access level to use to obtain results. The default is ``User`` .
          - **Key** *(string) --*
            The access level.
            * ``Account`` - Filter results based on the account.
            * ``Role`` - Filter results based on the federated role of the specified user.
            * ``User`` - Filter results based on the specified user.
          - **Value** *(string) --*
            The user to which the access level applies. The only supported value is ``Self`` .
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


class ListProvisioningArtifactsForServiceAction(Paginator):
    def paginate(self, ServiceActionId: str, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceCatalog.Client.list_provisioning_artifacts_for_service_action`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ServiceActionId='string',
              AcceptLanguage='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ProvisioningArtifactViews': [
                    {
                        'ProductViewSummary': {
                            'Id': 'string',
                            'ProductId': 'string',
                            'Name': 'string',
                            'Owner': 'string',
                            'ShortDescription': 'string',
                            'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
                            'Distributor': 'string',
                            'HasDefaultPath': True|False,
                            'SupportEmail': 'string',
                            'SupportDescription': 'string',
                            'SupportUrl': 'string'
                        },
                        'ProvisioningArtifact': {
                            'Id': 'string',
                            'Name': 'string',
                            'Description': 'string',
                            'CreatedTime': datetime(2015, 1, 1)
                        }
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProvisioningArtifactViews** *(list) --* 
              An array of objects with information about product views and provisioning artifacts.
              - *(dict) --* 
                An object that contains summary information about a product view and a provisioning artifact.
                - **ProductViewSummary** *(dict) --* 
                  Summary information about a product view.
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
                - **ProvisioningArtifact** *(dict) --* 
                  Information about a provisioning artifact. A provisioning artifact is also known as a product version.
                  - **Id** *(string) --* 
                    The identifier of the provisioning artifact.
                  - **Name** *(string) --* 
                    The name of the provisioning artifact.
                  - **Description** *(string) --* 
                    The description of the provisioning artifact.
                  - **CreatedTime** *(datetime) --* 
                    The UTC time stamp of the creation time.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ServiceActionId: string
        :param ServiceActionId: **[REQUIRED]**
          The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .
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
        """
        pass


class ListRecordHistory(Paginator):
    def paginate(self, AcceptLanguage: str = None, AccessLevelFilter: Dict = None, SearchFilter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceCatalog.Client.list_record_history`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListRecordHistory>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AcceptLanguage='string',
              AccessLevelFilter={
                  'Key': 'Account'|'Role'|'User',
                  'Value': 'string'
              },
              SearchFilter={
                  'Key': 'string',
                  'Value': 'string'
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
                'RecordDetails': [
                    {
                        'RecordId': 'string',
                        'ProvisionedProductName': 'string',
                        'Status': 'CREATED'|'IN_PROGRESS'|'IN_PROGRESS_IN_ERROR'|'SUCCEEDED'|'FAILED',
                        'CreatedTime': datetime(2015, 1, 1),
                        'UpdatedTime': datetime(2015, 1, 1),
                        'ProvisionedProductType': 'string',
                        'RecordType': 'string',
                        'ProvisionedProductId': 'string',
                        'ProductId': 'string',
                        'ProvisioningArtifactId': 'string',
                        'PathId': 'string',
                        'RecordErrors': [
                            {
                                'Code': 'string',
                                'Description': 'string'
                            },
                        ],
                        'RecordTags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RecordDetails** *(list) --* 
              The records, in reverse chronological order.
              - *(dict) --* 
                Information about a request operation.
                - **RecordId** *(string) --* 
                  The identifier of the record.
                - **ProvisionedProductName** *(string) --* 
                  The user-friendly name of the provisioned product.
                - **Status** *(string) --* 
                  The status of the provisioned product.
                  * ``CREATED`` - The request was created but the operation has not started. 
                  * ``IN_PROGRESS`` - The requested operation is in progress. 
                  * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback. 
                  * ``SUCCEEDED`` - The requested operation has successfully completed. 
                  * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using the error messages returned. 
                - **CreatedTime** *(datetime) --* 
                  The UTC time stamp of the creation time.
                - **UpdatedTime** *(datetime) --* 
                  The time when the record was last updated.
                - **ProvisionedProductType** *(string) --* 
                  The type of provisioned product. The supported values are ``CFN_STACK`` and ``CFN_STACKSET`` .
                - **RecordType** *(string) --* 
                  The record type.
                  * ``PROVISION_PRODUCT``   
                  * ``UPDATE_PROVISIONED_PRODUCT``   
                  * ``TERMINATE_PROVISIONED_PRODUCT``   
                - **ProvisionedProductId** *(string) --* 
                  The identifier of the provisioned product.
                - **ProductId** *(string) --* 
                  The product identifier.
                - **ProvisioningArtifactId** *(string) --* 
                  The identifier of the provisioning artifact.
                - **PathId** *(string) --* 
                  The path identifier.
                - **RecordErrors** *(list) --* 
                  The errors that occurred.
                  - *(dict) --* 
                    The error code and description resulting from an operation.
                    - **Code** *(string) --* 
                      The numeric value of the error.
                    - **Description** *(string) --* 
                      The description of the error.
                - **RecordTags** *(list) --* 
                  One or more tags.
                  - *(dict) --* 
                    Information about a tag, which is a key-value pair.
                    - **Key** *(string) --* 
                      The key for this tag.
                    - **Value** *(string) --* 
                      The value for this tag.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type AccessLevelFilter: dict
        :param AccessLevelFilter:
          The access level to use to obtain results. The default is ``User`` .
          - **Key** *(string) --*
            The access level.
            * ``Account`` - Filter results based on the account.
            * ``Role`` - Filter results based on the federated role of the specified user.
            * ``User`` - Filter results based on the specified user.
          - **Value** *(string) --*
            The user to which the access level applies. The only supported value is ``Self`` .
        :type SearchFilter: dict
        :param SearchFilter:
          The search filter to scope the results.
          - **Key** *(string) --*
            The filter key.
            * ``product`` - Filter results based on the specified product identifier.
            * ``provisionedproduct`` - Filter results based on the provisioned product identifier.
          - **Value** *(string) --*
            The filter value.
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


class ListResourcesForTagOption(Paginator):
    def paginate(self, TagOptionId: str, ResourceType: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceCatalog.Client.list_resources_for_tag_option`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListResourcesForTagOption>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              TagOptionId='string',
              ResourceType='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ResourceDetails': [
                    {
                        'Id': 'string',
                        'ARN': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'CreatedTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
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
        """
        pass


class ListServiceActions(Paginator):
    def paginate(self, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceCatalog.Client.list_service_actions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListServiceActions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AcceptLanguage='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ServiceActionSummaries': [
                    {
                        'Id': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'DefinitionType': 'SSM_AUTOMATION'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ServiceActionSummaries** *(list) --* 
              An object containing information about the service actions associated with the provisioning artifact.
              - *(dict) --* 
                Detailed information about the self-service action.
                - **Id** *(string) --* 
                  The self-service action identifier.
                - **Name** *(string) --* 
                  The self-service action name.
                - **Description** *(string) --* 
                  The self-service action description.
                - **DefinitionType** *(string) --* 
                  The self-service action definition type. For example, ``SSM_AUTOMATION`` .
            - **NextToken** *(string) --* 
              A token to resume pagination.
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
        """
        pass


class ListServiceActionsForProvisioningArtifact(Paginator):
    def paginate(self, ProductId: str, ProvisioningArtifactId: str, AcceptLanguage: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceCatalog.Client.list_service_actions_for_provisioning_artifact`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListServiceActionsForProvisioningArtifact>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ProductId='string',
              ProvisioningArtifactId='string',
              AcceptLanguage='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ServiceActionSummaries': [
                    {
                        'Id': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'DefinitionType': 'SSM_AUTOMATION'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ServiceActionSummaries** *(list) --* 
              An object containing information about the self-service actions associated with the provisioning artifact.
              - *(dict) --* 
                Detailed information about the self-service action.
                - **Id** *(string) --* 
                  The self-service action identifier.
                - **Name** *(string) --* 
                  The self-service action name.
                - **Description** *(string) --* 
                  The self-service action description.
                - **DefinitionType** *(string) --* 
                  The self-service action definition type. For example, ``SSM_AUTOMATION`` .
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ProductId: string
        :param ProductId: **[REQUIRED]**
          The product identifier. For example, ``prod-abcdzk7xy33qa`` .
        :type ProvisioningArtifactId: string
        :param ProvisioningArtifactId: **[REQUIRED]**
          The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .
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
        """
        pass


class ListTagOptions(Paginator):
    def paginate(self, Filters: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceCatalog.Client.list_tag_options`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListTagOptions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters={
                  'Key': 'string',
                  'Value': 'string',
                  'Active': True|False
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
                'TagOptionDetails': [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Active': True|False,
                        'Id': 'string'
                    },
                ],
                'NextToken': 'string'
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
        """
        pass


class ScanProvisionedProducts(Paginator):
    def paginate(self, AcceptLanguage: str = None, AccessLevelFilter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceCatalog.Client.scan_provisioned_products`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ScanProvisionedProducts>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AcceptLanguage='string',
              AccessLevelFilter={
                  'Key': 'Account'|'Role'|'User',
                  'Value': 'string'
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
                'ProvisionedProducts': [
                    {
                        'Name': 'string',
                        'Arn': 'string',
                        'Type': 'string',
                        'Id': 'string',
                        'Status': 'AVAILABLE'|'UNDER_CHANGE'|'TAINTED'|'ERROR'|'PLAN_IN_PROGRESS',
                        'StatusMessage': 'string',
                        'CreatedTime': datetime(2015, 1, 1),
                        'IdempotencyToken': 'string',
                        'LastRecordId': 'string',
                        'ProductId': 'string',
                        'ProvisioningArtifactId': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProvisionedProducts** *(list) --* 
              Information about the provisioned products.
              - *(dict) --* 
                Information about a provisioned product.
                - **Name** *(string) --* 
                  The user-friendly name of the provisioned product.
                - **Arn** *(string) --* 
                  The ARN of the provisioned product.
                - **Type** *(string) --* 
                  The type of provisioned product. The supported values are ``CFN_STACK`` and ``CFN_STACKSET`` .
                - **Id** *(string) --* 
                  The identifier of the provisioned product.
                - **Status** *(string) --* 
                  The current status of the provisioned product.
                  * ``AVAILABLE`` - Stable state, ready to perform any operation. The most recent operation succeeded and completed. 
                  * ``UNDER_CHANGE`` - Transitive state. Operations performed might not have valid results. Wait for an ``AVAILABLE`` status before performing operations. 
                  * ``TAINTED`` - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version. 
                  * ``ERROR`` - An unexpected error occurred. The provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack. 
                  * ``PLAN_IN_PROGRESS`` - Transitive state. The plan operations were performed to provision a new product, but resources have not yet been created. After reviewing the list of resources to be created, execute the plan. Wait for an ``AVAILABLE`` status before performing operations. 
                - **StatusMessage** *(string) --* 
                  The current status message of the provisioned product.
                - **CreatedTime** *(datetime) --* 
                  The UTC time stamp of the creation time.
                - **IdempotencyToken** *(string) --* 
                  A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
                - **LastRecordId** *(string) --* 
                  The record identifier of the last request performed on this provisioned product.
                - **ProductId** *(string) --* 
                  The product identifier. For example, ``prod-abcdzk7xy33qa`` .
                - **ProvisioningArtifactId** *(string) --* 
                  The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type AccessLevelFilter: dict
        :param AccessLevelFilter:
          The access level to use to obtain results. The default is ``User`` .
          - **Key** *(string) --*
            The access level.
            * ``Account`` - Filter results based on the account.
            * ``Role`` - Filter results based on the federated role of the specified user.
            * ``User`` - Filter results based on the specified user.
          - **Value** *(string) --*
            The user to which the access level applies. The only supported value is ``Self`` .
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


class SearchProductsAsAdmin(Paginator):
    def paginate(self, AcceptLanguage: str = None, PortfolioId: str = None, Filters: Dict = None, SortBy: str = None, SortOrder: str = None, ProductSource: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceCatalog.Client.search_products_as_admin`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/SearchProductsAsAdmin>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AcceptLanguage='string',
              PortfolioId='string',
              Filters={
                  'string': [
                      'string',
                  ]
              },
              SortBy='Title'|'VersionCount'|'CreationDate',
              SortOrder='ASCENDING'|'DESCENDING',
              ProductSource='ACCOUNT',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ProductViewDetails': [
                    {
                        'ProductViewSummary': {
                            'Id': 'string',
                            'ProductId': 'string',
                            'Name': 'string',
                            'Owner': 'string',
                            'ShortDescription': 'string',
                            'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
                            'Distributor': 'string',
                            'HasDefaultPath': True|False,
                            'SupportEmail': 'string',
                            'SupportDescription': 'string',
                            'SupportUrl': 'string'
                        },
                        'Status': 'AVAILABLE'|'CREATING'|'FAILED',
                        'ProductARN': 'string',
                        'CreatedTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
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
        """
        pass
