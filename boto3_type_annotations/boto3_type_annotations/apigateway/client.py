from typing import Union
from botocore.paginate import Paginator
from typing import IO
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_api_key(self, name: str = None, description: str = None, enabled: bool = None, generateDistinctId: bool = None, value: str = None, stageKeys: List = None, customerId: str = None) -> Dict:
        pass

    def create_authorizer(self, restApiId: str, name: str, type: str, providerARNs: List = None, authType: str = None, authorizerUri: str = None, authorizerCredentials: str = None, identitySource: str = None, identityValidationExpression: str = None, authorizerResultTtlInSeconds: int = None) -> Dict:
        pass

    def create_base_path_mapping(self, domainName: str, restApiId: str, basePath: str = None, stage: str = None) -> Dict:
        pass

    def create_deployment(self, restApiId: str, stageName: str = None, stageDescription: str = None, description: str = None, cacheClusterEnabled: bool = None, cacheClusterSize: str = None, variables: Dict = None, canarySettings: Dict = None, tracingEnabled: bool = None) -> Dict:
        pass

    def create_documentation_part(self, restApiId: str, location: Dict, properties: str) -> Dict:
        pass

    def create_documentation_version(self, restApiId: str, documentationVersion: str, stageName: str = None, description: str = None) -> Dict:
        pass

    def create_domain_name(self, domainName: str, certificateName: str = None, certificateBody: str = None, certificatePrivateKey: str = None, certificateChain: str = None, certificateArn: str = None, regionalCertificateName: str = None, regionalCertificateArn: str = None, endpointConfiguration: Dict = None) -> Dict:
        pass

    def create_model(self, restApiId: str, name: str, contentType: str, description: str = None, schema: str = None) -> Dict:
        pass

    def create_request_validator(self, restApiId: str, name: str = None, validateRequestBody: bool = None, validateRequestParameters: bool = None) -> Dict:
        pass

    def create_resource(self, restApiId: str, parentId: str, pathPart: str) -> Dict:
        pass

    def create_rest_api(self, name: str, description: str = None, version: str = None, cloneFrom: str = None, binaryMediaTypes: List = None, minimumCompressionSize: int = None, apiKeySource: str = None, endpointConfiguration: Dict = None, policy: str = None) -> Dict:
        pass

    def create_stage(self, restApiId: str, stageName: str, deploymentId: str, description: str = None, cacheClusterEnabled: bool = None, cacheClusterSize: str = None, variables: Dict = None, documentationVersion: str = None, canarySettings: Dict = None, tracingEnabled: bool = None, tags: Dict = None) -> Dict:
        pass

    def create_usage_plan(self, name: str, description: str = None, apiStages: List = None, throttle: Dict = None, quota: Dict = None) -> Dict:
        pass

    def create_usage_plan_key(self, usagePlanId: str, keyId: str, keyType: str) -> Dict:
        pass

    def create_vpc_link(self, name: str, targetArns: List, description: str = None) -> Dict:
        pass

    def delete_api_key(self, apiKey: str) -> NoReturn:
        pass

    def delete_authorizer(self, restApiId: str, authorizerId: str) -> NoReturn:
        pass

    def delete_base_path_mapping(self, domainName: str, basePath: str) -> NoReturn:
        pass

    def delete_client_certificate(self, clientCertificateId: str) -> NoReturn:
        pass

    def delete_deployment(self, restApiId: str, deploymentId: str) -> NoReturn:
        pass

    def delete_documentation_part(self, restApiId: str, documentationPartId: str) -> NoReturn:
        pass

    def delete_documentation_version(self, restApiId: str, documentationVersion: str) -> NoReturn:
        pass

    def delete_domain_name(self, domainName: str) -> NoReturn:
        pass

    def delete_gateway_response(self, restApiId: str, responseType: str) -> NoReturn:
        pass

    def delete_integration(self, restApiId: str, resourceId: str, httpMethod: str) -> NoReturn:
        pass

    def delete_integration_response(self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str) -> NoReturn:
        pass

    def delete_method(self, restApiId: str, resourceId: str, httpMethod: str) -> NoReturn:
        pass

    def delete_method_response(self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str) -> NoReturn:
        pass

    def delete_model(self, restApiId: str, modelName: str) -> NoReturn:
        pass

    def delete_request_validator(self, restApiId: str, requestValidatorId: str) -> NoReturn:
        pass

    def delete_resource(self, restApiId: str, resourceId: str) -> NoReturn:
        pass

    def delete_rest_api(self, restApiId: str) -> NoReturn:
        pass

    def delete_stage(self, restApiId: str, stageName: str) -> NoReturn:
        pass

    def delete_usage_plan(self, usagePlanId: str) -> NoReturn:
        pass

    def delete_usage_plan_key(self, usagePlanId: str, keyId: str) -> NoReturn:
        pass

    def delete_vpc_link(self, vpcLinkId: str) -> NoReturn:
        pass

    def flush_stage_authorizers_cache(self, restApiId: str, stageName: str) -> NoReturn:
        pass

    def flush_stage_cache(self, restApiId: str, stageName: str) -> NoReturn:
        pass

    def generate_client_certificate(self, description: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_account(self) -> Dict:
        pass

    def get_api_key(self, apiKey: str, includeValue: bool = None) -> Dict:
        pass

    def get_api_keys(self, position: str = None, limit: int = None, nameQuery: str = None, customerId: str = None, includeValues: bool = None) -> Dict:
        pass

    def get_authorizer(self, restApiId: str, authorizerId: str) -> Dict:
        pass

    def get_authorizers(self, restApiId: str, position: str = None, limit: int = None) -> Dict:
        pass

    def get_base_path_mapping(self, domainName: str, basePath: str) -> Dict:
        pass

    def get_base_path_mappings(self, domainName: str, position: str = None, limit: int = None) -> Dict:
        pass

    def get_client_certificate(self, clientCertificateId: str) -> Dict:
        pass

    def get_client_certificates(self, position: str = None, limit: int = None) -> Dict:
        pass

    def get_deployment(self, restApiId: str, deploymentId: str, embed: List = None) -> Dict:
        pass

    def get_deployments(self, restApiId: str, position: str = None, limit: int = None) -> Dict:
        pass

    def get_documentation_part(self, restApiId: str, documentationPartId: str) -> Dict:
        pass

    def get_documentation_parts(self, restApiId: str, type: str = None, nameQuery: str = None, path: str = None, position: str = None, limit: int = None, locationStatus: str = None) -> Dict:
        pass

    def get_documentation_version(self, restApiId: str, documentationVersion: str) -> Dict:
        pass

    def get_documentation_versions(self, restApiId: str, position: str = None, limit: int = None) -> Dict:
        pass

    def get_domain_name(self, domainName: str) -> Dict:
        pass

    def get_domain_names(self, position: str = None, limit: int = None) -> Dict:
        pass

    def get_export(self, restApiId: str, stageName: str, exportType: str, parameters: Dict = None, accepts: str = None) -> Dict:
        pass

    def get_gateway_response(self, restApiId: str, responseType: str) -> Dict:
        pass

    def get_gateway_responses(self, restApiId: str, position: str = None, limit: int = None) -> Dict:
        pass

    def get_integration(self, restApiId: str, resourceId: str, httpMethod: str) -> Dict:
        pass

    def get_integration_response(self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str) -> Dict:
        pass

    def get_method(self, restApiId: str, resourceId: str, httpMethod: str) -> Dict:
        pass

    def get_method_response(self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str) -> Dict:
        pass

    def get_model(self, restApiId: str, modelName: str, flatten: bool = None) -> Dict:
        pass

    def get_model_template(self, restApiId: str, modelName: str) -> Dict:
        pass

    def get_models(self, restApiId: str, position: str = None, limit: int = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_request_validator(self, restApiId: str, requestValidatorId: str) -> Dict:
        pass

    def get_request_validators(self, restApiId: str, position: str = None, limit: int = None) -> Dict:
        pass

    def get_resource(self, restApiId: str, resourceId: str, embed: List = None) -> Dict:
        pass

    def get_resources(self, restApiId: str, position: str = None, limit: int = None, embed: List = None) -> Dict:
        pass

    def get_rest_api(self, restApiId: str) -> Dict:
        pass

    def get_rest_apis(self, position: str = None, limit: int = None) -> Dict:
        pass

    def get_sdk(self, restApiId: str, stageName: str, sdkType: str, parameters: Dict = None) -> Dict:
        pass

    def get_sdk_type(self, id: str) -> Dict:
        pass

    def get_sdk_types(self, position: str = None, limit: int = None) -> Dict:
        pass

    def get_stage(self, restApiId: str, stageName: str) -> Dict:
        pass

    def get_stages(self, restApiId: str, deploymentId: str = None) -> Dict:
        pass

    def get_tags(self, resourceArn: str, position: str = None, limit: int = None) -> Dict:
        pass

    def get_usage(self, usagePlanId: str, startDate: str, endDate: str, keyId: str = None, position: str = None, limit: int = None) -> Dict:
        pass

    def get_usage_plan(self, usagePlanId: str) -> Dict:
        pass

    def get_usage_plan_key(self, usagePlanId: str, keyId: str) -> Dict:
        pass

    def get_usage_plan_keys(self, usagePlanId: str, position: str = None, limit: int = None, nameQuery: str = None) -> Dict:
        pass

    def get_usage_plans(self, position: str = None, keyId: str = None, limit: int = None) -> Dict:
        pass

    def get_vpc_link(self, vpcLinkId: str) -> Dict:
        pass

    def get_vpc_links(self, position: str = None, limit: int = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def import_api_keys(self, body: Union[bytes, IO], format: str, failOnWarnings: bool = None) -> Dict:
        pass

    def import_documentation_parts(self, restApiId: str, body: Union[bytes, IO], mode: str = None, failOnWarnings: bool = None) -> Dict:
        pass

    def import_rest_api(self, body: Union[bytes, IO], failOnWarnings: bool = None, parameters: Dict = None) -> Dict:
        pass

    def put_gateway_response(self, restApiId: str, responseType: str, statusCode: str = None, responseParameters: Dict = None, responseTemplates: Dict = None) -> Dict:
        pass

    def put_integration(self, restApiId: str, resourceId: str, httpMethod: str, type: str, integrationHttpMethod: str = None, uri: str = None, connectionType: str = None, connectionId: str = None, credentials: str = None, requestParameters: Dict = None, requestTemplates: Dict = None, passthroughBehavior: str = None, cacheNamespace: str = None, cacheKeyParameters: List = None, contentHandling: str = None, timeoutInMillis: int = None) -> Dict:
        pass

    def put_integration_response(self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str, selectionPattern: str = None, responseParameters: Dict = None, responseTemplates: Dict = None, contentHandling: str = None) -> Dict:
        pass

    def put_method(self, restApiId: str, resourceId: str, httpMethod: str, authorizationType: str, authorizerId: str = None, apiKeyRequired: bool = None, operationName: str = None, requestParameters: Dict = None, requestModels: Dict = None, requestValidatorId: str = None, authorizationScopes: List = None) -> Dict:
        pass

    def put_method_response(self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str, responseParameters: Dict = None, responseModels: Dict = None) -> Dict:
        pass

    def put_rest_api(self, restApiId: str, body: Union[bytes, IO], mode: str = None, failOnWarnings: bool = None, parameters: Dict = None) -> Dict:
        pass

    def tag_resource(self, resourceArn: str, tags: Dict) -> NoReturn:
        pass

    def test_invoke_authorizer(self, restApiId: str, authorizerId: str, headers: Dict = None, multiValueHeaders: Dict = None, pathWithQueryString: str = None, body: str = None, stageVariables: Dict = None, additionalContext: Dict = None) -> Dict:
        pass

    def test_invoke_method(self, restApiId: str, resourceId: str, httpMethod: str, pathWithQueryString: str = None, body: str = None, headers: Dict = None, multiValueHeaders: Dict = None, clientCertificateId: str = None, stageVariables: Dict = None) -> Dict:
        pass

    def untag_resource(self, resourceArn: str, tagKeys: List) -> NoReturn:
        pass

    def update_account(self, patchOperations: List = None) -> Dict:
        pass

    def update_api_key(self, apiKey: str, patchOperations: List = None) -> Dict:
        pass

    def update_authorizer(self, restApiId: str, authorizerId: str, patchOperations: List = None) -> Dict:
        pass

    def update_base_path_mapping(self, domainName: str, basePath: str, patchOperations: List = None) -> Dict:
        pass

    def update_client_certificate(self, clientCertificateId: str, patchOperations: List = None) -> Dict:
        pass

    def update_deployment(self, restApiId: str, deploymentId: str, patchOperations: List = None) -> Dict:
        pass

    def update_documentation_part(self, restApiId: str, documentationPartId: str, patchOperations: List = None) -> Dict:
        pass

    def update_documentation_version(self, restApiId: str, documentationVersion: str, patchOperations: List = None) -> Dict:
        pass

    def update_domain_name(self, domainName: str, patchOperations: List = None) -> Dict:
        pass

    def update_gateway_response(self, restApiId: str, responseType: str, patchOperations: List = None) -> Dict:
        pass

    def update_integration(self, restApiId: str, resourceId: str, httpMethod: str, patchOperations: List = None) -> Dict:
        pass

    def update_integration_response(self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str, patchOperations: List = None) -> Dict:
        pass

    def update_method(self, restApiId: str, resourceId: str, httpMethod: str, patchOperations: List = None) -> Dict:
        pass

    def update_method_response(self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str, patchOperations: List = None) -> Dict:
        pass

    def update_model(self, restApiId: str, modelName: str, patchOperations: List = None) -> Dict:
        pass

    def update_request_validator(self, restApiId: str, requestValidatorId: str, patchOperations: List = None) -> Dict:
        pass

    def update_resource(self, restApiId: str, resourceId: str, patchOperations: List = None) -> Dict:
        pass

    def update_rest_api(self, restApiId: str, patchOperations: List = None) -> Dict:
        pass

    def update_stage(self, restApiId: str, stageName: str, patchOperations: List = None) -> Dict:
        pass

    def update_usage(self, usagePlanId: str, keyId: str, patchOperations: List = None) -> Dict:
        pass

    def update_usage_plan(self, usagePlanId: str, patchOperations: List = None) -> Dict:
        pass

    def update_vpc_link(self, vpcLinkId: str, patchOperations: List = None) -> Dict:
        pass
