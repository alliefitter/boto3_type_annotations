from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def accept_portfolio_share(self, PortfolioId: str, AcceptLanguage: str = None, PortfolioShareType: str = None) -> Dict:
        pass

    def associate_principal_with_portfolio(self, PortfolioId: str, PrincipalARN: str, PrincipalType: str, AcceptLanguage: str = None) -> Dict:
        pass

    def associate_product_with_portfolio(self, ProductId: str, PortfolioId: str, AcceptLanguage: str = None, SourcePortfolioId: str = None) -> Dict:
        pass

    def associate_service_action_with_provisioning_artifact(self, ProductId: str, ProvisioningArtifactId: str, ServiceActionId: str, AcceptLanguage: str = None) -> Dict:
        pass

    def associate_tag_option_with_resource(self, ResourceId: str, TagOptionId: str) -> Dict:
        pass

    def batch_associate_service_action_with_provisioning_artifact(self, ServiceActionAssociations: List, AcceptLanguage: str = None) -> Dict:
        pass

    def batch_disassociate_service_action_from_provisioning_artifact(self, ServiceActionAssociations: List, AcceptLanguage: str = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def copy_product(self, SourceProductArn: str, IdempotencyToken: str, AcceptLanguage: str = None, TargetProductId: str = None, TargetProductName: str = None, SourceProvisioningArtifactIdentifiers: List = None, CopyOptions: List = None) -> Dict:
        pass

    def create_constraint(self, PortfolioId: str, ProductId: str, Parameters: str, Type: str, IdempotencyToken: str, AcceptLanguage: str = None, Description: str = None) -> Dict:
        pass

    def create_portfolio(self, DisplayName: str, ProviderName: str, IdempotencyToken: str, AcceptLanguage: str = None, Description: str = None, Tags: List = None) -> Dict:
        pass

    def create_portfolio_share(self, PortfolioId: str, AcceptLanguage: str = None, AccountId: str = None, OrganizationNode: Dict = None) -> Dict:
        pass

    def create_product(self, Name: str, Owner: str, ProductType: str, ProvisioningArtifactParameters: Dict, IdempotencyToken: str, AcceptLanguage: str = None, Description: str = None, Distributor: str = None, SupportDescription: str = None, SupportEmail: str = None, SupportUrl: str = None, Tags: List = None) -> Dict:
        pass

    def create_provisioned_product_plan(self, PlanName: str, PlanType: str, ProductId: str, ProvisionedProductName: str, ProvisioningArtifactId: str, IdempotencyToken: str, AcceptLanguage: str = None, NotificationArns: List = None, PathId: str = None, ProvisioningParameters: List = None, Tags: List = None) -> Dict:
        pass

    def create_provisioning_artifact(self, ProductId: str, Parameters: Dict, IdempotencyToken: str, AcceptLanguage: str = None) -> Dict:
        pass

    def create_service_action(self, Name: str, DefinitionType: str, Definition: Dict, IdempotencyToken: str, Description: str = None, AcceptLanguage: str = None) -> Dict:
        pass

    def create_tag_option(self, Key: str, Value: str) -> Dict:
        pass

    def delete_constraint(self, Id: str, AcceptLanguage: str = None) -> Dict:
        pass

    def delete_portfolio(self, Id: str, AcceptLanguage: str = None) -> Dict:
        pass

    def delete_portfolio_share(self, PortfolioId: str, AcceptLanguage: str = None, AccountId: str = None, OrganizationNode: Dict = None) -> Dict:
        pass

    def delete_product(self, Id: str, AcceptLanguage: str = None) -> Dict:
        pass

    def delete_provisioned_product_plan(self, PlanId: str, AcceptLanguage: str = None, IgnoreErrors: bool = None) -> Dict:
        pass

    def delete_provisioning_artifact(self, ProductId: str, ProvisioningArtifactId: str, AcceptLanguage: str = None) -> Dict:
        pass

    def delete_service_action(self, Id: str, AcceptLanguage: str = None) -> Dict:
        pass

    def delete_tag_option(self, Id: str) -> Dict:
        pass

    def describe_constraint(self, Id: str, AcceptLanguage: str = None) -> Dict:
        pass

    def describe_copy_product_status(self, CopyProductToken: str, AcceptLanguage: str = None) -> Dict:
        pass

    def describe_portfolio(self, Id: str, AcceptLanguage: str = None) -> Dict:
        pass

    def describe_portfolio_share_status(self, PortfolioShareToken: str) -> Dict:
        pass

    def describe_product(self, Id: str, AcceptLanguage: str = None) -> Dict:
        pass

    def describe_product_as_admin(self, Id: str, AcceptLanguage: str = None) -> Dict:
        pass

    def describe_product_view(self, Id: str, AcceptLanguage: str = None) -> Dict:
        pass

    def describe_provisioned_product(self, Id: str, AcceptLanguage: str = None) -> Dict:
        pass

    def describe_provisioned_product_plan(self, PlanId: str, AcceptLanguage: str = None, PageSize: int = None, PageToken: str = None) -> Dict:
        pass

    def describe_provisioning_artifact(self, ProvisioningArtifactId: str, ProductId: str, AcceptLanguage: str = None, Verbose: bool = None) -> Dict:
        pass

    def describe_provisioning_parameters(self, ProductId: str, ProvisioningArtifactId: str, AcceptLanguage: str = None, PathId: str = None) -> Dict:
        pass

    def describe_record(self, Id: str, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None) -> Dict:
        pass

    def describe_service_action(self, Id: str, AcceptLanguage: str = None) -> Dict:
        pass

    def describe_tag_option(self, Id: str) -> Dict:
        pass

    def disable_aws_organizations_access(self) -> Dict:
        pass

    def disassociate_principal_from_portfolio(self, PortfolioId: str, PrincipalARN: str, AcceptLanguage: str = None) -> Dict:
        pass

    def disassociate_product_from_portfolio(self, ProductId: str, PortfolioId: str, AcceptLanguage: str = None) -> Dict:
        pass

    def disassociate_service_action_from_provisioning_artifact(self, ProductId: str, ProvisioningArtifactId: str, ServiceActionId: str, AcceptLanguage: str = None) -> Dict:
        pass

    def disassociate_tag_option_from_resource(self, ResourceId: str, TagOptionId: str) -> Dict:
        pass

    def enable_aws_organizations_access(self) -> Dict:
        pass

    def execute_provisioned_product_plan(self, PlanId: str, IdempotencyToken: str, AcceptLanguage: str = None) -> Dict:
        pass

    def execute_provisioned_product_service_action(self, ProvisionedProductId: str, ServiceActionId: str, ExecuteToken: str, AcceptLanguage: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_aws_organizations_access_status(self) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_accepted_portfolio_shares(self, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None, PortfolioShareType: str = None) -> Dict:
        pass

    def list_constraints_for_portfolio(self, PortfolioId: str, AcceptLanguage: str = None, ProductId: str = None, PageSize: int = None, PageToken: str = None) -> Dict:
        pass

    def list_launch_paths(self, ProductId: str, AcceptLanguage: str = None, PageSize: int = None, PageToken: str = None) -> Dict:
        pass

    def list_organization_portfolio_access(self, PortfolioId: str, OrganizationNodeType: str, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None) -> Dict:
        pass

    def list_portfolio_access(self, PortfolioId: str, AcceptLanguage: str = None) -> Dict:
        pass

    def list_portfolios(self, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None) -> Dict:
        pass

    def list_portfolios_for_product(self, ProductId: str, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None) -> Dict:
        pass

    def list_principals_for_portfolio(self, PortfolioId: str, AcceptLanguage: str = None, PageSize: int = None, PageToken: str = None) -> Dict:
        pass

    def list_provisioned_product_plans(self, AcceptLanguage: str = None, ProvisionProductId: str = None, PageSize: int = None, PageToken: str = None, AccessLevelFilter: Dict = None) -> Dict:
        pass

    def list_provisioning_artifacts(self, ProductId: str, AcceptLanguage: str = None) -> Dict:
        pass

    def list_provisioning_artifacts_for_service_action(self, ServiceActionId: str, PageSize: int = None, PageToken: str = None, AcceptLanguage: str = None) -> Dict:
        pass

    def list_record_history(self, AcceptLanguage: str = None, AccessLevelFilter: Dict = None, SearchFilter: Dict = None, PageSize: int = None, PageToken: str = None) -> Dict:
        pass

    def list_resources_for_tag_option(self, TagOptionId: str, ResourceType: str = None, PageSize: int = None, PageToken: str = None) -> Dict:
        pass

    def list_service_actions(self, AcceptLanguage: str = None, PageSize: int = None, PageToken: str = None) -> Dict:
        pass

    def list_service_actions_for_provisioning_artifact(self, ProductId: str, ProvisioningArtifactId: str, PageSize: int = None, PageToken: str = None, AcceptLanguage: str = None) -> Dict:
        pass

    def list_tag_options(self, Filters: Dict = None, PageSize: int = None, PageToken: str = None) -> Dict:
        pass

    def provision_product(self, ProductId: str, ProvisioningArtifactId: str, ProvisionedProductName: str, ProvisionToken: str, AcceptLanguage: str = None, PathId: str = None, ProvisioningParameters: List = None, Tags: List = None, NotificationArns: List = None) -> Dict:
        pass

    def reject_portfolio_share(self, PortfolioId: str, AcceptLanguage: str = None, PortfolioShareType: str = None) -> Dict:
        pass

    def scan_provisioned_products(self, AcceptLanguage: str = None, AccessLevelFilter: Dict = None, PageSize: int = None, PageToken: str = None) -> Dict:
        pass

    def search_products(self, AcceptLanguage: str = None, Filters: Dict = None, PageSize: int = None, SortBy: str = None, SortOrder: str = None, PageToken: str = None) -> Dict:
        pass

    def search_products_as_admin(self, AcceptLanguage: str = None, PortfolioId: str = None, Filters: Dict = None, SortBy: str = None, SortOrder: str = None, PageToken: str = None, PageSize: int = None, ProductSource: str = None) -> Dict:
        pass

    def search_provisioned_products(self, AcceptLanguage: str = None, AccessLevelFilter: Dict = None, Filters: Dict = None, SortBy: str = None, SortOrder: str = None, PageSize: int = None, PageToken: str = None) -> Dict:
        pass

    def terminate_provisioned_product(self, TerminateToken: str, ProvisionedProductName: str = None, ProvisionedProductId: str = None, IgnoreErrors: bool = None, AcceptLanguage: str = None) -> Dict:
        pass

    def update_constraint(self, Id: str, AcceptLanguage: str = None, Description: str = None) -> Dict:
        pass

    def update_portfolio(self, Id: str, AcceptLanguage: str = None, DisplayName: str = None, Description: str = None, ProviderName: str = None, AddTags: List = None, RemoveTags: List = None) -> Dict:
        pass

    def update_product(self, Id: str, AcceptLanguage: str = None, Name: str = None, Owner: str = None, Description: str = None, Distributor: str = None, SupportDescription: str = None, SupportEmail: str = None, SupportUrl: str = None, AddTags: List = None, RemoveTags: List = None) -> Dict:
        pass

    def update_provisioned_product(self, UpdateToken: str, AcceptLanguage: str = None, ProvisionedProductName: str = None, ProvisionedProductId: str = None, ProductId: str = None, ProvisioningArtifactId: str = None, PathId: str = None, ProvisioningParameters: List = None) -> Dict:
        pass

    def update_provisioning_artifact(self, ProductId: str, ProvisioningArtifactId: str, AcceptLanguage: str = None, Name: str = None, Description: str = None, Active: bool = None) -> Dict:
        pass

    def update_service_action(self, Id: str, Name: str = None, Definition: Dict = None, Description: str = None, AcceptLanguage: str = None) -> Dict:
        pass

    def update_tag_option(self, Id: str, Value: str = None, Active: bool = None) -> Dict:
        pass
