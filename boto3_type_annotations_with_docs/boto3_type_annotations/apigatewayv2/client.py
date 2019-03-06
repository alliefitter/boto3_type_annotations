from typing import Union
from typing import List
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Optional
from typing import Dict
from botocore.client import BaseClient


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

    def create_api(self, Name: str, ProtocolType: str, RouteSelectionExpression: str, ApiKeySelectionExpression: str = None, Description: str = None, DisableSchemaValidation: bool = None, Version: str = None) -> Dict:
        """
        Creates an Api resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/CreateApi>`_
        
        **Request Syntax**
        ::
          response = client.create_api(
              ApiKeySelectionExpression='string',
              Description='string',
              DisableSchemaValidation=True|False,
              Name='string',
              ProtocolType='WEBSOCKET',
              RouteSelectionExpression='string',
              Version='string'
          )
        
        **Response Syntax**
        ::
            {
                'ApiEndpoint': 'string',
                'ApiId': 'string',
                'ApiKeySelectionExpression': 'string',
                'CreatedDate': datetime(2015, 1, 1),
                'Description': 'string',
                'DisableSchemaValidation': True|False,
                'Name': 'string',
                'ProtocolType': 'WEBSOCKET',
                'RouteSelectionExpression': 'string',
                'Version': 'string',
                'Warnings': [
                    'string',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            The request has succeeded and has resulted in the creation of a resource.
            - **ApiEndpoint** *(string) --* 
              The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name is typically appended to this URI to form a complete path to a deployed API stage.
            - **ApiId** *(string) --* 
              The API ID.
            - **ApiKeySelectionExpression** *(string) --* 
              An API key selection expression. See `API Key Selection Expressions <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions>`__ .
            - **CreatedDate** *(datetime) --* 
              The timestamp when the API was created.
            - **Description** *(string) --* 
              The description of the API.
            - **DisableSchemaValidation** *(boolean) --* 
              Avoid validating models when creating a deployment.
            - **Name** *(string) --* 
              The name of the API.
            - **ProtocolType** *(string) --* 
              The API protocol: HTTP or WEBSOCKET.
            - **RouteSelectionExpression** *(string) --* 
              The route selection expression for the API.
            - **Version** *(string) --* 
              A version identifier for the API.
            - **Warnings** *(list) --* 
              The warning messages reported when failonwarnings is turned on during API import.
              - *(string) --* 
        :type ApiKeySelectionExpression: string
        :param ApiKeySelectionExpression:
          An API key selection expression. See `API Key Selection Expressions <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions>`__ .
        :type Description: string
        :param Description:
          The description of the API.
        :type DisableSchemaValidation: boolean
        :param DisableSchemaValidation:
          Avoid validating models when creating a deployment.
        :type Name: string
        :param Name: **[REQUIRED]**
          The name of the API.
        :type ProtocolType: string
        :param ProtocolType: **[REQUIRED]**
          The API protocol: HTTP or WEBSOCKET.
        :type RouteSelectionExpression: string
        :param RouteSelectionExpression: **[REQUIRED]**
          The route selection expression for the API.
        :type Version: string
        :param Version:
          A version identifier for the API.
        :rtype: dict
        :returns:
        """
        pass

    def create_api_mapping(self, ApiId: str, DomainName: str, Stage: str, ApiMappingKey: str = None) -> Dict:
        """
        Creates an API mapping.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/CreateApiMapping>`_
        
        **Request Syntax**
        ::
          response = client.create_api_mapping(
              ApiId='string',
              ApiMappingKey='string',
              DomainName='string',
              Stage='string'
          )
        
        **Response Syntax**
        ::
            {
                'ApiId': 'string',
                'ApiMappingId': 'string',
                'ApiMappingKey': 'string',
                'Stage': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The request has succeeded and has resulted in the creation of a resource.
            - **ApiId** *(string) --* 
              The API identifier.
            - **ApiMappingId** *(string) --* 
              The API mapping identifier.
            - **ApiMappingKey** *(string) --* 
              The API mapping key.
            - **Stage** *(string) --* 
              The API stage.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type ApiMappingKey: string
        :param ApiMappingKey:
        :type DomainName: string
        :param DomainName: **[REQUIRED]**
          The domain name.
        :type Stage: string
        :param Stage: **[REQUIRED]**
          The API stage.
        :rtype: dict
        :returns:
        """
        pass

    def create_authorizer(self, ApiId: str, AuthorizerType: str, AuthorizerUri: str, IdentitySource: List, Name: str, AuthorizerCredentialsArn: str = None, AuthorizerResultTtlInSeconds: int = None, IdentityValidationExpression: str = None, ProviderArns: List = None) -> Dict:
        """
        Creates an Authorizer for an API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/CreateAuthorizer>`_
        
        **Request Syntax**
        ::
          response = client.create_authorizer(
              ApiId='string',
              AuthorizerCredentialsArn='string',
              AuthorizerResultTtlInSeconds=123,
              AuthorizerType='REQUEST',
              AuthorizerUri='string',
              IdentitySource=[
                  'string',
              ],
              IdentityValidationExpression='string',
              Name='string',
              ProviderArns=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'AuthorizerCredentialsArn': 'string',
                'AuthorizerId': 'string',
                'AuthorizerResultTtlInSeconds': 123,
                'AuthorizerType': 'REQUEST',
                'AuthorizerUri': 'string',
                'IdentitySource': [
                    'string',
                ],
                'IdentityValidationExpression': 'string',
                'Name': 'string',
                'ProviderArns': [
                    'string',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            The request has succeeded and has resulted in the creation of a resource.
            - **AuthorizerCredentialsArn** *(string) --* 
              Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.
            - **AuthorizerId** *(string) --* 
              The authorizer identifier.
            - **AuthorizerResultTtlInSeconds** *(integer) --* 
              The time to live (TTL), in seconds, of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, the default value is 300. The maximum value is 3600, or 1 hour.
            - **AuthorizerType** *(string) --* 
              The authorizer type. Currently the only valid value is REQUEST, for a Lambda function using incoming request parameters.
            - **AuthorizerUri** *(string) --* 
              The authorizer's Uniform Resource Identifier (URI). ForREQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations. In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api} , where {region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial /. For Lambda functions, this is usually of the form /2015-03-31/functions/[FunctionARN]/invocations.
            - **IdentitySource** *(list) --* 
              The identity source for which authorization is requested.
              For the REQUEST authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an Auth header and a Name query string parameters are defined as identity sources, this value is method.request.header.Auth, method.request.querystring.Name. These parameters will be used to derive the authorization caching key and to perform runtime validation of the REQUEST authorizer by verifying all of the identity-related request parameters are present, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.
              - *(string) --* 
            - **IdentityValidationExpression** *(string) --* 
              The validation expression does not apply to the REQUEST authorizer.
            - **Name** *(string) --* 
              The name of the authorizer.
            - **ProviderArns** *(list) --* 
              For REQUEST authorizer, this is not defined.
              - *(string) --* 
                Represents an Amazon Resource Name (ARN).
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type AuthorizerCredentialsArn: string
        :param AuthorizerCredentialsArn:
          Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role\'s Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.
        :type AuthorizerResultTtlInSeconds: integer
        :param AuthorizerResultTtlInSeconds:
          The time to live (TTL), in seconds, of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, the default value is 300. The maximum value is 3600, or 1 hour.
        :type AuthorizerType: string
        :param AuthorizerType: **[REQUIRED]**
          The authorizer type. Currently the only valid value is REQUEST, for a Lambda function using incoming request parameters.
        :type AuthorizerUri: string
        :param AuthorizerUri: **[REQUIRED]**
          The authorizer\'s Uniform Resource Identifier (URI). For REQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations. In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api} , where {region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial /. For Lambda functions, this is usually of the form /2015-03-31/functions/[FunctionARN]/invocations.
        :type IdentitySource: list
        :param IdentitySource: **[REQUIRED]**
          The identity source for which authorization is requested.
          For the REQUEST authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an Auth header and a Name query string parameters are defined as identity sources, this value is method.request.header.Auth, method.request.querystring.Name. These parameters will be used to derive the authorization caching key and to perform runtime validation of the REQUEST authorizer by verifying all of the identity-related request parameters are present, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.
          - *(string) --*
        :type IdentityValidationExpression: string
        :param IdentityValidationExpression:
          The validation expression does not apply to the REQUEST authorizer.
        :type Name: string
        :param Name: **[REQUIRED]**
          The name of the authorizer.
        :type ProviderArns: list
        :param ProviderArns:
          For REQUEST authorizer, this is not defined.
          - *(string) --*
            Represents an Amazon Resource Name (ARN).
        :rtype: dict
        :returns:
        """
        pass

    def create_deployment(self, ApiId: str, Description: str = None, StageName: str = None) -> Dict:
        """
        Creates a Deployment for an API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/CreateDeployment>`_
        
        **Request Syntax**
        ::
          response = client.create_deployment(
              ApiId='string',
              Description='string',
              StageName='string'
          )
        
        **Response Syntax**
        ::
            {
                'CreatedDate': datetime(2015, 1, 1),
                'DeploymentId': 'string',
                'DeploymentStatus': 'PENDING'|'FAILED'|'DEPLOYED',
                'DeploymentStatusMessage': 'string',
                'Description': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The request has succeeded and has resulted in the creation of a resource.
            - **CreatedDate** *(datetime) --* 
              The date and time when the Deployment resource was created.
            - **DeploymentId** *(string) --* 
              The identifier for the deployment.
            - **DeploymentStatus** *(string) --* 
              The status of the deployment: PENDING, FAILED, or SUCCEEDED.
            - **DeploymentStatusMessage** *(string) --* 
              May contain additional feedback on the status of an API deployment.
            - **Description** *(string) --* 
              The description for the deployment.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type Description: string
        :param Description:
          The description for the deployment resource.
        :type StageName: string
        :param StageName:
          The name of the Stage resource for the Deployment resource to create.
        :rtype: dict
        :returns:
        """
        pass

    def create_domain_name(self, DomainName: str, DomainNameConfigurations: List = None) -> Dict:
        """
        Creates a domain name.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/CreateDomainName>`_
        
        **Request Syntax**
        ::
          response = client.create_domain_name(
              DomainName='string',
              DomainNameConfigurations=[
                  {
                      'ApiGatewayDomainName': 'string',
                      'CertificateArn': 'string',
                      'CertificateName': 'string',
                      'CertificateUploadDate': datetime(2015, 1, 1),
                      'EndpointType': 'REGIONAL'|'EDGE',
                      'HostedZoneId': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'ApiMappingSelectionExpression': 'string',
                'DomainName': 'string',
                'DomainNameConfigurations': [
                    {
                        'ApiGatewayDomainName': 'string',
                        'CertificateArn': 'string',
                        'CertificateName': 'string',
                        'CertificateUploadDate': datetime(2015, 1, 1),
                        'EndpointType': 'REGIONAL'|'EDGE',
                        'HostedZoneId': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            The request has succeeded and has resulted in the creation of a resource.
            - **ApiMappingSelectionExpression** *(string) --* 
              The API mapping selection expression.
            - **DomainName** *(string) --* 
              The name of the DomainName resource.
            - **DomainNameConfigurations** *(list) --* 
              The domain name configurations.
              - *(dict) --* 
                The domain name configuration.
                - **ApiGatewayDomainName** *(string) --* 
                  A domain name for the WebSocket API.
                - **CertificateArn** *(string) --* 
                  An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.
                - **CertificateName** *(string) --* 
                  The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.
                - **CertificateUploadDate** *(datetime) --* 
                  The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.
                - **EndpointType** *(string) --* 
                  The endpoint type.
                - **HostedZoneId** *(string) --* 
                  The Amazon Route 53 Hosted Zone ID of the endpoint. See `AWS Regions and Endpoints for API Gateway <docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ .
        :type DomainName: string
        :param DomainName: **[REQUIRED]**
          The domain name.
        :type DomainNameConfigurations: list
        :param DomainNameConfigurations:
          The domain name configurations.
          - *(dict) --*
            The domain name configuration.
            - **ApiGatewayDomainName** *(string) --*
              A domain name for the WebSocket API.
            - **CertificateArn** *(string) --*
              An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.
            - **CertificateName** *(string) --*
              The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.
            - **CertificateUploadDate** *(datetime) --*
              The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.
            - **EndpointType** *(string) --*
              The endpoint type.
            - **HostedZoneId** *(string) --*
              The Amazon Route 53 Hosted Zone ID of the endpoint. See `AWS Regions and Endpoints for API Gateway <docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ .
        :rtype: dict
        :returns:
        """
        pass

    def create_integration(self, ApiId: str, ConnectionId: str = None, ConnectionType: str = None, ContentHandlingStrategy: str = None, CredentialsArn: str = None, Description: str = None, IntegrationMethod: str = None, IntegrationType: str = None, IntegrationUri: str = None, PassthroughBehavior: str = None, RequestParameters: Dict = None, RequestTemplates: Dict = None, TemplateSelectionExpression: str = None, TimeoutInMillis: int = None) -> Dict:
        """
        Creates an Integration.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/CreateIntegration>`_
        
        **Request Syntax**
        ::
          response = client.create_integration(
              ApiId='string',
              ConnectionId='string',
              ConnectionType='INTERNET'|'VPC_LINK',
              ContentHandlingStrategy='CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
              CredentialsArn='string',
              Description='string',
              IntegrationMethod='string',
              IntegrationType='AWS'|'HTTP'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
              IntegrationUri='string',
              PassthroughBehavior='WHEN_NO_MATCH'|'NEVER'|'WHEN_NO_TEMPLATES',
              RequestParameters={
                  'string': 'string'
              },
              RequestTemplates={
                  'string': 'string'
              },
              TemplateSelectionExpression='string',
              TimeoutInMillis=123
          )
        
        **Response Syntax**
        ::
            {
                'ConnectionId': 'string',
                'ConnectionType': 'INTERNET'|'VPC_LINK',
                'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                'CredentialsArn': 'string',
                'Description': 'string',
                'IntegrationId': 'string',
                'IntegrationMethod': 'string',
                'IntegrationResponseSelectionExpression': 'string',
                'IntegrationType': 'AWS'|'HTTP'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                'IntegrationUri': 'string',
                'PassthroughBehavior': 'WHEN_NO_MATCH'|'NEVER'|'WHEN_NO_TEMPLATES',
                'RequestParameters': {
                    'string': 'string'
                },
                'RequestTemplates': {
                    'string': 'string'
                },
                'TemplateSelectionExpression': 'string',
                'TimeoutInMillis': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            The request has succeeded and has resulted in the creation of a resource.
            - **ConnectionId** *(string) --* 
              The identifier of the VpcLink used for the integration when the connectionType is VPC_LINK; otherwise undefined.
            - **ConnectionType** *(string) --* 
              The type of the network connection to the integration endpoint. The valid value is INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and a network load balancer in a VPC. The default value is INTERNET.
            - **ContentHandlingStrategy** *(string) --* 
              Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
              CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
              CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
              If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
            - **CredentialsArn** *(string) --* 
              Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, specify null.
            - **Description** *(string) --* 
              Represents the description of an integration.
            - **IntegrationId** *(string) --* 
              Represents the identifier of an integration.
            - **IntegrationMethod** *(string) --* 
              Specifies the integration's HTTP method type.
            - **IntegrationResponseSelectionExpression** *(string) --* 
            - **IntegrationType** *(string) --* 
              The integration type of an integration. One of the following:
              AWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
              AWS_PROXY: for integrating the route or method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as Lambda proxy integration.
              HTTP: for integrating the route or method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
              HTTP_PROXY: for integrating route or method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as HTTP proxy integration.
              MOCK: for integrating the route or method request with API Gateway as a "loopback" endpoint without invoking any backend.
            - **IntegrationUri** *(string) --* 
              Specifies the Uniform Resource Identifier (URI) of the integration endpoint.
              For HTTP or HTTP_PROXY integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the `RFC-3986 specification <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard integration, where connectionType is not VPC_LINK, or private integration, where connectionType is VPC_LINK. For a private HTTP integration, the URI is not used for routing.
              For AWS or AWS_PROXY integrations, the URI is of the form arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}. Here, {Region} is the API Gateway region (e.g., us-east-1); {service} is the name of the integrated AWS service (e.g., s3); and {subdomain} is a designated subdomain supported by certain AWS service for fast host-name lookup. action can be used for an AWS service action-based API, using an Action={name}&{p1}={v1}&p2={v2}... query string. The ensuing {service_api} refers to a supported action {name} plus any required input parameters. Alternatively, path can be used for an AWS service path-based API. The ensuing service_api refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of GetObject, the URI can be either arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key} or arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}
            - **PassthroughBehavior** *(string) --* 
              Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER.
              WHEN_NO_MATCH passes the request body for unmapped content types through to the integration backend without transformation.
              NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.
              WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same HTTP 415 Unsupported Media Type response.
            - **RequestParameters** *(dict) --* 
              A key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.{location}.{name} , where {location} is querystring, path, or header; and {name} must be a valid and unique method request parameter name.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [1-512].
            - **RequestTemplates** *(dict) --* 
              Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [0-32768].
            - **TemplateSelectionExpression** *(string) --* 
              The template selection expression for the integration.
            - **TimeoutInMillis** *(integer) --* 
              Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type ConnectionId: string
        :param ConnectionId:
          The identifier of the VpcLink used for the integration when the connectionType is VPC_LINK; otherwise undefined.
        :type ConnectionType: string
        :param ConnectionType:
          The type of the network connection to the integration endpoint. The valid value is INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and a network load balancer in a VPC. The default value is INTERNET.
        :type ContentHandlingStrategy: string
        :param ContentHandlingStrategy:
          Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
          CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
          CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
          If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
        :type CredentialsArn: string
        :param CredentialsArn:
          Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role\'s Amazon Resource Name (ARN). To require that the caller\'s identity be passed through from the request, specify the string arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, specify null.
        :type Description: string
        :param Description:
          The description of the integration.
        :type IntegrationMethod: string
        :param IntegrationMethod:
          Specifies the integration\'s HTTP method type.
        :type IntegrationType: string
        :param IntegrationType:
          The integration type of an integration. One of the following:
          AWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
          AWS_PROXY: for integrating the route or method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as Lambda proxy integration.
          HTTP: for integrating the route or method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
          HTTP_PROXY: for integrating route or method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as HTTP proxy integration.
          MOCK: for integrating the route or method request with API Gateway as a \"loopback\" endpoint without invoking any backend.
        :type IntegrationUri: string
        :param IntegrationUri:
          Specifies the Uniform Resource Identifier (URI) of the integration endpoint.
          For HTTP or HTTP_PROXY integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the `RFC-3986 specification <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard integration, where connectionType is not VPC_LINK, or private integration, where connectionType is VPC_LINK. For a private HTTP integration, the URI is not used for routing.
          For AWS or AWS_PROXY integrations, the URI is of the form arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}. Here, {Region} is the API Gateway region (e.g., us-east-1); {service} is the name of the integrated AWS service (e.g., s3); and {subdomain} is a designated subdomain supported by certain AWS service for fast host-name lookup. action can be used for an AWS service action-based API, using an Action={name}&{p1}={v1}&p2={v2}... query string. The ensuing {service_api} refers to a supported action {name} plus any required input parameters. Alternatively, path can be used for an AWS service path-based API. The ensuing service_api refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of GetObject, the URI can be either arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key} or arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}
        :type PassthroughBehavior: string
        :param PassthroughBehavior:
          Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER.
          WHEN_NO_MATCH passes the request body for unmapped content types through to the integration backend without transformation.
          NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.
          WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same HTTP 415 Unsupported Media Type response.
        :type RequestParameters: dict
        :param RequestParameters:
          A key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.{location}.{name} , where {location} is querystring, path, or header; and {name} must be a valid and unique method request parameter name.
          - *(string) --*
            - *(string) --*
              A string with a length between [1-512].
        :type RequestTemplates: dict
        :param RequestTemplates:
          Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.
          - *(string) --*
            - *(string) --*
              A string with a length between [0-32768].
        :type TemplateSelectionExpression: string
        :param TemplateSelectionExpression:
          The template selection expression for the integration.
        :type TimeoutInMillis: integer
        :param TimeoutInMillis:
          Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.
        :rtype: dict
        :returns:
        """
        pass

    def create_integration_response(self, ApiId: str, IntegrationId: str, IntegrationResponseKey: str, ContentHandlingStrategy: str = None, ResponseParameters: Dict = None, ResponseTemplates: Dict = None, TemplateSelectionExpression: str = None) -> Dict:
        """
        Creates an IntegrationResponses.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/CreateIntegrationResponse>`_
        
        **Request Syntax**
        ::
          response = client.create_integration_response(
              ApiId='string',
              ContentHandlingStrategy='CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
              IntegrationId='string',
              IntegrationResponseKey='string',
              ResponseParameters={
                  'string': 'string'
              },
              ResponseTemplates={
                  'string': 'string'
              },
              TemplateSelectionExpression='string'
          )
        
        **Response Syntax**
        ::
            {
                'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                'IntegrationResponseId': 'string',
                'IntegrationResponseKey': 'string',
                'ResponseParameters': {
                    'string': 'string'
                },
                'ResponseTemplates': {
                    'string': 'string'
                },
                'TemplateSelectionExpression': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The request has succeeded and has resulted in the creation of a resource.
            - **ContentHandlingStrategy** *(string) --* 
              Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
              CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
              CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
              If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
            - **IntegrationResponseId** *(string) --* 
              The integration response ID.
            - **IntegrationResponseKey** *(string) --* 
              The integration response key.
            - **ResponseParameters** *(dict) --* 
              A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name}, where name is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name} or integration.response.body.{JSON-expression}, where name is a valid and unique response header name and JSON-expression is a valid JSON expression without the $ prefix.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [1-512].
            - **ResponseTemplates** *(dict) --* 
              The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [0-32768].
            - **TemplateSelectionExpression** *(string) --* 
              The template selection expressions for the integration response.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type ContentHandlingStrategy: string
        :param ContentHandlingStrategy:
          Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
          CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
          CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
          If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
        :type IntegrationId: string
        :param IntegrationId: **[REQUIRED]**
          The integration ID.
        :type IntegrationResponseKey: string
        :param IntegrationResponseKey: **[REQUIRED]**
          The integration response key.
        :type ResponseParameters: dict
        :param ResponseParameters:
          A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name}, where {name} is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name} or integration.response.body.{JSON-expression}, where {name} is a valid and unique response header name and {JSON-expression} is a valid JSON expression without the $ prefix.
          - *(string) --*
            - *(string) --*
              A string with a length between [1-512].
        :type ResponseTemplates: dict
        :param ResponseTemplates:
          The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.
          - *(string) --*
            - *(string) --*
              A string with a length between [0-32768].
        :type TemplateSelectionExpression: string
        :param TemplateSelectionExpression:
          The template selection expression for the integration response.
        :rtype: dict
        :returns:
        """
        pass

    def create_model(self, ApiId: str, Name: str, ContentType: str = None, Description: str = None, Schema: str = None) -> Dict:
        """
        Creates a Model for an API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/CreateModel>`_
        
        **Request Syntax**
        ::
          response = client.create_model(
              ApiId='string',
              ContentType='string',
              Description='string',
              Name='string',
              Schema='string'
          )
        
        **Response Syntax**
        ::
            {
                'ContentType': 'string',
                'Description': 'string',
                'ModelId': 'string',
                'Name': 'string',
                'Schema': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The request has succeeded and has resulted in the creation of a resource.
            - **ContentType** *(string) --* 
              The content-type for the model, for example, "application/json".
            - **Description** *(string) --* 
              The description of the model.
            - **ModelId** *(string) --* 
              The model identifier.
            - **Name** *(string) --* 
              The name of the model. Must be alphanumeric.
            - **Schema** *(string) --* 
              The schema for the model. For application/json models, this should be JSON schema draft 4 model.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type ContentType: string
        :param ContentType:
          The content-type for the model, for example, \"application/json\".
        :type Description: string
        :param Description:
          The description of the model.
        :type Name: string
        :param Name: **[REQUIRED]**
          The name of the model. Must be alphanumeric.
        :type Schema: string
        :param Schema:
          The schema for the model. For application/json models, this should be JSON schema draft 4 model.
        :rtype: dict
        :returns:
        """
        pass

    def create_route(self, ApiId: str, RouteKey: str, ApiKeyRequired: bool = None, AuthorizationScopes: List = None, AuthorizationType: str = None, AuthorizerId: str = None, ModelSelectionExpression: str = None, OperationName: str = None, RequestModels: Dict = None, RequestParameters: Dict = None, RouteResponseSelectionExpression: str = None, Target: str = None) -> Dict:
        """
        Creates a Route for an API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/CreateRoute>`_
        
        **Request Syntax**
        ::
          response = client.create_route(
              ApiId='string',
              ApiKeyRequired=True|False,
              AuthorizationScopes=[
                  'string',
              ],
              AuthorizationType='NONE'|'AWS_IAM'|'CUSTOM',
              AuthorizerId='string',
              ModelSelectionExpression='string',
              OperationName='string',
              RequestModels={
                  'string': 'string'
              },
              RequestParameters={
                  'string': {
                      'Required': True|False
                  }
              },
              RouteKey='string',
              RouteResponseSelectionExpression='string',
              Target='string'
          )
        
        **Response Syntax**
        ::
            {
                'ApiKeyRequired': True|False,
                'AuthorizationScopes': [
                    'string',
                ],
                'AuthorizationType': 'NONE'|'AWS_IAM'|'CUSTOM',
                'AuthorizerId': 'string',
                'ModelSelectionExpression': 'string',
                'OperationName': 'string',
                'RequestModels': {
                    'string': 'string'
                },
                'RequestParameters': {
                    'string': {
                        'Required': True|False
                    }
                },
                'RouteId': 'string',
                'RouteKey': 'string',
                'RouteResponseSelectionExpression': 'string',
                'Target': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The request has succeeded and has resulted in the creation of a resource.
            - **ApiKeyRequired** *(boolean) --* 
              Specifies whether an API key is required for this route.
            - **AuthorizationScopes** *(list) --* 
              The authorization scopes supported by this route. 
              - *(string) --* 
                A string with a length between [1-64].
            - **AuthorizationType** *(string) --* 
              The authorization type for the route. Valid values are NONE for open access, AWS_IAM for using AWS IAM permissions.
            - **AuthorizerId** *(string) --* 
              The identifier of the Authorizer resource to be associated with this route.
            - **ModelSelectionExpression** *(string) --* 
              The model selection expression for the route.
            - **OperationName** *(string) --* 
              The operation name for the route.
            - **RequestModels** *(dict) --* 
              The request models for the route.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [1-128].
            - **RequestParameters** *(dict) --* 
              The request parameters for the route.
              - *(string) --* 
                - *(dict) --* 
                  Validation constraints imposed on parameters of a request (path, query string, headers).
                  - **Required** *(boolean) --* 
                    Whether or not the parameter is required.
            - **RouteId** *(string) --* 
              The route ID.
            - **RouteKey** *(string) --* 
              The route key for the route.
            - **RouteResponseSelectionExpression** *(string) --* 
              The route response selection expression for the route.
            - **Target** *(string) --* 
              The target for the route.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type ApiKeyRequired: boolean
        :param ApiKeyRequired:
          Specifies whether an API key is required for the route.
        :type AuthorizationScopes: list
        :param AuthorizationScopes:
          The authorization scopes supported by this route.
          - *(string) --*
            A string with a length between [1-64].
        :type AuthorizationType: string
        :param AuthorizationType:
          The authorization type for the route. Valid values are NONE for open access, AWS_IAM for using AWS IAM permissions.
        :type AuthorizerId: string
        :param AuthorizerId:
          The identifier of the Authorizer resource to be associated with this route.
        :type ModelSelectionExpression: string
        :param ModelSelectionExpression:
          The model selection expression for the route.
        :type OperationName: string
        :param OperationName:
          The operation name for the route.
        :type RequestModels: dict
        :param RequestModels:
          The request models for the route.
          - *(string) --*
            - *(string) --*
              A string with a length between [1-128].
        :type RequestParameters: dict
        :param RequestParameters:
          The request parameters for the route.
          - *(string) --*
            - *(dict) --*
              Validation constraints imposed on parameters of a request (path, query string, headers).
              - **Required** *(boolean) --*
                Whether or not the parameter is required.
        :type RouteKey: string
        :param RouteKey: **[REQUIRED]**
          The route key for the route.
        :type RouteResponseSelectionExpression: string
        :param RouteResponseSelectionExpression:
          The route response selection expression for the route.
        :type Target: string
        :param Target:
          The target for the route.
        :rtype: dict
        :returns:
        """
        pass

    def create_route_response(self, ApiId: str, RouteId: str, RouteResponseKey: str, ModelSelectionExpression: str = None, ResponseModels: Dict = None, ResponseParameters: Dict = None) -> Dict:
        """
        Creates a RouteResponse for a Route.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/CreateRouteResponse>`_
        
        **Request Syntax**
        ::
          response = client.create_route_response(
              ApiId='string',
              ModelSelectionExpression='string',
              ResponseModels={
                  'string': 'string'
              },
              ResponseParameters={
                  'string': {
                      'Required': True|False
                  }
              },
              RouteId='string',
              RouteResponseKey='string'
          )
        
        **Response Syntax**
        ::
            {
                'ModelSelectionExpression': 'string',
                'ResponseModels': {
                    'string': 'string'
                },
                'ResponseParameters': {
                    'string': {
                        'Required': True|False
                    }
                },
                'RouteResponseId': 'string',
                'RouteResponseKey': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The request has succeeded and has resulted in the creation of a resource.
            - **ModelSelectionExpression** *(string) --* 
              Represents the model selection expression of a route response.
            - **ResponseModels** *(dict) --* 
              Represents the response models of a route response.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [1-128].
            - **ResponseParameters** *(dict) --* 
              Represents the response parameters of a route response.
              - *(string) --* 
                - *(dict) --* 
                  Validation constraints imposed on parameters of a request (path, query string, headers).
                  - **Required** *(boolean) --* 
                    Whether or not the parameter is required.
            - **RouteResponseId** *(string) --* 
              Represents the identifier of a route response.
            - **RouteResponseKey** *(string) --* 
              Represents the route response key of a route response.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type ModelSelectionExpression: string
        :param ModelSelectionExpression:
          The model selection expression for the route response.
        :type ResponseModels: dict
        :param ResponseModels:
          The response models for the route response.
          - *(string) --*
            - *(string) --*
              A string with a length between [1-128].
        :type ResponseParameters: dict
        :param ResponseParameters:
          The route response parameters.
          - *(string) --*
            - *(dict) --*
              Validation constraints imposed on parameters of a request (path, query string, headers).
              - **Required** *(boolean) --*
                Whether or not the parameter is required.
        :type RouteId: string
        :param RouteId: **[REQUIRED]**
          The route ID.
        :type RouteResponseKey: string
        :param RouteResponseKey: **[REQUIRED]**
          The route response key.
        :rtype: dict
        :returns:
        """
        pass

    def create_stage(self, ApiId: str, StageName: str, AccessLogSettings: Dict = None, ClientCertificateId: str = None, DefaultRouteSettings: Dict = None, DeploymentId: str = None, Description: str = None, RouteSettings: Dict = None, StageVariables: Dict = None) -> Dict:
        """
        Creates a Stage for an API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/CreateStage>`_
        
        **Request Syntax**
        ::
          response = client.create_stage(
              AccessLogSettings={
                  'DestinationArn': 'string',
                  'Format': 'string'
              },
              ApiId='string',
              ClientCertificateId='string',
              DefaultRouteSettings={
                  'DataTraceEnabled': True|False,
                  'DetailedMetricsEnabled': True|False,
                  'LoggingLevel': 'ERROR'|'INFO'|'false',
                  'ThrottlingBurstLimit': 123,
                  'ThrottlingRateLimit': 123.0
              },
              DeploymentId='string',
              Description='string',
              RouteSettings={
                  'string': {
                      'DataTraceEnabled': True|False,
                      'DetailedMetricsEnabled': True|False,
                      'LoggingLevel': 'ERROR'|'INFO'|'false',
                      'ThrottlingBurstLimit': 123,
                      'ThrottlingRateLimit': 123.0
                  }
              },
              StageName='string',
              StageVariables={
                  'string': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'AccessLogSettings': {
                    'DestinationArn': 'string',
                    'Format': 'string'
                },
                'ClientCertificateId': 'string',
                'CreatedDate': datetime(2015, 1, 1),
                'DefaultRouteSettings': {
                    'DataTraceEnabled': True|False,
                    'DetailedMetricsEnabled': True|False,
                    'LoggingLevel': 'ERROR'|'INFO'|'false',
                    'ThrottlingBurstLimit': 123,
                    'ThrottlingRateLimit': 123.0
                },
                'DeploymentId': 'string',
                'Description': 'string',
                'LastUpdatedDate': datetime(2015, 1, 1),
                'RouteSettings': {
                    'string': {
                        'DataTraceEnabled': True|False,
                        'DetailedMetricsEnabled': True|False,
                        'LoggingLevel': 'ERROR'|'INFO'|'false',
                        'ThrottlingBurstLimit': 123,
                        'ThrottlingRateLimit': 123.0
                    }
                },
                'StageName': 'string',
                'StageVariables': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            The request has succeeded and has resulted in the creation of a resource.
            - **AccessLogSettings** *(dict) --* 
              Settings for logging access in this stage.
              - **DestinationArn** *(string) --* 
                The ARN of the CloudWatch Logs log group to receive access logs.
              - **Format** *(string) --* 
                A single line format of the access logs of data, as specified by selected $context variables. The format must include at least $context.requestId.
            - **ClientCertificateId** *(string) --* 
              The identifier of a client certificate for a Stage.
            - **CreatedDate** *(datetime) --* 
              The timestamp when the stage was created.
            - **DefaultRouteSettings** *(dict) --* 
              Default route settings for the stage.
              - **DataTraceEnabled** *(boolean) --* 
                Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs.
              - **DetailedMetricsEnabled** *(boolean) --* 
                Specifies whether detailed metrics are enabled.
              - **LoggingLevel** *(string) --* 
                Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the log entries pushed to Amazon CloudWatch Logs.
              - **ThrottlingBurstLimit** *(integer) --* 
                Specifies the throttling burst limit.
              - **ThrottlingRateLimit** *(float) --* 
                Specifies the throttling rate limit.
            - **DeploymentId** *(string) --* 
              The identifier of the Deployment that the Stage is associated with.
            - **Description** *(string) --* 
              The description of the stage.
            - **LastUpdatedDate** *(datetime) --* 
              The timestamp when the stage was last updated.
            - **RouteSettings** *(dict) --* 
              Route settings for the stage.
              - *(string) --* 
                - *(dict) --* 
                  Represents a collection of route settings.
                  - **DataTraceEnabled** *(boolean) --* 
                    Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs.
                  - **DetailedMetricsEnabled** *(boolean) --* 
                    Specifies whether detailed metrics are enabled.
                  - **LoggingLevel** *(string) --* 
                    Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the log entries pushed to Amazon CloudWatch Logs.
                  - **ThrottlingBurstLimit** *(integer) --* 
                    Specifies the throttling burst limit.
                  - **ThrottlingRateLimit** *(float) --* 
                    Specifies the throttling rate limit.
            - **StageName** *(string) --* 
              The name of the stage.
            - **StageVariables** *(dict) --* 
              A map that defines the stage variables for a stage resource. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [0-2048].
        :type AccessLogSettings: dict
        :param AccessLogSettings:
          Settings for logging access in this stage.
          - **DestinationArn** *(string) --*
            The ARN of the CloudWatch Logs log group to receive access logs.
          - **Format** *(string) --*
            A single line format of the access logs of data, as specified by selected $context variables. The format must include at least $context.requestId.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type ClientCertificateId: string
        :param ClientCertificateId:
          The identifier of a client certificate for a Stage.
        :type DefaultRouteSettings: dict
        :param DefaultRouteSettings:
          The default route settings for the stage.
          - **DataTraceEnabled** *(boolean) --*
            Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs.
          - **DetailedMetricsEnabled** *(boolean) --*
            Specifies whether detailed metrics are enabled.
          - **LoggingLevel** *(string) --*
            Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the log entries pushed to Amazon CloudWatch Logs.
          - **ThrottlingBurstLimit** *(integer) --*
            Specifies the throttling burst limit.
          - **ThrottlingRateLimit** *(float) --*
            Specifies the throttling rate limit.
        :type DeploymentId: string
        :param DeploymentId:
          The deployment identifier of the API stage.
        :type Description: string
        :param Description:
          The description for the API stage.
        :type RouteSettings: dict
        :param RouteSettings:
          Route settings for the stage.
          - *(string) --*
            - *(dict) --*
              Represents a collection of route settings.
              - **DataTraceEnabled** *(boolean) --*
                Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs.
              - **DetailedMetricsEnabled** *(boolean) --*
                Specifies whether detailed metrics are enabled.
              - **LoggingLevel** *(string) --*
                Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the log entries pushed to Amazon CloudWatch Logs.
              - **ThrottlingBurstLimit** *(integer) --*
                Specifies the throttling burst limit.
              - **ThrottlingRateLimit** *(float) --*
                Specifies the throttling rate limit.
        :type StageName: string
        :param StageName: **[REQUIRED]**
          The name of the stage.
        :type StageVariables: dict
        :param StageVariables:
          A map that defines the stage variables for a Stage. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.
          - *(string) --*
            - *(string) --*
              A string with a length between [0-2048].
        :rtype: dict
        :returns:
        """
        pass

    def delete_api(self, ApiId: str):
        """
        Deletes an Api resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/DeleteApi>`_
        
        **Request Syntax**
        ::
          response = client.delete_api(
              ApiId='string'
          )
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :returns: None
        """
        pass

    def delete_api_mapping(self, ApiId: str, ApiMappingId: str, DomainName: str):
        """
        Deletes an API mapping.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/DeleteApiMapping>`_
        
        **Request Syntax**
        ::
          response = client.delete_api_mapping(
              ApiId='string',
              ApiMappingId='string',
              DomainName='string'
          )
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The identifier of the API.
        :type ApiMappingId: string
        :param ApiMappingId: **[REQUIRED]**
          The API mapping identifier.
        :type DomainName: string
        :param DomainName: **[REQUIRED]**
          The domain name.
        :returns: None
        """
        pass

    def delete_authorizer(self, ApiId: str, AuthorizerId: str):
        """
        Deletes an Authorizer.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/DeleteAuthorizer>`_
        
        **Request Syntax**
        ::
          response = client.delete_authorizer(
              ApiId='string',
              AuthorizerId='string'
          )
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type AuthorizerId: string
        :param AuthorizerId: **[REQUIRED]**
          The authorizer identifier.
        :returns: None
        """
        pass

    def delete_deployment(self, ApiId: str, DeploymentId: str):
        """
        Deletes a Deployment.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/DeleteDeployment>`_
        
        **Request Syntax**
        ::
          response = client.delete_deployment(
              ApiId='string',
              DeploymentId='string'
          )
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type DeploymentId: string
        :param DeploymentId: **[REQUIRED]**
          The deployment ID.
        :returns: None
        """
        pass

    def delete_domain_name(self, DomainName: str):
        """
        Deletes a domain name.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/DeleteDomainName>`_
        
        **Request Syntax**
        ::
          response = client.delete_domain_name(
              DomainName='string'
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]**
          The domain name.
        :returns: None
        """
        pass

    def delete_integration(self, ApiId: str, IntegrationId: str):
        """
        Deletes an Integration.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/DeleteIntegration>`_
        
        **Request Syntax**
        ::
          response = client.delete_integration(
              ApiId='string',
              IntegrationId='string'
          )
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type IntegrationId: string
        :param IntegrationId: **[REQUIRED]**
          The integration ID.
        :returns: None
        """
        pass

    def delete_integration_response(self, ApiId: str, IntegrationId: str, IntegrationResponseId: str):
        """
        Deletes an IntegrationResponses.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/DeleteIntegrationResponse>`_
        
        **Request Syntax**
        ::
          response = client.delete_integration_response(
              ApiId='string',
              IntegrationId='string',
              IntegrationResponseId='string'
          )
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type IntegrationId: string
        :param IntegrationId: **[REQUIRED]**
          The integration ID.
        :type IntegrationResponseId: string
        :param IntegrationResponseId: **[REQUIRED]**
          The integration response ID.
        :returns: None
        """
        pass

    def delete_model(self, ApiId: str, ModelId: str):
        """
        Deletes a Model.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/DeleteModel>`_
        
        **Request Syntax**
        ::
          response = client.delete_model(
              ApiId='string',
              ModelId='string'
          )
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type ModelId: string
        :param ModelId: **[REQUIRED]**
          The model ID.
        :returns: None
        """
        pass

    def delete_route(self, ApiId: str, RouteId: str):
        """
        Deletes a Route.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/DeleteRoute>`_
        
        **Request Syntax**
        ::
          response = client.delete_route(
              ApiId='string',
              RouteId='string'
          )
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type RouteId: string
        :param RouteId: **[REQUIRED]**
          The route ID.
        :returns: None
        """
        pass

    def delete_route_response(self, ApiId: str, RouteId: str, RouteResponseId: str):
        """
        Deletes a RouteResponse.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/DeleteRouteResponse>`_
        
        **Request Syntax**
        ::
          response = client.delete_route_response(
              ApiId='string',
              RouteId='string',
              RouteResponseId='string'
          )
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type RouteId: string
        :param RouteId: **[REQUIRED]**
          The route ID.
        :type RouteResponseId: string
        :param RouteResponseId: **[REQUIRED]**
          The route response ID.
        :returns: None
        """
        pass

    def delete_stage(self, ApiId: str, StageName: str):
        """
        Deletes a Stage.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/DeleteStage>`_
        
        **Request Syntax**
        ::
          response = client.delete_stage(
              ApiId='string',
              StageName='string'
          )
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type StageName: string
        :param StageName: **[REQUIRED]**
          The stage name.
        :returns: None
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

    def get_api(self, ApiId: str) -> Dict:
        """
        Gets an Api resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetApi>`_
        
        **Request Syntax**
        ::
          response = client.get_api(
              ApiId='string'
          )
        
        **Response Syntax**
        ::
            {
                'ApiEndpoint': 'string',
                'ApiId': 'string',
                'ApiKeySelectionExpression': 'string',
                'CreatedDate': datetime(2015, 1, 1),
                'Description': 'string',
                'DisableSchemaValidation': True|False,
                'Name': 'string',
                'ProtocolType': 'WEBSOCKET',
                'RouteSelectionExpression': 'string',
                'Version': 'string',
                'Warnings': [
                    'string',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **ApiEndpoint** *(string) --* 
              The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name is typically appended to this URI to form a complete path to a deployed API stage.
            - **ApiId** *(string) --* 
              The API ID.
            - **ApiKeySelectionExpression** *(string) --* 
              An API key selection expression. See `API Key Selection Expressions <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions>`__ .
            - **CreatedDate** *(datetime) --* 
              The timestamp when the API was created.
            - **Description** *(string) --* 
              The description of the API.
            - **DisableSchemaValidation** *(boolean) --* 
              Avoid validating models when creating a deployment.
            - **Name** *(string) --* 
              The name of the API.
            - **ProtocolType** *(string) --* 
              The API protocol: HTTP or WEBSOCKET.
            - **RouteSelectionExpression** *(string) --* 
              The route selection expression for the API.
            - **Version** *(string) --* 
              A version identifier for the API.
            - **Warnings** *(list) --* 
              The warning messages reported when failonwarnings is turned on during API import.
              - *(string) --* 
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :rtype: dict
        :returns:
        """
        pass

    def get_api_mapping(self, ApiId: str, ApiMappingId: str, DomainName: str) -> Dict:
        """
        The API mapping.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetApiMapping>`_
        
        **Request Syntax**
        ::
          response = client.get_api_mapping(
              ApiId='string',
              ApiMappingId='string',
              DomainName='string'
          )
        
        **Response Syntax**
        ::
            {
                'ApiId': 'string',
                'ApiMappingId': 'string',
                'ApiMappingKey': 'string',
                'Stage': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **ApiId** *(string) --* 
              The API identifier.
            - **ApiMappingId** *(string) --* 
              The API mapping identifier.
            - **ApiMappingKey** *(string) --* 
              The API mapping key.
            - **Stage** *(string) --* 
              The API stage.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The identifier of the API.
        :type ApiMappingId: string
        :param ApiMappingId: **[REQUIRED]**
          The API mapping identifier.
        :type DomainName: string
        :param DomainName: **[REQUIRED]**
          The domain name.
        :rtype: dict
        :returns:
        """
        pass

    def get_api_mappings(self, DomainName: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        The API mappings.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetApiMappings>`_
        
        **Request Syntax**
        ::
          response = client.get_api_mappings(
              DomainName='string',
              MaxResults='string',
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'ApiId': 'string',
                'ApiMappingId': 'string',
                'ApiMappingKey': 'string',
                'Stage': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **ApiId** *(string) --* 
              The API identifier.
            - **ApiMappingId** *(string) --* 
              The API mapping identifier.
            - **ApiMappingKey** *(string) --* 
              The API mapping key.
            - **Stage** *(string) --* 
              The API stage.
        :type DomainName: string
        :param DomainName: **[REQUIRED]**
          The domain name.
        :type MaxResults: string
        :param MaxResults:
          The maximum number of elements to be returned for this resource.
        :type NextToken: string
        :param NextToken:
          The next page of elements from this collection. Not valid for the last element of the collection.
        :rtype: dict
        :returns:
        """
        pass

    def get_apis(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        Gets a collection of Api resources.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetApis>`_
        
        **Request Syntax**
        ::
          response = client.get_apis(
              MaxResults='string',
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Items': [
                    {
                        'ApiEndpoint': 'string',
                        'ApiId': 'string',
                        'ApiKeySelectionExpression': 'string',
                        'CreatedDate': datetime(2015, 1, 1),
                        'Description': 'string',
                        'DisableSchemaValidation': True|False,
                        'Name': 'string',
                        'ProtocolType': 'WEBSOCKET',
                        'RouteSelectionExpression': 'string',
                        'Version': 'string',
                        'Warnings': [
                            'string',
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **Items** *(list) --* 
              The elements from this collection.
              - *(dict) --* 
                Represents an API.
                - **ApiEndpoint** *(string) --* 
                  The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name is typically appended to this URI to form a complete path to a deployed API stage.
                - **ApiId** *(string) --* 
                  The API ID.
                - **ApiKeySelectionExpression** *(string) --* 
                  An API key selection expression. See `API Key Selection Expressions <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions>`__ .
                - **CreatedDate** *(datetime) --* 
                  The timestamp when the API was created.
                - **Description** *(string) --* 
                  The description of the API.
                - **DisableSchemaValidation** *(boolean) --* 
                  Avoid validating models when creating a deployment.
                - **Name** *(string) --* 
                  The name of the API.
                - **ProtocolType** *(string) --* 
                  The API protocol: HTTP or WEBSOCKET.
                - **RouteSelectionExpression** *(string) --* 
                  The route selection expression for the API.
                - **Version** *(string) --* 
                  A version identifier for the API.
                - **Warnings** *(list) --* 
                  The warning messages reported when failonwarnings is turned on during API import.
                  - *(string) --* 
            - **NextToken** *(string) --* 
              The next page of elements from this collection. Not valid for the last element of the collection.
        :type MaxResults: string
        :param MaxResults:
          The maximum number of elements to be returned for this resource.
        :type NextToken: string
        :param NextToken:
          The next page of elements from this collection. Not valid for the last element of the collection.
        :rtype: dict
        :returns:
        """
        pass

    def get_authorizer(self, ApiId: str, AuthorizerId: str) -> Dict:
        """
        Gets an Authorizer.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetAuthorizer>`_
        
        **Request Syntax**
        ::
          response = client.get_authorizer(
              ApiId='string',
              AuthorizerId='string'
          )
        
        **Response Syntax**
        ::
            {
                'AuthorizerCredentialsArn': 'string',
                'AuthorizerId': 'string',
                'AuthorizerResultTtlInSeconds': 123,
                'AuthorizerType': 'REQUEST',
                'AuthorizerUri': 'string',
                'IdentitySource': [
                    'string',
                ],
                'IdentityValidationExpression': 'string',
                'Name': 'string',
                'ProviderArns': [
                    'string',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **AuthorizerCredentialsArn** *(string) --* 
              Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.
            - **AuthorizerId** *(string) --* 
              The authorizer identifier.
            - **AuthorizerResultTtlInSeconds** *(integer) --* 
              The time to live (TTL), in seconds, of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, the default value is 300. The maximum value is 3600, or 1 hour.
            - **AuthorizerType** *(string) --* 
              The authorizer type. Currently the only valid value is REQUEST, for a Lambda function using incoming request parameters.
            - **AuthorizerUri** *(string) --* 
              The authorizer's Uniform Resource Identifier (URI). ForREQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations. In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api} , where {region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial /. For Lambda functions, this is usually of the form /2015-03-31/functions/[FunctionARN]/invocations.
            - **IdentitySource** *(list) --* 
              The identity source for which authorization is requested.
              For the REQUEST authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an Auth header and a Name query string parameters are defined as identity sources, this value is method.request.header.Auth, method.request.querystring.Name. These parameters will be used to derive the authorization caching key and to perform runtime validation of the REQUEST authorizer by verifying all of the identity-related request parameters are present, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.
              - *(string) --* 
            - **IdentityValidationExpression** *(string) --* 
              The validation expression does not apply to the REQUEST authorizer.
            - **Name** *(string) --* 
              The name of the authorizer.
            - **ProviderArns** *(list) --* 
              For REQUEST authorizer, this is not defined.
              - *(string) --* 
                Represents an Amazon Resource Name (ARN).
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type AuthorizerId: string
        :param AuthorizerId: **[REQUIRED]**
          The authorizer identifier.
        :rtype: dict
        :returns:
        """
        pass

    def get_authorizers(self, ApiId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        Gets the Authorizers for an API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetAuthorizers>`_
        
        **Request Syntax**
        ::
          response = client.get_authorizers(
              ApiId='string',
              MaxResults='string',
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Items': [
                    {
                        'AuthorizerCredentialsArn': 'string',
                        'AuthorizerId': 'string',
                        'AuthorizerResultTtlInSeconds': 123,
                        'AuthorizerType': 'REQUEST',
                        'AuthorizerUri': 'string',
                        'IdentitySource': [
                            'string',
                        ],
                        'IdentityValidationExpression': 'string',
                        'Name': 'string',
                        'ProviderArns': [
                            'string',
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **Items** *(list) --* 
              The elements from this collection.
              - *(dict) --* 
                Represents an authorizer.
                - **AuthorizerCredentialsArn** *(string) --* 
                  Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.
                - **AuthorizerId** *(string) --* 
                  The authorizer identifier.
                - **AuthorizerResultTtlInSeconds** *(integer) --* 
                  The time to live (TTL), in seconds, of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, the default value is 300. The maximum value is 3600, or 1 hour.
                - **AuthorizerType** *(string) --* 
                  The authorizer type. Currently the only valid value is REQUEST, for a Lambda function using incoming request parameters.
                - **AuthorizerUri** *(string) --* 
                  The authorizer's Uniform Resource Identifier (URI). ForREQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations. In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api} , where {region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial /. For Lambda functions, this is usually of the form /2015-03-31/functions/[FunctionARN]/invocations.
                - **IdentitySource** *(list) --* 
                  The identity source for which authorization is requested.
                  For the REQUEST authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an Auth header and a Name query string parameters are defined as identity sources, this value is method.request.header.Auth, method.request.querystring.Name. These parameters will be used to derive the authorization caching key and to perform runtime validation of the REQUEST authorizer by verifying all of the identity-related request parameters are present, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.
                  - *(string) --* 
                - **IdentityValidationExpression** *(string) --* 
                  The validation expression does not apply to the REQUEST authorizer.
                - **Name** *(string) --* 
                  The name of the authorizer.
                - **ProviderArns** *(list) --* 
                  For REQUEST authorizer, this is not defined.
                  - *(string) --* 
                    Represents an Amazon Resource Name (ARN).
            - **NextToken** *(string) --* 
              The next page of elements from this collection. Not valid for the last element of the collection.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type MaxResults: string
        :param MaxResults:
          The maximum number of elements to be returned for this resource.
        :type NextToken: string
        :param NextToken:
          The next page of elements from this collection. Not valid for the last element of the collection.
        :rtype: dict
        :returns:
        """
        pass

    def get_deployment(self, ApiId: str, DeploymentId: str) -> Dict:
        """
        Gets a Deployment.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetDeployment>`_
        
        **Request Syntax**
        ::
          response = client.get_deployment(
              ApiId='string',
              DeploymentId='string'
          )
        
        **Response Syntax**
        ::
            {
                'CreatedDate': datetime(2015, 1, 1),
                'DeploymentId': 'string',
                'DeploymentStatus': 'PENDING'|'FAILED'|'DEPLOYED',
                'DeploymentStatusMessage': 'string',
                'Description': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **CreatedDate** *(datetime) --* 
              The date and time when the Deployment resource was created.
            - **DeploymentId** *(string) --* 
              The identifier for the deployment.
            - **DeploymentStatus** *(string) --* 
              The status of the deployment: PENDING, FAILED, or SUCCEEDED.
            - **DeploymentStatusMessage** *(string) --* 
              May contain additional feedback on the status of an API deployment.
            - **Description** *(string) --* 
              The description for the deployment.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type DeploymentId: string
        :param DeploymentId: **[REQUIRED]**
          The deployment ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_deployments(self, ApiId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        Gets the Deployments for an API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetDeployments>`_
        
        **Request Syntax**
        ::
          response = client.get_deployments(
              ApiId='string',
              MaxResults='string',
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Items': [
                    {
                        'CreatedDate': datetime(2015, 1, 1),
                        'DeploymentId': 'string',
                        'DeploymentStatus': 'PENDING'|'FAILED'|'DEPLOYED',
                        'DeploymentStatusMessage': 'string',
                        'Description': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **Items** *(list) --* 
              The elements from this collection.
              - *(dict) --* 
                An immutable representation of an API that can be called by users. A Deployment must be associated with a Stage for it to be callable over the internet.
                - **CreatedDate** *(datetime) --* 
                  The date and time when the Deployment resource was created.
                - **DeploymentId** *(string) --* 
                  The identifier for the deployment.
                - **DeploymentStatus** *(string) --* 
                  The status of the deployment: PENDING, FAILED, or SUCCEEDED.
                - **DeploymentStatusMessage** *(string) --* 
                  May contain additional feedback on the status of an API deployment.
                - **Description** *(string) --* 
                  The description for the deployment.
            - **NextToken** *(string) --* 
              The next page of elements from this collection. Not valid for the last element of the collection.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type MaxResults: string
        :param MaxResults:
          The maximum number of elements to be returned for this resource.
        :type NextToken: string
        :param NextToken:
          The next page of elements from this collection. Not valid for the last element of the collection.
        :rtype: dict
        :returns:
        """
        pass

    def get_domain_name(self, DomainName: str) -> Dict:
        """
        Gets a domain name.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetDomainName>`_
        
        **Request Syntax**
        ::
          response = client.get_domain_name(
              DomainName='string'
          )
        
        **Response Syntax**
        ::
            {
                'ApiMappingSelectionExpression': 'string',
                'DomainName': 'string',
                'DomainNameConfigurations': [
                    {
                        'ApiGatewayDomainName': 'string',
                        'CertificateArn': 'string',
                        'CertificateName': 'string',
                        'CertificateUploadDate': datetime(2015, 1, 1),
                        'EndpointType': 'REGIONAL'|'EDGE',
                        'HostedZoneId': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **ApiMappingSelectionExpression** *(string) --* 
              The API mapping selection expression.
            - **DomainName** *(string) --* 
              The name of the DomainName resource.
            - **DomainNameConfigurations** *(list) --* 
              The domain name configurations.
              - *(dict) --* 
                The domain name configuration.
                - **ApiGatewayDomainName** *(string) --* 
                  A domain name for the WebSocket API.
                - **CertificateArn** *(string) --* 
                  An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.
                - **CertificateName** *(string) --* 
                  The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.
                - **CertificateUploadDate** *(datetime) --* 
                  The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.
                - **EndpointType** *(string) --* 
                  The endpoint type.
                - **HostedZoneId** *(string) --* 
                  The Amazon Route 53 Hosted Zone ID of the endpoint. See `AWS Regions and Endpoints for API Gateway <docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ .
        :type DomainName: string
        :param DomainName: **[REQUIRED]**
          The domain name.
        :rtype: dict
        :returns:
        """
        pass

    def get_domain_names(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        Gets the domain names for an AWS account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetDomainNames>`_
        
        **Request Syntax**
        ::
          response = client.get_domain_names(
              MaxResults='string',
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Items': [
                    {
                        'ApiMappingSelectionExpression': 'string',
                        'DomainName': 'string',
                        'DomainNameConfigurations': [
                            {
                                'ApiGatewayDomainName': 'string',
                                'CertificateArn': 'string',
                                'CertificateName': 'string',
                                'CertificateUploadDate': datetime(2015, 1, 1),
                                'EndpointType': 'REGIONAL'|'EDGE',
                                'HostedZoneId': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **Items** *(list) --* 
              The elements from this collection.
              - *(dict) --* 
                Represents a domain name.
                - **ApiMappingSelectionExpression** *(string) --* 
                  The API mapping selection expression.
                - **DomainName** *(string) --* 
                  The name of the DomainName resource.
                - **DomainNameConfigurations** *(list) --* 
                  The domain name configurations.
                  - *(dict) --* 
                    The domain name configuration.
                    - **ApiGatewayDomainName** *(string) --* 
                      A domain name for the WebSocket API.
                    - **CertificateArn** *(string) --* 
                      An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.
                    - **CertificateName** *(string) --* 
                      The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.
                    - **CertificateUploadDate** *(datetime) --* 
                      The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.
                    - **EndpointType** *(string) --* 
                      The endpoint type.
                    - **HostedZoneId** *(string) --* 
                      The Amazon Route 53 Hosted Zone ID of the endpoint. See `AWS Regions and Endpoints for API Gateway <docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ .
            - **NextToken** *(string) --* 
              The next page of elements from this collection. Not valid for the last element of the collection.
        :type MaxResults: string
        :param MaxResults:
          The maximum number of elements to be returned for this resource.
        :type NextToken: string
        :param NextToken:
          The next page of elements from this collection. Not valid for the last element of the collection.
        :rtype: dict
        :returns:
        """
        pass

    def get_integration(self, ApiId: str, IntegrationId: str) -> Dict:
        """
        Gets an Integration.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetIntegration>`_
        
        **Request Syntax**
        ::
          response = client.get_integration(
              ApiId='string',
              IntegrationId='string'
          )
        
        **Response Syntax**
        ::
            {
                'ConnectionId': 'string',
                'ConnectionType': 'INTERNET'|'VPC_LINK',
                'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                'CredentialsArn': 'string',
                'Description': 'string',
                'IntegrationId': 'string',
                'IntegrationMethod': 'string',
                'IntegrationResponseSelectionExpression': 'string',
                'IntegrationType': 'AWS'|'HTTP'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                'IntegrationUri': 'string',
                'PassthroughBehavior': 'WHEN_NO_MATCH'|'NEVER'|'WHEN_NO_TEMPLATES',
                'RequestParameters': {
                    'string': 'string'
                },
                'RequestTemplates': {
                    'string': 'string'
                },
                'TemplateSelectionExpression': 'string',
                'TimeoutInMillis': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **ConnectionId** *(string) --* 
              The identifier of the VpcLink used for the integration when the connectionType is VPC_LINK; otherwise undefined.
            - **ConnectionType** *(string) --* 
              The type of the network connection to the integration endpoint. The valid value is INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and a network load balancer in a VPC. The default value is INTERNET.
            - **ContentHandlingStrategy** *(string) --* 
              Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
              CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
              CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
              If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
            - **CredentialsArn** *(string) --* 
              Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, specify null.
            - **Description** *(string) --* 
              Represents the description of an integration.
            - **IntegrationId** *(string) --* 
              Represents the identifier of an integration.
            - **IntegrationMethod** *(string) --* 
              Specifies the integration's HTTP method type.
            - **IntegrationResponseSelectionExpression** *(string) --* 
            - **IntegrationType** *(string) --* 
              The integration type of an integration. One of the following:
              AWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
              AWS_PROXY: for integrating the route or method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as Lambda proxy integration.
              HTTP: for integrating the route or method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
              HTTP_PROXY: for integrating route or method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as HTTP proxy integration.
              MOCK: for integrating the route or method request with API Gateway as a "loopback" endpoint without invoking any backend.
            - **IntegrationUri** *(string) --* 
              Specifies the Uniform Resource Identifier (URI) of the integration endpoint.
              For HTTP or HTTP_PROXY integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the `RFC-3986 specification <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard integration, where connectionType is not VPC_LINK, or private integration, where connectionType is VPC_LINK. For a private HTTP integration, the URI is not used for routing.
              For AWS or AWS_PROXY integrations, the URI is of the form arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}. Here, {Region} is the API Gateway region (e.g., us-east-1); {service} is the name of the integrated AWS service (e.g., s3); and {subdomain} is a designated subdomain supported by certain AWS service for fast host-name lookup. action can be used for an AWS service action-based API, using an Action={name}&{p1}={v1}&p2={v2}... query string. The ensuing {service_api} refers to a supported action {name} plus any required input parameters. Alternatively, path can be used for an AWS service path-based API. The ensuing service_api refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of GetObject, the URI can be either arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key} or arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}
            - **PassthroughBehavior** *(string) --* 
              Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER.
              WHEN_NO_MATCH passes the request body for unmapped content types through to the integration backend without transformation.
              NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.
              WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same HTTP 415 Unsupported Media Type response.
            - **RequestParameters** *(dict) --* 
              A key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.{location}.{name} , where {location} is querystring, path, or header; and {name} must be a valid and unique method request parameter name.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [1-512].
            - **RequestTemplates** *(dict) --* 
              Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [0-32768].
            - **TemplateSelectionExpression** *(string) --* 
              The template selection expression for the integration.
            - **TimeoutInMillis** *(integer) --* 
              Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type IntegrationId: string
        :param IntegrationId: **[REQUIRED]**
          The integration ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_integration_response(self, ApiId: str, IntegrationId: str, IntegrationResponseId: str) -> Dict:
        """
        Gets an IntegrationResponses.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetIntegrationResponse>`_
        
        **Request Syntax**
        ::
          response = client.get_integration_response(
              ApiId='string',
              IntegrationId='string',
              IntegrationResponseId='string'
          )
        
        **Response Syntax**
        ::
            {
                'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                'IntegrationResponseId': 'string',
                'IntegrationResponseKey': 'string',
                'ResponseParameters': {
                    'string': 'string'
                },
                'ResponseTemplates': {
                    'string': 'string'
                },
                'TemplateSelectionExpression': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **ContentHandlingStrategy** *(string) --* 
              Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
              CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
              CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
              If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
            - **IntegrationResponseId** *(string) --* 
              The integration response ID.
            - **IntegrationResponseKey** *(string) --* 
              The integration response key.
            - **ResponseParameters** *(dict) --* 
              A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name}, where name is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name} or integration.response.body.{JSON-expression}, where name is a valid and unique response header name and JSON-expression is a valid JSON expression without the $ prefix.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [1-512].
            - **ResponseTemplates** *(dict) --* 
              The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [0-32768].
            - **TemplateSelectionExpression** *(string) --* 
              The template selection expressions for the integration response.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type IntegrationId: string
        :param IntegrationId: **[REQUIRED]**
          The integration ID.
        :type IntegrationResponseId: string
        :param IntegrationResponseId: **[REQUIRED]**
          The integration response ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_integration_responses(self, ApiId: str, IntegrationId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        Gets the IntegrationResponses for an Integration.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetIntegrationResponses>`_
        
        **Request Syntax**
        ::
          response = client.get_integration_responses(
              ApiId='string',
              IntegrationId='string',
              MaxResults='string',
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Items': [
                    {
                        'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                        'IntegrationResponseId': 'string',
                        'IntegrationResponseKey': 'string',
                        'ResponseParameters': {
                            'string': 'string'
                        },
                        'ResponseTemplates': {
                            'string': 'string'
                        },
                        'TemplateSelectionExpression': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **Items** *(list) --* 
              The elements from this collection.
              - *(dict) --* 
                Represents an integration response.
                - **ContentHandlingStrategy** *(string) --* 
                  Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
                  CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
                  CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
                  If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
                - **IntegrationResponseId** *(string) --* 
                  The integration response ID.
                - **IntegrationResponseKey** *(string) --* 
                  The integration response key.
                - **ResponseParameters** *(dict) --* 
                  A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name}, where name is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name} or integration.response.body.{JSON-expression}, where name is a valid and unique response header name and JSON-expression is a valid JSON expression without the $ prefix.
                  - *(string) --* 
                    - *(string) --* 
                      A string with a length between [1-512].
                - **ResponseTemplates** *(dict) --* 
                  The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.
                  - *(string) --* 
                    - *(string) --* 
                      A string with a length between [0-32768].
                - **TemplateSelectionExpression** *(string) --* 
                  The template selection expressions for the integration response.
            - **NextToken** *(string) --* 
              The next page of elements from this collection. Not valid for the last element of the collection.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type IntegrationId: string
        :param IntegrationId: **[REQUIRED]**
          The integration ID.
        :type MaxResults: string
        :param MaxResults:
          The maximum number of elements to be returned for this resource.
        :type NextToken: string
        :param NextToken:
          The next page of elements from this collection. Not valid for the last element of the collection.
        :rtype: dict
        :returns:
        """
        pass

    def get_integrations(self, ApiId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        Gets the Integrations for an API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetIntegrations>`_
        
        **Request Syntax**
        ::
          response = client.get_integrations(
              ApiId='string',
              MaxResults='string',
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Items': [
                    {
                        'ConnectionId': 'string',
                        'ConnectionType': 'INTERNET'|'VPC_LINK',
                        'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                        'CredentialsArn': 'string',
                        'Description': 'string',
                        'IntegrationId': 'string',
                        'IntegrationMethod': 'string',
                        'IntegrationResponseSelectionExpression': 'string',
                        'IntegrationType': 'AWS'|'HTTP'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                        'IntegrationUri': 'string',
                        'PassthroughBehavior': 'WHEN_NO_MATCH'|'NEVER'|'WHEN_NO_TEMPLATES',
                        'RequestParameters': {
                            'string': 'string'
                        },
                        'RequestTemplates': {
                            'string': 'string'
                        },
                        'TemplateSelectionExpression': 'string',
                        'TimeoutInMillis': 123
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **Items** *(list) --* 
              The elements from this collection.
              - *(dict) --* 
                Represents an integration.
                - **ConnectionId** *(string) --* 
                  The identifier of the VpcLink used for the integration when the connectionType is VPC_LINK; otherwise undefined.
                - **ConnectionType** *(string) --* 
                  The type of the network connection to the integration endpoint. The valid value is INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and a network load balancer in a VPC. The default value is INTERNET.
                - **ContentHandlingStrategy** *(string) --* 
                  Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
                  CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
                  CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
                  If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
                - **CredentialsArn** *(string) --* 
                  Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, specify null.
                - **Description** *(string) --* 
                  Represents the description of an integration.
                - **IntegrationId** *(string) --* 
                  Represents the identifier of an integration.
                - **IntegrationMethod** *(string) --* 
                  Specifies the integration's HTTP method type.
                - **IntegrationResponseSelectionExpression** *(string) --* 
                - **IntegrationType** *(string) --* 
                  The integration type of an integration. One of the following:
                  AWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
                  AWS_PROXY: for integrating the route or method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as Lambda proxy integration.
                  HTTP: for integrating the route or method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
                  HTTP_PROXY: for integrating route or method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as HTTP proxy integration.
                  MOCK: for integrating the route or method request with API Gateway as a "loopback" endpoint without invoking any backend.
                - **IntegrationUri** *(string) --* 
                  Specifies the Uniform Resource Identifier (URI) of the integration endpoint.
                  For HTTP or HTTP_PROXY integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the `RFC-3986 specification <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard integration, where connectionType is not VPC_LINK, or private integration, where connectionType is VPC_LINK. For a private HTTP integration, the URI is not used for routing.
                  For AWS or AWS_PROXY integrations, the URI is of the form arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}. Here, {Region} is the API Gateway region (e.g., us-east-1); {service} is the name of the integrated AWS service (e.g., s3); and {subdomain} is a designated subdomain supported by certain AWS service for fast host-name lookup. action can be used for an AWS service action-based API, using an Action={name}&{p1}={v1}&p2={v2}... query string. The ensuing {service_api} refers to a supported action {name} plus any required input parameters. Alternatively, path can be used for an AWS service path-based API. The ensuing service_api refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of GetObject, the URI can be either arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key} or arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}
                - **PassthroughBehavior** *(string) --* 
                  Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER.
                  WHEN_NO_MATCH passes the request body for unmapped content types through to the integration backend without transformation.
                  NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.
                  WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same HTTP 415 Unsupported Media Type response.
                - **RequestParameters** *(dict) --* 
                  A key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.{location}.{name} , where {location} is querystring, path, or header; and {name} must be a valid and unique method request parameter name.
                  - *(string) --* 
                    - *(string) --* 
                      A string with a length between [1-512].
                - **RequestTemplates** *(dict) --* 
                  Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.
                  - *(string) --* 
                    - *(string) --* 
                      A string with a length between [0-32768].
                - **TemplateSelectionExpression** *(string) --* 
                  The template selection expression for the integration.
                - **TimeoutInMillis** *(integer) --* 
                  Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.
            - **NextToken** *(string) --* 
              The next page of elements from this collection. Not valid for the last element of the collection.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type MaxResults: string
        :param MaxResults:
          The maximum number of elements to be returned for this resource.
        :type NextToken: string
        :param NextToken:
          The next page of elements from this collection. Not valid for the last element of the collection.
        :rtype: dict
        :returns:
        """
        pass

    def get_model(self, ApiId: str, ModelId: str) -> Dict:
        """
        Gets a Model.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetModel>`_
        
        **Request Syntax**
        ::
          response = client.get_model(
              ApiId='string',
              ModelId='string'
          )
        
        **Response Syntax**
        ::
            {
                'ContentType': 'string',
                'Description': 'string',
                'ModelId': 'string',
                'Name': 'string',
                'Schema': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **ContentType** *(string) --* 
              The content-type for the model, for example, "application/json".
            - **Description** *(string) --* 
              The description of the model.
            - **ModelId** *(string) --* 
              The model identifier.
            - **Name** *(string) --* 
              The name of the model. Must be alphanumeric.
            - **Schema** *(string) --* 
              The schema for the model. For application/json models, this should be JSON schema draft 4 model.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type ModelId: string
        :param ModelId: **[REQUIRED]**
          The model ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_model_template(self, ApiId: str, ModelId: str) -> Dict:
        """
        Gets a model template.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetModelTemplate>`_
        
        **Request Syntax**
        ::
          response = client.get_model_template(
              ApiId='string',
              ModelId='string'
          )
        
        **Response Syntax**
        ::
            {
                'Value': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **Value** *(string) --* 
              The template value.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type ModelId: string
        :param ModelId: **[REQUIRED]**
          The model ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_models(self, ApiId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        Gets the Models for an API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetModels>`_
        
        **Request Syntax**
        ::
          response = client.get_models(
              ApiId='string',
              MaxResults='string',
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Items': [
                    {
                        'ContentType': 'string',
                        'Description': 'string',
                        'ModelId': 'string',
                        'Name': 'string',
                        'Schema': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **Items** *(list) --* 
              The elements from this collection.
              - *(dict) --* 
                Represents a data model for an API. See `Create Models and Mapping Templates for Request and Response Mappings <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__ .
                - **ContentType** *(string) --* 
                  The content-type for the model, for example, "application/json".
                - **Description** *(string) --* 
                  The description of the model.
                - **ModelId** *(string) --* 
                  The model identifier.
                - **Name** *(string) --* 
                  The name of the model. Must be alphanumeric.
                - **Schema** *(string) --* 
                  The schema for the model. For application/json models, this should be JSON schema draft 4 model.
            - **NextToken** *(string) --* 
              The next page of elements from this collection. Not valid for the last element of the collection.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type MaxResults: string
        :param MaxResults:
          The maximum number of elements to be returned for this resource.
        :type NextToken: string
        :param NextToken:
          The next page of elements from this collection. Not valid for the last element of the collection.
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

    def get_route(self, ApiId: str, RouteId: str) -> Dict:
        """
        Gets a Route.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetRoute>`_
        
        **Request Syntax**
        ::
          response = client.get_route(
              ApiId='string',
              RouteId='string'
          )
        
        **Response Syntax**
        ::
            {
                'ApiKeyRequired': True|False,
                'AuthorizationScopes': [
                    'string',
                ],
                'AuthorizationType': 'NONE'|'AWS_IAM'|'CUSTOM',
                'AuthorizerId': 'string',
                'ModelSelectionExpression': 'string',
                'OperationName': 'string',
                'RequestModels': {
                    'string': 'string'
                },
                'RequestParameters': {
                    'string': {
                        'Required': True|False
                    }
                },
                'RouteId': 'string',
                'RouteKey': 'string',
                'RouteResponseSelectionExpression': 'string',
                'Target': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **ApiKeyRequired** *(boolean) --* 
              Specifies whether an API key is required for this route.
            - **AuthorizationScopes** *(list) --* 
              The authorization scopes supported by this route. 
              - *(string) --* 
                A string with a length between [1-64].
            - **AuthorizationType** *(string) --* 
              The authorization type for the route. Valid values are NONE for open access, AWS_IAM for using AWS IAM permissions.
            - **AuthorizerId** *(string) --* 
              The identifier of the Authorizer resource to be associated with this route.
            - **ModelSelectionExpression** *(string) --* 
              The model selection expression for the route.
            - **OperationName** *(string) --* 
              The operation name for the route.
            - **RequestModels** *(dict) --* 
              The request models for the route.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [1-128].
            - **RequestParameters** *(dict) --* 
              The request parameters for the route.
              - *(string) --* 
                - *(dict) --* 
                  Validation constraints imposed on parameters of a request (path, query string, headers).
                  - **Required** *(boolean) --* 
                    Whether or not the parameter is required.
            - **RouteId** *(string) --* 
              The route ID.
            - **RouteKey** *(string) --* 
              The route key for the route.
            - **RouteResponseSelectionExpression** *(string) --* 
              The route response selection expression for the route.
            - **Target** *(string) --* 
              The target for the route.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type RouteId: string
        :param RouteId: **[REQUIRED]**
          The route ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_route_response(self, ApiId: str, RouteId: str, RouteResponseId: str) -> Dict:
        """
        Gets a RouteResponse.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetRouteResponse>`_
        
        **Request Syntax**
        ::
          response = client.get_route_response(
              ApiId='string',
              RouteId='string',
              RouteResponseId='string'
          )
        
        **Response Syntax**
        ::
            {
                'ModelSelectionExpression': 'string',
                'ResponseModels': {
                    'string': 'string'
                },
                'ResponseParameters': {
                    'string': {
                        'Required': True|False
                    }
                },
                'RouteResponseId': 'string',
                'RouteResponseKey': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **ModelSelectionExpression** *(string) --* 
              Represents the model selection expression of a route response.
            - **ResponseModels** *(dict) --* 
              Represents the response models of a route response.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [1-128].
            - **ResponseParameters** *(dict) --* 
              Represents the response parameters of a route response.
              - *(string) --* 
                - *(dict) --* 
                  Validation constraints imposed on parameters of a request (path, query string, headers).
                  - **Required** *(boolean) --* 
                    Whether or not the parameter is required.
            - **RouteResponseId** *(string) --* 
              Represents the identifier of a route response.
            - **RouteResponseKey** *(string) --* 
              Represents the route response key of a route response.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type RouteId: string
        :param RouteId: **[REQUIRED]**
          The route ID.
        :type RouteResponseId: string
        :param RouteResponseId: **[REQUIRED]**
          The route response ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_route_responses(self, ApiId: str, RouteId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        Gets the RouteResponses for a Route.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetRouteResponses>`_
        
        **Request Syntax**
        ::
          response = client.get_route_responses(
              ApiId='string',
              MaxResults='string',
              NextToken='string',
              RouteId='string'
          )
        
        **Response Syntax**
        ::
            {
                'Items': [
                    {
                        'ModelSelectionExpression': 'string',
                        'ResponseModels': {
                            'string': 'string'
                        },
                        'ResponseParameters': {
                            'string': {
                                'Required': True|False
                            }
                        },
                        'RouteResponseId': 'string',
                        'RouteResponseKey': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **Items** *(list) --* 
              The elements from this collection.
              - *(dict) --* 
                Represents a route response.
                - **ModelSelectionExpression** *(string) --* 
                  Represents the model selection expression of a route response.
                - **ResponseModels** *(dict) --* 
                  Represents the response models of a route response.
                  - *(string) --* 
                    - *(string) --* 
                      A string with a length between [1-128].
                - **ResponseParameters** *(dict) --* 
                  Represents the response parameters of a route response.
                  - *(string) --* 
                    - *(dict) --* 
                      Validation constraints imposed on parameters of a request (path, query string, headers).
                      - **Required** *(boolean) --* 
                        Whether or not the parameter is required.
                - **RouteResponseId** *(string) --* 
                  Represents the identifier of a route response.
                - **RouteResponseKey** *(string) --* 
                  Represents the route response key of a route response.
            - **NextToken** *(string) --* 
              The next page of elements from this collection. Not valid for the last element of the collection.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type MaxResults: string
        :param MaxResults:
          The maximum number of elements to be returned for this resource.
        :type NextToken: string
        :param NextToken:
          The next page of elements from this collection. Not valid for the last element of the collection.
        :type RouteId: string
        :param RouteId: **[REQUIRED]**
          The route ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_routes(self, ApiId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        Gets the Routes for an API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetRoutes>`_
        
        **Request Syntax**
        ::
          response = client.get_routes(
              ApiId='string',
              MaxResults='string',
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Items': [
                    {
                        'ApiKeyRequired': True|False,
                        'AuthorizationScopes': [
                            'string',
                        ],
                        'AuthorizationType': 'NONE'|'AWS_IAM'|'CUSTOM',
                        'AuthorizerId': 'string',
                        'ModelSelectionExpression': 'string',
                        'OperationName': 'string',
                        'RequestModels': {
                            'string': 'string'
                        },
                        'RequestParameters': {
                            'string': {
                                'Required': True|False
                            }
                        },
                        'RouteId': 'string',
                        'RouteKey': 'string',
                        'RouteResponseSelectionExpression': 'string',
                        'Target': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **Items** *(list) --* 
              The elements from this collection.
              - *(dict) --* 
                Represents a route.
                - **ApiKeyRequired** *(boolean) --* 
                  Specifies whether an API key is required for this route.
                - **AuthorizationScopes** *(list) --* 
                  The authorization scopes supported by this route. 
                  - *(string) --* 
                    A string with a length between [1-64].
                - **AuthorizationType** *(string) --* 
                  The authorization type for the route. Valid values are NONE for open access, AWS_IAM for using AWS IAM permissions.
                - **AuthorizerId** *(string) --* 
                  The identifier of the Authorizer resource to be associated with this route.
                - **ModelSelectionExpression** *(string) --* 
                  The model selection expression for the route.
                - **OperationName** *(string) --* 
                  The operation name for the route.
                - **RequestModels** *(dict) --* 
                  The request models for the route.
                  - *(string) --* 
                    - *(string) --* 
                      A string with a length between [1-128].
                - **RequestParameters** *(dict) --* 
                  The request parameters for the route.
                  - *(string) --* 
                    - *(dict) --* 
                      Validation constraints imposed on parameters of a request (path, query string, headers).
                      - **Required** *(boolean) --* 
                        Whether or not the parameter is required.
                - **RouteId** *(string) --* 
                  The route ID.
                - **RouteKey** *(string) --* 
                  The route key for the route.
                - **RouteResponseSelectionExpression** *(string) --* 
                  The route response selection expression for the route.
                - **Target** *(string) --* 
                  The target for the route.
            - **NextToken** *(string) --* 
              The next page of elements from this collection. Not valid for the last element of the collection.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type MaxResults: string
        :param MaxResults:
          The maximum number of elements to be returned for this resource.
        :type NextToken: string
        :param NextToken:
          The next page of elements from this collection. Not valid for the last element of the collection.
        :rtype: dict
        :returns:
        """
        pass

    def get_stage(self, ApiId: str, StageName: str) -> Dict:
        """
        Gets a Stage.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetStage>`_
        
        **Request Syntax**
        ::
          response = client.get_stage(
              ApiId='string',
              StageName='string'
          )
        
        **Response Syntax**
        ::
            {
                'AccessLogSettings': {
                    'DestinationArn': 'string',
                    'Format': 'string'
                },
                'ClientCertificateId': 'string',
                'CreatedDate': datetime(2015, 1, 1),
                'DefaultRouteSettings': {
                    'DataTraceEnabled': True|False,
                    'DetailedMetricsEnabled': True|False,
                    'LoggingLevel': 'ERROR'|'INFO'|'false',
                    'ThrottlingBurstLimit': 123,
                    'ThrottlingRateLimit': 123.0
                },
                'DeploymentId': 'string',
                'Description': 'string',
                'LastUpdatedDate': datetime(2015, 1, 1),
                'RouteSettings': {
                    'string': {
                        'DataTraceEnabled': True|False,
                        'DetailedMetricsEnabled': True|False,
                        'LoggingLevel': 'ERROR'|'INFO'|'false',
                        'ThrottlingBurstLimit': 123,
                        'ThrottlingRateLimit': 123.0
                    }
                },
                'StageName': 'string',
                'StageVariables': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **AccessLogSettings** *(dict) --* 
              Settings for logging access in this stage.
              - **DestinationArn** *(string) --* 
                The ARN of the CloudWatch Logs log group to receive access logs.
              - **Format** *(string) --* 
                A single line format of the access logs of data, as specified by selected $context variables. The format must include at least $context.requestId.
            - **ClientCertificateId** *(string) --* 
              The identifier of a client certificate for a Stage.
            - **CreatedDate** *(datetime) --* 
              The timestamp when the stage was created.
            - **DefaultRouteSettings** *(dict) --* 
              Default route settings for the stage.
              - **DataTraceEnabled** *(boolean) --* 
                Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs.
              - **DetailedMetricsEnabled** *(boolean) --* 
                Specifies whether detailed metrics are enabled.
              - **LoggingLevel** *(string) --* 
                Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the log entries pushed to Amazon CloudWatch Logs.
              - **ThrottlingBurstLimit** *(integer) --* 
                Specifies the throttling burst limit.
              - **ThrottlingRateLimit** *(float) --* 
                Specifies the throttling rate limit.
            - **DeploymentId** *(string) --* 
              The identifier of the Deployment that the Stage is associated with.
            - **Description** *(string) --* 
              The description of the stage.
            - **LastUpdatedDate** *(datetime) --* 
              The timestamp when the stage was last updated.
            - **RouteSettings** *(dict) --* 
              Route settings for the stage.
              - *(string) --* 
                - *(dict) --* 
                  Represents a collection of route settings.
                  - **DataTraceEnabled** *(boolean) --* 
                    Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs.
                  - **DetailedMetricsEnabled** *(boolean) --* 
                    Specifies whether detailed metrics are enabled.
                  - **LoggingLevel** *(string) --* 
                    Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the log entries pushed to Amazon CloudWatch Logs.
                  - **ThrottlingBurstLimit** *(integer) --* 
                    Specifies the throttling burst limit.
                  - **ThrottlingRateLimit** *(float) --* 
                    Specifies the throttling rate limit.
            - **StageName** *(string) --* 
              The name of the stage.
            - **StageVariables** *(dict) --* 
              A map that defines the stage variables for a stage resource. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [0-2048].
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type StageName: string
        :param StageName: **[REQUIRED]**
          The stage name.
        :rtype: dict
        :returns:
        """
        pass

    def get_stages(self, ApiId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        Gets the Stages for an API.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetStages>`_
        
        **Request Syntax**
        ::
          response = client.get_stages(
              ApiId='string',
              MaxResults='string',
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Items': [
                    {
                        'AccessLogSettings': {
                            'DestinationArn': 'string',
                            'Format': 'string'
                        },
                        'ClientCertificateId': 'string',
                        'CreatedDate': datetime(2015, 1, 1),
                        'DefaultRouteSettings': {
                            'DataTraceEnabled': True|False,
                            'DetailedMetricsEnabled': True|False,
                            'LoggingLevel': 'ERROR'|'INFO'|'false',
                            'ThrottlingBurstLimit': 123,
                            'ThrottlingRateLimit': 123.0
                        },
                        'DeploymentId': 'string',
                        'Description': 'string',
                        'LastUpdatedDate': datetime(2015, 1, 1),
                        'RouteSettings': {
                            'string': {
                                'DataTraceEnabled': True|False,
                                'DetailedMetricsEnabled': True|False,
                                'LoggingLevel': 'ERROR'|'INFO'|'false',
                                'ThrottlingBurstLimit': 123,
                                'ThrottlingRateLimit': 123.0
                            }
                        },
                        'StageName': 'string',
                        'StageVariables': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **Items** *(list) --* 
              The elements from this collection.
              - *(dict) --* 
                Represents an API stage.
                - **AccessLogSettings** *(dict) --* 
                  Settings for logging access in this stage.
                  - **DestinationArn** *(string) --* 
                    The ARN of the CloudWatch Logs log group to receive access logs.
                  - **Format** *(string) --* 
                    A single line format of the access logs of data, as specified by selected $context variables. The format must include at least $context.requestId.
                - **ClientCertificateId** *(string) --* 
                  The identifier of a client certificate for a Stage.
                - **CreatedDate** *(datetime) --* 
                  The timestamp when the stage was created.
                - **DefaultRouteSettings** *(dict) --* 
                  Default route settings for the stage.
                  - **DataTraceEnabled** *(boolean) --* 
                    Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs.
                  - **DetailedMetricsEnabled** *(boolean) --* 
                    Specifies whether detailed metrics are enabled.
                  - **LoggingLevel** *(string) --* 
                    Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the log entries pushed to Amazon CloudWatch Logs.
                  - **ThrottlingBurstLimit** *(integer) --* 
                    Specifies the throttling burst limit.
                  - **ThrottlingRateLimit** *(float) --* 
                    Specifies the throttling rate limit.
                - **DeploymentId** *(string) --* 
                  The identifier of the Deployment that the Stage is associated with.
                - **Description** *(string) --* 
                  The description of the stage.
                - **LastUpdatedDate** *(datetime) --* 
                  The timestamp when the stage was last updated.
                - **RouteSettings** *(dict) --* 
                  Route settings for the stage.
                  - *(string) --* 
                    - *(dict) --* 
                      Represents a collection of route settings.
                      - **DataTraceEnabled** *(boolean) --* 
                        Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs.
                      - **DetailedMetricsEnabled** *(boolean) --* 
                        Specifies whether detailed metrics are enabled.
                      - **LoggingLevel** *(string) --* 
                        Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the log entries pushed to Amazon CloudWatch Logs.
                      - **ThrottlingBurstLimit** *(integer) --* 
                        Specifies the throttling burst limit.
                      - **ThrottlingRateLimit** *(float) --* 
                        Specifies the throttling rate limit.
                - **StageName** *(string) --* 
                  The name of the stage.
                - **StageVariables** *(dict) --* 
                  A map that defines the stage variables for a stage resource. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.
                  - *(string) --* 
                    - *(string) --* 
                      A string with a length between [0-2048].
            - **NextToken** *(string) --* 
              The next page of elements from this collection. Not valid for the last element of the collection.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type MaxResults: string
        :param MaxResults:
          The maximum number of elements to be returned for this resource.
        :type NextToken: string
        :param NextToken:
          The next page of elements from this collection. Not valid for the last element of the collection.
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

    def update_api(self, ApiId: str, ApiKeySelectionExpression: str = None, Description: str = None, DisableSchemaValidation: bool = None, Name: str = None, RouteSelectionExpression: str = None, Version: str = None) -> Dict:
        """
        Updates an Api resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/UpdateApi>`_
        
        **Request Syntax**
        ::
          response = client.update_api(
              ApiId='string',
              ApiKeySelectionExpression='string',
              Description='string',
              DisableSchemaValidation=True|False,
              Name='string',
              RouteSelectionExpression='string',
              Version='string'
          )
        
        **Response Syntax**
        ::
            {
                'ApiEndpoint': 'string',
                'ApiId': 'string',
                'ApiKeySelectionExpression': 'string',
                'CreatedDate': datetime(2015, 1, 1),
                'Description': 'string',
                'DisableSchemaValidation': True|False,
                'Name': 'string',
                'ProtocolType': 'WEBSOCKET',
                'RouteSelectionExpression': 'string',
                'Version': 'string',
                'Warnings': [
                    'string',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **ApiEndpoint** *(string) --* 
              The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name is typically appended to this URI to form a complete path to a deployed API stage.
            - **ApiId** *(string) --* 
              The API ID.
            - **ApiKeySelectionExpression** *(string) --* 
              An API key selection expression. See `API Key Selection Expressions <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions>`__ .
            - **CreatedDate** *(datetime) --* 
              The timestamp when the API was created.
            - **Description** *(string) --* 
              The description of the API.
            - **DisableSchemaValidation** *(boolean) --* 
              Avoid validating models when creating a deployment.
            - **Name** *(string) --* 
              The name of the API.
            - **ProtocolType** *(string) --* 
              The API protocol: HTTP or WEBSOCKET.
            - **RouteSelectionExpression** *(string) --* 
              The route selection expression for the API.
            - **Version** *(string) --* 
              A version identifier for the API.
            - **Warnings** *(list) --* 
              The warning messages reported when failonwarnings is turned on during API import.
              - *(string) --* 
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type ApiKeySelectionExpression: string
        :param ApiKeySelectionExpression:
          An API key selection expression. See `API Key Selection Expressions <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions>`__ .
        :type Description: string
        :param Description:
          The description of the API.
        :type DisableSchemaValidation: boolean
        :param DisableSchemaValidation:
          Avoid validating models when creating a deployment.
        :type Name: string
        :param Name:
          The name of the API.
        :type RouteSelectionExpression: string
        :param RouteSelectionExpression:
          The route selection expression for the API.
        :type Version: string
        :param Version:
          A version identifier for the API.
        :rtype: dict
        :returns:
        """
        pass

    def update_api_mapping(self, ApiId: str, ApiMappingId: str, DomainName: str, ApiMappingKey: str = None, Stage: str = None) -> Dict:
        """
        The API mapping.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/UpdateApiMapping>`_
        
        **Request Syntax**
        ::
          response = client.update_api_mapping(
              ApiId='string',
              ApiMappingId='string',
              ApiMappingKey='string',
              DomainName='string',
              Stage='string'
          )
        
        **Response Syntax**
        ::
            {
                'ApiId': 'string',
                'ApiMappingId': 'string',
                'ApiMappingKey': 'string',
                'Stage': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **ApiId** *(string) --* 
              The API identifier.
            - **ApiMappingId** *(string) --* 
              The API mapping identifier.
            - **ApiMappingKey** *(string) --* 
              The API mapping key.
            - **Stage** *(string) --* 
              The API stage.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type ApiMappingId: string
        :param ApiMappingId: **[REQUIRED]**
          The API mapping identifier.
        :type ApiMappingKey: string
        :param ApiMappingKey:
          The API mapping key.
        :type DomainName: string
        :param DomainName: **[REQUIRED]**
          The domain name.
        :type Stage: string
        :param Stage:
          The API stage.
        :rtype: dict
        :returns:
        """
        pass

    def update_authorizer(self, ApiId: str, AuthorizerId: str, AuthorizerCredentialsArn: str = None, AuthorizerResultTtlInSeconds: int = None, AuthorizerType: str = None, AuthorizerUri: str = None, IdentitySource: List = None, IdentityValidationExpression: str = None, Name: str = None, ProviderArns: List = None) -> Dict:
        """
        Updates an Authorizer.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/UpdateAuthorizer>`_
        
        **Request Syntax**
        ::
          response = client.update_authorizer(
              ApiId='string',
              AuthorizerCredentialsArn='string',
              AuthorizerId='string',
              AuthorizerResultTtlInSeconds=123,
              AuthorizerType='REQUEST',
              AuthorizerUri='string',
              IdentitySource=[
                  'string',
              ],
              IdentityValidationExpression='string',
              Name='string',
              ProviderArns=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'AuthorizerCredentialsArn': 'string',
                'AuthorizerId': 'string',
                'AuthorizerResultTtlInSeconds': 123,
                'AuthorizerType': 'REQUEST',
                'AuthorizerUri': 'string',
                'IdentitySource': [
                    'string',
                ],
                'IdentityValidationExpression': 'string',
                'Name': 'string',
                'ProviderArns': [
                    'string',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **AuthorizerCredentialsArn** *(string) --* 
              Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.
            - **AuthorizerId** *(string) --* 
              The authorizer identifier.
            - **AuthorizerResultTtlInSeconds** *(integer) --* 
              The time to live (TTL), in seconds, of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, the default value is 300. The maximum value is 3600, or 1 hour.
            - **AuthorizerType** *(string) --* 
              The authorizer type. Currently the only valid value is REQUEST, for a Lambda function using incoming request parameters.
            - **AuthorizerUri** *(string) --* 
              The authorizer's Uniform Resource Identifier (URI). ForREQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations. In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api} , where {region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial /. For Lambda functions, this is usually of the form /2015-03-31/functions/[FunctionARN]/invocations.
            - **IdentitySource** *(list) --* 
              The identity source for which authorization is requested.
              For the REQUEST authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an Auth header and a Name query string parameters are defined as identity sources, this value is method.request.header.Auth, method.request.querystring.Name. These parameters will be used to derive the authorization caching key and to perform runtime validation of the REQUEST authorizer by verifying all of the identity-related request parameters are present, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.
              - *(string) --* 
            - **IdentityValidationExpression** *(string) --* 
              The validation expression does not apply to the REQUEST authorizer.
            - **Name** *(string) --* 
              The name of the authorizer.
            - **ProviderArns** *(list) --* 
              For REQUEST authorizer, this is not defined.
              - *(string) --* 
                Represents an Amazon Resource Name (ARN).
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type AuthorizerCredentialsArn: string
        :param AuthorizerCredentialsArn:
          Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role\'s Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.
        :type AuthorizerId: string
        :param AuthorizerId: **[REQUIRED]**
          The authorizer identifier.
        :type AuthorizerResultTtlInSeconds: integer
        :param AuthorizerResultTtlInSeconds:
          The time to live (TTL), in seconds, of cached authorizer results. If it is zero, authorization caching is disabled. If it is greater than zero, API Gateway will cache authorizer responses. If this field is not set, the default value is 300. The maximum value is 3600, or 1 hour.
        :type AuthorizerType: string
        :param AuthorizerType:
          The authorizer type. Currently the only valid value is REQUEST, for a Lambda function using incoming request parameters.
        :type AuthorizerUri: string
        :param AuthorizerUri:
          The authorizer\'s Uniform Resource Identifier (URI). For REQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations. In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api} , where {region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial /. For Lambda functions, this is usually of the form /2015-03-31/functions/[FunctionARN]/invocations.
        :type IdentitySource: list
        :param IdentitySource:
          The identity source for which authorization is requested.
          For the REQUEST authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an Auth header, a Name query string parameter are defined as identity sources, this value is $method.request.header.Auth, $method.request.querystring.Name. These parameters will be used to derive the authorization caching key and to perform runtime validation of the REQUEST authorizer by verifying all of the identity-related request parameters are present, not null and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.
          - *(string) --*
        :type IdentityValidationExpression: string
        :param IdentityValidationExpression:
          The validation expression does not apply to the REQUEST authorizer.
        :type Name: string
        :param Name:
          The name of the authorizer.
        :type ProviderArns: list
        :param ProviderArns:
          For REQUEST authorizer, this is not defined.
          - *(string) --*
            Represents an Amazon Resource Name (ARN).
        :rtype: dict
        :returns:
        """
        pass

    def update_deployment(self, ApiId: str, DeploymentId: str, Description: str = None) -> Dict:
        """
        Updates a Deployment.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/UpdateDeployment>`_
        
        **Request Syntax**
        ::
          response = client.update_deployment(
              ApiId='string',
              DeploymentId='string',
              Description='string'
          )
        
        **Response Syntax**
        ::
            {
                'CreatedDate': datetime(2015, 1, 1),
                'DeploymentId': 'string',
                'DeploymentStatus': 'PENDING'|'FAILED'|'DEPLOYED',
                'DeploymentStatusMessage': 'string',
                'Description': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **CreatedDate** *(datetime) --* 
              The date and time when the Deployment resource was created.
            - **DeploymentId** *(string) --* 
              The identifier for the deployment.
            - **DeploymentStatus** *(string) --* 
              The status of the deployment: PENDING, FAILED, or SUCCEEDED.
            - **DeploymentStatusMessage** *(string) --* 
              May contain additional feedback on the status of an API deployment.
            - **Description** *(string) --* 
              The description for the deployment.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type DeploymentId: string
        :param DeploymentId: **[REQUIRED]**
          The deployment ID.
        :type Description: string
        :param Description:
          The description for the deployment resource.
        :rtype: dict
        :returns:
        """
        pass

    def update_domain_name(self, DomainName: str, DomainNameConfigurations: List = None) -> Dict:
        """
        Updates a domain name.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/UpdateDomainName>`_
        
        **Request Syntax**
        ::
          response = client.update_domain_name(
              DomainName='string',
              DomainNameConfigurations=[
                  {
                      'ApiGatewayDomainName': 'string',
                      'CertificateArn': 'string',
                      'CertificateName': 'string',
                      'CertificateUploadDate': datetime(2015, 1, 1),
                      'EndpointType': 'REGIONAL'|'EDGE',
                      'HostedZoneId': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'ApiMappingSelectionExpression': 'string',
                'DomainName': 'string',
                'DomainNameConfigurations': [
                    {
                        'ApiGatewayDomainName': 'string',
                        'CertificateArn': 'string',
                        'CertificateName': 'string',
                        'CertificateUploadDate': datetime(2015, 1, 1),
                        'EndpointType': 'REGIONAL'|'EDGE',
                        'HostedZoneId': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **ApiMappingSelectionExpression** *(string) --* 
              The API mapping selection expression.
            - **DomainName** *(string) --* 
              The name of the DomainName resource.
            - **DomainNameConfigurations** *(list) --* 
              The domain name configurations.
              - *(dict) --* 
                The domain name configuration.
                - **ApiGatewayDomainName** *(string) --* 
                  A domain name for the WebSocket API.
                - **CertificateArn** *(string) --* 
                  An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.
                - **CertificateName** *(string) --* 
                  The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.
                - **CertificateUploadDate** *(datetime) --* 
                  The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.
                - **EndpointType** *(string) --* 
                  The endpoint type.
                - **HostedZoneId** *(string) --* 
                  The Amazon Route 53 Hosted Zone ID of the endpoint. See `AWS Regions and Endpoints for API Gateway <docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ .
        :type DomainName: string
        :param DomainName: **[REQUIRED]**
          The domain name.
        :type DomainNameConfigurations: list
        :param DomainNameConfigurations:
          The domain name configurations.
          - *(dict) --*
            The domain name configuration.
            - **ApiGatewayDomainName** *(string) --*
              A domain name for the WebSocket API.
            - **CertificateArn** *(string) --*
              An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.
            - **CertificateName** *(string) --*
              The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.
            - **CertificateUploadDate** *(datetime) --*
              The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.
            - **EndpointType** *(string) --*
              The endpoint type.
            - **HostedZoneId** *(string) --*
              The Amazon Route 53 Hosted Zone ID of the endpoint. See `AWS Regions and Endpoints for API Gateway <docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ .
        :rtype: dict
        :returns:
        """
        pass

    def update_integration(self, ApiId: str, IntegrationId: str, ConnectionId: str = None, ConnectionType: str = None, ContentHandlingStrategy: str = None, CredentialsArn: str = None, Description: str = None, IntegrationMethod: str = None, IntegrationType: str = None, IntegrationUri: str = None, PassthroughBehavior: str = None, RequestParameters: Dict = None, RequestTemplates: Dict = None, TemplateSelectionExpression: str = None, TimeoutInMillis: int = None) -> Dict:
        """
        Updates an Integration.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/UpdateIntegration>`_
        
        **Request Syntax**
        ::
          response = client.update_integration(
              ApiId='string',
              ConnectionId='string',
              ConnectionType='INTERNET'|'VPC_LINK',
              ContentHandlingStrategy='CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
              CredentialsArn='string',
              Description='string',
              IntegrationId='string',
              IntegrationMethod='string',
              IntegrationType='AWS'|'HTTP'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
              IntegrationUri='string',
              PassthroughBehavior='WHEN_NO_MATCH'|'NEVER'|'WHEN_NO_TEMPLATES',
              RequestParameters={
                  'string': 'string'
              },
              RequestTemplates={
                  'string': 'string'
              },
              TemplateSelectionExpression='string',
              TimeoutInMillis=123
          )
        
        **Response Syntax**
        ::
            {
                'ConnectionId': 'string',
                'ConnectionType': 'INTERNET'|'VPC_LINK',
                'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                'CredentialsArn': 'string',
                'Description': 'string',
                'IntegrationId': 'string',
                'IntegrationMethod': 'string',
                'IntegrationResponseSelectionExpression': 'string',
                'IntegrationType': 'AWS'|'HTTP'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                'IntegrationUri': 'string',
                'PassthroughBehavior': 'WHEN_NO_MATCH'|'NEVER'|'WHEN_NO_TEMPLATES',
                'RequestParameters': {
                    'string': 'string'
                },
                'RequestTemplates': {
                    'string': 'string'
                },
                'TemplateSelectionExpression': 'string',
                'TimeoutInMillis': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **ConnectionId** *(string) --* 
              The identifier of the VpcLink used for the integration when the connectionType is VPC_LINK; otherwise undefined.
            - **ConnectionType** *(string) --* 
              The type of the network connection to the integration endpoint. The valid value is INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and a network load balancer in a VPC. The default value is INTERNET.
            - **ContentHandlingStrategy** *(string) --* 
              Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
              CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
              CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
              If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
            - **CredentialsArn** *(string) --* 
              Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, specify null.
            - **Description** *(string) --* 
              Represents the description of an integration.
            - **IntegrationId** *(string) --* 
              Represents the identifier of an integration.
            - **IntegrationMethod** *(string) --* 
              Specifies the integration's HTTP method type.
            - **IntegrationResponseSelectionExpression** *(string) --* 
            - **IntegrationType** *(string) --* 
              The integration type of an integration. One of the following:
              AWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
              AWS_PROXY: for integrating the route or method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as Lambda proxy integration.
              HTTP: for integrating the route or method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
              HTTP_PROXY: for integrating route or method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as HTTP proxy integration.
              MOCK: for integrating the route or method request with API Gateway as a "loopback" endpoint without invoking any backend.
            - **IntegrationUri** *(string) --* 
              Specifies the Uniform Resource Identifier (URI) of the integration endpoint.
              For HTTP or HTTP_PROXY integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the `RFC-3986 specification <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard integration, where connectionType is not VPC_LINK, or private integration, where connectionType is VPC_LINK. For a private HTTP integration, the URI is not used for routing.
              For AWS or AWS_PROXY integrations, the URI is of the form arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}. Here, {Region} is the API Gateway region (e.g., us-east-1); {service} is the name of the integrated AWS service (e.g., s3); and {subdomain} is a designated subdomain supported by certain AWS service for fast host-name lookup. action can be used for an AWS service action-based API, using an Action={name}&{p1}={v1}&p2={v2}... query string. The ensuing {service_api} refers to a supported action {name} plus any required input parameters. Alternatively, path can be used for an AWS service path-based API. The ensuing service_api refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of GetObject, the URI can be either arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key} or arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}
            - **PassthroughBehavior** *(string) --* 
              Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER.
              WHEN_NO_MATCH passes the request body for unmapped content types through to the integration backend without transformation.
              NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.
              WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same HTTP 415 Unsupported Media Type response.
            - **RequestParameters** *(dict) --* 
              A key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.{location}.{name} , where {location} is querystring, path, or header; and {name} must be a valid and unique method request parameter name.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [1-512].
            - **RequestTemplates** *(dict) --* 
              Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [0-32768].
            - **TemplateSelectionExpression** *(string) --* 
              The template selection expression for the integration.
            - **TimeoutInMillis** *(integer) --* 
              Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type ConnectionId: string
        :param ConnectionId:
          The identifier of the VpcLink used for the integration when the connectionType is VPC_LINK; otherwise undefined.
        :type ConnectionType: string
        :param ConnectionType:
          The type of the network connection to the integration endpoint. The valid value is INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and a network load balancer in a VPC. The default value is INTERNET.
        :type ContentHandlingStrategy: string
        :param ContentHandlingStrategy:
          Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
          CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
          CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
          If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
        :type CredentialsArn: string
        :param CredentialsArn:
          Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role\'s Amazon Resource Name (ARN). To require that the caller\'s identity be passed through from the request, specify the string arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, specify null.
        :type Description: string
        :param Description:
          The description of the integration
        :type IntegrationId: string
        :param IntegrationId: **[REQUIRED]**
          The integration ID.
        :type IntegrationMethod: string
        :param IntegrationMethod:
          Specifies the integration\'s HTTP method type.
        :type IntegrationType: string
        :param IntegrationType:
          The integration type of an integration. One of the following:
          AWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
          AWS_PROXY: for integrating the route or method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as Lambda proxy integration.
          HTTP: for integrating the route or method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
          HTTP_PROXY: for integrating route or method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as HTTP proxy integration.
          MOCK: for integrating the route or method request with API Gateway as a \"loopback\" endpoint without invoking any backend.
        :type IntegrationUri: string
        :param IntegrationUri:
          Specifies the Uniform Resource Identifier (URI) of the integration endpoint.
          For HTTP or HTTP_PROXY integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the `RFC-3986 specification <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for either standard integration, where connectionType is not VPC_LINK, or private integration, where connectionType is VPC_LINK. For a private HTTP integration, the URI is not used for routing.
          For AWS or AWS_PROXY integrations, the URI is of the form arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}. Here, {Region} is the API Gateway region (e.g., us-east-1); {service} is the name of the integrated AWS service (e.g., s3); and {subdomain} is a designated subdomain supported by certain AWS service for fast host-name lookup. action can be used for an AWS service action-based API, using an Action={name}&{p1}={v1}&p2={v2}... query string. The ensuing {service_api} refers to a supported action {name} plus any required input parameters. Alternatively, path can be used for an AWS service path-based API. The ensuing service_api refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of GetObject, the URI can be either arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key} or arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}
        :type PassthroughBehavior: string
        :param PassthroughBehavior:
          Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER.
          WHEN_NO_MATCH passes the request body for unmapped content types through to the integration backend without transformation.
          NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.
          WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same HTTP 415 Unsupported Media Type response.
        :type RequestParameters: dict
        :param RequestParameters:
          A key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.{location}.{name} , where {location} is querystring, path, or header; and {name} must be a valid and unique method request parameter name.
          - *(string) --*
            - *(string) --*
              A string with a length between [1-512].
        :type RequestTemplates: dict
        :param RequestTemplates:
          Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.
          - *(string) --*
            - *(string) --*
              A string with a length between [0-32768].
        :type TemplateSelectionExpression: string
        :param TemplateSelectionExpression:
          The template selection expression for the integration.
        :type TimeoutInMillis: integer
        :param TimeoutInMillis:
          Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.
        :rtype: dict
        :returns:
        """
        pass

    def update_integration_response(self, ApiId: str, IntegrationId: str, IntegrationResponseId: str, ContentHandlingStrategy: str = None, IntegrationResponseKey: str = None, ResponseParameters: Dict = None, ResponseTemplates: Dict = None, TemplateSelectionExpression: str = None) -> Dict:
        """
        Updates an IntegrationResponses.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/UpdateIntegrationResponse>`_
        
        **Request Syntax**
        ::
          response = client.update_integration_response(
              ApiId='string',
              ContentHandlingStrategy='CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
              IntegrationId='string',
              IntegrationResponseId='string',
              IntegrationResponseKey='string',
              ResponseParameters={
                  'string': 'string'
              },
              ResponseTemplates={
                  'string': 'string'
              },
              TemplateSelectionExpression='string'
          )
        
        **Response Syntax**
        ::
            {
                'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                'IntegrationResponseId': 'string',
                'IntegrationResponseKey': 'string',
                'ResponseParameters': {
                    'string': 'string'
                },
                'ResponseTemplates': {
                    'string': 'string'
                },
                'TemplateSelectionExpression': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **ContentHandlingStrategy** *(string) --* 
              Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
              CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
              CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
              If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
            - **IntegrationResponseId** *(string) --* 
              The integration response ID.
            - **IntegrationResponseKey** *(string) --* 
              The integration response key.
            - **ResponseParameters** *(dict) --* 
              A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name}, where name is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name} or integration.response.body.{JSON-expression}, where name is a valid and unique response header name and JSON-expression is a valid JSON expression without the $ prefix.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [1-512].
            - **ResponseTemplates** *(dict) --* 
              The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [0-32768].
            - **TemplateSelectionExpression** *(string) --* 
              The template selection expressions for the integration response.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type ContentHandlingStrategy: string
        :param ContentHandlingStrategy:
          Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
          CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
          CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
          If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
        :type IntegrationId: string
        :param IntegrationId: **[REQUIRED]**
          The integration ID.
        :type IntegrationResponseId: string
        :param IntegrationResponseId: **[REQUIRED]**
          The integration response ID.
        :type IntegrationResponseKey: string
        :param IntegrationResponseKey:
          The integration response key.
        :type ResponseParameters: dict
        :param ResponseParameters:
          A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name} , where name is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name} or integration.response.body.{JSON-expression} , where {name} is a valid and unique response header name and {JSON-expression} is a valid JSON expression without the $ prefix.
          - *(string) --*
            - *(string) --*
              A string with a length between [1-512].
        :type ResponseTemplates: dict
        :param ResponseTemplates:
          The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.
          - *(string) --*
            - *(string) --*
              A string with a length between [0-32768].
        :type TemplateSelectionExpression: string
        :param TemplateSelectionExpression:
          The template selection expression for the integration response.
        :rtype: dict
        :returns:
        """
        pass

    def update_model(self, ApiId: str, ModelId: str, ContentType: str = None, Description: str = None, Name: str = None, Schema: str = None) -> Dict:
        """
        Updates a Model.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/UpdateModel>`_
        
        **Request Syntax**
        ::
          response = client.update_model(
              ApiId='string',
              ContentType='string',
              Description='string',
              ModelId='string',
              Name='string',
              Schema='string'
          )
        
        **Response Syntax**
        ::
            {
                'ContentType': 'string',
                'Description': 'string',
                'ModelId': 'string',
                'Name': 'string',
                'Schema': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **ContentType** *(string) --* 
              The content-type for the model, for example, "application/json".
            - **Description** *(string) --* 
              The description of the model.
            - **ModelId** *(string) --* 
              The model identifier.
            - **Name** *(string) --* 
              The name of the model. Must be alphanumeric.
            - **Schema** *(string) --* 
              The schema for the model. For application/json models, this should be JSON schema draft 4 model.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type ContentType: string
        :param ContentType:
          The content-type for the model, for example, \"application/json\".
        :type Description: string
        :param Description:
          The description of the model.
        :type ModelId: string
        :param ModelId: **[REQUIRED]**
          The model ID.
        :type Name: string
        :param Name:
          The name of the model.
        :type Schema: string
        :param Schema:
          The schema for the model. For application/json models, this should be JSON schema draft 4 model.
        :rtype: dict
        :returns:
        """
        pass

    def update_route(self, ApiId: str, RouteId: str, ApiKeyRequired: bool = None, AuthorizationScopes: List = None, AuthorizationType: str = None, AuthorizerId: str = None, ModelSelectionExpression: str = None, OperationName: str = None, RequestModels: Dict = None, RequestParameters: Dict = None, RouteKey: str = None, RouteResponseSelectionExpression: str = None, Target: str = None) -> Dict:
        """
        Updates a Route.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/UpdateRoute>`_
        
        **Request Syntax**
        ::
          response = client.update_route(
              ApiId='string',
              ApiKeyRequired=True|False,
              AuthorizationScopes=[
                  'string',
              ],
              AuthorizationType='NONE'|'AWS_IAM'|'CUSTOM',
              AuthorizerId='string',
              ModelSelectionExpression='string',
              OperationName='string',
              RequestModels={
                  'string': 'string'
              },
              RequestParameters={
                  'string': {
                      'Required': True|False
                  }
              },
              RouteId='string',
              RouteKey='string',
              RouteResponseSelectionExpression='string',
              Target='string'
          )
        
        **Response Syntax**
        ::
            {
                'ApiKeyRequired': True|False,
                'AuthorizationScopes': [
                    'string',
                ],
                'AuthorizationType': 'NONE'|'AWS_IAM'|'CUSTOM',
                'AuthorizerId': 'string',
                'ModelSelectionExpression': 'string',
                'OperationName': 'string',
                'RequestModels': {
                    'string': 'string'
                },
                'RequestParameters': {
                    'string': {
                        'Required': True|False
                    }
                },
                'RouteId': 'string',
                'RouteKey': 'string',
                'RouteResponseSelectionExpression': 'string',
                'Target': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **ApiKeyRequired** *(boolean) --* 
              Specifies whether an API key is required for this route.
            - **AuthorizationScopes** *(list) --* 
              The authorization scopes supported by this route. 
              - *(string) --* 
                A string with a length between [1-64].
            - **AuthorizationType** *(string) --* 
              The authorization type for the route. Valid values are NONE for open access, AWS_IAM for using AWS IAM permissions.
            - **AuthorizerId** *(string) --* 
              The identifier of the Authorizer resource to be associated with this route.
            - **ModelSelectionExpression** *(string) --* 
              The model selection expression for the route.
            - **OperationName** *(string) --* 
              The operation name for the route.
            - **RequestModels** *(dict) --* 
              The request models for the route.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [1-128].
            - **RequestParameters** *(dict) --* 
              The request parameters for the route.
              - *(string) --* 
                - *(dict) --* 
                  Validation constraints imposed on parameters of a request (path, query string, headers).
                  - **Required** *(boolean) --* 
                    Whether or not the parameter is required.
            - **RouteId** *(string) --* 
              The route ID.
            - **RouteKey** *(string) --* 
              The route key for the route.
            - **RouteResponseSelectionExpression** *(string) --* 
              The route response selection expression for the route.
            - **Target** *(string) --* 
              The target for the route.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type ApiKeyRequired: boolean
        :param ApiKeyRequired:
          Specifies whether an API key is required for the route.
        :type AuthorizationScopes: list
        :param AuthorizationScopes:
          The authorization scopes supported by this route.
          - *(string) --*
            A string with a length between [1-64].
        :type AuthorizationType: string
        :param AuthorizationType:
          The authorization type for the route. Valid values are NONE for open access, AWS_IAM for using AWS IAM permissions.
        :type AuthorizerId: string
        :param AuthorizerId:
          The identifier of the Authorizer resource to be associated with this route.
        :type ModelSelectionExpression: string
        :param ModelSelectionExpression:
          The model selection expression for the route.
        :type OperationName: string
        :param OperationName:
          The operation name for the route.
        :type RequestModels: dict
        :param RequestModels:
          The request models for the route.
          - *(string) --*
            - *(string) --*
              A string with a length between [1-128].
        :type RequestParameters: dict
        :param RequestParameters:
          The request parameters for the route.
          - *(string) --*
            - *(dict) --*
              Validation constraints imposed on parameters of a request (path, query string, headers).
              - **Required** *(boolean) --*
                Whether or not the parameter is required.
        :type RouteId: string
        :param RouteId: **[REQUIRED]**
          The route ID.
        :type RouteKey: string
        :param RouteKey:
          The route key for the route.
        :type RouteResponseSelectionExpression: string
        :param RouteResponseSelectionExpression:
          The route response selection expression for the route.
        :type Target: string
        :param Target:
          The target for the route.
        :rtype: dict
        :returns:
        """
        pass

    def update_route_response(self, ApiId: str, RouteId: str, RouteResponseId: str, ModelSelectionExpression: str = None, ResponseModels: Dict = None, ResponseParameters: Dict = None, RouteResponseKey: str = None) -> Dict:
        """
        Updates a RouteResponse.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/UpdateRouteResponse>`_
        
        **Request Syntax**
        ::
          response = client.update_route_response(
              ApiId='string',
              ModelSelectionExpression='string',
              ResponseModels={
                  'string': 'string'
              },
              ResponseParameters={
                  'string': {
                      'Required': True|False
                  }
              },
              RouteId='string',
              RouteResponseId='string',
              RouteResponseKey='string'
          )
        
        **Response Syntax**
        ::
            {
                'ModelSelectionExpression': 'string',
                'ResponseModels': {
                    'string': 'string'
                },
                'ResponseParameters': {
                    'string': {
                        'Required': True|False
                    }
                },
                'RouteResponseId': 'string',
                'RouteResponseKey': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **ModelSelectionExpression** *(string) --* 
              Represents the model selection expression of a route response.
            - **ResponseModels** *(dict) --* 
              Represents the response models of a route response.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [1-128].
            - **ResponseParameters** *(dict) --* 
              Represents the response parameters of a route response.
              - *(string) --* 
                - *(dict) --* 
                  Validation constraints imposed on parameters of a request (path, query string, headers).
                  - **Required** *(boolean) --* 
                    Whether or not the parameter is required.
            - **RouteResponseId** *(string) --* 
              Represents the identifier of a route response.
            - **RouteResponseKey** *(string) --* 
              Represents the route response key of a route response.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type ModelSelectionExpression: string
        :param ModelSelectionExpression:
          The model selection expression for the route response.
        :type ResponseModels: dict
        :param ResponseModels:
          The response models for the route response.
          - *(string) --*
            - *(string) --*
              A string with a length between [1-128].
        :type ResponseParameters: dict
        :param ResponseParameters:
          The route response parameters.
          - *(string) --*
            - *(dict) --*
              Validation constraints imposed on parameters of a request (path, query string, headers).
              - **Required** *(boolean) --*
                Whether or not the parameter is required.
        :type RouteId: string
        :param RouteId: **[REQUIRED]**
          The route ID.
        :type RouteResponseId: string
        :param RouteResponseId: **[REQUIRED]**
          The route response ID.
        :type RouteResponseKey: string
        :param RouteResponseKey:
          The route response key.
        :rtype: dict
        :returns:
        """
        pass

    def update_stage(self, ApiId: str, StageName: str, AccessLogSettings: Dict = None, ClientCertificateId: str = None, DefaultRouteSettings: Dict = None, DeploymentId: str = None, Description: str = None, RouteSettings: Dict = None, StageVariables: Dict = None) -> Dict:
        """
        Updates a Stage.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/UpdateStage>`_
        
        **Request Syntax**
        ::
          response = client.update_stage(
              AccessLogSettings={
                  'DestinationArn': 'string',
                  'Format': 'string'
              },
              ApiId='string',
              ClientCertificateId='string',
              DefaultRouteSettings={
                  'DataTraceEnabled': True|False,
                  'DetailedMetricsEnabled': True|False,
                  'LoggingLevel': 'ERROR'|'INFO'|'false',
                  'ThrottlingBurstLimit': 123,
                  'ThrottlingRateLimit': 123.0
              },
              DeploymentId='string',
              Description='string',
              RouteSettings={
                  'string': {
                      'DataTraceEnabled': True|False,
                      'DetailedMetricsEnabled': True|False,
                      'LoggingLevel': 'ERROR'|'INFO'|'false',
                      'ThrottlingBurstLimit': 123,
                      'ThrottlingRateLimit': 123.0
                  }
              },
              StageName='string',
              StageVariables={
                  'string': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'AccessLogSettings': {
                    'DestinationArn': 'string',
                    'Format': 'string'
                },
                'ClientCertificateId': 'string',
                'CreatedDate': datetime(2015, 1, 1),
                'DefaultRouteSettings': {
                    'DataTraceEnabled': True|False,
                    'DetailedMetricsEnabled': True|False,
                    'LoggingLevel': 'ERROR'|'INFO'|'false',
                    'ThrottlingBurstLimit': 123,
                    'ThrottlingRateLimit': 123.0
                },
                'DeploymentId': 'string',
                'Description': 'string',
                'LastUpdatedDate': datetime(2015, 1, 1),
                'RouteSettings': {
                    'string': {
                        'DataTraceEnabled': True|False,
                        'DetailedMetricsEnabled': True|False,
                        'LoggingLevel': 'ERROR'|'INFO'|'false',
                        'ThrottlingBurstLimit': 123,
                        'ThrottlingRateLimit': 123.0
                    }
                },
                'StageName': 'string',
                'StageVariables': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Success
            - **AccessLogSettings** *(dict) --* 
              Settings for logging access in this stage.
              - **DestinationArn** *(string) --* 
                The ARN of the CloudWatch Logs log group to receive access logs.
              - **Format** *(string) --* 
                A single line format of the access logs of data, as specified by selected $context variables. The format must include at least $context.requestId.
            - **ClientCertificateId** *(string) --* 
              The identifier of a client certificate for a Stage.
            - **CreatedDate** *(datetime) --* 
              The timestamp when the stage was created.
            - **DefaultRouteSettings** *(dict) --* 
              Default route settings for the stage.
              - **DataTraceEnabled** *(boolean) --* 
                Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs.
              - **DetailedMetricsEnabled** *(boolean) --* 
                Specifies whether detailed metrics are enabled.
              - **LoggingLevel** *(string) --* 
                Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the log entries pushed to Amazon CloudWatch Logs.
              - **ThrottlingBurstLimit** *(integer) --* 
                Specifies the throttling burst limit.
              - **ThrottlingRateLimit** *(float) --* 
                Specifies the throttling rate limit.
            - **DeploymentId** *(string) --* 
              The identifier of the Deployment that the Stage is associated with.
            - **Description** *(string) --* 
              The description of the stage.
            - **LastUpdatedDate** *(datetime) --* 
              The timestamp when the stage was last updated.
            - **RouteSettings** *(dict) --* 
              Route settings for the stage.
              - *(string) --* 
                - *(dict) --* 
                  Represents a collection of route settings.
                  - **DataTraceEnabled** *(boolean) --* 
                    Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs.
                  - **DetailedMetricsEnabled** *(boolean) --* 
                    Specifies whether detailed metrics are enabled.
                  - **LoggingLevel** *(string) --* 
                    Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the log entries pushed to Amazon CloudWatch Logs.
                  - **ThrottlingBurstLimit** *(integer) --* 
                    Specifies the throttling burst limit.
                  - **ThrottlingRateLimit** *(float) --* 
                    Specifies the throttling rate limit.
            - **StageName** *(string) --* 
              The name of the stage.
            - **StageVariables** *(dict) --* 
              A map that defines the stage variables for a stage resource. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.
              - *(string) --* 
                - *(string) --* 
                  A string with a length between [0-2048].
        :type AccessLogSettings: dict
        :param AccessLogSettings:
          Settings for logging access in this stage.
          - **DestinationArn** *(string) --*
            The ARN of the CloudWatch Logs log group to receive access logs.
          - **Format** *(string) --*
            A single line format of the access logs of data, as specified by selected $context variables. The format must include at least $context.requestId.
        :type ApiId: string
        :param ApiId: **[REQUIRED]**
          The API identifier.
        :type ClientCertificateId: string
        :param ClientCertificateId:
          The identifier of a client certificate for a Stage.
        :type DefaultRouteSettings: dict
        :param DefaultRouteSettings:
          The default route settings for the stage.
          - **DataTraceEnabled** *(boolean) --*
            Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs.
          - **DetailedMetricsEnabled** *(boolean) --*
            Specifies whether detailed metrics are enabled.
          - **LoggingLevel** *(string) --*
            Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the log entries pushed to Amazon CloudWatch Logs.
          - **ThrottlingBurstLimit** *(integer) --*
            Specifies the throttling burst limit.
          - **ThrottlingRateLimit** *(float) --*
            Specifies the throttling rate limit.
        :type DeploymentId: string
        :param DeploymentId:
          The deployment identifier for the API stage.
        :type Description: string
        :param Description:
          The description for the API stage.
        :type RouteSettings: dict
        :param RouteSettings:
          Route settings for the stage.
          - *(string) --*
            - *(dict) --*
              Represents a collection of route settings.
              - **DataTraceEnabled** *(boolean) --*
                Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs.
              - **DetailedMetricsEnabled** *(boolean) --*
                Specifies whether detailed metrics are enabled.
              - **LoggingLevel** *(string) --*
                Specifies the logging level for this route: DEBUG, INFO, or WARN. This property affects the log entries pushed to Amazon CloudWatch Logs.
              - **ThrottlingBurstLimit** *(integer) --*
                Specifies the throttling burst limit.
              - **ThrottlingRateLimit** *(float) --*
                Specifies the throttling rate limit.
        :type StageName: string
        :param StageName: **[REQUIRED]**
          The stage name.
        :type StageVariables: dict
        :param StageVariables:
          A map that defines the stage variables for a Stage. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.
          - *(string) --*
            - *(string) --*
              A string with a length between [0-2048].
        :rtype: dict
        :returns:
        """
        pass
