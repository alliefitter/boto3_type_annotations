from typing import Union
from typing import List
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Optional
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def accept_portfolio_share(self, PortfolioId: str, AcceptLanguage: str = None, PortfolioShareType: str = None) -> Dict:
        """
        Accepts an offer to share the specified portfolio.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/AcceptPortfolioShare>`_
        
        **Request Syntax**
        ::
          response = client.accept_portfolio_share(
              AcceptLanguage='string',
              PortfolioId='string',
              PortfolioShareType='IMPORTED'|'AWS_SERVICECATALOG'|'AWS_ORGANIZATIONS'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type PortfolioId: string
        :param PortfolioId: **[REQUIRED]**
          The portfolio identifier.
        :type PortfolioShareType: string
        :param PortfolioShareType:
          The type of shared portfolios to accept. The default is to accept imported portfolios.
          * ``AWS_ORGANIZATIONS`` - Accept portfolios shared by the master account of your organization.
          * ``IMPORTED`` - Accept imported portfolios.
          * ``AWS_SERVICECATALOG`` - Not supported. (Throws ResourceNotFoundException.)
          For example, ``aws servicecatalog accept-portfolio-share --portfolio-id \"port-2qwzkwxt3y5fk\" --portfolio-share-type AWS_ORGANIZATIONS``
        :rtype: dict
        :returns:
        """
        pass

    def associate_principal_with_portfolio(self, PortfolioId: str, PrincipalARN: str, PrincipalType: str, AcceptLanguage: str = None) -> Dict:
        """
        Associates the specified principal ARN with the specified portfolio.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio>`_
        
        **Request Syntax**
        ::
          response = client.associate_principal_with_portfolio(
              AcceptLanguage='string',
              PortfolioId='string',
              PrincipalARN='string',
              PrincipalType='IAM'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type PortfolioId: string
        :param PortfolioId: **[REQUIRED]**
          The portfolio identifier.
        :type PrincipalARN: string
        :param PrincipalARN: **[REQUIRED]**
          The ARN of the principal (IAM user, role, or group).
        :type PrincipalType: string
        :param PrincipalType: **[REQUIRED]**
          The principal type. The supported value is ``IAM`` .
        :rtype: dict
        :returns:
        """
        pass

    def associate_product_with_portfolio(self, ProductId: str, PortfolioId: str, AcceptLanguage: str = None, SourcePortfolioId: str = None) -> Dict:
        """
        Associates the specified product with the specified portfolio.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/AssociateProductWithPortfolio>`_
        
        **Request Syntax**
        ::
          response = client.associate_product_with_portfolio(
              AcceptLanguage='string',
              ProductId='string',
              PortfolioId='string',
              SourcePortfolioId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type ProductId: string
        :param ProductId: **[REQUIRED]**
          The product identifier.
        :type PortfolioId: string
        :param PortfolioId: **[REQUIRED]**
          The portfolio identifier.
        :type SourcePortfolioId: string
        :param SourcePortfolioId:
          The identifier of the source portfolio.
        :rtype: dict
        :returns:
        """
        pass

    def associate_service_action_with_provisioning_artifact(self, ProductId: str, ProvisioningArtifactId: str, ServiceActionId: str, AcceptLanguage: str = None) -> Dict:
        """
        Associates a self-service action with a provisioning artifact.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/AssociateServiceActionWithProvisioningArtifact>`_
        
        **Request Syntax**
        ::
          response = client.associate_service_action_with_provisioning_artifact(
              ProductId='string',
              ProvisioningArtifactId='string',
              ServiceActionId='string',
              AcceptLanguage='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ProductId: string
        :param ProductId: **[REQUIRED]**
          The product identifier. For example, ``prod-abcdzk7xy33qa`` .
        :type ProvisioningArtifactId: string
        :param ProvisioningArtifactId: **[REQUIRED]**
          The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .
        :type ServiceActionId: string
        :param ServiceActionId: **[REQUIRED]**
          The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :rtype: dict
        :returns:
        """
        pass

    def associate_tag_option_with_resource(self, ResourceId: str, TagOptionId: str) -> Dict:
        """
        Associate the specified TagOption with the specified portfolio or product.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/AssociateTagOptionWithResource>`_
        
        **Request Syntax**
        ::
          response = client.associate_tag_option_with_resource(
              ResourceId='string',
              TagOptionId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**
          The resource identifier.
        :type TagOptionId: string
        :param TagOptionId: **[REQUIRED]**
          The TagOption identifier.
        :rtype: dict
        :returns:
        """
        pass

    def batch_associate_service_action_with_provisioning_artifact(self, ServiceActionAssociations: List, AcceptLanguage: str = None) -> Dict:
        """
        Associates multiple self-service actions with provisioning artifacts.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/BatchAssociateServiceActionWithProvisioningArtifact>`_
        
        **Request Syntax**
        ::
          response = client.batch_associate_service_action_with_provisioning_artifact(
              ServiceActionAssociations=[
                  {
                      'ServiceActionId': 'string',
                      'ProductId': 'string',
                      'ProvisioningArtifactId': 'string'
                  },
              ],
              AcceptLanguage='string'
          )
        
        **Response Syntax**
        ::
            {
                'FailedServiceActionAssociations': [
                    {
                        'ServiceActionId': 'string',
                        'ProductId': 'string',
                        'ProvisioningArtifactId': 'string',
                        'ErrorCode': 'DUPLICATE_RESOURCE'|'INTERNAL_FAILURE'|'LIMIT_EXCEEDED'|'RESOURCE_NOT_FOUND'|'THROTTLING',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FailedServiceActionAssociations** *(list) --* 
              An object that contains a list of errors, along with information to help you identify the self-service action.
              - *(dict) --* 
                An object containing information about the error, along with identifying information about the self-service action and its associations.
                - **ServiceActionId** *(string) --* 
                  The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .
                - **ProductId** *(string) --* 
                  The product identifier. For example, ``prod-abcdzk7xy33qa`` .
                - **ProvisioningArtifactId** *(string) --* 
                  The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .
                - **ErrorCode** *(string) --* 
                  The error code. Valid values are listed below.
                - **ErrorMessage** *(string) --* 
                  A text description of the error.
        :type ServiceActionAssociations: list
        :param ServiceActionAssociations: **[REQUIRED]**
          One or more associations, each consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.
          - *(dict) --*
            A self-service action association consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.
            - **ServiceActionId** *(string) --* **[REQUIRED]**
              The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .
            - **ProductId** *(string) --* **[REQUIRED]**
              The product identifier. For example, ``prod-abcdzk7xy33qa`` .
            - **ProvisioningArtifactId** *(string) --* **[REQUIRED]**
              The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :rtype: dict
        :returns:
        """
        pass

    def batch_disassociate_service_action_from_provisioning_artifact(self, ServiceActionAssociations: List, AcceptLanguage: str = None) -> Dict:
        """
        Disassociates a batch of self-service actions from the specified provisioning artifact.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/BatchDisassociateServiceActionFromProvisioningArtifact>`_
        
        **Request Syntax**
        ::
          response = client.batch_disassociate_service_action_from_provisioning_artifact(
              ServiceActionAssociations=[
                  {
                      'ServiceActionId': 'string',
                      'ProductId': 'string',
                      'ProvisioningArtifactId': 'string'
                  },
              ],
              AcceptLanguage='string'
          )
        
        **Response Syntax**
        ::
            {
                'FailedServiceActionAssociations': [
                    {
                        'ServiceActionId': 'string',
                        'ProductId': 'string',
                        'ProvisioningArtifactId': 'string',
                        'ErrorCode': 'DUPLICATE_RESOURCE'|'INTERNAL_FAILURE'|'LIMIT_EXCEEDED'|'RESOURCE_NOT_FOUND'|'THROTTLING',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FailedServiceActionAssociations** *(list) --* 
              An object that contains a list of errors, along with information to help you identify the self-service action.
              - *(dict) --* 
                An object containing information about the error, along with identifying information about the self-service action and its associations.
                - **ServiceActionId** *(string) --* 
                  The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .
                - **ProductId** *(string) --* 
                  The product identifier. For example, ``prod-abcdzk7xy33qa`` .
                - **ProvisioningArtifactId** *(string) --* 
                  The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .
                - **ErrorCode** *(string) --* 
                  The error code. Valid values are listed below.
                - **ErrorMessage** *(string) --* 
                  A text description of the error.
        :type ServiceActionAssociations: list
        :param ServiceActionAssociations: **[REQUIRED]**
          One or more associations, each consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.
          - *(dict) --*
            A self-service action association consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.
            - **ServiceActionId** *(string) --* **[REQUIRED]**
              The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .
            - **ProductId** *(string) --* **[REQUIRED]**
              The product identifier. For example, ``prod-abcdzk7xy33qa`` .
            - **ProvisioningArtifactId** *(string) --* **[REQUIRED]**
              The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :rtype: dict
        :returns:
        """
        pass

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

    def copy_product(self, SourceProductArn: str, IdempotencyToken: str, AcceptLanguage: str = None, TargetProductId: str = None, TargetProductName: str = None, SourceProvisioningArtifactIdentifiers: List = None, CopyOptions: List = None) -> Dict:
        """
        Copies the specified source product to the specified target product or a new product.
        You can copy a product to the same account or another account. You can copy a product to the same region or another region.
        This operation is performed asynchronously. To track the progress of the operation, use  DescribeCopyProductStatus .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/CopyProduct>`_
        
        **Request Syntax**
        ::
          response = client.copy_product(
              AcceptLanguage='string',
              SourceProductArn='string',
              TargetProductId='string',
              TargetProductName='string',
              SourceProvisioningArtifactIdentifiers=[
                  {
                      'string': 'string'
                  },
              ],
              CopyOptions=[
                  'CopyTags',
              ],
              IdempotencyToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'CopyProductToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CopyProductToken** *(string) --* 
              The token to use to track the progress of the operation.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type SourceProductArn: string
        :param SourceProductArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the source product.
        :type TargetProductId: string
        :param TargetProductId:
          The identifier of the target product. By default, a new product is created.
        :type TargetProductName: string
        :param TargetProductName:
          A name for the target product. The default is the name of the source product.
        :type SourceProvisioningArtifactIdentifiers: list
        :param SourceProvisioningArtifactIdentifiers:
          The identifiers of the provisioning artifacts (also known as versions) of the product to copy. By default, all provisioning artifacts are copied.
          - *(dict) --*
            - *(string) --*
              - *(string) --*
        :type CopyOptions: list
        :param CopyOptions:
          The copy options. If the value is ``CopyTags`` , the tags from the source product are copied to the target product.
          - *(string) --*
        :type IdempotencyToken: string
        :param IdempotencyToken: **[REQUIRED]**
          A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
          This field is autopopulated if not provided.
        :rtype: dict
        :returns:
        """
        pass

    def create_constraint(self, PortfolioId: str, ProductId: str, Parameters: str, Type: str, IdempotencyToken: str, AcceptLanguage: str = None, Description: str = None) -> Dict:
        """
        Creates a constraint.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/CreateConstraint>`_
        
        **Request Syntax**
        ::
          response = client.create_constraint(
              AcceptLanguage='string',
              PortfolioId='string',
              ProductId='string',
              Parameters='string',
              Type='string',
              Description='string',
              IdempotencyToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'ConstraintDetail': {
                    'ConstraintId': 'string',
                    'Type': 'string',
                    'Description': 'string',
                    'Owner': 'string'
                },
                'ConstraintParameters': 'string',
                'Status': 'AVAILABLE'|'CREATING'|'FAILED'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ConstraintDetail** *(dict) --* 
              Information about the constraint.
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
            - **ConstraintParameters** *(string) --* 
              The constraint parameters.
            - **Status** *(string) --* 
              The status of the current request.
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
        :param ProductId: **[REQUIRED]**
          The product identifier.
        :type Parameters: string
        :param Parameters: **[REQUIRED]**
          The constraint parameters, in JSON format. The syntax depends on the constraint type as follows:
            LAUNCH
          Specify the ``RoleArn`` property as follows:
           ``{\"RoleArn\" : \"arn:aws:iam::123456789012:role/LaunchRole\"}``
          You cannot have both a ``LAUNCH`` and a ``STACKSET`` constraint.
          You also cannot have more than one ``LAUNCH`` constraint on a product and portfolio.
            NOTIFICATION
          Specify the ``NotificationArns`` property as follows:
           ``{\"NotificationArns\" : [\"arn:aws:sns:us-east-1:123456789012:Topic\"]}``
            STACKSET
          Specify the ``Parameters`` property as follows:
           ``{\"Version\": \"String\", \"Properties\": {\"AccountList\": [ \"String\" ], \"RegionList\": [ \"String\" ], \"AdminRole\": \"String\", \"ExecutionRole\": \"String\"}}``
          You cannot have both a ``LAUNCH`` and a ``STACKSET`` constraint.
          You also cannot have more than one ``STACKSET`` constraint on a product and portfolio.
          Products with a ``STACKSET`` constraint will launch an AWS CloudFormation stack set.
            TEMPLATE
          Specify the ``Rules`` property. For more information, see `Template Constraint Rules <http://docs.aws.amazon.com/servicecatalog/latest/adminguide/reference-template_constraint_rules.html>`__ .
        :type Type: string
        :param Type: **[REQUIRED]**
          The type of constraint.
          * ``LAUNCH``
          * ``NOTIFICATION``
          * ``STACKSET``
          * ``TEMPLATE``
        :type Description: string
        :param Description:
          The description of the constraint.
        :type IdempotencyToken: string
        :param IdempotencyToken: **[REQUIRED]**
          A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
          This field is autopopulated if not provided.
        :rtype: dict
        :returns:
        """
        pass

    def create_portfolio(self, DisplayName: str, ProviderName: str, IdempotencyToken: str, AcceptLanguage: str = None, Description: str = None, Tags: List = None) -> Dict:
        """
        Creates a portfolio.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/CreatePortfolio>`_
        
        **Request Syntax**
        ::
          response = client.create_portfolio(
              AcceptLanguage='string',
              DisplayName='string',
              Description='string',
              ProviderName='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              IdempotencyToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'PortfolioDetail': {
                    'Id': 'string',
                    'ARN': 'string',
                    'DisplayName': 'string',
                    'Description': 'string',
                    'CreatedTime': datetime(2015, 1, 1),
                    'ProviderName': 'string'
                },
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PortfolioDetail** *(dict) --* 
              Information about the portfolio.
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
            - **Tags** *(list) --* 
              Information about the tags associated with the portfolio.
              - *(dict) --* 
                Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
                - **Key** *(string) --* 
                  The tag key.
                - **Value** *(string) --* 
                  The value for this key.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type DisplayName: string
        :param DisplayName: **[REQUIRED]**
          The name to use for display purposes.
        :type Description: string
        :param Description:
          The description of the portfolio.
        :type ProviderName: string
        :param ProviderName: **[REQUIRED]**
          The name of the portfolio provider.
        :type Tags: list
        :param Tags:
          One or more tags.
          - *(dict) --*
            Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
            - **Key** *(string) --* **[REQUIRED]**
              The tag key.
            - **Value** *(string) --* **[REQUIRED]**
              The value for this key.
        :type IdempotencyToken: string
        :param IdempotencyToken: **[REQUIRED]**
          A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
          This field is autopopulated if not provided.
        :rtype: dict
        :returns:
        """
        pass

    def create_portfolio_share(self, PortfolioId: str, AcceptLanguage: str = None, AccountId: str = None, OrganizationNode: Dict = None) -> Dict:
        """
        Shares the specified portfolio with the specified account or organization node. Shares to an organization node can only be created by the master account of an Organization. AWSOrganizationsAccess must be enabled in order to create a portfolio share to an organization node.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/CreatePortfolioShare>`_
        
        **Request Syntax**
        ::
          response = client.create_portfolio_share(
              AcceptLanguage='string',
              PortfolioId='string',
              AccountId='string',
              OrganizationNode={
                  'Type': 'ORGANIZATION'|'ORGANIZATIONAL_UNIT'|'ACCOUNT',
                  'Value': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'PortfolioShareToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PortfolioShareToken** *(string) --* 
              The portfolio share unique identifier. This will only be returned if portfolio is shared to an organization node.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type PortfolioId: string
        :param PortfolioId: **[REQUIRED]**
          The portfolio identifier.
        :type AccountId: string
        :param AccountId:
          The AWS account ID. For example, ``123456789012`` .
        :type OrganizationNode: dict
        :param OrganizationNode:
          The organization node to whom you are going to share. If ``OrganizationNode`` is passed in, ``PortfolioShare`` will be created for the node and its children (when applies), and a ``PortfolioShareToken`` will be returned in the output in order for the administrator to monitor the status of the ``PortfolioShare`` creation process.
          - **Type** *(string) --*
            The organization node type.
          - **Value** *(string) --*
            The identifier of the organization node.
        :rtype: dict
        :returns:
        """
        pass

    def create_product(self, Name: str, Owner: str, ProductType: str, ProvisioningArtifactParameters: Dict, IdempotencyToken: str, AcceptLanguage: str = None, Description: str = None, Distributor: str = None, SupportDescription: str = None, SupportEmail: str = None, SupportUrl: str = None, Tags: List = None) -> Dict:
        """
        Creates a product.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/CreateProduct>`_
        
        **Request Syntax**
        ::
          response = client.create_product(
              AcceptLanguage='string',
              Name='string',
              Owner='string',
              Description='string',
              Distributor='string',
              SupportDescription='string',
              SupportEmail='string',
              SupportUrl='string',
              ProductType='CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              ProvisioningArtifactParameters={
                  'Name': 'string',
                  'Description': 'string',
                  'Info': {
                      'string': 'string'
                  },
                  'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR'
              },
              IdempotencyToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'ProductViewDetail': {
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
                'ProvisioningArtifactDetail': {
                    'Id': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
                    'CreatedTime': datetime(2015, 1, 1),
                    'Active': True|False
                },
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProductViewDetail** *(dict) --* 
              Information about the product view.
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
            - **ProvisioningArtifactDetail** *(dict) --* 
              Information about the provisioning artifact.
              - **Id** *(string) --* 
                The identifier of the provisioning artifact.
              - **Name** *(string) --* 
                The name of the provisioning artifact.
              - **Description** *(string) --* 
                The description of the provisioning artifact.
              - **Type** *(string) --* 
                The type of provisioning artifact.
                * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template 
                * ``MARKETPLACE_AMI`` - AWS Marketplace AMI 
                * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources 
              - **CreatedTime** *(datetime) --* 
                The UTC time stamp of the creation time.
              - **Active** *(boolean) --* 
                Indicates whether the product version is active.
            - **Tags** *(list) --* 
              Information about the tags associated with the product.
              - *(dict) --* 
                Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
                - **Key** *(string) --* 
                  The tag key.
                - **Value** *(string) --* 
                  The value for this key.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type Name: string
        :param Name: **[REQUIRED]**
          The name of the product.
        :type Owner: string
        :param Owner: **[REQUIRED]**
          The owner of the product.
        :type Description: string
        :param Description:
          The description of the product.
        :type Distributor: string
        :param Distributor:
          The distributor of the product.
        :type SupportDescription: string
        :param SupportDescription:
          The support information about the product.
        :type SupportEmail: string
        :param SupportEmail:
          The contact email for product support.
        :type SupportUrl: string
        :param SupportUrl:
          The contact URL for product support.
        :type ProductType: string
        :param ProductType: **[REQUIRED]**
          The type of product.
        :type Tags: list
        :param Tags:
          One or more tags.
          - *(dict) --*
            Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
            - **Key** *(string) --* **[REQUIRED]**
              The tag key.
            - **Value** *(string) --* **[REQUIRED]**
              The value for this key.
        :type ProvisioningArtifactParameters: dict
        :param ProvisioningArtifactParameters: **[REQUIRED]**
          The configuration of the provisioning artifact.
          - **Name** *(string) --*
            The name of the provisioning artifact (for example, v1 v2beta). No spaces are allowed.
          - **Description** *(string) --*
            The description of the provisioning artifact, including how it differs from the previous provisioning artifact.
          - **Info** *(dict) --* **[REQUIRED]**
            The URL of the CloudFormation template in Amazon S3. Specify the URL in JSON format as follows:
             ``\"LoadTemplateFromURL\": \"https://s3.amazonaws.com/cf-templates-ozkq9d3hgiq2-us-east-1/...\"``
            - *(string) --*
              - *(string) --*
          - **Type** *(string) --*
            The type of provisioning artifact.
            * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template
            * ``MARKETPLACE_AMI`` - AWS Marketplace AMI
            * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources
        :type IdempotencyToken: string
        :param IdempotencyToken: **[REQUIRED]**
          A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
          This field is autopopulated if not provided.
        :rtype: dict
        :returns:
        """
        pass

    def create_provisioned_product_plan(self, PlanName: str, PlanType: str, ProductId: str, ProvisionedProductName: str, ProvisioningArtifactId: str, IdempotencyToken: str, AcceptLanguage: str = None, NotificationArns: List = None, PathId: str = None, ProvisioningParameters: List = None, Tags: List = None) -> Dict:
        """
        Creates a plan. A plan includes the list of resources to be created (when provisioning a new product) or modified (when updating a provisioned product) when the plan is executed.
        You can create one plan per provisioned product. To create a plan for an existing provisioned product, the product status must be AVAILBLE or TAINTED.
        To view the resource changes in the change set, use  DescribeProvisionedProductPlan . To create or modify the provisioned product, use  ExecuteProvisionedProductPlan .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/CreateProvisionedProductPlan>`_
        
        **Request Syntax**
        ::
          response = client.create_provisioned_product_plan(
              AcceptLanguage='string',
              PlanName='string',
              PlanType='CLOUDFORMATION',
              NotificationArns=[
                  'string',
              ],
              PathId='string',
              ProductId='string',
              ProvisionedProductName='string',
              ProvisioningArtifactId='string',
              ProvisioningParameters=[
                  {
                      'Key': 'string',
                      'Value': 'string',
                      'UsePreviousValue': True|False
                  },
              ],
              IdempotencyToken='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'PlanName': 'string',
                'PlanId': 'string',
                'ProvisionProductId': 'string',
                'ProvisionedProductName': 'string',
                'ProvisioningArtifactId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PlanName** *(string) --* 
              The name of the plan.
            - **PlanId** *(string) --* 
              The plan identifier.
            - **ProvisionProductId** *(string) --* 
              The product identifier.
            - **ProvisionedProductName** *(string) --* 
              The user-friendly name of the provisioned product.
            - **ProvisioningArtifactId** *(string) --* 
              The identifier of the provisioning artifact.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type PlanName: string
        :param PlanName: **[REQUIRED]**
          The name of the plan.
        :type PlanType: string
        :param PlanType: **[REQUIRED]**
          The plan type.
        :type NotificationArns: list
        :param NotificationArns:
          Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.
          - *(string) --*
        :type PathId: string
        :param PathId:
          The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use  ListLaunchPaths .
        :type ProductId: string
        :param ProductId: **[REQUIRED]**
          The product identifier.
        :type ProvisionedProductName: string
        :param ProvisionedProductName: **[REQUIRED]**
          A user-friendly name for the provisioned product. This value must be unique for the AWS account and cannot be updated after the product is provisioned.
        :type ProvisioningArtifactId: string
        :param ProvisioningArtifactId: **[REQUIRED]**
          The identifier of the provisioning artifact.
        :type ProvisioningParameters: list
        :param ProvisioningParameters:
          Parameters specified by the administrator that are required for provisioning the product.
          - *(dict) --*
            The parameter key-value pair used to update a provisioned product.
            - **Key** *(string) --*
              The parameter key.
            - **Value** *(string) --*
              The parameter value.
            - **UsePreviousValue** *(boolean) --*
              If set to true, ``Value`` is ignored and the previous parameter value is kept.
        :type IdempotencyToken: string
        :param IdempotencyToken: **[REQUIRED]**
          A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
          This field is autopopulated if not provided.
        :type Tags: list
        :param Tags:
          One or more tags.
          - *(dict) --*
            Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
            - **Key** *(string) --* **[REQUIRED]**
              The tag key.
            - **Value** *(string) --* **[REQUIRED]**
              The value for this key.
        :rtype: dict
        :returns:
        """
        pass

    def create_provisioning_artifact(self, ProductId: str, Parameters: Dict, IdempotencyToken: str, AcceptLanguage: str = None) -> Dict:
        """
        Creates a provisioning artifact (also known as a version) for the specified product.
        You cannot create a provisioning artifact for a product that was shared with you.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/CreateProvisioningArtifact>`_
        
        **Request Syntax**
        ::
          response = client.create_provisioning_artifact(
              AcceptLanguage='string',
              ProductId='string',
              Parameters={
                  'Name': 'string',
                  'Description': 'string',
                  'Info': {
                      'string': 'string'
                  },
                  'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR'
              },
              IdempotencyToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'ProvisioningArtifactDetail': {
                    'Id': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
                    'CreatedTime': datetime(2015, 1, 1),
                    'Active': True|False
                },
                'Info': {
                    'string': 'string'
                },
                'Status': 'AVAILABLE'|'CREATING'|'FAILED'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProvisioningArtifactDetail** *(dict) --* 
              Information about the provisioning artifact.
              - **Id** *(string) --* 
                The identifier of the provisioning artifact.
              - **Name** *(string) --* 
                The name of the provisioning artifact.
              - **Description** *(string) --* 
                The description of the provisioning artifact.
              - **Type** *(string) --* 
                The type of provisioning artifact.
                * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template 
                * ``MARKETPLACE_AMI`` - AWS Marketplace AMI 
                * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources 
              - **CreatedTime** *(datetime) --* 
                The UTC time stamp of the creation time.
              - **Active** *(boolean) --* 
                Indicates whether the product version is active.
            - **Info** *(dict) --* 
              The URL of the CloudFormation template in Amazon S3, in JSON format.
              - *(string) --* 
                - *(string) --* 
            - **Status** *(string) --* 
              The status of the current request.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type ProductId: string
        :param ProductId: **[REQUIRED]**
          The product identifier.
        :type Parameters: dict
        :param Parameters: **[REQUIRED]**
          The configuration for the provisioning artifact.
          - **Name** *(string) --*
            The name of the provisioning artifact (for example, v1 v2beta). No spaces are allowed.
          - **Description** *(string) --*
            The description of the provisioning artifact, including how it differs from the previous provisioning artifact.
          - **Info** *(dict) --* **[REQUIRED]**
            The URL of the CloudFormation template in Amazon S3. Specify the URL in JSON format as follows:
             ``\"LoadTemplateFromURL\": \"https://s3.amazonaws.com/cf-templates-ozkq9d3hgiq2-us-east-1/...\"``
            - *(string) --*
              - *(string) --*
          - **Type** *(string) --*
            The type of provisioning artifact.
            * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template
            * ``MARKETPLACE_AMI`` - AWS Marketplace AMI
            * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources
        :type IdempotencyToken: string
        :param IdempotencyToken: **[REQUIRED]**
          A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
          This field is autopopulated if not provided.
        :rtype: dict
        :returns:
        """
        pass

    def create_service_action(self, Name: str, DefinitionType: str, Definition: Dict, IdempotencyToken: str, Description: str = None, AcceptLanguage: str = None) -> Dict:
        """
        Creates a self-service action.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/CreateServiceAction>`_
        
        **Request Syntax**
        ::
          response = client.create_service_action(
              Name='string',
              DefinitionType='SSM_AUTOMATION',
              Definition={
                  'string': 'string'
              },
              Description='string',
              AcceptLanguage='string',
              IdempotencyToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'ServiceActionDetail': {
                    'ServiceActionSummary': {
                        'Id': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'DefinitionType': 'SSM_AUTOMATION'
                    },
                    'Definition': {
                        'string': 'string'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ServiceActionDetail** *(dict) --* 
              An object containing information about the self-service action.
              - **ServiceActionSummary** *(dict) --* 
                Summary information about the self-service action.
                - **Id** *(string) --* 
                  The self-service action identifier.
                - **Name** *(string) --* 
                  The self-service action name.
                - **Description** *(string) --* 
                  The self-service action description.
                - **DefinitionType** *(string) --* 
                  The self-service action definition type. For example, ``SSM_AUTOMATION`` .
              - **Definition** *(dict) --* 
                A map that defines the self-service action.
                - *(string) --* 
                  - *(string) --* 
        :type Name: string
        :param Name: **[REQUIRED]**
          The self-service action name.
        :type DefinitionType: string
        :param DefinitionType: **[REQUIRED]**
          The service action definition type. For example, ``SSM_AUTOMATION`` .
        :type Definition: dict
        :param Definition: **[REQUIRED]**
          The self-service action definition. Can be one of the following:
            Name
          The name of the AWS Systems Manager Document. For example, ``AWS-RestartEC2Instance`` .
            Version
          The AWS Systems Manager automation document version. For example, ``\"Version\": \"1\"``
            AssumeRole
          The Amazon Resource Name (ARN) of the role that performs the self-service actions on your behalf. For example, ``\"AssumeRole\": \"arn:aws:iam::12345678910:role/ActionRole\"`` .
          To reuse the provisioned product launch role, set to ``\"AssumeRole\": \"LAUNCH_ROLE\"`` .
            Parameters
          The list of parameters in JSON format.
          For example: ``[{\\"Name\\":\\"InstanceId\\",\\"Type\\":\\"TARGET\\"}]`` .
          - *(string) --*
            - *(string) --*
        :type Description: string
        :param Description:
          The self-service action description.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type IdempotencyToken: string
        :param IdempotencyToken: **[REQUIRED]**
          A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
          This field is autopopulated if not provided.
        :rtype: dict
        :returns:
        """
        pass

    def create_tag_option(self, Key: str, Value: str) -> Dict:
        """
        Creates a TagOption.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/CreateTagOption>`_
        
        **Request Syntax**
        ::
          response = client.create_tag_option(
              Key='string',
              Value='string'
          )
        
        **Response Syntax**
        ::
            {
                'TagOptionDetail': {
                    'Key': 'string',
                    'Value': 'string',
                    'Active': True|False,
                    'Id': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TagOptionDetail** *(dict) --* 
              Information about the TagOption.
              - **Key** *(string) --* 
                The TagOption key.
              - **Value** *(string) --* 
                The TagOption value.
              - **Active** *(boolean) --* 
                The TagOption active state.
              - **Id** *(string) --* 
                The TagOption identifier.
        :type Key: string
        :param Key: **[REQUIRED]**
          The TagOption key.
        :type Value: string
        :param Value: **[REQUIRED]**
          The TagOption value.
        :rtype: dict
        :returns:
        """
        pass

    def delete_constraint(self, Id: str, AcceptLanguage: str = None) -> Dict:
        """
        Deletes the specified constraint.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DeleteConstraint>`_
        
        **Request Syntax**
        ::
          response = client.delete_constraint(
              AcceptLanguage='string',
              Id='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type Id: string
        :param Id: **[REQUIRED]**
          The identifier of the constraint.
        :rtype: dict
        :returns:
        """
        pass

    def delete_portfolio(self, Id: str, AcceptLanguage: str = None) -> Dict:
        """
        Deletes the specified portfolio.
        You cannot delete a portfolio if it was shared with you or if it has associated products, users, constraints, or shared accounts.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DeletePortfolio>`_
        
        **Request Syntax**
        ::
          response = client.delete_portfolio(
              AcceptLanguage='string',
              Id='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type Id: string
        :param Id: **[REQUIRED]**
          The portfolio identifier.
        :rtype: dict
        :returns:
        """
        pass

    def delete_portfolio_share(self, PortfolioId: str, AcceptLanguage: str = None, AccountId: str = None, OrganizationNode: Dict = None) -> Dict:
        """
        Stops sharing the specified portfolio with the specified account or organization node. Shares to an organization node can only be deleted by the master account of an Organization.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DeletePortfolioShare>`_
        
        **Request Syntax**
        ::
          response = client.delete_portfolio_share(
              AcceptLanguage='string',
              PortfolioId='string',
              AccountId='string',
              OrganizationNode={
                  'Type': 'ORGANIZATION'|'ORGANIZATIONAL_UNIT'|'ACCOUNT',
                  'Value': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'PortfolioShareToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PortfolioShareToken** *(string) --* 
              The portfolio share unique identifier. This will only be returned if delete is made to an organization node.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type PortfolioId: string
        :param PortfolioId: **[REQUIRED]**
          The portfolio identifier.
        :type AccountId: string
        :param AccountId:
          The AWS account ID.
        :type OrganizationNode: dict
        :param OrganizationNode:
          The organization node to whom you are going to stop sharing.
          - **Type** *(string) --*
            The organization node type.
          - **Value** *(string) --*
            The identifier of the organization node.
        :rtype: dict
        :returns:
        """
        pass

    def delete_product(self, Id: str, AcceptLanguage: str = None) -> Dict:
        """
        Deletes the specified product.
        You cannot delete a product if it was shared with you or is associated with a portfolio.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DeleteProduct>`_
        
        **Request Syntax**
        ::
          response = client.delete_product(
              AcceptLanguage='string',
              Id='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type Id: string
        :param Id: **[REQUIRED]**
          The product identifier.
        :rtype: dict
        :returns:
        """
        pass

    def delete_provisioned_product_plan(self, PlanId: str, AcceptLanguage: str = None, IgnoreErrors: bool = None) -> Dict:
        """
        Deletes the specified plan.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DeleteProvisionedProductPlan>`_
        
        **Request Syntax**
        ::
          response = client.delete_provisioned_product_plan(
              AcceptLanguage='string',
              PlanId='string',
              IgnoreErrors=True|False
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type PlanId: string
        :param PlanId: **[REQUIRED]**
          The plan identifier.
        :type IgnoreErrors: boolean
        :param IgnoreErrors:
          If set to true, AWS Service Catalog stops managing the specified provisioned product even if it cannot delete the underlying resources.
        :rtype: dict
        :returns:
        """
        pass

    def delete_provisioning_artifact(self, ProductId: str, ProvisioningArtifactId: str, AcceptLanguage: str = None) -> Dict:
        """
        Deletes the specified provisioning artifact (also known as a version) for the specified product.
        You cannot delete a provisioning artifact associated with a product that was shared with you. You cannot delete the last provisioning artifact for a product, because a product must have at least one provisioning artifact.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DeleteProvisioningArtifact>`_
        
        **Request Syntax**
        ::
          response = client.delete_provisioning_artifact(
              AcceptLanguage='string',
              ProductId='string',
              ProvisioningArtifactId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type ProductId: string
        :param ProductId: **[REQUIRED]**
          The product identifier.
        :type ProvisioningArtifactId: string
        :param ProvisioningArtifactId: **[REQUIRED]**
          The identifier of the provisioning artifact.
        :rtype: dict
        :returns:
        """
        pass

    def delete_service_action(self, Id: str, AcceptLanguage: str = None) -> Dict:
        """
        Deletes a self-service action.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DeleteServiceAction>`_
        
        **Request Syntax**
        ::
          response = client.delete_service_action(
              Id='string',
              AcceptLanguage='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type Id: string
        :param Id: **[REQUIRED]**
          The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :rtype: dict
        :returns:
        """
        pass

    def delete_tag_option(self, Id: str) -> Dict:
        """
        Deletes the specified TagOption.
        You cannot delete a TagOption if it is associated with a product or portfolio.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DeleteTagOption>`_
        
        **Request Syntax**
        ::
          response = client.delete_tag_option(
              Id='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type Id: string
        :param Id: **[REQUIRED]**
          The TagOption identifier.
        :rtype: dict
        :returns:
        """
        pass

    def describe_constraint(self, Id: str, AcceptLanguage: str = None) -> Dict:
        """
        Gets information about the specified constraint.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeConstraint>`_
        
        **Request Syntax**
        ::
          response = client.describe_constraint(
              AcceptLanguage='string',
              Id='string'
          )
        
        **Response Syntax**
        ::
            {
                'ConstraintDetail': {
                    'ConstraintId': 'string',
                    'Type': 'string',
                    'Description': 'string',
                    'Owner': 'string'
                },
                'ConstraintParameters': 'string',
                'Status': 'AVAILABLE'|'CREATING'|'FAILED'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ConstraintDetail** *(dict) --* 
              Information about the constraint.
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
            - **ConstraintParameters** *(string) --* 
              The constraint parameters.
            - **Status** *(string) --* 
              The status of the current request.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type Id: string
        :param Id: **[REQUIRED]**
          The identifier of the constraint.
        :rtype: dict
        :returns:
        """
        pass

    def describe_copy_product_status(self, CopyProductToken: str, AcceptLanguage: str = None) -> Dict:
        """
        Gets the status of the specified copy product operation.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeCopyProductStatus>`_
        
        **Request Syntax**
        ::
          response = client.describe_copy_product_status(
              AcceptLanguage='string',
              CopyProductToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'CopyProductStatus': 'SUCCEEDED'|'IN_PROGRESS'|'FAILED',
                'TargetProductId': 'string',
                'StatusDetail': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CopyProductStatus** *(string) --* 
              The status of the copy product operation.
            - **TargetProductId** *(string) --* 
              The identifier of the copied product.
            - **StatusDetail** *(string) --* 
              The status message.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type CopyProductToken: string
        :param CopyProductToken: **[REQUIRED]**
          The token for the copy product operation. This token is returned by  CopyProduct .
        :rtype: dict
        :returns:
        """
        pass

    def describe_portfolio(self, Id: str, AcceptLanguage: str = None) -> Dict:
        """
        Gets information about the specified portfolio.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribePortfolio>`_
        
        **Request Syntax**
        ::
          response = client.describe_portfolio(
              AcceptLanguage='string',
              Id='string'
          )
        
        **Response Syntax**
        ::
            {
                'PortfolioDetail': {
                    'Id': 'string',
                    'ARN': 'string',
                    'DisplayName': 'string',
                    'Description': 'string',
                    'CreatedTime': datetime(2015, 1, 1),
                    'ProviderName': 'string'
                },
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'TagOptions': [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Active': True|False,
                        'Id': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PortfolioDetail** *(dict) --* 
              Information about the portfolio.
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
            - **Tags** *(list) --* 
              Information about the tags associated with the portfolio.
              - *(dict) --* 
                Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
                - **Key** *(string) --* 
                  The tag key.
                - **Value** *(string) --* 
                  The value for this key.
            - **TagOptions** *(list) --* 
              Information about the TagOptions associated with the portfolio.
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
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type Id: string
        :param Id: **[REQUIRED]**
          The portfolio identifier.
        :rtype: dict
        :returns:
        """
        pass

    def describe_portfolio_share_status(self, PortfolioShareToken: str) -> Dict:
        """
        Gets the status of the specified portfolio share operation. This API can only be called by the master account in the organization.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribePortfolioShareStatus>`_
        
        **Request Syntax**
        ::
          response = client.describe_portfolio_share_status(
              PortfolioShareToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'PortfolioShareToken': 'string',
                'PortfolioId': 'string',
                'OrganizationNodeValue': 'string',
                'Status': 'NOT_STARTED'|'IN_PROGRESS'|'COMPLETED'|'COMPLETED_WITH_ERRORS'|'ERROR',
                'ShareDetails': {
                    'SuccessfulShares': [
                        'string',
                    ],
                    'ShareErrors': [
                        {
                            'Accounts': [
                                'string',
                            ],
                            'Message': 'string',
                            'Error': 'string'
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PortfolioShareToken** *(string) --* 
              The token for the portfolio share operation. For example, ``share-6v24abcdefghi`` .
            - **PortfolioId** *(string) --* 
              The portfolio identifier.
            - **OrganizationNodeValue** *(string) --* 
              Organization node identifier. It can be either account id, organizational unit id or organization id.
            - **Status** *(string) --* 
              Status of the portfolio share operation.
            - **ShareDetails** *(dict) --* 
              Information about the portfolio share operation.
              - **SuccessfulShares** *(list) --* 
                List of accounts for whom the operation succeeded.
                - *(string) --* 
              - **ShareErrors** *(list) --* 
                List of errors.
                - *(dict) --* 
                  Errors that occurred during the portfolio share operation.
                  - **Accounts** *(list) --* 
                    List of accounts impacted by the error.
                    - *(string) --* 
                  - **Message** *(string) --* 
                    Information about the error.
                  - **Error** *(string) --* 
                    Error type that happened when processing the operation.
        :type PortfolioShareToken: string
        :param PortfolioShareToken: **[REQUIRED]**
          The token for the portfolio share operation. This token is returned either by CreatePortfolioShare or by DeletePortfolioShare.
        :rtype: dict
        :returns:
        """
        pass

    def describe_product(self, Id: str, AcceptLanguage: str = None) -> Dict:
        """
        Gets information about the specified product.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeProduct>`_
        
        **Request Syntax**
        ::
          response = client.describe_product(
              AcceptLanguage='string',
              Id='string'
          )
        
        **Response Syntax**
        ::
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
                'ProvisioningArtifacts': [
                    {
                        'Id': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'CreatedTime': datetime(2015, 1, 1)
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
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
            - **ProvisioningArtifacts** *(list) --* 
              Information about the provisioning artifacts for the specified product.
              - *(dict) --* 
                Information about a provisioning artifact. A provisioning artifact is also known as a product version.
                - **Id** *(string) --* 
                  The identifier of the provisioning artifact.
                - **Name** *(string) --* 
                  The name of the provisioning artifact.
                - **Description** *(string) --* 
                  The description of the provisioning artifact.
                - **CreatedTime** *(datetime) --* 
                  The UTC time stamp of the creation time.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type Id: string
        :param Id: **[REQUIRED]**
          The product identifier.
        :rtype: dict
        :returns:
        """
        pass

    def describe_product_as_admin(self, Id: str, AcceptLanguage: str = None) -> Dict:
        """
        Gets information about the specified product. This operation is run with administrator access.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeProductAsAdmin>`_
        
        **Request Syntax**
        ::
          response = client.describe_product_as_admin(
              AcceptLanguage='string',
              Id='string'
          )
        
        **Response Syntax**
        ::
            {
                'ProductViewDetail': {
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
                'ProvisioningArtifactSummaries': [
                    {
                        'Id': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'CreatedTime': datetime(2015, 1, 1),
                        'ProvisioningArtifactMetadata': {
                            'string': 'string'
                        }
                    },
                ],
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'TagOptions': [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Active': True|False,
                        'Id': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProductViewDetail** *(dict) --* 
              Information about the product view.
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
            - **ProvisioningArtifactSummaries** *(list) --* 
              Information about the provisioning artifacts (also known as versions) for the specified product.
              - *(dict) --* 
                Summary information about a provisioning artifact (also known as a version) for a product.
                - **Id** *(string) --* 
                  The identifier of the provisioning artifact.
                - **Name** *(string) --* 
                  The name of the provisioning artifact.
                - **Description** *(string) --* 
                  The description of the provisioning artifact.
                - **CreatedTime** *(datetime) --* 
                  The UTC time stamp of the creation time.
                - **ProvisioningArtifactMetadata** *(dict) --* 
                  The metadata for the provisioning artifact. This is used with AWS Marketplace products.
                  - *(string) --* 
                    - *(string) --* 
            - **Tags** *(list) --* 
              Information about the tags associated with the product.
              - *(dict) --* 
                Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
                - **Key** *(string) --* 
                  The tag key.
                - **Value** *(string) --* 
                  The value for this key.
            - **TagOptions** *(list) --* 
              Information about the TagOptions associated with the product.
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
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type Id: string
        :param Id: **[REQUIRED]**
          The product identifier.
        :rtype: dict
        :returns:
        """
        pass

    def describe_product_view(self, Id: str, AcceptLanguage: str = None) -> Dict:
        """
        Gets information about the specified product.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeProductView>`_
        
        **Request Syntax**
        ::
          response = client.describe_product_view(
              AcceptLanguage='string',
              Id='string'
          )
        
        **Response Syntax**
        ::
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
                'ProvisioningArtifacts': [
                    {
                        'Id': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'CreatedTime': datetime(2015, 1, 1)
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProductViewSummary** *(dict) --* 
              Summary information about the product.
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
            - **ProvisioningArtifacts** *(list) --* 
              Information about the provisioning artifacts for the product.
              - *(dict) --* 
                Information about a provisioning artifact. A provisioning artifact is also known as a product version.
                - **Id** *(string) --* 
                  The identifier of the provisioning artifact.
                - **Name** *(string) --* 
                  The name of the provisioning artifact.
                - **Description** *(string) --* 
                  The description of the provisioning artifact.
                - **CreatedTime** *(datetime) --* 
                  The UTC time stamp of the creation time.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type Id: string
        :param Id: **[REQUIRED]**
          The product view identifier.
        :rtype: dict
        :returns:
        """
        pass

    def describe_provisioned_product(self, Id: str, AcceptLanguage: str = None) -> Dict:
        """
        Gets information about the specified provisioned product.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeProvisionedProduct>`_
        
        **Request Syntax**
        ::
          response = client.describe_provisioned_product(
              AcceptLanguage='string',
              Id='string'
          )
        
        **Response Syntax**
        ::
            {
                'ProvisionedProductDetail': {
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
                'CloudWatchDashboards': [
                    {
                        'Name': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProvisionedProductDetail** *(dict) --* 
              Information about the provisioned product.
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
            - **CloudWatchDashboards** *(list) --* 
              Any CloudWatch dashboards that were created when provisioning the product.
              - *(dict) --* 
                Information about a CloudWatch dashboard.
                - **Name** *(string) --* 
                  The name of the CloudWatch dashboard.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type Id: string
        :param Id: **[REQUIRED]**
          The provisioned product identifier.
        :rtype: dict
        :returns:
        """
        pass

    def describe_provisioned_product_plan(self, PlanId: str, AcceptLanguage: str = None, PageSize: int = None, PageToken: str = None) -> Dict:
        """
        Gets information about the resource changes for the specified plan.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeProvisionedProductPlan>`_
        
        **Request Syntax**
        ::
          response = client.describe_provisioned_product_plan(
              AcceptLanguage='string',
              PlanId='string',
              PageSize=123,
              PageToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'ProvisionedProductPlanDetails': {
                    'CreatedTime': datetime(2015, 1, 1),
                    'PathId': 'string',
                    'ProductId': 'string',
                    'PlanName': 'string',
                    'PlanId': 'string',
                    'ProvisionProductId': 'string',
                    'ProvisionProductName': 'string',
                    'PlanType': 'CLOUDFORMATION',
                    'ProvisioningArtifactId': 'string',
                    'Status': 'CREATE_IN_PROGRESS'|'CREATE_SUCCESS'|'CREATE_FAILED'|'EXECUTE_IN_PROGRESS'|'EXECUTE_SUCCESS'|'EXECUTE_FAILED',
                    'UpdatedTime': datetime(2015, 1, 1),
                    'NotificationArns': [
                        'string',
                    ],
                    'ProvisioningParameters': [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'UsePreviousValue': True|False
                        },
                    ],
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'StatusMessage': 'string'
                },
                'ResourceChanges': [
                    {
                        'Action': 'ADD'|'MODIFY'|'REMOVE',
                        'LogicalResourceId': 'string',
                        'PhysicalResourceId': 'string',
                        'ResourceType': 'string',
                        'Replacement': 'TRUE'|'FALSE'|'CONDITIONAL',
                        'Scope': [
                            'PROPERTIES'|'METADATA'|'CREATIONPOLICY'|'UPDATEPOLICY'|'DELETIONPOLICY'|'TAGS',
                        ],
                        'Details': [
                            {
                                'Target': {
                                    'Attribute': 'PROPERTIES'|'METADATA'|'CREATIONPOLICY'|'UPDATEPOLICY'|'DELETIONPOLICY'|'TAGS',
                                    'Name': 'string',
                                    'RequiresRecreation': 'NEVER'|'CONDITIONALLY'|'ALWAYS'
                                },
                                'Evaluation': 'STATIC'|'DYNAMIC',
                                'CausingEntity': 'string'
                            },
                        ]
                    },
                ],
                'NextPageToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProvisionedProductPlanDetails** *(dict) --* 
              Information about the plan.
              - **CreatedTime** *(datetime) --* 
                The UTC time stamp of the creation time.
              - **PathId** *(string) --* 
                The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use  ListLaunchPaths .
              - **ProductId** *(string) --* 
                The product identifier.
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
              - **Status** *(string) --* 
                The status.
              - **UpdatedTime** *(datetime) --* 
                The time when the plan was last updated.
              - **NotificationArns** *(list) --* 
                Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.
                - *(string) --* 
              - **ProvisioningParameters** *(list) --* 
                Parameters specified by the administrator that are required for provisioning the product.
                - *(dict) --* 
                  The parameter key-value pair used to update a provisioned product.
                  - **Key** *(string) --* 
                    The parameter key.
                  - **Value** *(string) --* 
                    The parameter value.
                  - **UsePreviousValue** *(boolean) --* 
                    If set to true, ``Value`` is ignored and the previous parameter value is kept.
              - **Tags** *(list) --* 
                One or more tags.
                - *(dict) --* 
                  Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
                  - **Key** *(string) --* 
                    The tag key.
                  - **Value** *(string) --* 
                    The value for this key.
              - **StatusMessage** *(string) --* 
                The status message.
            - **ResourceChanges** *(list) --* 
              Information about the resource changes that will occur when the plan is executed.
              - *(dict) --* 
                Information about a resource change that will occur when a plan is executed.
                - **Action** *(string) --* 
                  The change action.
                - **LogicalResourceId** *(string) --* 
                  The ID of the resource, as defined in the CloudFormation template.
                - **PhysicalResourceId** *(string) --* 
                  The ID of the resource, if it was already created.
                - **ResourceType** *(string) --* 
                  The type of resource.
                - **Replacement** *(string) --* 
                  If the change type is ``Modify`` , indicates whether the existing resource is deleted and replaced with a new one.
                - **Scope** *(list) --* 
                  The change scope.
                  - *(string) --* 
                - **Details** *(list) --* 
                  Information about the resource changes.
                  - *(dict) --* 
                    Information about a change to a resource attribute.
                    - **Target** *(dict) --* 
                      Information about the resource attribute to be modified.
                      - **Attribute** *(string) --* 
                        The attribute to be changed.
                      - **Name** *(string) --* 
                        If the attribute is ``Properties`` , the value is the name of the property. Otherwise, the value is null.
                      - **RequiresRecreation** *(string) --* 
                        If the attribute is ``Properties`` , indicates whether a change to this property causes the resource to be re-created.
                    - **Evaluation** *(string) --* 
                      For static evaluations, the value of the resource attribute will change and the new value is known. For dynamic evaluations, the value might change, and any new value will be determined when the plan is updated.
                    - **CausingEntity** *(string) --* 
                      The ID of the entity that caused the change.
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type PlanId: string
        :param PlanId: **[REQUIRED]**
          The plan identifier.
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :rtype: dict
        :returns:
        """
        pass

    def describe_provisioning_artifact(self, ProvisioningArtifactId: str, ProductId: str, AcceptLanguage: str = None, Verbose: bool = None) -> Dict:
        """
        Gets information about the specified provisioning artifact (also known as a version) for the specified product.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeProvisioningArtifact>`_
        
        **Request Syntax**
        ::
          response = client.describe_provisioning_artifact(
              AcceptLanguage='string',
              ProvisioningArtifactId='string',
              ProductId='string',
              Verbose=True|False
          )
        
        **Response Syntax**
        ::
            {
                'ProvisioningArtifactDetail': {
                    'Id': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
                    'CreatedTime': datetime(2015, 1, 1),
                    'Active': True|False
                },
                'Info': {
                    'string': 'string'
                },
                'Status': 'AVAILABLE'|'CREATING'|'FAILED'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProvisioningArtifactDetail** *(dict) --* 
              Information about the provisioning artifact.
              - **Id** *(string) --* 
                The identifier of the provisioning artifact.
              - **Name** *(string) --* 
                The name of the provisioning artifact.
              - **Description** *(string) --* 
                The description of the provisioning artifact.
              - **Type** *(string) --* 
                The type of provisioning artifact.
                * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template 
                * ``MARKETPLACE_AMI`` - AWS Marketplace AMI 
                * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources 
              - **CreatedTime** *(datetime) --* 
                The UTC time stamp of the creation time.
              - **Active** *(boolean) --* 
                Indicates whether the product version is active.
            - **Info** *(dict) --* 
              The URL of the CloudFormation template in Amazon S3.
              - *(string) --* 
                - *(string) --* 
            - **Status** *(string) --* 
              The status of the current request.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type ProvisioningArtifactId: string
        :param ProvisioningArtifactId: **[REQUIRED]**
          The identifier of the provisioning artifact.
        :type ProductId: string
        :param ProductId: **[REQUIRED]**
          The product identifier.
        :type Verbose: boolean
        :param Verbose:
          Indicates whether a verbose level of detail is enabled.
        :rtype: dict
        :returns:
        """
        pass

    def describe_provisioning_parameters(self, ProductId: str, ProvisioningArtifactId: str, AcceptLanguage: str = None, PathId: str = None) -> Dict:
        """
        Gets information about the configuration required to provision the specified product using the specified provisioning artifact.
        If the output contains a TagOption key with an empty list of values, there is a TagOption conflict for that key. The end user cannot take action to fix the conflict, and launch is not blocked. In subsequent calls to  ProvisionProduct , do not include conflicted TagOption keys as tags, or this causes the error "Parameter validation failed: Missing required parameter in Tags[*N* ]:*Value* ". Tag the provisioned product with the value ``sc-tagoption-conflict-portfolioId-productId`` .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeProvisioningParameters>`_
        
        **Request Syntax**
        ::
          response = client.describe_provisioning_parameters(
              AcceptLanguage='string',
              ProductId='string',
              ProvisioningArtifactId='string',
              PathId='string'
          )
        
        **Response Syntax**
        ::
            {
                'ProvisioningArtifactParameters': [
                    {
                        'ParameterKey': 'string',
                        'DefaultValue': 'string',
                        'ParameterType': 'string',
                        'IsNoEcho': True|False,
                        'Description': 'string',
                        'ParameterConstraints': {
                            'AllowedValues': [
                                'string',
                            ]
                        }
                    },
                ],
                'ConstraintSummaries': [
                    {
                        'Type': 'string',
                        'Description': 'string'
                    },
                ],
                'UsageInstructions': [
                    {
                        'Type': 'string',
                        'Value': 'string'
                    },
                ],
                'TagOptions': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'ProvisioningArtifactPreferences': {
                    'StackSetAccounts': [
                        'string',
                    ],
                    'StackSetRegions': [
                        'string',
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProvisioningArtifactParameters** *(list) --* 
              Information about the parameters used to provision the product.
              - *(dict) --* 
                Information about a parameter used to provision a product.
                - **ParameterKey** *(string) --* 
                  The parameter key.
                - **DefaultValue** *(string) --* 
                  The default value.
                - **ParameterType** *(string) --* 
                  The parameter type.
                - **IsNoEcho** *(boolean) --* 
                  If this value is true, the value for this parameter is obfuscated from view when the parameter is retrieved. This parameter is used to hide sensitive information.
                - **Description** *(string) --* 
                  The description of the parameter.
                - **ParameterConstraints** *(dict) --* 
                  Constraints that the administrator has put on a parameter.
                  - **AllowedValues** *(list) --* 
                    The values that the administrator has allowed for the parameter.
                    - *(string) --* 
            - **ConstraintSummaries** *(list) --* 
              Information about the constraints used to provision the product.
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
            - **UsageInstructions** *(list) --* 
              Any additional metadata specifically related to the provisioning of the product. For example, see the ``Version`` field of the CloudFormation template.
              - *(dict) --* 
                Additional information provided by the administrator.
                - **Type** *(string) --* 
                  The usage instruction type for the value.
                - **Value** *(string) --* 
                  The usage instruction value for this type.
            - **TagOptions** *(list) --* 
              Information about the TagOptions associated with the resource.
              - *(dict) --* 
                Summary information about a TagOption.
                - **Key** *(string) --* 
                  The TagOption key.
                - **Values** *(list) --* 
                  The TagOption value.
                  - *(string) --* 
            - **ProvisioningArtifactPreferences** *(dict) --* 
              An object that contains information about preferences, such as regions and accounts, for the provisioning artifact.
              - **StackSetAccounts** *(list) --* 
                One or more AWS accounts where stack instances are deployed from the stack set. These accounts can be scoped in ``ProvisioningPreferences$StackSetAccounts`` and ``UpdateProvisioningPreferences$StackSetAccounts`` .
                Applicable only to a ``CFN_STACKSET`` provisioned product type.
                - *(string) --* 
              - **StackSetRegions** *(list) --* 
                One or more AWS Regions where stack instances are deployed from the stack set. These regions can be scoped in ``ProvisioningPreferences$StackSetRegions`` and ``UpdateProvisioningPreferences$StackSetRegions`` .
                Applicable only to a ``CFN_STACKSET`` provisioned product type.
                - *(string) --* 
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type ProductId: string
        :param ProductId: **[REQUIRED]**
          The product identifier.
        :type ProvisioningArtifactId: string
        :param ProvisioningArtifactId: **[REQUIRED]**
          The identifier of the provisioning artifact.
        :type PathId: string
        :param PathId:
          The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use  ListLaunchPaths .
        :rtype: dict
        :returns:
        """
        pass

    def describe_record(self, Id: str, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None) -> Dict:
        """
        Gets information about the specified request operation.
        Use this operation after calling a request operation (for example,  ProvisionProduct ,  TerminateProvisionedProduct , or  UpdateProvisionedProduct ). 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeRecord>`_
        
        **Request Syntax**
        ::
          response = client.describe_record(
              AcceptLanguage='string',
              Id='string',
              PageToken='string',
              PageSize=123
          )
        
        **Response Syntax**
        ::
            {
                'RecordDetail': {
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
                'RecordOutputs': [
                    {
                        'OutputKey': 'string',
                        'OutputValue': 'string',
                        'Description': 'string'
                    },
                ],
                'NextPageToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RecordDetail** *(dict) --* 
              Information about the product.
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
            - **RecordOutputs** *(list) --* 
              Information about the product created as the result of a request. For example, the output for a CloudFormation-backed product that creates an S3 bucket would include the S3 bucket URL.
              - *(dict) --* 
                The output for the product created as the result of a request. For example, the output for a CloudFormation-backed product that creates an S3 bucket would include the S3 bucket URL.
                - **OutputKey** *(string) --* 
                  The output key.
                - **OutputValue** *(string) --* 
                  The output value.
                - **Description** *(string) --* 
                  The description of the output.
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type Id: string
        :param Id: **[REQUIRED]**
          The record identifier of the provisioned product. This identifier is returned by the request operation.
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :rtype: dict
        :returns:
        """
        pass

    def describe_service_action(self, Id: str, AcceptLanguage: str = None) -> Dict:
        """
        Describes a self-service action.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeServiceAction>`_
        
        **Request Syntax**
        ::
          response = client.describe_service_action(
              Id='string',
              AcceptLanguage='string'
          )
        
        **Response Syntax**
        ::
            {
                'ServiceActionDetail': {
                    'ServiceActionSummary': {
                        'Id': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'DefinitionType': 'SSM_AUTOMATION'
                    },
                    'Definition': {
                        'string': 'string'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ServiceActionDetail** *(dict) --* 
              Detailed information about the self-service action.
              - **ServiceActionSummary** *(dict) --* 
                Summary information about the self-service action.
                - **Id** *(string) --* 
                  The self-service action identifier.
                - **Name** *(string) --* 
                  The self-service action name.
                - **Description** *(string) --* 
                  The self-service action description.
                - **DefinitionType** *(string) --* 
                  The self-service action definition type. For example, ``SSM_AUTOMATION`` .
              - **Definition** *(dict) --* 
                A map that defines the self-service action.
                - *(string) --* 
                  - *(string) --* 
        :type Id: string
        :param Id: **[REQUIRED]**
          The self-service action identifier.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :rtype: dict
        :returns:
        """
        pass

    def describe_tag_option(self, Id: str) -> Dict:
        """
        Gets information about the specified TagOption.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeTagOption>`_
        
        **Request Syntax**
        ::
          response = client.describe_tag_option(
              Id='string'
          )
        
        **Response Syntax**
        ::
            {
                'TagOptionDetail': {
                    'Key': 'string',
                    'Value': 'string',
                    'Active': True|False,
                    'Id': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TagOptionDetail** *(dict) --* 
              Information about the TagOption.
              - **Key** *(string) --* 
                The TagOption key.
              - **Value** *(string) --* 
                The TagOption value.
              - **Active** *(boolean) --* 
                The TagOption active state.
              - **Id** *(string) --* 
                The TagOption identifier.
        :type Id: string
        :param Id: **[REQUIRED]**
          The TagOption identifier.
        :rtype: dict
        :returns:
        """
        pass

    def disable_aws_organizations_access(self) -> Dict:
        """
        Disable portfolio sharing through AWS Organizations feature. This feature will not delete your current shares but it will prevent you from creating new shares throughout your organization. Current shares will not be in sync with your organization structure if it changes after calling this API. This API can only be called by the master account in the organization.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess>`_
        
        **Request Syntax**
        ::
          response = client.disable_aws_organizations_access()
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :rtype: dict
        :returns:
        """
        pass

    def disassociate_principal_from_portfolio(self, PortfolioId: str, PrincipalARN: str, AcceptLanguage: str = None) -> Dict:
        """
        Disassociates a previously associated principal ARN from a specified portfolio.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio>`_
        
        **Request Syntax**
        ::
          response = client.disassociate_principal_from_portfolio(
              AcceptLanguage='string',
              PortfolioId='string',
              PrincipalARN='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type PortfolioId: string
        :param PortfolioId: **[REQUIRED]**
          The portfolio identifier.
        :type PrincipalARN: string
        :param PrincipalARN: **[REQUIRED]**
          The ARN of the principal (IAM user, role, or group).
        :rtype: dict
        :returns:
        """
        pass

    def disassociate_product_from_portfolio(self, ProductId: str, PortfolioId: str, AcceptLanguage: str = None) -> Dict:
        """
        Disassociates the specified product from the specified portfolio. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DisassociateProductFromPortfolio>`_
        
        **Request Syntax**
        ::
          response = client.disassociate_product_from_portfolio(
              AcceptLanguage='string',
              ProductId='string',
              PortfolioId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type ProductId: string
        :param ProductId: **[REQUIRED]**
          The product identifier.
        :type PortfolioId: string
        :param PortfolioId: **[REQUIRED]**
          The portfolio identifier.
        :rtype: dict
        :returns:
        """
        pass

    def disassociate_service_action_from_provisioning_artifact(self, ProductId: str, ProvisioningArtifactId: str, ServiceActionId: str, AcceptLanguage: str = None) -> Dict:
        """
        Disassociates the specified self-service action association from the specified provisioning artifact.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact>`_
        
        **Request Syntax**
        ::
          response = client.disassociate_service_action_from_provisioning_artifact(
              ProductId='string',
              ProvisioningArtifactId='string',
              ServiceActionId='string',
              AcceptLanguage='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ProductId: string
        :param ProductId: **[REQUIRED]**
          The product identifier. For example, ``prod-abcdzk7xy33qa`` .
        :type ProvisioningArtifactId: string
        :param ProvisioningArtifactId: **[REQUIRED]**
          The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .
        :type ServiceActionId: string
        :param ServiceActionId: **[REQUIRED]**
          The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :rtype: dict
        :returns:
        """
        pass

    def disassociate_tag_option_from_resource(self, ResourceId: str, TagOptionId: str) -> Dict:
        """
        Disassociates the specified TagOption from the specified resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DisassociateTagOptionFromResource>`_
        
        **Request Syntax**
        ::
          response = client.disassociate_tag_option_from_resource(
              ResourceId='string',
              TagOptionId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**
          The resource identifier.
        :type TagOptionId: string
        :param TagOptionId: **[REQUIRED]**
          The TagOption identifier.
        :rtype: dict
        :returns:
        """
        pass

    def enable_aws_organizations_access(self) -> Dict:
        """
        Enable portfolio sharing feature through AWS Organizations. This API will allow Service Catalog to receive updates on your organization in order to sync your shares with the current structure. This API can only be called by the master account in the organization.
        By calling this API Service Catalog will make a call to organizations:EnableAWSServiceAccess on your behalf so that your shares can be in sync with any changes in your AWS Organizations structure.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess>`_
        
        **Request Syntax**
        ::
          response = client.enable_aws_organizations_access()
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :rtype: dict
        :returns:
        """
        pass

    def execute_provisioned_product_plan(self, PlanId: str, IdempotencyToken: str, AcceptLanguage: str = None) -> Dict:
        """
        Provisions or modifies a product based on the resource changes for the specified plan.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ExecuteProvisionedProductPlan>`_
        
        **Request Syntax**
        ::
          response = client.execute_provisioned_product_plan(
              AcceptLanguage='string',
              PlanId='string',
              IdempotencyToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'RecordDetail': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RecordDetail** *(dict) --* 
              Information about the result of provisioning the product.
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
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type PlanId: string
        :param PlanId: **[REQUIRED]**
          The plan identifier.
        :type IdempotencyToken: string
        :param IdempotencyToken: **[REQUIRED]**
          A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
          This field is autopopulated if not provided.
        :rtype: dict
        :returns:
        """
        pass

    def execute_provisioned_product_service_action(self, ProvisionedProductId: str, ServiceActionId: str, ExecuteToken: str, AcceptLanguage: str = None) -> Dict:
        """
        Executes a self-service action against a provisioned product.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ExecuteProvisionedProductServiceAction>`_
        
        **Request Syntax**
        ::
          response = client.execute_provisioned_product_service_action(
              ProvisionedProductId='string',
              ServiceActionId='string',
              ExecuteToken='string',
              AcceptLanguage='string'
          )
        
        **Response Syntax**
        ::
            {
                'RecordDetail': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RecordDetail** *(dict) --* 
              An object containing detailed information about the result of provisioning the product.
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
        :type ProvisionedProductId: string
        :param ProvisionedProductId: **[REQUIRED]**
          The identifier of the provisioned product.
        :type ServiceActionId: string
        :param ServiceActionId: **[REQUIRED]**
          The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .
        :type ExecuteToken: string
        :param ExecuteToken: **[REQUIRED]**
          An idempotency token that uniquely identifies the execute request.
          This field is autopopulated if not provided.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
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

    def get_aws_organizations_access_status(self) -> Dict:
        """
        Get the Access Status for AWS Organization portfolio share feature. This API can only be called by the master account in the organization.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus>`_
        
        **Request Syntax**
        ::
          response = client.get_aws_organizations_access_status()
        
        **Response Syntax**
        ::
            {
                'AccessStatus': 'ENABLED'|'UNDER_CHANGE'|'DISABLED'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AccessStatus** *(string) --* 
              The status of the portfolio share feature.
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

    def list_accepted_portfolio_shares(self, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None, PortfolioShareType: str = None) -> Dict:
        """
        Lists all portfolios for which sharing was accepted by this account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListAcceptedPortfolioShares>`_
        
        **Request Syntax**
        ::
          response = client.list_accepted_portfolio_shares(
              AcceptLanguage='string',
              PageToken='string',
              PageSize=123,
              PortfolioShareType='IMPORTED'|'AWS_SERVICECATALOG'|'AWS_ORGANIZATIONS'
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
                'NextPageToken': 'string'
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
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :type PortfolioShareType: string
        :param PortfolioShareType:
          The type of shared portfolios to list. The default is to list imported portfolios.
          * ``AWS_ORGANIZATIONS`` - List portfolios shared by the master account of your organization
          * ``AWS_SERVICECATALOG`` - List default portfolios
          * ``IMPORTED`` - List imported portfolios
        :rtype: dict
        :returns:
        """
        pass

    def list_constraints_for_portfolio(self, PortfolioId: str, AcceptLanguage: str = None, ProductId: str = None, PageSize: int = None, PageToken: str = None) -> Dict:
        """
        Lists the constraints for the specified portfolio and product.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListConstraintsForPortfolio>`_
        
        **Request Syntax**
        ::
          response = client.list_constraints_for_portfolio(
              AcceptLanguage='string',
              PortfolioId='string',
              ProductId='string',
              PageSize=123,
              PageToken='string'
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
                'NextPageToken': 'string'
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
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
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
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :rtype: dict
        :returns:
        """
        pass

    def list_launch_paths(self, ProductId: str, AcceptLanguage: str = None, PageSize: int = None, PageToken: str = None) -> Dict:
        """
        Lists the paths to the specified product. A path is how the user has access to a specified product, and is necessary when provisioning a product. A path also determines the constraints put on the product.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListLaunchPaths>`_
        
        **Request Syntax**
        ::
          response = client.list_launch_paths(
              AcceptLanguage='string',
              ProductId='string',
              PageSize=123,
              PageToken='string'
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
                'NextPageToken': 'string'
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
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type ProductId: string
        :param ProductId: **[REQUIRED]**
          The product identifier.
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :rtype: dict
        :returns:
        """
        pass

    def list_organization_portfolio_access(self, PortfolioId: str, OrganizationNodeType: str, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None) -> Dict:
        """
        Lists the organization nodes that have access to the specified portfolio. This API can only be called by the master account in the organization.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess>`_
        
        **Request Syntax**
        ::
          response = client.list_organization_portfolio_access(
              AcceptLanguage='string',
              PortfolioId='string',
              OrganizationNodeType='ORGANIZATION'|'ORGANIZATIONAL_UNIT'|'ACCOUNT',
              PageToken='string',
              PageSize=123
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
                'NextPageToken': 'string'
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
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
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
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :rtype: dict
        :returns:
        """
        pass

    def list_portfolio_access(self, PortfolioId: str, AcceptLanguage: str = None) -> Dict:
        """
        Lists the account IDs that have access to the specified portfolio.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListPortfolioAccess>`_
        
        **Request Syntax**
        ::
          response = client.list_portfolio_access(
              AcceptLanguage='string',
              PortfolioId='string'
          )
        
        **Response Syntax**
        ::
            {
                'AccountIds': [
                    'string',
                ],
                'NextPageToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AccountIds** *(list) --* 
              Information about the AWS accounts with access to the portfolio.
              - *(string) --* 
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type PortfolioId: string
        :param PortfolioId: **[REQUIRED]**
          The portfolio identifier.
        :rtype: dict
        :returns:
        """
        pass

    def list_portfolios(self, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None) -> Dict:
        """
        Lists all portfolios in the catalog.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListPortfolios>`_
        
        **Request Syntax**
        ::
          response = client.list_portfolios(
              AcceptLanguage='string',
              PageToken='string',
              PageSize=123
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
                'NextPageToken': 'string'
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
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :rtype: dict
        :returns:
        """
        pass

    def list_portfolios_for_product(self, ProductId: str, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None) -> Dict:
        """
        Lists all portfolios that the specified product is associated with.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListPortfoliosForProduct>`_
        
        **Request Syntax**
        ::
          response = client.list_portfolios_for_product(
              AcceptLanguage='string',
              ProductId='string',
              PageToken='string',
              PageSize=123
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
                'NextPageToken': 'string'
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
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type ProductId: string
        :param ProductId: **[REQUIRED]**
          The product identifier.
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :rtype: dict
        :returns:
        """
        pass

    def list_principals_for_portfolio(self, PortfolioId: str, AcceptLanguage: str = None, PageSize: int = None, PageToken: str = None) -> Dict:
        """
        Lists all principal ARNs associated with the specified portfolio.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListPrincipalsForPortfolio>`_
        
        **Request Syntax**
        ::
          response = client.list_principals_for_portfolio(
              AcceptLanguage='string',
              PortfolioId='string',
              PageSize=123,
              PageToken='string'
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
                'NextPageToken': 'string'
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
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type PortfolioId: string
        :param PortfolioId: **[REQUIRED]**
          The portfolio identifier.
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :rtype: dict
        :returns:
        """
        pass

    def list_provisioned_product_plans(self, AcceptLanguage: str = None, ProvisionProductId: str = None, PageSize: int = None, PageToken: str = None, AccessLevelFilter: Dict = None) -> Dict:
        """
        Lists the plans for the specified provisioned product or all plans to which the user has access.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListProvisionedProductPlans>`_
        
        **Request Syntax**
        ::
          response = client.list_provisioned_product_plans(
              AcceptLanguage='string',
              ProvisionProductId='string',
              PageSize=123,
              PageToken='string',
              AccessLevelFilter={
                  'Key': 'Account'|'Role'|'User',
                  'Value': 'string'
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
                'NextPageToken': 'string'
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
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type ProvisionProductId: string
        :param ProvisionProductId:
          The product identifier.
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
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
        :rtype: dict
        :returns:
        """
        pass

    def list_provisioning_artifacts(self, ProductId: str, AcceptLanguage: str = None) -> Dict:
        """
        Lists all provisioning artifacts (also known as versions) for the specified product.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListProvisioningArtifacts>`_
        
        **Request Syntax**
        ::
          response = client.list_provisioning_artifacts(
              AcceptLanguage='string',
              ProductId='string'
          )
        
        **Response Syntax**
        ::
            {
                'ProvisioningArtifactDetails': [
                    {
                        'Id': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
                        'CreatedTime': datetime(2015, 1, 1),
                        'Active': True|False
                    },
                ],
                'NextPageToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProvisioningArtifactDetails** *(list) --* 
              Information about the provisioning artifacts.
              - *(dict) --* 
                Information about a provisioning artifact (also known as a version) for a product.
                - **Id** *(string) --* 
                  The identifier of the provisioning artifact.
                - **Name** *(string) --* 
                  The name of the provisioning artifact.
                - **Description** *(string) --* 
                  The description of the provisioning artifact.
                - **Type** *(string) --* 
                  The type of provisioning artifact.
                  * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template 
                  * ``MARKETPLACE_AMI`` - AWS Marketplace AMI 
                  * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources 
                - **CreatedTime** *(datetime) --* 
                  The UTC time stamp of the creation time.
                - **Active** *(boolean) --* 
                  Indicates whether the product version is active.
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type ProductId: string
        :param ProductId: **[REQUIRED]**
          The product identifier.
        :rtype: dict
        :returns:
        """
        pass

    def list_provisioning_artifacts_for_service_action(self, ServiceActionId: str, PageSize: int = None, PageToken: str = None, AcceptLanguage: str = None) -> Dict:
        """
        Lists all provisioning artifacts (also known as versions) for the specified self-service action.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction>`_
        
        **Request Syntax**
        ::
          response = client.list_provisioning_artifacts_for_service_action(
              ServiceActionId='string',
              PageSize=123,
              PageToken='string',
              AcceptLanguage='string'
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
                'NextPageToken': 'string'
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
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
        :type ServiceActionId: string
        :param ServiceActionId: **[REQUIRED]**
          The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :rtype: dict
        :returns:
        """
        pass

    def list_record_history(self, AcceptLanguage: str = None, AccessLevelFilter: Dict = None, SearchFilter: Dict = None, PageSize: int = None, PageToken: str = None) -> Dict:
        """
        Lists the specified requests or all performed requests.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListRecordHistory>`_
        
        **Request Syntax**
        ::
          response = client.list_record_history(
              AcceptLanguage='string',
              AccessLevelFilter={
                  'Key': 'Account'|'Role'|'User',
                  'Value': 'string'
              },
              SearchFilter={
                  'Key': 'string',
                  'Value': 'string'
              },
              PageSize=123,
              PageToken='string'
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
                'NextPageToken': 'string'
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
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
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
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :rtype: dict
        :returns:
        """
        pass

    def list_resources_for_tag_option(self, TagOptionId: str, ResourceType: str = None, PageSize: int = None, PageToken: str = None) -> Dict:
        """
        Lists the resources associated with the specified TagOption.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListResourcesForTagOption>`_
        
        **Request Syntax**
        ::
          response = client.list_resources_for_tag_option(
              TagOptionId='string',
              ResourceType='string',
              PageSize=123,
              PageToken='string'
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
                'PageToken': 'string'
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
            - **PageToken** *(string) --* 
              The page token for the next set of results. To retrieve the first set of results, use null.
        :type TagOptionId: string
        :param TagOptionId: **[REQUIRED]**
          The TagOption identifier.
        :type ResourceType: string
        :param ResourceType:
          The resource type.
          * ``Portfolio``
          * ``Product``
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :rtype: dict
        :returns:
        """
        pass

    def list_service_actions(self, AcceptLanguage: str = None, PageSize: int = None, PageToken: str = None) -> Dict:
        """
        Lists all self-service actions.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListServiceActions>`_
        
        **Request Syntax**
        ::
          response = client.list_service_actions(
              AcceptLanguage='string',
              PageSize=123,
              PageToken='string'
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
                'NextPageToken': 'string'
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
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :rtype: dict
        :returns:
        """
        pass

    def list_service_actions_for_provisioning_artifact(self, ProductId: str, ProvisioningArtifactId: str, PageSize: int = None, PageToken: str = None, AcceptLanguage: str = None) -> Dict:
        """
        Returns a paginated list of self-service actions associated with the specified Product ID and Provisioning Artifact ID.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListServiceActionsForProvisioningArtifact>`_
        
        **Request Syntax**
        ::
          response = client.list_service_actions_for_provisioning_artifact(
              ProductId='string',
              ProvisioningArtifactId='string',
              PageSize=123,
              PageToken='string',
              AcceptLanguage='string'
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
                'NextPageToken': 'string'
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
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
        :type ProductId: string
        :param ProductId: **[REQUIRED]**
          The product identifier. For example, ``prod-abcdzk7xy33qa`` .
        :type ProvisioningArtifactId: string
        :param ProvisioningArtifactId: **[REQUIRED]**
          The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :rtype: dict
        :returns:
        """
        pass

    def list_tag_options(self, Filters: Dict = None, PageSize: int = None, PageToken: str = None) -> Dict:
        """
        Lists the specified TagOptions or all TagOptions.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListTagOptions>`_
        
        **Request Syntax**
        ::
          response = client.list_tag_options(
              Filters={
                  'Key': 'string',
                  'Value': 'string',
                  'Active': True|False
              },
              PageSize=123,
              PageToken='string'
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
                'PageToken': 'string'
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
            - **PageToken** *(string) --* 
              The page token for the next set of results. To retrieve the first set of results, use null.
        :type Filters: dict
        :param Filters:
          The search filters. If no search filters are specified, the output includes all TagOptions.
          - **Key** *(string) --*
            The TagOption key.
          - **Value** *(string) --*
            The TagOption value.
          - **Active** *(boolean) --*
            The active state.
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :rtype: dict
        :returns:
        """
        pass

    def provision_product(self, ProductId: str, ProvisioningArtifactId: str, ProvisionedProductName: str, ProvisionToken: str, AcceptLanguage: str = None, PathId: str = None, ProvisioningParameters: List = None, ProvisioningPreferences: Dict = None, Tags: List = None, NotificationArns: List = None) -> Dict:
        """
        Provisions the specified product.
        A provisioned product is a resourced instance of a product. For example, provisioning a product based on a CloudFormation template launches a CloudFormation stack and its underlying resources. You can check the status of this request using  DescribeRecord .
        If the request contains a tag key with an empty list of values, there is a tag conflict for that key. Do not include conflicted keys as tags, or this causes the error "Parameter validation failed: Missing required parameter in Tags[*N* ]:*Value* ".
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ProvisionProduct>`_
        
        **Request Syntax**
        ::
          response = client.provision_product(
              AcceptLanguage='string',
              ProductId='string',
              ProvisioningArtifactId='string',
              PathId='string',
              ProvisionedProductName='string',
              ProvisioningParameters=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              ProvisioningPreferences={
                  'StackSetAccounts': [
                      'string',
                  ],
                  'StackSetRegions': [
                      'string',
                  ],
                  'StackSetFailureToleranceCount': 123,
                  'StackSetFailureTolerancePercentage': 123,
                  'StackSetMaxConcurrencyCount': 123,
                  'StackSetMaxConcurrencyPercentage': 123
              },
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              NotificationArns=[
                  'string',
              ],
              ProvisionToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'RecordDetail': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RecordDetail** *(dict) --* 
              Information about the result of provisioning the product.
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
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type ProductId: string
        :param ProductId: **[REQUIRED]**
          The product identifier.
        :type ProvisioningArtifactId: string
        :param ProvisioningArtifactId: **[REQUIRED]**
          The identifier of the provisioning artifact.
        :type PathId: string
        :param PathId:
          The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use  ListLaunchPaths .
        :type ProvisionedProductName: string
        :param ProvisionedProductName: **[REQUIRED]**
          A user-friendly name for the provisioned product. This value must be unique for the AWS account and cannot be updated after the product is provisioned.
        :type ProvisioningParameters: list
        :param ProvisioningParameters:
          Parameters specified by the administrator that are required for provisioning the product.
          - *(dict) --*
            Information about a parameter used to provision a product.
            - **Key** *(string) --*
              The parameter key.
            - **Value** *(string) --*
              The parameter value.
        :type ProvisioningPreferences: dict
        :param ProvisioningPreferences:
          An object that contains information about the provisioning preferences for a stack set.
          - **StackSetAccounts** *(list) --*
            One or more AWS accounts that will have access to the provisioned product.
            Applicable only to a ``CFN_STACKSET`` provisioned product type.
            The AWS accounts specified should be within the list of accounts in the ``STACKSET`` constraint. To get the list of accounts in the ``STACKSET`` constraint, use the ``DescribeProvisioningParameters`` operation.
            If no values are specified, the default value is all accounts from the ``STACKSET`` constraint.
            - *(string) --*
          - **StackSetRegions** *(list) --*
            One or more AWS Regions where the provisioned product will be available.
            Applicable only to a ``CFN_STACKSET`` provisioned product type.
            The specified regions should be within the list of regions from the ``STACKSET`` constraint. To get the list of regions in the ``STACKSET`` constraint, use the ``DescribeProvisioningParameters`` operation.
            If no values are specified, the default value is all regions from the ``STACKSET`` constraint.
            - *(string) --*
          - **StackSetFailureToleranceCount** *(integer) --*
            The number of accounts, per region, for which this operation can fail before AWS Service Catalog stops the operation in that region. If the operation is stopped in a region, AWS Service Catalog doesn\'t attempt the operation in any subsequent regions.
            Applicable only to a ``CFN_STACKSET`` provisioned product type.
            Conditional: You must specify either ``StackSetFailureToleranceCount`` or ``StackSetFailureTolerancePercentage`` , but not both.
            The default value is ``0`` if no value is specified.
          - **StackSetFailureTolerancePercentage** *(integer) --*
            The percentage of accounts, per region, for which this stack operation can fail before AWS Service Catalog stops the operation in that region. If the operation is stopped in a region, AWS Service Catalog doesn\'t attempt the operation in any subsequent regions.
            When calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number.
            Applicable only to a ``CFN_STACKSET`` provisioned product type.
            Conditional: You must specify either ``StackSetFailureToleranceCount`` or ``StackSetFailureTolerancePercentage`` , but not both.
          - **StackSetMaxConcurrencyCount** *(integer) --*
            The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of ``StackSetFailureToleranceCount`` . ``StackSetMaxConcurrentCount`` is at most one more than the ``StackSetFailureToleranceCount`` .
            Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
            Applicable only to a ``CFN_STACKSET`` provisioned product type.
            Conditional: You must specify either ``StackSetMaxConcurrentCount`` or ``StackSetMaxConcurrentPercentage`` , but not both.
          - **StackSetMaxConcurrencyPercentage** *(integer) --*
            The maximum percentage of accounts in which to perform this operation at one time.
            When calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, AWS Service Catalog sets the number as ``1`` instead.
            Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
            Applicable only to a ``CFN_STACKSET`` provisioned product type.
            Conditional: You must specify either ``StackSetMaxConcurrentCount`` or ``StackSetMaxConcurrentPercentage`` , but not both.
        :type Tags: list
        :param Tags:
          One or more tags.
          - *(dict) --*
            Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
            - **Key** *(string) --* **[REQUIRED]**
              The tag key.
            - **Value** *(string) --* **[REQUIRED]**
              The value for this key.
        :type NotificationArns: list
        :param NotificationArns:
          Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.
          - *(string) --*
        :type ProvisionToken: string
        :param ProvisionToken: **[REQUIRED]**
          An idempotency token that uniquely identifies the provisioning request.
          This field is autopopulated if not provided.
        :rtype: dict
        :returns:
        """
        pass

    def reject_portfolio_share(self, PortfolioId: str, AcceptLanguage: str = None, PortfolioShareType: str = None) -> Dict:
        """
        Rejects an offer to share the specified portfolio.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/RejectPortfolioShare>`_
        
        **Request Syntax**
        ::
          response = client.reject_portfolio_share(
              AcceptLanguage='string',
              PortfolioId='string',
              PortfolioShareType='IMPORTED'|'AWS_SERVICECATALOG'|'AWS_ORGANIZATIONS'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type PortfolioId: string
        :param PortfolioId: **[REQUIRED]**
          The portfolio identifier.
        :type PortfolioShareType: string
        :param PortfolioShareType:
          The type of shared portfolios to reject. The default is to reject imported portfolios.
          * ``AWS_ORGANIZATIONS`` - Reject portfolios shared by the master account of your organization.
          * ``IMPORTED`` - Reject imported portfolios.
          * ``AWS_SERVICECATALOG`` - Not supported. (Throws ResourceNotFoundException.)
          For example, ``aws servicecatalog reject-portfolio-share --portfolio-id \"port-2qwzkwxt3y5fk\" --portfolio-share-type AWS_ORGANIZATIONS``
        :rtype: dict
        :returns:
        """
        pass

    def scan_provisioned_products(self, AcceptLanguage: str = None, AccessLevelFilter: Dict = None, PageSize: int = None, PageToken: str = None) -> Dict:
        """
        Lists the provisioned products that are available (not terminated).
        To use additional filtering, see  SearchProvisionedProducts .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ScanProvisionedProducts>`_
        
        **Request Syntax**
        ::
          response = client.scan_provisioned_products(
              AcceptLanguage='string',
              AccessLevelFilter={
                  'Key': 'Account'|'Role'|'User',
                  'Value': 'string'
              },
              PageSize=123,
              PageToken='string'
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
                'NextPageToken': 'string'
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
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
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
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :rtype: dict
        :returns:
        """
        pass

    def search_products(self, AcceptLanguage: str = None, Filters: Dict = None, PageSize: int = None, SortBy: str = None, SortOrder: str = None, PageToken: str = None) -> Dict:
        """
        Gets information about the products to which the caller has access.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/SearchProducts>`_
        
        **Request Syntax**
        ::
          response = client.search_products(
              AcceptLanguage='string',
              Filters={
                  'string': [
                      'string',
                  ]
              },
              PageSize=123,
              SortBy='Title'|'VersionCount'|'CreationDate',
              SortOrder='ASCENDING'|'DESCENDING',
              PageToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'ProductViewSummaries': [
                    {
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
                ],
                'ProductViewAggregations': {
                    'string': [
                        {
                            'Value': 'string',
                            'ApproximateCount': 123
                        },
                    ]
                },
                'NextPageToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProductViewSummaries** *(list) --* 
              Information about the product views.
              - *(dict) --* 
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
            - **ProductViewAggregations** *(dict) --* 
              The product view aggregations.
              - *(string) --* 
                - *(list) --* 
                  - *(dict) --* 
                    A single product view aggregation value/count pair, containing metadata about each product to which the calling user has access.
                    - **Value** *(string) --* 
                      The value of the product view aggregation.
                    - **ApproximateCount** *(integer) --* 
                      An approximate count of the products that match the value.
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type Filters: dict
        :param Filters:
          The search filters. If no search filters are specified, the output includes all products to which the caller has access.
          - *(string) --*
            - *(list) --*
              - *(string) --*
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :type SortBy: string
        :param SortBy:
          The sort field. If no value is specified, the results are not sorted.
        :type SortOrder: string
        :param SortOrder:
          The sort order. If no value is specified, the results are not sorted.
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :rtype: dict
        :returns:
        """
        pass

    def search_products_as_admin(self, AcceptLanguage: str = None, PortfolioId: str = None, Filters: Dict = None, SortBy: str = None, SortOrder: str = None, PageToken: str = None, PageSize: int = None, ProductSource: str = None) -> Dict:
        """
        Gets information about the products for the specified portfolio or all products.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/SearchProductsAsAdmin>`_
        
        **Request Syntax**
        ::
          response = client.search_products_as_admin(
              AcceptLanguage='string',
              PortfolioId='string',
              Filters={
                  'string': [
                      'string',
                  ]
              },
              SortBy='Title'|'VersionCount'|'CreationDate',
              SortOrder='ASCENDING'|'DESCENDING',
              PageToken='string',
              PageSize=123,
              ProductSource='ACCOUNT'
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
                'NextPageToken': 'string'
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
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
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
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :type ProductSource: string
        :param ProductSource:
          Access level of the source of the product.
        :rtype: dict
        :returns:
        """
        pass

    def search_provisioned_products(self, AcceptLanguage: str = None, AccessLevelFilter: Dict = None, Filters: Dict = None, SortBy: str = None, SortOrder: str = None, PageSize: int = None, PageToken: str = None) -> Dict:
        """
        Gets information about the provisioned products that meet the specified criteria.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/SearchProvisionedProducts>`_
        
        **Request Syntax**
        ::
          response = client.search_provisioned_products(
              AcceptLanguage='string',
              AccessLevelFilter={
                  'Key': 'Account'|'Role'|'User',
                  'Value': 'string'
              },
              Filters={
                  'string': [
                      'string',
                  ]
              },
              SortBy='string',
              SortOrder='ASCENDING'|'DESCENDING',
              PageSize=123,
              PageToken='string'
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
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'PhysicalId': 'string',
                        'ProductId': 'string',
                        'ProvisioningArtifactId': 'string',
                        'UserArn': 'string',
                        'UserArnSession': 'string'
                    },
                ],
                'TotalResultsCount': 123,
                'NextPageToken': 'string'
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
                - **Tags** *(list) --* 
                  One or more tags.
                  - *(dict) --* 
                    Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
                    - **Key** *(string) --* 
                      The tag key.
                    - **Value** *(string) --* 
                      The value for this key.
                - **PhysicalId** *(string) --* 
                  The assigned identifier for the resource, such as an EC2 instance ID or an S3 bucket name.
                - **ProductId** *(string) --* 
                  The product identifier.
                - **ProvisioningArtifactId** *(string) --* 
                  The identifier of the provisioning artifact.
                - **UserArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the IAM user.
                - **UserArnSession** *(string) --* 
                  The ARN of the IAM user in the session. This ARN might contain a session ID.
            - **TotalResultsCount** *(integer) --* 
              The number of provisioned products found.
            - **NextPageToken** *(string) --* 
              The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
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
        :type Filters: dict
        :param Filters:
          The search filters.
          When the key is ``SearchQuery`` , the searchable fields are ``arn`` , ``createdTime`` , ``id`` , ``lastRecordId`` , ``idempotencyToken`` , ``name`` , ``physicalId`` , ``productId`` , ``provisioningArtifact`` , ``type`` , ``status`` , ``tags`` , ``userArn`` , and ``userArnSession`` .
          Example: ``\"SearchQuery\":[\"status:AVAILABLE\"]``
          - *(string) --*
            - *(list) --*
              - *(string) --*
        :type SortBy: string
        :param SortBy:
          The sort field. If no value is specified, the results are not sorted. The valid values are ``arn`` , ``id`` , ``name`` , and ``lastRecordId`` .
        :type SortOrder: string
        :param SortOrder:
          The sort order. If no value is specified, the results are not sorted.
        :type PageSize: integer
        :param PageSize:
          The maximum number of items to return with this call.
        :type PageToken: string
        :param PageToken:
          The page token for the next set of results. To retrieve the first set of results, use null.
        :rtype: dict
        :returns:
        """
        pass

    def terminate_provisioned_product(self, TerminateToken: str, ProvisionedProductName: str = None, ProvisionedProductId: str = None, IgnoreErrors: bool = None, AcceptLanguage: str = None) -> Dict:
        """
        Terminates the specified provisioned product.
        This operation does not delete any records associated with the provisioned product.
        You can check the status of this request using  DescribeRecord .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/TerminateProvisionedProduct>`_
        
        **Request Syntax**
        ::
          response = client.terminate_provisioned_product(
              ProvisionedProductName='string',
              ProvisionedProductId='string',
              TerminateToken='string',
              IgnoreErrors=True|False,
              AcceptLanguage='string'
          )
        
        **Response Syntax**
        ::
            {
                'RecordDetail': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RecordDetail** *(dict) --* 
              Information about the result of this request.
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
        :type ProvisionedProductName: string
        :param ProvisionedProductName:
          The name of the provisioned product. You cannot specify both ``ProvisionedProductName`` and ``ProvisionedProductId`` .
        :type ProvisionedProductId: string
        :param ProvisionedProductId:
          The identifier of the provisioned product. You cannot specify both ``ProvisionedProductName`` and ``ProvisionedProductId`` .
        :type TerminateToken: string
        :param TerminateToken: **[REQUIRED]**
          An idempotency token that uniquely identifies the termination request. This token is only valid during the termination process. After the provisioned product is terminated, subsequent requests to terminate the same provisioned product always return **ResourceNotFound** .
          This field is autopopulated if not provided.
        :type IgnoreErrors: boolean
        :param IgnoreErrors:
          If set to true, AWS Service Catalog stops managing the specified provisioned product even if it cannot delete the underlying resources.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :rtype: dict
        :returns:
        """
        pass

    def update_constraint(self, Id: str, AcceptLanguage: str = None, Description: str = None) -> Dict:
        """
        Updates the specified constraint.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/UpdateConstraint>`_
        
        **Request Syntax**
        ::
          response = client.update_constraint(
              AcceptLanguage='string',
              Id='string',
              Description='string'
          )
        
        **Response Syntax**
        ::
            {
                'ConstraintDetail': {
                    'ConstraintId': 'string',
                    'Type': 'string',
                    'Description': 'string',
                    'Owner': 'string'
                },
                'ConstraintParameters': 'string',
                'Status': 'AVAILABLE'|'CREATING'|'FAILED'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ConstraintDetail** *(dict) --* 
              Information about the constraint.
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
            - **ConstraintParameters** *(string) --* 
              The constraint parameters.
            - **Status** *(string) --* 
              The status of the current request.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type Id: string
        :param Id: **[REQUIRED]**
          The identifier of the constraint.
        :type Description: string
        :param Description:
          The updated description of the constraint.
        :rtype: dict
        :returns:
        """
        pass

    def update_portfolio(self, Id: str, AcceptLanguage: str = None, DisplayName: str = None, Description: str = None, ProviderName: str = None, AddTags: List = None, RemoveTags: List = None) -> Dict:
        """
        Updates the specified portfolio.
        You cannot update a product that was shared with you.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/UpdatePortfolio>`_
        
        **Request Syntax**
        ::
          response = client.update_portfolio(
              AcceptLanguage='string',
              Id='string',
              DisplayName='string',
              Description='string',
              ProviderName='string',
              AddTags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              RemoveTags=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'PortfolioDetail': {
                    'Id': 'string',
                    'ARN': 'string',
                    'DisplayName': 'string',
                    'Description': 'string',
                    'CreatedTime': datetime(2015, 1, 1),
                    'ProviderName': 'string'
                },
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PortfolioDetail** *(dict) --* 
              Information about the portfolio.
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
            - **Tags** *(list) --* 
              Information about the tags associated with the portfolio.
              - *(dict) --* 
                Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
                - **Key** *(string) --* 
                  The tag key.
                - **Value** *(string) --* 
                  The value for this key.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type Id: string
        :param Id: **[REQUIRED]**
          The portfolio identifier.
        :type DisplayName: string
        :param DisplayName:
          The name to use for display purposes.
        :type Description: string
        :param Description:
          The updated description of the portfolio.
        :type ProviderName: string
        :param ProviderName:
          The updated name of the portfolio provider.
        :type AddTags: list
        :param AddTags:
          The tags to add.
          - *(dict) --*
            Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
            - **Key** *(string) --* **[REQUIRED]**
              The tag key.
            - **Value** *(string) --* **[REQUIRED]**
              The value for this key.
        :type RemoveTags: list
        :param RemoveTags:
          The tags to remove.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def update_product(self, Id: str, AcceptLanguage: str = None, Name: str = None, Owner: str = None, Description: str = None, Distributor: str = None, SupportDescription: str = None, SupportEmail: str = None, SupportUrl: str = None, AddTags: List = None, RemoveTags: List = None) -> Dict:
        """
        Updates the specified product.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/UpdateProduct>`_
        
        **Request Syntax**
        ::
          response = client.update_product(
              AcceptLanguage='string',
              Id='string',
              Name='string',
              Owner='string',
              Description='string',
              Distributor='string',
              SupportDescription='string',
              SupportEmail='string',
              SupportUrl='string',
              AddTags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              RemoveTags=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'ProductViewDetail': {
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
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProductViewDetail** *(dict) --* 
              Information about the product view.
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
            - **Tags** *(list) --* 
              Information about the tags associated with the product.
              - *(dict) --* 
                Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
                - **Key** *(string) --* 
                  The tag key.
                - **Value** *(string) --* 
                  The value for this key.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type Id: string
        :param Id: **[REQUIRED]**
          The product identifier.
        :type Name: string
        :param Name:
          The updated product name.
        :type Owner: string
        :param Owner:
          The updated owner of the product.
        :type Description: string
        :param Description:
          The updated description of the product.
        :type Distributor: string
        :param Distributor:
          The updated distributor of the product.
        :type SupportDescription: string
        :param SupportDescription:
          The updated support description for the product.
        :type SupportEmail: string
        :param SupportEmail:
          The updated support email for the product.
        :type SupportUrl: string
        :param SupportUrl:
          The updated support URL for the product.
        :type AddTags: list
        :param AddTags:
          The tags to add to the product.
          - *(dict) --*
            Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.
            - **Key** *(string) --* **[REQUIRED]**
              The tag key.
            - **Value** *(string) --* **[REQUIRED]**
              The value for this key.
        :type RemoveTags: list
        :param RemoveTags:
          The tags to remove from the product.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def update_provisioned_product(self, UpdateToken: str, AcceptLanguage: str = None, ProvisionedProductName: str = None, ProvisionedProductId: str = None, ProductId: str = None, ProvisioningArtifactId: str = None, PathId: str = None, ProvisioningParameters: List = None, ProvisioningPreferences: Dict = None) -> Dict:
        """
        Requests updates to the configuration of the specified provisioned product.
        If there are tags associated with the object, they cannot be updated or added. Depending on the specific updates requested, this operation can update with no interruption, with some interruption, or replace the provisioned product entirely.
        You can check the status of this request using  DescribeRecord .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/UpdateProvisionedProduct>`_
        
        **Request Syntax**
        ::
          response = client.update_provisioned_product(
              AcceptLanguage='string',
              ProvisionedProductName='string',
              ProvisionedProductId='string',
              ProductId='string',
              ProvisioningArtifactId='string',
              PathId='string',
              ProvisioningParameters=[
                  {
                      'Key': 'string',
                      'Value': 'string',
                      'UsePreviousValue': True|False
                  },
              ],
              ProvisioningPreferences={
                  'StackSetAccounts': [
                      'string',
                  ],
                  'StackSetRegions': [
                      'string',
                  ],
                  'StackSetFailureToleranceCount': 123,
                  'StackSetFailureTolerancePercentage': 123,
                  'StackSetMaxConcurrencyCount': 123,
                  'StackSetMaxConcurrencyPercentage': 123,
                  'StackSetOperationType': 'CREATE'|'UPDATE'|'DELETE'
              },
              UpdateToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'RecordDetail': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RecordDetail** *(dict) --* 
              Information about the result of the request.
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
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type ProvisionedProductName: string
        :param ProvisionedProductName:
          The updated name of the provisioned product. You cannot specify both ``ProvisionedProductName`` and ``ProvisionedProductId`` .
        :type ProvisionedProductId: string
        :param ProvisionedProductId:
          The identifier of the provisioned product. You cannot specify both ``ProvisionedProductName`` and ``ProvisionedProductId`` .
        :type ProductId: string
        :param ProductId:
          The identifier of the product.
        :type ProvisioningArtifactId: string
        :param ProvisioningArtifactId:
          The identifier of the provisioning artifact.
        :type PathId: string
        :param PathId:
          The new path identifier. This value is optional if the product has a default path, and required if the product has more than one path.
        :type ProvisioningParameters: list
        :param ProvisioningParameters:
          The new parameters.
          - *(dict) --*
            The parameter key-value pair used to update a provisioned product.
            - **Key** *(string) --*
              The parameter key.
            - **Value** *(string) --*
              The parameter value.
            - **UsePreviousValue** *(boolean) --*
              If set to true, ``Value`` is ignored and the previous parameter value is kept.
        :type ProvisioningPreferences: dict
        :param ProvisioningPreferences:
          An object that contains information about the provisioning preferences for a stack set.
          - **StackSetAccounts** *(list) --*
            One or more AWS accounts that will have access to the provisioned product.
            Applicable only to a ``CFN_STACKSET`` provisioned product type.
            The AWS accounts specified should be within the list of accounts in the ``STACKSET`` constraint. To get the list of accounts in the ``STACKSET`` constraint, use the ``DescribeProvisioningParameters`` operation.
            If no values are specified, the default value is all accounts from the ``STACKSET`` constraint.
            - *(string) --*
          - **StackSetRegions** *(list) --*
            One or more AWS Regions where the provisioned product will be available.
            Applicable only to a ``CFN_STACKSET`` provisioned product type.
            The specified regions should be within the list of regions from the ``STACKSET`` constraint. To get the list of regions in the ``STACKSET`` constraint, use the ``DescribeProvisioningParameters`` operation.
            If no values are specified, the default value is all regions from the ``STACKSET`` constraint.
            - *(string) --*
          - **StackSetFailureToleranceCount** *(integer) --*
            The number of accounts, per region, for which this operation can fail before AWS Service Catalog stops the operation in that region. If the operation is stopped in a region, AWS Service Catalog doesn\'t attempt the operation in any subsequent regions.
            Applicable only to a ``CFN_STACKSET`` provisioned product type.
            Conditional: You must specify either ``StackSetFailureToleranceCount`` or ``StackSetFailureTolerancePercentage`` , but not both.
            The default value is ``0`` if no value is specified.
          - **StackSetFailureTolerancePercentage** *(integer) --*
            The percentage of accounts, per region, for which this stack operation can fail before AWS Service Catalog stops the operation in that region. If the operation is stopped in a region, AWS Service Catalog doesn\'t attempt the operation in any subsequent regions.
            When calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number.
            Applicable only to a ``CFN_STACKSET`` provisioned product type.
            Conditional: You must specify either ``StackSetFailureToleranceCount`` or ``StackSetFailureTolerancePercentage`` , but not both.
          - **StackSetMaxConcurrencyCount** *(integer) --*
            The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of ``StackSetFailureToleranceCount`` . ``StackSetMaxConcurrentCount`` is at most one more than the ``StackSetFailureToleranceCount`` .
            Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
            Applicable only to a ``CFN_STACKSET`` provisioned product type.
            Conditional: You must specify either ``StackSetMaxConcurrentCount`` or ``StackSetMaxConcurrentPercentage`` , but not both.
          - **StackSetMaxConcurrencyPercentage** *(integer) --*
            The maximum percentage of accounts in which to perform this operation at one time.
            When calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, AWS Service Catalog sets the number as ``1`` instead.
            Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
            Applicable only to a ``CFN_STACKSET`` provisioned product type.
            Conditional: You must specify either ``StackSetMaxConcurrentCount`` or ``StackSetMaxConcurrentPercentage`` , but not both.
          - **StackSetOperationType** *(string) --*
            Determines what action AWS Service Catalog performs to a stack set or a stack instance represented by the provisioned product. The default value is ``UPDATE`` if nothing is specified.
            Applicable only to a ``CFN_STACKSET`` provisioned product type.
              CREATE
            Creates a new stack instance in the stack set represented by the provisioned product. In this case, only new stack instances are created based on accounts and regions; if new ProductId or ProvisioningArtifactID are passed, they will be ignored.
              UPDATE
            Updates the stack set represented by the provisioned product and also its stack instances.
              DELETE
            Deletes a stack instance in the stack set represented by the provisioned product.
        :type UpdateToken: string
        :param UpdateToken: **[REQUIRED]**
          The idempotency token that uniquely identifies the provisioning update request.
          This field is autopopulated if not provided.
        :rtype: dict
        :returns:
        """
        pass

    def update_provisioning_artifact(self, ProductId: str, ProvisioningArtifactId: str, AcceptLanguage: str = None, Name: str = None, Description: str = None, Active: bool = None) -> Dict:
        """
        Updates the specified provisioning artifact (also known as a version) for the specified product.
        You cannot update a provisioning artifact for a product that was shared with you.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/UpdateProvisioningArtifact>`_
        
        **Request Syntax**
        ::
          response = client.update_provisioning_artifact(
              AcceptLanguage='string',
              ProductId='string',
              ProvisioningArtifactId='string',
              Name='string',
              Description='string',
              Active=True|False
          )
        
        **Response Syntax**
        ::
            {
                'ProvisioningArtifactDetail': {
                    'Id': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
                    'CreatedTime': datetime(2015, 1, 1),
                    'Active': True|False
                },
                'Info': {
                    'string': 'string'
                },
                'Status': 'AVAILABLE'|'CREATING'|'FAILED'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ProvisioningArtifactDetail** *(dict) --* 
              Information about the provisioning artifact.
              - **Id** *(string) --* 
                The identifier of the provisioning artifact.
              - **Name** *(string) --* 
                The name of the provisioning artifact.
              - **Description** *(string) --* 
                The description of the provisioning artifact.
              - **Type** *(string) --* 
                The type of provisioning artifact.
                * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template 
                * ``MARKETPLACE_AMI`` - AWS Marketplace AMI 
                * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources 
              - **CreatedTime** *(datetime) --* 
                The UTC time stamp of the creation time.
              - **Active** *(boolean) --* 
                Indicates whether the product version is active.
            - **Info** *(dict) --* 
              The URL of the CloudFormation template in Amazon S3.
              - *(string) --* 
                - *(string) --* 
            - **Status** *(string) --* 
              The status of the current request.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :type ProductId: string
        :param ProductId: **[REQUIRED]**
          The product identifier.
        :type ProvisioningArtifactId: string
        :param ProvisioningArtifactId: **[REQUIRED]**
          The identifier of the provisioning artifact.
        :type Name: string
        :param Name:
          The updated name of the provisioning artifact.
        :type Description: string
        :param Description:
          The updated description of the provisioning artifact.
        :type Active: boolean
        :param Active:
          Indicates whether the product version is active.
        :rtype: dict
        :returns:
        """
        pass

    def update_service_action(self, Id: str, Name: str = None, Definition: Dict = None, Description: str = None, AcceptLanguage: str = None) -> Dict:
        """
        Updates a self-service action.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/UpdateServiceAction>`_
        
        **Request Syntax**
        ::
          response = client.update_service_action(
              Id='string',
              Name='string',
              Definition={
                  'string': 'string'
              },
              Description='string',
              AcceptLanguage='string'
          )
        
        **Response Syntax**
        ::
            {
                'ServiceActionDetail': {
                    'ServiceActionSummary': {
                        'Id': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'DefinitionType': 'SSM_AUTOMATION'
                    },
                    'Definition': {
                        'string': 'string'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ServiceActionDetail** *(dict) --* 
              Detailed information about the self-service action.
              - **ServiceActionSummary** *(dict) --* 
                Summary information about the self-service action.
                - **Id** *(string) --* 
                  The self-service action identifier.
                - **Name** *(string) --* 
                  The self-service action name.
                - **Description** *(string) --* 
                  The self-service action description.
                - **DefinitionType** *(string) --* 
                  The self-service action definition type. For example, ``SSM_AUTOMATION`` .
              - **Definition** *(dict) --* 
                A map that defines the self-service action.
                - *(string) --* 
                  - *(string) --* 
        :type Id: string
        :param Id: **[REQUIRED]**
          The self-service action identifier.
        :type Name: string
        :param Name:
          The self-service action name.
        :type Definition: dict
        :param Definition:
          A map that defines the self-service action.
          - *(string) --*
            - *(string) --*
        :type Description: string
        :param Description:
          The self-service action description.
        :type AcceptLanguage: string
        :param AcceptLanguage:
          The language code.
          * ``en`` - English (default)
          * ``jp`` - Japanese
          * ``zh`` - Chinese
        :rtype: dict
        :returns:
        """
        pass

    def update_tag_option(self, Id: str, Value: str = None, Active: bool = None) -> Dict:
        """
        Updates the specified TagOption.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/UpdateTagOption>`_
        
        **Request Syntax**
        ::
          response = client.update_tag_option(
              Id='string',
              Value='string',
              Active=True|False
          )
        
        **Response Syntax**
        ::
            {
                'TagOptionDetail': {
                    'Key': 'string',
                    'Value': 'string',
                    'Active': True|False,
                    'Id': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TagOptionDetail** *(dict) --* 
              Information about the TagOption.
              - **Key** *(string) --* 
                The TagOption key.
              - **Value** *(string) --* 
                The TagOption value.
              - **Active** *(boolean) --* 
                The TagOption active state.
              - **Id** *(string) --* 
                The TagOption identifier.
        :type Id: string
        :param Id: **[REQUIRED]**
          The TagOption identifier.
        :type Value: string
        :param Value:
          The updated value.
        :type Active: boolean
        :param Active:
          The updated active state.
        :rtype: dict
        :returns:
        """
        pass
