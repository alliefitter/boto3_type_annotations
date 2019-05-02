from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_api(self, Name: str, ProtocolType: str, RouteSelectionExpression: str, ApiKeySelectionExpression: str = None, Description: str = None, DisableSchemaValidation: bool = None, Version: str = None) -> Dict:
        pass

    def create_api_mapping(self, ApiId: str, DomainName: str, Stage: str, ApiMappingKey: str = None) -> Dict:
        pass

    def create_authorizer(self, ApiId: str, AuthorizerType: str, AuthorizerUri: str, IdentitySource: List, Name: str, AuthorizerCredentialsArn: str = None, AuthorizerResultTtlInSeconds: int = None, IdentityValidationExpression: str = None, ProviderArns: List = None) -> Dict:
        pass

    def create_deployment(self, ApiId: str, Description: str = None, StageName: str = None) -> Dict:
        pass

    def create_domain_name(self, DomainName: str, DomainNameConfigurations: List = None) -> Dict:
        pass

    def create_integration(self, ApiId: str, IntegrationType: str, ConnectionId: str = None, ConnectionType: str = None, ContentHandlingStrategy: str = None, CredentialsArn: str = None, Description: str = None, IntegrationMethod: str = None, IntegrationUri: str = None, PassthroughBehavior: str = None, RequestParameters: Dict = None, RequestTemplates: Dict = None, TemplateSelectionExpression: str = None, TimeoutInMillis: int = None) -> Dict:
        pass

    def create_integration_response(self, ApiId: str, IntegrationId: str, IntegrationResponseKey: str, ContentHandlingStrategy: str = None, ResponseParameters: Dict = None, ResponseTemplates: Dict = None, TemplateSelectionExpression: str = None) -> Dict:
        pass

    def create_model(self, ApiId: str, Name: str, Schema: str, ContentType: str = None, Description: str = None) -> Dict:
        pass

    def create_route(self, ApiId: str, RouteKey: str, ApiKeyRequired: bool = None, AuthorizationScopes: List = None, AuthorizationType: str = None, AuthorizerId: str = None, ModelSelectionExpression: str = None, OperationName: str = None, RequestModels: Dict = None, RequestParameters: Dict = None, RouteResponseSelectionExpression: str = None, Target: str = None) -> Dict:
        pass

    def create_route_response(self, ApiId: str, RouteId: str, RouteResponseKey: str, ModelSelectionExpression: str = None, ResponseModels: Dict = None, ResponseParameters: Dict = None) -> Dict:
        pass

    def create_stage(self, ApiId: str, StageName: str, AccessLogSettings: Dict = None, ClientCertificateId: str = None, DefaultRouteSettings: Dict = None, DeploymentId: str = None, Description: str = None, RouteSettings: Dict = None, StageVariables: Dict = None) -> Dict:
        pass

    def delete_api(self, ApiId: str):
        pass

    def delete_api_mapping(self, ApiMappingId: str, DomainName: str):
        pass

    def delete_authorizer(self, ApiId: str, AuthorizerId: str):
        pass

    def delete_deployment(self, ApiId: str, DeploymentId: str):
        pass

    def delete_domain_name(self, DomainName: str):
        pass

    def delete_integration(self, ApiId: str, IntegrationId: str):
        pass

    def delete_integration_response(self, ApiId: str, IntegrationId: str, IntegrationResponseId: str):
        pass

    def delete_model(self, ApiId: str, ModelId: str):
        pass

    def delete_route(self, ApiId: str, RouteId: str):
        pass

    def delete_route_response(self, ApiId: str, RouteId: str, RouteResponseId: str):
        pass

    def delete_stage(self, ApiId: str, StageName: str):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_api(self, ApiId: str) -> Dict:
        pass

    def get_api_mapping(self, ApiMappingId: str, DomainName: str) -> Dict:
        pass

    def get_api_mappings(self, DomainName: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def get_apis(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def get_authorizer(self, ApiId: str, AuthorizerId: str) -> Dict:
        pass

    def get_authorizers(self, ApiId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def get_deployment(self, ApiId: str, DeploymentId: str) -> Dict:
        pass

    def get_deployments(self, ApiId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def get_domain_name(self, DomainName: str) -> Dict:
        pass

    def get_domain_names(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def get_integration(self, ApiId: str, IntegrationId: str) -> Dict:
        pass

    def get_integration_response(self, ApiId: str, IntegrationId: str, IntegrationResponseId: str) -> Dict:
        pass

    def get_integration_responses(self, ApiId: str, IntegrationId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def get_integrations(self, ApiId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def get_model(self, ApiId: str, ModelId: str) -> Dict:
        pass

    def get_model_template(self, ApiId: str, ModelId: str) -> Dict:
        pass

    def get_models(self, ApiId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_route(self, ApiId: str, RouteId: str) -> Dict:
        pass

    def get_route_response(self, ApiId: str, RouteId: str, RouteResponseId: str) -> Dict:
        pass

    def get_route_responses(self, ApiId: str, RouteId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def get_routes(self, ApiId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def get_stage(self, ApiId: str, StageName: str) -> Dict:
        pass

    def get_stages(self, ApiId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def update_api(self, ApiId: str, ApiKeySelectionExpression: str = None, Description: str = None, DisableSchemaValidation: bool = None, Name: str = None, RouteSelectionExpression: str = None, Version: str = None) -> Dict:
        pass

    def update_api_mapping(self, ApiId: str, ApiMappingId: str, DomainName: str, ApiMappingKey: str = None, Stage: str = None) -> Dict:
        pass

    def update_authorizer(self, ApiId: str, AuthorizerId: str, AuthorizerCredentialsArn: str = None, AuthorizerResultTtlInSeconds: int = None, AuthorizerType: str = None, AuthorizerUri: str = None, IdentitySource: List = None, IdentityValidationExpression: str = None, Name: str = None, ProviderArns: List = None) -> Dict:
        pass

    def update_deployment(self, ApiId: str, DeploymentId: str, Description: str = None) -> Dict:
        pass

    def update_domain_name(self, DomainName: str, DomainNameConfigurations: List = None) -> Dict:
        pass

    def update_integration(self, ApiId: str, IntegrationId: str, ConnectionId: str = None, ConnectionType: str = None, ContentHandlingStrategy: str = None, CredentialsArn: str = None, Description: str = None, IntegrationMethod: str = None, IntegrationType: str = None, IntegrationUri: str = None, PassthroughBehavior: str = None, RequestParameters: Dict = None, RequestTemplates: Dict = None, TemplateSelectionExpression: str = None, TimeoutInMillis: int = None) -> Dict:
        pass

    def update_integration_response(self, ApiId: str, IntegrationId: str, IntegrationResponseId: str, ContentHandlingStrategy: str = None, IntegrationResponseKey: str = None, ResponseParameters: Dict = None, ResponseTemplates: Dict = None, TemplateSelectionExpression: str = None) -> Dict:
        pass

    def update_model(self, ApiId: str, ModelId: str, ContentType: str = None, Description: str = None, Name: str = None, Schema: str = None) -> Dict:
        pass

    def update_route(self, ApiId: str, RouteId: str, ApiKeyRequired: bool = None, AuthorizationScopes: List = None, AuthorizationType: str = None, AuthorizerId: str = None, ModelSelectionExpression: str = None, OperationName: str = None, RequestModels: Dict = None, RequestParameters: Dict = None, RouteKey: str = None, RouteResponseSelectionExpression: str = None, Target: str = None) -> Dict:
        pass

    def update_route_response(self, ApiId: str, RouteId: str, RouteResponseId: str, ModelSelectionExpression: str = None, ResponseModels: Dict = None, ResponseParameters: Dict = None, RouteResponseKey: str = None) -> Dict:
        pass

    def update_stage(self, ApiId: str, StageName: str, AccessLogSettings: Dict = None, ClientCertificateId: str = None, DefaultRouteSettings: Dict = None, DeploymentId: str = None, Description: str = None, RouteSettings: Dict = None, StageVariables: Dict = None) -> Dict:
        pass
